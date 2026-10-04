---
title: "Delete a session"
source: https://gtidocs.virustotal.com/reference/delete-session
slug: delete-session
section: reference
group: "agentic"
updatedAt: 2026-08-04T08:18:35.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [agentic](../README.md) › [Sessions](../sessions.md) › Delete a session

---

# delete-a-session

Deletes a [session](../../17-api-objects/agentic-session-object.md) by its ID.

# openapi-definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "Agentic",
    "version": "1.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3"
    }
  ],
  "tags": [
    {
      "name": "Sessions",
      "description": "Create, list, retrieve, update, delete and share agentic sessions."
    }
  ],
  "security": [],
  "paths": {
    "/agentspace/sessions/{session_id}": {
      "delete": {
        "operationId": "delete-session",
        "summary": "Delete a session",
        "tags": [
          "Sessions"
        ],
        "deprecated": false,
        "parameters": [
          {
            "name": "session_id",
            "in": "path",
            "required": true,
            "description": "The unique identifier of the session.",
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
            "description": "Session deleted successfully."
          }
        },
        "security": []
      }
    }
  },
  "x-readme": {
    "explorer-enabled": true,
    "headers": [],
    "proxy-enabled": false,
    "samples-enabled": true
  }
}
```

---

← [Update a session](update-session.md) · [up](../README.md) · [Activity Log](../../17-api-objects/activity-log.md) →

*Archived from <https://gtidocs.virustotal.com/reference/delete-session>.*
