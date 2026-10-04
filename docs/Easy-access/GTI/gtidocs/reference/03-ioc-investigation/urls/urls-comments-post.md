---
title: "Add a comment on a URL"
source: https://gtidocs.virustotal.com/reference/urls-comments-post
slug: urls-comments-post
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T02:04:23.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [URLs](../urls.md) › Add a comment on a URL

---

# add-a-comment-on-a-url

> 📘 See [URL identifiers](../urls.md#url-identifiers) from more information about how to generate a valid URL identifier for a URL.

With this endpoint you can post a comment for a given URL. The body for the POST request must be the JSON representation of a comment object. Notice however that you don't need to provide an ID for the object, as they are automatically generated for new comments.

Any word starting with # in your comment's text will be considered a tag, and added to the comment's tag attribute.

```json Example request
{
  "data": {
    "type": "comment",
    "attributes": {
    	"text": "Lorem #ipsum dolor sit ..."
    }
  }
}
```

Returns a [Comment](../comments.md) object.

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
      "post": {
        "tags": [
          "URLs"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "urls-comments-post",
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
            "description": "Your API key",
            "in": "header",
            "name": "x-apikey",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "properties": {
                  "data": {
                    "default": "{\"type\": \"comment\", \"attributes\": {\"text\": \"Lorem ipsum dolor sit ...\"}}",
                    "description": "A comment object",
                    "format": "json",
                    "type": "string"
                  }
                },
                "required": [
                  "data"
                ],
                "type": "object"
              }
            }
          }
        },
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
        "summary": "Add a comment on a URL"
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

← [Get comments on a URL](urls-comments-get.md) · [up](../README.md) · [Get object descriptors related to a URL](urls-relationships-ids.md) →

*Archived from <https://gtidocs.virustotal.com/reference/urls-comments-post>.*
