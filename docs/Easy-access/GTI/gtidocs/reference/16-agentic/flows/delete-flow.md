---
title: "Delete a Flow"
source: https://gtidocs.virustotal.com/reference/delete-flow
slug: delete-flow
section: reference
group: "agentic"
updatedAt: 2026-08-04T08:18:35.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [agentic](../README.md) › [Flows](../flows.md) › Delete a Flow

---

# delete-a-flow

Delete an existing Agentic Flow.

Permanently deletes a Flow. This also removes the Flow's trigger; its past executions are retained unless separately deleted. Requires owner or editor access.

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
      "name": "Flows"
    }
  ],
  "security": [],
  "paths": {
    "/flows/{id}": {
      "delete": {
        "tags": [
          "Flows"
        ],
        "deprecated": false,
        "operationId": "delete-flow",
        "parameters": [
          {
            "description": "Flow ID.",
            "in": "path",
            "name": "id",
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
          },
          {
            "description": "Optional. ID of the group whose API quota should be charged for the request. If omitted, the parent group's quota is used. Only relevant when your API key belongs to more than one group (multi-tenancy).",
            "in": "header",
            "name": "X-Active-Group",
            "required": false,
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
                    "value": "{\n  \"data\": {}\n}"
                  }
                },
                "schema": {
                  "type": "object"
                }
              }
            },
            "description": "Empty object on success."
          }
        },
        "security": [],
        "summary": "Delete a Flow"
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

← [Update a Flow](update-flow.md) · [up](../README.md) · [Run a Flow now](execute-flow.md) →

*Archived from <https://gtidocs.virustotal.com/reference/delete-flow>.*
