---
title: "Get objects related to an attack tactic"
source: https://gtidocs.virustotal.com/reference/attack_tacticsidrelationship
slug: attack_tacticsidrelationship
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T02:04:41.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Attack Tactics](../attack-tactics.md) › Get objects related to an attack tactic

---

# get-objects-related-to-an-attack-tactic

Available relationships are described in the [Attack Tactic](../attack-tactics.md) object documentation.

# openapi-definition

```json
{
  "info": {
    "title": "IoC Investigation",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Attack Tactics"
    }
  ],
  "paths": {
    "/attack_tactics/{id}/{relationship}": {
      "get": {
        "tags": [
          "Attack Tactics"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "attack_tacticsidrelationship",
        "parameters": [
          {
            "description": "Attack tactic's ID",
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
            "description": "Relationship name (see [table](https://gtidocs.readme.io/reference/object-attack-tactics#relationships))",
            "in": "path",
            "name": "relationship",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Maximum number of related objects to retrieve",
            "in": "query",
            "name": "limit",
            "schema": {
              "default": 10,
              "format": "int32",
              "type": "integer",
              "maximum": 40,
              "minimum": 0
            }
          },
          {
            "description": "Continuation cursor",
            "in": "query",
            "name": "cursor",
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
        "summary": "Get objects related to an attack tactic"
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

← [Get object descriptors related to an attack tactic](attack_tacticsidrelationshipsrelationship.md) · [up](../README.md) · [Attack Techniques](../attack-techniques.md) →

*Archived from <https://gtidocs.virustotal.com/reference/attack_tacticsidrelationship>.*
