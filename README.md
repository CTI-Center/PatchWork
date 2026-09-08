This framework exists to turn analyst observations of adversary activity into an actionable,
standards-conformant threat intelligence compatible with STIX 2.1, **in a record where each
judgement stays revisable without destroying the ones around it**. **Patchwork** is a threat-intelligence framework for tracking adversaries and sharing reports, currently composed from Five published standards that patching-together is where the name comes from. 

> **Status: draft v0.1, circulated for community review.** Several design choices were close
> calls and are marked as such in the text. Disagreement is useful — see
> [CONTRIBUTING.md](docs/CONTRIBUTING.md).

This project began as personal documentation. As it grew, I realized that each standard
contributes a piece of the puzzle I was looking for. I'm grateful you're here to build on what I
started, and I value your time. This framework will be published once it reaches a version worth
sharing.

Please note: *the document structure was generated with AI assistance and may contain errors.*

## Table-of-contents

- [Repository-layout](#repository-layout)
- [Authoring-conventions](#authoring-conventions)
  - [Headings-are-kebab-case](#headings-are-kebab-case)
  - [Obsidian-settings](#obsidian-settings)
- [Contributing](#contributing)
- [Licence](#licence)
- [Start-here](#start-here)
---

## Repository-layout

```markdown
├── docs
│   ├── CONTRIBUTING.md			How to propose changes
│   ├── img/				Diagrams referenced by the docs
│   ├── Patchwork-CTI-Framework.md	The specification
│   ├── report-types.md			which report type to use, and when
│   ├── samples/			Real world report samples
│   ├── Sectors.md			Sector taxonomy
│   ├── templates/			15 per-type skeletons, one per report type
│   └── Vocabularies.md			Controlled value sets
├── scripts/
│   └── check-links.py			Internal-link and anchor validation
└── README.md
```

## Authoring-conventions

This repo is written in [Obsidian](https://obsidian.md) and read on GitHub. The two resolve links differently, and a few conventions keep both usable. If you edit in a plain text editor, none of this needs configuring — just match the form you see in the files.

### Headings-are-kebab-case

Words in a heading are joined with hyphens, and every cross-reference points at that text,
lowercased:

```markdown
### 4.1-Three-tiers-of-object,-linked

[4.1](docs/Patchwork-CTI-Framework.md#4.1-three-tiers-of-object,-linked)
```

Obsidian matches an anchor against the literal heading text. GitHub matches a slug it builds by
lowercasing the heading and deleting its punctuation. The two are not reconcilable — no single
anchor string satisfies both — and this framework is authored in Obsidian day to day, so
headings are written in the form Obsidian resolves. The cost is that section anchors do not
scroll on github.com; the links still open the right file.
Only whitespace becomes a hyphen. Everything else — dots, commas, em dashes, backticks — is
preserved exactly.


### Obsidian-settings

Under **Settings → Files and links**, three settings matter. Without them, Obsidian rewrites
links into forms GitHub cannot follow:

| Setting                                 | Value                     | Why                                                                                                                                                                                                                 |
| --------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Use `[[Wikilinks]]`**                 | **off**                   | Wikilinks are an Obsidian extension. GitHub renders `[[Some Note]]` as literal text, not a link.                                                                                                                    |
| **New link format**                     | **Relative path to file** | GitHub resolves a relative link against the file that contains it, not the repo root. "Path from vault folder" writes `docs/…` into a file that already lives in `docs/`, which GitHub then reads as `docs/docs/…`. |
| **Automatically update internal links** | **on**                    | Keeps references correct when a file is renamed or moved. Only safe in combination with the setting above.                                                                                                          |

Your vault root can be anywhere — the repo folder itself, or a parent directory. With relative
links it makes no difference.

## Contributing

Design questions get talked through in the [Matrix room](https://matrix.to/#/#cti-center:matrix.org)
before they turn into an edit — attribution modelling and taxonomy design have enough surface
area that a conversation usually saves a rewritten pull request.

For anything concrete — a wording fix, a broken reference, a new worked example, a proposed
resolution to one of the open divergences — open an issue or pull request. See
[CONTRIBUTING.md](docs/CONTRIBUTING.md) for what a well-formed change looks like.

## Licence

The framework, templates and documentation are **CC BY 4.0** — adopt and adapt freely, with
attribution. Scripts and tooling are **MIT**. The licence texts are not yet committed to the
repo.

Portions are adapted from the [CERT-EU Cyber Threat Intelligence Framework](https://cert.europa.eu/publications/threat-intelligence/cyber-threat-intelligence-framework/markdown),
© CERT-EU, licensed CC BY 4.0.


## Start-here

| Document | What it covers |
| --- | --- |
| **[The framework](docs/Patchwork-CTI-Framework.md)** | The specification itself — adversary model, attribution ladder, classification, confidence, sharing and STIX serialisation. Has its own [table of contents](docs/Patchwork-CTI-Framework.md#table-of-contents) and [glossary](docs/Patchwork-CTI-Framework.md#glossary). |
| **[Report types](docs/report-types.md)** | Which report type to use when, a template for each of the 15 hand-authored kinds, and the worked samples. |
| **[Vocabularies](docs/Vocabularies.md)** · **[Sectors](docs/Sectors.md)** | The controlled value sets. |
| **[Contributing](docs/CONTRIBUTING.md)** | How to propose a change, and what a good one looks like. |
