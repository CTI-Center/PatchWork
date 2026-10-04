---
title: "Get objects related to a private file's behaviour report"
source: https://gtidocs.virustotal.com/reference/privatefile-behaviourssandbox-idrelationship
slug: privatefile-behaviourssandbox-idrelationship
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:37:08.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private Files Behaviours](../private-files-behaviours.md) › Get objects related to a private file's behaviour report

---

# get-objects-related-to-a-private-file's-behaviour-report

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

As mentioned in the [Relationships](../../01-api-introduction/api-responses/introduction-relationships.md) section, those related objects can be retrieved by sending `GET` requests to the relationship URL.

Available relationships are described in the [private file behaviour](../../17-api-objects/private-file-behaviours-object.md) object documentation.

# openapi-definition

```json
{
  "info": {
    "title": "Private Scanning",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Private Files Behaviours"
    }
  ],
  "paths": {
    "/file_behaviours/{sandbox_id}/{relationship}": {
      "get": {
        "tags": [
          "Private Files Behaviours"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "privatefile-behaviourssandbox-idrelationship",
        "parameters": [
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
            "description": "Sandbox report ID. See \"Sandbox Report identifiers\" section above for more info.",
            "in": "path",
            "name": "sandbox_id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Relationship name (see [table](https://gtidocs.readme.io/reference/private-file-behaviours-object#relationships))",
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
        "summary": "Get objects related to a private file's behaviour report"
      }
    }
  },
  "security": [],
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3/private"
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

← [Get object descriptors related to a private file's behaviour report](privatefile-behaviourssandbox-idrelationshipsrelationship.md) · [up](../README.md) · [Get a summary of all MITRE ATT&CK techniques observed in a file](get-summary-all-mitre-attack-techniques-observed-in-a-file.md) →

*Archived from <https://gtidocs.virustotal.com/reference/privatefile-behaviourssandbox-idrelationship>.*
