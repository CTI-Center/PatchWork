---
title: "Get objects descriptors related to a Crowdsourced YARA rule"
source: https://gtidocs.virustotal.com/reference/crowdsourced-yara-rule-relationship-descriptors-endpoint
slug: crowdsourced-yara-rule-relationship-descriptors-endpoint
section: reference
group: "YARA Hunting"
updatedAt: 2025-09-25T02:04:57.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [YARA Rules](../yara-rules.md) › Get objects descriptors related to a Crowdsourced YARA rule

---

# get-objects-descriptors-related-to-a-crowdsourced-yara-rule

Same as [/yara\_rules/\{id}/\{relationships}](crowdsourced-yara-rule-relationship-endpoint.md) except it returns just the related object's descriptor (and context attributes, if any) instead of returning all attributes.

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
    "/yara_rules/{id}/relationships/{relationship}": {
      "get": {
        "tags": [
          "YARA Rules"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "crowdsourced-yara-rule-relationship-descriptors-endpoint",
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
          },
          {
            "description": "Relationship name (see [table](https://gtidocs.readme.io/reference/yara-rule-object#relationships))",
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
        "summary": "Get objects descriptors related to a Crowdsourced YARA rule"
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

← [Get a Crowdsourced YARA rule](get-a-crowdsourced-yara-rule.md) · [up](../README.md) · [Get objects related to a Crowdsourced YARA rule](crowdsourced-yara-rule-relationship-endpoint.md) →

*Archived from <https://gtidocs.virustotal.com/reference/crowdsourced-yara-rule-relationship-descriptors-endpoint>.*
