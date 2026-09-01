# Contributing

Patchwork is a draft, v0.1, circulated for community review. Several design choices in
[Patchwork-CTI-Framework.md](Patchwork-CTI-Framework.md) were close calls, and the document says so wherever that's true. Disagreement is useful — it's the point of publishing a draft rather than sitting on it.

## Where-to-start

- **[2.4 Deliberate divergences](Patchwork-CTI-Framework.md#2.4-deliberate-divergences)** and
  **[2.5 Not adopted](Patchwork-CTI-Framework.md#2.5-not-adopted)** are the
  standing list of places the framework knowingly diverges from its source standards, and of
  constructs it hasn't adopted. It's the first place to look for open questions worth arguing
  about — the design register, not an afterthought.
- Anything marked as a close call in the text (search for "diverges", "not adopted", or the
  ⚠️ callouts) is fair game for a counter-proposal.
- Typos, broken links, unclear wording, and structural issues (this document not rendering
  somewhere it should, an inconsistent cross-reference) are always welcome as small, direct
  fixes.

## How-to-propose-something

- **Discuss first, for anything non-trivial.** The [Matrix room](<https://matrix.to/#/#cti-center:matrix.org>) is where design questions get talked through before they turn into an edit — attribution modelling and taxonomy design have enough surface area that a quick conversation usually saves a rewritten pull request later.
- **Open a GitHub issue or pull request** for anything concrete: a wording fix, a broken  reference, a new worked example, a proposed resolution to one of the [divergences](Patchwork-CTI-Framework.md#2.4-deliberate-divergences) or [gaps](Patchwork-CTI-Framework.md#2.5-not-adopted).
- If your change affects the technical model (new object types, new custom properties, a changed relationship), explain what it costs and what it buys — the document's own style is to weigh a decision against the alternatives it rejected (see [2.2](Patchwork-CTI-Framework.md#2.2-where-the-standards-disagree,-and-who-wins) and [2.4](Patchwork-CTI-Framework.md#2.4-deliberate-divergences) for the pattern), not just assert the new behavior.

## Keeping-the-revision-history-honest

`Patchwork-CTI-Framework.md` ends with a **Revision history** table. A substantive change to the
framework should add a new row there (version, date, one paragraph on what changed and why) —
append to it, don't rewrite past entries. That table is itself an application of the framework's
own principle: the record should accumulate, not quietly absorb its own history.