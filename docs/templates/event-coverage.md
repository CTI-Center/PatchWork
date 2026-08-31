> [!NOTE] About this template — Event Coverage (`event-coverage`)
> **Use this when:** Cyber activity around a specific real-world event (election, conflict, summit).
>
> **Use something else if:** the activity is a coordinated campaign in its own right — use `threat-activity`.
>
> Picker: [report-types](../report-types.md) · Controlled values: [Vocabularies](../Vocabularies.md) · Framework: [Patchwork-CTI-Framework](../Patchwork-CTI-Framework.md)
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
| Threat level | | `High` \| `Medium` \| `Low` (§3.4) — urgency and proximity, **not** a confidence grade. Emitted as `x_threat_level` |
| Threat domain | | `Constituency` \| `National` \| `Regional` \| `Partner` \| `World` (§3.3). Highest applicable rung wins. Emitted as `x_threat_domain` |
| Activity category | | One or more of the nine categories in §5.2 — emitted as `x_activity_category` |

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

