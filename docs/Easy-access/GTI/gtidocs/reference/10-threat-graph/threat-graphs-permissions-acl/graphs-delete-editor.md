---
title: "Revoke edit graph permissions from a user or group"
source: https://gtidocs.virustotal.com/reference/graphs-delete-editor
slug: graphs-delete-editor
section: reference
group: "Threat Graph"
updatedAt: 2025-09-25T00:38:44.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Threat Graph](../README.md) › [Threat Graphs Permissions & ACL](../threat-graphs-permissions-acl.md) › Revoke edit graph permissions from a user or group

---

# revoke-edit-graph-permissions-from-a-user-or-group

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
    "/graphs/{id}/relationships/editors/{user_or_group_id}": {
      "delete": {
        "tags": [
          "Threat Graphs Permissions & ACL"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "graphs-delete-editor",
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
        "security": [],
        "summary": "Revoke edit graph permissions from a user or group"
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

← [Grant users and groups permission to edit a graph](graphs-add-editor.md) · [up](../README.md) · [Check if a user or group can edit a graph](graphs-check-editor.md) →

*Archived from <https://gtidocs.virustotal.com/reference/graphs-delete-editor>.*
