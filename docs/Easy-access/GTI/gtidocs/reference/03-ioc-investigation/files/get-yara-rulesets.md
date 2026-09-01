---
title: "Get a crowdsourced YARA ruleset"
source: https://gtidocs.virustotal.com/reference/get-yara-rulesets
slug: get-yara-rulesets
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T00:35:13.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Files](../files.md) › Get a crowdsourced YARA ruleset

---

# get-a-crowdsourced-yara-ruleset

Returns a [YARA Ruleset](../../17-api-objects/yara-rulesets-object.md) object used in our crowdsourced YARA results.

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
    "/yara_rulesets/{id}": {
      "get": {
        "tags": [
          "Files"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-yara-rulesets",
        "parameters": [
          {
            "description": "Ruleset ID to fetch.",
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
        "summary": "Get a crowdsourced YARA ruleset"
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

← [Get a crowdsourced Sigma rule object](get-sigma-rules.md) · [up](../README.md) · [Files Behaviours](../files-behaviours.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-yara-rulesets>.*
