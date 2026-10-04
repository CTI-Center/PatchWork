---
title: "Update a report"
source: https://gtidocs.virustotal.com/reference/update-report
slug: update-report
section: reference
group: "Reports & Analysis"
updatedAt: 2026-04-10T10:34:08.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Reports & Analysis](../README.md) › [Reports](../reports.md) › Update a report

---

# update-a-report

Use this endpoint to update attributes of a [Report](../../17-api-objects/report-object.md). It supports the same JSON **attributes** defined in the [creation endpoint](create-report.md).

> ❗️
>
> This endpoint is currently in **Private Preview**.

Note that you don't need to include `collection_type` in the request body since this attribute is automatically inferred.

> 🚧
>
> This endpoint supports **partial updates**: only the attributes provided in the request body will be modified. However, **list-based attributes follow a "full replace" logic**: if a list is included in the payload, its current contents will be entirely overwritten by the new data. To add, remove or change items from a list, **you must include the entire set of elements** in your request. We recommend [fetching](get-report.md) the current object first to ensure existing items are preserved before submitting your update.

## examples

Set the description to "Work in progress" for Report report--f64d8bb1acdd4fb498082b9c48e92c67 and overwrite its tags to "WIP" and "P0".  Additionally, assign Ana as author.

```python
import requests

object_id = "report--f64d8bb1acdd4fb498082b9c48e92c67"
url = f"https://www.virustotal.com/api/v3/collections/{object_id}"
payload = {
  "data": {
    "type": "collection",
    "attributes": {
      "description": "Work in progress",
      "tags":["WIP", "P0"],
      "author": "Ana"
    }
  }
}
headers = {"accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"}
response = requests.patch(url, json=payload, headers=headers)
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
      "patch": {
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
            "description": "Report's ID"
          },
          {
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            },
            "description": "Your API key.",
            "required": true
          }
        ],
        "operationId": "patch_collections-id",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "data": {
                    "type": "object",
                    "properties": {},
                    "description": "Report object"
                  }
                },
                "required": [
                  "data"
                ]
              }
            }
          }
        }
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

← [Delete a report](delete-report.md) · [up](../README.md) · [Add new associations, IoCs or TTPs to a report](add-element-to-report.md) →

*Archived from <https://gtidocs.virustotal.com/reference/update-report>.*
