---
title: "SeverityAnalysis"
source: https://gtidocs.virustotal.com/reference/severityanalysis-object
slug: severityanalysis-object
section: reference
group: "API OBJECTS"
updatedAt: 2026-03-04T11:29:45.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Alerts](../alerts-object.md) › SeverityAnalysis

---

# severityanalysis

Structured severity analysis for a threat.

```json JSON Representation
{
  "severityLevel": enum (SeverityLevel),
  "confidence": enum (ConfidenceLevel),
  "reasoning": string
}
```

<br />

* **`severityLevel`**: `enum (SeverityLevel)` — The level of severity.
* **`confidence`**: `enum (ConfidenceLevel)` — The level of confidence in the given verdict.
* **`reasoning`**: `string` — Human-readable explanation from the model, detailing why a particular result is considered to have a certain severity.

## severitylevel

Severity Level of an issue.

* **`SEVERITY_LEVEL_UNSPECIFIED`**: Default value, should never be set.
* **`SEVERITY_LEVEL_LOW`**: Low Severity.
* **`SEVERITY_LEVEL_MEDIUM`**: Medium Severity.
* **`SEVERITY_LEVEL_HIGH`**: High Severity.

---

← [RelevanceAnalysis](relevanceanalysis-object.md) · [up](../README.md) · [Analyses](../analyses-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/severityanalysis-object>.*
