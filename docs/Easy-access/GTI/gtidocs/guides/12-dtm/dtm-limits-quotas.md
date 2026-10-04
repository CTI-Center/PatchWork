---
title: "DTM API Limits and Quotas"
source: https://gtidocs.virustotal.com/docs/dtm-limits-quotas
slug: dtm-limits-quotas
section: guides
group: "DTM"
updatedAt: 2026-08-18T15:23:49.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [DTM](README.md) › DTM API Limits and Quotas

---

# dtm-api-limits-and-quotas

The Digital Threat Monitoring (DTM) API has a number of limits in place to help ensure a secure and consistent experience for all users. 

> ℹ️
>
> If you need increases to any configurable limits, you can work with your Customer Success Manager.

## api-rate-limits

Rate limits provide guardrails for the number of API calls a user and or organization can make in a given time frame.

| **Description**                                                                                                                                                                             | **Duration** | **Limit** | **Scope** | **Configurable** |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------- | --------- | ---------------- |
| **All APIs**: The total number of API requests allowed.                                                                                                                                     | 24 hours     | 50,000    | Per user  | Yes              |
| **Alert backfill**: The number of backfills allowed during monitor creation. This applies to [POST](https://gtidocs.readme.io/reference/post-monitor-backfill) and [PATCH](https://gtidocs.readme.io/reference/patch-monitor-backfill) operations.          | 24 hours     | 50        | Per user  | Yes              |
| **Invalid requests**: The total number of requests with a status code of 400 or greater.                                                                                                    | 1 hour       | 100       | Per user  | Yes              |
| **Bulk alert update**: The number of [bulk alert changes](https://gtidocs.readme.io/reference/post-alerts-bulk-apply) allowed. A bulk change applies when selecting more than 100 alerts and changing their status or tags. | 1 hour       | 10        | Per user  | Yes              |

## api-concurrency-limits

Concurrency limits provide limitations on the number of concurrent API requests that can be active at any given time.

| **Description**                         | **Concurrency Limit** | **Scope** | **Configurable** |
| --------------------------------------- | --------------------- | --------- | ---------------- |
| [Document Search](https://gtidocs.readme.io/reference/post-docs-search) | 5                     | Per user  | No               |
| [List alerts](https://gtidocs.readme.io/reference/get-alerts)           | 10                    | Per user  | No               |

## api-quotas

API quotas provide limitations that define the maximum number of resources a single organization can have.

| **Description**            | **Quota** | **Scope**        | **Configurable** |
| -------------------------- | --------- | ---------------- | ---------------- |
| Number of monitors         | 100       | Per organization | Yes              |
| Number of verified domains | 15,000    | Per organization | Yes              |

## monitor-limits

Limitations that define how many alerts a monitor can generate and how many resources those monitors can use while generating monitors.

| Description                                                                                                                                                                                                                                                                                                                                                                                                                                  | Quota              | Scope       | Configurable |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ----------- | ------------ |
| **Alert Limit**: The alert limit is calculated as a running average starting from the moment the monitor is enabled; the rate is then projected out to twenty-four (24) hours. This means that if a recently-enabled monitor generates many alerts immediately, then the monitor can get disabled before hitting the maximum daily limit. This was done to prevent monitor misconfigurations from creating an overwhelming number of alerts. | 10,000 alerts/day  | Per monitor | No           |
| **Complexity Limit**: The complexity limit is calculated by timing the average amount of CPU time a monitor consumes when searching documents. If the average time exceeds the threshold, the monitor is disabled.                                                                                                                                                                                                                           | 2 seconds/document | Per monitor | No           |

## inactive-monitor-policy

To optimize system resources and reduce processing load, DTM monitors that remain inactive for more than 90 days may be automatically disabled.

### inactivity-criteria

A monitor is considered inactive if it is enabled and generating alerts, but none of the following actions have occurred within the last 90 days:

* **Alert interaction**: No interaction with any generated alerts via the UI or API.
* **Configuration update**: No modifications made to the monitor's configuration.

### notification-and-prevention

* **Advance Notice**: An email notification is sent to account administrators **7 days** before a monitor is scheduled for automatic disabling.
* **Keeping a Monitor Active**: You can prevent a monitor from being disabled by performing either of the following actions during the 7-day grace period:
  * Editing the monitor configuration.
  * Viewing or interacting with any alert generated by the monitor.

---

← [Digital Threat Monitoring FAQ](digital-threat-monitoring-faq.md) · [up](README.md) · [Digital Threat Monitoring](digital-threat-monitoring.md) →

*Archived from <https://gtidocs.virustotal.com/docs/dtm-limits-quotas>.*
