---
title: "Get a session share token"
source: https://gtidocs.virustotal.com/reference/get-session-token
slug: get-session-token
section: reference
group: "agentic"
updatedAt: 2026-08-04T08:18:35.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [agentic](../README.md) › [Sessions](../sessions.md) › Get a session share token

---

# get-a-session-share-token

This endpoint returns a share token for a specific [agentic chat session](../../17-api-objects/agentic-session-object.md), allowing the session to be imported by another user.

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
    "/agentspace/sessions/{session_id}/token": {
      "get": {
        "operationId": "get-session-token",
        "summary": "Get a session share token",
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
            "description": "Share token payload.",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                }
              }
            }
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

← [Get a session](get-session.md) · [up](../README.md) · [Create a session from a shared token](create-session-from-token.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-session-token>.*
