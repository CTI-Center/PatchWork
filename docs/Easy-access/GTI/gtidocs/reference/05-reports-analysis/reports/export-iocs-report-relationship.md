---
title: "Export IOCs from a given report's relationship"
source: https://gtidocs.virustotal.com/reference/export-iocs-report-relationship
slug: export-iocs-report-relationship
section: reference
group: "Reports & Analysis"
updatedAt: 2025-09-25T00:36:47.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Reports & Analysis](../README.md) › [Reports](../reports.md) › Export IOCs from a given report's relationship

---

# export-iocs-from-a-given-report's-relationship

> 🚧 Special privileges required
>
> Reports & Analysis are only available to users with the Google Threat Intelligence (Google TI) Enterprise or Enterprise Plus licenses.

## examples

Export the list of domains related to a given [Report](../../17-api-objects/report-object.md).

```python
import requests
import urllib

object_id = "report--24-10074013"
relationship = "domains"
format = "stix"
url = f"https://www.virustotal.com/api/v3/collections/{object_id}/{relationship}/download/{format}"
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
    "/collections/{id}/{relationship}/download/{format}": {
      "get": {
        "tags": [
          "Reports"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "export-iocs-report-relationship",
        "parameters": [
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
            "description": "Export format (one of `json`, `csv`, or `stix`)",
            "in": "path",
            "name": "format",
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
                    "value": "{\n  \"files\": [\n    \"009cc0f34f60467552ef79c3892c501043c972be55fe936efb30584975d45ec0\",\n    \"153117aa54492ca955b540ac0a8c21c1be98e9f7dd8636a36d73581ec1ddcf58\",\n    \"18479a93fc2d5acd7d71d596f27a5834b2b236b44219bb08f6ca06cf760b74f6\"\n  ]\n}"
                  }
                },
                "schema": {
                  "properties": {
                    "files": {
                      "items": {
                        "type": "string"
                      },
                      "type": "array"
                    }
                  },
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
        "summary": "Export IOCs from a given report's relationship"
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

← [Export aggregations / commonalities from a report](export-report-aggregations.md) · [up](../README.md) · [Download a Report](download-report.md) →

*Archived from <https://gtidocs.virustotal.com/reference/export-iocs-report-relationship>.*
