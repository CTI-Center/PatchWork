---
title: "Get comments on a graph"
source: https://gtidocs.virustotal.com/reference/get-graph-comments
slug: get-graph-comments
section: reference
group: "Threat Graph"
updatedAt: 2025-09-25T00:38:38.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Threat Graph](../README.md) › [Threat Graphs](../threat-graphs.md) › Get comments on a graph

---

# get-comments-on-a-graph

This endpoint returns the comments posted in a given graph. Check [Graph comments relationship page](../../17-api-objects/graph-object/graph-comments.md) to know more about the returned object.

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
    "/graphs/{id}/comments": {
      "get": {
        "tags": [
          "Threat Graphs"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-graph-comments",
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
            "description": "Maximum number of related objects to retrieve",
            "in": "query",
            "name": "limit",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Continuation cursor",
            "in": "query",
            "name": "cursor",
            "schema": {
              "type": "string"
            }
          }
        ],
        "security": [],
        "summary": "Get comments on a graph"
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

← [Update a graph object](graphs-update.md) · [up](../README.md) · [Add a comment to a graph](post-graphs-comments.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-graph-comments>.*
