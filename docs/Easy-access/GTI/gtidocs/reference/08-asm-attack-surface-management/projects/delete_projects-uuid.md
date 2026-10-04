---
title: "Delete"
source: https://gtidocs.virustotal.com/reference/delete_projects-uuid
slug: delete_projects-uuid
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:17.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Projects](../projects.md) › Delete

---

# delete

This api endpoint will delete a project.

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
      "name": "Projects",
      "description": "Projects are the most foundational unit of organization in the ASM platform. Collections exist within one and only one project."
    }
  ],
  "paths": {
    "/projects/{uuid}": {
      "delete": {
        "tags": [
          "Projects"
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
            "description": "Required: uuid to delete from /api/v3/asm/projects"
          }
        ],
        "responses": {
          "200": {
            "description": "Project deleted.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                },
                "example": {
                  "success": true,
                  "message": "Deleted Project",
                  "result": {
                    "id": 7048,
                    "created_at": "2022-09-09T16:20:11.576Z",
                    "uuid": "bbc7b1dc-0d9f-4e3f-91a3-9746fcb91b35",
                    "icon": null,
                    "role": null,
                    "name": "New Project Name",
                    "owner_email": null,
                    "description": null,
                    "expired_at": null,
                    "organization_name": "ASMQA AttackSurfaceAPP",
                    "organization_uuid": "075892c8-fe6f-454e-a071-34a7342c16a3",
                    "plan_expires_at": "2025-09-17T00:00:00.000Z",
                    "plan_status": "paid",
                    "deleted_at": null,
                    "deleted": false,
                    "primary": false
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

← [Create](post_projects.md) · [up](../README.md) · [ASM Collections](../asm-collections.md) →

*Archived from <https://gtidocs.virustotal.com/reference/delete_projects-uuid>.*
