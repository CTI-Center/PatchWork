---
title: "Get a private analysis"
source: https://gtidocs.virustotal.com/reference/private-analysis
slug: private-analysis
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:37:13.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private Analyses](../private-analyses.md) › Get a private analysis

---

# get-a-private-analysis

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

With this endpoint you can check the status of a private file analysis. It expects the analysis ID returned by the [POST /private/files](../private-files/upload-file-private-scanning.md) endpoint, and will return a private analysis object with information about the analysis.

```json Example response
{
  "meta": {
    "file_info": {
      "size": 5,
      "sha256": "11a77c3d96c06974b53d7f40a577e6813739eb5c811b2a86f59038ea90add772",
      "sha1": "7bae8076a5771865123be7112468b79e9d78a640",
      "md5": "e5828c564f71fea3a12dde8bd5d27063"
    }
  },
  "data": {
    "attributes": {
      "date": 1620127014,
      "status": "completed"
    },
    "type": "private_analysis",
    "id": "ZTU4MjhjNTY0ZjcxZmVhM2ExMmRkZThiZDVkMjcwNjM6MTYyMDEyNzAxNA==",
    "links": {
      "self": "https://virustotal.com/api/v3/private/analyses/ZTU4MjhjNTY0ZjcxZmVhM2ExMmRkZThiZDVkMjcwNjM6MTYyMDEyNzAxNA=="
    }
  }
}
```

The `status` attribute in the private analysis object can be any of the following:

`initializing`\
`enqueueing`\
`queued`\
`running`\
`post-processing`\
`finished`\
`error`\
`retrying`\
`unsupported file type`\
`corrupted file`\
`timeout`\
`startup error`\
`missing dependency`

Once it gets completed, you can use the `sha256` in the `file_info` section with the [GET /private/files/\{id}](../private-files/private-files-info.md) for getting all the information that VirusTotal has generated for the analysed file. Alternatively you could use [GET /private/analyses/\{id}/item](private-analyses-relationship.md) for the same purpose.

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
      "name": "Private Analyses"
    }
  ],
  "paths": {
    "/analyses/{id}": {
      "get": {
        "tags": [
          "Private Analyses"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "private-analysis",
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
            "description": "Analysis identifier",
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
        "summary": "Get a private analysis"
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

← [List private analyses](list-private-analyses.md) · [up](../README.md) · [Get object descriptors related to a private analysis](private-analyses-relationships-descriptor.md) →

*Archived from <https://gtidocs.virustotal.com/reference/private-analysis>.*
