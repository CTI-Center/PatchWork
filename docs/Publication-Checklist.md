# Publication-checklist

Publication target: **Patchwork CTI Framework v0.7.2, a community-review draft**.
Preparing a package is not making a repository public, releasing the compatible
platform or certifying an implementation. Keep those distinctions in the
announcement and release notes.

## Technical-checks

- [ ] README, framework frontmatter and contribution instructions identify the
  same review version, and the framework revision history records the changes.
- [ ] Every tool's offline tests pass, the public README tree is current, and
  all source Markdown and public-export Markdown pass local link validation.
- [ ] A new history-free export is generated and the actual exported copy is
  checked, including its assets, registry, notices and publication instructions.
- [ ] OpenCTI-transfer plans, other internal plans, Git metadata, recovery
  backups, caches, credentials and application prototypes are absent from the
  copy intended for publication.
- [ ] New provisional designations use allocation years, for example
  `CL-UNK-2026-0001` locally or `cc-CL-UNK-2026-0001` in shared STIX names.
  Existing identifiers are not silently migrated or renumbered.

The commands are in [documentation automation](../tools/documentation/README.md)
and [public-review export](../tools/public-review/README.md). Always use a new
output directory. Only package that export, never the entire `dist/` directory.

The automated checks validate local navigation and export safety, not every
external website, the truth of intelligence assessments, an implementation's
STIX conformance or third-party rights. Template blanks and labelled synthetic
fixtures are intentional; JSON skeletons must be completed before exchange.

## Owner-approval

- [ ] Approve redistribution of every included third-party source and asset,
  following [Third-Party-Notices.md](Third-Party-Notices.md). The current notices
  do not record permission for all vendor reference copies; this gate remains
  open until the owner records applicable terms or permission.
- [ ] Review examples and images for private case details, PII and material
  subject to handling restrictions. Approve the publication of actual contacts
  before adding them to [the member registry](Member-Registry.md).
- [ ] Choose the new public repository's owner and name, and approve its
  description, licence presentation and community-review announcement.
- [ ] Check the chosen public destination's links while signed out, including
  any links used by published STIX extension definitions or downstream tools.

## Publish-without-private-history

Create a **new repository from only the validated export**, with fresh Git
history. Keep the original repository and its `docs/opencti-transfer` branch
private. A branch cannot be private inside a public repository, and removing a
file from its latest commit does not remove its older versions or other refs.
Do not push the original repository's branches, tags, stash or recovery bundle
to the new public destination. Follow
[Publish-safely](../tools/public-review/README.md#publish-safely).

If the new public repository will run the tag-build workflow, create its own
`development` branch from the clean public history and push a fresh `docs-v*`
tag reachable from that branch. Do not copy a tag from the original history.
Tags label builds; they do not change version fields or create GitHub releases.

GitHub artifact uploads can be blocked by storage quota even when validation
and package generation pass. Resolve that separately or use the validated
local export; do not claim a downloadable artifact exists when upload failed.
Nothing in this checklist authorises automatic billing changes or deletion of
other repositories' artifacts.
