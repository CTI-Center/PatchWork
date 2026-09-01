---
title: "Get a URL analysis DOM"
source: https://gtidocs.virustotal.com/reference/analysis-dom
slug: analysis-dom
section: reference
group: "IoC Investigation"
updatedAt: 2026-07-02T10:07:09.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Analyses, Submissions & Operations](../analyses-submissions-operations.md) › Get a URL analysis DOM

---

# get-a-url-analysis-dom

This endpoint returns the rendered DOM that the browser captured at the end of a [URL Analysis](../../17-api-objects/url-analysis-object.md).

The response `302 Found` redirects to a short-lived (5 minutes) signed URL pointing at the HTML artifact in Google Cloud Storage. Follow redirects to download the file.

## examples

Get the DOM for Analysis ID "u-109b1fe44b83bfdeaeee0d238e041915b6d71f6ce4b91f8f9ad79eac3ac7d27f-6d2fb381".

```python
import requests

id = "u-109b1fe44b83bfdeaeee0d238e041915b6d71f6ce4b91f8f9ad79eac3ac7d27f-6d2fb381"
local_filename = "dom.html"
url = f"https://www.virustotal.com/api/v3/analyses/{id}/dom"

headers = {
    "accept": "application/json",
    "x-apikey": <api-key>
}

response = requests.get(url, headers=headers)
response.raise_for_status()
with open(local_filename, 'wb') as f:
    f.write(response.content)
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
    "/analyses/{id}/dom": {
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
        "operationId": "get_analyses-id-dom",
        "summary": "Get a URL analysis DOM"
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

← [Get the URL for a URL analysis screenshot](analysis-screenshot-url.md) · [up](../README.md) · [Get the URL for a URL analysis DOM](analysis-dom-url.md) →

*Archived from <https://gtidocs.virustotal.com/reference/analysis-dom>.*
