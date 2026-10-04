---
title: "Get objects related to a user"
source: https://gtidocs.virustotal.com/reference/users-relationships
slug: users-relationships
section: reference
group: "Users and group management"
updatedAt: 2025-09-25T00:38:53.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Users and group management](../README.md) › [User Management](../user-management.md) › Get objects related to a user

---

# get-objects-related-to-a-user

Users are related to other objects in our dataset. As mentioned in the [Relationships](../../01-api-introduction/api-responses/introduction-relationships.md) section, those related objects can be retrieved by sending `GET` requests to this API endpoint.

Some relationships are only accessible to their account's owners and their group's admins.

The supported relationships are documented in the [User](../../17-api-objects/user-object.md#relationships) API object page.

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
    "/users/{id}/{relationship}": {
      "get": {
        "tags": [
          "User Management"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "users-relationships",
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
        "summary": "Get objects related to a user"
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

← [Get object descriptors related to a user](get-users-relationships-ids.md) · [up](../README.md) · [Group Management](../group-management.md) →

*Archived from <https://gtidocs.virustotal.com/reference/users-relationships>.*
