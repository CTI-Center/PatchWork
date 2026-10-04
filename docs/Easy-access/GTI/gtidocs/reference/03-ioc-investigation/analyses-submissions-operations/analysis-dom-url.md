---
title: "Get the URL for a URL analysis DOM"
source: https://gtidocs.virustotal.com/reference/analysis-dom-url
slug: analysis-dom-url
section: reference
group: "IoC Investigation"
updatedAt: 2026-07-02T10:07:23.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Analyses, Submissions & Operations](../analyses-submissions-operations.md) › Get the URL for a URL analysis DOM

---

# get-the-url-for-a-url-analysis-dom

This endpoint returns the short-lived signed URL of the rendered DOM captured during a [URL Analysis](../../17-api-objects/url-analysis-object.md), wrapped in a JSON response:

```json
{
  "data": "https://vtdom.commondatastorage.googleapis.com/9fda61....."
}
```

Use this endpoint instead of [GET /analyses/{id}/dom](analysis-dom.md) when you need the link itself rather than the HTML bytes.

Note that the signed URL is valid for 5 minutes. If the link expires, you must request the endpoint again to generate a new one. The underlying asset is an HTML file.

## examples

Get the DOM for Analysis ID "u-109b1fe44b83bfdeaeee0d238e041915b6d71f6ce4b91f8f9ad79eac3ac7d27f-6d2fb381".

```python
import requests

id = "u-109b1fe44b83bfdeaeee0d238e041915b6d71f6ce4b91f8f9ad79eac3ac7d27f-6d2fb381"
url = f"https://www.virustotal.com/api/v3/analyses/{id}/dom_url"

headers = {
    "accept": "application/json",
    "x-apikey": <api-key>
}

response = requests.get(url, headers=headers)
```

<br />

# openapi-definition

```json
{
  "info": {
    "title": "IoC Investigation",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "paths": {
    "/analyses/{id}/dom_url": {
      "get": {
        "description": "",
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
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
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          }
        },
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "URL analysis ID. Must match the format `u-<sha256>-<suffix>`. File analyses do not have a DOM."
          },
          {
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            },
            "description": "Your API key",
            "required": true
          }
        ],
        "operationId": "get_analyses-id-dom-url",
        "summary": "Get the URL for a URL analysis DOM"
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

← [Get a URL analysis DOM](analysis-dom.md) · [up](../README.md) · [Get strings extracted from the content downloaded during a URL analysis](analysis-content-strings.md) →

*Archived from <https://gtidocs.virustotal.com/reference/analysis-dom-url>.*
