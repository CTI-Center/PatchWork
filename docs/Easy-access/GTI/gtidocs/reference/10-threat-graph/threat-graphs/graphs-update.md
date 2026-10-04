---
title: "Update a graph object"
source: https://gtidocs.virustotal.com/reference/graphs-update
slug: graphs-update
section: reference
group: "Threat Graph"
updatedAt: 2025-09-25T00:38:37.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Threat Graph](../README.md) › [Threat Graphs](../threat-graphs.md) › Update a graph object

---

# update-a-graph-object

```json Update request example
{
  "data":{
    "attributes": {
      "private": true
    },
    "type":"graph"
  }
}
```

```json Response example
{
  "data": {
    "attributes": {
      "private": false,
      "nodes": [
        {
          "type":"domain",
          "entity_id":"www.hooli.com",
          "x":-18,
          "y":65,
          "text":"Root Node",
          "index":0
        },
        {
          "type":"relationship",
          "entity_id":"relationships_resolutions_wwwhoolicom",
          "x":-56,
          "y":42,
          "index":1
        },
        {
          "type":"ip_address",
          "entity_id":"8.8.8.8",
          "x":-64,
          "y":0,
          "index":2,
          "fx":3.3,
          "fy":4.4
        },
        {
          "type":"file",
          "entity_id":"131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267",
          "x":-64,
          "y":0,
          "index":2,
          "fx":3.3,
          "fy":4.4
        },
        {
          "type":"url",
          "entity_id":"1a0556926f7e76419d12e4c6ad52f10388af11f2689f6c0fb6111a2b85f131de",
          "x":-64,
          "y":0,
          "index":2,
          "fx":3.3,
          "fy":4.4
        }
      ],
        "links":[
          {
            "source":"www.hooli.com",
            "target":"relationships_resolutions_wwwhoolicom",
            "connection_type":"resolutions"
          },
          {
            "source":"relationships_resolutions_wwwhoolicom",
            "target":"8.8.8.8",
            "connection_type":"resolutions"
          }
        ],
          "position": {
            "x":897,
              "y":388,
                "scale":"1"
          },
            "graph_data": {
              "description": "Hooli.com graph"
            }
    },
      "type": "graph"
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
      "patch": {
        "tags": [
          "Threat Graphs"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "graphs-update",
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
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "properties": {
                  "graph_data": {
                    "description": "Highlevel graph data.",
                    "properties": {
                      "version": {
                        "description": "Current version of the graph.",
                        "type": "string"
                      }
                    },
                    "type": "object"
                  },
                  "links": {
                    "description": "Array of links.",
                    "items": {
                      "properties": {
                        "connection_type": {
                          "description": "Type of the connection between the source and the target.",
                          "type": "string"
                        },
                        "source": {
                          "description": "Entity id of the link source.",
                          "type": "string"
                        },
                        "target": {
                          "description": "Entity id of the link target.",
                          "type": "string"
                        }
                      },
                      "type": "object"
                    },
                    "type": "array"
                  },
                  "nodes": {
                    "description": "Array of nodes.",
                    "items": {
                      "properties": {
                        "entity_attributes": {
                          "description": "(optional) Entity related attributes.",
                          "type": "object"
                        },
                        "entity_id": {
                          "description": "Node entity id.",
                          "type": "string"
                        },
                        "fx": {
                          "description": "(optional) Force x position.",
                          "format": "float",
                          "type": "number"
                        },
                        "fy": {
                          "description": "(optional) Force y position.",
                          "format": "float",
                          "type": "number"
                        },
                        "index": {
                          "description": "Index of the node list.",
                          "format": "int32",
                          "type": "integer",
                          "minimum": 0
                        },
                        "text": {
                          "description": "(optional) Node label.",
                          "type": "string"
                        },
                        "type": {
                          "description": "Node entity type.",
                          "type": "string"
                        },
                        "x": {
                          "description": "X position of the node.",
                          "format": "float",
                          "type": "number"
                        },
                        "y": {
                          "description": "Y position of the node.",
                          "format": "float",
                          "type": "number"
                        }
                      },
                      "type": "object"
                    },
                    "type": "array"
                  },
                  "private": {
                    "description": "Private status.",
                    "type": "boolean"
                  }
                },
                "type": "object"
              }
            }
          }
        },
        "security": [],
        "summary": "Update a graph object"
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

← [Get a graph object](graphs-info.md) · [up](../README.md) · [Get comments on a graph](get-graph-comments.md) →

*Archived from <https://gtidocs.virustotal.com/reference/graphs-update>.*
