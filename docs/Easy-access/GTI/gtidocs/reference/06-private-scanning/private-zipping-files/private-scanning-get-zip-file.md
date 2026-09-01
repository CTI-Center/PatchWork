---
title: "Check a ZIP file’s status"
source: https://gtidocs.virustotal.com/reference/private-scanning-get-zip-file
slug: private-scanning-get-zip-file
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:37:22.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private Zipping files](../private-zipping-files.md) › Check a ZIP file’s status

---

# check-a-zip-file’s-status

This endpoint returns information about a ZIP file.

```json Example response
{
  \"data\": {
    \"type\": \"zip_file\",
    \"id\": \"4939392292\",
    \"attributes\": {
      \"status\": \"creating\",
      \"progress\": 45,
      \"files_ok\": 3,
      \"files_error\": 0
    }
  }
}
```

The `status` attribute contains one of the following statuses:

* `starting`
* `creating`
* `finished`
* `timeout`
* `error-starting`
* `error-creating`

When the status is finished you may proceed to download the file.

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
    "/zip_files/{id}": {
      "get": {
        "tags": [
          "Private Zipping files"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "private-scanning-get-zip-file",
        "parameters": [
          {
            "description": "ZIP file identifier",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Your API key",
            "in": "header",
            "name": "x-apikey",
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
        "summary": "Check a ZIP file’s status"
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

← [Create a password-protected ZIP with Google Threat Intelligence files](private-scanning-zip-files.md) · [up](../README.md) · [Download a ZIP file](private-scanning-download-zip-file.md) →

*Archived from <https://gtidocs.virustotal.com/reference/private-scanning-get-zip-file>.*
