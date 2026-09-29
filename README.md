![381](docs/Resources/PatchWork_logo-transparent-croped.png)

---
This framework exists to turn analyst observations of adversary activity into an actionable, standards-conformant threat intelligence compatible with STIX 2.1, **in a record where each judgement stays revisable without destroying the ones around it**. **Patchwork** is a threat-intelligence framework for tracking adversaries and sharing reports, composed from five published standards — that patching-together is where the name comes from.

> **Status: draft v0.6, circulated for community review.**
> Several design choices were close calls and are marked as such in the text. Disagreement is useful — see  [CONTRIBUTING.md](docs/CONTRIBUTING.md).

This project began as personal documentation. As it grew, I realized that each standard contributes a piece of the puzzle I was looking for. I'm grateful you're here to build on what I started, and I value your time. This framework will be published once it reaches a version worth sharing.

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

Generated from the repository by [`tools/repo-tree`](tools/repo-tree/README.md) — move a folder, re-run it, and this block follows. Edit the descriptions in `tools/repo-tree/descriptions.json`, not here.

<!-- repo-tree:start -->

```markdown
├── .gitignore                      Local caches and editor config kept out of the repo
├── docs/
│   ├── CONTRIBUTING.md             How to propose changes
│   ├── Easy-access/                Local copies of the source standards
│   ├── OpenCTI-Transfer-Plan.md    GTI-aligned OpenCTI migration proposal
│   ├── Patchwork-CTI-Framework.md  The specification
│   ├── Real-Examples/              Worked report samples
│   ├── Report-Templates/           One skeleton per report type — 13 to author, 3 retired
│   ├── Report-Types.md             Which report type to use, and when
│   ├── Resources/                  Diagrams and screenshots referenced by the docs
│   ├── Sectors.md                  Sector taxonomy
│   └── Vocabularies.md             Controlled value sets
├── LICENSE                         CC BY 4.0 — framework, templates, documentation
├── LICENSE-MIT                     MIT — scripts and tooling
├── README.md
└── tools/                          Scripts — see each tool's own README
    ├── check-links/                Validates the internal links in docs/
    ├── gtidocs-mirror/             Refreshes the GTI documentation snapshot
    └── repo-tree/                  Regenerates the tree on this page
```

<!-- repo-tree:end -->

## Authoring-conventions

This repo is written in [Obsidian](https://obsidian.md) and read on GitHub. The two resolve links differently, and a few conventions keep both usable. If you edit in a plain text editor, none of this needs configuring — just match the form you see in the files.

### Headings-are-kebab-case

Words in a heading are joined with hyphens, and every cross-reference points at that text, lowercased:

```markdown
### 4.1-Three-tiers-of-object,-linked

[4.1](docs/Patchwork-CTI-Framework.md#4.1-three-tiers-of-object,-linked)
```

Obsidian matches an anchor against the literal heading text. GitHub matches a slug it builds by lowercasing the heading and deleting its punctuation. The two are not reconcilable — no single anchor string satisfies both — and this framework is authored in Obsidian day to day, so headings are written in the form Obsidian resolves. The cost is that section anchors do not scroll on github.com; the links still open the right file. Only whitespace becomes a hyphen. Everything else — dots, commas, em dashes, backticks — is preserved exactly.


### Obsidian-settings

Under **Settings → Files and links**, three settings matter. Without them, Obsidian rewrites links into forms GitHub cannot follow:

| Setting                                 | Value                     | Why                                                                                                                                                                                                                 |
| --------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Use `[[Wikilinks]]`**                 | **off**                   | Wikilinks are an Obsidian extension. GitHub renders `[[Some Note]]` as literal text, not a link.                                                                                                                    |
| **New link format**                     | **Relative path to file** | GitHub resolves a relative link against the file that contains it, not the repo root. "Path from vault folder" writes `docs/…` into a file that already lives in `docs/`, which GitHub then reads as `docs/docs/…`. |
| **Automatically update internal links** | **on**                    | Keeps references correct when a file is renamed or moved. Only safe in combination with the setting above.                                                                                                          |

Your vault root can be anywhere — the repo folder itself, or a parent directory. With relative links it makes no difference.

## Contributing

Design questions get talked through in the [Matrix room](https://matrix.to/#/#cti-center:matrix.org) before they turn into an edit — attribution modelling and taxonomy design have enough surface area that a conversation usually saves a rewritten pull request.

For anything concrete — a wording fix, a broken reference, a new worked example, a proposed resolution to one of the open divergences — open an issue or pull request. See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for what a well-formed change looks like.

## Licence

The framework, templates and documentation are **CC BY 4.0** — adopt and adapt freely, with attribution ([LICENSE](LICENSE)). Scripts and tooling are **MIT** ([LICENSE-MIT](LICENSE-MIT)).

Portions are adapted from the [CERT-EU Cyber Threat Intelligence Framework](https://cert.europa.eu/publications/threat-intelligence/cyber-threat-intelligence-framework/markdown), © CERT-EU, licensed CC BY 4.0.

`docs/Easy-access/` holds local copies of the sources this framework builds on, so its citations can be followed without leaving the repo. **Those copies keep their own licences and are not covered by the CC BY 4.0 above.** Each records its origin, though the form varies: the gtidocs mirror carries a `retrieved:` date, the Unit 42 and Mandiant copies a `created:` date, and the CISA and OASIS copies state their origin in prose rather than in frontmatter. In particular `docs/Easy-access/GTI/gtidocs/` is an *unofficial* snapshot of the [Google Threat Intelligence documentation hub](https://gtidocs.virustotal.com/docs/), © Google, mirrored for reference only and refreshed by [`tools/gtidocs-mirror`](tools/gtidocs-mirror/README.md) — check the live page linked at the foot of any archived file before relying on it.


## Start-here

| Document | What it covers |
| --- | --- |
| **[The framework](docs/Patchwork-CTI-Framework.md)** | The specification itself — adversary model, attribution ladder, classification, confidence, sharing and STIX serialisation. Has its own [table of contents](docs/Patchwork-CTI-Framework.md#table-of-contents) and [glossary](docs/Patchwork-CTI-Framework.md#glossary). |
| **[OpenCTI + GTI development roadmap](docs/OpenCTI-Transfer-Plan.md)** | Source-audited plan to reuse, configure and extend OpenCTI for GTI mappings, Patchwork serialization, analyst UI, security and production readiness. |
| **[Report types](docs/Report-Types.md)** | Which report type to use when, a template for each of the 13 authored kinds, and the worked samples. |
| **[Vocabularies](docs/Vocabularies.md)** · **[Sectors](docs/Sectors.md)** | The controlled value sets. |
| **[Contributing](docs/CONTRIBUTING.md)** | How to propose a change, and what a good one looks like. |
