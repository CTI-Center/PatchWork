---
title: "Get an operation object"
source: https://gtidocs.virustotal.com/reference/get-operations-id
slug: get-operations-id
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T02:04:38.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Analyses, Submissions & Operations](../analyses-submissions-operations.md) › Get an operation object

---

# get-an-operation-object

Returns an [Operation](../../17-api-objects/operation-object.md) object.

# openapi-definition

```json
{
  "info": {
    "title": "IoC Investigation",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Analyses, Submissions & Operations"
    }
  ],
  "paths": {
    "/operations/{id}": {
      "get": {
        "tags": [
          "Analyses, Submissions & Operations"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-operations-id",
        "parameters": [
          {
            "description": "Operation ID",
            "in": "path",
            "name": "id",
            "required": true,
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
                    "value": "{}"
                  }
                },
                "schema": {
                  "properties": {},
                  "type": "object"
                }
              }
            },
            "description": "200"
          },
          "400": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "properties": {},
                  "type": "object"
                }
              }
            },
            "description": "400"
          }
        },
        "security": [],
        "summary": "Get an operation object"
      }
    }
  },
  "security": [],
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

← [Get a submission object](get-submission.md) · [up](../README.md) · [Get a URL analysis screenshot](analysis-screenshot.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-operations-id>.*
