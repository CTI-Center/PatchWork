---
title: "Create"
source: https://gtidocs.virustotal.com/reference/post_user-collections-collection-uuid-integration-collections
slug: post_user-collections-collection-uuid-integration-collections
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:32.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Integration Collections](../integration-collections.md) › Create

---

# create

Assigns an existing integration to a collection. To create an integration, see Integrations Section.

"integration_uuid" within the body can be found in /api/v3/asm/projects/:uuid/integrations

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
      "name": "Integration Collections",
      "description": "Configure Collections with integrations for Cloud credential associations."
    }
  ],
  "paths": {
    "/user_collections/{collection_uuid}/integration_collections": {
      "post": {
        "tags": [
          "Integration Collections"
        ],
        "summary": "Create",
        "description": "",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "example": {
                  "integration_uuid": ""
                }
              }
            }
          }
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
            "name": "collection_uuid",
            "in": "path",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Required: uuid from /api/v3/asm/user_collections"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "headers": {
              "Date": {
                "schema": {
                  "type": "string",
                  "example": "Fri, 09 Sep 2022 16:56:07 GMT"
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
                  "example": "{\"endpoints\":[{\"url\":\"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=4JX6CTHhqCDy04rb5XSFZbFugMBXgz%2FNux%2Fsk0vTjGKT2jwozSyDDDFxUfGv%2FN16LLAVglSqbIXsVtqbuKza0a10c4uhdErTYkIjPeQYaaFUNvo49EFkjn7G5eIM7NNrnw%3D%3D\"}],\"group\":\"cf-nel\",\"max_age\":604800}"
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
                  "example": "748174938f0a86fc-ORD"
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
                  "message": "Success",
                  "result": {
                    "id": 117,
                    "uuid": "b0258e9c-33a6-4987-b756-ff0c6f68ecdd",
                    "integration_id": 180,
                    "integration_uuid": "8bc49144-7704-4381-994c-2e7ada9fee98",
                    "integration_name": "Github Integration 1",
                    "integration_type": "github",
                    "integration_created_at": "2022-09-06T23:38:10.751Z",
                    "collection_id": 132956,
                    "collection_uuid": "c1b502fe-1020-4a85-a620-e02614526ee9",
                    "created_at": "2022-09-09T16:56:07.271Z",
                    "updated_at": "2022-09-09T00:00:00.000Z"
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

← [Destroy](delete_integration-collections-uuid.md) · [up](../README.md) · [Library](../library.md) →

*Archived from <https://gtidocs.virustotal.com/reference/post_user-collections-collection-uuid-integration-collections>.*
