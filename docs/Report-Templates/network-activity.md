> [!WARNING] Retired — do not start a new report from this template
> `network-activity` is a **retired** type. It is still a valid `report_types` value so
> historical imports stay readable, but nothing new should be authored with it
> ([why](<../Report-Types.md#retired-—-valid,-not-authored-(3)>)). The slug named a
> network-flow product against industrial ports; what this template grew into — a general
> adversary-infrastructure write-up — was never what the value meant.
>
> **Write this instead:** [`threat-activity`](threat-activity.md) for the activity itself,
> [`ttp-deep-dive`](ttp-deep-dive.md) for the tradecraft, or
> [`malware-profile`](malware-profile.md) where the infrastructure belongs to one family.
>
> Picker: [Report-Types](../Report-Types.md) · Controlled values: [Vocabularies](../Vocabularies.md) · Framework: [Patchwork-CTI-Framework](../Patchwork-CTI-Framework.md)
>
> These `[!tip]` callouts are guidance, not content — delete each one as you fill its section.

# <Title>-—-Network-Activity

## Report-metadata

| Field | Value | Hint |
| ----- | ----- | ---- |
| Report Type | `network-activity` | Fixed for this template — emitted as `report_types: ["network-activity"]` |
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

## Infrastructure-observed

| Asset | Type | First seen | Last seen |
| --- | --- | --- | --- |
|  |  |  |  |


## Traffic-patterns

> [!TIP] What goes here
> Beaconing intervals, protocols, volumes, timing.



## Pivots

> [!TIP] What goes here
> How this infrastructure links to other known activity — the reusable part.



## Objects-referenced

> [!TIP] What goes here
> What belongs in this report's `object_refs` so the narrative and the STIX
> container agree. For `network-activity`: indicators, observed-data, and the intrusion-set operating the infrastructure.

-
-


## Sources

> [!TIP] What goes here
> External references: vendor reporting, news, internal case ids.

| Source | Reference / URL | Reliability |
| --- | --- | --- |
|  |  |  |

