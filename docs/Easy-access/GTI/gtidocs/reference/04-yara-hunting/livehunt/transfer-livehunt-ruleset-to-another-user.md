---
title: "Transfer Livehunt ruleset to another user"
source: https://gtidocs.virustotal.com/reference/transfer-livehunt-ruleset-to-another-user
slug: transfer-livehunt-ruleset-to-another-user
section: reference
group: "YARA Hunting"
updatedAt: 2025-09-25T00:36:28.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [Livehunt](../livehunt.md) › Transfer Livehunt ruleset to another user

---

# transfer-livehunt-ruleset-to-another-user

Note: The new owner must be a member of the same group the ruleset was created with.

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
    "/intelligence/hunting_rulesets/{id}/relationships/owner": {
      "post": {
        "tags": [
          "Livehunt"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "transfer-livehunt-ruleset-to-another-user",
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
                    "description": "A user object descriptor",
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
        "summary": "Transfer Livehunt ruleset to another user"
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

← [Check if a user or group is a Livehunt ruleset editor](check-user-hunting-ruleset-editor.md) · [up](../README.md) · [Get object descriptors related to a Livehunt ruleset](get-hunting-ruleset-relationship.md) →

*Archived from <https://gtidocs.virustotal.com/reference/transfer-livehunt-ruleset-to-another-user>.*
