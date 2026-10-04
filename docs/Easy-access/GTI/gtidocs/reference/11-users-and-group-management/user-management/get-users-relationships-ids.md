---
title: "Get object descriptors related to a user"
source: https://gtidocs.virustotal.com/reference/get-users-relationships-ids
slug: get-users-relationships-ids
section: reference
group: "Users and group management"
updatedAt: 2026-02-09T10:15:26.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Users and group management](../README.md) › [User Management](../user-management.md) › Get object descriptors related to a user

---

# get-object-descriptors-related-to-a-user

This endpoint mirrors [/users/\{id}/\{relationship}](users-relationships.md)but returns the object's descriptor (IDs and any context attributes) instead of the complete object.

# openapi-definition

```json
{
  "info": {
    "title": "Users and group management",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "User Management"
    }
  ],
  "paths": {
    "/users/{id}/relationships/{relationship}": {
      "get": {
        "tags": [
          "User Management"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-users-relationships-ids",
        "parameters": [
          {
            "description": "Username or API key",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Relationship name (see [table](https://gtidocs.readme.io/reference/user-object#relationships))",
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
        "summary": "Get object descriptors related to a user"
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

← [Update a user object](patch-user-id.md) · [up](../README.md) · [Get objects related to a user](users-relationships.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-users-relationships-ids>.*
