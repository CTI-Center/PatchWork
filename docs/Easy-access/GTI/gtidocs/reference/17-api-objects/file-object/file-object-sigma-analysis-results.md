---
title: "sigma_analysis_results"
source: https://gtidocs.virustotal.com/reference/file-object-sigma-analysis-results
slug: file-object-sigma-analysis-results
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:42:24.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › sigma_analysis_results

---

# sigma_analysis_results

Sigma results for the file.

List of dictionaries containing aggregated [sigma](https://github.com/SigmaHQ/sigma) analyses results from all sandbox generated EVTX files. Each item contains the following subfields:

* `rule_title`: <*string*> matched sigma rule title.
* `rule_source`: <*string*> sigma ruleset where this rule belongs to.
* `match_context`: <*dictionary*> specific matched events. This dictionary contains the following key:
  * `values`: <*list of map\<str, str>>* all matched events represented as key-value.
* `rule_level`: <*string*> rule level, can be either of "critical", "high", "medium", "low".
* `rule_description`: <*string*> rule description
* `rule_author`: <*string*> rule author
* `rule_id`: <*string*> rule ID in Google Threat Intelligence. You can use this to find other files matching this same rule.

---

← [sigma_analysis_stats](file-object-sigma-analysis-stats.md) · [up](../README.md) · [sandbox_verdicts](file-object-sandbox-verdicts.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-sigma-analysis-results>.*
