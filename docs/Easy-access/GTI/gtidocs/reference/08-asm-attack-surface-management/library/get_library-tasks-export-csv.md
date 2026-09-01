---
title: "Tasks List - Export as CSV"
source: https://gtidocs.virustotal.com/reference/get_library-tasks-export-csv
slug: get_library-tasks-export-csv
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:37.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Library](../library.md) › Tasks List - Export as CSV

---

# tasks-list---export-as-csv

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
    "/library/tasks/export/csv": {
      "get": {
        "tags": [
          "Library"
        ],
        "summary": "Tasks List - Export as CSV",
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

← [Issues List - Export as CSV](get_library-issues-export-csv.md) · [up](../README.md) · [Catalog Stats](get_library-catalog-stats.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_library-tasks-export-csv>.*
