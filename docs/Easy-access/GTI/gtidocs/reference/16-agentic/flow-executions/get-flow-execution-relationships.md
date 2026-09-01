---
title: "Get objects related to a Flow Execution"
source: https://gtidocs.virustotal.com/reference/get-flow-execution-relationships
slug: get-flow-execution-relationships
section: reference
group: "agentic"
updatedAt: 2026-08-04T08:18:35.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [agentic](../README.md) › [Flow Executions](../flow-executions.md) › Get objects related to a Flow Execution

---

# get-objects-related-to-a-flow-execution

Retrieve objects related to a specific Flow Execution.

Returns objects related to a Flow Execution. Available relationships: `flow` (the current parent Flow), `flow_snapshot` (the Flow definition frozen at execution time), `owner` (the user who triggered it), and `group`. Use `GET /flow_executions/{id}/relationships/{relationship}` for descriptors only.

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
    "/flow_executions/{id}/{relationship}": {
      "get": {
        "tags": [
          "Flow Executions"
        ],
        "deprecated": false,
        "operationId": "get-flow-execution-relationships",
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
                    "value": "{\n  \"data\": {\n    \"type\": \"flow\",\n    \"id\": \"f2e7c4a0-1b2c-4d3e-8f90-abcdef012345\",\n    \"attributes\": {\n      \"name\": \"Daily malicious-URL digest\",\n      \"enabled\": true,\n      \"nodes\": [\n        {\n          \"id\": \"n1\",\n          \"type\": \"NODE_TYPE_SCHEDULE_TIME\",\n          \"name\": \"Every morning\",\n          \"schedule_node\": {\n            \"cron_expression\": \"0 9 * * *\",\n            \"timezone\": \"UTC\"\n          }\n        },\n        {\n          \"id\": \"n2\",\n          \"type\": \"NODE_TYPE_RUN_PROMPT\",\n          \"name\": \"Summarise new detections\",\n          \"run_prompt_node\": {\n            \"prompt\": \"Summarise URLs first seen in the last 24h that are flagged malicious by 5+ engines.\"\n          }\n        },\n        {\n          \"id\": \"n3\",\n          \"type\": \"NODE_TYPE_SEND_EMAIL\",\n          \"name\": \"Email the SOC\",\n          \"send_email_node\": {\n            \"notification_emails\": [\n              \"soc@example.com\"\n            ],\n            \"email_subject\": \"Daily malicious-URL digest\",\n            \"message\": \"See attached summary.\"\n          }\n        }\n      ],\n      \"connections\": [\n        {\n          \"source_node_id\": \"n1\",\n          \"target_node_id\": \"n2\",\n          \"source_handle\": \"\"\n        },\n        {\n          \"source_node_id\": \"n2\",\n          \"target_node_id\": \"n3\",\n          \"source_handle\": \"\"\n        }\n      ],\n      \"trigger_state\": {\n        \"last_run_at\": 1783852800\n      },\n      \"creation_date\": 1783334400,\n      \"last_modification_date\": 1783939200\n    },\n    \"links\": {\n      \"self\": \"https://www.virustotal.com/api/v3/flows/f2e7c4a0-1b2c-4d3e-8f90-abcdef012345\"\n    },\n    \"relationships\": {\n      \"group\": {\n        \"data\": {\n          \"type\": \"group\",\n          \"id\": \"acmecorp\"\n        }\n      }\n    }\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object"
                }
              }
            },
            "description": "The related object."
          }
        },
        "security": [],
        "summary": "Get objects related to a Flow Execution"
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

← [Get a Flow Execution](info-flow-execution.md) · [up](../README.md) · [Get object descriptors related to a Flow Execution](get-flow-execution-related-descriptors.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-flow-execution-relationships>.*
