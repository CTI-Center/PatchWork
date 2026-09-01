---
title: "Get the behaviour reports from a private file"
source: https://gtidocs.virustotal.com/reference/get-all-behaviour-reports-from-a-private-file
slug: get-all-behaviour-reports-from-a-private-file
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:37:01.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private Files Behaviours](../private-files-behaviours.md) › Get the behaviour reports from a private file

---

# get-the-behaviour-reports-from-a-private-file

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

Fetches all the [Private File Behaviour](../../17-api-objects/private-file-behaviours-object.md) reports available for a private file.

# openapi-definition

```json
{
  "info": {
    "title": "Private Scanning",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Private Files Behaviours"
    }
  ],
  "paths": {
    "/file/{id}/behaviours": {
      "get": {
        "tags": [
          "Private Files Behaviours"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-all-behaviour-reports-from-a-private-file",
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
        "summary": "Get the behaviour reports from a private file"
      }
    }
  },
  "security": [],
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3/private"
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

← [Private Files Behaviours](../private-files-behaviours.md) · [up](../README.md) · [Get a behaviour report from a private file](privatefile-behaviourssandbox-id.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-all-behaviour-reports-from-a-private-file>.*
