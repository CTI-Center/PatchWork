---
title: "Create a Flow"
source: https://gtidocs.virustotal.com/reference/create-flow
slug: create-flow
section: reference
group: "agentic"
updatedAt: 2026-08-04T08:18:35.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [agentic](../README.md) › [Flows](../flows.md) › Create a Flow

---

# create-a-flow

Create a new Agentic Flow.

Creates a new [Flow](../../17-api-objects/flow-object.md) inside the caller's group. `name` is required (max 255 characters). The graph itself (`nodes` and `connections`) can be supplied at creation time or added later with a partial update. A Flow only runs on its trigger while `enabled` is `true`.

```json Request example
{
  "data": {
    "type": "flow",
    "attributes": {
      "name": "Daily malicious-URL digest",
      "enabled": true,
      "nodes": [
        {
          "id": "n1",
          "type": "NODE_TYPE_SCHEDULE_TIME",
          "name": "Every morning",
          "schedule_node": {
            "cron_expression": "0 9 * * *",
            "timezone": "UTC"
          }
        },
        {
          "id": "n2",
          "type": "NODE_TYPE_RUN_PROMPT",
          "name": "Summarise new detections",
          "run_prompt_node": {
            "prompt": "Summarise URLs first seen in the last 24h that are flagged malicious by 5+ engines."
          }
        },
        {
          "id": "n3",
          "type": "NODE_TYPE_SEND_EMAIL",
          "name": "Email the SOC",
          "send_email_node": {
            "notification_emails": [
              "soc@example.com"
            ],
            "email_subject": "Daily malicious-URL digest",
            "message": "See attached summary."
          }
        }
      ],
      "connections": [
        {
          "source_node_id": "n1",
          "target_node_id": "n2",
          "source_handle": ""
        },
        {
          "source_node_id": "n2",
          "target_node_id": "n3",
          "source_handle": ""
        }
      ]
    }
  }
}
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
    "/flows": {
      "post": {
        "tags": [
          "Flows"
        ],
        "deprecated": false,
        "operationId": "create-flow",
        "parameters": [
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
        "requestBody": {
          "content": {
            "application/json": {
              "examples": {
                "Result": {
                  "value": "{\n  \"data\": {\n    \"type\": \"flow\",\n    \"attributes\": {\n      \"name\": \"Daily malicious-URL digest\",\n      \"enabled\": true,\n      \"nodes\": [\n        {\n          \"id\": \"n1\",\n          \"type\": \"NODE_TYPE_SCHEDULE_TIME\",\n          \"name\": \"Every morning\",\n          \"schedule_node\": {\n            \"cron_expression\": \"0 9 * * *\",\n            \"timezone\": \"UTC\"\n          }\n        },\n        {\n          \"id\": \"n2\",\n          \"type\": \"NODE_TYPE_RUN_PROMPT\",\n          \"name\": \"Summarise new detections\",\n          \"run_prompt_node\": {\n            \"prompt\": \"Summarise URLs first seen in the last 24h that are flagged malicious by 5+ engines.\"\n          }\n        },\n        {\n          \"id\": \"n3\",\n          \"type\": \"NODE_TYPE_SEND_EMAIL\",\n          \"name\": \"Email the SOC\",\n          \"send_email_node\": {\n            \"notification_emails\": [\n              \"soc@example.com\"\n            ],\n            \"email_subject\": \"Daily malicious-URL digest\",\n            \"message\": \"See attached summary.\"\n          }\n        }\n      ],\n      \"connections\": [\n        {\n          \"source_node_id\": \"n1\",\n          \"target_node_id\": \"n2\",\n          \"source_handle\": \"\"\n        },\n        {\n          \"source_node_id\": \"n2\",\n          \"target_node_id\": \"n3\",\n          \"source_handle\": \"\"\n        }\n      ]\n    }\n  }\n}"
                }
              },
              "schema": {
                "properties": {
                  "data": {
                    "description": "A Flow object. Required: `attributes.name`.",
                    "format": "json",
                    "type": "string"
                  }
                },
                "required": [
                  "data"
                ],
                "type": "object"
              }
            }
          }
        },
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
            "description": "The created Flow object."
          },
          "400": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"error\": {\n    \"code\": \"BadRequestError\",\n    \"message\": \"Invalid node data.\"\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object"
                }
              }
            },
            "description": "Missing `name`, name too long, or malformed node / connection data."
          }
        },
        "security": [],
        "summary": "Create a Flow"
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

← [List Flows](list-flows.md) · [up](../README.md) · [Get a Flow](info-flow.md) →

*Archived from <https://gtidocs.virustotal.com/reference/create-flow>.*
