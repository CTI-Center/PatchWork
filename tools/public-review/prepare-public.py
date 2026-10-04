#!/usr/bin/env python3
"""Prepare a validated framework-only snapshot without copying Git history."""

import argparse
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile

from public_files import public_paths


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def load_tool(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def prepare(source, destination):
    if destination.exists():
        raise ValueError(f"destination already exists; choose a new directory: {destination}")
    if destination == source or destination in source.parents:
        raise ValueError("destination cannot be the source directory or its ancestor")
    if source in destination.parents and source / "dist" not in destination.parents:
        raise ValueError("an output inside the source must be under dist/")
    files = public_paths(source)
    required = {"README.md", "LICENSE", "LICENSE-MIT", "docs/Patchwork-CTI-Framework.md"}
    missing = required - set(files)
    if missing:
        raise ValueError("missing required public files: " + ", ".join(sorted(missing)))
    checker = load_tool("check_links", ROOT / "tools/check-links/check-links.py")
    tree = load_tool("repo_tree", ROOT / "tools/repo-tree/repo-tree.py")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".patchwork-public-", dir=destination.parent) as temp:
        stage = Path(temp)
        for relative in files:
            target = stage / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source / relative, target)
        # Check the actual copy, including source mirrors: no private target can
        # accidentally pass just because it exists in the working repository.
        problems = []
        cache = {}
        for relative in files:
            if relative.endswith(".md"):
                problems.extend(checker.check_file(stage / relative, stage, cache))
        if problems:
            for path, line, message in problems:
                print(f"{path}:{line}: {message}", file=sys.stderr)
            raise ValueError(f"public link validation failed: {len(problems)} problem(s); no export created")
        readme = stage / "README.md"
        text = readme.read_text(encoding="utf-8")
        if tree.START not in text or tree.END not in text:
            raise ValueError("public README needs repository-tree markers")
        descriptions_path = stage / "tools/repo-tree/descriptions.json"
        descriptions = json.loads(descriptions_path.read_text()) if descriptions_path.exists() else {}
        descriptions = {k.rstrip("/"): v for k, v in descriptions.items() if not k.startswith("_")}
        rows = tree.flatten(tree.nest(files, 2))
        rendered, missing_descriptions, stale = tree.render(rows, descriptions)
        if descriptions_path.exists() and (missing_descriptions or stale):
            raise ValueError(f"public tree descriptions need updating: missing={missing_descriptions}, stale={stale}")
        before, rest = text.split(tree.START, 1)
        _, after = rest.split(tree.END, 1)
        readme.write_text(f"{before}{tree.START}\n\n```markdown\n{rendered}\n```\n\n{tree.END}{after}", encoding="utf-8")
        shutil.move(str(stage), str(destination))
    print(f"Public snapshot: {destination}")
    print(f"{len(files)} files; all internal Markdown links checked; no Git history copied.")
    print("Publish this snapshot as a NEW repository. Do not change the original repository's visibility.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True, help="new destination; never overwritten")
    args = parser.parse_args()
    try:
        prepare(args.source.resolve(), args.output.resolve())
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
