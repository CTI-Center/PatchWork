---
title: "Get object descriptors related to a private file's behaviour report"
source: https://gtidocs.virustotal.com/reference/privatefile-behaviourssandbox-idrelationshipsrelationship
slug: privatefile-behaviourssandbox-idrelationshipsrelationship
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:37:07.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private Files Behaviours](../private-files-behaviours.md) › Get object descriptors related to a private file's behaviour report

---

# get-object-descriptors-related-to-a-private-file's-behaviour-report

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

This endpoint is the same as [/private/file\_behaviours/\{sandbox\_id}/\{relationship}](privatefile-behaviourssandbox-idrelationship.md) except it returns just the related object's IDs (and context attributes, if any) instead of returning all attributes.

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
    "/file_behaviours/{sandbox_id}/relationships/{relationship}": {
      "get": {
        "tags": [
          "Private Files Behaviours"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "privatefile-behaviourssandbox-idrelationshipsrelationship",
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
        "summary": "Get object descriptors related to a private file's behaviour report"
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

← [Get the PCAP file generated during a private file’s behavior analysis](file-behaviourssandbox-idmemdump.md) · [up](../README.md) · [Get objects related to a private file's behaviour report](privatefile-behaviourssandbox-idrelationship.md) →

*Archived from <https://gtidocs.virustotal.com/reference/privatefile-behaviourssandbox-idrelationshipsrelationship>.*
