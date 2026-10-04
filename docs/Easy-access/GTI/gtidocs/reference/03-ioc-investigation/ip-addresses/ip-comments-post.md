---
title: "Add a comment to an IP address"
source: https://gtidocs.virustotal.com/reference/ip-comments-post
slug: ip-comments-post
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T02:03:33.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [IP addresses](../ip-addresses.md) › Add a comment to an IP address

---

# add-a-comment-to-an-ip-address

With this endpoint you can post a comment for a given IP address. The body for the POST request must be the JSON representation of a comment object. Notice however that you don't need to provide an ID for the object, as they are automatically generated for new comments.

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

Returns a [Comment](../../17-api-objects/comment-object.md) object.

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
      "name": "IP addresses"
    }
  ],
  "paths": {
    "/ip_addresses/{ip}/comments": {
      "post": {
        "tags": [
          "IP addresses"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "ip-comments-post",
        "parameters": [
          {
            "description": "IP address",
            "in": "path",
            "name": "ip",
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
        "summary": "Add a comment to an IP address"
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

← [Request an IP address (re)scan](ip-analyse.md) · [up](../README.md) · [Get object descriptors related to an IP address](ip-relationships-ids.md) →

*Archived from <https://gtidocs.virustotal.com/reference/ip-comments-post>.*
