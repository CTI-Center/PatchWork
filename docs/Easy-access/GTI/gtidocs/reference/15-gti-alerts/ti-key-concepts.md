---
title: "Key Concepts"
source: https://gtidocs.virustotal.com/reference/ti-key-concepts
slug: ti-key-concepts
section: reference
group: "GTI Alerts"
updatedAt: 2026-06-17T13:47:02.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [GTI Alerts](README.md) › Key Concepts

---

# key-concepts

This document explains the core data structures and logic used by the Google Threat Intelligence Alerts API. To start calling the API, see the [Get Started](ti-get-started.md) guide, and to see all the available methods, see the [Google Threat Intelligence API Reference](alerts.md).

## customer-profile

The Customer Profile is a structured data object stored within the [`projects.configurations`](configurations/configurations-overview.md) resource. It encapsulates the entity's characteristics used for threat matching.

A profile typically contains:

* **Identity:** Company name, brands, and key persons.
* **Assets:** Domains, IPs, and tech precences.
* **Context:** Industry, geographic regions, and security considerations.

The system uses the customer profile to perform nuanced, context-aware semantic matching beyond keyword search.

## findings-vs.-alerts

The API distinguishes between raw detections and actionable incidents using two distinct resources:

### findings

**Resource:** [`projects.findings`](findings/findings-overview.md)

A Finding is an immutable record of a **specific** threat detection event. It contains:

* **Source Data:** The raw content (e.g., forum post body, file hash).
* **Match Metadata:** Why it matched, severity, and confidence.
* **Timestamp:** When the event was observed.
* **Technology Watch List:** Monitoring for mentions of specific technologies.

### alerts

**Resource:** [`projects.alerts`](alerts/alerts-overview.md)

An Alert is a mutable, stateful object that **groups one or more Findings**. It represents a security incident that requires investigation. Alerts are enriched with:

* **Aggregated Context:** Summary of all related findings.
* **Status:** Triage state (e.g., New, Triaged, Resolved).
* **Severity:** Computed risk score based on the findings and related asset criticality.

## threat-scenarios

Threat Scenarios organizes and groups relevant alerts together, and are the logical definitions that determine detection behavior.

Supported scenarios include:

* **Data Leakage:** Identifying potentially sensitive data on external platforms.
* **Initial Access Broker (IAB):** Detecting potential sale of network access.
* **Insider Threats:** Detecting potential recruitment attempts and insider offerings.
* **Technology Watch List:** Monitoring for mentions of specific technologies.

<br />

---

← [Export Dashboard Data](../14-dashboards/dashboards/dashboards-download.md) · [up](README.md) · [Get Started](ti-get-started.md) →

*Archived from <https://gtidocs.virustotal.com/reference/ti-key-concepts>.*
