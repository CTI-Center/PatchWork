---
title: "Get objects related to a comment"
source: https://gtidocs.virustotal.com/reference/comments-relationships
slug: comments-relationships
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T00:35:46.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Comments](../comments.md) › Get objects related to a comment

---

# get-objects-related-to-a-comment

Comment objects are related to other objects in the Google Threat Intelligence dataset. As mentioned in the [Relationships](../../01-api-introduction/api-responses/introduction-relationships.md) section, those related objects can be retrieved by sending `GET` requests to the relationships endpoint.

All available relationships are documented in the [Comment](../../17-api-objects/comment-object.md) API object page.

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
    "/comments/{id}/{relationship}": {
      "get": {
        "tags": [
          "Comments"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "comments-relationships",
        "parameters": [
          {
            "description": "Comment identifier",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Relationship name (see [table](https://gtidocs.readme.io/reference/comment-object#relationships))",
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
          }
        },
        "security": [],
        "summary": "Get objects related to a comment"
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

← [Add a vote to a comment](vote-comment.md) · [up](../README.md) · [Analyses, Submissions & Operations](../analyses-submissions-operations.md) →

*Archived from <https://gtidocs.virustotal.com/reference/comments-relationships>.*
