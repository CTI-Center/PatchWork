---
title: "Delete an IoC Stream notification"
source: https://gtidocs.virustotal.com/reference/delete-an-ioc-stream-notification
slug: delete-an-ioc-stream-notification
section: reference
group: "YARA Hunting"
updatedAt: 2025-09-25T00:36:16.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [IoC Stream](../ioc-stream.md) › Delete an IoC Stream notification

---

# delete-an-ioc-stream-notification

Deletes an IoC Stream notification.

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
      "delete": {
        "tags": [
          "IoC Stream"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "delete-an-ioc-stream-notification",
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
                    "value": ""
                  }
                }
              }
            },
            "description": "200"
          }
        },
        "summary": "Delete an IoC Stream notification"
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

← [Get objects from the IoC Stream](get-objects-from-the-ioc-stream.md) · [up](../README.md) · [Get an IoC Stream notification](get-an-ioc-stream-notification.md) →

*Archived from <https://gtidocs.virustotal.com/reference/delete-an-ioc-stream-notification>.*
