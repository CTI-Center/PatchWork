---
title: "Get object descriptors related to a URL"
source: https://gtidocs.virustotal.com/reference/urls-relationships-ids
slug: urls-relationships-ids
section: reference
group: "IoC Investigation"
updatedAt: 2026-05-26T09:30:11.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [URLs](../urls.md) › Get object descriptors related to a URL

---

# get-object-descriptors-related-to-a-url

> 📘 See [URL identifiers](../urls.md#url-identifiers) from more information about how to generate a valid URL identifier for a URL.

This endpoint is the same as [/urls/\{id}/\{relationship}](../../01-api-introduction/api-responses/introduction-relationships.md) except it returns just the related object's IDs (and context attributes, if any) instead of returning all attributes.

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
    "/urls/{id}/relationships/{relationship}": {
      "get": {
        "tags": [
          "URLs"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "urls-relationships-ids",
        "parameters": [
          {
            "description": "URL ID",
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
            "description": "Maximum number of related objects to retrieve",
            "in": "query",
            "name": "limit",
            "schema": {
              "default": "10",
              "type": "string"
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
        "summary": "Get object descriptors related to a URL"
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

← [Add a comment on a URL](urls-comments-post.md) · [up](../README.md) · [Get votes on a URL](urls-votes-get.md) →

*Archived from <https://gtidocs.virustotal.com/reference/urls-relationships-ids>.*
