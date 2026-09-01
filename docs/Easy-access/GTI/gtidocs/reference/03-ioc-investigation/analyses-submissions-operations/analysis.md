---
title: "Get a URL / file analysis"
source: https://gtidocs.virustotal.com/reference/analysis
slug: analysis
section: reference
group: "IoC Investigation"
updatedAt: 2026-04-17T12:36:27.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Analyses, Submissions & Operations](../analyses-submissions-operations.md) › Get a URL / file analysis

---

# get-a-url-/-file-analysis

This endpoint returns an [Analysis](../../17-api-objects/analyses-object.md) object.

Note that quotas are not incremented if the user is the original submitter of the file or URL and is requesting the initial analysis report.

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
    "/analyses/{id}": {
      "get": {
        "tags": [
          "Analyses, Submissions & Operations"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "analysis",
        "parameters": [
          {
            "description": "Analysis identifier",
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
        "summary": "Get a URL / file analysis"
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

← [Analyses, Submissions & Operations](../analyses-submissions-operations.md) · [up](../README.md) · [Get object descriptors related to an analysis](analyses-get-descriptors.md) →

*Archived from <https://gtidocs.virustotal.com/reference/analysis>.*
