#!/usr/bin/env python3
"""Accept documentation tags only for the checked-out development-history commit."""

import argparse
from pathlib import Path
import re
import subprocess
import sys


TAG_FORMAT = re.compile(r"docs-v[0-9]+\.[0-9]+(?:\.[0-9]+)?(?:-[A-Za-z0-9]+(?:[.-][A-Za-z0-9]+)*)?")
ROOT = Path(__file__).resolve().parents[2]


def commit(root, ref, label):
    result = subprocess.run(
        ["git", "rev-parse", "--verify", "--end-of-options", ref + "^{commit}"],
        cwd=root, capture_output=True, text=True,
    )
    if result.returncode:
        raise ValueError(f"cannot resolve {label}; fetch complete branches and tags first")
    return result.stdout.strip()


def validate(root, tag):
    if not TAG_FORMAT.fullmatch(tag):
        raise ValueError("invalid tag format; use docs-v0.7, docs-v0.7.1 or docs-v0.7.1-rc.1")
    tagged = commit(root, "refs/tags/" + tag, "tag")
    head = commit(root, "HEAD", "checked-out commit")
    if head != tagged:
        raise ValueError("the checked-out commit does not match the documentation tag")
    development = commit(root, "refs/remotes/origin/development", "origin/development")
    ancestry = subprocess.run(
        ["git", "merge-base", "--is-ancestor", tagged, development],
        cwd=root, capture_output=True, text=True,
    )
    if ancestry.returncode:
        raise ValueError("tagged commit is not in development history, or ancestry cannot be verified")
    return tagged


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag", required=True)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        sha = validate(args.repo_root.resolve(), args.tag)
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(f"Verified {args.tag}: {sha} is the checked-out development-history commit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
