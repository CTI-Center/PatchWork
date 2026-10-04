---
title: "Update a Livehunt ruleset"
source: https://gtidocs.virustotal.com/reference/modify-hunting-ruleset
slug: modify-hunting-ruleset
section: reference
group: "YARA Hunting"
updatedAt: 2026-05-22T07:37:07.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [Livehunt](../livehunt.md) › Update a Livehunt ruleset

---

# update-a-livehunt-ruleset

Use this endpoint to update an existing [Hunting Ruleset](../../17-api-objects/hunting-ruleset-object.md) object attributes as follows:

```json Example request
{
  "data": {
    "type": "hunting_ruleset",
    "id": "{id}",
    "attributes": {
      "enabled": true,
      "limit": 10,
      "name": "bar",
      "notification_emails": ["notifications@acme.com"],
      "rules": "rule foo {condition: false}"
    }
  }
}
```

It returns the updated [Hunting Ruleset](../../17-api-objects/hunting-ruleset-object.md) object.

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
    "/intelligence/hunting_rulesets/{id}": {
      "patch": {
        "tags": [
          "Livehunt"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "modify-hunting-ruleset",
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
                    "description": "A Hunting Ruleset object",
                    "format": "json",
                    "type": "string"
                  }
                },
                "required": [
                  "data"
                ],
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
        "summary": "Update a Livehunt ruleset"
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

← [Get a Livehunt ruleset](get-hunting-ruleset.md) · [up](../README.md) · [Delete IoC Collections association from Hunting ruleset](delete-ioc-collections-relationship.md) →

*Archived from <https://gtidocs.virustotal.com/reference/modify-hunting-ruleset>.*
