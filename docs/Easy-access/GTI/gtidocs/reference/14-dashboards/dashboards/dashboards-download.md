---
title: "Export Dashboard Data"
source: https://gtidocs.virustotal.com/reference/dashboards-download
slug: dashboards-download
section: reference
group: "Dashboards"
updatedAt: 2025-12-16T14:15:50.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Dashboards](../README.md) › [Dashboards](../dashboards.md) › Export Dashboard Data

---

# export-dashboard-data

Use this endpoint to filter and export the data behind our dashboards, which currently supports:

* [**Ransomware Data Leaks**](https://www.virustotal.com/gui/ransomware-dls) -> Use `ransomware` as the `{dashboard_type}` path parameter.

This endpoint returns the underlying data records used to populate the dashboard in several formats:

* JSON - a list of JSON objects
* CSV
* Markdown - as a table
* Plain text - as a table
* HTML - as a table
* XLSX
* PNG

# filters

Filtering in this case is done via request body as:

```json Request body example
{
  "filters": {
     "Primary Industry": "The industry of the organization identified as a victim on a Data Leak Site (DLS).",
     "Company": "The name of the organization identified as a victim on a Data Leak Site (DLS).",
     "Company Website":"The website of the organization identified as a victim on a Data Leak Site (DLS).",
     "Country":"The country of the organization identified as a victim on a Data Leak Site (DLS).",
     "Date of Collection":"The date the victim entry was indexed by our systems."
  },
  "limit": "This parameter is a numerical value that represents the maximum number of elements from the database to be retrieved. By default it returns all elements matching the defined filters."
}
```

Filters for this endpoint follow [**Looker filter expression syntax**](https://docs.cloud.google.com/looker/docs/filter-expressions). While the examples below demonstrate common use cases, you can refer to the Looker filter documentation for a comprehensive guide on [string filtering expressions](https://docs.cloud.google.com/looker/docs/filter-expressions#string).

# examples

Retrieve all DLS events from the last 30 days involving organizations in the German education sector. Export the data in JSON format.

```python
import requests

dashboard_type = "ransomware"
format = "json"
url = f"https://www.virustotal.com/api/v3/dashboards/{dashboard_type}/download/{format}"
payload = {
  "filters": {
     "Primary Industry": "education",
     "Country":"Germany",
     "Date of Collection":"30 days"
  }
}
headers = {"accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"}
response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

Retrieve all DLS events from 2021 and 2022 for German and Spanish organizations within the Energy & Utilities, and Oil & Gas sectors. Save the resulting data visualization as a PNG file in the local execution directory.

```python
import requests

dashboard_type = "ransomware"
format = "png"
url = f"https://www.virustotal.com/api/v3/dashboards/{dashboard_type}/download/{format}"
payload = {
  "filters": {
     "Primary Industry": "%energy%,%oil%",
     "Country":"Germany , Spain",
     "Date of Collection":"2021-01-01 00:00:00 to 2023-01-01 00:00:00",
  }
}
headers = {"accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"}
response = requests.post(url, json=payload, headers=headers)

with open("data_image.png", "wb") as f:
    f.write(response.content)
```

Extract the 20 most recent DLS events involving organizations whose websites end with "group.com", and print the Markdown table as a result.

```python
import requests

dashboard_type = "ransomware"
format = "md"
url = f"https://www.virustotal.com/api/v3/dashboards/{dashboard_type}/download/{format}"
payload = {
  "filters": {
     "Company Website":"%group.com"
  },
  "limit": 20
}
headers = {"accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"}
response = requests.post(url, json=payload, headers=headers)

print(response.text)
```

# openapi-definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "version": "1.0.0",
    "title": "Dashboards"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3"
    }
  ],
  "paths": {
    "/dashboards/{dashboard_type}/download/{format}": {
      "post": {
        "description": "",
        "operationId": "post_dashboards{dashboard_id}download{format}",
        "responses": {
          "200": {
            "description": "200"
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          }
        },
        "parameters": [
          {
            "in": "path",
            "name": "format",
            "schema": {
              "type": "string",
              "enum": [
                "json",
                "csv",
                "txt",
                "html",
                "md",
                "xlsx",
                "png"
              ]
            },
            "required": true
          },
          {
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Your API Key."
          },
          {
            "in": "path",
            "name": "dashboard_type",
            "schema": {
              "type": "string",
              "enum": [
                "ransomware"
              ]
            },
            "required": true
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "filters": {
                    "type": "string",
                    "format": "json",
                    "default": ""
                  },
                  "limit": {
                    "type": "integer",
                    "default": ""
                  }
                }
              },
              "examples": {}
            }
          }
        }
      }
    }
  },
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": false
  }
}
```

---

← [Dashboards](../dashboards.md) · [up](../README.md) · [Key Concepts](../../15-gti-alerts/ti-key-concepts.md) →

*Archived from <https://gtidocs.virustotal.com/reference/dashboards-download>.*
