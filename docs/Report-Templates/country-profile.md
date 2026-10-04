> [!NOTE] About this template — Country Profile (`country-profile`)
> **Use this when:**
> The threat landscape for one country over a period.
>
> **Use something else if:**
> focused on one sector — use `industry`.
>
> Picker: [Report-Types](../Report-Types.md) · Controlled values: [Vocabularies](../Vocabularies.md) · Framework: [Patchwork-CTI-Framework](../Patchwork-CTI-Framework.md)
>
> These `[!tip]` callouts are guidance, not content — delete each one as you fill its section.

# <Title>-—-Country-Profile

> ⚠️ **This type may also be generated automatically in your environment.** Where a member's own tooling emits `country-profile` reports from incident data, reports deduplicate on **name + published** ([9.2](../Patchwork-CTI-Framework.md#92-identity-and-merge-rules)) — so a hand-written report that reuses the generated title pattern (something of the shape `<member>-<Country> cyber threat landscape <year>`) will **merge into and overwrite** the generated one. Give yours a distinct title. This is a statement about *your own* environment, not about any upstream platform ([Report-Types](<../Report-Types.md#before-you-write-four-things-that-bite>)).

## Report-metadata

| Field | Value | Hint |
| ----- | ----- | ---- |
| Report Type | `country-profile` | Fixed for this template — emitted as `report_types: ["country-profile"]` |
| Title | | Prefix with **your member namespace token** (§4.2) — e.g. `acme-`. Pick it once; it is stable forever |
| Published | | **Stable anchor date.** Dedup is name + published (§9.2), so a date that changes on revision forks a new report |
| TLP | | `Clear` \| `Green` \| `Amber` \| `Amber+Strict` \| `Red` (TLP 2.0, §8.1). `Clear` was called `White` and keeps the same STIX id; `Amber+Strict` withdraws the client carve-out and is dual-marked with `Amber` |
| Author | | **Your member identity** — becomes `created_by_ref` (§8.2) |
| Source Reliability | | Admiralty `A`–`F` |
| Info Credibility | | Admiralty `1`–`6` |
| Threat level | | `High` \| `Medium` \| `Low` (§3.4) — urgency and proximity, **not** a confidence grade. Emitted as `threat_level` in the Patchwork extension ([9.3](../Patchwork-CTI-Framework.md#93-classification-properties)) |
| Threat domain | | **This report's scope claim rests on this field.** `Constituency` \| `National` \| `Regional` \| `Partner` \| `World` (§3.3). Highest applicable rung wins. Emitted as `threat_domain` in the Patchwork extension ([9.3](../Patchwork-CTI-Framework.md#93-classification-properties)) |
| Activity category | | One or more of the nine categories in §5.2 — emitted as `activity_category` in the Patchwork extension ([9.3](../Patchwork-CTI-Framework.md#93-classification-properties)) |
| Observed date | | **Required where this report records an incident.** When the activity was *observed*, not when this was written. It contributes to the incident's identity key (§9.2), so a wrong date forks a duplicate rather than updating. Emitted as `observed_date` in the Patchwork extension ([9.3](../Patchwork-CTI-Framework.md#93-classification-properties)) |

## Key-judgments

> [!TIP] What goes here
> 3-5 bullets. The part a reader acts on — put it first, not at the end. State confidence, and say plainly what you cannot support.

- - -

## Landscape

> [!TIP] What goes here
> The overall picture for the period.



## Actors-active

| Actor | Tier | Activity level |
| --- | --- | --- |
|  |  |  |


## Sectors-targeted

| Sector | Incidents | Notes |
| --- | --- | --- |
|  |  |  |


## Year-over-year

> [!TIP] What goes here
> What changed versus the previous period, and what it implies.



## Objects-referenced

> [!TIP] What goes here
> What belongs in this report's `object_refs` so the narrative and the STIX container agree. For `country-profile`: incidents in scope, the intrusion-sets behind them, locations and sectors.

- -


## Sources

> [!TIP] What goes here
> External references: vendor reporting, news, internal case ids.

| Source | Reference / URL | Reliability |
| --- | --- | --- |
|  |  |  |
