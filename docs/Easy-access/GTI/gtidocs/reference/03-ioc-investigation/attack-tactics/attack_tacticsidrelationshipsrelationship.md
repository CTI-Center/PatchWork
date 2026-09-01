---
title: "Get object descriptors related to an attack tactic"
source: https://gtidocs.virustotal.com/reference/attack_tacticsidrelationshipsrelationship
slug: attack_tacticsidrelationshipsrelationship
section: reference
group: "IoC Investigation"
updatedAt: 2026-02-05T12:43:34.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Attack Tactics](../attack-tactics.md) › Get object descriptors related to an attack tactic

---

# get-object-descriptors-related-to-an-attack-tactic

This endpoint is the same as [/attack\_tactics/\{id}/\{relationship}](attack_tacticsidrelationship.md) except it returns just the related object's descriptor instead of returning all attributes.

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
    "/attack_tactics/{id}/relationships/{relationship}": {
      "get": {
        "tags": [
          "Attack Tactics"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "attack_tacticsidrelationshipsrelationship",
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
        "summary": "Get object descriptors related to an attack tactic"
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

← [Get an attack tactic object](attack_tacticsid.md) · [up](../README.md) · [Get objects related to an attack tactic](attack_tacticsidrelationship.md) →

*Archived from <https://gtidocs.virustotal.com/reference/attack_tacticsidrelationshipsrelationship>.*
