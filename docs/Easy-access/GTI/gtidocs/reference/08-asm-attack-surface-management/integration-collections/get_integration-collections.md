---
title: "Index"
source: https://gtidocs.virustotal.com/reference/get_integration-collections
slug: get_integration-collections
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:32.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Integration Collections](../integration-collections.md) › Index

---

# index

Returns current integrations assigned to collections.

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
    "/integration_collections": {
      "get": {
        "tags": [
          "Integration Collections"
        ],
        "summary": "Index",
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
                  "example": "Fri, 09 Sep 2022 16:54:43 GMT"
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
                  "example": "{\"endpoints\":[{\"url\":\"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=DiZWkiz8tAvFdPtFnyIXqqZgD47jX3FKeoIqJTKvq6A3xdVKh2Y1fFcUOAPr2gh3htyIt9N9EwGNHy4qZmM6xloi6Gm8yZwapjy4DT1CeyP%2Bxo6LHb19sB1qeXNE%2FIL4ng%3D%3D\"}],\"group\":\"cf-nel\",\"max_age\":604800}"
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
                  "example": "74817284ef7c86fc-ORD"
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
                  "result": [
                    {
                      "id": 116,
                      "uuid": "b98ad9be-c38b-4b16-b0e0-1f464e7ede9a",
                      "integration_id": 180,
                      "integration_uuid": "8bc49144-7704-4381-994c-2e7ada9fee98",
                      "integration_name": "Github Integration 1",
                      "integration_type": "github",
                      "integration_created_at": "2022-09-06T23:38:10.751Z",
                      "collection_id": 132956,
                      "collection_uuid": "c1b502fe-1020-4a85-a620-e02614526ee9",
                      "created_at": "2022-09-09T15:44:41.133Z",
                      "updated_at": "2022-09-09T00:00:00.000Z"
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

← [Integration Collections](../integration-collections.md) · [up](../README.md) · [Destroy](delete_integration-collections-uuid.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_integration-collections>.*
