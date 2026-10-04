---
title: "Remove a user from a group"
source: https://gtidocs.virustotal.com/reference/delete-user-from-group
slug: delete-user-from-group
section: reference
group: "Users and group management"
updatedAt: 2025-09-25T00:38:59.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Users and group management](../README.md) › [Group Management](../group-management.md) › Remove a user from a group

---

# remove-a-user-from-a-group

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
    "/groups/{id}/relationships/users/{user_id}": {
      "delete": {
        "tags": [
          "Group Management"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "delete-user-from-group",
        "parameters": [
          {
            "description": "Group ID",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "User to remove.",
            "in": "path",
            "name": "user_id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Your API key.",
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
        "summary": "Remove a user from a group"
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

← [Add users to a group](update-group-users.md) · [up](../README.md) · [Check if a user is a group member](check-user-in-group.md) →

*Archived from <https://gtidocs.virustotal.com/reference/delete-user-from-group>.*
