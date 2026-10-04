---
title: "Check if a user is a group member"
source: https://gtidocs.virustotal.com/reference/check-user-in-group
slug: check-user-in-group
section: reference
group: "Users and group management"
updatedAt: 2025-09-25T00:39:00.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Users and group management](../README.md) › [Group Management](../group-management.md) › Check if a user is a group member

---

# check-if-a-user-is-a-group-member

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
      "get": {
        "tags": [
          "Group Management"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "check-user-in-group",
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
            "description": "User to check.",
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
        "summary": "Check if a user is a group member"
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

← [Remove a user from a group](delete-user-from-group.md) · [up](../README.md) · [Get object descriptors related to a group](groups-relationships-ids.md) →

*Archived from <https://gtidocs.virustotal.com/reference/check-user-in-group>.*
