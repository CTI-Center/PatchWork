---
title: "Delete a report"
source: https://gtidocs.virustotal.com/reference/delete-report
slug: delete-report
section: reference
group: "Reports & Analysis"
updatedAt: 2026-04-07T14:24:09.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Reports & Analysis](../README.md) › [Reports](../reports.md) › Delete a report

---

# delete-a-report

As the owner, you can use this endpoint to delete a [Report](../../17-api-objects/report-object.md).

> ❗️
>
> This endpoint is currently in **Private Preview**.

## examples

Delete a Report.

```python
import requests

object_id = "report--f64d8bb1acdd4fb498082b9c48e92c67"
url = f"https://www.virustotal.com/api/v3/collections/{object_id}"
headers = {
    "accept": "application/json","x-apikey": <api-key>
}
response = requests.delete(url, headers=headers)
```

# openapi-definition

```json
{
  "info": {
    "title": "Reports & Analysis",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "paths": {
    "/collections/{id}": {
      "delete": {
        "description": "",
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
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
            "name": "id",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Report's id"
          },
          {
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Your API key."
          }
        ],
        "operationId": "delete_collections-id"
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

← [Create a new report](create-report.md) · [up](../README.md) · [Update a report](update-report.md) →

*Archived from <https://gtidocs.virustotal.com/reference/delete-report>.*
