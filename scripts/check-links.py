#!/usr/bin/env python3
"""Validate internal Markdown links against Patchwork's authoring conventions.

Checks every tracked .md file for:
  - relative file links that do not resolve (images included, %20-decoded)
  - section anchors that match no heading in the target file
  - [[wikilinks]], which GitHub renders as literal text

Anchors are matched in the Obsidian form the repo uses deliberately (README
"Authoring-conventions"): heading text, whitespace collapsed to hyphens,
lowercased, all other punctuation preserved. GitHub's slug algorithm is NOT
used -- validating against it would report every anchor here as broken.

Content inside fenced code blocks and inline code spans is ignored, so
documentation *about* links is not mistaken for links.

Usage:  python3 scripts/check-links.py [--quiet] [root]
Exit:   0 clean, 1 problems found.
"""

import re
import sys
import urllib.parse
from pathlib import Path

EXTERNAL = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|//)", re.I)
INLINE_LINK = re.compile(r"!?\[(?P<text>[^\]]*)\]\((?P<target>[^)\s]+)(?:\s+\"[^\"]*\")?\)")
HTML_SRC = re.compile(r"<(?:img|a)\b[^>]*?\b(?:src|href)=\"(?P<target>[^\"]+)\"", re.I)
WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")
HEADING = re.compile(r"^(?P<hashes>#{1,6})\s+(?P<text>.+?)\s*#*$", re.M)
FOOTNOTE_REF = re.compile(r"\[\^[^\]]+\]")
FENCE = re.compile(r"^(?P<indent>[ \t]*)(?P<mark>```+|~~~+)(?P<info>.*)$")


def strip_code(text: str) -> str:
    """Blank out fenced blocks and inline spans, preserving line/column offsets."""
    lines = text.split("\n")
    fence_mark = None
    for i, line in enumerate(lines):
        m = FENCE.match(line)
        if fence_mark is None:
            if m:
                fence_mark = m.group("mark")[0] * 3
                lines[i] = ""
            continue
        # inside a fence: blank everything, close on a matching marker
        stripped = line.strip()
        lines[i] = ""
        if stripped.startswith(fence_mark) and not stripped.rstrip(fence_mark[0]):
            fence_mark = None
    out = "\n".join(lines)
    # inline code spans -> spaces, keeping length so columns stay honest
    return re.sub(r"`+[^`\n]*`+", lambda m: " " * len(m.group(0)), out)


def anchor_form(heading_text: str) -> str:
    """Heading text -> the anchor string this repo links to."""
    text = FOOTNOTE_REF.sub("", heading_text)
    text = re.sub(r"[`*_]", "", text)
    return re.sub(r"\s+", "-", text.strip()).lower()


def headings_of(path: Path, cache: dict) -> set:
    if path not in cache:
        try:
            body = strip_code(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError):
            cache[path] = set()
            return cache[path]
        anchors = set()
        for m in HEADING.finditer(body):
            raw = m.group("text").strip()
            anchors.add(anchor_form(raw))
            anchors.add(anchor_form(raw).rstrip("."))
        cache[path] = anchors
    return cache[path]


def line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def check_file(path: Path, root: Path, cache: dict) -> list:
    problems = []
    raw = path.read_text(encoding="utf-8")
    body = strip_code(raw)

    def report(pos, msg):
        problems.append((path.relative_to(root), line_of(body, pos), msg))

    for m in WIKILINK.finditer(body):
        report(m.start(), f"wikilink [[{m.group(1)}]] -- GitHub renders this as literal text")

    targets = [(m.start(), m.group("target")) for m in INLINE_LINK.finditer(body)]
    targets += [(m.start(), m.group("target")) for m in HTML_SRC.finditer(body)]

    for pos, target in targets:
        target = target.strip().lstrip("<").rstrip(">")
        if not target or EXTERNAL.match(target):
            continue

        rel, _, anchor = target.partition("#")
        rel = urllib.parse.unquote(rel)
        anchor = urllib.parse.unquote(anchor).lower()

        if rel:
            dest = (path.parent / rel).resolve()
            if not dest.exists():
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


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    quiet = "--quiet" in sys.argv or "-q" in sys.argv
    root = Path(args[0] if args else ".").resolve()

    files = sorted(p for p in root.rglob("*.md") if ".git" not in p.parts)
    if not files:
        print(f"no markdown files under {root}", file=sys.stderr)
        return 1

    cache: dict = {}
    problems = []
    for path in files:
        problems.extend(check_file(path, root, cache))

    for rel, line, msg in problems:
        print(f"{rel}:{line}: {msg}")

    if not quiet:
        summary = f"{len(files)} files checked, {len(problems)} problem(s)"
        print(f"\n{summary}", file=sys.stderr)

    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
