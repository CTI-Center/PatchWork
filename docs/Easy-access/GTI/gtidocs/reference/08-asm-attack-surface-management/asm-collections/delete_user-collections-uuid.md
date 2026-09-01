---
title: "Delete"
source: https://gtidocs.virustotal.com/reference/delete_user-collections-uuid
slug: delete_user-collections-uuid
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:40.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [ASM Collections](../asm-collections.md) › Delete

---

# delete

Delete a collection

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
    "/user_collections/{uuid}": {
      "delete": {
        "tags": [
          "ASM Collections"
        ],
        "summary": "Delete",
        "description": "",
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
            "description": "Collection deleted",
            "content": {
              "text/plain": {
                "schema": {
                  "type": "string"
                },
                "example": "{\n    \"success\": true,\n    \"message\": \"Collection permanently deleted!\",\n    \"result\": true\n}"
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

← [Read](get_user-collections-uuid.md) · [up](../README.md) · [Archive](patch_user-collections-uuid-archive.md) →

*Archived from <https://gtidocs.virustotal.com/reference/delete_user-collections-uuid>.*
