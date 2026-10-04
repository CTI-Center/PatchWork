# check-links

Validates local Markdown links using **GitHub's generated heading anchors**, including relative file/image paths, reference-link destinations, HTML links inside Markdown, duplicate headings and explicit HTML anchors. Wikilinks are reported because GitHub does not render them as links.

```bash
python3 tools/check-links/check-links.py --public --all  # every public Markdown file
python3 tools/check-links/check-links.py --public        # authored public docs only
python3 tools/check-links/check-links.py --all            # all Git-shippable Markdown
python3 -m unittest discover -s tools/check-links -p 'test_*.py'
```

Python 3.9+, standard library only. Output is `path:line: message`, exit 1 on any finding, so wiring it into CI is just the run command.

## GitHub-anchors

GitHub lowercases rendered heading text, replaces spaces with hyphens, removes punctuation and formatting, and numbers duplicate anchors. For example, `4.1-Three-tiers-of-object,-linked` generates `#41-three-tiers-of-object-linked`. The old Obsidian-only fragment containing dots and commas is rejected.

In a Git checkout, only tracked and non-ignored untracked Markdown files are checked. In a clean export, the filesystem is checked instead. Local caches and graph output are excluded in either case. `--public` uses the allowlist from [`tools/public-review`](../public-review/README.md) and rejects links to files outside that distribution, even when the private file still exists locally.

## What-it-checks

- relative file links that do not resolve, images included, `%20`-decoded
- section anchors matching no GitHub-generated heading or explicit HTML anchor in the target file
- reference-style link destinations
- wikilinks, which GitHub renders as literal text

Fenced code blocks and inline code spans are skipped, so documentation *about* links — the README's own wikilink example, the sample cross-reference — is not mistaken for a link.

Both CommonMark destination forms are read: bare `[x](target.md#anchor)`, and the angle form `[x](<target.md#anchor-(with-parens)>)` this repo uses whenever an anchor contains brackets.

## Underscores-are-literal

Inline code contributes its visible text to the anchor. Literal underscores in identifiers are retained: `### 1.10-report_types_ov` generates `#110-report_types_ov`. Underscores used as emphasis delimiters are removed with the formatting.

A heading using `_emphasis_` generates `#emphasis`; the obsolete literal-heading variant is not accepted.

## Vendored-documentation

`docs/Easy-access/` is skipped unless you pass `--all`. **Use `--public --all` for release verification**, so reference-copy navigation is included rather than silently assumed to work.

The skip is never silent: the summary line says how many files it passed over, so a clean run cannot be mistaken for "the whole repo is fine".

## What-it-cannot-catch

- prose cross-references, which are not links — a `Vocabularies §3.10` citation that should read `§1.10` is plain text
- a link that resolves but points at the wrong section
- anything about the *content* on the other end
- remote HTTP availability or redistribution rights
- complete CommonMark rendering or links in standalone HTML applications

## Wiring-it-into-something

Nothing runs it automatically. As a CI step:

```yaml
- run: python3 tools/check-links/check-links.py --public --all
```
