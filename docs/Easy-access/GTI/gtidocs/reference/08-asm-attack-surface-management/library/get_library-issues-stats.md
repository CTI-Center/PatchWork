---
title: "Issues Stats"
source: https://gtidocs.virustotal.com/reference/get_library-issues-stats
slug: get_library-issues-stats
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:35.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Library](../library.md) › Issues Stats

---

# issues-stats

Statistics about the issues, Total count, Count by category:

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
    "/library/issues/stats": {
      "get": {
        "tags": [
          "Library"
        ],
        "summary": "Issues Stats",
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

← [Issues List - Specific Isssue](get_library-issues-issue-name.md) · [up](../README.md) · [Tasks List](get_library-tasks.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_library-issues-stats>.*
