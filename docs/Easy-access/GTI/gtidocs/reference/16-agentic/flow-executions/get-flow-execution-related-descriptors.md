---
title: "Get object descriptors related to a Flow Execution"
source: https://gtidocs.virustotal.com/reference/get-flow-execution-related-descriptors
slug: get-flow-execution-related-descriptors
section: reference
group: "agentic"
updatedAt: 2026-08-04T08:18:35.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [agentic](../README.md) › [Flow Executions](../flow-executions.md) › Get object descriptors related to a Flow Execution

---

# get-object-descriptors-related-to-a-flow-execution

Retrieve descriptors (type + id) of objects related to a Flow Execution.

This endpoint is the same as [`GET /flow_executions/{id}/{relationship}`](get-flow-execution-relationships.md) except it returns just the related object's [descriptor](https://gtidocs.readme.io/docs/api-relationships) (`type` and `id`) instead of its full attributes.

Available relationships: `flow`, `flow_snapshot`, `owner`, and `group`.

## examples

Get the descriptor of the parent Flow related to a Flow Execution.

```python
import requests

object_id = "9a1b2c3d-4e5f-6071-8293-a4b5c6d7e8f9"
relationship = "flow"
url = f"https://www.virustotal.com/api/v3/flow_executions/{object_id}/relationships/{relationship}"
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
      "name": "Flow Executions"
    }
  ],
  "security": [],
  "paths": {
    "/flow_executions/{id}/relationships/{relationship}": {
      "get": {
        "tags": [
          "Flow Executions"
        ],
        "deprecated": false,
        "description": "Returns the descriptors (`type` and `id` only) of objects related to a Flow Execution. Same as `GET /flow_executions/{id}/{relationship}` but returns just the related object's descriptor instead of its full attributes. Available relationships: `flow`, `flow_snapshot`, `owner`, and `group`.",
        "operationId": "get-flow-execution-related-descriptors",
        "parameters": [
          {
            "description": "Flow Execution ID.",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Relationship name: `flow`, `flow_snapshot`, `owner`, or `group`.",
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
                    "value": "{\n  \"data\": {\n    \"type\": \"flow\",\n    \"id\": \"f2e7c4a0-1b2c-4d3e-8f90-abcdef012345\"\n  },\n  \"links\": {\n    \"self\": \"https://www.virustotal.com/api/v3/flow_executions/9a1b2c3d-4e5f-6071-8293-a4b5c6d7e8f9/relationships/flow\"\n  }\n}"
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
        "summary": "Get object descriptors related to a Flow Execution"
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

← [Get objects related to a Flow Execution](get-flow-execution-relationships.md) · [up](../README.md) · [Cancel a Flow Execution](cancel-flow-execution.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-flow-execution-related-descriptors>.*
