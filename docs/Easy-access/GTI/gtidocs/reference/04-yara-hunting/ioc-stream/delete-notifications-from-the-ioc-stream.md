---
title: "Delete notifications from the IoC Stream"
source: https://gtidocs.virustotal.com/reference/delete-notifications-from-the-ioc-stream
slug: delete-notifications-from-the-ioc-stream
section: reference
group: "YARA Hunting"
updatedAt: 2025-09-25T00:36:14.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [IoC Stream](../ioc-stream.md) › Delete notifications from the IoC Stream

---

# delete-notifications-from-the-ioc-stream

Uses the same filters than the IoC Stream ([GET /ioc\_stream](get-objects-from-the-ioc-stream.md)) to delete all the matching notifications.

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
    "/ioc_stream": {
      "delete": {
        "tags": [
          "IoC Stream"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "delete-notifications-from-the-ioc-stream",
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
            "description": "Filter string",
            "in": "query",
            "name": "filter",
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
                    "value": ""
                  }
                }
              }
            },
            "description": "200"
          },
          "429": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n  \"error\": {\n    \"code\": \"TooManyRequests\",\n    \"message\": \"Notifications already being deleted. Depending on volume this may take a while.\"\n}"
                  }
                }
              }
            },
            "description": "429"
          }
        },
        "summary": "Delete notifications from the IoC Stream"
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

← [IoC Stream](../ioc-stream.md) · [up](../README.md) · [Get objects from the IoC Stream](get-objects-from-the-ioc-stream.md) →

*Archived from <https://gtidocs.virustotal.com/reference/delete-notifications-from-the-ioc-stream>.*
