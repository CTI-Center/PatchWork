---
title: "Delete"
source: https://gtidocs.virustotal.com/reference/delete_tags-item-type-item-uid-tag-name
slug: delete_tags-item-type-item-uid-tag-name
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:29.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Tags](../tags.md) › Delete

---

# delete

Deletes a tag on an issue

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
    "/tags/{item_type}/{item_uid}/{tag_name}": {
      "delete": {
        "tags": [
          "Tags"
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
            "example": "entity"
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
          },
          {
            "name": "tag_name",
            "in": "path",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "tage name to delete",
            "example": "test Tag"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "headers": {
              "Date": {
                "schema": {
                  "type": "string",
                  "example": "Fri, 09 Sep 2022 16:53:16 GMT"
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
                  "example": "{\"endpoints\":[{\"url\":\"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=xBLtmBD%2F2oGWQ%2BaECEYETZQxSLgt%2FywkSiCWHNqH2DxLseOwpu4aFVlieJf%2Beb%2FpjsYOHQJla1DbK9iD1r%2BcEqbxrKBgtseHz4Tvw3xwKffPIDIiw5MekVEc5NXq0FtBBQ%3D%3D\"}],\"group\":\"cf-nel\",\"max_age\":604800}"
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
                  "example": "748170691eed86fc-ORD"
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
                  "message": "tag remove queued for entity a4cfa1fddf10ea18959c863c7864d343f8b9568248ad75504005980ca6253a01",
                  "result": true
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

← [Create](post_tags-item-type-item-uid.md) · [up](../README.md) · [Seeds](../seeds.md) →

*Archived from <https://gtidocs.virustotal.com/reference/delete_tags-item-type-item-uid-tag-name>.*
