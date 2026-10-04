---
title: "Get a group object"
source: https://gtidocs.virustotal.com/reference/groups
slug: groups
section: reference
group: "Users and group management"
updatedAt: 2026-02-09T10:05:58.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Users and group management](../README.md) › [Group Management](../group-management.md) › Get a group object

---

# get-a-group-object

This endpoint returns a [Group](../../17-api-objects/group-object.md)  object.

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
    "/groups/{id}": {
      "get": {
        "tags": [
          "Group Management"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "groups",
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
        "summary": "Get a group object"
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

← [Group Management](../group-management.md) · [up](../README.md) · [Update a group object](patch-group.md) →

*Archived from <https://gtidocs.virustotal.com/reference/groups>.*
