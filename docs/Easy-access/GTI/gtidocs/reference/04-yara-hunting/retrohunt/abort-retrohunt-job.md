---
title: "Abort a Retrohunt job"
source: https://gtidocs.virustotal.com/reference/abort-retrohunt-job
slug: abort-retrohunt-job
section: reference
group: "YARA Hunting"
updatedAt: 2025-09-25T00:36:34.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [Retrohunt](../retrohunt.md) › Abort a Retrohunt job

---

# abort-a-retrohunt-job

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
    "/intelligence/retrohunt_jobs/{id}/abort": {
      "post": {
        "tags": [
          "Retrohunt"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "abort-retrohunt-job",
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
        "summary": "Abort a Retrohunt job"
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

← [Get a Retrohunt job object](get-retrohunt-job.md) · [up](../README.md) · [Retrieve matches for a Retrohunt job](get-retrohunt-job-relationships.md) →

*Archived from <https://gtidocs.virustotal.com/reference/abort-retrohunt-job>.*
