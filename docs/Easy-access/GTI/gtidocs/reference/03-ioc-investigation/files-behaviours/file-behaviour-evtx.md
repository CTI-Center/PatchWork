---
title: "Get the EVTX file generated during a file’s behavior analysis"
source: https://gtidocs.virustotal.com/reference/file-behaviour-evtx
slug: file-behaviour-evtx
section: reference
group: "IoC Investigation"
updatedAt: 2026-02-05T12:43:34.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Files Behaviours](../files-behaviours.md) › Get the EVTX file generated during a file’s behavior analysis

---

# get-the-evtx-file-generated-during-a-file’s-behavior-analysis

> 🚧 Special privileges required
>
> This endpoint is only available for users with special privileges.

Fetch the EVTX file associated with the sandbox execution.

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
      "name": "Files Behaviours"
    }
  ],
  "paths": {
    "/file_behaviours/{sandbox_id}/evtx": {
      "get": {
        "tags": [
          "Files Behaviours"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "file-behaviour-evtx",
        "parameters": [
          {
            "description": "Sandbox report ID.",
            "in": "path",
            "name": "sandbox_id",
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
        "summary": "Get the EVTX file generated during a file’s behavior analysis"
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

← [Get a file behavior report from a sandbox](get-file-behaviour-id.md) · [up](../README.md) · [Get a detailed HTML behaviour report](get-file-behaviour-html.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-behaviour-evtx>.*
