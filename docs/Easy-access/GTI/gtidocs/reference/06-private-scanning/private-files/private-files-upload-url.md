---
title: "Get a URL for uploading large files"
source: https://gtidocs.virustotal.com/reference/private-files-upload-url
slug: private-files-upload-url
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:36:55.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private Files](../private-files.md) › Get a URL for uploading large files

---

# get-a-url-for-uploading-large-files

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

For uploading files smaller than 32MB you can simply use the [POST /files](upload-file-private-scanning.md) endpoint, but for larger files you need to obtain a special upload URL first, and then send the `POST` request to the upload URL instead of sending it to `/private/files`. The `POST` request should have the same format expected by the  [POST /files](upload-file-private-scanning.md) endpoint. Each upload URL can be used only once.

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
    "/files/upload_url": {
      "get": {
        "tags": [
          "Private Files"
        ],
        "parameters": [
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
        "deprecated": false,
        "description": "",
        "operationId": "private-files-upload-url",
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
        "summary": "Get a URL for uploading large files"
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

← [List private files](list-private-files.md) · [up](../README.md) · [Delete a private file report](delete-file-private-scanning.md) →

*Archived from <https://gtidocs.virustotal.com/reference/private-files-upload-url>.*
