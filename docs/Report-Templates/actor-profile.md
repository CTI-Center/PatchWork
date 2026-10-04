> [!NOTE] About this template — Actor Profile (`actor-profile`)
> **Use this when:**
> A standing profile of one adversary.
>
> **Use something else if:**
> the subject is activity whose relevance has become elevated — use `threat-activity`. One operation with a start and an end is a `campaign` **object**, not a report type ([9.4](../Patchwork-CTI-Framework.md#94-curation-layer)).
>
> Picker: [Report-Types](../Report-Types.md) · Controlled values: [Vocabularies](../Vocabularies.md) · Framework: [Patchwork-CTI-Framework](../Patchwork-CTI-Framework.md)
>
> These `[!tip]` callouts are guidance, not content — delete each one as you fill its section.

# <Title>-—-Actor-Profile

> ⚠️ **This type may also be generated automatically in your environment.** Where a member's own tooling emits `actor-profile` reports from incident data, reports deduplicate on **name + published** ([9.2](../Patchwork-CTI-Framework.md#92-identity-and-merge-rules)) — so a hand-written report that reuses the generated title pattern (something of the shape `<member>-<Actor> (<handle>) — activity profile`) will **merge into and overwrite** the generated one. Give yours a distinct title. This is a statement about *your own* environment, not about any upstream platform ([Report-Types](<../Report-Types.md#before-you-write-four-things-that-bite>)).

## Report-metadata

| Field | Value | Hint |
| ----- | ----- | ---- |
| Report Type | `actor-profile` | Fixed for this template — emitted as `report_types: ["actor-profile"]` |
| Title | | Prefix with **your member namespace token** (§4.2) — e.g. `acme-`. Pick it once; it is stable forever |
| Published | | **Stable anchor date.** Dedup is name + published (§9.2), so a date that changes on revision forks a new report |
| TLP | | `Clear` \| `Green` \| `Amber` \| `Amber+Strict` \| `Red` (TLP 2.0, §8.1). `Clear` was called `White` and keeps the same STIX id; `Amber+Strict` withdraws the client carve-out and is dual-marked with `Amber` |
| Author | | **Your member identity** — becomes `created_by_ref` (§8.2) |
| Source Reliability | | Admiralty `A`–`F` |
| Info Credibility | | Admiralty `1`–`6` |
| Threat level | | `High` \| `Medium` \| `Low` (§3.4) — urgency and proximity, **not** a confidence grade. Emitted as `threat_level` in the Patchwork extension ([9.3](../Patchwork-CTI-Framework.md#93-classification-properties)) |
| Threat domain | | `Constituency` \| `National` \| `Regional` \| `Partner` \| `World` (§3.3). Highest applicable rung wins. Emitted as `threat_domain` in the Patchwork extension ([9.3](../Patchwork-CTI-Framework.md#93-classification-properties)) |
| Activity category | | One or more of the nine categories in §5.2 — emitted as `activity_category` in the Patchwork extension ([9.3](../Patchwork-CTI-Framework.md#93-classification-properties)) |
| Observed date | | **Required where this report records an incident.** When the activity was *observed*, not when this was written. It contributes to the incident's identity key (§9.2), so a wrong date forks a duplicate rather than updating. Emitted as `observed_date` in the Patchwork extension ([9.3](../Patchwork-CTI-Framework.md#93-classification-properties)) |

## Key-judgments

> [!TIP] What goes here
> 3-5 bullets. The part a reader acts on — put it first, not at the end. State confidence, and say plainly what you cannot support.

- - -

## Designation-and-aliases

> [!TIP] What goes here
> For a new provisional intrusion-set, use `<member>-CL-<MOT>-YYYY-####` (Cluster) or `<member>-TGR-<MOT>-YYYY-####` (Temporary) as the name. `YYYY` is the code-allocation year, not the activity year; mature adversaries retain their freely chosen names. Keep handles/personas on separate `threat-actor` objects, linked with `attributed-to`, not in the intrusion-set's aliases. See [4.3](../Patchwork-CTI-Framework.md#43-attribution-codes-are-assigned-once-and-never-reused), [4.4](../Patchwork-CTI-Framework.md#44-personas-are-objects-not-aliases) and [9.3](../Patchwork-CTI-Framework.md#93-classification-properties).

| Designation | Aliases | Tier |
| --- | --- | --- |
|  |  |  |


## Motivation-and-tier

> [!TIP] What goes here
> Tier: `Cluster` · `Temporary` · `Mature` ([4.1](<../Patchwork-CTI-Framework.md#41-three-tiers-of-object-linked>)) — the framework fixes no numeric confidence per tier; see the promotion evidence checklist at [4.6](../Patchwork-CTI-Framework.md#46-minimum-evidence-for-promotion). Motivation per [5.1](../Patchwork-CTI-Framework.md#51-the-analyst-facing-motivation-classes) and intent per [5.3](../Patchwork-CTI-Framework.md#53-intent).



## Targeting

> [!TIP] What goes here
> Sectors, countries, victim profile.



## TTPs

> [!TIP] What goes here
> Bare ATT&CK IDs.

| ATT&CK ID | Technique | Notes |
| --- | --- | --- |
|  |  |  |


## Assessment

> [!TIP] What goes here
> Your analytic judgment and its confidence. Say what you cannot support.



## Objects-referenced

> [!TIP] What goes here
> What belongs in this report's `object_refs` so the narrative and the STIX container agree. For `actor-profile`: the intrusion-set, its incidents, campaigns, attack-patterns, victims and sectors.

- -


## Sources

> [!TIP] What goes here
> External references: vendor reporting, news, internal case ids.

| Source | Reference / URL | Reliability |
| --- | --- | --- |
|  |  |  |
