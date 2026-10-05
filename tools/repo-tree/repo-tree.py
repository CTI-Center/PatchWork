#!/usr/bin/env python3
"""Generate the repository-layout tree in README.md from the repository itself.

The tree in README used to be hand-maintained, so it drifted: it listed `img/`,
`report-types.md`, `samples/` and `templates/` long after those were renamed to
`Resources/`, `Report-Types.md`, `Real-Examples/` and `Report-Templates/`. A reader's
first impression of the repo was a map of a repo that no longer existed.

This script derives the structure from git and rewrites the block between the
`repo-tree` markers in README.md, so moving a folder and re-running is the whole
update. Only the *descriptions* are hand-written, and they live in
`descriptions.json` beside this script.

What it lists is what git would ship: tracked files, plus untracked files that
`.gitignore` does not exclude. Ignored junk (`.obsidian/`, `.claude/`, the mirror
cache) never appears, and a file staged but not yet committed does — which is what
you want while a change is in progress.

Renames are surfaced rather than silently swallowed. A path with no description is
reported as MISSING, and a description whose path has disappeared is reported as
STALE; `--check` turns either into a non-zero exit, so CI or a pre-commit hook can
refuse a layout change that left the descriptions behind.

Usage
-----
    python3 tools/repo-tree/repo-tree.py              # rewrite README.md
    python3 tools/repo-tree/repo-tree.py --check      # exit 1 if README is stale
    python3 tools/repo-tree/repo-tree.py --print      # write nothing, show the tree
    python3 tools/repo-tree/repo-tree.py --depth 3    # descend one level further

Python 3.9+, standard library only.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

START = "<!-- repo-tree:start -->"
END = "<!-- repo-tree:end -->"

TEE, ELBOW, PIPE, SPACE = "├── ", "└── ", "│   ", "    "

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
DESCRIPTIONS = HERE / "descriptions.json"
README = ROOT / "README.md"


def repo_paths() -> list[str]:
    """Every path git would ship: tracked, plus untracked and not ignored."""
    try:
        git_root = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout.strip()
        if Path(git_root).resolve() != ROOT.resolve():
            raise OSError("public copy is not the enclosing checkout's root")
        out = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout
    except (subprocess.CalledProcessError, OSError):
        # not a git checkout - fall back to the filesystem, minus the obvious noise
        skip = {".git", ".obsidian", ".claude", ".remember", "__pycache__"}
        return sorted(
            str(p.relative_to(ROOT))
            for p in ROOT.rglob("*")
            if p.is_file() and not skip & set(p.relative_to(ROOT).parts)
        )
    # `--cached` reports the index, which still names the old path after a plain
    # `mv`. Intersect with the working tree so a rename shows up immediately
    # rather than only once it is staged.
    return sorted(p for p in out.splitlines() if p and (ROOT / p).exists())


def nest(paths: list[str], depth: int) -> dict:
    """{name: subtree-or-None}, where None marks a file and {} a collapsed directory."""
    root: dict = {}
    for path in paths:
        parts = path.split("/")
        node = root
        for i, part in enumerate(parts):
            is_file = i == len(parts) - 1
            if i == depth - 1 and not is_file:
                node.setdefault(part, {})       # collapsed directory
                break
            if is_file:
                node.setdefault(part, None)
            else:
                nxt = node.get(part)
                if not isinstance(nxt, dict):
                    nxt = {}
                    node[part] = nxt
                node = nxt
    return root


def flatten(node: dict, prefix: str = "", path: str = "") -> list[tuple[str, str]]:
    """Render to (drawn-line, repo-relative-path) pairs, directories first-class."""
    rows: list[tuple[str, str]] = []
    # alphabetical, case-insensitive, files and directories interleaved -
    # the same order `docs/` was already written in by hand
    names = sorted(node, key=lambda s: (s.lower(), s))
    for i, name in enumerate(names):
        child = node[name]
        last = i == len(names) - 1
        is_dir = isinstance(child, dict)
        here = f"{path}/{name}" if path else name
        label = f"{name}/" if is_dir else name
        rows.append((prefix + (ELBOW if last else TEE) + label, here))
        if is_dir and child:
            rows.extend(flatten(child, prefix + (SPACE if last else PIPE), here))
    return rows


def render(rows: list[tuple[str, str]], desc: dict[str, str]) -> tuple[str, list[str], list[str]]:
    described = [(line, desc[p]) for line, p in rows if p in desc]
    width = max((len(l) for l, _ in described), default=0) + 2
    out = []
    for line, path in rows:
        d = desc.get(path)
        out.append(f"{line.ljust(width)}{d}" if d else line)
    missing = [p for line, p in rows if p not in desc and _wants_desc(line)]
    stale = [k for k in desc if k not in {p for _, p in rows}]
    return "\n".join(out), missing, stale


def _wants_desc(line: str) -> bool:
    """Only flag top-level and second-level entries; deeper ones are self-evident."""
    return line.count(PIPE) + line.count(SPACE) <= 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="exit 1 if README is stale")
    ap.add_argument("--print", dest="show", action="store_true", help="print, write nothing")
    ap.add_argument("--depth", type=int, default=2, help="levels to descend (default 2)")
    ap.add_argument("--public", action="store_true", help="use the framework-only export allowlist")
    args = ap.parse_args()

    desc = json.loads(DESCRIPTIONS.read_text()) if DESCRIPTIONS.exists() else {}
    # keys starting with "_" are notes to the reader, not paths
    desc = {k.rstrip("/"): v for k, v in desc.items() if not k.startswith("_")}

    if args.public:
        sys.path.insert(0, str(ROOT / "tools/public-review"))
        from public_files import public_paths
        paths = public_paths(ROOT)
    else:
        paths = repo_paths()
    rows = flatten(nest(paths, args.depth))
    tree, missing, stale = render(rows, desc)
    block = f"{START}\n\n```markdown\n{tree}\n```\n\n{END}"

    for p in missing:
        print(f"MISSING description: {p}", file=sys.stderr)
    for p in stale:
        print(f"STALE description (path is gone): {p}", file=sys.stderr)

    if args.show:
        print(tree)
        return 1 if (missing or stale) else 0

    text = README.read_text()
    if START not in text or END not in text:
        print(f"error: {README.name} has no {START} / {END} markers", file=sys.stderr)
        return 2
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    new = head + block + tail

    if args.check:
        if new != text:
            print("error: README repository layout is out of date - "
                  "run tools/repo-tree/repo-tree.py", file=sys.stderr)
            return 1
        return 1 if (missing or stale) else 0

    if new != text:
        README.write_text(new)
        print(f"updated {README.relative_to(ROOT)}")
    else:
        print("README already up to date")
    return 1 if (missing or stale) else 0


if __name__ == "__main__":
    sys.exit(main())
