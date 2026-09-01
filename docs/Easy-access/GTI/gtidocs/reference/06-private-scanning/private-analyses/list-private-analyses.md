---
title: "List private analyses"
source: https://gtidocs.virustotal.com/reference/list-private-analyses
slug: list-private-analyses
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:37:12.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private Analyses](../private-analyses.md) › List private analyses

---

# list-private-analyses

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

Returns a list of the last [private analyses](../../17-api-objects/private-analyses-object.md). The analyses are sorted by most recent first. You can use `?order=date-` to reverse the order.

```json /api/v3/private/analyses
{
  "meta": {
    "cursor": <string>,
    "count": <int>
  },
  "data": {
    <PRIVATE_ANALYSIS_OBJECT>,
    <PRIVATE_ANALYSIS_OBJECT>,
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
		"count": 90,
		"cursor": "1"
	},
	"data": [
		{
			"attributes": {
				"status": "completed",
				"sandbox_status": {
					"Zenbox": {
						"status": "finished",
						"in_progress_percent": 100
					}
				},
				"sandbox_configuration": {
					"enable_internet": false,
					"command_line": ""
				},
				"date": 1666170912
			},
			"type": "private_analysis",
			"id": "NTJjNTM1MThmMzhiNWRiNGE1ZWQ5ZDhiZjQyNWY2NzM6NTJjMjllYmQ3MThjODM2OWRjNmFiNmIzOTc2MmM3OTY6MTY2NjE3MDkxMg==",
			"links": {
				"item": "https://www.virustotal.com/api/v3/private/files/16f6c6439c5b971218b9cd1d616ba40c7cad08c94984ecfde443dfa3c61c6152",
				"self": "https://www.virustotal.com/api/v3/private/analyses/NTJjNTM1MThmMzhiNWRiNGE1ZWQ5ZDhiZjQyNWY2NzM6NTJjMjllYmQ3MThjODM2OWRjNmFiNmIzOTc2MmM3OTY6MTY2NjE3MDkxMg=="
			}
		}
	],
	"links": {
		"self": "https://www.virustotal.com/api/v3/private/analyses?limit=1",
		"next": "https://www.virustotal.com/api/v3/private/analyses?cursor=1&limit=1"
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
      "name": "Private Analyses"
    }
  ],
  "paths": {
    "/analyses": {
      "get": {
        "tags": [
          "Private Analyses"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "list-private-analyses",
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
          },
          {
            "description": "Sorting order",
            "in": "query",
            "name": "order",
            "schema": {
              "default": "date-",
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
        "summary": "List private analyses"
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

← [Private Analyses](../private-analyses.md) · [up](../README.md) · [Get a private analysis](private-analysis.md) →

*Archived from <https://gtidocs.virustotal.com/reference/list-private-analyses>.*
