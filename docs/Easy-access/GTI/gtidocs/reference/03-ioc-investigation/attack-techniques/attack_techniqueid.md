---
title: "Get an attack technique object"
source: https://gtidocs.virustotal.com/reference/attack_techniqueid
slug: attack_techniqueid
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T02:04:42.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Attack Techniques](../attack-techniques.md) › Get an attack technique object

---

# get-an-attack-technique-object

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
    "/attack_techniques/{id}": {
      "get": {
        "tags": [
          "Attack Techniques"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "attack_techniqueid",
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
        "summary": "Get an attack technique object"
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

← [Attack Techniques](../attack-techniques.md) · [up](../README.md) · [Get object descriptors related to an attack technique](attack_techniquesidrelationshipsrelationship.md) →

*Archived from <https://gtidocs.virustotal.com/reference/attack_techniqueid>.*
