---
title: "Get a graph object"
source: https://gtidocs.virustotal.com/reference/graphs-info
slug: graphs-info
section: reference
group: "Threat Graph"
updatedAt: 2025-09-25T00:38:37.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Threat Graph](../README.md) › [Threat Graphs](../threat-graphs.md) › Get a graph object

---

# get-a-graph-object

Returns a [Graph](../../17-api-objects/graph-object.md) object.

```json Response example
{
  "data": {
    "attributes": {
      "graph_data": {
        "description": "Hooli.com investigation"
      },
      "links": [
        {
          "connection_type": "resolutions",
          "source": "www.hooli.com",
          "target": "relationships_resolutions_wwwhoolicom"
        },
        {
          "connection_type": "resolutions",
          "source": "relationships_resolutions_wwwhoolicom",
          "target": "8.8.8.8"
        }
      ],
      "private": false,
      "creation_date": 1530006951,
      "position": {
        "y": 388,
        "x": 897,
        "scale": "1"
      },
      "nodes": [
        {
          "index": 0,
          "entity_id": "www.hooli.com",
          "text": "Root Node",
          "y": 65,
          "x": -18,
          "type": "domain"
        },
        {
          "y": 42,
          "index": 1,
          "entity_id": "relationships_resolutions_wwwhoolicom",
          "type": "relationship",
          "x": -56
        },
        {
          "index": 2,
          "entity_id": "8.8.8.8",
          "fx": 3.3,
          "fy": 4.4,
          "y": 0,
          "x": -64,
          "type": "ip_address"
        },
        {
          "index": 2,
          "entity_id": "131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267",
          "fx": 3.3,
          "fy": 4.4,
          "y": 0,
          "x": -64,
          "type": "file"
        },
        {
          "index": 2,
          "entity_id": "1a0556926f7e76419d12e4c6ad52f10388af11f2689f6c0fb6111a2b85f131de",
          "fx": 3.3,
          "fy": 4.4,
          "y": 0,
          "x": -64,
          "type": "url"
        }
      ]
    },
    "type": "graph",
    "id": "g3ad78ce6c21ae675e81ac376a6fc016c37befa6dc87484b95a2b069f8d04ef44",
    "links": {
      "self": "https://www.virustotal.com/api/v3/graphs/g3ad78ce6c21ae675e81ac376a6fc016c37befa6dc87484b95a2b069f8d04ef44"
    }
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
      "name": "Threat Graphs"
    }
  ],
  "paths": {
    "/graphs/{id}": {
      "get": {
        "tags": [
          "Threat Graphs"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "graphs-info",
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
        "summary": "Get a graph object"
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

← [Delete a graph](graphs-delete.md) · [up](../README.md) · [Update a graph object](graphs-update.md) →

*Archived from <https://gtidocs.virustotal.com/reference/graphs-info>.*
