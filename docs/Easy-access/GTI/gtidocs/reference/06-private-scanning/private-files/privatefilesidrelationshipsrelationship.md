---
title: "Get object descriptors related to a file"
source: https://gtidocs.virustotal.com/reference/privatefilesidrelationshipsrelationship
slug: privatefilesidrelationshipsrelationship
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:36:58.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private Files](../private-files.md) › Get object descriptors related to a file

---

# get-object-descriptors-related-to-a-file

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

This endpoint is the same as [/files/\{id}/\{relationship}](private-files-relationships.md) except it returns just the related object's IDs (and context attributes, if any) instead of returning all attributes.

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
      "name": "Private Files"
    }
  ],
  "paths": {
    "/files/{id}/relationships/{relationship}": {
      "get": {
        "tags": [
          "Private Files"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "privatefilesidrelationshipsrelationship",
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
            "description": "File's SHA-256",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Relationship name (see [table](https://gtidocs.readme.io/reference/private-files-object#relationships))",
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
        "summary": "Get object descriptors related to a file"
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

← [Get a private file report](private-files-info.md) · [up](../README.md) · [Get objects related to a private file](private-files-relationships.md) →

*Archived from <https://gtidocs.virustotal.com/reference/privatefilesidrelationshipsrelationship>.*
