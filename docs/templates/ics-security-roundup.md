> [!NOTE] About this template — ICS Security Roundup (`ics-security-roundup`)
> **Use this when:** Periodic roundup of OT/ICS security activity.
>
> **Use something else if:** a single ICS incident — use the incident report template or `threat-alert`.
>
> Picker: [report-types](../report-types.md) · Controlled values: [Vocabularies](../Vocabularies.md) · Framework: [Patchwork-CTI-Framework](../Patchwork-CTI-Framework.md)
>
> These `[!tip]` callouts are guidance, not content — delete each one as you fill its section.

# <Title>-—-ICS-Security-Roundup

## Report-metadata

| Field | Value | Hint |
| ----- | ----- | ---- |
| Report Type | `ics-security-roundup` | Fixed for this template — emitted as `report_types: ["ics-security-roundup"]` |
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

## OT/ICS-incidents

| Date | Target | Impact |
| --- | --- | --- |
|  |  |  |


## Affected-systems

> [!TIP] What goes here
> Vendors, protocols, device classes (PLC, HMI, SCADA, historian).



## Sector-impact

> [!TIP] What goes here
> Utilities, energy, manufacturing, water — operational consequence, not just IT.



## Objects-referenced

> [!TIP] What goes here
> What belongs in this report's `object_refs` so the narrative and the STIX
> container agree. For `ics-security-roundup`: ICS-related incidents, affected sectors, and the actors involved.

-
-


## Sources

> [!TIP] What goes here
> External references: vendor reporting, news, internal case ids.

| Source | Reference / URL | Reliability |
| --- | --- | --- |
|  |  |  |

