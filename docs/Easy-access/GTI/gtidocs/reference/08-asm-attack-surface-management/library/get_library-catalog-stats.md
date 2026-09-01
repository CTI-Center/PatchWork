---
title: "Catalog Stats"
source: https://gtidocs.virustotal.com/reference/get_library-catalog-stats
slug: get_library-catalog-stats
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:38.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Library](../library.md) › Catalog Stats

---

# catalog-stats

Statistics about the Catalog

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
    "/library/catalog/stats": {
      "get": {
        "tags": [
          "Library"
        ],
        "summary": "Catalog Stats",
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

← [Tasks List - Export as CSV](get_library-tasks-export-csv.md) · [up](../README.md) · [DTM Pagination](../../09-dtm-digital-threat-monitoring/dtm-pagination.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_library-catalog-stats>.*
