---
title: "List reports"
source: https://gtidocs.virustotal.com/reference/list-reports
slug: list-reports
section: reference
group: "Reports & Analysis"
updatedAt: 2025-11-19T10:36:33.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Reports & Analysis](../README.md) › [Reports](../reports.md) › List reports

---

# list-reports

> 🚧 Special privileges required
>
> Reports & Analysis are only available to users with the Google Threat Intelligence (Google TI) Enterprise or Enterprise Plus licenses.

This endpoint allows us to search and filter Google TI [Reports](../../17-api-objects/report-object.md) effectively. It returns a list of Report objects only when filtering by the parameter `collection_type`:`report`.

### searches-observations

* if you don't filter by the `collection_type` this endpoint will return not only Vulnerabilities but other types of objects such as [Vulnerabilitie](../../17-api-objects/vulnerability-object.md), [Threat Actors](../../17-api-objects/threat-actor-object.md), [Malware families](../../17-api-objects/malware-family-object.md), [Software or Toolkits](../../17-api-objects/software-toolkit-object.md), [Campaigns](../../17-api-objects/campaign-object.md) or [IoC Collections](../../17-api-objects/ioc-collection-object.md), matching the rest of the filters.
* filers' values are case-insensitive
* several filters can be combined together in a more complex and specific search
* boolean operators can be used in more complex searches: `AND`, `OR`, `NOT`
* quotes are needed for filters' values with spaces: `description:"Phishing campaign"`
* wildcards (\*) can be used for partial matches: `name:Ransom*`
* date filters formats: `YYYY-MM-DD`, `YYYY-MM-DDTHH-mm-ss`
* date relative formats: `60d` (for days), `10m` (for minutes)
* date ranges can be specified with `+` or `-`: `last_modification_date:7d+`, `creation_date:2024-01-01-`

## allowed-filters-by-object

View the full list of allowed filters [here](https://gtidocs.readme.io/docs/reports-search-modifiers).

> 🚧
>
> To restrict the results to Report objects only, you must use the `collection_type`:`report` search modifier / extra filter.

## allowed-orders

* `order:name+`: sorts objects alphabetically by name, ascending `+` or descending `-`.
* `order:creation_date-`: sorts objects descending `-` (default) by most recently created objects first, or ascending `+` by oldest objects first.
* `order:last_modification_date-`: sorts objects descending `-` by most recently modified objects first, or ascending `+` by firstly modified objects first.
* `order:lookups_trend-`: sorts objects ascending `+` or descending `-` based on the trend of the daily distinct-user lookups over the IoCs of the object in the last 14 days.
* `order:submissions_trend-`: sorts objects ascending `+` or descending `-` based on the trend of the daily distinct-user submissions of IoCs of the object in the last 14 days.
* `order:relevance+`: sorts objects ascending `+` or descending `-` based on the relevance of the object.
* `order:exploitation_state+`: sorts objects ascending `+` or descending `-` based on the exploitation state of the vulnerability.
* `order:risk_rating+`: sorts objects ascending `+` or descending `-` based on the risk rating of the vulnerability.

## examples

Get the list of all crowdsourced Reports created from the beginning of 2024 whose name contains the "phishing" word and sort results descending by creation date (FIFO order).

```python
import requests
import urllib

filters = "collection_type:report name:phishing creation_date:2024-01-01+ origin:Crowdsourced"
order = "creation_date-"
url = f"https://www.virustotal.com/api/v3/collections?filter={urllib.parse.quote(filters)}&order={order}"
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
    "/collections": {
      "get": {
        "tags": [
          "Reports"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "list-reports",
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
            "description": "Maximum number of reports to retrieve (max 40)",
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
            "description": "Filter reports / objects by different properties. ",
            "in": "query",
            "name": "filter",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Sorting order",
            "in": "query",
            "name": "order",
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
                    "value": "{\n\"meta\": {\n  \"cursor\": <string>\n},\n\"data\": [\n  <REPORT_OBJ>,\n  <REPORT_OBJ>,\n  ...\n],\n\"links\": {\n  \"self\": <string>,\n  \"next\": <string>\n}"
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
        "summary": "List reports"
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

← [Reports](../reports.md) · [up](../README.md) · [Get a report](get-report.md) →

*Archived from <https://gtidocs.virustotal.com/reference/list-reports>.*
