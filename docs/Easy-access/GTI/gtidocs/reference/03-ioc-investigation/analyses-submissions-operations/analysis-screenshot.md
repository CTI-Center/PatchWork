---
title: "Get a URL analysis screenshot"
source: https://gtidocs.virustotal.com/reference/analysis-screenshot
slug: analysis-screenshot
section: reference
group: "IoC Investigation"
updatedAt: 2026-05-26T10:18:38.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Analyses, Submissions & Operations](../analyses-submissions-operations.md) › Get a URL analysis screenshot

---

# get-a-url-analysis-screenshot

This endpoint returns the rendered screenshot captured by Google TI's browser at the end of a [URL Analysis](../../17-api-objects/url-analysis-object.md).

The response `302 Found` redirects to a short-lived (5 minutes) signed URL pointing at the PNG file in Google Cloud Storage. Follow redirects in your HTTP client to retrieve the image bytes.

## examples

Check if a screenshot is available for Analysis ID "u-109b1fe44b83bfdeaeee0d238e041915b6d71f6ce4b91f8f9ad79eac3ac7d27f-6d2fb381".

```python
import requests

id = "u-109b1fe44b83bfdeaeee0d238e041915b6d71f6ce4b91f8f9ad79eac3ac7d27f-6d2fb381"
local_filename = "screenshot.png"
url = f"https://www.virustotal.com/api/v3/analyses/{id}/screenshot"

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
    "/analyses/{id}/screenshot": {
      "get": {
        "description": "",
        "responses": {
          "200": {
            "description": "200",
            "content": {}
          },
          "400": {
            "description": "400",
            "content": {}
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
            "description": "your API key",
            "required": true
          }
        ],
        "operationId": "get_analyses-id-screenshot",
        "summary": "Get a URL analysis screenshot"
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

← [Get an operation object](get-operations-id.md) · [up](../README.md) · [Get the URL for a URL analysis screenshot](analysis-screenshot-url.md) →

*Archived from <https://gtidocs.virustotal.com/reference/analysis-screenshot>.*
