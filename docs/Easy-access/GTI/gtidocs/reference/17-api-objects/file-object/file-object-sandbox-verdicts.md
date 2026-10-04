---
title: "sandbox_verdicts"
source: https://gtidocs.virustotal.com/reference/file-object-sandbox-verdicts
slug: file-object-sandbox-verdicts
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:42:25.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › sandbox_verdicts

---

# sandbox_verdicts

Sandbox verdicts for the file.

A summary of all sandbox verdicts for a given file. It's a dictionary, where each key is the sandbox name and each value is a dictionary containing the following keys:

* `category`: <*string*> normalized verdict category. It can be one of `suspicious`, `malicious`, `harmless` or `undetected`.
* `confidence`: <*integer*> verdict confidence from 0 to 100.
* `malware_classification`: <*list of strings*> raw sandbox verdicts.
* `malware_names`: <*list of strings*> malware family names.
* `sandbox_name`: <*string*> sandbox that provided the verdict.

---

← [sigma_analysis_results](file-object-sigma-analysis-results.md) · [up](../README.md) · [detectiteasy](file-object-detectiteasy.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-sandbox-verdicts>.*
