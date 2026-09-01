---
title: "Get a URL's latest analysis DOM"
source: https://gtidocs.virustotal.com/reference/urls-dom
slug: urls-dom
section: reference
group: "IoC Investigation"
updatedAt: 2026-07-02T10:08:05.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [URLs](../urls.md) › Get a URL's latest analysis DOM

---

# get-a-url's-latest-analysis-dom

> 📘 See [URL identifiers](../urls.md#url-identifiers) from more information about how to generate a valid URL identifier for a URL.

This endpoint returns the rendered DOM that the browser captured during the latest analysis.

The response `302 Found` redirects to a short-lived (5 minutes) signed URL pointing at the HTML artifact in Google Cloud Storage. Follow redirects to download the file.

## examples

Get the DOM for URL ID "c9d09bb06e6b480d98faca5b84f6b87fdb2bafe2cd91b1957ee0a1ee56c6628e".

```python
import requests

id = "c9d09bb06e6b480d98faca5b84f6b87fdb2bafe2cd91b1957ee0a1ee56c6628e"
local_filename = "dom.html"
url = f"https://www.virustotal.com/api/v3/urls/{id}/dom"

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
    "/urls/{id}/dom": {
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
            "description": "URL ID"
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
        "operationId": "get_urls-id-dom",
        "summary": "Get a URL's latest analysis DOM"
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

← [Get the URL for a URL's latest analysis screenshot](urls-screenshot-url.md) · [up](../README.md) · [Get the URL for a URL's latest analysis DOM](urls-dom-url.md) →

*Archived from <https://gtidocs.virustotal.com/reference/urls-dom>.*
