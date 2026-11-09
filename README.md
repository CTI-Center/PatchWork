![Patchwork CTI Framework logo](docs/Resources/PatchWork_logo-transparent-croped.png)

---
This framework turns analyst observations of adversary activity into actionable threat intelligence designed for STIX 2.1 exchange, **in a record where each judgement stays revisable without destroying the ones around it**. **Patchwork** is a threat-intelligence framework for tracking adversaries and sharing reports, composed from five foundational published standards — that patching-together is where the name comes from. A complementary [ENISA production-method layer](docs/ENISA-Alignment.md) supports reviewed annual threat-landscape reporting without changing the STIX model.

> **Status: draft v0.7.2, prepared for community review.**
> Several design choices were close calls and are marked as such in the text. Disagreement is useful — see [CONTRIBUTING.md](docs/CONTRIBUTING.md).

This project began as personal documentation. As it grew, I realized that each standard contributes a piece of the puzzle I was looking for. I'm grateful you're here to build on what I started, and I value your time. This draft is shared for public review, not as a final standard.

We are developing a threat-intelligence platform designed to be compatible with the Patchwork CTI framework. The platform is a work in progress, not a released or verified-conformant implementation. The framework remains platform-independent; this distribution contains its specification, templates, examples and tools, not the platform's internal development plans.

Please note: *the document structure was generated with AI assistance and may contain errors.* Public review is not a certification of an implementation's STIX conformance.

Maintainers: complete the [publication checklist](docs/Publication-Checklist.md) before making a distribution public. Passing the automated checks does not approve third-party redistribution or remove private material from the original repository's history.

## Table-of-contents

- [Repository-layout](#repository-layout)
- [Documentation-automation](#documentation-automation)
- [Authoring-conventions](#authoring-conventions)
  - [Headings-are-kebab-case](#headings-are-kebab-case)
  - [Obsidian-settings](#obsidian-settings)
- [Contributing](#contributing)
- [Licence](#licence)
- [Start-here](#start-here)
---

## Repository-layout

This is the framework-only public distribution. [`tools/public-review`](tools/public-review/README.md) prepares a clean copy and regenerates its layout using [`tools/repo-tree`](tools/repo-tree/README.md). Edit the descriptions in `tools/repo-tree/descriptions.json`, not here.

<!-- repo-tree:start -->

```markdown
├── .github/                        Automated public documentation checks
│   └── workflows/                  Documentation checks and tag-triggered builds
├── .gitignore                      Local caches and editor config kept out of the repo
├── docs/
│   ├── CONTRIBUTING.md             How to propose changes
│   ├── Easy-access/                Local copies of the source standards
│   ├── ENISA-Alignment.md          ENISA production-method alignment and annual-report profile
│   ├── Member-Registry.md          Member tokens and mature-name registrations
│   ├── Patchwork-CTI-Framework.md  The specification
│   ├── Publication-Checklist.md    Technical checks and owner approval before publication
│   ├── Real-Examples/              Worked report samples
│   ├── Report-Templates/           13 authored types, 3 retired skeletons and an annual-report profile
│   ├── Report-Types.md             Which report type to use, and when
│   ├── Resources/                  Diagrams and screenshots referenced by the docs
│   ├── Sectors.md                  Sector taxonomy
│   ├── Third-Party-Notices.md      Source attribution and redistribution review requirements
│   └── Vocabularies.md             Controlled value sets
├── LICENSE                         CC BY 4.0 — framework, templates, documentation
├── LICENSE-MIT                     MIT — scripts and tooling
├── README.md
└── tools/                          Scripts — see each tool's own README
    ├── check-links/                Validates the internal links in docs/
    ├── documentation/              Validates development tags for documentation builds
    ├── gtidocs-mirror/             Refreshes the GTI documentation snapshot
    ├── public-review/              Prepares a validated framework-only public copy
    └── repo-tree/                  Regenerates the tree on this page
```

<!-- repo-tree:end -->

## Documentation-automation

Push a `docs-v*` tag from `development` to run all offline tool tests, check the
complete Markdown collection and generate a validated documentation package.
Download the package and reports from the GitHub Actions run's **Artifacts**
section. The build verifies development ancestry and excludes transfer plans,
Git history and local backups; it does not create bot commits or publish a release.
See [the build instructions](tools/documentation/README.md) for tagging and local
verification commands.

## Authoring-conventions

This repo is written in [Obsidian](https://obsidian.md) and read on GitHub. The two resolve links differently, and a few conventions keep both usable. If you edit in a plain text editor, none of this needs configuring — just match the form you see in the files.

### Headings-are-kebab-case

Words in a heading are joined with hyphens. Section links use GitHub's generated anchor, not the literal heading:

```markdown
### 4.1-Three-tiers-of-object,-linked

[4.1](docs/Patchwork-CTI-Framework.md#41-three-tiers-of-object-linked)
```

Published section links use **GitHub's generated anchors**: lowercase heading text, spaces replaced by hyphens, punctuation and formatting removed, with numbered suffixes for duplicate headings. Literal underscores in vocabulary identifiers remain. For example, the heading above generates `#41-three-tiers-of-object-linked`, not Obsidian's literal `#4.1-three-tiers-of-object,-linked`.

When editing in Obsidian, preserve the published GitHub anchors rather than replacing them with literal-heading fragments. Check the public documents, including the reference copies, before publishing:

```sh
python3 tools/check-links/check-links.py --public --all
```


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

The [third-party notices](docs/Third-Party-Notices.md) identify the reference copies and the redistribution checks still required before publication. Attribution alone is not permission to redistribute a source.

`docs/Easy-access/` holds local copies of the sources this framework builds on, so its citations can be followed without leaving the repo. **Those copies keep their own licences and are not covered by the CC BY 4.0 above.** Each records its origin, though the form varies: the gtidocs mirror carries a `retrieved:` date, the Unit 42 and Mandiant copies a `created:` date, and the CISA and OASIS copies state their origin in prose rather than in frontmatter. In particular `docs/Easy-access/GTI/gtidocs/` is an *unofficial* snapshot of the [Google Threat Intelligence documentation hub](https://gtidocs.virustotal.com/docs/), © Google, mirrored for reference only and refreshed by [`tools/gtidocs-mirror`](tools/gtidocs-mirror/README.md) — check the live page linked at the foot of any archived file before relying on it.


## Start-here

| Document | What it covers |
| --- | --- |
| **[The framework](docs/Patchwork-CTI-Framework.md)** | The specification itself — adversary model, attribution ladder, classification, confidence, sharing and STIX serialisation. Has its own [table of contents](docs/Patchwork-CTI-Framework.md#table-of-contents) and [glossary](docs/Patchwork-CTI-Framework.md#glossary). |
| **[Report types](docs/Report-Types.md)** | Which report type to use when, a template for each of the 13 authored kinds, and the worked samples. |
| **[ENISA alignment](docs/ENISA-Alignment.md)** · **[Annual report template](docs/Report-Templates/annual-threat-landscape.md)** | Lifecycle adoption decisions and an annual `net-assessment` profile, traced to the [CTL methodology](docs/Easy-access/ENISA/enisa-ctl-methodology-2026.md) and [annual source structure](docs/Easy-access/ENISA/enisa-threat-landscape-2026-schema.md). |
| **[Vocabularies](docs/Vocabularies.md)** · **[Sectors](docs/Sectors.md)** | The controlled value sets. |
| **[Member registry](docs/Member-Registry.md)** | Token reservations and mature-name registrations; example tokens are not registrations. |
| **[Publication checklist](docs/Publication-Checklist.md)** | Validation, privacy, third-party rights and history-free publication gates. |
| **[Contributing](docs/CONTRIBUTING.md)** | How to propose a change, and what a good one looks like. |
