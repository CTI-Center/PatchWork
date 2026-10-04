---
title: "Create"
source: https://gtidocs.virustotal.com/reference/post_user-collections-collection-uuid-user-entities
slug: post_user-collections-collection-uuid-user-entities
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:30.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Seeds](../seeds.md) › Create

---

# create

endpoint which creates a user entity (could be a seed or not) for a collection

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
      "name": "Seeds",
      "description": "deletes a user entity / seed"
    }
  ],
  "paths": {
    "/user_collections/{collection_uuid}/user_entities": {
      "post": {
        "tags": [
          "Seeds"
        ],
        "summary": "Create",
        "description": "",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "entities": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "properties": {
                        "name": {
                          "type": "string"
                        },
                        "type": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "name",
                        "type"
                      ]
                    },
                    "example": {
                      "entities": [
                        {
                          "type": "Domain",
                          "name": "ASM2.io"
                        },
                        {
                          "type": "Domain",
                          "name": "ASM1.io"
                        }
                      ]
                    }
                  }
                },
                "required": [
                  "entities"
                ]
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
            "name": "PROJECT-ID",
            "in": "header",
            "schema": {
              "type": "string"
            },
            "description": "Required: id from /api/v3/asm/projects",
            "example": "{{project-id}}"
          },
          {
            "name": "collection_uuid",
            "in": "path",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "uuid of collection from /api/v3/asm/user_collections"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "headers": {
              "Date": {
                "schema": {
                  "type": "string",
                  "example": "Fri, 09 Sep 2022 16:49:33 GMT"
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
                  "example": "{\"endpoints\":[{\"url\":\"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=Adr%2BzXWfvZ0qIZlfmNtdt0jayyekR%2BUJ%2BKsPNxnP5kzID%2BO2QYw8KKvvZhv%2FWlUyoANl7bUDZBcD9%2Fa9Kcy7%2BpdIMfUJwRn8BvZQqPwq239GSqsEgyzoDaIMwHTW8pphEQ%3D%3D\"}],\"group\":\"cf-nel\",\"max_age\":604800}"
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
                  "example": "74816af38c0286fc-ORD"
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
                  "message": "User entities added to collection",
                  "result": [
                    {
                      "id": 1506950,
                      "type": "Domain",
                      "name": "ASM2.io",
                      "details": null,
                      "claimed": false,
                      "seed": true,
                      "created_at": "2022-09-09T16:49:33.093Z",
                      "updated_at": "2022-09-09T16:49:33.093Z",
                      "last_modified": null
                    },
                    {
                      "id": 1506951,
                      "type": "Domain",
                      "name": "ASM1.io",
                      "details": null,
                      "claimed": false,
                      "seed": true,
                      "created_at": "2022-09-09T16:49:33.108Z",
                      "updated_at": "2022-09-09T16:49:33.108Z",
                      "last_modified": null
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

← [Index](get_user-collections-collection-uuid-user-entities.md) · [up](../README.md) · [Delete](delete_entities-entity-id.md) →

*Archived from <https://gtidocs.virustotal.com/reference/post_user-collections-collection-uuid-user-entities>.*
