---
title: "Get a Flow Execution"
source: https://gtidocs.virustotal.com/reference/info-flow-execution
slug: info-flow-execution
section: reference
group: "agentic"
updatedAt: 2026-08-04T08:18:35.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [agentic](../README.md) › [Flow Executions](../flow-executions.md) › Get a Flow Execution

---

# get-a-flow-execution

Retrieve details of a specific Flow Execution.

Retrieves a single [Flow Execution](../../17-api-objects/flow-execution-object.md), including its per-node `steps` with typed output. Visibility is inherited from the parent Flow: you must have at least viewer access on that Flow, otherwise a 404 is returned.

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
    "/flow_executions/{id}": {
      "get": {
        "tags": [
          "Flow Executions"
        ],
        "deprecated": false,
        "operationId": "info-flow-execution",
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
                    "value": "{\n  \"data\": {\n    \"type\": \"flow_execution\",\n    \"id\": \"9a1b2c3d-4e5f-6071-8293-a4b5c6d7e8f9\",\n    \"attributes\": {\n      \"flow_id\": \"f2e7c4a0-1b2c-4d3e-8f90-abcdef012345\",\n      \"status\": \"EXECUTION_STATUS_COMPLETED\",\n      \"duration_seconds\": 42,\n      \"steps\": [\n        {\n          \"step_id\": \"s1\",\n          \"node_id\": \"n2\",\n          \"node_type\": \"NODE_TYPE_RUN_PROMPT\",\n          \"status\": \"STEP_STATUS_SUCCESS\",\n          \"started_at\": 1783939205,\n          \"ended_at\": 1783939240,\n          \"duration_seconds\": 35,\n          \"run_prompt_output\": {\n            \"session_id\": \"1234567890123456789\",\n            \"gti_agentic_response\": \"Found 12 new malicious URLs...\"\n          }\n        },\n        {\n          \"step_id\": \"s2\",\n          \"node_id\": \"n3\",\n          \"node_type\": \"NODE_TYPE_SEND_EMAIL\",\n          \"status\": \"STEP_STATUS_SUCCESS\",\n          \"started_at\": 1783939240,\n          \"ended_at\": 1783939247,\n          \"duration_seconds\": 7,\n          \"send_email_output\": {\n            \"dispatched\": true\n          }\n        }\n      ],\n      \"creation_date\": 1783939200,\n      \"last_modification_date\": 1783939247\n    },\n    \"links\": {\n      \"self\": \"https://www.virustotal.com/api/v3/flow_executions/9a1b2c3d-4e5f-6071-8293-a4b5c6d7e8f9\"\n    }\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object"
                }
              }
            },
            "description": "The Flow Execution object."
          },
          "404": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"error\": {\n    \"code\": \"NotFoundError\",\n    \"message\": \"Not found.\"\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object"
                }
              }
            },
            "description": "Execution not found or parent Flow not visible."
          }
        },
        "security": [],
        "summary": "Get a Flow Execution"
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

← [List Flow Executions](list-flow-executions.md) · [up](../README.md) · [Get objects related to a Flow Execution](get-flow-execution-relationships.md) →

*Archived from <https://gtidocs.virustotal.com/reference/info-flow-execution>.*
