---
title: "Get object descriptors related to a Flow"
source: https://gtidocs.virustotal.com/reference/get-flow-related-descriptors
slug: get-flow-related-descriptors
section: reference
group: "agentic"
updatedAt: 2026-08-04T08:18:35.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [agentic](../README.md) › [Flows](../flows.md) › Get object descriptors related to a Flow

---

# get-object-descriptors-related-to-a-flow

Retrieve descriptors (type + id) of objects related to an Agentic Flow.

This endpoint is the same as [`GET /flows/{id}/{relationship}`](get-flow-relationships.md) except it returns just the related object's [descriptor](https://gtidocs.readme.io/docs/api-relationships) (`type` and `id`) instead of its full attributes.

Available relationships: `group` and `flow_executions`.

## examples

Get the descriptors of the executions related to a Flow.

```python
import requests

object_id = "f2e7c4a0-1b2c-4d3e-8f90-abcdef012345"
relationship = "flow_executions"
limit = "10"
url = f"https://www.virustotal.com/api/v3/flows/{object_id}/relationships/{relationship}?limit={limit}"
headers = {"accept": "application/json", "x-apikey": <api-key>}
response = requests.get(url, headers=headers)
```

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
    "/flows/{id}/relationships/{relationship}": {
      "get": {
        "tags": [
          "Flows"
        ],
        "deprecated": false,
        "description": "Returns the descriptors (`type` and `id` only) of objects related to a Flow. Same as `GET /flows/{id}/{relationship}` but returns just the related object's descriptor instead of its full attributes. Available relationships: `group` and `flow_executions`.",
        "operationId": "get-flow-related-descriptors",
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
            "description": "Relationship name: `group` or `flow_executions`.",
            "in": "path",
            "name": "relationship",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Maximum number of related object descriptors to return.",
            "in": "query",
            "name": "limit",
            "schema": {
              "default": 10,
              "format": "int32",
              "type": "integer",
              "maximum": 40,
              "minimum": 0
            }
          },
          {
            "description": "Continuation cursor.",
            "in": "query",
            "name": "cursor",
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
                    "value": "{\n  \"data\": [\n    {\n      \"type\": \"flow_execution\",\n      \"id\": \"9a1b2c3d-4e5f-6071-8293-a4b5c6d7e8f9\"\n    }\n  ],\n  \"links\": {\n    \"self\": \"https://www.virustotal.com/api/v3/flows/f2e7c4a0-1b2c-4d3e-8f90-abcdef012345/relationships/flow_executions\"\n  },\n  \"meta\": {\n    \"count\": 1,\n    \"cursor\": \"eyJvZmZzZXQiOjEwfQ==\"\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object"
                }
              }
            },
            "description": "Related object descriptors (type + id)."
          }
        },
        "security": [],
        "summary": "Get object descriptors related to a Flow"
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

← [Get objects related to a Flow](get-flow-relationships.md) · [up](../README.md) · [Unsubscribe from a Flow's email notifications](unsubscribe-flow.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-flow-related-descriptors>.*
