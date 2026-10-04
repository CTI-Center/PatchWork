---
title: "Export aggregations / commonalities from a report"
source: https://gtidocs.virustotal.com/reference/export-report-aggregations
slug: export-report-aggregations
section: reference
group: "Reports & Analysis"
updatedAt: 2025-09-25T00:36:46.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Reports & Analysis](../README.md) › [Reports](../reports.md) › Export aggregations / commonalities from a report

---

# export-aggregations-/-commonalities-from-a-report

> 🚧 Special privileges required
>
> Reports & Analysis are only available to users with the Google Threat Intelligence (Google TI) Enterprise or Enterprise Plus licenses.

## examples

Export commonalities from a [Report](../../17-api-objects/report-object.md).

```python
import requests
import urllib

object_id = "report--24-10074013"
format = "csv"
url = f"https://www.virustotal.com/api/v3/collections/{object_id}/aggregations/download/{format}"
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
    "/collections/{id}/aggregations/download/{format}": {
      "get": {
        "tags": [
          "Reports"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "export-report-aggregations",
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
            "description": "Export format (one of `json` or `csv`)",
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
                    "value": "{\n\t\"files\": {\n\t\t\"contacted_urls\": [\n\t\t\t{\n\t\t\t\t\"count\": 2,\n\t\t\t\t\"value\": \"http://ocsp.digicert.com/\"\n\t\t\t},\n\t\t\t{\n\t\t\t\t\"count\": 2,\n\t\t\t\t\"value\": \"http://crl3.digicert.com/Omniroot2025.crl\"\n\t\t\t}\n      ...\n\t\t],\n\t\t\"contacted_domains\": [\n\t\t\t{\n\t\t\t\t\"count\": 4,\n\t\t\t\t\"value\": \"nexusrules.officeapps.live.com\"\n\t\t\t},\n\t\t\t{\n\t\t\t\t\"count\": 4,\n\t\t\t\t\"value\": \"officeclient.microsoft.com\"\n\t\t\t},\n      ...\n\t\t],\n    ...\n\t},\n  ...\n}"
                  }
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
        "summary": "Export aggregations / commonalities from a report"
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

← [Export IOCs from a report](export-report-iocs.md) · [up](../README.md) · [Export IOCs from a given report's relationship](export-iocs-report-relationship.md) →

*Archived from <https://gtidocs.virustotal.com/reference/export-report-aggregations>.*
