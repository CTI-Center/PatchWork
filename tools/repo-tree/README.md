# repo-tree

Regenerates the **Repository-layout** tree in the top-level [README](../../README.md) from the repository itself, so moving a folder and re-running is the whole update.

```bash
python3 tools/repo-tree/repo-tree.py              # rewrite README.md
python3 tools/repo-tree/repo-tree.py --check      # exit 1 if README is stale
python3 tools/repo-tree/repo-tree.py --print      # write nothing, show the tree
python3 tools/repo-tree/repo-tree.py --depth 3    # descend one level further
```

Python 3.9+, standard library only. Output is deterministic, so running it twice changes nothing the second time.

## Why-it-exists

The tree was hand-maintained and drifted. It listed `img/`, `report-types.md`, `samples/` and `templates/` long after those became `Resources/`, `Report-Types.md`, `Real-Examples/` and `Report-Templates/` — so a reader's first impression of the repo was a map of a repo that no longer existed.

## What-it-lists

What git would ship: tracked files, plus untracked files `.gitignore` does not exclude, **intersected with what is actually on disk**. Three consequences worth knowing:

- Ignored junk never appears — `.obsidian/`, `.claude/`, `.remember/`, `tools/gtidocs-mirror/.cache/`.
- A file that is staged but not yet committed **does** appear, which is what you want while a change is in progress.
- A folder renamed with a plain `mv` shows at its new path immediately, without waiting for the rename to be staged. `git ls-files --cached` alone would keep reporting the old one.

## Descriptions

Structure comes from the repository; the descriptions beside each entry cannot, so they live in [`descriptions.json`](descriptions.json), keyed by repo-relative path. An empty string means *listed, deliberately undescribed* — that is how `README.md` and `docs/` render with no trailing text.

**Renames are surfaced rather than silently swallowed.** The script reports:

- `MISSING description: <path>` —
	a new top- or second-level entry nobody has described yet.
- `STALE description (path is gone): <path>` —
	a description whose path no longer exists, which is what a rename looks like.

Either one makes it exit non-zero, so `--check` refuses a layout change that left the descriptions behind. Keys beginning with `_` are notes to the reader and are ignored.

## Wiring-it-into-something

Nothing runs it automatically. To have CI refuse a stale README, `--check` is the whole integration:

```yaml
- run: python3 tools/repo-tree/repo-tree.py --check
```

As a pre-commit hook, regenerate and re-stage instead:

```bash
python3 tools/repo-tree/repo-tree.py && git add README.md
```

## Markers

The script rewrites only the block between these two lines in `README.md`, and errors out if it cannot find them:

```markdown
<!-- repo-tree:start -->
<!-- repo-tree:end -->
```
