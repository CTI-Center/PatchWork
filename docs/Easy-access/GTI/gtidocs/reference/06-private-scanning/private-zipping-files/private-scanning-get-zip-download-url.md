---
title: "Get a ZIP file’s download URL"
source: https://gtidocs.virustotal.com/reference/private-scanning-get-zip-download-url
slug: private-scanning-get-zip-download-url
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T01:35:07.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private Zipping files](../private-zipping-files.md) › Get a ZIP file’s download URL

---

# get-a-zip-file’s-download-url

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
    "/zip_files/{id}/download_url": {
      "get": {
        "tags": [
          "Private Zipping files"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "private-scanning-get-zip-download-url",
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

← [Download a ZIP file](private-scanning-download-zip-file.md) · [up](../README.md) · [Vulnerabilities](../../07-vulnerability-intelligence/vulnerabilities.md) →

*Archived from <https://gtidocs.virustotal.com/reference/private-scanning-get-zip-download-url>.*
