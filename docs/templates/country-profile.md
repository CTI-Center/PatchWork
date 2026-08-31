> [!NOTE] About this template — Country Profile (`country-profile`)
> **Use this when:** The threat landscape for one country over a period.
>
> **Use something else if:** focused on one sector — use `industry`.
>
> Picker: [report-types](../report-types.md) · Controlled values: [Vocabularies](../Vocabularies.md) · Framework: [Patchwork-CTI-Framework](../Patchwork-CTI-Framework.md)
>
> These `[!tip]` callouts are guidance, not content — delete each one as you fill its section.

# <Title>-—-Country-Profile

> ⚠️ **This type is also generated automatically.** `cti-aggregate.js` already
> emits `country-profile` reports from the incident data, and OpenCTI deduplicates
> reports on **name + published**. If you title this report using the generated
> pattern — `cc-Iran cyber threat landscape <year>` — it will **merge into and
> overwrite** the automatic one. Give your hand-written report a distinct title.

## Report-metadata

| Field | Value | Hint |
| ----- | ----- | ---- |
| Report Type | `country-profile` | Fixed for this template — emitted as `report_types: ["country-profile"]` |
| Title | | Prefix with **your member namespace token** (§4.2) — e.g. `acme-`. Pick it once; it is stable forever |
| Published | | **Stable anchor date.** Dedup is name + published (§9.2), so a date that changes on revision forks a new report |
| TLP | | `White` \| `Green` \| `Amber` \| `Red` |
| Author | | **Your member identity** — becomes `created_by_ref` (§8.2) |
| Source Reliability | | Admiralty `A`–`F` |
| Info Credibility | | Admiralty `1`–`6` |
| Threat level | | `High` \| `Medium` \| `Low` (§3.4) — urgency and proximity, **not** a confidence grade. Emitted as `x_threat_level` |
| Threat domain | | **This report's scope claim rests on this field.** `Constituency` \| `National` \| `Regional` \| `Partner` \| `World` (§3.3). Highest applicable rung wins. Emitted as `x_threat_domain` |
| Activity category | | One or more of the nine categories in §5.2 — emitted as `x_activity_category` |

## Key-judgments

> [!TIP] What goes here
> 3-5 bullets. The part a reader acts on — put it first, not at the end.
> State confidence, and say plainly what you cannot support.

-
-
-

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
> What belongs in this report's `object_refs` so the narrative and the STIX
> container agree. For `country-profile`: incidents in scope, the intrusion-sets behind them, locations and sectors.

-
-


## Sources

> [!TIP] What goes here
> External references: vendor reporting, news, internal case ids.

| Source | Reference / URL | Reliability |
| --- | --- | --- |
|  |  |  |

