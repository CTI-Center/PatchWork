---
title: "Fingerprints List"
source: https://gtidocs.virustotal.com/reference/get_library-fingerprints
slug: get_library-fingerprints
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:36.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Library](../library.md) › Fingerprints List

---

# fingerprints-list

Returns Technology fingerprints from Library.

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
    "/library/fingerprints": {
      "get": {
        "tags": [
          "Library"
        ],
        "summary": "Fingerprints List",
        "description": "",
        "parameters": [
          {
            "name": "sort",
            "in": "query",
            "schema": {
              "type": "string"
            },
            "description": "name, product, vendory, version",
            "example": "name"
          },
          {
            "name": "search",
            "in": "query",
            "schema": {
              "type": "string"
            },
            "description": "searches vendor and product fields",
            "example": "\"apache http server\""
          },
          {
            "name": "page",
            "in": "query",
            "schema": {
              "type": "integer"
            },
            "example": "1"
          },
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

← [Tasks Stats](get_library-tasks-stats.md) · [up](../README.md) · [Fingerprint Stats](get_library-fingerprints-stats.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_library-fingerprints>.*
