---
title: "Get object descriptors related to an attack technique"
source: https://gtidocs.virustotal.com/reference/attack_techniquesidrelationshipsrelationship
slug: attack_techniquesidrelationshipsrelationship
section: reference
group: "IoC Investigation"
updatedAt: 2026-02-05T12:43:34.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Attack Techniques](../attack-techniques.md) › Get object descriptors related to an attack technique

---

# get-object-descriptors-related-to-an-attack-technique

This endpoint is the same as [/attack\_techniques/\{id}/\{relationship}](attack_techniqueidrelationship.md) except it returns just the related object's descriptor instead of returning all attributes.

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
      "name": "Attack Techniques"
    }
  ],
  "paths": {
    "/attack_techniques/{id}/relationships/{relationship}": {
      "get": {
        "tags": [
          "Attack Techniques"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "attack_techniquesidrelationshipsrelationship",
        "parameters": [
          {
            "description": "Attack technique's ID",
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
            "description": "Relationship name (see [table](https://gtidocs.readme.io/reference/object-attack-techniques#relationships))",
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
        "summary": "Get object descriptors related to an attack technique"
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

← [Get an attack technique object](attack_techniqueid.md) · [up](../README.md) · [Get objects related to an attack technique](attack_techniqueidrelationship.md) →

*Archived from <https://gtidocs.virustotal.com/reference/attack_techniquesidrelationshipsrelationship>.*
