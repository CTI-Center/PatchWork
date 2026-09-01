---
title: "Get a URL analysis report"
source: https://gtidocs.virustotal.com/reference/get-a-private-url-analysis-report
slug: get-a-private-url-analysis-report
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:37:17.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private URLs](../private-urls.md) › Get a URL analysis report

---

# get-a-url-analysis-report

> 📘
>
> See [URL identifiers](../private-urls.md#url-identifiers) from more information about how to generate a valid URL identifier for a URL.

> 🚧 gti\_assessment attribute
>
> To get the **gti\_assessment** attribute in the JSON response, ensure that the **x-tool** header is added to the request headers. This header should be used to identify your tool or service with a custom name.

Returns a [URL](../../17-api-objects/url-object.md) object.

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
      "name": "Private URLs"
    }
  ],
  "paths": {
    "/urls/{id}": {
      "get": {
        "tags": [
          "Private URLs"
        ],
        "summary": "Get a URL analysis report",
        "description": "",
        "operationId": "get-a-private-url-analysis-report",
        "parameters": [
          {
            "name": "x-apikey",
            "in": "header",
            "description": "Your API key",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "id",
            "in": "path",
            "description": "URL identifier or base64 representation of URL to scan (w/o padding)",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "description": "The name of your tool or service. This is required to obtain the gti_assesment data",
            "in": "header",
            "name": "x-tool",
            "required": false,
            "schema": {
              "type": "string"
            }
          }
        ],
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
        "security": []
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

← [Private Scan URL](private-scan-url.md) · [up](../README.md) · [Get objects related to a private URL](private-get-objects-related-to-a-url.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-a-private-url-analysis-report>.*
