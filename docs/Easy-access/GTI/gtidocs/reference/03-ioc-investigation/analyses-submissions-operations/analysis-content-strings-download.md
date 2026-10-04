---
title: "Download strings extracted from the content downloaded during a URL analysis"
source: https://gtidocs.virustotal.com/reference/analysis-content-strings-download
slug: analysis-content-strings-download
section: reference
group: "IoC Investigation"
updatedAt: 2026-07-02T10:07:50.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Analyses, Submissions & Operations](../analyses-submissions-operations.md) › Download strings extracted from the content downloaded during a URL analysis

---

# download-strings-extracted-from-the-content-downloaded-during-a-url-analysis

This endpoint returns the same strings exposed by [GET /analyses/{id}/content\_strings](analysis-content-strings.md), but joined with newlines and served as a plain-text attachment so it can be saved straight to disk.

# openapi-definition

```json
{
  "info": {
    "title": "IoC Investigation",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "paths": {
    "/analyses/{id}/content_strings/download": {
      "get": {
        "description": "",
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "text/plain": {
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
            "description": "URL analysis ID. Must match the format `u-<sha256>-<suffix>`. File analyses do not have a strings."
          }
        ],
        "summary": "Download strings extracted from the content downloaded during a URL analysis",
        "operationId": "get_analyses-id-content-strings-download"
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

← [Get a preview of the content downloaded during a URL analysis](analysis-content-preview.md) · [up](../README.md) · [Attack Tactics](../attack-tactics.md) →

*Archived from <https://gtidocs.virustotal.com/reference/analysis-content-strings-download>.*
