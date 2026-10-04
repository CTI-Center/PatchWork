---
title: "Delete a graph"
source: https://gtidocs.virustotal.com/reference/graphs-delete
slug: graphs-delete
section: reference
group: "Threat Graph"
updatedAt: 2025-09-25T00:38:36.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Threat Graph](../README.md) › [Threat Graphs](../threat-graphs.md) › Delete a graph

---

# delete-a-graph

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
      "name": "Threat Graphs"
    }
  ],
  "paths": {
    "/graphs/{id}": {
      "delete": {
        "tags": [
          "Threat Graphs"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "graphs-delete",
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
        "summary": "Delete a graph"
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

← [Create a graph](create-graphs.md) · [up](../README.md) · [Get a graph object](graphs-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/graphs-delete>.*
