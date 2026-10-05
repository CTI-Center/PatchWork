#!/usr/bin/env python3
"""Mirror the Google Threat Intelligence documentation hub as local markdown.

gtidocs.virustotal.com is a readme.io hub. Two upstream affordances make a faithful
mirror possible:

  * appending ``.md`` to any page URL returns that page's markdown source, and
  * every rendered HTML page embeds the complete left-nav tree as a ``"sidebar":[...]``
    JSON blob, giving group titles, page titles, slugs, ordering and nesting.

This script walks that tree, fetches each page, rewrites it to the repository's
authoring conventions (see ../../README.md), and writes a browsable directory tree with
breadcrumbs, group indexes and prev/next footers.

Output is deterministic: the same upstream produces byte-identical files, so refreshing
the archive is a `git diff` against the previous snapshot.

Usage
-----
    python3 tools/gtidocs-mirror/mirror.py                     # refresh everything
    python3 tools/gtidocs-mirror/mirror.py --section guides    # guides|reference|changelog
    python3 tools/gtidocs-mirror/mirror.py --no-images
    python3 tools/gtidocs-mirror/mirror.py --dry-run
    python3 tools/gtidocs-mirror/mirror.py --use-cache         # reuse previously fetched pages

MIT licensed, in line with the repository's tooling licence.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as _dt
import gzip
import hashlib
import json
import os
import re

import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

# --------------------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------------------

PRIMARY_HOST = "https://gtidocs.virustotal.com"
FALLBACK_HOST = "https://gtidocs.readme.io"
LLMS_TXT = f"{FALLBACK_HOST}/llms.txt"

# Sections, in the order they are written. ``url_path`` is the upstream path segment;
# ``probe`` is a page whose HTML carries that section's sidebar tree.
SECTIONS = {
    "guides": {
        "url_path": "docs",
        "probe": f"{PRIMARY_HOST}/docs/report-types",
        "title": "Guides",
    },
    "reference": {
        "url_path": "reference",
        "probe": f"{PRIMARY_HOST}/reference/api-overview",
        "title": "API Reference",
    },
    "changelog": {
        "url_path": "changelog",
        "probe": None,  # no sidebar; discovered from llms.txt
        "title": "Changelog",
    },
}

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) patchwork-gtidocs-mirror/1.0 "
    "(+https://github.com/CTI-Center/PatchWork)"
)

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT_ROOT = os.path.join(REPO_ROOT, "docs", "Easy-access", "GTI", "gtidocs")
CACHE_ROOT = os.path.join(HERE, ".cache")
IMG_DIRNAME = "img"

MAX_WORKERS = 3
REQUEST_DELAY = 0.4           # seconds, per worker, between requests
RETRY_BACKOFF = (2.0, 6.0, 15.0, 30.0)
SOCKET_TIMEOUT = 30
CHALLENGE_COOLDOWN = 20       # seconds all workers pause after a bot challenge

# The line readme.io prepends to every markdown response.
BOILERPLATE_RE = re.compile(
    r"^Fetch the complete documentation index at:.*?\n", re.MULTILINE
)

_print_lock = threading.Lock()
_cooldown_lock = threading.Lock()
_cooldown_until = 0.0


def log(msg: str) -> None:
    with _print_lock:
        print(msg, flush=True)


def trip_cooldown(seconds: float = CHALLENGE_COOLDOWN) -> None:
    """Pause every worker after a bot challenge.

    Retrying the one page that was refused is not enough: the block is per-client, so
    the other workers are about to be refused too. Backing the whole crawl off for a
    moment is what actually clears it.
    """
    global _cooldown_until
    with _cooldown_lock:
        _cooldown_until = max(_cooldown_until, time.monotonic() + seconds)


def await_cooldown() -> None:
    while True:
        with _cooldown_lock:
            remaining = _cooldown_until - time.monotonic()
        if remaining <= 0:
            return
        time.sleep(min(remaining, 2.0))


# --------------------------------------------------------------------------------------
# Slug helpers
# --------------------------------------------------------------------------------------

def kebab_heading(text: str) -> str:
    """The repository's heading convention (see README.md, 'Headings-are-kebab-case').

    Lowercase the text; collapse each run of whitespace to a single hyphen; preserve
    everything else exactly -- dots, commas, question marks, em dashes, backticks.
    """
    return re.sub(r"\s+", "-", text.strip().lower())


def github_slug(text: str) -> str:
    """GitHub's anchor slug, used to match anchors as upstream wrote them."""
    s = text.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    # One hyphen per whitespace character, not per run -- "Analysis / Sandbox" loses the
    # slash and keeps both spaces, so the anchor GitHub and readme.io generate is
    # "analysis--sandbox".
    return re.sub(r"\s", "-", s)


def dir_slug(text: str) -> str:
    """Filesystem- and link-safe directory name for a nav group title."""
    s = text.strip().lower()
    s = re.sub(r"[^\w\s-]", " ", s, flags=re.UNICODE)
    s = re.sub(r"[\s_]+", "-", s)
    return re.sub(r"-{2,}", "-", s).strip("-") or "group"


def md_target(path: str) -> str:
    """Wrap a link target in angle brackets when it holds markdown-hostile characters."""
    return f"<{path}>" if re.search(r"[ ()]", path) else path


# --------------------------------------------------------------------------------------
# HTTP
# --------------------------------------------------------------------------------------

class FetchError(RuntimeError):
    pass


def _raw_get(url: str, timeout: int = SOCKET_TIMEOUT) -> tuple[bytes, str]:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "*/*",
            "Accept-Encoding": "gzip",
            "Accept-Language": "en",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = resp.read()
        if resp.headers.get("Content-Encoding") == "gzip":
            body = gzip.decompress(body)
        return body, (resp.headers.get("Content-Type") or "")


CHALLENGE_RE = re.compile(r"\A(?:<!doctype html\b|<html[\s>])", re.IGNORECASE)


def _looks_like_html(text: str) -> bool:
    """readme.io's bot challenge answers with HTTP 200 and an HTML body.

    Status codes are therefore not a success signal; the body has to be inspected. The
    test anchors at the start of the document -- a page whose *content* mentions HTML is
    common (readme.io's own `<HTMLBlock>` component, for one) and must not trip it.
    """
    return CHALLENGE_RE.match(text.lstrip()) is not None


def fetch_markdown(url_path: str, slug: str) -> str:
    """Fetch one page's markdown, retrying and falling back to the alternate host."""
    last = None
    for attempt, backoff in enumerate((0.0,) + RETRY_BACKOFF):
        if backoff:
            time.sleep(backoff)
        await_cooldown()
        host = PRIMARY_HOST if attempt % 2 == 0 else FALLBACK_HOST
        url = f"{host}/{url_path}/{urllib.parse.quote(slug)}.md"
        try:
            body, ctype = _raw_get(url)
        except urllib.error.HTTPError as exc:
            last = f"HTTP {exc.code}"
            if exc.code == 404:
                break
            continue
        except Exception as exc:  # network hiccup, timeout, TLS
            last = f"{type(exc).__name__}: {exc}"
            continue
        text = body.decode("utf-8", errors="replace")
        if "text/markdown" not in ctype:
            last = f"content-type {ctype!r}"
            continue
        if _looks_like_html(text):
            last = "bot challenge (HTML body with 200)"
            trip_cooldown()
            continue
        return text
    raise FetchError(f"{url_path}/{slug}: {last}")


def fetch_text(url: str) -> str:
    for attempt, backoff in enumerate((0.0,) + RETRY_BACKOFF):
        if backoff:
            time.sleep(backoff)
        try:
            body, _ = _raw_get(url)
        except Exception as exc:
            last = f"{type(exc).__name__}: {exc}"
            continue
        text = body.decode("utf-8", errors="replace")
        if _looks_like_html(text) and not url.endswith((".html", "/")):
            last = "bot challenge"
            continue
        return text
    raise FetchError(f"{url}: {last}")


def fetch_html(url: str) -> str:
    for attempt, backoff in enumerate((0.0,) + RETRY_BACKOFF):
        if backoff:
            time.sleep(backoff)
        try:
            body, _ = _raw_get(url)
        except Exception as exc:
            last = f"{type(exc).__name__}: {exc}"
            continue
        text = body.decode("utf-8", errors="replace")
        if '"sidebar":[' not in text:
            last = "no sidebar payload in response (bot challenge?)"
            continue
        return text
    raise FetchError(f"{url}: {last}")


# --------------------------------------------------------------------------------------
# Discovery: the sidebar tree
# --------------------------------------------------------------------------------------

def extract_json_after(text: str, key: str):
    """Return the JSON value following ``key`` in ``text``, by balanced-delimiter scan."""
    i = text.index(key)
    start = i + len(key)
    depth = 0
    in_str = False
    esc = False
    for j in range(start, len(text)):
        c = text[j]
        if in_str:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                in_str = False
            continue
        if c == '"':
            in_str = True
        elif c in "[{":
            depth += 1
        elif c in "]}":
            depth -= 1
            if depth == 0:
                return json.loads(text[start : j + 1])
    raise ValueError(f"unterminated JSON after {key!r}")


class Page:
    """One node of the mirrored navigation tree."""

    __slots__ = (
        "slug", "title", "kind", "link_url", "section", "group", "children",
        "rel_path", "raw", "body", "headings", "updated_at", "images",
    )

    def __init__(self, node: dict, section: str, group: str):
        self.slug = node["slug"]
        self.title = (node.get("title") or self.slug).strip()
        self.kind = node.get("type") or "basic"
        self.link_url = node.get("link_url")
        self.section = section
        self.group = group
        self.children: list["Page"] = [
            Page(c, section, group) for c in (node.get("pages") or [])
        ]
        self.rel_path = ""      # path under OUT_ROOT, set by assign_paths()
        self.raw = ""
        self.body = ""
        self.headings: dict[str, str] = {}   # github slug -> kebab anchor
        self.updated_at = node.get("updatedAt") or ""
        self.images: list[str] = []

    @property
    def is_link(self) -> bool:
        return self.kind == "link"

    def walk(self):
        yield self
        for c in self.children:
            yield from c.walk()


class Group:
    __slots__ = ("title", "dirname", "pages", "section")

    def __init__(self, title: str, index: int, section: str):
        self.title = title
        self.dirname = f"{index:02d}-{dir_slug(title)}"
        self.section = section
        self.pages: list[Page] = []

    def walk(self):
        for p in self.pages:
            yield from p.walk()


def discover_sidebar(section: str, use_cache: bool) -> list[Group]:
    cache = os.path.join(CACHE_ROOT, f"sidebar-{section}.json")
    data = None
    if use_cache and os.path.exists(cache):
        with open(cache, encoding="utf-8") as fh:
            data = json.load(fh)
    if data is None:
        html = fetch_html(SECTIONS[section]["probe"])
        data = extract_json_after(html, '"sidebar":')
        os.makedirs(CACHE_ROOT, exist_ok=True)
        with open(cache, "w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=1)
    groups = []
    for i, raw_group in enumerate(data, start=1):
        title = (raw_group.get("title") or f"Group {i}").strip()
        group = Group(title, i, section)
        for node in raw_group.get("pages") or []:
            group.pages.append(Page(node, section, title))
        if group.pages:
            groups.append(group)
    return groups


def discover_changelog(llms: str) -> list[Group]:
    """The changelog has no sidebar; llms.txt lists it newest-first."""
    group = Group("Changelog", 1, "changelog")
    in_section = False
    for line in llms.splitlines():
        if line.startswith("## "):
            in_section = line.strip() == "## Changelog"
            continue
        if not in_section:
            continue
        m = re.match(r"- \[(.+?)\]\((https?://[^)]+?)\)", line)
        if not m:
            continue
        title, url = m.group(1), m.group(2)
        slug = url.rsplit("/", 1)[-1]
        if slug.endswith(".md"):
            slug = slug[:-3]
        group.pages.append(
            Page({"slug": slug, "title": title, "type": "basic"}, "changelog", "Changelog")
        )
    return [group] if group.pages else []


def parse_llms_slugs(llms: str) -> dict[str, set[str]]:
    """Slugs listed in llms.txt, keyed by upstream path segment, for cross-checking."""
    out: dict[str, set[str]] = {}
    for m in re.finditer(r"https?://[^/]+/(docs|reference|changelog)/([^)\s]+?)\.md", llms):
        out.setdefault(m.group(1), set()).add(m.group(2))
    return out


def assign_paths(groups: list[Group], section: str) -> None:
    """Mirror the nav shape on disk.

    A page with children keeps its own ``<slug>.md`` and gains a sibling ``<slug>/``
    directory holding them -- a form both Obsidian and GitHub resolve.
    """
    def walk(pages: list[Page], prefix: str) -> None:
        for page in pages:
            page.rel_path = f"{prefix}/{page.slug}.md"
            if page.children:
                walk(page.children, f"{prefix}/{page.slug}")

    for group in groups:
        base = section if section == "changelog" else f"{section}/{group.dirname}"
        walk(group.pages, base)


def ordered_pages(groups: list[Group]) -> list[Page]:
    """Depth-first sidebar order -- what prev/next follows."""
    return [p for g in groups for p in g.walk()]


# --------------------------------------------------------------------------------------
# Transform
# --------------------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
FENCE_RE = re.compile(r"^\s*(```|~~~)")
HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*\s*$")
IMAGE_TAG_RE = re.compile(r"<Image\b([^>]*?)/?>", re.IGNORECASE | re.DOTALL)
CALLOUT_RE = re.compile(
    r"<Callout\b([^>]*)>\s*\n?(.*?)\n?\s*</Callout>", re.IGNORECASE | re.DOTALL
)
ATTR_RE = re.compile(r'(\w[\w-]*)\s*=\s*"([^"]*)"')
HTMLBLOCK_RE = re.compile(
    r"<HTMLBlock>\s*\{\s*`(.*?)`\s*\}\s*</HTMLBlock>", re.IGNORECASE | re.DOTALL
)
STYLE_ONLY_RE = re.compile(
    r"\A(?:\s*<(style|script)\b.*?</\1>)+\s*\Z", re.IGNORECASE | re.DOTALL
)
EMBED_RE = re.compile(r"<Embed\b([^>]*?)/?>", re.IGNORECASE | re.DOTALL)
ANCHOR_RE = re.compile(r"<Anchor\b([^>]*)>(.*?)</Anchor>", re.IGNORECASE | re.DOTALL)
TABLE_RE = re.compile(r"<Table\b([^>]*)>(.*?)</Table>", re.IGNORECASE | re.DOTALL)
ROW_RE = re.compile(r"<tr\b[^>]*>(.*?)</tr>", re.IGNORECASE | re.DOTALL)
CELL_RE = re.compile(r"<t([hd])\b[^>]*>(.*?)</t\1>", re.IGNORECASE | re.DOTALL)
ALIGN_RE = re.compile(r"align=\{\[(.*?)\]\}", re.DOTALL)
UNKNOWN_TAG_RE = re.compile(r"<([A-Z][A-Za-z0-9]*)(?=[\s/>])")


def split_fences(text: str):
    """Yield ``(line, in_code)`` so transforms can leave fenced blocks alone."""
    in_code = False
    fence = ""
    for line in text.split("\n"):
        m = FENCE_RE.match(line)
        if m:
            if not in_code:
                in_code, fence = True, m.group(1)
                yield line, True
                continue
            if line.strip().startswith(fence):
                in_code = False
                yield line, True
                continue
        yield line, in_code


def strip_frontmatter(text: str) -> tuple[dict, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip().strip('"')
    return meta, text[m.end():]


def convert_components(text: str, slug: str, unknown: dict) -> str:
    """Turn readme.io MDX components into markdown both Obsidian and GitHub render."""

    def image(m):
        attrs = dict(ATTR_RE.findall(m.group(1)))
        src = attrs.get("src", "")
        alt = attrs.get("alt", "")
        return f"![{alt}]({src})" if src else ""

    def callout(m):
        attrs = dict(ATTR_RE.findall(m.group(1)))
        icon = attrs.get("icon", "").strip()
        lines = [ln.strip() for ln in m.group(2).split("\n")]
        while lines and not lines[0]:
            lines.pop(0)
        while lines and not lines[-1]:
            lines.pop()
        out = [f"> {icon}".rstrip(), ">"] if icon else []
        out += [f"> {ln}".rstrip() for ln in lines]
        return "\n".join(out)

    def embed(m):
        attrs = dict(ATTR_RE.findall(m.group(1)))
        url = attrs.get("url") or attrs.get("href") or ""
        label = attrs.get("title") or url
        return f"[{label}]({url})" if url else ""

    def anchor(m):
        attrs = dict(ATTR_RE.findall(m.group(1)))
        href = attrs.get("href", "")
        label = m.group(2).strip() or attrs.get("title") or href
        return f"[{label}]({href})" if href else label

    def cell(text_: str) -> str:
        # A markdown cell is one line: upstream's soft breaks become <br>, and any
        # literal pipe has to be escaped or it would end the cell.
        text_ = re.sub(r"[ \t]*\n[ \t]*", "\n", text_.strip())
        text_ = re.sub(r"\n+", "<br>", text_)
        return text_.replace("|", "\\|")

    def table(m):
        aligns = [a.strip().strip('"') for a in
                  (ALIGN_RE.search(m.group(1)).group(1).split(",")
                   if ALIGN_RE.search(m.group(1)) else [])]
        rows = []
        for row in ROW_RE.findall(m.group(2)):
            rows.append([cell(c) for _, c in CELL_RE.findall(row)])
        rows = [r for r in rows if r]
        if not rows:
            return m.group(0)
        width = max(len(r) for r in rows)
        rows = [r + [""] * (width - len(r)) for r in rows]
        rule = []
        for i in range(width):
            a = aligns[i] if i < len(aligns) else "left"
            rule.append({"center": ":---:", "right": "---:"}.get(a, "---"))
        out = ["| " + " | ".join(rows[0]) + " |", "| " + " | ".join(rule) + " |"]
        out += ["| " + " | ".join(r) + " |" for r in rows[1:]]
        return "\n" + "\n".join(out) + "\n"

    def html_block(m):
        inner = m.group(1).strip()
        # Nearly every one of these carries only page styling for the live site, which
        # is meaningless in an archive. Anything else is kept as raw HTML.
        return "" if STYLE_ONLY_RE.match(inner) else inner

    text = IMAGE_TAG_RE.sub(image, text)
    text = CALLOUT_RE.sub(callout, text)
    text = HTMLBLOCK_RE.sub(html_block, text)
    text = TABLE_RE.sub(table, text)
    text = EMBED_RE.sub(embed, text)
    text = ANCHOR_RE.sub(anchor, text)

    # Anything else that looks like an MDX component is reported rather than silently
    # left in place -- 1,000 pages hold more component types than a sample shows.
    known = {"Image", "Callout", "HTMLBlock", "Table", "Embed", "Anchor"}
    for line, in_code in split_fences(text):
        if in_code:
            continue          # `$html = "<HTML "` in a sample is not a component
        for m in UNKNOWN_TAG_RE.finditer(line):
            if m.group(1) not in known:
                unknown.setdefault(m.group(1), set()).add(slug)
    return text


def transform_page(page: Page, unknown: dict) -> None:
    """First pass: everything that does not need the other pages to exist yet."""
    meta, body = strip_frontmatter(page.raw)
    page.updated_at = meta.get("updatedAt", page.updated_at)

    body = BOILERPLATE_RE.sub("", body)
    body = convert_components(body, page.slug, unknown)

    out_lines: list[str] = []
    first_h1 = None
    for line, in_code in split_fences(body):
        if in_code:
            out_lines.append(line)
            continue
        m = HEADING_RE.match(line)
        if not m:
            out_lines.append(line)
            continue
        hashes, text_ = m.group(1), m.group(2).strip()
        if first_h1 is None and len(hashes) == 1:
            first_h1 = text_
        anchor = kebab_heading(text_)
        page.headings[github_slug(text_)] = anchor
        page.headings[anchor] = anchor
        out_lines.append(f"{hashes} {anchor}")

    if first_h1:
        page.title = first_h1

    body = "\n".join(out_lines).strip("\n")
    # Collapse the runs of blank lines that component removal leaves behind.
    page.body = re.sub(r"\n{3,}", "\n\n", body)

    for m in IMAGE_URL_RE.finditer(page.body):
        page.images.append(m.group(2))


# --------------------------------------------------------------------------------------
# Second pass: links, images, page rendering
# --------------------------------------------------------------------------------------

INTERNAL_LINK_RE = re.compile(
    r"https?://gtidocs\.(?:readme\.io|virustotal\.com)"
    r"/(docs|reference|changelog)/([A-Za-z0-9][A-Za-z0-9._-]*?)(?:\.md)?(#[^)\s\"']*)?(?=[)\s\"'\]]|$)"
)
# Assets live on two hosts: readme.io's own CDN and Google's documentation bucket.
ASSET_HOST_RE = r"https://(?:files\.readme\.io|storage\.googleapis\.com/gtidocresources)/[^)\s]+"
IMAGE_URL_RE = re.compile(r"(!\[[^\]]*\]\()(" + ASSET_HOST_RE + r")(\))")
# Upstream also writes site-root-relative links (`/docs/foo`) and bare slugs (`foo#bar`).
LOCAL_LINK_RE = re.compile(r"(?<=\]\()\s*(/?[A-Za-z0-9][A-Za-z0-9._-]*(?:/[A-Za-z0-9._-]+)?)(#[^)\s]*)?\s*(?=\))")


def rel_link(from_rel: str, to_rel: str) -> str:
    return os.path.relpath(to_rel, os.path.dirname(from_rel)).replace(os.sep, "/")


def image_filename(url: str) -> str:
    name = urllib.parse.unquote(url.rsplit("/", 1)[-1].split("?")[0])
    name = re.sub(r"[^\w.\-]+", "-", name) or "image"
    if re.match(r"[0-9a-f]{32,}-", name):
        return name          # readme.io already prefixes a content hash
    # Google's bucket reuses plain names across directories, so key on the full URL.
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:10]
    return f"{digest}-{name}"


def rewrite_links(page: Page, by_slug: dict, want_images: bool) -> str:
    """Point internal links at mirrored files; leave anything unmirrored absolute."""

    def link(m):
        seg, slug, anchor = m.group(1), m.group(2), m.group(3) or ""
        target = by_slug.get((seg, slug))
        if target is None:
            return m.group(0)          # hidden, deleted or out-of-scope: keep upstream URL
        if anchor:
            key = anchor[1:].lower()
            anchor = "#" + target.headings.get(key, anchor[1:])
        return md_target(rel_link(page.rel_path, target.rel_path) + anchor)

    def image(m):
        if not want_images:
            return m.group(0)
        rel = rel_link(page.rel_path, f"{IMG_DIRNAME}/{image_filename(m.group(2))}")
        return m.group(1) + md_target(rel) + m.group(3)

    def local(m):
        target, anchor = m.group(1).strip(), m.group(2) or ""
        parts = target.strip("/").split("/")
        if target.startswith("/"):
            # `/docs/foo`, or a bare `/changelog` pointing at a section landing page.
            if parts[0] not in {"docs", "reference", "changelog"}:
                return m.group(0)
            if len(parts) == 1:
                section = next(k for k, v in SECTIONS.items() if v["url_path"] == parts[0])
                return md_target(rel_link(page.rel_path, f"{section}/README.md"))
            found = by_slug.get((parts[0], parts[1]))
        elif len(parts) == 1 and "." not in target:
            # A bare slug, resolved in this page's own section.
            found = by_slug.get((SECTIONS[page.section]["url_path"], target))
        else:
            return m.group(0)
        if found is None:
            return m.group(0)
        if anchor:
            anchor = "#" + found.headings.get(anchor[1:].lower(), anchor[1:])
        return md_target(rel_link(page.rel_path, found.rel_path) + anchor)

    out = []
    for line, in_code in split_fences(page.body):
        if not in_code:
            line = INTERNAL_LINK_RE.sub(link, line)
            line = IMAGE_URL_RE.sub(image, line)
            line = LOCAL_LINK_RE.sub(local, line)
        out.append(line)
    return "\n".join(out)


def yaml_str(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def render_page(page: Page, body: str, crumbs: list[tuple[str, str]], up_rel: str,
                prev: Page | None, nxt: Page | None, retrieved: str) -> str:
    url_path = SECTIONS[page.section]["url_path"]
    source = f"{PRIMARY_HOST}/{url_path}/{page.slug}"

    fm = [
        "---",
        f"title: {yaml_str(page.title)}",
        f"source: {source}",
        f"slug: {page.slug}",
        f"section: {page.section}",
        f"group: {yaml_str(page.group)}",
    ]
    if page.updated_at:
        fm.append(f"updatedAt: {page.updated_at}")
    fm += [f"retrieved: {retrieved}", "---", ""]

    trail = " › ".join(
        f"[{label}]({md_target(rel_link(page.rel_path, target))})" if target else label
        for label, target in crumbs
    )

    nav = []
    if prev:
        nav.append(f"← [{prev.title}]({md_target(rel_link(page.rel_path, prev.rel_path))})")
    nav.append(f"[up]({md_target(rel_link(page.rel_path, up_rel))})")
    if nxt:
        nav.append(f"[{nxt.title}]({md_target(rel_link(page.rel_path, nxt.rel_path))}) →")

    return "\n".join(
        fm
        + [trail, "", "---", "", body, "", "---", "", " · ".join(nav), "",
           f"*Archived from <{source}>.*", ""]
    )


# --------------------------------------------------------------------------------------
# Indexes
# --------------------------------------------------------------------------------------

def page_bullets(pages: list[Page], from_rel: str, depth: int = 0) -> list[str]:
    out = []
    for p in pages:
        pad = "  " * depth
        if p.is_link:
            out.append(f"{pad}- [{p.title}]({p.link_url}) ↗")
        else:
            out.append(f"{pad}- [{p.title}]({md_target(rel_link(from_rel, p.rel_path))})")
        out += page_bullets(p.children, from_rel, depth + 1)
    return out


def render_group_index(group: Group, section: str, retrieved: str) -> tuple[str, str]:
    rel = (f"{section}/{group.dirname}/README.md" if section != "changelog"
           else "changelog/README.md")
    crumbs = [
        ("gtidocs", "README.md"),
        (SECTIONS[section]["title"], f"{section}/README.md"),
        (group.title, ""),
    ]
    trail = " › ".join(
        f"[{lbl}]({md_target(rel_link(rel, tgt))})" if tgt else lbl for lbl, tgt in crumbs
    )
    lines = [
        "---",
        f"title: {yaml_str(group.title)}",
        f"section: {section}",
        f"retrieved: {retrieved}",
        "---",
        "",
        trail,
        "",
        "---",
        "",
        f"## {kebab_heading(group.title)}",
        "",
    ]
    lines += page_bullets(group.pages, rel)
    lines.append("")
    return rel, "\n".join(lines)


def render_section_index(section: str, groups: list[Group], retrieved: str) -> tuple[str, str]:
    rel = f"{section}/README.md"
    title = SECTIONS[section]["title"]
    lines = [
        "---",
        f"title: {yaml_str(title)}",
        f"source: {PRIMARY_HOST}/{SECTIONS[section]['url_path']}/",
        f"section: {section}",
        f"retrieved: {retrieved}",
        "---",
        "",
        f"[gtidocs]({md_target(rel_link(rel, 'README.md'))}) › {title}",
        "",
        "---",
        "",
        f"## {kebab_heading(title)}",
        "",
        f"{sum(1 for g in groups for _ in g.walk())} pages in "
        f"{len(groups)} groups, in the order the site's navigation lists them.",
        "",
    ]
    for group in groups:
        if section == "changelog":
            lines += page_bullets(group.pages, rel) + [""]
            continue
        gi = f"{section}/{group.dirname}/README.md"
        lines.append(f"### [{group.title}]({md_target(rel_link(rel, gi))})")
        lines.append("")
        lines += page_bullets(group.pages, rel)
        lines.append("")
    return rel, "\n".join(lines)


ROOT_README = """---
title: "Google Threat Intelligence documentation (archived)"
source: {primary}/docs/
retrieved: {retrieved}
---

## google-threat-intelligence-documentation-(archived)

An **unofficial** local snapshot of the Google Threat Intelligence documentation hub,
<{primary}/docs/>, taken on {retrieved}. It exists so this repository's
documents can cite and deep-link GTI material without depending on a live website.

The documentation is © Google and is **not** covered by this repository's CC BY 4.0
licence. Nothing here is authoritative — check the live page (linked at the foot of every
file) before relying on it.

### contents

| Section | Pages | Upstream |
| --- | --- | --- |
{rows}

### how-this-was-made

Generated by [`tools/gtidocs-mirror/mirror.py`]({tool}), which walks the site's own
navigation tree, fetches each page's markdown, rewrites headings to this repository's
kebab-case convention, downloads images and relinks everything locally. Refresh with:

```bash
python3 tools/gtidocs-mirror/mirror.py
```

The output is deterministic, so a refresh shows up as a readable `git diff`.
"""


def render_root_index(sections: dict[str, list[Group]], retrieved: str) -> str:
    rows = []
    for name, groups in sections.items():
        count = sum(1 for g in groups for _ in g.walk())
        rows.append(
            f"| [{SECTIONS[name]['title']}]({name}/README.md) | {count} | "
            f"<{PRIMARY_HOST}/{SECTIONS[name]['url_path']}/> |"
        )
    return ROOT_README.format(
        primary=PRIMARY_HOST,
        retrieved=retrieved,
        rows="\n".join(rows),
        tool="../../../../tools/gtidocs-mirror/mirror.py",
    )


RETRIEVED_LINE_RE = re.compile(r"^retrieved: .*$", re.MULTILINE)


def write_if_changed(dest: str, text: str) -> bool:
    """Write only when the content really differs, ignoring the `retrieved` stamp.

    Without this, every refresh would rewrite all ~1,000 files with today's date and
    bury the handful of genuine upstream changes in the diff. A page whose content is
    unchanged keeps the date it was actually captured on.
    """
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if os.path.exists(dest):
        with open(dest, encoding="utf-8") as fh:
            old = fh.read()
        if RETRIEVED_LINE_RE.sub("", old) == RETRIEVED_LINE_RE.sub("", text):
            return False
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(text)
    return True


# --------------------------------------------------------------------------------
# Driver
# --------------------------------------------------------------------------------------

def fetch_all(pages: list[Page], section: str, use_cache: bool) -> list[str]:
    """Fetch every page body, caching raw responses. Returns slugs that failed."""
    url_path = SECTIONS[section]["url_path"]
    cache_dir = os.path.join(CACHE_ROOT, "raw", section)
    os.makedirs(cache_dir, exist_ok=True)
    todo, failures = [], []
    done = 0

    for page in pages:
        cached = os.path.join(cache_dir, f"{page.slug}.md")
        if use_cache and os.path.exists(cached):
            with open(cached, encoding="utf-8") as fh:
                page.raw = fh.read()
        else:
            todo.append(page)

    def work(page: Page):
        time.sleep(REQUEST_DELAY)
        text = fetch_markdown(url_path, page.slug)
        with open(os.path.join(cache_dir, f"{page.slug}.md"), "w", encoding="utf-8") as fh:
            fh.write(text)
        return page, text

    with concurrent.futures.ThreadPoolExecutor(MAX_WORKERS) as pool:
        futures = {pool.submit(work, p): p for p in todo}
        for fut in concurrent.futures.as_completed(futures):
            page = futures[fut]
            done += 1
            try:
                _, text = fut.result()
                page.raw = text
            except Exception as exc:
                failures.append(page.slug)
                log(f"    ! {page.slug}: {exc}")
            if done % 25 == 0 or done == len(todo):
                log(f"    {done}/{len(todo)} fetched")

    # Serial retry sweeps. The bot challenge is transient and clears when unhurried, so
    # the recovery path is one request at a time with a real pause between them.
    for sweep in range(3):
        if not failures:
            break
        pending = set(failures)
        log(f"    retry sweep {sweep + 1}: {len(pending)} page(s), serially")
        failures = []
        for page in [p for p in todo if p.slug in pending]:
            time.sleep(2.0 * (sweep + 1))
            try:
                page.raw = fetch_markdown(url_path, page.slug)
                with open(os.path.join(cache_dir, f"{page.slug}.md"), "w",
                          encoding="utf-8") as fh:
                    fh.write(page.raw)
            except Exception as exc:
                failures.append(page.slug)
                log(f"    ! {page.slug}: {exc}")
    return failures


def download_images(urls: set[str], out_dir: str) -> list[str]:
    os.makedirs(out_dir, exist_ok=True)
    failures = []

    def work(url: str):
        dest = os.path.join(out_dir, image_filename(url))
        if os.path.exists(dest):
            return
        time.sleep(REQUEST_DELAY)
        body, _ = _raw_get(url)
        with open(dest, "wb") as fh:
            fh.write(body)

    with concurrent.futures.ThreadPoolExecutor(MAX_WORKERS) as pool:
        futures = {pool.submit(work, u): u for u in sorted(urls)}
        for fut in concurrent.futures.as_completed(futures):
            try:
                fut.result()
            except Exception as exc:
                failures.append(futures[fut])
                log(f"    ! image {futures[fut]}: {exc}")
    return failures


def build_crumbs(page: Page, ancestors: list[Page], section: str, group: Group):
    crumbs = [("gtidocs", "README.md"), (SECTIONS[section]["title"], f"{section}/README.md")]
    if section == "changelog":
        crumbs.append((group.title, "changelog/README.md"))
    else:
        crumbs.append((group.title, f"{section}/{group.dirname}/README.md"))
    for anc in ancestors:
        crumbs.append((anc.title, anc.rel_path))
    crumbs.append((page.title, ""))
    return crumbs


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--section", action="append", choices=list(SECTIONS),
                    help="limit to one section (repeatable); default is all three")
    ap.add_argument("--no-images", action="store_true", help="leave images hotlinked")
    ap.add_argument("--dry-run", action="store_true",
                    help="discover and report only; fetch nothing, write nothing")
    ap.add_argument("--use-cache", action="store_true",
                    help="reuse previously fetched pages instead of re-downloading")
    ap.add_argument("--out", default=OUT_ROOT, help=f"output root (default: {OUT_ROOT})")
    args = ap.parse_args()

    wanted = args.section or list(SECTIONS)
    retrieved = _dt.date.today().isoformat()
    want_images = not args.no_images

    log(f"gtidocs mirror — sections: {', '.join(wanted)}")
    llms = fetch_text(LLMS_TXT)
    os.makedirs(CACHE_ROOT, exist_ok=True)
    with open(os.path.join(CACHE_ROOT, "llms.txt"), "w", encoding="utf-8") as fh:
        fh.write(llms)
    llms_slugs = parse_llms_slugs(llms)

    sections: dict[str, list[Group]] = {}
    for name in wanted:
        groups = (discover_changelog(llms) if name == "changelog"
                  else discover_sidebar(name, args.use_cache))
        assign_paths(groups, name)
        sections[name] = groups
        pages = ordered_pages(groups)
        links = [p for p in pages if p.is_link]
        seg = SECTIONS[name]["url_path"]
        only_llms = llms_slugs.get(seg, set()) - {p.slug for p in pages}
        log(f"  {name}: {len(groups)} groups, {len(pages)} pages "
            f"({len(links)} external link entries)")
        if only_llms:
            log(f"    note: {len(only_llms)} slug(s) in llms.txt but not in the sidebar: "
                f"{', '.join(sorted(only_llms)[:5])}"
                f"{' …' if len(only_llms) > 5 else ''}")

    if args.dry_run:
        log("dry run — nothing fetched or written")
        return 0

    by_slug: dict[tuple[str, str], Page] = {}
    unknown_components: dict[str, set] = {}
    all_images: set[str] = set()
    failed: list[str] = []

    for name, groups in sections.items():
        pages = [p for p in ordered_pages(groups) if not p.is_link]
        log(f"  fetching {name} ({len(pages)} pages)")
        failed += [f"{name}/{s}" for s in fetch_all(pages, name, args.use_cache)]
        for page in pages:
            if not page.raw:
                continue
            transform_page(page, unknown_components)
            by_slug[(SECTIONS[name]["url_path"], page.slug)] = page
            all_images.update(page.images)

    if want_images and all_images:
        log(f"  downloading {len(all_images)} image(s)")
        img_failed = download_images(all_images, os.path.join(args.out, IMG_DIRNAME))
        failed += [f"image/{u}" for u in img_failed]

    written = 0
    for name, groups in sections.items():
        flat = [p for p in ordered_pages(groups) if not p.is_link and p.raw]
        # One walk builds every page's group and ancestor chain, rather than re-searching
        # the tree per page.
        context: dict[int, tuple[Group, list[Page]]] = {}
        for grp in groups:
            stack = [(pg, []) for pg in reversed(grp.pages)]
            while stack:
                node, path = stack.pop()
                context[id(node)] = (grp, path)
                stack += [(c, path + [node]) for c in reversed(node.children)]
        for i, page in enumerate(flat):
            group, ancestors = context[id(page)]
            up_rel = (f"{name}/{group.dirname}/README.md" if name != "changelog"
                      else "changelog/README.md")
            body = rewrite_links(page, by_slug, want_images)
            text = render_page(
                page, body,
                build_crumbs(page, ancestors, name, group),
                up_rel,
                flat[i - 1] if i else None,
                flat[i + 1] if i + 1 < len(flat) else None,
                retrieved,
            )
            if write_if_changed(os.path.join(args.out, page.rel_path), text):
                written += 1

        rel, text = render_section_index(name, groups, retrieved)
        write_if_changed(os.path.join(args.out, rel), text)
        if name != "changelog":
            for group in groups:
                rel, text = render_group_index(group, name, retrieved)
                write_if_changed(os.path.join(args.out, rel), text)

    if set(sections) == set(SECTIONS):
        write_if_changed(os.path.join(args.out, "README.md"),
                         render_root_index(sections, retrieved))

    log(f"{written} page file(s) changed under {args.out}")
    if unknown_components:
        log("  unconverted MDX components (add handlers if these matter):")
        for tag, slugs in sorted(unknown_components.items()):
            log(f"    <{tag}> in {len(slugs)} page(s), e.g. {sorted(slugs)[0]}")
    if failed:
        log(f"FAILED: {len(failed)} item(s) could not be retrieved:")
        for item in failed[:20]:
            log(f"  {item}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
