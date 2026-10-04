---
title: "Get a crowdsourced Sigma rule object"
source: https://gtidocs.virustotal.com/reference/get-sigma-rules
slug: get-sigma-rules
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T02:03:58.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Files](../files.md) › Get a crowdsourced Sigma rule object

---

# get-a-crowdsourced-sigma-rule-object

Returns a [Sigma Rule](../../17-api-objects/sigma-rule-object.md) object.

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
      "name": "Files"
    }
  ],
  "paths": {
    "/sigma_rules/{id}": {
      "get": {
        "tags": [
          "Files"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-sigma-rules",
        "parameters": [
          {
            "description": "Rule ID",
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
        "summary": "Get a crowdsourced Sigma rule object"
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

← [Get objects related to a file](files-relationships.md) · [up](../README.md) · [Get a crowdsourced YARA ruleset](get-yara-rulesets.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-sigma-rules>.*
