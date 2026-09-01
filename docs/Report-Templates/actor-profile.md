> [!NOTE] About this template — Actor Profile (`actor-profile`)
> **Use this when:** A standing profile of one adversary.
>
> **Use something else if:** the subject is activity whose relevance has become elevated — use `threat-activity`. One operation with a start and an end is a `campaign` **object**, not a report type ([9.4](../Patchwork-CTI-Framework.md#9.4-curation-layer)).
>
> Picker: [Report-Types](../Report-Types.md) · Controlled values: [Vocabularies](../Vocabularies.md) · Framework: [Patchwork-CTI-Framework](../Patchwork-CTI-Framework.md)
>
> These `[!tip]` callouts are guidance, not content — delete each one as you fill its section.

# <Title>-—-Actor-Profile

> ⚠️ **This type is also generated automatically.** `cti-aggregate.js` already
> emits `actor-profile` reports from the incident data, and OpenCTI deduplicates
> reports on **name + published**. If you title this report using the generated
> pattern — `cc-<Actor> (<handle>) — activity profile` — it will **merge into and
> overwrite** the automatic one. Give your hand-written report a distinct title.

## Report-metadata

| Field | Value | Hint |
| ----- | ----- | ---- |
| Report Type | `actor-profile` | Fixed for this template — emitted as `report_types: ["actor-profile"]` |
| Title | | Prefix with **your member namespace token** (§4.2) — e.g. `acme-`. Pick it once; it is stable forever |
| Published | | **Stable anchor date.** Dedup is name + published (§9.2), so a date that changes on revision forks a new report |
| TLP | | `White` \| `Green` \| `Amber` \| `Red` |
| Author | | **Your member identity** — becomes `created_by_ref` (§8.2) |
| Source Reliability | | Admiralty `A`–`F` |
| Info Credibility | | Admiralty `1`–`6` |
| Threat level | | `High` \| `Medium` \| `Low` (§3.4) — urgency and proximity, **not** a confidence grade. Emitted as `threat_level` in the Patchwork extension ([9.3](../Patchwork-CTI-Framework.md#9.3-classification-properties)) |
| Threat domain | | `Constituency` \| `National` \| `Regional` \| `Partner` \| `World` (§3.3). Highest applicable rung wins. Emitted as `threat_domain` in the Patchwork extension ([9.3](../Patchwork-CTI-Framework.md#9.3-classification-properties)) |
| Activity category | | One or more of the nine categories in §5.2 — emitted as `activity_category` in the Patchwork extension ([9.3](../Patchwork-CTI-Framework.md#9.3-classification-properties)) |

## Key-judgments

> [!TIP] What goes here
> 3-5 bullets. The part a reader acts on — put it first, not at the end.
> State confidence, and say plainly what you cannot support.

-
-
-

## Designation-and-aliases

> [!TIP] What goes here
> Code (cc-CL-<MOT>-####) as the name; handles/personas as aliases. See CTI-Framework.md §9.

| Designation | Aliases | Tier |
| --- | --- | --- |
|  |  |  |


## Motivation-and-tier

> [!TIP] What goes here
> Tier: Cluster (confidence 30) · Temporary (60) · Named (85). Motivation per Appendix A1 of the incident template.



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
> What belongs in this report's `object_refs` so the narrative and the STIX
> container agree. For `actor-profile`: the intrusion-set, its incidents, campaigns, attack-patterns, victims and sectors.

-
-


## Sources

> [!TIP] What goes here
> External references: vendor reporting, news, internal case ids.

| Source | Reference / URL | Reliability |
| --- | --- | --- |
|  |  |  |

