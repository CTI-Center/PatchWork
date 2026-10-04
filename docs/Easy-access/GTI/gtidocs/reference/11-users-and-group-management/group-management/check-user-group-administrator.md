---
title: "Check if a user is a group admin"
source: https://gtidocs.virustotal.com/reference/check-user-group-administrator
slug: check-user-group-administrator
section: reference
group: "Users and group management"
updatedAt: 2025-09-25T00:38:58.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Users and group management](../README.md) › [Group Management](../group-management.md) › Check if a user is a group admin

---

# check-if-a-user-is-a-group-admin

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
      "name": "Group Management"
    }
  ],
  "paths": {
    "/groups/{id}/relationships/administrators/{user_id}": {
      "get": {
        "tags": [
          "Group Management"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "check-user-group-administrator",
        "parameters": [
          {
            "description": "Group id",
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
            "description": "User ID to check.",
            "in": "path",
            "name": "user_id",
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
                    "value": "{\n  \"data\": true\n}"
                  }
                },
                "schema": {
                  "properties": {
                    "data": {
                      "default": true,
                      "type": "boolean"
                    }
                  },
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
        "summary": "Check if a user is a group admin"
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

← [Manage Roles](patch-group-users-roles.md) · [up](../README.md) · [Get group users](get-group-users.md) →

*Archived from <https://gtidocs.virustotal.com/reference/check-user-group-administrator>.*
