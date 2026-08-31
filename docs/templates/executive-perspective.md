> [!NOTE] About this template — Executive Perspective (`executive-perspective`)
> **Use this when:** A leadership briefing — decisions and risk, not technical detail.
>
> **Use something else if:** the audience is analysts or defenders — almost any other type fits better.
>
> Picker: [report-types](../report-types.md) · Controlled values: [Vocabularies](../Vocabularies.md) · Framework: [Patchwork-CTI-Framework](../Patchwork-CTI-Framework.md)
>
> These `[!tip]` callouts are guidance, not content — delete each one as you fill its section.

# <Title>-—-Executive-Perspective

## Report-metadata

| Field | Value | Hint |
| ----- | ----- | ---- |
| Report Type | `executive-perspective` | Fixed for this template — emitted as `report_types: ["executive-perspective"]` |
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

## Bottom-line

> [!TIP] What goes here
> One paragraph. No jargon, no ATT&CK IDs, no tool names.



## Business-impact

> [!TIP] What goes here
> Operational, financial, regulatory, reputational.



## Recommended-posture

> [!TIP] What goes here
> Decisions being asked of leadership, with the cost of each.

-
-


## Objects-referenced

> [!TIP] What goes here
> What belongs in this report's `object_refs` so the narrative and the STIX
> container agree. For `executive-perspective`: the incidents/campaigns underpinning the assessment (readers will not follow them, but the container should still be complete).

-
-


## Sources

> [!TIP] What goes here
> External references: vendor reporting, news, internal case ids.

| Source | Reference / URL | Reliability |
| --- | --- | --- |
|  |  |  |

