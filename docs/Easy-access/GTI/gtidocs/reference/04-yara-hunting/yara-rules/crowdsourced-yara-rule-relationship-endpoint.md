---
title: "Get objects related to a Crowdsourced YARA rule"
source: https://gtidocs.virustotal.com/reference/crowdsourced-yara-rule-relationship-endpoint
slug: crowdsourced-yara-rule-relationship-endpoint
section: reference
group: "YARA Hunting"
updatedAt: 2025-09-25T00:36:12.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [YARA Rules](../yara-rules.md) › Get objects related to a Crowdsourced YARA rule

---

# get-objects-related-to-a-crowdsourced-yara-rule

YARA rule objects have relationships to other objects. As mentioned in the [Relationships](../../01-api-introduction/api-responses/introduction-relationships.md) section, those related objects can be retrieved by sending `GET` requests to the relationship URL.

The relationships supported by YARA rule objects are documented in the [YARA Rules](../../17-api-objects/yara-rule-object.md#relationships) API object page.

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
    "/yara_rules/{id}/{relationship}": {
      "get": {
        "tags": [
          "YARA Rules"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "crowdsourced-yara-rule-relationship-endpoint",
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
        "summary": "Get objects related to a Crowdsourced YARA rule"
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

← [Get objects descriptors related to a Crowdsourced YARA rule](crowdsourced-yara-rule-relationship-descriptors-endpoint.md) · [up](../README.md) · [IoC Stream](../ioc-stream.md) →

*Archived from <https://gtidocs.virustotal.com/reference/crowdsourced-yara-rule-relationship-endpoint>.*
