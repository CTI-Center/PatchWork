---
title: "Add a vote to a comment"
source: https://gtidocs.virustotal.com/reference/vote-comment
slug: vote-comment
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T02:04:31.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Comments](../comments.md) › Add a vote to a comment

---

# add-a-vote-to-a-comment

```json Example response
{
    "data": {
        "abuse": 0,
        "negative": 0,
        "positive": 1
    }
}
```

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
      "name": "Comments"
    }
  ],
  "paths": {
    "/comments/{id}/vote": {
      "post": {
        "tags": [
          "Comments"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "vote-comment",
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
            "description": "Comment ID",
            "in": "path",
            "name": "id",
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
                    "description": "Vote type. Can be either `positive`, `negative` or `abuse`",
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
        "summary": "Add a vote to a comment"
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

← [Get object descriptors related to a comment](comments-relationships-ids.md) · [up](../README.md) · [Get objects related to a comment](comments-relationships.md) →

*Archived from <https://gtidocs.virustotal.com/reference/vote-comment>.*
