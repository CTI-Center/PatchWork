> [!NOTE] About this template — Event Coverage (`event-coverage`)
> **Use this when:** The implications of a recent cyber event or campaign — including a first look published while the analysis is still running.
>
> **Use something else if:** the event needs action today rather than assessment — use `threat-alert`; if you are building the standing picture of the actor behind it — use `actor-profile`.
>
> Picker: [Report-Types](../Report-Types.md) · Controlled values: [Vocabularies](../Vocabularies.md) · Framework: [Patchwork-CTI-Framework](../Patchwork-CTI-Framework.md)
>
> These `[!tip]` callouts are guidance, not content — delete each one as you fill its section.

# <Title>-—-Event-Coverage

## Report-metadata

| Field | Value | Hint |
| ----- | ----- | ---- |
| Report Type | `event-coverage` | Fixed for this template — emitted as `report_types: ["event-coverage"]` |
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

## The-event

> [!TIP] What goes here
> What it is, when, why it draws threat activity.



## Cyber-dimension

> [!TIP] What goes here
> What is actually happening in cyberspace around it.



## Actors-leveraging-it

| Actor | Activity | Motivation |
| --- | --- | --- |
|  |  |  |


## Objects-referenced

> [!TIP] What goes here
> What belongs in this report's `object_refs` so the narrative and the STIX
> container agree. For `event-coverage`: incidents during the event window, actors involved, and affected locations.

-
-


## Sources

> [!TIP] What goes here
> External references: vendor reporting, news, internal case ids.

| Source | Reference / URL | Reliability |
| --- | --- | --- |
|  |  |  |

