---
title: "Get object descriptors related to a Livehunt ruleset"
source: https://gtidocs.virustotal.com/reference/get-hunting-ruleset-relationship
slug: get-hunting-ruleset-relationship
section: reference
group: "YARA Hunting"
updatedAt: 2025-09-25T00:36:29.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [Livehunt](../livehunt.md) › Get object descriptors related to a Livehunt ruleset

---

# get-object-descriptors-related-to-a-livehunt-ruleset

Same as [/hunting\_rulesets/\{id}/\{relationships}](get-hunting-ruleset-full-relationships.md) except it returns just the related object's descriptor (and context attributes, if any) instead of returning all attributes.

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
    "/intelligence/hunting_rulesets/{id}/relationships/{relationship}": {
      "get": {
        "tags": [
          "Livehunt"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-hunting-ruleset-relationship",
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
          },
          {
            "description": "Relationship name (see [table](https://gtidocs.readme.io/reference/hunting-ruleset-object#relationships))",
            "in": "path",
            "name": "relationship",
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
        "summary": "Get object descriptors related to a Livehunt ruleset"
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

← [Transfer Livehunt ruleset to another user](transfer-livehunt-ruleset-to-another-user.md) · [up](../README.md) · [Get objects related to a Livehunt ruleset](get-hunting-ruleset-full-relationships.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-hunting-ruleset-relationship>.*
