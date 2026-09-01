---
title: "Download a ZIP file"
source: https://gtidocs.virustotal.com/reference/zip-files-download
slug: zip-files-download
section: reference
group: "IoC Investigation"
updatedAt: 2026-02-05T12:43:34.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Zipping files](../zipping-files.md) › Download a ZIP file

---

# download-a-zip-file

This endpoint is similar to [GET /zip\_files/\{id}/download\_url](zip-files-download-url.md), but it redirects you to the download URL. The download URL you are redirected to can be reused as many times as you want for a period of 1 hour. After that period the URL expires and can't be used anymore.

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
    "/intelligence/zip_files/{id}/download": {
      "get": {
        "tags": [
          "Zipping files"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "zip-files-download",
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
        "summary": "Download a ZIP file"
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

← [Check a ZIP file’s status](get-zip-file.md) · [up](../README.md) · [Get a ZIP file’s download URL](zip-files-download-url.md) →

*Archived from <https://gtidocs.virustotal.com/reference/zip-files-download>.*
