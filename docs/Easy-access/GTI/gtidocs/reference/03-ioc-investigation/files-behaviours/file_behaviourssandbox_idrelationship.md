---
title: "Get objects related to a behaviour report"
source: https://gtidocs.virustotal.com/reference/file_behaviourssandbox_idrelationship
slug: file_behaviourssandbox_idrelationship
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T00:35:20.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Files Behaviours](../files-behaviours.md) › Get objects related to a behaviour report

---

# get-objects-related-to-a-behaviour-report

As mentioned in the [Relationships](../../01-api-introduction/api-responses/introduction-relationships.md) section, those related objects can be retrieved by sending `GET` requests to the relationship URL.

Available relationships are described in the [File behaviour](../../17-api-objects/file-behaviour-summary-object.md) object documentation.

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
      "name": "Files Behaviours"
    }
  ],
  "paths": {
    "/file_behaviours/{sandbox_id}/{relationship}": {
      "get": {
        "tags": [
          "Files Behaviours"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "file_behaviourssandbox_idrelationship",
        "parameters": [
          {
            "description": "Sandbox report ID",
            "in": "path",
            "name": "sandbox_id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Relationship name (see [table](https://gtidocs.readme.io/reference/file-behaviour-summary-object#relationships))",
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
        "summary": "Get objects related to a behaviour report"
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

← [Get object descriptors related to a behaviour report](file_behaviourssandbox_idrelationshipsrelationship.md) · [up](../README.md) · [Get a summary of all MITRE ATT&CK techniques observed in a file](get-a-summary-of-all-mitre-attck-techniques-observed-in-a-file.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file_behaviourssandbox_idrelationship>.*
