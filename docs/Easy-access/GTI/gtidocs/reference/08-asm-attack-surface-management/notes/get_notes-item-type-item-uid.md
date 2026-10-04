---
title: "Index"
source: https://gtidocs.virustotal.com/reference/get_notes-item-type-item-uid
slug: get_notes-item-type-item-uid
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:26.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Notes](../notes.md) › Index

---

# index

Lists all notes on an entity or issue.

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
      "name": "Notes"
    }
  ],
  "paths": {
    "/notes/{item_type}/{item_uid}": {
      "get": {
        "tags": [
          "Notes"
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
            "example": "6b884a854d4998f787e1dde6b937f0ca63c844dcfe9558e1c2758cef0ca6d459"
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
                  "example": "Mon, 24 Apr 2023 19:32:00 GMT"
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
                  "example": "887"
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
                  "message": "Notes for issue 6b884a854d4998f787e1dde6b937f0ca63c844dcfe9558e1c2758cef0ca6d459",
                  "result": [
                    {
                      "uuid": "1112f519-06a9-4e2c-845c-aa79996c804a",
                      "dynamic_id": "issue##c1ac6a07-fda8-4568-90c3-ea2ba6ec2535#2022-10-18T17:28:41Z",
                      "collection_name": "attacksurface_mw3tdwq",
                      "created_by_user_uuid": "c1ac6a07-fda8-4568-90c3-ea2ba6ec2535",
                      "item_name": null,
                      "item_uid": "6b884a854d4998f787e1dde6b937f0ca63c844dcfe9558e1c2758cef0ca6d459",
                      "item_type": "issue",
                      "note": "- testing a note that supports markdown\n- and has some neat new features",
                      "uid": "a67d6376f53176204957185bdc54d65bc6021b1d75aa88cc779de901a13ae833",
                      "created_at": "2022-10-18T17:28:41.128Z",
                      "updated_at": "2022-10-18T00:00:00.000Z",
                      "collection_id": 132956,
                      "created_by_user_id": 10354,
                      "created_by_user": {
                        "email": "Name@domain.app",
                        "printable_name": "FirstName LastName",
                        "uuid": "c1ac6a07-df89-1258-90c3-ea2ba6ec2535"
                      }
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

← [Notes](../notes.md) · [up](../README.md) · [Create](post_notes-item-type-item-uid.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_notes-item-type-item-uid>.*
