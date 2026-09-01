---
title: "List Flow Executions"
source: https://gtidocs.virustotal.com/reference/list-flow-executions
slug: list-flow-executions
section: reference
group: "agentic"
updatedAt: 2026-08-04T08:18:35.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [agentic](../README.md) › [Flow Executions](../flow-executions.md) › List Flow Executions

---

# list-flow-executions

Retrieve a list of Agentic Flow Executions.

Returns the [Flow Executions](../../17-api-objects/flow-execution-object.md) owned by the caller. Supports `filter` (e.g. `flow_id:<id>`, `status:running`), `order`, and cursor pagination.

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
    "/flow_executions": {
      "get": {
        "tags": [
          "Flow Executions"
        ],
        "deprecated": false,
        "operationId": "list-flow-executions",
        "parameters": [
          {
            "description": "Maximum number of executions to return.",
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
            "description": "Filter expression using search-modifier syntax (e.g. `flow_id:f2e7c4a0-...`, `status:completed`, `duration:10+`).",
            "in": "query",
            "name": "filter",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Sort spec: `<field>` / `<field>+` / `<field>-`. Sortable fields: `creation_date`, `last_modification_date`, `duration_seconds`, `status`.",
            "in": "query",
            "name": "order",
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
                    "value": "{\n  \"data\": [\n    {\n      \"type\": \"flow_execution\",\n      \"id\": \"9a1b2c3d-4e5f-6071-8293-a4b5c6d7e8f9\",\n      \"attributes\": {\n        \"flow_id\": \"f2e7c4a0-1b2c-4d3e-8f90-abcdef012345\",\n        \"status\": \"EXECUTION_STATUS_COMPLETED\",\n        \"duration_seconds\": 42,\n        \"steps\": [\n          {\n            \"step_id\": \"s1\",\n            \"node_id\": \"n2\",\n            \"node_type\": \"NODE_TYPE_RUN_PROMPT\",\n            \"status\": \"STEP_STATUS_SUCCESS\",\n            \"started_at\": 1783939205,\n            \"ended_at\": 1783939240,\n            \"duration_seconds\": 35,\n            \"run_prompt_output\": {\n              \"session_id\": \"1234567890123456789\",\n              \"gti_agentic_response\": \"Found 12 new malicious URLs...\"\n            }\n          },\n          {\n            \"step_id\": \"s2\",\n            \"node_id\": \"n3\",\n            \"node_type\": \"NODE_TYPE_SEND_EMAIL\",\n            \"status\": \"STEP_STATUS_SUCCESS\",\n            \"started_at\": 1783939240,\n            \"ended_at\": 1783939247,\n            \"duration_seconds\": 7,\n            \"send_email_output\": {\n              \"dispatched\": true\n            }\n          }\n        ],\n        \"creation_date\": 1783939200,\n        \"last_modification_date\": 1783939247\n      },\n      \"links\": {\n        \"self\": \"https://www.virustotal.com/api/v3/flow_executions/9a1b2c3d-4e5f-6071-8293-a4b5c6d7e8f9\"\n      }\n    }\n  ],\n  \"links\": {\n    \"self\": \"https://www.virustotal.com/api/v3/flow_executions\"\n  },\n  \"meta\": {\n    \"count\": 1,\n    \"cursor\": \"eyJvZmZzZXQiOjEwfQ==\"\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object"
                }
              }
            },
            "description": "List of Flow Execution objects."
          }
        },
        "security": [],
        "summary": "List Flow Executions"
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

← [Flow Executions](../flow-executions.md) · [up](../README.md) · [Get a Flow Execution](info-flow-execution.md) →

*Archived from <https://gtidocs.virustotal.com/reference/list-flow-executions>.*
