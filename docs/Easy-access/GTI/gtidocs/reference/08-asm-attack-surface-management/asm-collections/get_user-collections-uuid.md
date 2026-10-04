---
title: "Read"
source: https://gtidocs.virustotal.com/reference/get_user-collections-uuid
slug: get_user-collections-uuid
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:39.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [ASM Collections](../asm-collections.md) › Read

---

# read

Show details for a specified collection

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
      "get": {
        "tags": [
          "ASM Collections"
        ],
        "summary": "Read",
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
            "description": "uuid from /api/v3/asm/user_collections",
            "example": "a161bde5-4611-43b2-b32a-9d8d8f8d62aa"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                },
                "example": {
                  "success": true,
                  "message": "Collection retrieved!",
                  "result": {
                    "id": 132956,
                    "uuid": "c1b502fe-1020-4a85-a620-e02614526ee9",
                    "type": "user_collection",
                    "name": "collectionname_mw3tdwq",
                    "following": null,
                    "auto_refresh_schedule": "daily",
                    "workflow_name": null,
                    "printable_name": "Collection Name",
                    "tags": [],
                    "last_updated": "2022-09-09T05:56:21.000Z",
                    "created_at": "2022-08-18T16:10:20.930Z",
                    "deleted": false,
                    "deleted_at": null,
                    "deleted_by": null,
                    "local_icon_path": "/branding/icons/org.png",
                    "entity_count": 0,
                    "new_entity_count": 0,
                    "total_entity_count": 14,
                    "issues_by_severity": {
                      "4": 1,
                      "5": 3
                    },
                    "notify_emails_new_entities": null,
                    "notify_webhooks_new_entities": null,
                    "pointer_collection_id": null,
                    "pointer_collection_uuid": null,
                    "config": null,
                    "refreshing": false,
                    "project-id": 1234,
                    "project_uuid": "be884e25-a0bb-4836-a836-df5eab176186",
                    "project_name": "Project Name",
                    "owner_id": 1234,
                    "owner_uuid": "be884e25-a0bb-4836-a836-df5eab176186",
                    "owner_type": "project",
                    "owner_name": "Project_name",
                    "role": "admin"
                  }
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

← [Create](post_user-collections.md) · [up](../README.md) · [Delete](delete_user-collections-uuid.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_user-collections-uuid>.*
