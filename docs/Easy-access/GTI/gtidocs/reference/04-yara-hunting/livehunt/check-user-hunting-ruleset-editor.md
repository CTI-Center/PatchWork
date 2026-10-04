---
title: "Check if a user or group is a Livehunt ruleset editor"
source: https://gtidocs.virustotal.com/reference/check-user-hunting-ruleset-editor
slug: check-user-hunting-ruleset-editor
section: reference
group: "YARA Hunting"
updatedAt: 2025-09-25T00:36:27.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [Livehunt](../livehunt.md) › Check if a user or group is a Livehunt ruleset editor

---

# check-if-a-user-or-group-is-a-livehunt-ruleset-editor

This endpoint returns true if the user has editing access to the Hunting ruleset.

```json Response example
{
    "data": true
}
```

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
    "/intelligence/hunting_rulesets/{id}/relationships/editors/{user_or_group_id}": {
      "get": {
        "tags": [
          "Livehunt"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "check-user-hunting-ruleset-editor",
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
            "description": "Ruleset identifier",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "User or group ID",
            "in": "path",
            "name": "user_or_group_id",
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
                    "value": "{\n  \"data\": true\n}"
                  }
                },
                "schema": {
                  "properties": {
                    "data": {
                      "default": true,
                      "type": "boolean"
                    }
                  },
                  "type": "object"
                }
              }
            },
            "description": "200"
          }
        },
        "security": [],
        "summary": "Check if a user or group is a Livehunt ruleset editor"
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

← [Revoke Livehunt ruleset edit permission from a user or group](delete-hunting-ruleset-editor.md) · [up](../README.md) · [Transfer Livehunt ruleset to another user](transfer-livehunt-ruleset-to-another-user.md) →

*Archived from <https://gtidocs.virustotal.com/reference/check-user-hunting-ruleset-editor>.*
