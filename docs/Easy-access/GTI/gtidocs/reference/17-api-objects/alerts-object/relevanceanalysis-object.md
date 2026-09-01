---
title: "RelevanceAnalysis"
source: https://gtidocs.virustotal.com/reference/relevanceanalysis-object
slug: relevanceanalysis-object
section: reference
group: "API OBJECTS"
updatedAt: 2026-03-04T11:28:54.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Alerts](../alerts-object.md) › RelevanceAnalysis

---

# relevanceanalysis

Structured relevance analysis for a threat.

```json JSON Representation
{
  "relevant": boolean,
  "confidence": enum (ConfidenceLevel),
  "reasoning": string,
  "evidence": {
    object (Evidence)
  },
  "relevanceLevel": enum (RelevanceLevel)
}
```

* **`relevant`**: `boolean` — Indicates whether the threat is considered relevant.
* **`confidence`**: `enum (ConfidenceLevel)` — The level of confidence in the given verdict.
* **`reasoning`**: `string` — Human-readable explanation from the matcher, detailing why a particular result is considered relevant or not relevant.
* **`evidence`**: `object (Evidence)` — Evidence supporting the verdict, including matched and unmatched items.
* **`relevanceLevel`**: `enum (RelevanceLevel)` — The level of relevance.

## evidence

Details the evidence used to determine the relevance verdict.

```json JSON Representation
{
  "commonThemes": [
    string
  ],
  "distinctThemes": [
    string
  ]
}
```

* **`commonThemes[]`**: `string` — A list of semantic themes or concepts found to be common, related, or aligned between the sources, supporting the verdict.
* **`distinctThemes[]`**: `string` — A list of semantic themes or descriptions unique to one source or semantically distant.

## relevancelevel

Relevance Level of an issue.

* **`RELEVANCE_LEVEL_UNSPECIFIED`**: Default value, should never be set ([source](https://docs.cloud.google.com/threat-intelligence/reference/rest/v1beta/RelevanceAnalysis?content_ref=default+value+should+never+be+set)).
* **`RELEVANCE_LEVEL_LOW`**: Low Relevance.
* **`RELEVANCE_LEVEL_MEDIUM`**: Medium Relevance.
* **`RELEVANCE_LEVEL_HIGH`**: High Relevance.

---

← [ConfidenceLevel](confidencelevel-object.md) · [up](../README.md) · [SeverityAnalysis](severityanalysis-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/relevanceanalysis-object>.*
