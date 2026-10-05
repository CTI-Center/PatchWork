# Documentation-automation

The [tagged documentation workflow](../../.github/workflows/documentation-tag.yml)
checks the complete committed document collection and generates a validated,
framework-only package. It runs when a `docs-v*` tag is pushed. Regular pushes and
pull requests also run the offline tool tests and public-document checks.

## Trigger-a-build

Create a new tag from a clean, updated `development` checkout:

```sh
git switch development
git pull --ff-only origin development
git push origin development
git tag -a docs-v0.7.1 -m "Build Patchwork documentation 0.7.1"
git push origin docs-v0.7.1
```

Use a unique build label each time, for example `docs-v0.7.2` or
`docs-v0.8.0-rc.1`. Tags do not change document version fields automatically and
are not GitHub releases. Do not move an existing tag to a different commit.
The tagged commit must already be pushed to `development` and contain this
workflow; tags on older commits without the workflow cannot start a build.

Git tags have no branch ownership. `check_tag.py` therefore verifies the tag
format, resolves lightweight and annotated tags, requires the checked-out commit
to match, and checks that it is reachable from `origin/development`. A tag on a
transfer-only or other divergent commit fails before building. A historical
development commit remains valid if development has advanced since tagging.

```sh
python3 tools/documentation/check_tag.py --tag docs-v0.7.1
python3 -m unittest discover -s tools/documentation -p 'test_*.py'
```

## Checks-and-generated-files

The workflow:

1. Compiles the Python tools, runs each tool directory's tests, and smoke-tests
   the command-line entry points.
2. Verifies the public README layout and every Git-shippable Markdown document,
   including the vendored references, using GitHub-compatible local links.
3. Separately checks the public export allowlist so links cannot depend on files
   that would be absent from the package.
4. Generates the complete Markdown/assets/tools snapshot with
   [public-review](../public-review/README.md), including its regenerated README
   layout, and verifies the actual exported copy.
5. Uploads `patchwork-documentation-<tag>-<attempt>` and diagnostic reports to the workflow
   run's **Artifacts** section, retained for 30 days. Failed checks produce no
   new documentation artifact; reports are uploaded when available. Separate
   attempt numbers preserve artifacts when rerunning a tag's workflow.

Only the explicit framework allowlist is packaged. OpenCTI-transfer plans,
internal design files, Git history, local backups and caches are excluded. No
bot commits, branch merges, repository publication or releases are performed.
This generates a navigable source-document package, not PDF or rendered HTML.

The GTI mirror's conversion tests and CLI run offline. A live snapshot refresh
is deliberately separate: it changes roughly a thousand files and depends on
upstream availability. Refresh it manually, review and commit its changes, then
tag that development snapshot. External HTTP availability, semantic accuracy and
third-party redistribution rights are not validated by these checks.

## Local-verification

```sh
for tool in tools/*/; do
  python3 -m unittest discover -s "$tool" -p 'test_*.py' || exit 1
done
python3 tools/repo-tree/repo-tree.py --public --check
python3 tools/check-links/check-links.py --all
python3 tools/check-links/check-links.py --public --all
python3 tools/public-review/prepare-public.py --output dist/documentation-local
```

The output directory must be new. Never upload the original checkout or the
entire `dist/` directory; it may contain local recovery backups.

## Artifact-storage-limits

GitHub can reject uploads when the account's Actions storage quota is exhausted,
even when every test, link check and generation step succeeded. The workflow
keeps this failure visible rather than claiming a downloadable package exists.
Free appropriate Actions artifact storage or adjust the account's storage limit,
then rerun or push a new build tag. GitHub reports that quota usage can take
6–12 hours to recalculate. No artifact deletion or billing changes are automated.
