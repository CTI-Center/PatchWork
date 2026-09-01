---
title: "Get objects related to a report"
source: https://gtidocs.virustotal.com/reference/get-report-relationships
slug: get-report-relationships
section: reference
group: "Reports & Analysis"
updatedAt: 2026-08-18T15:00:51.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Reports & Analysis](../README.md) › [Reports](../reports.md) › Get objects related to a report

---

# get-objects-related-to-a-report

> 🚧 Special privileges required
>
> Reports & Analysis are only available to users with the Google Threat Intelligence (Google TI) Enterprise or Enterprise Plus licenses.

This endpoint returns available Report's relationships that are described in the [Reports](../../17-api-objects/report-object.md#relationships) object documentation.

## examples

Get 15 files related to the Zarya Hacktivist Group `report--24-10072685`

```python
import requests
import urllib

object_id = "report--24-10072685"
relationship = "files"
limit = 10
url = f"https://www.virustotal.com/api/v3/collections/{object_id}/{relationship}?limit={limit}"
headers = {"accept": "application/json","x-apikey": <api-key>}
response = requests.get(url, headers=headers)
```

Get all the objects associated to this Blizzard related report `report--42da08f2694dbad8af81281fa3ccc83a44891c13bb56134ca54098127977c222`

```python
import requests
import urllib

object_id = "report--42da08f2694dbad8af81281fa3ccc83a44891c13bb56134ca54098127977c222"
relationship = "associations"
url = f"https://www.virustotal.com/api/v3/collections/{object_id}/{relationship}"
headers = {"accept": "application/json","x-apikey": <api-key>}
response = requests.get(url, headers=headers)
```

# openapi-definition

```json
{
  "info": {
    "title": "Reports & Analysis",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Reports",
      "description": "Reports & Analysis endpoints"
    }
  ],
  "paths": {
    "/collections/{id}/{relationship}": {
      "get": {
        "tags": [
          "Reports"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-report-relationships",
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
            "description": "Report's ID",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Relationship name (see [table](https://gtidocs.readme.io/reference/report-object#relationships))",
            "in": "path",
            "name": "relationship",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Maximum number of related objects to retrieve",
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
        "security": [],
        "summary": "Get objects related to a report"
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

← [Get object descriptors related to a report](get-report-related-descriptors.md) · [up](../README.md) · [Get comments from a report](get-report-comments.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-report-relationships>.*
