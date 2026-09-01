---
title: "Grant users and groups permission to see a graph"
source: https://gtidocs.virustotal.com/reference/graphs-add-viewer
slug: graphs-add-viewer
section: reference
group: "Threat Graph"
updatedAt: 2025-09-25T00:38:48.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Threat Graph](../README.md) › [Threat Graphs Permissions & ACL](../threat-graphs-permissions-acl.md) › Grant users and groups permission to see a graph

---

# grant-users-and-groups-permission-to-see-a-graph

This endpoint adds a user or group as a graph viewer.

```json Response example
{
    "data": [
        {
            "attributes": {
                "first_name": "Bertram",
                "last_name": "Gilfoyle",
                "profile_phrase": "",
                "reputation": 1,
                "status": "active",
                "user_since": 1530008602
            },
            "id": "gilfoyle",
            "links": {
                "self": "https://www.virustotal.com/api/v3/users/gilfoyle"
            },
            "type": "user"
        }
    ],
    "links": {
        "self": "https://www.virustotal.com/api/v3/graphs/g5598743d5f3c699f1c90e76c2c2d541d41f1b56bd8114c06d181ed3f60cfcada/viewers?limit=10"
    }
}
```

# openapi-definition

```json
{
  "components": {
    "securitySchemes": {
      "sec0": {
        "in": "header",
        "name": "x-apikey",
        "type": "apiKey"
      }
    }
  },
  "info": {
    "title": "Threat Graph",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Threat Graphs Permissions & ACL"
    }
  ],
  "paths": {
    "/graphs/{id}/relationships/viewers": {
      "post": {
        "tags": [
          "Threat Graphs Permissions & ACL"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "graphs-add-viewer",
        "parameters": [
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
            "description": "A 65 char length id which uniquely identify the graph.",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "security": [],
        "summary": "Grant users and groups permission to see a graph"
      }
    }
  },
  "security": [
    {
      "sec0": []
    }
  ],
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

← [Get users and groups that can view a graph](graphs-viewers.md) · [up](../README.md) · [User Management](../../11-users-and-group-management/user-management.md) →

*Archived from <https://gtidocs.virustotal.com/reference/graphs-add-viewer>.*
