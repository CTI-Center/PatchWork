---
title: "Destroy"
source: https://gtidocs.virustotal.com/reference/delete_integration-collections-uuid
slug: delete_integration-collections-uuid
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:32.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Integration Collections](../integration-collections.md) › Destroy

---

# destroy

Removes integration from a Collection. Integration will not be deleted from the platform.

UUID is of the integration_collection. found in /api/v3/asm/integration_collections. This value is also displayed in the post Create /api/v3/asm/user_collections/:collection_uuid/integration_collections

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
    "/integration_collections/{uuid}": {
      "delete": {
        "tags": [
          "Integration Collections"
        ],
        "summary": "Destroy",
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
            "description": "Required: uuid from /api/v3/asm/integration_collections"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "headers": {
              "Date": {
                "schema": {
                  "type": "string",
                  "example": "Fri, 09 Sep 2022 16:55:23 GMT"
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
                  "example": "{\"endpoints\":[{\"url\":\"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=9RC0aGZPWR0eLgOeYa6ku9vdmLmoIjoiQqdfn1BYLSZMjDsMbh1WaRfQxsRHCCiOuEnrGeMWKtyqwTZYyI2dRbU%2BXQCa%2B1ZkaO9CYUhBdUGmPuit9jVXWYkMhMPBZtHvYw%3D%3D\"}],\"group\":\"cf-nel\",\"max_age\":604800}"
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
                  "example": "74817380ba0c86fc-ORD"
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
                  "success": false,
                  "message": "Success",
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

← [Index](get_integration-collections.md) · [up](../README.md) · [Create](post_user-collections-collection-uuid-integration-collections.md) →

*Archived from <https://gtidocs.virustotal.com/reference/delete_integration-collections-uuid>.*
