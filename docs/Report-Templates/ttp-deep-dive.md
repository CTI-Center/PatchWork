> [!NOTE] About this template — TTP Deep Dive (`ttp-deep-dive`)
> **Use this when:**
> One adversary and the tactics, techniques and procedures they use to reach a specific goal.
>
> **Use something else if:**
> covering a whole malware family — use `malware-profile`; if the actor rather than their tradecraft is the subject — use `actor-profile`.
>
> Picker: [Report-Types](../Report-Types.md) · Controlled values: [Vocabularies](../Vocabularies.md) · Framework: [Patchwork-CTI-Framework](../Patchwork-CTI-Framework.md)
>
> These `[!tip]` callouts are guidance, not content — delete each one as you fill its section.

# `<Title>`-—-TTP-Deep-Dive

## Report-metadata

| Field | Value | Hint |
| ----- | ----- | ---- |
| Report Type | `ttp-deep-dive` | Fixed for this template — emitted as `report_types: ["ttp-deep-dive"]` |
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

## Technique

> [!TIP] What goes here
> Bare ATT&CK ID (T1486, sub-technique T1566.001) — do not paste full URLs.

| ATT&CK ID | Technique name | Tactic |
| --- | --- | --- |
|  |  |  |


## Observed-usage

> [!TIP] What goes here
> Who uses it, against whom, how it is operationalised in practice.



## Detection-logic

> [!TIP] What goes here
> Concrete queries/rules, not "monitor for anomalies".



## Mitigations

> [!TIP] What goes here
> What actually stops it, and the cost of each.

- -


## Objects-referenced

> [!TIP] What goes here
> What belongs in this report's `object_refs` so the narrative and the STIX container agree. For `ttp-deep-dive`: the attack-pattern (keyed on its ATT&CK id), plus intrusion-sets and incidents that exercise it.

- -


## Sources

> [!TIP] What goes here
> External references: vendor reporting, news, internal case ids.

| Source | Reference / URL | Reliability |
| --- | --- | --- |
|  |  |  |
