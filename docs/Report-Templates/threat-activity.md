> [!NOTE] About this template — Threat Activity (`threat-activity`)
> **Use this when:** Activity — historical or recent — whose relevance has become elevated by current circumstances.
>
> **Use something else if:** building a standing picture of the actor — use `actor-profile`; if the point is the implication of one event — use `event-coverage`.
>
> **This is not the campaign object.** One operation with a start and an end is a `campaign` ([9.4](../Patchwork-CTI-Framework.md#9.4-curation-layer)); this report is the write-up of why that activity matters now, and it references the campaign rather than replacing it.
>
> Picker: [Report-Types](../Report-Types.md) · Controlled values: [Vocabularies](../Vocabularies.md) · Framework: [Patchwork-CTI-Framework](../Patchwork-CTI-Framework.md)
>
> These `[!tip]` callouts are guidance, not content — delete each one as you fill its section.

# <Title>-—-Threat-Activity

> ⚠️ **This type is also generated automatically.** `cti-aggregate.js` already
> emits `threat-activity` reports from the incident data, and OpenCTI deduplicates
> reports on **name + published**. If you title this report using the generated
> pattern — `cc-<Campaign> — threat activity` — it will **merge into and
> overwrite** the automatic one. Give your hand-written report a distinct title.

## Report-metadata

| Field | Value | Hint |
| ----- | ----- | ---- |
| Report Type | `threat-activity` | Fixed for this template — emitted as `report_types: ["threat-activity"]` |
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

## Activity-scope

> [!TIP] What goes here
> What activity this report covers, and **why its relevance is elevated now** — that second
> half is the reason this report exists rather than a note in the file.
> If the activity forms one operation, say what ties the incidents together and reference the
> `campaign` object; the coordination claim lives there, not here
> ([9.4](../Patchwork-CTI-Framework.md#9.4-curation-layer)).



## Timeline

| Date | Event |
| --- | --- |
|  |  |


## Victims

| Victim | Sector | Country |
| --- | --- | --- |
|  |  |  |


## Attribution-confidence

> [!TIP] What goes here
> Who, and how sure. Cite the linking evidence rather than asserting.



## Objects-referenced

> [!TIP] What goes here
> What belongs in this report's `object_refs` so the narrative and the STIX
> container agree. For `threat-activity`: the campaign, its incidents, the attributed intrusion-set(s) and attack-patterns.

-
-


## Sources

> [!TIP] What goes here
> External references: vendor reporting, news, internal case ids.

| Source | Reference / URL | Reliability |
| --- | --- | --- |
|  |  |  |

