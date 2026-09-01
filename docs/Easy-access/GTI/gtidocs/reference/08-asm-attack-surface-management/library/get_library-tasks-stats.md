---
title: "Tasks Stats"
source: https://gtidocs.virustotal.com/reference/get_library-tasks-stats
slug: get_library-tasks-stats
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:36.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Library](../library.md) › Tasks Stats

---

# tasks-stats

Returns a list of current task type count, and count by Author:

# openapi-definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "ASM (ATTACK SURFACE MANAGEMENT)",
    "version": "1.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3/asm"
    }
  ],
  "tags": [
    {
      "name": "Library"
    }
  ],
  "paths": {
    "/library/tasks/stats": {
      "get": {
        "tags": [
          "Library"
        ],
        "summary": "Tasks Stats",
        "parameters": [
          {
            "description": "Your API key",
            "in": "header",
            "name": "x-apikey",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "description": "",
        "responses": {
          "200": {
            "description": "Successful response",
            "content": {
              "application/json": {}
            }
          }
        }
      }
    }
  },
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": false,
    "samples-enabled": true
  }
}
```

---

← [Tasks List](get_library-tasks.md) · [up](../README.md) · [Fingerprints List](get_library-fingerprints.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_library-tasks-stats>.*
