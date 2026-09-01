---
title: "Create"
source: https://gtidocs.virustotal.com/reference/post_user-collections
slug: post_user-collections
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:39.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [ASM Collections](../asm-collections.md) › Create

---

# create

Creates a new collection

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
      "post": {
        "tags": [
          "ASM Collections"
        ],
        "summary": "Create",
        "description": "",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string"
                  },
                  "workflow_name": {
                    "type": "string",
                    "enum": [
                      "external_discovery_and_assessment",
                      "authenticated_cloud_discovery",
                      "code_repository_discovery_and_assessment",
                      "suspicious_domain_discovery",
                      "mobile_app_discovery",
                      "external_application_assessment",
                      "third_party_workflow"
                    ]
                  }
                },
                "required": [
                  "name",
                  "workflow_name"
                ],
                "example": {
                  "name": "Test Collection"
                }
              }
            }
          }
        },
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
              "Server": {
                "schema": {
                  "type": "string",
                  "example": "Cowboy"
                }
              },
              "Date": {
                "schema": {
                  "type": "string",
                  "example": "Fri, 17 Feb 2023 22:42:58 GMT"
                }
              },
              "Connection": {
                "schema": {
                  "type": "string",
                  "example": "keep-alive"
                }
              },
              "Content-Type": {
                "schema": {
                  "type": "string",
                  "example": "application/json"
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
              "Content-Length": {
                "schema": {
                  "type": "integer",
                  "example": "966"
                }
              },
              "Via": {
                "schema": {
                  "type": "string",
                  "example": "1.1 vegur"
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
                  "message": "Collection created!",
                  "result": {
                    "id": 139738,
                    "uuid": "a161bde5-4611-43b2-b32a-9d8d8f8d62aa",
                    "type": "user_collection",
                    "name": "testcollection__5tkayo",
                    "following": null,
                    "auto_refresh_schedule": "daily",
                    "workflow_name": null,
                    "printable_name": "Test collection",
                    "global_labels": [],
                    "last_updated": "2018-01-01T00:00:00.000Z",
                    "created_at": "2023-02-17T22:42:52.655Z",
                    "deleted": false,
                    "deleted_at": null,
                    "deleted_by": null,
                    "local_icon_path": "/branding/icons/org.png",
                    "entity_count": 0,
                    "new_entity_count": 0,
                    "total_entity_count": 0,
                    "issues_by_severity": {},
                    "notify_emails_new_entities": null,
                    "notify_webhooks_new_entities": null,
                    "pointer_collection_id": null,
                    "pointer_collection_uuid": null,
                    "config": null,
                    "refreshing": null,
                    "project-id": 1234,
                    "project_uuid": "be884e25-a0bb-4836-a836-df5eab176186",
                    "project_name": "Project_Name",
                    "owner_id": 1234,
                    "owner_uuid": "be884e25-a0bb-4836-a836-df5eab176186",
                    "owner_type": "project",
                    "owner_name": "Project_name"
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

← [Index](get_user-collections.md) · [up](../README.md) · [Read](get_user-collections-uuid.md) →

*Archived from <https://gtidocs.virustotal.com/reference/post_user-collections>.*
