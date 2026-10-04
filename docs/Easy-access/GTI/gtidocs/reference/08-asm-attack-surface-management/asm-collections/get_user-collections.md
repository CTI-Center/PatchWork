---
title: "Index"
source: https://gtidocs.virustotal.com/reference/get_user-collections
slug: get_user-collections
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:39.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [ASM Collections](../asm-collections.md) › Index

---

# index

List all collections. if invalid, or no PROJECT-ID is passed, only collections from top project are returned.

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
    "/user_collections": {
      "get": {
        "tags": [
          "ASM Collections"
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
          },
          {
            "name": "PROJECT-ID",
            "in": "header",
            "schema": {
              "type": "string"
            },
            "description": "Required: id from /api/v3/asm/projects",
            "example": "{{project-id}}"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "headers": {
              "Date": {
                "schema": {
                  "type": "string",
                  "example": "Fri, 09 Sep 2022 16:57:24 GMT"
                }
              },
              "Content-Type": {
                "schema": {
                  "type": "string",
                  "example": "application/json"
                }
              },
              "Transfer-Encoding": {
                "schema": {
                  "type": "string",
                  "example": "chunked"
                }
              },
              "Connection": {
                "schema": {
                  "type": "string",
                  "example": "keep-alive"
                }
              },
              "X-Content-Type-Options": {
                "schema": {
                  "type": "string",
                  "example": "nosniff"
                }
              },
              "Vary": {
                "schema": {
                  "type": "string",
                  "example": "Origin"
                }
              },
              "Via": {
                "schema": {
                  "type": "string",
                  "example": "1.1 vegur"
                }
              },
              "CF-Cache-Status": {
                "schema": {
                  "type": "string",
                  "example": "DYNAMIC"
                }
              },
              "Report-To": {
                "schema": {
                  "type": "string",
                  "example": "{\"endpoints\":[{\"url\":\"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=Xede4Yk68bG1B4jfDfuYebXyUGUmiICrwwp%2FXYhv8T%2Fs0Ef6CzOnBffKS2LIAyHQm7R87cV7S7%2BP1hcErLI6ljfWp0uqL3pTpXGVjGAuenxbVJiECvfxxcNVP73vhxuDlA%3D%3D\"}],\"group\":\"cf-nel\",\"max_age\":604800}"
                }
              },
              "NEL": {
                "schema": {
                  "type": "string",
                  "example": "{\"success_fraction\":0,\"report_to\":\"cf-nel\",\"max_age\":604800}"
                }
              },
              "Server": {
                "schema": {
                  "type": "string",
                  "example": "cloudflare"
                }
              },
              "CF-RAY": {
                "schema": {
                  "type": "string",
                  "example": "74817676a8f886fc-ORD"
                }
              },
              "Content-Encoding": {
                "schema": {
                  "type": "string",
                  "example": "br"
                }
              }
            },
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                },
                "example": {
                  "success": true,
                  "message": "User collections",
                  "result": [
                    {
                      "id": 132956,
                      "uuid": "c1b502fe-1020-4a85-a620-e02614526ee9",
                      "type": "user_collection",
                      "name": "attacksurface_mw3tdwq",
                      "following": null,
                      "auto_refresh_schedule": "daily",
                      "workflow_name": null,
                      "printable_name": "Attacksurface_APP_QA",
                      "tags": [],
                      "last_updated": "2022-09-09T16:48:13.000Z",
                      "created_at": "2022-08-18T16:10:20.930Z",
                      "deleted": false,
                      "deleted_at": null,
                      "deleted_by": null,
                      "local_icon_path": "/branding/icons/org.png",
                      "entity_count": 1,
                      "new_entity_count": 1,
                      "total_entity_count": 16,
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
                      "project-id": 6797,
                      "project_uuid": "be884e25-a0bb-4836-a836-df5eab176186",
                      "project_name": "ASMQA_AttackSurfaceAPP",
                      "owner_id": 6797,
                      "owner_uuid": "be884e25-a0bb-4836-a836-df5eab176186",
                      "owner_type": "project",
                      "owner_name": "ASMQA_AttackSurfaceAPP",
                      "role": "admin"
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

← [ASM Collections](../asm-collections.md) · [up](../README.md) · [Create](post_user-collections.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_user-collections>.*
