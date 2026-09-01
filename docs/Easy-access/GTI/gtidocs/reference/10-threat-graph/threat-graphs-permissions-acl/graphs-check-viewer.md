---
title: "Check if a user or group can view a graph"
source: https://gtidocs.virustotal.com/reference/graphs-check-viewer
slug: graphs-check-viewer
section: reference
group: "Threat Graph"
updatedAt: 2025-09-25T00:38:46.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Threat Graph](../README.md) › [Threat Graphs Permissions & ACL](../threat-graphs-permissions-acl.md) › Check if a user or group can view a graph

---

# check-if-a-user-or-group-can-view-a-graph

This endpoint returns true if the user has `Viewer` access to the graph.

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
    "/graphs/{id}/relationships/viewers/{user_or_group_id}": {
      "get": {
        "tags": [
          "Threat Graphs Permissions & ACL"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "graphs-check-viewer",
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
          },
          {
            "description": "User or group ID",
            "in": "path",
            "name": "user_or_group_id",
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
                    "value": "{\n    \"data\": true\n}"
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
          }
        },
        "security": [],
        "summary": "Check if a user or group can view a graph"
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

← [Revoke view permission from a user or group](graphs-delete-viewer.md) · [up](../README.md) · [Get users and groups that can view a graph](graphs-viewers.md) →

*Archived from <https://gtidocs.virustotal.com/reference/graphs-check-viewer>.*
