---
title: "Get a preview of the content downloaded during a URL analysis"
source: https://gtidocs.virustotal.com/reference/analysis-content-preview
slug: analysis-content-preview
section: reference
group: "IoC Investigation"
updatedAt: 2026-07-02T10:07:43.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Analyses, Submissions & Operations](../analyses-submissions-operations.md) › Get a preview of the content downloaded during a URL analysis

---

# get-a-preview-of-the-content-downloaded-during-a-url-analysis

When a [URL Analysis](../../17-api-objects/url-analysis-object.md) downloads a non-binary response (HTML, JSON, XML, plain text, …), this endpoint returns UTF-8 plain-text preview slices of that content.

The endpoint pages through the file: each request returns up to `limit` bytes starting at `cursor`, and reports a new cursor in the response so you can continue from where you left off.

```json
{
  "data": "<preview text>",
  "meta": {
    "cursor": 65536
  }
}
```

Note that only the **first page** (`cursor == 0`) consumes intelligence download quota; subsequent paged calls do not.

# openapi-definition

```json
{
  "info": {
    "title": "IoC Investigation",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "paths": {
    "/analyses/{id}/content_preview": {
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
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Your API key"
          },
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "URL analysis ID. Must match the format `u-<sha256>-<suffix>`. File analyses do not have a preview."
          },
          {
            "in": "query",
            "name": "limit",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": "3,145,728 bytes (3MB)"
            },
            "description": "The maximum number of bytes to return in this request. Max value 3,145,728 bytes (3MB)."
          },
          {
            "in": "query",
            "name": "cursor",
            "schema": {
              "type": "integer",
              "default": "0",
              "format": "int32"
            },
            "description": "Byte offset to start from"
          }
        ],
        "summary": "Get a preview of the content downloaded during a URL analysis",
        "operationId": "get_analyses-id-content-preview"
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

← [Get strings extracted from the content downloaded during a URL analysis](analysis-content-strings.md) · [up](../README.md) · [Download strings extracted from the content downloaded during a URL analysis](analysis-content-strings-download.md) →

*Archived from <https://gtidocs.virustotal.com/reference/analysis-content-preview>.*
