---
title: "Grant Livehunt ruleset edit permissions for a user or group"
source: https://gtidocs.virustotal.com/reference/edit-hunting-ruleset-relationship
slug: edit-hunting-ruleset-relationship
section: reference
group: "YARA Hunting"
updatedAt: 2025-09-25T00:36:25.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [Livehunt](../livehunt.md) › Grant Livehunt ruleset edit permissions for a user or group

---

# grant-livehunt-ruleset-edit-permissions-for-a-user-or-group

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
    "/intelligence/hunting_rulesets/{id}/relationships/editors": {
      "post": {
        "tags": [
          "Livehunt"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "edit-hunting-ruleset-relationship",
        "parameters": [
          {
            "description": "Ruleset identifier",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Your API key",
            "in": "header",
            "name": "x-apikey",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "properties": {
                  "data": {
                    "description": "A list of user/groups to be added as editors or set as owners of the ruleset",
                    "format": "json",
                    "type": "string"
                  }
                },
                "type": "object"
              }
            }
          }
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "properties": {},
                  "type": "object"
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
                    "value": "{}"
                  }
                },
                "schema": {
                  "properties": {},
                  "type": "object"
                }
              }
            },
            "description": "400"
          }
        },
        "security": [],
        "summary": "Grant Livehunt ruleset edit permissions for a user or group"
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

← [Add IoC Collectios association to a Hunting ruleset](add-ioc-collections-relationship.md) · [up](../README.md) · [Revoke Livehunt ruleset edit permission from a user or group](delete-hunting-ruleset-editor.md) →

*Archived from <https://gtidocs.virustotal.com/reference/edit-hunting-ruleset-relationship>.*
