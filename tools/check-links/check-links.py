#!/usr/bin/env python3
"""Validate internal Markdown links and GitHub-rendered heading anchors.

Checks every tracked .md file for:
  - relative file links that do not resolve (images included, %20-decoded)
  - section anchors that match no heading in the target file
  - [[wikilinks]], which GitHub renders as literal text

Anchors use GitHub's rendered-heading form: lowercase text, spaces replaced
by hyphens, punctuation/formatting removed, duplicate anchors numbered.

Content inside fenced code blocks and inline code spans is ignored, so
documentation *about* links is not mistaken for links.

`docs/Easy-access/` is skipped by default: it is a mirror of other people's
documentation, so its broken breadcrumbs are theirs to fix, not ours, and at
roughly forty findings per authored one they bury everything that is.

Usage:  python3 tools/check-links/check-links.py [--quiet] [--all] [--public] [root]
Exit:   0 clean, 1 problems found.
"""

import html
import importlib.util
import re
import subprocess
import sys
import unicodedata
import urllib.parse
from pathlib import Path

# Mirrored third-party documentation. Excluded unless --all.
VENDORED = ("docs/Easy-access",)

EXTERNAL = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|//)", re.I)
# CommonMark allows two destination forms. The <angle> one is what this repo
# uses whenever an anchor contains brackets -- `[x](<#author-these-(13)>)` --
# and reading it as the bare form truncates the anchor at the first ")".
INLINE_LINK = re.compile(
    r"!?\[(?P<text>[^\]]*)\]\("
    r"(?:<(?P<angle>[^<>\n]*)>|(?P<bare>(?:[^()\s]|\([^()\s]*\))+))"
    r"(?:\s+\"[^\"]*\")?\)"
)
HTML_SRC = re.compile(r"<(?:img|a)\b[^>]*?\b(?:src|href)=\"(?P<target>[^\"]+)\"", re.I)
HTML_ANCHOR = re.compile(r"<[^>]+\b(?:id|name)=[\"']([^\"']+)[\"']", re.I)
REFERENCE = re.compile(r"^ {0,3}\[(?!\^)[^\]\n]+\]:\s*(?:<(?P<angle>[^<>\n]+)>|(?P<bare>\S+))", re.M)
WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")
HEADING = re.compile(r"^ {0,3}(?:>\s*)*(?P<hashes>#{1,6})[ \t]+(?P<text>.+?)(?:[ \t]+#+)?[ \t]*$", re.M)
FOOTNOTE_REF = re.compile(r"\[\^[^\]]+\]")
FENCE = re.compile(r"^(?P<indent>[ \t]*)(?P<mark>```+|~~~+)(?P<info>.*)$")


def strip_fenced_code(text: str) -> str:
    """Blank fenced blocks, retaining offsets and inline heading text."""
    lines = text.split("\n")
    fence_mark = None
    for i, line in enumerate(lines):
        m = FENCE.match(line)
        if fence_mark is None:
            if m:
                fence_mark = m.group("mark")
                lines[i] = " " * len(line)
            continue
        # inside a fence: blank everything, close on a matching marker
        stripped = line.strip()
        lines[i] = " " * len(line)
        if len(stripped) >= len(fence_mark) and not stripped.rstrip(fence_mark[0]):
            fence_mark = None
    return "\n".join(lines)


def strip_code(text: str) -> str:
    """Blank code examples while retaining line/column offsets."""
    out = strip_fenced_code(text)
    # inline code spans -> spaces, keeping length so columns stay honest
    return re.sub(r"`+[^`\n]*`+", lambda m: " " * len(m.group(0)), out)


def anchor_form(heading_text: str) -> str:
    """Rendered heading text -> GitHub anchor (without duplicate suffix)."""
    text = FOOTNOTE_REF.sub("", heading_text)
    text = INLINE_LINK.sub(lambda m: m.group("text"), text)
    text = re.sub(r"<[^>]*>", "", text)
    # Preserve underscores inside code spans and identifiers; remove emphasis.
    code = {}
    def protect_code(match):
        key = f"\x00{len(code)}\x00"
        code[key] = match.group(1)
        return key
    text = re.sub(r"`+([^`]+)`+", protect_code, text)
    text = re.sub(r"(?<!\w)_{1,2}(.+?)_{1,2}(?!\w)", r"\1", text)
    text = text.replace("*", "").replace("~", "")
    for key, value in code.items():
        text = text.replace(key, value)
    text = html.unescape(text).strip().lower()
    text = "".join(c for c in text if c in " -_" or unicodedata.category(c)[0] not in "PSCZ")
    return text.replace(" ", "-")


def headings_of(path: Path, cache: dict) -> set:
    if path not in cache:
        try:
            body = strip_fenced_code(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError):
            cache[path] = set()
            return cache[path]
        anchors = set()
        for m in HEADING.finditer(body):
            raw = m.group("text").strip()
            base = anchor_form(raw)
            anchor = base
            suffix = 0
            while anchor in anchors:
                suffix += 1
                anchor = f"{base}-{suffix}"
            anchors.add(anchor)
        anchors.update(html.unescape(m.group(1)) for m in HTML_ANCHOR.finditer(body))
        cache[path] = anchors
    return cache[path]


def line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def check_file(path: Path, root: Path, cache: dict, published=None) -> list:
    problems = []
    raw = path.read_text(encoding="utf-8")
    body = strip_code(raw)

    def report(pos, msg):
        problems.append((path.relative_to(root), line_of(body, pos), msg))

    for m in WIKILINK.finditer(body):
        report(m.start(), f"wikilink [[{m.group(1)}]] -- GitHub renders this as literal text")

    targets = [
        (m.start(), m.group("angle") if m.group("angle") is not None else m.group("bare"))
        for m in INLINE_LINK.finditer(body)
    ]
    targets += [(m.start(), m.group("target")) for m in HTML_SRC.finditer(body)]
    targets += [(m.start(), m.group("angle") or m.group("bare")) for m in REFERENCE.finditer(body)]

    for pos, target in targets:
        target = target.strip()
        if not target or EXTERNAL.match(target):
            continue

        rel, _, anchor = target.partition("#")
        rel = urllib.parse.unquote(rel)
        anchor = urllib.parse.unquote(anchor)

        if rel:
            dest = (path.parent / rel).resolve()
            inside = dest == root or root in dest.parents
            available = published is None or dest in published or (dest.is_dir() and any(dest in p.parents for p in published))
            if not inside or not dest.exists() or not available:
                hint = ""
                if rel.startswith("docs/") and path.parent != root:
                    hint = " -- vault-root-absolute? links resolve from the containing file"
                report(pos, f"missing file: {target}{hint}")
                continue
        else:
            dest = path  # bare "#anchor" -> this file

        if anchor and dest.suffix.lower() == ".md":
            if anchor not in headings_of(dest, cache):
                where = "this file" if dest == path else rel
                report(pos, f"no heading matches anchor #{anchor} in {where}")

    return problems


def markdown_files(root: Path) -> list[Path]:
    """Check what Git would ship, not ignored caches or local graph output."""
    try:
        git_root = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=root, check=True, capture_output=True, text=True).stdout.strip()
        if Path(git_root).resolve() != root.resolve():
            raise OSError("export is not the enclosing checkout's root")
        output = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=root, check=True, capture_output=True, text=True).stdout
        files = [root / p for p in output.split("\0") if p.endswith(".md")]
    except (OSError, subprocess.CalledProcessError):
        files = list(root.rglob("*.md"))
    skip = {".git", ".cache", ".codex", ".claude", ".obsidian", "__pycache__", "graphify-out"}
    return sorted(set(p for p in files if p.is_file() and not skip.intersection(p.relative_to(root).parts)))


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    quiet = "--quiet" in sys.argv or "-q" in sys.argv
    check_all = "--all" in sys.argv
    root = Path(args[0] if args else ".").resolve()

    found = markdown_files(root)
    published = None
    if "--public" in sys.argv:
        helper = Path(__file__).resolve().parents[1] / "public-review/public_files.py"
        spec = importlib.util.spec_from_file_location("public_files", helper)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        published = {(root / p).resolve() for p in module.public_paths(root)}
        found = [p for p in found if p.resolve() in published]
    if not found:
        print(f"no markdown files under {root}", file=sys.stderr)
        return 1

    vendored = [] if check_all else [root / v for v in VENDORED]
    files = [p for p in found if not any(v in p.parents for v in vendored)]
    skipped = len(found) - len(files)

    cache: dict = {}
    problems = []
    for path in files:
        problems.extend(check_file(path, root, cache, published))

    for rel, line, msg in problems:
        print(f"{rel}:{line}: {msg}")

    if not quiet:
        summary = f"{len(files)} files checked, {len(problems)} problem(s)"
        if skipped:
            # Never let the exclusion be silent -- a clean run has to say what
            # it did not look at, or it reads as "the whole repo is fine".
            summary += f"; {skipped} vendored file(s) skipped ({', '.join(VENDORED)}) -- --all to include"
        print(f"\n{summary}", file=sys.stderr)

    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
