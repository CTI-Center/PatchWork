---
title: "Overview"
source: https://gtidocs.virustotal.com/reference/findings-overview
slug: findings-overview
section: reference
group: "GTI Alerts"
updatedAt: 2026-03-06T12:09:47.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [GTI Alerts](../README.md) › [Findings](../findings.md) › Overview

---

# overview

## resource:-finding

A ‘stateless’ and a point in time event that a check produced a result of interest.

```json JSON representation
{
  "name": string,
  "provider": string,
  "displayName": string,
  "detail": {
    object (FindingDetail)
  },
  "severity": number,
  "reoccurrenceTimes": [
    string
  ],
  "relevanceAnalysis": {
    object (RelevanceAnalysis)
  },
  "severityAnalysis": {
    object (SeverityAnalysis)
  },
  "aiSummary": string,
  "audit": {
    object (Audit)
  },
  "alert": string,
  "configurations": [
    string
  ]
}
```

| Fields                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                        | `string`<br /><br />Identifier. Server generated name for the finding (leave clear during creation). Format: projects/\{project}/findings/\{finding}                                                                                                                                                                                                                                                                                                                        |
| `provider`                    | `string`<br /><br />Required. Logical source of this finding (name of the sub-engine).                                                                                                                                                                                                                                                                                                                                                                                      |
| `displayName`                 | `string`<br /><br />Required. A short descriptive title for the finding <= 250 chars. EX: "Actor 'baddy' offering $1000 for credentials of 'goodguy'".                                                                                                                                                                                                                                                                                                                      |
| `detail`                      | `object (`[FindingDetail](#findingdetail) `)`<br /><br />Required. Holder of the domain specific details of the finding.                                                                                                                                                                                                                                                                                                                                                    |
| `severity   **(deprecated)**` | `number`<br /><br />This item is deprecated!<br /><br />Optional. Deprecated: Use the `severityAnalysis` field instead. Base severity score from the finding source.                                                                                                                                                                                                                                                                                                        |
| `reoccurrenceTimes[]`         | `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) ` format)`<br /><br />Output only. When identical finding (same labels and same details) has re-occurred.<br /><br />Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |
| `relevanceAnalysis`           | `object (`[RelevanceAnalysis](../../17-api-objects/alerts-object/relevanceanalysis-object.md) `)`<br /><br />Output only. High-Precision Relevance Analysis verdict for the finding.                                                                                                                                                                                                                                                                                                                          |
| `severityAnalysis`            | `object (`[SeverityAnalysis](../../17-api-objects/alerts-object/severityanalysis-object.md) `)`<br /><br />Output only. High-Precision Severity Analysis verdict for the finding.                                                                                                                                                                                                                                                                                                                             |
| `aiSummary`                   | `string`<br /><br />Optional. AI summary of the finding.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `audit`                       | `object (`[Audit](../../17-api-objects/alerts-object/audit-object.md) `)`<br /><br />Output only. Audit data about the finding.                                                                                                                                                                                                                                                                                                                                                                               |
| `alert`                       | `string`<br /><br />Optional. Name of the alert that this finding is bound to.                                                                                                                                                                                                                                                                                                                                                                                              |
| `configurations[]`            | `string`<br /><br />Optional. Configuration names that are bound to this finding.                                                                                                                                                                                                                                                                                                                                                                                           |

## findingdetail

Wrapper class that contains the union struct for all the various findings detail specific classes.

```json JSON representation
{
  "detailType": string,

  // Union field detail can be only one of the following:
  "initialAccessBroker": {
    object (InitialAccessBrokerFindingDetail)
  },
  "dataLeak": {
    object (DataLeakFindingDetail)
  },
  "insiderThreat": {
    object (InsiderThreatFindingDetail)
  }
  // End of list of possible types for union field detail.
}
```

| Fields                                                                                                                                                                      |                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `detailType`                                                                                                                                                                | `string`<br /><br />Output only. Name of the detail type. Will be set by the server during creation to the name of the field that is set in the detail union. |
| Union field `detail`. Domain specific details object which includes a high level summary of the finding for use in ATD contexts. `detail` can be only one of the following: |                                                                                                                                                               |
| `initialAccessBroker`                                                                                                                                                       | `object (`[InitialAccessBrokerFindingDetail](#initialaccessbrokerfindingdetail) `)`<br /><br />Initial Access Broker finding detail type.                     |
| `dataLeak`                                                                                                                                                                  | `object (`[DataLeakFindingDetail](#dataleakfindingdetail) `)`<br /><br />Data Leak finding detail type.                                                       |
| `insiderThreat`                                                                                                                                                             | `object (`[InsiderThreatFindingDetail](#insiderthreatfindingdetail) `)`<br /><br />Insider Threat finding detail type.                                        |

## initialaccessbrokerfindingdetail

A detail object for an Initial Access Broker (IAB) finding.

```json JSON representation
{
  "matchScore": number,
  "severity": enum (Severity),
  "documentId": string
}
```

<br />

| Fields       |                                                                                                                                                                                                                                      |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `matchScore` | `number`<br /><br />Required. Reference to the match score of the IAB finding. This is a float value between 0 and 1 calculated by the matching engine based on the similarity of the document and the user provided configurations. |
| `severity`   | `enum (`[Severity](#severity) `)`<br /><br />Required. The severity of the IAB finding. This indicates the potential impact of the threat.                                                                                           |
| `documentId` | `string`<br /><br />Required. The unique identifier of the document that triggered the IAB finding. This ID can be used to retrieve the content of the document for further analysis.                                                |

## severity

Severity of the threat finding

| Enums                  |   |
| ---------------------- | - |
| `SEVERITY_UNSPECIFIED` |   |
| `LOW`                  |   |
| `MEDIUM`               |   |
| `HIGH`                 |   |
| `CRITICAL`             |   |

## dataleakfindingdetail

A detail object for a Data Leak finding.

```json JSON representation
{
  "matchScore": number,
  "severity": enum (Severity),
  "documentId": string
}
```

| Fields       |                                                                                                                                                                                                                                                                       |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `matchScore` | `number`<br /><br />Required. Reference to the match score of the Data Leak finding. This is a float value greater than 0 and less than or equal to 1 calculated by the matching engine based on the similarity of the document and the user provided configurations. |
| `severity`   | `enum (`[Severity](#severity-1) `)`<br /><br />Required. The severity of the Data Leak finding. This indicates the potential impact of the threat.                                                                                                                    |
| `documentId` | `string`<br /><br />Required. The unique identifier of the document that triggered the Data Leak finding. This ID can be used to retrieve the content of the document for further analysis.                                                                           |

## severity

Severity of the threat finding.

| Enums                  |                                     |
| ---------------------- | ----------------------------------- |
| `SEVERITY_UNSPECIFIED` | Default value, should never be set. |
| `LOW`                  | Low severity.                       |
| `MEDIUM`               | Medium severity.                    |
| `HIGH`                 | High severity.                      |
| `CRITICAL`             | Critical severity.                  |

## insiderthreatfindingdetail

A detail object for a InsiderThreat finding.

```json JSON representation
{
  "matchScore": number,
  "severity": enum (Severity),
  "documentId": string
}
```

<br />

| Fields       |                                                                                                                                                                                                                                                                           |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `matchScore` | `number`<br /><br />Required. Reference to the match score of the InsiderThreat finding. This is a float value greater than 0 and less than or equal to 1 calculated by the matching engine based on the similarity of the document and the user provided configurations. |
| `severity`   | `enum (`[Severity](#severity-2) `)`<br /><br />Required. The severity of the InsiderThreat finding. This indicates the potential impact of the threat.                                                                                                                    |
| `documentId` | `string`<br /><br />Required. The unique identifier of the document that triggered the InsiderThreat finding. This ID can be used to retrieve the content of the document for further analysis.                                                                           |

## severity

Severity of the threat finding.

| Enums                  |                                     |
| ---------------------- | ----------------------------------- |
| `SEVERITY_UNSPECIFIED` | Default value, should never be set. |
| `LOW`                  | Low severity.                       |
| `MEDIUM`               | Medium severity.                    |
| `HIGH`                 | High severity.                      |
| `CRITICAL`             | Critical severity.                  |

### methods

|                               |                                                                                                                                                                             |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get](get-finding.md)        | Get a finding by name.                                                                                                                                                      |
| [list](list-findings.md)     | Get a list of findings that meet the filter criteria.                                                                                                                       |
| [search](search-findings.md) | SearchFindings is a more powerful version of ListFindings that supports complex queries like "findings for alerts" using functions such as `has_alert` in the query string. |

---

← [Findings](../findings.md) · [up](../README.md) · [Get finding](get-finding.md) →

*Archived from <https://gtidocs.virustotal.com/reference/findings-overview>.*
