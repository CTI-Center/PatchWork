---
title: "Scan URL"
source: https://gtidocs.virustotal.com/reference/scan-url
slug: scan-url
section: reference
group: "IoC Investigation"
updatedAt: 2026-04-17T12:39:11.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [URLs](../urls.md) › Scan URL

---

# scan-url

This returns an [Analysis](../../17-api-objects/analyses-object.md) ID. The analysis can be retrieved by using the [Analysis](../analyses-submissions-operations/analysis.md) endpoint.

Quota counts are not impacted if the submitted URL is unique and has no prior record in the database.

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
      "name": "URLs"
    }
  ],
  "paths": {
    "/urls": {
      "post": {
        "summary": "Scan URL",
        "description": "",
        "operationId": "scan-url",
        "parameters": [
          {
            "name": "x-apikey",
            "in": "header",
            "description": "Your API key",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/x-www-form-urlencoded": {
              "schema": {
                "type": "object",
                "required": [
                  "url"
                ],
                "properties": {
                  "url": {
                    "type": "string",
                    "description": "URL to scan"
                  }
                }
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          }
        },
        "deprecated": false,
        "security": [],
        "tags": [
          "URLs"
        ]
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

← [URLs](../urls.md) · [up](../README.md) · [Get a URL report](url-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/scan-url>.*
