---
title: "Get strings extracted from the content downloaded during a URL analysis"
source: https://gtidocs.virustotal.com/reference/analysis-content-strings
slug: analysis-content-strings
section: reference
group: "IoC Investigation"
updatedAt: 2026-07-02T10:07:30.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Analyses, Submissions & Operations](../analyses-submissions-operations.md) › Get strings extracted from the content downloaded during a URL analysis

---

# get-strings-extracted-from-the-content-downloaded-during-a-url-analysis

This endpoint returns the list of printable strings extracted from the file downloaded during a [URL Analysis](../../17-api-objects/url-analysis-object.md). It is useful for triaging payloads dropped by a malicious URL (binaries, scripts, archives) without downloading the full file.

The strings are returned as a paginated list where each entry includes the string itself  (`value`) and its encoding format (`type`), which can be either `unicode` or `ascii`:

```json
{
  "data": [
    {
      "value": "<printable string>",
      "type": "ascii"
    },
    {
      "value": "<another string>",
      "type": "ascii"
    }
  ],
  "meta": {
    "cursor": "<opaque>"
  }
}
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
    "/analyses/{id}/content_strings": {
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
            "description": "URL analysis ID. Must match the format `u-<sha256>-<suffix>`. File analyses do not have a strings."
          },
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
            "in": "query",
            "name": "limit",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": "10"
            },
            "description": "maximum number of strings to return in a single page. Max value 40."
          },
          {
            "in": "query",
            "name": "cursor",
            "schema": {
              "type": "string"
            },
            "description": "Pagination cursor returned by a previous request"
          }
        ],
        "operationId": "get_analyses-id-content-strings",
        "summary": "Get strings extracted from the content downloaded during a URL analysis"
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

← [Get the URL for a URL analysis DOM](analysis-dom-url.md) · [up](../README.md) · [Get a preview of the content downloaded during a URL analysis](analysis-content-preview.md) →

*Archived from <https://gtidocs.virustotal.com/reference/analysis-content-strings>.*
