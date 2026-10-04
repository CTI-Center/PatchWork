---
title: "Get a URL for uploading large files"
source: https://gtidocs.virustotal.com/reference/files-upload-url
slug: files-upload-url
section: reference
group: "IoC Investigation"
updatedAt: 2026-02-05T12:43:34.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Files](../files.md) › Get a URL for uploading large files

---

# get-a-url-for-uploading-large-files

For uploading files smaller than 32MB you can simply use the [POST /files](files-scan.md) endpoint, but for larger files you need to obtain a special upload URL first, and then send the `POST` request to the upload URL instead of sending it to `/files`. The `POST` request should have the same format expected by the  [POST /files](files-scan.md) endpoint. Each upload URL can be used only once.

> 📘 Files larger than 200MBs
>
> Notice that although the actual size limit is 650MBs, files larger than 200MBs tend to be bundles of some sort, (compressed files, ISO images, etc.) in these cases it makes sense to upload the inner individual files instead for several reasons, as an example:
>
> * Engines tend to have performance issues on big files (timeouts, some may not even scan them).
> * Some engines are not able to inspect certain file types whereas they will be able to inspect the inner files if submitted.
> * When scanning a big bundle you lose context on which specific inner file is causing the detection.

```json Example response
{
  "data": "http://www.virustotal.com/_ah/upload/AMmfu6b-_DXUeFe36Sb3b0F4B8mH9Nb-CHbRoUNVOPwG/"
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
    "/files/upload_url": {
      "get": {
        "tags": [
          "Files"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "files-upload-url",
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
        "summary": "Get a URL for uploading large files"
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

← [Files](../files.md) · [up](../README.md) · [Upload a file](files-scan.md) →

*Archived from <https://gtidocs.virustotal.com/reference/files-upload-url>.*
