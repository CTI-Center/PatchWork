---
title: "Audit"
source: https://gtidocs.virustotal.com/reference/audit-object
slug: audit-object
section: reference
group: "API OBJECTS"
updatedAt: 2026-03-04T11:26:24.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Alerts](../alerts-object.md) › Audit

---

# audit

Tracks basic CRUD facts.

```json Json Representation
{
  "updateTime": string,
  "createTime": string,
  "creator": string,
  "updater": string
}
```

<br />

* **`updateTime`**: `string (Timestamp format)` — Output only. Time of creation or last update .
* **`createTime`**: `string (Timestamp format)` — Output only. Time of creation .
* **`creator`**: `string` — Output only. Agent that created or updated the record, which could be a UserId or a JobId .
* **`updater`**: `string` — Output only. Agent that last updated the record, which could be a UserId or a JobId .

---

← [Alerts](../alerts-object.md) · [up](../README.md) · [ConfidenceLevel](confidencelevel-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/audit-object>.*
