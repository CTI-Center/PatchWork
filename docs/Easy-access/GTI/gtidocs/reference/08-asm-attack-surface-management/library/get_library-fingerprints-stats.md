---
title: "Fingerprint Stats"
source: https://gtidocs.virustotal.com/reference/get_library-fingerprints-stats
slug: get_library-fingerprints-stats
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:37.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Library](../library.md) › Fingerprint Stats

---

# fingerprint-stats

Statistics about the Fingerprint (ident) capabilities

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
    "/library/fingerprints/stats": {
      "get": {
        "tags": [
          "Library"
        ],
        "summary": "Fingerprint Stats",
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

← [Fingerprints List](get_library-fingerprints.md) · [up](../README.md) · [Issues List - Export as CSV](get_library-issues-export-csv.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_library-fingerprints-stats>.*
