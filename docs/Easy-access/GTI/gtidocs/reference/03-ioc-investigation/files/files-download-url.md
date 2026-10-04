---
title: "Get a file’s download URL"
source: https://gtidocs.virustotal.com/reference/files-download-url
slug: files-download-url
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T02:03:53.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Files](../files.md) › Get a file’s download URL

---

# get-a-file’s-download-url

This endpoint returns a signed URL from where you can download the specified file. Getting the URL counts as a file download in your quota, even if you don't actually download the file, but once you have the URL you can use it to download the file multiple times without consuming any quota at all. The URL expires after 1 hour.

```json Example response
{
  "data": "https://vtsamples.commondatastorage.googleapis.com/275a..fd0f?GoogleAccessId=758681729565-rc7fcckv235v1@developer.gserviceaccount.com&Expires=1524733537&Signature=GRs9WLy...oHA%3D"
}
```

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
      "name": "Files"
    }
  ],
  "paths": {
    "/files/{id}/download_url": {
      "get": {
        "tags": [
          "Files"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "files-download-url",
        "parameters": [
          {
            "description": "SHA-256, SHA-1 or MD5 identifying the file",
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
        "summary": "Get a file’s download URL"
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

← [Download a file](files-download.md) · [up](../README.md) · [Get object descriptors related to a file](files-relationships-ids.md) →

*Archived from <https://gtidocs.virustotal.com/reference/files-download-url>.*
