---
title: "Get the URL for a URL's latest analysis screenshot"
source: https://gtidocs.virustotal.com/reference/urls-screenshot-url
slug: urls-screenshot-url
section: reference
group: "IoC Investigation"
updatedAt: 2026-07-06T08:52:17.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [URLs](../urls.md) › Get the URL for a URL's latest analysis screenshot

---

# get-the-url-for-a-url's-latest-analysis-screenshot

> 📘
>
> ### See [URL identifiers](../urls.md#url-identifiers) from more information about how to generate a valid URL identifier for a URL.

This endpoint returns the short-lived signed URL of the PNG screenshot captured during the latest URL analysis, wrapped in a JSON response:

```json
{
  "data": "https://vturlscreenshot.commondatastorage.googleapis.com/u-af2c53e..."
}
```

Use this endpoint if you only need the screenshot link. If you prefer to stream the image bytes directly, [GET /urls/{id}/screenshot](urls-screenshot.md)

Note that the signed URL is valid for 5 minutes. If the link expires, you must request the endpoint again to generate a new one. The underlying asset is an image/png file.

## examples

Check if a screenshot is available for URL ID "c9d09bb06e6b480d98faca5b84f6b87fdb2bafe2cd91b1957ee0a1ee56c6628e".

```python
import requests

id = "c9d09bb06e6b480d98faca5b84f6b87fdb2bafe2cd91b1957ee0a1ee56c6628e"
url = f"https://www.virustotal.com/api/v3/urls/{id}/screenshot_url"

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
    "/urls/{id}/screenshot_url": {
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
        "operationId": "get_urls-id-screenshot-url",
        "summary": "Get the URL for a URL's latest analysis screenshot"
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

← [Get a URL's latest analysis screenshot](urls-screenshot.md) · [up](../README.md) · [Get a URL's latest analysis DOM](urls-dom.md) →

*Archived from <https://gtidocs.virustotal.com/reference/urls-screenshot-url>.*
