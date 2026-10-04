---
title: "Overview"
source: https://gtidocs.virustotal.com/reference/alerts-overview
slug: alerts-overview
section: reference
group: "GTI Alerts"
updatedAt: 2026-04-09T14:22:05.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [GTI Alerts](../README.md) › [Alerts](../alerts.md) › Overview

---

# overview

## resource:-alert

Stateful object representing a group of Findings. Key feature to an Alert is that it expresses the user's intent towards the findings of that group, even those that haven't occurred yet.

```json JSON representation
{
  "name": string,
  "findings": [
    string
  ],
  "state": enum (State),
  "audit": {
    object (Audit)
  },
  "displayName": string,
  "detail": {
    object (AlertDetail)
  },
  "duplicateOf": string,
  "duplicatedBy": [
    string
  ],
  "etag": string,
  "externalId": string,
  "aiSummary": string,
  "relevanceAnalysis": {
    object (RelevanceAnalysis)
  },
  "severityAnalysis": {
    object (SeverityAnalysis)
  },
  "priorityAnalysis": {
    object (PriorityAnalysis)
  },
  "findingCount": string,
  "configurations": [
    string
  ]
}
```

<br />

| Fields              |                                                                                                                                                                                                                      |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`              | `string`<br /><br />Identifier. Server generated name for the alert. format is projects/\{project}/alerts/\{alert}                                                                                                   |
| `findings[]`        | `string`<br /><br />Output only. Findings that are covered by this alert.                                                                                                                                            |
| `state`             | `enum (`[State](#state) `)`<br /><br />Output only. State of the alert.                                                                                                                                              |
| `audit`             | `object (`[Audit](../../17-api-objects/alerts-object/audit-object.md) `)`<br /><br />Output only. Audit information for the alert.                                                                                                                     |
| `displayName`       | `string`<br /><br />Output only. A short title for the alert.                                                                                                                                                        |
| `detail`            | `object (`[AlertDetail](#alertdetail) `)`<br /><br />Output only. Details object for the alert, not all alerts will have a details object.                                                                           |
| `duplicateOf`       | `string`<br /><br />Output only. alert name of the alert this alert is a duplicate of. Format: projects/\{project}/alerts/\{alert}                                                                                   |
| `duplicatedBy[]`    | `string`<br /><br />Output only. alert names of the alerts that are duplicates of this alert. Format: projects/\{project}/alerts/\{alert}                                                                            |
| `etag`              | `string`<br /><br />Optional. If included when updating an alert, this should be set to the current etag of the alert. If the etags do not match, the update will be rejected and an ABORTED error will be returned. |
| `externalId`        | `string`<br /><br />Output only. External ID for the alert. This is used internally to provide protection against out of order updates.                                                                              |
| `aiSummary`         | `string`<br /><br />Optional. AI summary of the finding.                                                                                                                                                             |
| `relevanceAnalysis` | `object (`[RelevanceAnalysis](../../17-api-objects/alerts-object/relevanceanalysis-object.md) `)`<br /><br />Output only. High-Precision Relevance Analysis verdict for the alert.                                                                     |
| `severityAnalysis`  | `object (`[SeverityAnalysis](../../17-api-objects/alerts-object/severityanalysis-object.md) `)`<br /><br />Output only. High-Precision Severity Analysis for the alert.                                                                                |
| `priorityAnalysis`  | `object (`[PriorityAnalysis](#priorityanalysis) `)`<br /><br />Output only. High-Precision Priority Analysis for the alert.                                                                                          |
| `findingCount`      | `string (`[int64](https://developers.google.com/discovery/v1/type-format)  format`)`<br /><br />Output only. The number of findings associated with this alert.                                                      |
| `configurations[]`  | `string`<br /><br />Output only. The resource names of the Configurations bound to this alert. Format: projects/\{project}/configurations/\{configuration}                                                           |

## state

alert state is used to track the lifecycle of an alert. More state values may be added in the future.

| Enums                |                                                  |
| -------------------- | ------------------------------------------------ |
| `STATE_UNSPECIFIED`  | Default value, should never be set.              |
| `NEW`                | alert is new.                                    |
| `READ`               | alert was read by a human.                       |
| `TRIAGED`            | alert has been triaged.                          |
| `ESCALATED`          | alert has been escalated.                        |
| `RESOLVED`           | alert has been resolved.                         |
| `DUPLICATE`          | alert is a duplicate of another alert.           |
| `FALSE_POSITIVE`     | alert is a false positive and should be ignored. |
| `NOT_ACTIONABLE`     | alert is not actionable.                         |
| `BENIGN`             | alert is benign.                                 |
| `TRACKED_EXTERNALLY` | alert is tracked externally.                     |

## alertdetail

Container for different types of alert details.

```json JSON representation
{
  "detailType": string,

  // Union field detail can be only one of the following:
  "initialAccessBroker": {
    object (InitialAccessBrokerAlertDetail)
  },
  "dataLeak": {
    object (DataLeakAlertDetail)
  },
  "insiderThreat": {
    object (InsiderThreatAlertDetail)
  }
  // End of list of possible types for union field detail.
}
```

| Fields                                                                                                                                                                       |                                                                                                                                                               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `detailType`                                                                                                                                                                 | `string`<br /><br />Output only. Name of the detail type. Will be set by the server during creation to the name of the field that is set in the detail union. |
| Union field `detail`. Domain specific details object which includes a high level summary of the finding for use in CTEM contexts. `detail` can be only one of the following: |                                                                                                                                                               |
| `initialAccessBroker`                                                                                                                                                        | `object (`[InitialAccessBrokerAlertDetail](#initialaccessbrokeralertdetail) `)`<br /><br />Initial Access Broker alert detail type.                           |
| `dataLeak`                                                                                                                                                                   | `object (`[DataLeakAlertDetail](#dataleakalertdetail) `)`<br /><br />Data Leak alert detail type.                                                             |
| `insiderThreat`                                                                                                                                                              | `object (`[InsiderThreatAlertDetail](#insiderthreatalertdetail) `)`<br /><br />Insider Threat alert detail type.                                              |

## initialaccessbrokeralertdetail

Captures the specific details of InitialAccessBroker (IAB) alert.

```json JSON representation
{
  "severity": string,
  "discoveryDocumentIds": [
    string
  ]
}
```

<br />

| Fields                   |                                                                                                                                           |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `severity`               | `string`<br /><br />Required. The severity of the Initial Access Broker (IAB) alert. Allowed values are: `LOW` `MEDIUM` `HIGH` `CRITICAL` |
| `discoveryDocumentIds[]` | `string`<br /><br />Required. Array of ids to accommodate multiple discovery documents                                                    |

## dataleakalertdetail

Captures the specific details of Data Leak alert.

```json JSON representation
{
  "severity": string,
  "discoveryDocumentIds": [
    string
  ]
}
```

<br />

| Fields                   |                                                                                                                         |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| `severity`               | `string`<br /><br />Required. The severity of the Data Leak alert. Allowed values are: `LOW` `MEDIUM` `HIGH` `CRITICAL` |
| `discoveryDocumentIds[]` | `string`<br /><br />Required. Array of ids to accommodate multiple discovery documents                                  |

## insiderthreatalertdetail

Captures the specific details of InsiderThreat alert.

```json JSON representation
{
  "severity": string,
  "discoveryDocumentIds": [
    string
  ]
}
```

<br />

| Fields                   |                                                                                                                              |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| `severity`               | `string`<br /><br />Required. The severity of the Insider Threat alert. Allowed values are: `LOW` `MEDIUM` `HIGH` `CRITICAL` |
| `discoveryDocumentIds[]` | `string`<br /><br />Required. Array of ids to accommodate multiple discovery documents                                       |

## priorityanalysis

Structured priority analysis for a threat.

```json JSON representation
{
  "priorityLevel": enum (PriorityLevel),
  "confidence": enum (ConfidenceLevel),
  "reasoning": string
}
```

<br />

| Fields          |                                                                                                                                            |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `priorityLevel` | `enum (`[PriorityLevel](#prioritylevel) `)`<br /><br />The level of Priority.                                                              |
| `confidence`    | `enum (`[ConfidenceLevel](../../17-api-objects/alerts-object/confidencelevel-object.md) `)`<br /><br />The level of confidence in the given verdict.                         |
| `reasoning`     | `string`<br /><br />Human-readable explanation from the model, detailing why a particular result is considered to have a certain priority. |

## prioritylevel

Priority Level of an issue.

| Enums                        |                                     |
| ---------------------------- | ----------------------------------- |
| `PRIORITY_LEVEL_UNSPECIFIED` | Default value, should never be set. |
| `PRIORITY_LEVEL_LOW`         | Low Priority.                       |
| `PRIORITY_LEVEL_MEDIUM`      | Medium Priority.                    |
| `PRIORITY_LEVEL_HIGH`        | High Priority.                      |
| `PRIORITY_LEVEL_CRITICAL`    | Critical Priority.                  |

### methods

|                                                     |                                                                                                                                    |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| [benign](triage-alerts/markalertasbenign.md)                     | Marks an alert as benign - BENIGN.                                                                                                 |
| [duplicate](triage-alerts/markalertasduplicate.md)               | Marks an alert as a duplicate of another alert.                                                                                    |
| [enumerateFacets](enumerate-alert-facets.md)       | EnumerateAlertFacets returns the facets and the number of alerts that meet the filter criteria and have that value for each facet. |
| [escalate](triage-alerts/markalertasescalated.md)                | Marks an alert as escalated - ESCALATED.                                                                                           |
| [falsePositive](triage-alerts/markalertasfalsepositive.md)       | Marks an alert as a false positive - FALSE\_POSITIVE.                                                                              |
| [get](get-alert.md)                                | Get an alert by name.                                                                                                              |
| [list](list-alerts.md)                             | Get a list of alerts that meet the filter criteria.                                                                                |
| [notActionable](triage-alerts/markalertasnotactionable.md)       | Marks an alert as not actionable - NOT\_ACTIONABLE.                                                                                |
| [read](triage-alerts/markalertasread.md)                         | Marks an alert as read - READ.                                                                                                     |
| [resolve](triage-alerts/markalertasresolved.md)                  | Marks an alert to closed state - RESOLVED.                                                                                         |
| [trackExternally](triage-alerts/markalertastrackedexternally.md) | Marks an alert as tracked externally - TRACKED\_EXTERNALLY.                                                                        |
| [triage](triage-alerts/markalertastriaged.md)                    | Marks an alert as triaged - TRIAGED.                                                                                               |

<br />

---

← [Alerts](../alerts.md) · [up](../README.md) · [Get Alert](get-alert.md) →

*Archived from <https://gtidocs.virustotal.com/reference/alerts-overview>.*
