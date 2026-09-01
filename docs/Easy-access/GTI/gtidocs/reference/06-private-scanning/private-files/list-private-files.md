---
title: "List private files"
source: https://gtidocs.virustotal.com/reference/list-private-files
slug: list-private-files
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:36:54.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private Files](../private-files.md) › List private files

---

# list-private-files

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

Returns a list of previously analysed [private files](../../17-api-objects/private-files-object.md). The files are always ordered by SHA256.

```json /api/v3/private/files
{
  "meta": {
    "cursor": <string>,
    "count": <int>
  },
  "data": {
    <PRIVATE_FILE_OBJECT>,
    <PRIVATE_FILE_OBJECT>,
    ...
  },
  "links": {
    "self": <string>,
    "next": <string>
  }
}
```
```json
{
	"meta": {
		"cursor": "079b1db08ac52c94be8fdb5b638134a6109a510bc10a87c15413d6c793985678",
		"count": 19
	},
	"data": [
		{
			"attributes": {
				"type_description": "Windows Installer",
        ...
      },
      "type": "private_file",
      "id": "079b1db08ac52c94be8fdb5b638134a6109a510bc10a87c15413d6c793985678",
      "links": {
        "self": "https://www.virustotal.com/api/v3/private/files/079b1db08ac52c94be8fdb5b638134a6109a510bc10a87c15413d6c793985678"
      }
    },
    ...
  ],
  "links": {
		"self": "https://www.virustotal.com/api/v3/private/files?limit=1",
		"next": "https://www.virustotal.com/api/v3/private/files?cursor=079b1db08ac52c94be8fdb5b638134a6109a510bc10a87c15413d6c793985678&limit=1"
	}
}
```

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
    "/files": {
      "get": {
        "tags": [
          "Private Files"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "list-private-files",
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
            "description": "Maximum number of files to retrieve (40 max)",
            "in": "query",
            "name": "limit",
            "schema": {
              "default": 10,
              "format": "int32",
              "type": "integer",
              "maximum": 40,
              "minimum": 0
            }
          },
          {
            "description": "Continuation cursor",
            "in": "query",
            "name": "cursor",
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
        "summary": "List private files"
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

← [Upload a file](upload-file-private-scanning.md) · [up](../README.md) · [Get a URL for uploading large files](private-files-upload-url.md) →

*Archived from <https://gtidocs.virustotal.com/reference/list-private-files>.*
