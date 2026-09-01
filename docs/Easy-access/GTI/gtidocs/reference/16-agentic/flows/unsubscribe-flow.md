---
title: "Unsubscribe from a Flow's email notifications"
source: https://gtidocs.virustotal.com/reference/unsubscribe-flow
slug: unsubscribe-flow
section: reference
group: "agentic"
updatedAt: 2026-08-04T08:18:35.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [agentic](../README.md) › [Flows](../flows.md) › Unsubscribe from a Flow's email notifications

---

# unsubscribe-from-a-flow's-email-notifications

Unsubscribe an email address from Flow notifications.

Public, token-authenticated endpoint that backs the unsubscribe link in every Agentic Flows notification email. No API key or account is required: authorization is carried entirely by the signed `token`, which encodes the Flow, the Send Email node, and the recipient address. Idempotent — removing an address that is no longer subscribed still succeeds. The `token` must have been issued for the `{id}` in the path.

```json Request example
{
  "token": "<signed-unsubscribe-token>"
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
    "/flows/{id}/unsubscribe": {
      "post": {
        "tags": [
          "Flows"
        ],
        "deprecated": false,
        "operationId": "unsubscribe-flow",
        "parameters": [
          {
            "description": "Flow ID (must match the Flow encoded in the token).",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Not required for this endpoint.",
            "in": "header",
            "name": "x-apikey",
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
                  "value": "{\n  \"token\": \"<signed-unsubscribe-token>\"\n}"
                }
              },
              "schema": {
                "properties": {
                  "token": {
                    "description": "The signed unsubscribe token from the email link.",
                    "type": "string"
                  }
                },
                "required": [
                  "token"
                ],
                "type": "object"
              }
            }
          },
          "description": "The signed unsubscribe token from the email link."
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"data\": {\n    \"unsubscribed\": true\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object"
                }
              }
            },
            "description": "Confirmation that the address was unsubscribed."
          },
          "400": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"error\": {\n    \"code\": \"BadRequestError\",\n    \"message\": \"Invalid token.\"\n  }\n}"
                  }
                },
                "schema": {
                  "type": "object"
                }
              }
            },
            "description": "Missing, malformed, or mismatched token."
          }
        },
        "security": [],
        "summary": "Unsubscribe from a Flow's email notifications"
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

← [Get object descriptors related to a Flow](get-flow-related-descriptors.md) · [up](../README.md) · [Flow Executions](../flow-executions.md) →

*Archived from <https://gtidocs.virustotal.com/reference/unsubscribe-flow>.*
