---
title: "Update a user object"
source: https://gtidocs.virustotal.com/reference/patch-user-id
slug: patch-user-id
section: reference
group: "Users and group management"
updatedAt: 2025-09-25T02:07:22.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Users and group management](../README.md) › [User Management](../user-management.md) › Update a user object

---

# update-a-user-object

This request accepts a JSON body containing the user attributes to update. Attributes not present in the request body remain the same. It returns the updated [User](../../17-api-objects/user-object.md) object.

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
      "patch": {
        "tags": [
          "User Management"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "patch-user-id",
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
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "properties": {
                  "data": {
                    "description": "User object",
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
              "text/plain": {
                "examples": {
                  "Result": {
                    "value": ""
                  }
                }
              }
            },
            "description": "200"
          }
        },
        "security": [],
        "summary": "Update a user object"
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

← [Get a user object](user.md) · [up](../README.md) · [Get object descriptors related to a user](get-users-relationships-ids.md) →

*Archived from <https://gtidocs.virustotal.com/reference/patch-user-id>.*
