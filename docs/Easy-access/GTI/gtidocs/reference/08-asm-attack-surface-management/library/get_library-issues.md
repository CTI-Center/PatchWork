---
title: "Issues List"
source: https://gtidocs.virustotal.com/reference/get_library-issues
slug: get_library-issues
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:34.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Library](../library.md) › Issues List

---

# issues-list

View list of all issue types. Change Page value to display next 100 issues.

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
    "/library/issues": {
      "get": {
        "tags": [
          "Library"
        ],
        "summary": "Issues List",
        "description": "",
        "parameters": [
          {
            "name": "page",
            "in": "query",
            "schema": {
              "type": "integer"
            },
            "example": "2"
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

← [Entities Stats](get_library-entities-stats.md) · [up](../README.md) · [Issues List - Specific Isssue](get_library-issues-issue-name.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_library-issues>.*
