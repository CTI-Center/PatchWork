---
title: "Rescan a private file"
source: https://gtidocs.virustotal.com/reference/rescan-a-private-file
slug: rescan-a-private-file
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:37:00.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private Files](../private-files.md) › Rescan a private file

---

# rescan-a-private-file

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

Reanalyses a private file. The same params from [/files](../../03-ioc-investigation/files/files-scan.md) (other than the file) are accepted. Returns a [private analysis](../../17-api-objects/private-analyses-object.md).

```json Example
{
	"data": {
		"type": "private_analysis",
		"id": "ZmI5Y2VmNGJmZDIwZTkzNmQ5MzY0NTcwMGI2Nzc2M2Q6Tm9uZToxNjYwODI1NDE1"
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
    "/files/{sha256}/analyse": {
      "post": {
        "tags": [
          "Private Files"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "rescan-a-private-file",
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
            "description": "File's SHA256 hash",
            "in": "path",
            "name": "sha256",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Command line arguments to use when running the file in sandboxes.",
            "in": "query",
            "name": "command_line",
            "required": false,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "If true, then the file won't be detonated in sandbox environments. False by default.",
            "in": "query",
            "name": "disable_sandbox",
            "required": false,
            "schema": {
              "type": "string",
              "default": "false"
            }
          },
          {
            "description": "If the file should have internet access when running in sandboxes. False by default.",
            "in": "query",
            "name": "enable_internet",
            "required": false,
            "schema": {
              "type": "string",
              "default": "false"
            }
          },
          {
            "description": "Intercept HTTPS/TLS/SSL communication. Intercept HTTPS to view encypted URLS, hostnames and HTTP headers.  This is detectable by any sample that checks certificates, and makes JA3 hashes unusable.",
            "in": "query",
            "name": "intercept_tls",
            "required": false,
            "schema": {
              "type": "string",
              "default": "false"
            }
          },
          {
            "description": "Select the sandbox desired for interactive use.",
            "in": "query",
            "name": "interaction_sandbox",
            "required": false,
            "schema": {
              "type": "string",
              "default": "cape"
            }
          },
          {
            "description": "Interaction timeout in seconds, minimum value: 60. (1 minute.) Max value: 1800: (30 minutes).",
            "in": "query",
            "name": "interaction_timeout",
            "required": false,
            "schema": {
              "type": "integer",
              "default": 60,
              "format": "int32",
              "maximum": 1800,
              "minimum": 60
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
        "summary": "Rescan a private file"
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

← [Get objects related to a private file](private-files-relationships.md) · [up](../README.md) · [Private Files Behaviours](../private-files-behaviours.md) →

*Archived from <https://gtidocs.virustotal.com/reference/rescan-a-private-file>.*
