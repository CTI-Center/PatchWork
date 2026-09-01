---
title: "Get a detailed HTML behaviour report"
source: https://gtidocs.virustotal.com/reference/get-file-behaviour-html
slug: get-file-behaviour-html
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T00:35:16.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Files Behaviours](../files-behaviours.md) › Get a detailed HTML behaviour report

---

# get-a-detailed-html-behaviour-report

Returns a [File behaviour](../../17-api-objects/file-behaviour-summary-object.md) object as an HTML report.

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
    "/file_behaviours/{sandbox_id}/html": {
      "get": {
        "tags": [
          "Files Behaviours"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-file-behaviour-html",
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
              "text/plain": {
                "examples": {
                  "Result": {
                    "value": "<!DOCTYPE html>\n<html lang=\"en\">\n  ..."
                  }
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
        "summary": "Get a detailed HTML behaviour report"
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

← [Get the EVTX file generated during a file’s behavior analysis](file-behaviour-evtx.md) · [up](../README.md) · [Get the memdump file generated during a file’s behavior analysis](file-behaviour-memdump.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-file-behaviour-html>.*
