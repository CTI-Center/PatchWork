# check-links

Validates the internal Markdown links in [`docs/`](../../docs) — that relative paths resolve, that section anchors match a real heading, and that no `[[wikilink]]` has slipped in.

```bash
python3 tools/check-links/check-links.py           # check the repo
python3 tools/check-links/check-links.py --all     # include docs/Easy-access/
python3 tools/check-links/check-links.py --quiet   # findings only, no summary
```

Python 3.9+, standard library only. Output is `path:line: message`, exit 1 on any finding, so wiring it into CI is just the run command.

## Why-not-an-off-the-shelf-checker

Anchors here point at Obsidian's literal-heading form, not GitHub's slug algorithm — `#4.1-three-tiers-of-object,-linked`, with commas and dots preserved. That is deliberate (README "Authoring-conventions"), and it is the whole problem: every standard Markdown link checker validates against GitHub slugs, so pointing one at this repo reports all 133 anchor links as broken and buries the two that are.

The cost of writing our own is that it is one more script to maintain, and it encodes a convention rather than a specification. The benefit is a clean run that means something.

## What-it-checks

- relative file links that do not resolve, images included, `%20`-decoded
- section anchors matching no heading in the target file
- wikilinks, which GitHub renders as literal text

Fenced code blocks and inline code spans are skipped, so documentation *about* links — the README's own wikilink example, the sample cross-reference — is not mistaken for a link.

Both CommonMark destination forms are read: bare `[x](target.md#anchor)`, and the angle form `[x](<target.md#anchor-(with-parens)>)` this repo uses whenever an anchor contains brackets.

## Underscores-are-literal

Heading text is lowercased and its whitespace collapsed to hyphens; everything else survives. Emphasis markers are the one exception, and `_` is deliberately **not** treated as one — it is literal in every STIX vocabulary name the headings carry, so `### 1.10-report_types_ov` has to keep it or no link can reach it.

A heading using `_emphasis_` still resolves: both readings are registered, which is permissive by design. The job is finding broken links, not adjudicating emphasis.

## Vendored-documentation

`docs/Easy-access/` is skipped unless you pass `--all`. It mirrors other people's documentation, and their breadcrumbs point out of the mirror root — roughly 1,300 findings against 28 authored files. They are not ours to fix, and left in they hide everything that is.

The skip is never silent: the summary line says how many files it passed over, so a clean run cannot be mistaken for "the whole repo is fine".

## What-it-cannot-catch

- prose cross-references, which are not links — a `Vocabularies §3.10` citation that should read `§1.10` is plain text
- a link that resolves but points at the wrong section
- anything about the *content* on the other end

## Wiring-it-into-something

Nothing runs it automatically. As a CI step:

```yaml
- run: python3 tools/check-links/check-links.py
```
