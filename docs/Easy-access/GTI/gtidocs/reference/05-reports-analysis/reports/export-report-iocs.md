---
title: "Export IOCs from a report"
source: https://gtidocs.virustotal.com/reference/export-report-iocs
slug: export-report-iocs
section: reference
group: "Reports & Analysis"
updatedAt: 2025-09-25T00:36:45.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Reports & Analysis](../README.md) › [Reports](../reports.md) › Export IOCs from a report

---

# export-iocs-from-a-report

> 🚧 Special privileges required
>
> Reports & Analysis are only available to users with the Google Threat Intelligence (Google TI) Enterprise or Enterprise Plus licenses.

## examples

Export IoCs from a [Report](../../17-api-objects/report-object.md).

```python
import requests
import urllib

object_id = "report--24-10074013"
format = "json"
url = f"https://www.virustotal.com/api/v3/collections/{object_id}/download/{format}"
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
    "/collections/{id}/download/{format}": {
      "get": {
        "tags": [
          "Reports"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "export-report-iocs",
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
            "description": "Export format (one of `json`, `csv`, or `stix`)",
            "in": "path",
            "name": "format",
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
                    "value": "{\n  \"files\": [\n    \"009cc0f34f60467552ef79c3892c501043c972be55fe936efb30584975d45ec0\",\n    \"153117aa54492ca955b540ac0a8c21c1be98e9f7dd8636a36d73581ec1ddcf58\",\n    \"18479a93fc2d5acd7d71d596f27a5834b2b236b44219bb08f6ca06cf760b74f6\"\n  ],\n  \"threat_actors\": [\n    \"muddywater\"\n  ],\n  \"references\": [\n    \"153590cf5677a6ab5b5103382d41d4d8868a878a04104e86e936db63e4d186b8\"\n  ],\n  \"urls\": [\n    \"http://abrahamseed.co.za/db_template.php\",\n    \"http://absfinancialplanning.co.za/images/db_template.php\"\n  ]\n}"
                  }
                },
                "schema": {
                  "properties": {
                    "files": {
                      "items": {
                        "type": "string"
                      },
                      "type": "array"
                    },
                    "references": {
                      "items": {
                        "type": "string"
                      },
                      "type": "array"
                    },
                    "threat_actors": {
                      "items": {
                        "type": "string"
                      },
                      "type": "array"
                    },
                    "urls": {
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
        "summary": "Export IOCs from a report"
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

← [Search IoCs inside a report](search-iocs-inside-a-report.md) · [up](../README.md) · [Export aggregations / commonalities from a report](export-report-aggregations.md) →

*Archived from <https://gtidocs.virustotal.com/reference/export-report-iocs>.*
