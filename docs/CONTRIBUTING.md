# Contributing

Patchwork is a draft, v0.7.2, prepared for community review. Several design choices in [Patchwork-CTI-Framework.md](Patchwork-CTI-Framework.md) were close calls, and the document says so wherever that's true. Disagreement is useful — it's the point of publishing a draft rather than sitting on it.

## Where-to-start

- **[2.4 Deliberate divergences](Patchwork-CTI-Framework.md#24-deliberate-divergences)** and **[2.5 Not adopted](Patchwork-CTI-Framework.md#25-not-adopted)** are the standing list of places the framework knowingly diverges from its source standards, and of constructs it hasn't adopted. It's the first place to look for open questions worth arguing about — the design register, not an afterthought.
- Anything marked as a close call in the text (search for "diverges", "not adopted", or the ⚠️ callouts) is fair game for a counter-proposal.
- Typos, broken links, unclear wording, and structural issues (this document not rendering somewhere it should, an inconsistent cross-reference) are always welcome as small, direct fixes.

## How-to-propose-something

- **Discuss first, for anything non-trivial.**
	The [Matrix room](<https://matrix.to/#/#cti-center:matrix.org>) is where design questions get talked through before they turn into an edit — attribution modelling and taxonomy design have enough surface area that a quick conversation usually saves a rewritten pull request later.
- **Open a GitHub issue or pull request** for anything concrete: a wording fix, a broken  reference, a new worked example, a proposed resolution to one of the [divergences](Patchwork-CTI-Framework.md#24-deliberate-divergences) or [gaps](Patchwork-CTI-Framework.md#25-not-adopted).
- If your change affects the technical model (new object types, new custom properties, a changed relationship), explain what it costs and what it buys — the document's own style is to weigh a decision against the alternatives it rejected (see [2.2](Patchwork-CTI-Framework.md#22-where-the-standards-disagree-and-who-wins) and [2.4](Patchwork-CTI-Framework.md#24-deliberate-divergences) for the pattern), not just assert the new behavior.

## Keeping-the-revision-history-honest

`Patchwork-CTI-Framework.md` ends with a **Revision history** list, running newest first. A substantive change to the framework should add a new entry at the **top**, in the form `- **<version>** · <date> — <one paragraph on what changed and why>`. Add to it, don't rewrite past entries. That list is itself an application of the framework's own principle: the record should accumulate, not quietly absorb its own history.

## Registering-a-member-or-mature-name

Use a pull request to update [Member-Registry.md](Member-Registry.md). Supply the member's stable lowercase token, exact STIX identity name and a contact approved for public collision/retraction traffic. A proposed token or name is not reserved until the registration is accepted. Maintainers record the UTC acceptance time; do not invent a registration date or include private contact details without consent.

Mature-name proposals must satisfy the collision checks in [4.7](Patchwork-CTI-Framework.md#47-mature-name-collisions-and-the-member-registry). Preserve earlier registrations and record corrections rather than silently removing their history.
