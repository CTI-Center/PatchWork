---
title: "Revoke Livehunt ruleset edit permission from a user or group"
source: https://gtidocs.virustotal.com/reference/delete-hunting-ruleset-editor
slug: delete-hunting-ruleset-editor
section: reference
group: "YARA Hunting"
updatedAt: 2025-09-25T00:36:26.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [Livehunt](../livehunt.md) › Revoke Livehunt ruleset edit permission from a user or group

---

# revoke-livehunt-ruleset-edit-permission-from-a-user-or-group

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
      "delete": {
        "tags": [
          "Livehunt"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "delete-hunting-ruleset-editor",
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
                    "value": ""
                  }
                }
              }
            },
            "description": "200"
          }
        },
        "security": [],
        "summary": "Revoke Livehunt ruleset edit permission from a user or group"
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

← [Grant Livehunt ruleset edit permissions for a user or group](edit-hunting-ruleset-relationship.md) · [up](../README.md) · [Check if a user or group is a Livehunt ruleset editor](check-user-hunting-ruleset-editor.md) →

*Archived from <https://gtidocs.virustotal.com/reference/delete-hunting-ruleset-editor>.*
