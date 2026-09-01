---
title: "Get a file behaviour's detailed HTML report"
source: https://gtidocs.virustotal.com/reference/file-behaviour-feed-html
slug: file-behaviour-feed-html
section: reference
group: "IoC Feeds"
updatedAt: 2025-09-25T02:07:46.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Feeds](../README.md) › [Sandbox analyses feed](../sandbox-analyses-feed.md) › Get a file behaviour's detailed HTML report

---

# get-a-file-behaviour's-detailed-html-report

> 🚧 Special privileges required
>
> Sandbox analyses feeds endpoints are only available to users with a Sandbox feeds license. [Contact us](https://www.virustotal.com/gui/contact-us/) for more information.

Each JSON object contained in the file behaviour feed packages include a URL to this API endpoint to download the the file's sandbox execution HTML report. The available in the feed link already includes the download token required by this endpoint. The following snippet represents the JSON structure in the file behaviour feed that takes to the link:

```json
{
  "context_attributes": {
    "html_report": "https://www.virustotal.com/api/v3/feeds/file_behaviours/<TOKEN>/evtx"
  }
}
```

The link only works during the feed's lifetime. Check [/feeds/file\_behaviours/\{time}](feeds-file-behaviour.md) for more information.

# openapi-definition

```json
{
  "components": {
    "securitySchemes": {
      "sec0": {
        "in": "header",
        "name": "x-apikey",
        "type": "apiKey"
      }
    }
  },
  "info": {
    "title": "IoC Feeds",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Sandbox analyses feed"
    }
  ],
  "paths": {
    "/feeds/file_behaviours/{token}/html": {
      "get": {
        "tags": [
          "Sandbox analyses feed"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "file-behaviour-feed-html",
        "parameters": [
          {
            "description": "Download token. It can be found inside the behaviour object's properties in the file behaviour feed.",
            "in": "path",
            "name": "token",
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
        "summary": "Get a file behaviour's detailed HTML report"
      }
    }
  },
  "security": [
    {
      "sec0": []
    }
  ],
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

← [Get the EVTX file generated during a file’s behavior analysis](file-behaviour-feed-evtx.md) · [up](../README.md) · [Get the memdump file generated during a file’s behavior analysis](file-behaviour-feed-memdump.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-behaviour-feed-html>.*
