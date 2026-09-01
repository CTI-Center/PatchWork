---
title: "Get a detailed HTML behaviour report"
source: https://gtidocs.virustotal.com/reference/privatefile-behaviourssandbox-idhtml
slug: privatefile-behaviourssandbox-idhtml
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:37:04.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private Files Behaviours](../private-files-behaviours.md) › Get a detailed HTML behaviour report

---

# get-a-detailed-html-behaviour-report

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

Returns a [Private File Behaviour](../../17-api-objects/private-file-behaviours-object.md) object as an HTML report. It expects the sandbox ID returned by the [GET /private/files/\{id}/behaviours](get-all-behaviour-reports-from-a-private-file.md) endpoint.

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
    "/file_behaviours/{sandbox_id}/html": {
      "get": {
        "tags": [
          "Private Files Behaviours"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "privatefile-behaviourssandbox-idhtml",
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
        "summary": "Get a detailed HTML behaviour report"
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

← [Get the EVTX file generated during a private file’s behavior analysis](file-behaviourssandbox-idevtx.md) · [up](../README.md) · [Get the memdump file generated during a private file’s behavior analysis](privatefile-behaviourssandbox-idpcap.md) →

*Archived from <https://gtidocs.virustotal.com/reference/privatefile-behaviourssandbox-idhtml>.*
