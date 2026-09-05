> [!NOTE] About this template — Threat Alert (`threat-alert`)
> **Use this when:**
> An urgent, time-sensitive warning that needs action now.
>
> **Use something else if:**
> the activity is ongoing but not urgent — use `threat-activity`; or you are assessing what the event implies rather than demanding action on it — use `event-coverage`.
>
> Picker: [Report-Types](../Report-Types.md) · Controlled values: [Vocabularies](../Vocabularies.md) · Framework: [Patchwork-CTI-Framework](../Patchwork-CTI-Framework.md)
>
> These `[!tip]` callouts are guidance, not content — delete each one as you fill its section.

# <Title>-—-Threat-Alert

## Report-metadata

| Field | Value | Hint |
| ----- | ----- | ---- |
| Report Type | `threat-alert` | Fixed for this template — emitted as `report_types: ["threat-alert"]` |
| Title | | Prefix with **your member namespace token** (§4.2) — e.g. `acme-`. Pick it once; it is stable forever |
| Published | | **Stable anchor date.** Dedup is name + published (§9.2), so a date that changes on revision forks a new report |
| TLP | | `Clear` \| `Green` \| `Amber` \| `Amber+Strict` \| `Red` (TLP 2.0, §8.1). `Clear` was called `White` and keeps the same STIX id; `Amber+Strict` withdraws the client carve-out and is dual-marked with `Amber` |
| Author | | **Your member identity** — becomes `created_by_ref` (§8.2) |
| Source Reliability | | Admiralty `A`–`F` |
| Info Credibility | | Admiralty `1`–`6` |
| Threat level | | **REQUIRED for this type.** `High` \| `Medium` \| `Low` (§3.4) — urgency and proximity, **not** a confidence grade. This is the field a reader triages on; an alert without it cannot be prioritised. Emitted as `threat_level` in the Patchwork extension ([9.3](../Patchwork-CTI-Framework.md#9.3-classification-properties)) |
| Threat domain | | `Constituency` \| `National` \| `Regional` \| `Partner` \| `World` (§3.3). Highest applicable rung wins. Emitted as `threat_domain` in the Patchwork extension ([9.3](../Patchwork-CTI-Framework.md#9.3-classification-properties)) |
| Activity category | | One or more of the nine categories in §5.2 — emitted as `activity_category` in the Patchwork extension ([9.3](../Patchwork-CTI-Framework.md#9.3-classification-properties)) |
| Observed date | | **Required where this report records an incident.** When the activity was *observed*, not when this was written. It contributes to the incident's identity key (§9.2), so a wrong date forks a duplicate rather than updating. Emitted as `observed_date` in the Patchwork extension ([9.3](../Patchwork-CTI-Framework.md#9.3-classification-properties)) |

## Key-judgments

> [!TIP] What goes here
> 3-5 bullets. The part a reader acts on — put it first, not at the end. State confidence, and say plainly what you cannot support.

- - -

## What-happened

> [!TIP] What goes here
> Plain, factual. Assume the reader has 30 seconds.



## Who's-affected

> [!TIP] What goes here
> Sectors, regions, products, versions.



## Immediate-actions

> [!TIP] What goes here
> Ordered by urgency. Each item must be something the reader can actually do today.

- -


## Detection

> [!TIP] What goes here
> Signatures, log queries, indicators to hunt for. Bare ATT&CK IDs (T1486).

| Detection method | Detail |
| --- | --- |
|  |  |


## Objects-referenced

> [!TIP] What goes here
> What belongs in this report's `object_refs` so the narrative and the STIX container agree. For `threat-alert`: the incident(s), the intrusion-set, attack-patterns, affected victims/sectors, and any indicators.

- -


## Sources

> [!TIP] What goes here
> External references: vendor reporting, news, internal case ids.

| Source | Reference / URL | Reliability |
| --- | --- | --- |
|  |  |  |

