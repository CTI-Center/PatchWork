---
title: "Download a ZIP file"
source: https://gtidocs.virustotal.com/reference/private-scanning-download-zip-file
slug: private-scanning-download-zip-file
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T01:35:07.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private Zipping files](../private-zipping-files.md) › Download a ZIP file

---

# download-a-zip-file

# openapi-definition

```json
{
  "info": {
    "title": "Private Scanning",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Private Zipping files"
    }
  ],
  "paths": {
    "/zip_files/{id}/download": {
      "get": {
        "tags": [
          "Private Zipping files"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "private-scanning-download-zip-file",
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
      "url": "https://www.virustotal.com/api/v3/private"
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

← [Check a ZIP file’s status](private-scanning-get-zip-file.md) · [up](../README.md) · [Get a ZIP file’s download URL](private-scanning-get-zip-download-url.md) →

*Archived from <https://gtidocs.virustotal.com/reference/private-scanning-download-zip-file>.*
