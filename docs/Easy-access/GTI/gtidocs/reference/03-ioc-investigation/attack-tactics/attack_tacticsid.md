---
title: "Get an attack tactic object"
source: https://gtidocs.virustotal.com/reference/attack_tacticsid
slug: attack_tacticsid
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T02:04:39.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Attack Tactics](../attack-tactics.md) › Get an attack tactic object

---

# get-an-attack-tactic-object

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
    "/attack_tactics/{id}": {
      "get": {
        "tags": [
          "Attack Tactics"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "attack_tacticsid",
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
        "summary": "Get an attack tactic object"
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

← [Attack Tactics](../attack-tactics.md) · [up](../README.md) · [Get object descriptors related to an attack tactic](attack_tacticsidrelationshipsrelationship.md) →

*Archived from <https://gtidocs.virustotal.com/reference/attack_tacticsid>.*
