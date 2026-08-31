# Report-types-—-pick-one,-then-use-its-template

Every report carries a `report_types` value from `report_types_ov`
(26 values, [Vocabularies](Vocabularies.md) §3.10). This page exists so you can tell **which one
to pick** and start from a real structure instead of a blank page.

## How-to-choose

Ask what the report is *about*, not what prompted it:

- One **adversary**, standing picture → `actor-profile`
- One **operation** with a start and end → `threat-activity`
- One **malware family** → `malware-profile`
- One **technique** → `ttp-deep-dive`
- Something **urgent** needing action today → `threat-alert`
- A **region** or a **sector** over a period → `country-profile` / `industry`
- For **leadership** rather than defenders → `executive-perspective`

## Before-you-write-—-three-things-that-bite

1. **Title carries your member namespace token.** Assertions a member authors are
   namespaced so two members' reports never collide on name-based dedup
   ([4.2](Patchwork-CTI-Framework.md#4.2-member-namespaces)). Pick your token once —
   changing it later forks every object that carries it.
2. **`published` must be a stable anchor date.** Reports deduplicate on
   **`name` + `published`** ([9.2](Patchwork-CTI-Framework.md#9.2-identity-and-merge-rules)).
   A date that shifts when you revise forks a second report instead of updating the first.
   Anchor it to the earliest activity the report covers, never the latest.
3. **Three types may also be produced by tooling** — `actor-profile`,
   `threat-activity`, `country-profile`. If your member generates these from
   incident data, a hand-written one needs a distinct title or the two merge and
   one overwrites the other. Each template spells out the pattern to avoid.
4. **The three classification fields are not optional.** Threat level, threat domain
   and activity category ([3](Patchwork-CTI-Framework.md#3.-what-we-track-and-how-we-scope-it))
   are how a receiving member triages your report and scopes it against their own
   constituency. A report without them cannot be prioritised by anyone but you.

Author identity on everything: **your own member identity**, emitted as `created_by_ref`
([8.2](Patchwork-CTI-Framework.md#8.2-provenance)).

## Hand-authored-types-(15)

| Type                         | Use this when                                                         | Template                                                            | Sample                                                      |
| ---------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------- |
| `threat-alert`               | Urgent, time-sensitive warning that needs action now                  | [threat-alert](templates/threat-alert.md)                             | 1. [Access-sale-scenario](samples/Access-sale-scenario.md) , 2. [Access-sale-scenario-2](samples/Access-sale-scenario-2.md) |
| `actor-profile`              | Standing profile of one adversary — **also AUTO**                     | [actor-profile](templates/actor-profile.md)                           |                                                             |
| `threat-activity`            | One campaign or coordinated operation — **also AUTO**                 | [threat-activity](templates/threat-activity.md)                       |                                                             |
| `malware-profile`            | Deep dive on one malware family                                       | [malware-profile](templates/malware-profile.md)                       | 1. [CRESCENTHARVEST](samples/CRESCENTHARVEST.md)                                      |
| `ttp-deep-dive`              | Detailed analysis of a single technique or tactic                     | [ttp-deep-dive](templates/ttp-deep-dive.md)                           |                                                             |
| `country-profile`            | Threat landscape for one country over a period — **also AUTO**        | [country-profile](templates/country-profile.md)                       |                                                             |
| `industry`                   | Threats to one sector, across countries                               | [industry](templates/industry.md)                                     |                                                             |
| `executive-perspective`      | Leadership briefing — decisions and risk, not technical detail        | [executive-perspective](templates/executive-perspective.md)           |                                                             |
| `vulnerability-exploitation` | A specific vulnerability being exploited in the wild                  | [vulnerability-exploitation](templates/vulnerability-exploitation.md) |                                                             |
| `patch`                      | Remediation guidance for a patch or patch cycle                       | [patch](templates/patch.md)                                           |                                                             |
| `network-activity`           | Adversary infrastructure or observed traffic analysis                 | [network-activity](templates/network-activity.md)                     |                                                             |
| `event-coverage`             | Cyber activity around a real-world event (election, conflict, summit) | [event-coverage](templates/event-coverage.md)                         |                                                             |
| `news-analysis`              | Assessing public reporting, adding what the article cannot give       | [news-analysis](templates/news-analysis.md)                           |                                                             |
| `trends-forecasting`         | Forward-looking analysis over a period                                | [trends-forecasting](templates/trends-forecasting.md)                 |                                                             |
| `ics-security-roundup`       | Periodic roundup of OT/ICS security activity                          | [ics-security-roundup](templates/ics-security-roundup.md)             |                                                             |

## Feed-assigned-types-(11)-—-no-template

These are the base STIX slugs the **GTI and Mandiant connectors** apply to
reports they import, classifying a report by the kind of object it concerns.
They are valid values and you will see them on imported reports, but nobody
hand-writes one — there is no `observed-data` report to sit down and author.
If you were about to reach for one of these, the hand-authored table above
almost certainly has what you want.

| Type | Applied to |
| ---- | ---------- |
| `attack-pattern` | Imported report about a technique → prefer `ttp-deep-dive` |
| `campaign` | Imported report about a campaign → prefer `threat-activity` |
| `identity` | Imported report about an organization or victim |
| `indicator` | Imported report delivering indicators |
| `intrusion-set` | Imported report about an adversary → prefer `actor-profile` |
| `malware` | Imported report about malware → prefer `malware-profile` |
| `observed-data` | Imported raw observation data |
| `threat-actor` | Imported report about a named threat actor |
| `threat-report` | Generic imported threat report with no finer classification |
| `tool` | Imported report about a tool |
| `vulnerability` | Imported report about a vulnerability → prefer `vulnerability-exploitation` |
