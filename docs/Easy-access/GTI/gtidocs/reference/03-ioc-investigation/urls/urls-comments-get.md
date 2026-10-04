---
title: "Get comments on a URL"
source: https://gtidocs.virustotal.com/reference/urls-comments-get
slug: urls-comments-get
section: reference
group: "IoC Investigation"
updatedAt: 2026-02-05T12:43:34.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [URLs](../urls.md) › Get comments on a URL

---

# get-comments-on-a-url

> 📘 See [URL identifiers](../urls.md#url-identifiers) from more information about how to generate a valid URL identifier for a URL.

Returns a list of [Comment](../comments.md) objects.
Check comments done in VT Community regarding a specific URL.

* `data`: list of ("comment" objects)\[ref:comment-object].
* `links`: contains "self" with a reference to this group of comments and "next", with a reference to the next group.
* `cursor`: contains the cursor token used to access the next group of comments.

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
    "/urls/{id}/comments": {
      "get": {
        "tags": [
          "URLs"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "urls-comments-get",
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
            "description": "Maximum number of comments to retrieve",
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
        "summary": "Get comments on a URL"
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

← [Request a URL rescan (re-analyse)](urls-analyse.md) · [up](../README.md) · [Add a comment on a URL](urls-comments-post.md) →

*Archived from <https://gtidocs.virustotal.com/reference/urls-comments-get>.*
