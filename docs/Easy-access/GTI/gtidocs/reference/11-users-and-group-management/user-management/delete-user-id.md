---
title: "Delete a user"
source: https://gtidocs.virustotal.com/reference/delete-user-id
slug: delete-user-id
section: reference
group: "Users and group management"
updatedAt: 2025-09-25T02:07:20.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Users and group management](../README.md) › [User Management](../user-management.md) › Delete a user

---

# delete-a-user

This request deletes a given user. A user account can only be deleted by its owner, a 403 error is returned otherwise.

An additional `x-user-password` header is required, which is used as confirmation.

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
    "/users/{id}": {
      "delete": {
        "tags": [
          "User Management"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "delete-user-id",
        "parameters": [
          {
            "description": "User ID or API key",
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
          },
          {
            "description": "User password, needed as confirmation.",
            "in": "header",
            "name": "x-user-password",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "text/plain": {
                "examples": {
                  "Result": {
                    "value": ""
                  }
                }
              }
            },
            "description": "200"
          },
          "403": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"error\": {\n    \"code\": \"ForbiddenError\",\n    \"message\": \"You are not authorized to perform the requested operation\"\n  }\n}"
                  }
                },
                "schema": {
                  "properties": {
                    "error": {
                      "properties": {
                        "code": {
                          "type": "string"
                        },
                        "message": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    }
                  },
                  "type": "object"
                }
              }
            },
            "description": "403"
          }
        },
        "security": [],
        "summary": "Delete a user"
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

← [User Management](../user-management.md) · [up](../README.md) · [Get a user object](user.md) →

*Archived from <https://gtidocs.virustotal.com/reference/delete-user-id>.*
