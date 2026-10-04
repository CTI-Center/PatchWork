---
title: "List sessions"
source: https://gtidocs.virustotal.com/reference/list-sessions
slug: list-sessions
section: reference
group: "agentic"
updatedAt: 2026-08-04T08:18:35.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [agentic](../README.md) › [Sessions](../sessions.md) › List sessions

---

# list-sessions

Lists [sessions](../../17-api-objects/agentic-session-object.md) for the authenticated user, with support for cursor-based pagination.

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
    "/agentspace/sessions": {
      "get": {
        "operationId": "list-sessions",
        "summary": "List sessions",
        "tags": [
          "Sessions"
        ],
        "deprecated": false,
        "parameters": [
          {
            "name": "limit",
            "in": "query",
            "required": false,
            "description": "Maximum number of sessions to return per page.",
            "schema": {
              "type": "integer",
              "default": 5
            }
          },
          {
            "name": "cursor",
            "in": "query",
            "required": false,
            "description": "A token identifying a page of results.",
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
            "description": "A list of sessions.",
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

← [Sessions](../sessions.md) · [up](../README.md) · [Get a session](get-session.md) →

*Archived from <https://gtidocs.virustotal.com/reference/list-sessions>.*
