---
title: "Get objects related to a graph"
source: https://gtidocs.virustotal.com/reference/graphs-relationships
slug: graphs-relationships
section: reference
group: "Threat Graph"
updatedAt: 2025-09-25T00:38:41.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Threat Graph](../README.md) › [Threat Graphs](../threat-graphs.md) › Get objects related to a graph

---

# get-objects-related-to-a-graph

Graph objects have number of relationships to other objects. As mentioned in the  [Relationships](../../01-api-introduction/api-responses/introduction-relationships.md) section, those related objects can be retrieved by sending `GET` requests to the relationship URL.

Some relationships are accesible only to users who have access to Google Threat Intelligence.

The relationships supported by graph objects are documented in the [Graph](../../17-api-objects/graph-object.md) API object page.

```json Response example for owner
{
    "data": {
        "attributes": {
            "first_name": "Richard",
            "last_name": "Hendricks",
            "profile_phrase": "CEO of Pied Piper",
            "reputation": 1,
            "status": "active",
            "user_since": 1528111032
        },
        "id": "hendricks",
        "links": {
            "self": "https://www.virustotal.com/api/v3/users/hendricks"
        },
        "type": "user"
    },
    "links": {
        "self": "https://www.virustotal.com/api/v3/graphs/g510b3e01190b9e6001f7ed7d14015558b11ca9d3e87367b6b809bbb402645bf2/owner"
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
    "/graphs/{id}/{relationship}": {
      "get": {
        "tags": [
          "Threat Graphs"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "graphs-relationships",
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
            "description": "Relationship name (see [table](https://gtidocs.readme.io/reference/graph-object#relationships))",
            "in": "path",
            "name": "relationship",
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
        "summary": "Get objects related to a graph"
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

← [Get object descriptors related to a graph](graphs-relationships-ids.md) · [up](../README.md) · [Threat Graphs Permissions & ACL](../threat-graphs-permissions-acl.md) →

*Archived from <https://gtidocs.virustotal.com/reference/graphs-relationships>.*
