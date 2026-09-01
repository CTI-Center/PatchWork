---
title: "Unarchive"
source: https://gtidocs.virustotal.com/reference/patch_user-collections-uuid-unarchive
slug: patch_user-collections-uuid-unarchive
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:41.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [ASM Collections](../asm-collections.md) › Unarchive

---

# unarchive

Unarchive a collection

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
      "name": "ASM Collections",
      "description": "Collections live under a project and are another foundational unit of organization in the ASM platform. They define the process of collecting entities, issues and technologies. All entities, issues and technologies live within one and only one collection (and its corresponding project)."
    }
  ],
  "paths": {
    "/user_collections/{uuid}/unarchive": {
      "patch": {
        "tags": [
          "ASM Collections"
        ],
        "summary": "Unarchive",
        "description": "",
        "requestBody": {
          "content": {}
        },
        "parameters": [
          {
            "description": "Your API key",
            "in": "header",
            "name": "x-apikey",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "uuid",
            "in": "path",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "uuid from /api/v3/asm/user_collections"
          }
        ],
        "responses": {
          "200": {
            "description": "Collection unarchived",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                },
                "example": {
                  "success": false,
                  "message": "Collection unarchived",
                  "result": null
                }
              }
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

← [Archive](patch_user-collections-uuid-archive.md) · [up](../README.md) · [Collection Runs](../collection-runs.md) →

*Archived from <https://gtidocs.virustotal.com/reference/patch_user-collections-uuid-unarchive>.*
