---
title: "Request a file rescan (re-analyse)"
source: https://gtidocs.virustotal.com/reference/files-analyse
slug: files-analyse
section: reference
group: "IoC Investigation"
updatedAt: 2026-02-05T12:43:34.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Files](../files.md) › Request a file rescan (re-analyse)

---

# request-a-file-rescan-(re-analyse)

> ❗️ Caution
>
> This API endpoint has the potential to produce a denial of service on the scanning infrastructure if abused. Please contact us if you are going to be rescanning more than 50K files per day.

Files that have been already uploaded to Google TI can be re-analysed without uploading them again, you can use this endpoint for that purpose. The response is an object descriptor for the new analysis as in the [POST /files](files-scan.md) endpoint. The ID contained in the descriptor can be used with the [GET /analyses/\{id}](../analyses-submissions-operations/analysis.md) endpoint to get information about the analysis.

```json Example response
{
  "data": {
    "type": "analysis",
    "id": "NjY0MjRlOTFjMDIyYTkyNWM0NjU2NWQzYWNlMzFmZmI6MTQ3NTA0ODI3Nw=="
  }
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
    "/files/{id}/analyse": {
      "post": {
        "tags": [
          "Files"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "files-analyse",
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
        "summary": "Request a file rescan (re-analyse)"
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

← [Get a file report](file-info.md) · [up](../README.md) · [Get comments on a file](files-comments-get.md) →

*Archived from <https://gtidocs.virustotal.com/reference/files-analyse>.*
