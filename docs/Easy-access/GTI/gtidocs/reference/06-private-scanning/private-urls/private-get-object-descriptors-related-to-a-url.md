---
title: "Get object descriptors related to a private URL"
source: https://gtidocs.virustotal.com/reference/private-get-object-descriptors-related-to-a-url
slug: private-get-object-descriptors-related-to-a-url
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:37:19.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private URLs](../private-urls.md) › Get object descriptors related to a private URL

---

# get-object-descriptors-related-to-a-private-url

This endpoint is the same as [/private/urls/\{id}/\{relationship}](private-get-objects-related-to-a-url.md) except it returns just the related object's IDs (and context attributes, if any) instead of returning all attributes.

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
      "name": "Private URLs"
    }
  ],
  "paths": {
    "/urls/{id}/relationships/{relationship}": {
      "get": {
        "tags": [
          "Private URLs"
        ],
        "summary": "Get object descriptors related to a private URL",
        "description": "",
        "operationId": "private-get-object-descriptors-related-to-a-url",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "URL ID",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "relationship",
            "in": "path",
            "description": "Relationship name (see [table](https://gtidocs.readme.io/reference/private-urls-object#relationships))",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Maximum number of related objects to retrieve",
            "schema": {
              "type": "string",
              "default": "10"
            }
          },
          {
            "name": "cursor",
            "in": "query",
            "description": "Continuation cursor",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "x-apikey",
            "in": "header",
            "description": "Your API key",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          }
        },
        "deprecated": false
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

← [Get objects related to a private URL](private-get-objects-related-to-a-url.md) · [up](../README.md) · [Private Zipping files](../private-zipping-files.md) →

*Archived from <https://gtidocs.virustotal.com/reference/private-get-object-descriptors-related-to-a-url>.*
