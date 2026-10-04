---
title: "Get a submission object"
source: https://gtidocs.virustotal.com/reference/get-submission
slug: get-submission
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T02:04:37.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Analyses, Submissions & Operations](../analyses-submissions-operations.md) › Get a submission object

---

# get-a-submission-object

Returns a [Submission](../../17-api-objects/submission-object.md) object.

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
    "/submission/{id}": {
      "get": {
        "tags": [
          "Analyses, Submissions & Operations"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-submission",
        "parameters": [
          {
            "description": "Submission object ID",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Your API key",
            "in": "header",
            "name": "x-apikey",
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
        "summary": "Get a submission object"
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

← [Get objects related to an analysis](analyses-get-objects.md) · [up](../README.md) · [Get an operation object](get-operations-id.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-submission>.*
