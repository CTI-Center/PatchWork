> [!NOTE] About this template — Net Assessment (`net-assessment`)
> **Use this when:** Retrospective — the top threats you reported on or observed across the period just ended.
>
> **Use something else if:** the analysis points forward — use `trends-forecasting`; if it is scoped to one region or sector rather than to a period — use `country-profile` or `industry`.
>
> Picker: [Report-Types](../Report-Types.md) · Controlled values: [Vocabularies](../Vocabularies.md) · Framework: [Patchwork-CTI-Framework](../Patchwork-CTI-Framework.md)
>
> These `[!tip]` callouts are guidance, not content — delete each one as you fill its section.

# <Title>-—-Net-Assessment

## Report-metadata

| Field | Value | Hint |
| ----- | ----- | ---- |
| Report Type | `net-assessment` | Fixed for this template — emitted as `report_types: ["net-assessment"]` |
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

## Period-covered

> [!TIP] What goes here
> The exact window, and what "top" was measured against — volume, proximity to your
> constituency, threat level, something else. A ranking whose criterion is unstated cannot
> be compared against the previous edition.
>
> This type recurs, so its `Published` date needs care: anchor it to the **first day of the
> period covered**. That keeps each edition distinct under name + published dedup (§9.2)
> without the date shifting when you revise one.



## Top-threats

> [!TIP] What goes here
> The threats themselves, ranked. One row each, pointing at the reports that carried them —
> this assessment summarises work already published, it does not re-argue it.

| Rank | Threat | Actor / family | Why it ranked | Reports |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |


## What-changed

> [!TIP] What goes here
> Movement against the previous edition: what entered the ranking, what left it, what held
> position but changed character. A retrospective with no comparison is a list.



## Outlook

> [!TIP] What goes here
> What this period implies for the next one — briefly. A full forward-looking argument
> belongs in `trends-forecasting`, not here; link to it rather than duplicating it.



## Objects-referenced

> [!TIP] What goes here
> What belongs in this report's `object_refs` so the narrative and the STIX
> container agree. For `net-assessment`: the actors, campaigns and malware families named
> in the ranking, and the reports being summarised.

-
-


## Sources

> [!TIP] What goes here
> External references: vendor reporting, news, internal case ids.

| Source | Reference / URL | Reliability |
| --- | --- | --- |
|  |  |  |
