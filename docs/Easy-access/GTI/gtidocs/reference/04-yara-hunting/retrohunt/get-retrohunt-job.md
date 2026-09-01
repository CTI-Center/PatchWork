---
title: "Get a Retrohunt job object"
source: https://gtidocs.virustotal.com/reference/get-retrohunt-job
slug: get-retrohunt-job
section: reference
group: "YARA Hunting"
updatedAt: 2025-09-25T00:36:33.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [Retrohunt](../retrohunt.md) › Get a Retrohunt job object

---

# get-a-retrohunt-job-object

Returns a [Retrohunt Job](../../17-api-objects/retrohunt-job-object.md) object.

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
    "/intelligence/retrohunt_jobs/{id}": {
      "get": {
        "tags": [
          "Retrohunt"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-retrohunt-job",
        "parameters": [
          {
            "description": "Your API key",
            "in": "header",
            "name": "x-apikey",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Job identifier",
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
        "summary": "Get a Retrohunt job object"
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

← [Delete a Retrohunt job](delete-retrohunt-job.md) · [up](../README.md) · [Abort a Retrohunt job](abort-retrohunt-job.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-retrohunt-job>.*
