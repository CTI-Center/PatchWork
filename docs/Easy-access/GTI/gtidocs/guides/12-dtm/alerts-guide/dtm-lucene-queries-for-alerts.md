---
title: "Lucene Queries for DTM Alerts"
source: https://gtidocs.virustotal.com/docs/dtm-lucene-queries-for-alerts
slug: dtm-lucene-queries-for-alerts
section: guides
group: "DTM"
updatedAt: 2025-09-25T00:30:02.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [DTM](../README.md) › [Alerts](../alerts-guide.md) › Lucene Queries for DTM Alerts

---

# lucene-queries-for-dtm-alerts

When using Lucene queries to search DTM Alerts, only basic string queries are supported.

The following alert fields are available for Lucene searches:

* `doc_text`
* `doc_keywords`
* `monitor_id`
* `id`
* `title`
* `doc_ref.id`
* `tags`
* `tags.lower`
* `aggregated_alerts.id`
* `aggregated_alerts.monitor_id`
* `aggregated_alerts.tags`
* `aggregated_alerts.tags.lower`

---

← [Group Alerts](dtm-group-alerts.md) · [up](../README.md) · [Monitors](../monitors-guide.md) →

*Archived from <https://gtidocs.virustotal.com/docs/dtm-lucene-queries-for-alerts>.*
