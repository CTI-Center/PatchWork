---
title: "Tasks List"
source: https://gtidocs.virustotal.com/reference/get_library-tasks
slug: get_library-tasks
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:35.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Library](../library.md) › Tasks List

---

# tasks-list

View all tasks. Change Page value to display next 100

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
    "/library/tasks": {
      "get": {
        "tags": [
          "Library"
        ],
        "summary": "Tasks List",
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

← [Issues Stats](get_library-issues-stats.md) · [up](../README.md) · [Tasks Stats](get_library-tasks-stats.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_library-tasks>.*
