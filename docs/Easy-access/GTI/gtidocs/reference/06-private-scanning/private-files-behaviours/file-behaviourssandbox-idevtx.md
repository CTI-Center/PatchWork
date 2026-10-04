---
title: "Get the EVTX file generated during a private file’s behavior analysis"
source: https://gtidocs.virustotal.com/reference/file-behaviourssandbox-idevtx
slug: file-behaviourssandbox-idevtx
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:37:03.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private Files Behaviours](../private-files-behaviours.md) › Get the EVTX file generated during a private file’s behavior analysis

---

# get-the-evtx-file-generated-during-a-private-file’s-behavior-analysis

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

Fetch the EVTX file associated with the sandbox execution.

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
    "/file_behaviours/{sandbox_id}/evtx": {
      "get": {
        "tags": [
          "Private Files Behaviours"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "file-behaviourssandbox-idevtx",
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
            "description": "Sandbox report ID",
            "in": "path",
            "name": "sandbox_id",
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
        "summary": "Get the EVTX file generated during a private file’s behavior analysis"
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

← [Get a behaviour report from a private file](privatefile-behaviourssandbox-id.md) · [up](../README.md) · [Get a detailed HTML behaviour report](privatefile-behaviourssandbox-idhtml.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-behaviourssandbox-idevtx>.*
