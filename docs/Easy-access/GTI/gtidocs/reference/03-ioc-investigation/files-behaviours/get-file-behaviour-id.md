---
title: "Get a file behavior report from a sandbox"
source: https://gtidocs.virustotal.com/reference/get-file-behaviour-id
slug: get-file-behaviour-id
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T02:04:00.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Files Behaviours](../files-behaviours.md) › Get a file behavior report from a sandbox

---

# get-a-file-behavior-report-from-a-sandbox

Fetches a [File behaviour](../../17-api-objects/file-behaviour-summary-object.md) object by ID.

> 📘 This API call only fetches the behaviour report for a single behavioural analysis you can fetch all of them with [file-all-behaviours-summary.md](file-all-behaviours-summary.md)

## sandbox-report-identifiers

A Sandbox report ID has two main components: the **analysed file's SHA256** and the **sandbox name**. These two components are joined by a `_` character. For example, ID `5353e23f3653402339c93a8565307c6308ff378e03fcf23a4378f31c434030b0_VirusTotal Jujubox` fetches the sandbox report for a file having a SHA256 `5353e23f3653402339c93a8565307c6308ff378e03fcf23a4378f31c434030b0` analysed in the `VirusTotal Jujubox` sandbox.

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
    "/file_behaviours/{sandbox_id}": {
      "get": {
        "tags": [
          "Files Behaviours"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-file-behaviour-id",
        "parameters": [
          {
            "description": "Sandbox report ID. See \"Sandbox Report identifiers\" section below for more info.",
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
        "summary": "Get a file behavior report from a sandbox"
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

← [Files Behaviours](../files-behaviours.md) · [up](../README.md) · [Get the EVTX file generated during a file’s behavior analysis](file-behaviour-evtx.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-file-behaviour-id>.*
