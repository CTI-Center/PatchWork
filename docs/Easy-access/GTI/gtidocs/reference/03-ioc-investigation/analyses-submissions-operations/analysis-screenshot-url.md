---
title: "Get the URL for a URL analysis screenshot"
source: https://gtidocs.virustotal.com/reference/analysis-screenshot-url
slug: analysis-screenshot-url
section: reference
group: "IoC Investigation"
updatedAt: 2026-05-26T10:12:31.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Analyses, Submissions & Operations](../analyses-submissions-operations.md) › Get the URL for a URL analysis screenshot

---

# get-the-url-for-a-url-analysis-screenshot

This endpoint returns the short-lived signed URL of the PNG screenshot captured during a [URL Analysis](../../17-api-objects/url-analysis-object.md), wrapped in a JSON response:

```json
{
  "data": "https://vturlscreenshot.commondatastorage.googleapis.com/u-af2c53e..."
}
```

Use this endpoint if you only need the screenshot link. If you prefer to stream the image bytes directly, use [GET /analyses/\{id}/screenshot](analysis-screenshot.md)

Note that the signed URL is valid for 5 minutes. If the link expires, you must request the endpoint again to generate a new one. The underlying asset is an image/png file.

## examples

Check if a screenshot is available for Analysis ID "u-109b1fe44b83bfdeaeee0d238e041915b6d71f6ce4b91f8f9ad79eac3ac7d27f-6d2fb381".

```python
import requests

id = "u-109b1fe44b83bfdeaeee0d238e041915b6d71f6ce4b91f8f9ad79eac3ac7d27f-6d2fb381"
url = f"https://www.virustotal.com/api/v3/analyses/{id}/screenshot_url"

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
    "/analyses/{id}/screenshot_url": {
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
            "description": "URL analysis ID. Must match the format `u-<sha256>-<suffix>`. File analyses do not have a screenshot."
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
        "operationId": "get_analyses-id-screenshot-url",
        "summary": "Get the URL for a URL analysis screenshot"
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

← [Get a URL analysis screenshot](analysis-screenshot.md) · [up](../README.md) · [Get a URL analysis DOM](analysis-dom.md) →

*Archived from <https://gtidocs.virustotal.com/reference/analysis-screenshot-url>.*
