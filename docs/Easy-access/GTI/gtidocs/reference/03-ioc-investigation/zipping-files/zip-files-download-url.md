---
title: "Get a ZIP file’s download URL"
source: https://gtidocs.virustotal.com/reference/zip-files-download-url
slug: zip-files-download-url
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T02:04:49.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Zipping files](../zipping-files.md) › Get a ZIP file’s download URL

---

# get-a-zip-file’s-download-url

This endpoint returns a signed URL from where you can download the specified ZIP file. The URL expires after 1 hour.

# openapi-definition

```json
{
  "info": {
    "title": "IoC Investigation",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Zipping files"
    }
  ],
  "paths": {
    "/intelligence/zip_files/{id}/download_url": {
      "get": {
        "tags": [
          "Zipping files"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "zip-files-download-url",
        "parameters": [
          {
            "description": "Your API key",
            "in": "header",
            "name": "x-apikey",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "ZIP file identifier",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "properties": {},
                  "type": "object"
                }
              }
            },
            "description": "200"
          },
          "400": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "properties": {},
                  "type": "object"
                }
              }
            },
            "description": "400"
          }
        },
        "security": [],
        "summary": "Get a ZIP file’s download URL"
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

← [Download a ZIP file](zip-files-download.md) · [up](../README.md) · [Search & Metadata](../search-metadata.md) →

*Archived from <https://gtidocs.virustotal.com/reference/zip-files-download-url>.*
