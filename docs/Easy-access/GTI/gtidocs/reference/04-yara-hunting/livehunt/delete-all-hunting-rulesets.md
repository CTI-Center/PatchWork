---
title: "Remove all Livehunt rulesets"
source: https://gtidocs.virustotal.com/reference/delete-all-hunting-rulesets
slug: delete-all-hunting-rulesets
section: reference
group: "YARA Hunting"
updatedAt: 2025-09-25T00:36:18.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [Livehunt](../livehunt.md) › Remove all Livehunt rulesets

---

# remove-all-livehunt-rulesets

This API call deletes all rulesets owned by the user and removes the user from the list of editors in rules shared with them. This operation is asynchronous: the handler launches a background job and returns immediately. This API endpoint returns a [Operation](../../17-api-objects/operation-object.md) object.

# openapi-definition

```json
{
  "info": {
    "title": "YARA Hunting",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Livehunt"
    }
  ],
  "paths": {
    "/intelligence/hunting_rulesets": {
      "delete": {
        "tags": [
          "Livehunt"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "delete-all-hunting-rulesets",
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
            "description": "Since this is a very destructive operation, this additional header must be set to your username.",
            "in": "header",
            "name": "x-confirm-delete",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": ""
                  }
                }
              }
            },
            "description": "200"
          },
          "400": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"error\": {\n    \"code\": \"BadRequestError\",\n    \"message\": \"Send a x-confirm-delete header with your username as a confirmation\"\n  }\n}"
                  }
                },
                "schema": {
                  "properties": {
                    "error": {
                      "properties": {
                        "code": {
                          "type": "string"
                        },
                        "message": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    }
                  },
                  "type": "object"
                }
              }
            },
            "description": "400"
          }
        },
        "security": [],
        "summary": "Remove all Livehunt rulesets"
      }
    }
  },
  "security": [],
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3"
    }
  ],
  "x-readme": {
    "explorer-enabled": true,
    "headers": [],
    "proxy-enabled": false,
    "samples-enabled": true
  }
}
```

---

← [Livehunt](../livehunt.md) · [up](../README.md) · [Get Livehunt rulesets](list-hunting-rulesets.md) →

*Archived from <https://gtidocs.virustotal.com/reference/delete-all-hunting-rulesets>.*
