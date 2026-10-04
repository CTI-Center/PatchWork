---
title: "Get objects related to a Flow"
source: https://gtidocs.virustotal.com/reference/get-flow-relationships
slug: get-flow-relationships
section: reference
group: "agentic"
updatedAt: 2026-08-04T08:18:35.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [agentic](../README.md) › [Flows](../flows.md) › Get objects related to a Flow

---

# get-objects-related-to-a-flow

Retrieve objects related to a specific Agentic Flow.

Returns objects related to a Flow. Available relationships: `group` (the owning group) and `flow_executions` (the Flow's execution history). Use `GET /flows/{id}/relationships/{relationship}` instead to get object [descriptors](https://gtidocs.readme.io/docs/api-relationships) (type + id only) rather than full objects.

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
    "/flows/{id}/{relationship}": {
      "get": {
        "tags": [
          "Flows"
        ],
        "deprecated": false,
        "operationId": "get-flow-relationships",
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
            "description": "Maximum number of related objects to return.",
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
                    "value": "{\n  \"data\": [\n    {\n      \"type\": \"flow_execution\",\n      \"id\": \"9a1b2c3d-4e5f-6071-8293-a4b5c6d7e8f9\",\n      \"attributes\": {\n        \"flow_id\": \"f2e7c4a0-1b2c-4d3e-8f90-abcdef012345\",\n        \"status\": \"EXECUTION_STATUS_COMPLETED\",\n        \"duration_seconds\": 42,\n        \"steps\": [\n          {\n            \"step_id\": \"s1\",\n            \"node_id\": \"n2\",\n            \"node_type\": \"NODE_TYPE_RUN_PROMPT\",\n            \"status\": \"STEP_STATUS_SUCCESS\",\n            \"started_at\": 1783939205,\n            \"ended_at\": 1783939240,\n            \"duration_seconds\": 35,\n            \"run_prompt_output\": {\n              \"session_id\": \"1234567890123456789\",\n              \"gti_agentic_response\": \"Found 12 new malicious URLs...\"\n            }\n          },\n          {\n            \"step_id\": \"s2\",\n            \"node_id\": \"n3\",\n            \"node_type\": \"NODE_TYPE_SEND_EMAIL\",\n            \"status\": \"STEP_STATUS_SUCCESS\",\n            \"started_at\": 1783939240,\n            \"ended_at\": 1783939247,\n            \"duration_seconds\": 7,\n            \"send_email_output\": {\n              \"dispatched\": true\n            }\n          }\n        ],\n        \"creation_date\": 1783939200,\n        \"last_modification_date\": 1783939247\n      },\n      \"links\": {\n        \"self\": \"https://www.virustotal.com/api/v3/flow_executions/9a1b2c3d-4e5f-6071-8293-a4b5c6d7e8f9\"\n      }\n    }\n  ],\n  \"links\": {\n    \"self\": \"https://www.virustotal.com/api/v3/flows/f2e7c4a0-1b2c-4d3e-8f90-abcdef012345/flow_executions\"\n  },\n  \"meta\": {\n    \"count\": 1\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object"
                }
              }
            },
            "description": "Related objects."
          }
        },
        "security": [],
        "summary": "Get objects related to a Flow"
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

← [Run a Flow now](execute-flow.md) · [up](../README.md) · [Get object descriptors related to a Flow](get-flow-related-descriptors.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-flow-relationships>.*
