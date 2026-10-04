---
title: "Get a private file report"
source: https://gtidocs.virustotal.com/reference/private-files-info
slug: private-files-info
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:36:57.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private Files](../private-files.md) › Get a private file report

---

# get-a-private-file-report

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

> 🚧 gti\_assessment attribute
>
> To get the **gti\_assessment** attribute in the JSON response, ensure that the **x-tool** header is added to the request headers. This header should be used to identify your tool or service with a custom name.

This endpoint return information about a file scanned privately. Notice that it only accepts SHA-256 as the file's ID, MD5 and SHA-1 are not supported like in its [GET /files/\{id}](../../03-ioc-investigation/files/file-info.md) public counterpart. The SHA-256 for the analysed file can be computed by yourself or obtained from the response to the call to [GET /analyses/\{id}](../private-analyses/private-analysis.md).

```json Example response
{
  "data": {
    "attributes": {
      "sha1": "7bae8076a5771865123be7112468b79e9d78a640",
      "magic": "ASCII text",
      "tags": [
        "text"
      ],
      "exiftool": {
        "MIMEType": "text/plain",
        "LineCount": "1",
        "MIMEEncoding": "us-ascii",
        "FileTypeExtension": "txt",
        "FileType": "TXT",
        "WordCount": "1",
        "Newlines": "Unix LF"
      },
      "trid": [
        {
          "file_type": "file seems to be plain text/ASCII",
          "probability": 0.0
        }
      ],
      "vhash": "9eecb7db59d16c80417c72d1e1f4fbf1",
      "sha256": "11a77c3d96c06974b53d7f40a577e6813739eb5c811b2a86f59038ea90add772",
      "ssdeep": "3:tdn:T",
      "md5": "e5828c564f71fea3a12dde8bd5d27063",
      "size": 5
    },
    "type": "private_file",
    "id": "11a77c3d96c06974b53d7f40a577e6813739eb5c811b2a86f59038ea90add772",
    "links": {
      "self": "https://www.virustotal.com/api/v3/private/files/11a77c3d96c06974b53d7f40a577e6813739eb5c811b2a86f59038ea90add772"
    }
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
    "/files/{id}": {
      "get": {
        "tags": [
          "Private Files"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "private-files-info",
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
            "description": "The name of your tool or service. This is required to obtain the gti_assesment data",
            "in": "header",
            "name": "x-tool",
            "required": false,
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
        "summary": "Get a private file report"
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

← [Delete a private file report](delete-file-private-scanning.md) · [up](../README.md) · [Get object descriptors related to a file](privatefilesidrelationshipsrelationship.md) →

*Archived from <https://gtidocs.virustotal.com/reference/private-files-info>.*
