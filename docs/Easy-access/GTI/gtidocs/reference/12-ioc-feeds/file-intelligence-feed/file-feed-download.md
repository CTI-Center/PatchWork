---
title: "Download a file published in the file feed"
source: https://gtidocs.virustotal.com/reference/file-feed-download
slug: file-feed-download
section: reference
group: "IoC Feeds"
updatedAt: 2025-09-25T02:07:42.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Feeds](../README.md) › [File intelligence feed](../file-intelligence-feed.md) › Download a file published in the file feed

---

# download-a-file-published-in-the-file-feed

> 🚧 Special privileges required
>
> File feeds endpoints are only available to users with a File feeds license. For this particular endpoint, download file privilege is also required. [Contact us](https://www.virustotal.com/gui/contact-us/) for more information.

Each JSON object contained in the file feed packages include a URL to this API endpoint to download the corresponding file. The link only works during the feed's lifetime, which is 7 days. Check [/feeds/files/\{time}](feeds-file.md) for more information.

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
      "name": "File intelligence feed"
    }
  ],
  "paths": {
    "/feeds/files/{token}/download": {
      "get": {
        "tags": [
          "File intelligence feed"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "file-feed-download",
        "parameters": [
          {
            "description": "Download token. It can be found inside the file's properties in the file feed.",
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
        "summary": "Download a file published in the file feed"
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

← [Get a per-minute file feed batch](feeds-file.md) · [up](../README.md) · [Sandbox analyses feed](../sandbox-analyses-feed.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-feed-download>.*
