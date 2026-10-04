---
title: "Get an IoC Stream notification"
source: https://gtidocs.virustotal.com/reference/get-an-ioc-stream-notification
slug: get-an-ioc-stream-notification
section: reference
group: "YARA Hunting"
updatedAt: 2025-09-25T00:36:17.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [IoC Stream](../ioc-stream.md) › Get an IoC Stream notification

---

# get-an-ioc-stream-notification

Returns an IoC Stream notification.

# openapi-definition

```json
{
  "info": {
    "title": "YARA Hunting",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "IoC Stream"
    }
  ],
  "paths": {
    "/ioc_stream_notifications/{id}": {
      "get": {
        "tags": [
          "IoC Stream"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-an-ioc-stream-notification",
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
            "description": "The ID of the IoC Stream notification",
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
        "summary": "Get an IoC Stream notification"
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

← [Delete an IoC Stream notification](delete-an-ioc-stream-notification.md) · [up](../README.md) · [Livehunt](../livehunt.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-an-ioc-stream-notification>.*
