---
title: "Delete a Retrohunt job"
source: https://gtidocs.virustotal.com/reference/delete-retrohunt-job
slug: delete-retrohunt-job
section: reference
group: "YARA Hunting"
updatedAt: 2025-09-25T00:36:32.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [Retrohunt](../retrohunt.md) › Delete a Retrohunt job

---

# delete-a-retrohunt-job

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
      "delete": {
        "tags": [
          "Retrohunt"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "delete-retrohunt-job",
        "parameters": [
          {
            "description": "Job identifier",
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
        "summary": "Delete a Retrohunt job"
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

← [Create a new Retrohunt job](create-retrohunt-job.md) · [up](../README.md) · [Get a Retrohunt job object](get-retrohunt-job.md) →

*Archived from <https://gtidocs.virustotal.com/reference/delete-retrohunt-job>.*
