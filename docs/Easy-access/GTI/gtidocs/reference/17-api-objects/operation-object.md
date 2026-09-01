---
title: "Operations"
source: https://gtidocs.virustotal.com/reference/operation-object
slug: operation-object
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T01:05:56.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Operations

---

# operations

Asynchronous operations

Not all API operations can be executed synchronously (i.e. the API endpoint can't wait for the operation to complete before returning). In those cases, the API returns an operation object so the client can periodically ask about the operation status. Its attributes are:

* `status`: <*string*> can be one of "aborted", "finished" or "running".

```json Operation objects
{
  "data": {
    "attributes": {
      "status": "<string>"
    },
    "id": "<string>",
    "type": "operation"
  }
}
```
```json Example
{
  "data": {
    "attributes": {
      "status": "finished"
    },
    "id": "334b32b7fa5b47c78369600fad91d1b4",
    "links": {
      "self": "https://www.virustotal.com/api/v3/operations/334b32b7fa5b47c78369600fad91d1b4"
    },
    "type": "operation"
  }
}
```

---

← [Malware Family](malware-family-object.md) · [up](README.md) · [Private Analyses](private-analyses-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/operation-object>.*
