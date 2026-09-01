---
title: "Get the PCAP file generated during a file’s behavior analysis"
source: https://gtidocs.virustotal.com/reference/file-behaviour-feed-pcap
slug: file-behaviour-feed-pcap
section: reference
group: "IoC Feeds"
updatedAt: 2025-09-25T02:07:47.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Feeds](../README.md) › [Sandbox analyses feed](../sandbox-analyses-feed.md) › Get the PCAP file generated during a file’s behavior analysis

---

# get-the-pcap-file-generated-during-a-file’s-behavior-analysis

> 🚧 Special privileges required
>
> Sandbox analyses feeds endpoints are only available to users with a Sandbox feeds license. [Contact us](https://www.virustotal.com/gui/contact-us/) for more information.

Each JSON object contained in the file behaviour feed packages include a URL to this API endpoint to download the extracted PCAP from the file's sandbox execution. The available in the feed link already includes the download token required by this endpoint. The following snippet represents the JSON structure in the file behaviour feed that takes to the link:

```json JSON structure
{
  "context_attributes": {
    "pcap": "https://www.virustotal.com/api/v3/feeds/file_behaviours/<TOKEN>/pcap"
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
    "/feeds/file_behaviours/{token}/pcap": {
      "get": {
        "tags": [
          "Sandbox analyses feed"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "file-behaviour-feed-pcap",
        "parameters": [
          {
            "description": "Download token. It can be found inside the behaviour object's properties in the behaviour feed.",
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
        "summary": "Get the PCAP file generated during a file’s behavior analysis"
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

← [Get the memdump file generated during a file’s behavior analysis](file-behaviour-feed-memdump.md) · [up](../README.md) · [Domain intelligence feed](../domain-intelligence-feed.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-behaviour-feed-pcap>.*
