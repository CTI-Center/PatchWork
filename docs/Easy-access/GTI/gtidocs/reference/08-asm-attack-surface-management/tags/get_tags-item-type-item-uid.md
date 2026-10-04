---
title: "Index"
source: https://gtidocs.virustotal.com/reference/get_tags-item-type-item-uid
slug: get_tags-item-type-item-uid
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:28.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Tags](../tags.md) › Index

---

# index

Lists all tags on an entity or issue.

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
      "name": "Tags"
    }
  ],
  "paths": {
    "/tags/{item_type}/{item_uid}": {
      "get": {
        "tags": [
          "Tags"
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
          },
          {
            "name": "item_type",
            "in": "path",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "issue or entity",
            "example": "issue"
          },
          {
            "name": "item_uid",
            "in": "path",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "id from /api/v3/asm/search/issues/collection:CollectionName or /api/v3/asm/search/entities/collection:CollectionName",
            "example": "a4cfa1fddf10ea18959c863c7864d343f8b9568248ad75504005980ca6253a01"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "headers": {
              "Date": {
                "schema": {
                  "type": "string",
                  "example": "Fri, 09 Sep 2022 16:53:04 GMT"
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
                  "example": "{\"endpoints\":[{\"url\":\"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=%2BzqSiEYXA0ClzqPQPwwAAvNcyK5LMJDrpcF3hpdNcxhWw3BLBdmy%2B%2FQQVpFYE1ffgwH%2B4BvzacFRM%2BKC12jUK%2FEOJdngq0wvEl5yjY%2FWR84%2FjpJ24JhfbQVKl4YYxBoeXw%3D%3D\"}],\"group\":\"cf-nel\",\"max_age\":604800}"
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
                  "example": "7481701ede0186fc-ORD"
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
                  "message": "Tags for entity a4cfa1fddf10ea18959c863c7864d343f8b9568248ad75504005980ca6253a01",
                  "result": [
                    "test Tag"
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

← [Tags](../tags.md) · [up](../README.md) · [Create](post_tags-item-type-item-uid.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_tags-item-type-item-uid>.*
