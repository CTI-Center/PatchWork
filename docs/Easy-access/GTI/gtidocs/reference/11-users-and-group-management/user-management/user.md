---
title: "Get a user object"
source: https://gtidocs.virustotal.com/reference/user
slug: user
section: reference
group: "Users and group management"
updatedAt: 2026-02-09T10:03:38.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Users and group management](../README.md) › [User Management](../user-management.md) › Get a user object

---

# get-a-user-object

This endpoint returns a [User](../../17-api-objects/user-object.md) object. The user can be retrieved either by user ID or by API key, but the former only works if the requester is the user himself or an administrator of a group the user belongs to.

<br />

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
      "get": {
        "tags": [
          "User Management"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "user",
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
        "security": [],
        "summary": "Get a user object"
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

← [Delete a user](delete-user-id.md) · [up](../README.md) · [Update a user object](patch-user-id.md) →

*Archived from <https://gtidocs.virustotal.com/reference/user>.*
