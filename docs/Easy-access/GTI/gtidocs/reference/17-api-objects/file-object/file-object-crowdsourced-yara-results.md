---
title: "crowdsourced_yara_results"
source: https://gtidocs.virustotal.com/reference/file-object-crowdsourced-yara-results
slug: file-object-crowdsourced-yara-results
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:42:20.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › crowdsourced_yara_results

---

# crowdsourced_yara_results

YARA matches from crowdsourced rules.

YARA matches for the file. Every item on the list contains the following attributes:

* `author`: <*string*> rule author.
* `description`: <*string*> matched rule description.
* `match_in_subfile`: <*boolean*> whether the match was in a [subfile](file-object-bundled-files.md) or not.
* `rule_name`: <*string*> matched rule name.
* `ruleset_id`: <*string*> Google Threat Intelligence's ruleset ID. You can use this ID to fetch the ruleset info in the [/api/v3/yara\_rulesets/\{id}](../../03-ioc-investigation/files/get-yara-rulesets.md) endpoint.
* `ruleset_name`: <*string*> matched rule's ruleset name.
* `source`: <*string*> ruleset source.

---

← [🔀 related_threat_actors](file-object-related-threat-actors.md) · [up](../README.md) · [crowdsourced_ids_results](file-object-crowdsourced-ids-results.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-crowdsourced-yara-results>.*
