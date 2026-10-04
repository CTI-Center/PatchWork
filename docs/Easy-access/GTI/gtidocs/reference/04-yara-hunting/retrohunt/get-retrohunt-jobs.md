---
title: "Get a list of Retrohunt jobs"
source: https://gtidocs.virustotal.com/reference/get-retrohunt-jobs
slug: get-retrohunt-jobs
section: reference
group: "YARA Hunting"
updatedAt: 2025-09-25T00:36:31.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [Retrohunt](../retrohunt.md) › Get a list of Retrohunt jobs

---

# get-a-list-of-retrohunt-jobs

Returns a list of [Retrohunt Job](../../17-api-objects/retrohunt-job-object.md) objects. Accepted filters are `status:(starting|running|aborting|aborted|finished)`.

# openapi-definition

```json
{
  "info": {
    "title": "YARA Hunting",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Retrohunt"
    }
  ],
  "paths": {
    "/intelligence/retrohunt_jobs": {
      "get": {
        "tags": [
          "Retrohunt"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-retrohunt-jobs",
        "parameters": [
          {
            "description": "Maximum number jobs to retrieve",
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
            "description": "Return the jobs matching the given criteria only",
            "in": "query",
            "name": "filter",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Continuation cursor",
            "in": "query",
            "name": "cursor",
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
        "summary": "Get a list of Retrohunt jobs"
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

← [Retrohunt](../retrohunt.md) · [up](../README.md) · [Create a new Retrohunt job](create-retrohunt-job.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-retrohunt-jobs>.*
