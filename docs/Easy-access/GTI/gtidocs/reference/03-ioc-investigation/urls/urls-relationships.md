---
title: "Get objects related to a URL"
source: https://gtidocs.virustotal.com/reference/urls-relationships
slug: urls-relationships
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T00:35:40.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [URLs](../urls.md) › Get objects related to a URL

---

# get-objects-related-to-a-url

> 📘 See [URL identifiers](../urls.md#url-identifiers) from more information about how to generate a valid URL identifier for a URL.

URL objects have number of relationships to other URLs and objects. As mentioned in the [Relationships](../../01-api-introduction/api-responses/introduction-relationships.md) section, those related objects can be retrieved by sending `GET` requests to the relationship URL.

The relationships supported by URL objects are documented in the [URL](../../17-api-objects/url-object.md) API object page.

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
      "name": "URLs"
    }
  ],
  "paths": {
    "/urls/{id}/{relationship}": {
      "get": {
        "tags": [
          "URLs"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "urls-relationships",
        "parameters": [
          {
            "description": "URL identifier",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Relationship name (see [table](https://gtidocs.readme.io/reference/url-object#relationships))",
            "in": "path",
            "name": "relationship",
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
        "security": [],
        "summary": "Get objects related to a URL"
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

← [Add a vote on a URL](urls-votes-post.md) · [up](../README.md) · [Get a URL's latest analysis screenshot](urls-screenshot.md) →

*Archived from <https://gtidocs.virustotal.com/reference/urls-relationships>.*
