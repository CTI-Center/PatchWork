---
title: "Delete a private file report"
source: https://gtidocs.virustotal.com/reference/delete-file-private-scanning
slug: delete-file-private-scanning
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:36:56.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private Files](../private-files.md) › Delete a private file report

---

# delete-a-private-file-report

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

This endpoint deletes a private file from storage, as well as all the PrivateFile and PrivateAnalysis associated with it (unless `only_from_storage=true` is used.

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
      "name": "Private Files"
    }
  ],
  "paths": {
    "/files/{id}": {
      "delete": {
        "tags": [
          "Private Files"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "delete-file-private-scanning",
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
            "description": "File's SHA-256",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "If true, only the file will be deleted from storage, but the generated reports and analyses won't.",
            "in": "query",
            "name": "only_from_storage",
            "schema": {
              "default": false,
              "type": "boolean"
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
        "summary": "Delete a private file report"
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

← [Get a URL for uploading large files](private-files-upload-url.md) · [up](../README.md) · [Get a private file report](private-files-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/delete-file-private-scanning>.*
