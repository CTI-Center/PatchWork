---
title: "Get a Crowdsourced YARA rule"
source: https://gtidocs.virustotal.com/reference/get-a-crowdsourced-yara-rule
slug: get-a-crowdsourced-yara-rule
section: reference
group: "YARA Hunting"
updatedAt: 2025-09-25T02:04:56.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [YARA Rules](../yara-rules.md) › Get a Crowdsourced YARA rule

---

# get-a-crowdsourced-yara-rule

Returns a [YARA rule](../../17-api-objects/yara-rule-object.md) object.

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
      "name": "YARA Rules"
    }
  ],
  "paths": {
    "/yara_rules/{id}": {
      "get": {
        "tags": [
          "YARA Rules"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-a-crowdsourced-yara-rule",
        "parameters": [
          {
            "description": "Rule identifier",
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
        "summary": "Get a Crowdsourced YARA rule"
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

← [List Crowdsourced YARA Rules](list-crowdsourced-yara-rules.md) · [up](../README.md) · [Get objects descriptors related to a Crowdsourced YARA rule](crowdsourced-yara-rule-relationship-descriptors-endpoint.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-a-crowdsourced-yara-rule>.*
