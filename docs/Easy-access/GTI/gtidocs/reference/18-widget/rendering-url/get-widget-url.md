---
title: "Get a widget rendering URL"
source: https://gtidocs.virustotal.com/reference/get-widget-url
slug: get-widget-url
section: reference
group: "Widget"
updatedAt: 2025-09-25T00:46:35.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Widget](../README.md) › [Rendering URL](../rendering-url.md) › Get a widget rendering URL

---

# get-a-widget-rendering-url

Get a widget rendering URL

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
    "title": "Widget",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Rendering URL"
    }
  ],
  "paths": {
    "/gtiwidget": {
      "get": {
        "tags": [
          "Rendering URL"
        ],
        "deprecated": false,
        "description": "Get a widget rendering URL",
        "operationId": "get-widget-url",
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
            "description": "IOC, can be a sha256 file hash, a domain, an IPv4 address or an url.",
            "in": "query",
            "name": "query",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "The name of your tool or service. This is required to obtain the gti_assesment data.",
            "in": "header",
            "name": "x-tool",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Theme option, you can use light or dark",
            "in": "query",
            "name": "theme",
            "schema": {
              "type": "string",
              "enum": [
                "light",
                "dark"
              ]
            }
          },
          {
            "description": "Theme primary background color in hex notation.",
            "in": "query",
            "name": "bg1",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Theme secondary background color in hex notation.",
            "in": "query",
            "name": "bg2",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Theme terciary background color in hex notation.",
            "in": "query",
            "name": "bg3",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Theme primary foreground color in hex notation.",
            "in": "query",
            "name": "fg1",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Theme secondary foreground color in hex notation.",
            "in": "query",
            "name": "fg2",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Theme terciary foreground color in hex notation.",
            "in": "query",
            "name": "fg3",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Theme accent color in hex notation.",
            "in": "query",
            "name": "acc",
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
        "summary": "Get a widget rendering URL"
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

← [Rendering URL](../rendering-url.md) · [up](../README.md)

*Archived from <https://gtidocs.virustotal.com/reference/get-widget-url>.*
