---
title: "Index"
source: https://gtidocs.virustotal.com/reference/get_projects
slug: get_projects
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:16.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Projects](../projects.md) › Index

---

# index

List all projects

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
    "/projects": {
      "get": {
        "tags": [
          "Projects"
        ],
        "summary": "Index",
        "description": "",
        "security": [],
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
            "description": "Project obtained.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                },
                "example": {
                  "success": true,
                  "message": "Projects",
                  "result": [
                    {
                      "id": 6797,
                      "created_at": "2022-08-18T16:10:20.842Z",
                      "uuid": "be884e25-a0bb-4836-a836-df5eab176186",
                      "icon": "🏡",
                      "role": "owner",
                      "name": "ASMQA_AttackSurfaceAPP",
                      "owner_email": "name@attacksurface.app",
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
                  ]
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

← [Projects](../projects.md) · [up](../README.md) · [Create](post_projects.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_projects>.*
