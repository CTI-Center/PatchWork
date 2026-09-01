---
title: "Retrieve matches for a Retrohunt job"
source: https://gtidocs.virustotal.com/reference/get-retrohunt-job-relationships
slug: get-retrohunt-job-relationships
section: reference
group: "YARA Hunting"
updatedAt: 2025-09-25T00:36:35.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [Retrohunt](../retrohunt.md) › Retrieve matches for a Retrohunt job

---

# retrieve-matches-for-a-retrohunt-job

Retrohunt jobs are related to other objects. As mentioned in the [Relationships](../../01-api-introduction/api-responses/introduction-relationships.md) section, those related objects can be retrieved by sending `GET` requests to the relationships URL.

The supported relationships for Retrohunt jobs are described in the [Retrohunt Jobs](../../17-api-objects/retrohunt-job-object.md) API object page.

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
    "/intelligence/retrohunt_jobs/{id}/matching_files": {
      "get": {
        "tags": [
          "Retrohunt"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-retrohunt-job-relationships",
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
            "description": "Maximum number of matching files to retrieve",
            "in": "query",
            "name": "limit",
            "schema": {
              "default": 10,
              "format": "int32",
              "type": "integer",
              "maximum": 40,
              "minimum": 0
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
        "summary": "Retrieve matches for a Retrohunt job"
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

← [Abort a Retrohunt job](abort-retrohunt-job.md) · [up](../README.md) · [Reports](../../05-reports-analysis/reports.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-retrohunt-job-relationships>.*
