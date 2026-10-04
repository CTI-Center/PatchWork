---
title: "Delete subscription from a report"
source: https://gtidocs.virustotal.com/reference/delete-report-subscription-preferences
slug: delete-report-subscription-preferences
section: reference
group: "Reports & Analysis"
updatedAt: 2025-09-25T00:36:51.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Reports & Analysis](../README.md) › [Reports](../reports.md) › Delete subscription from a report

---

# delete-subscription-from-a-report

> 🚧 Special privileges required
>
> Reports & Analysis are only available to users with the Google Threat Intelligence (Google TI) Enterprise or Enterprise Plus licenses.

Use this endpoint to unfollow a certain [Report](../../17-api-objects/report-object.md), stopping IoC Stream and email notifications for new IoCs added to it.

## examples

Unfollow the Report with report--25-10029825 identifier.

```python
import requests

object_id = "report--25-10029825"
url = f"https://www.virustotal.com/api/v3/collections/{object_id}/subscription_preferences"
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
  "tags": [
    {
      "name": "Reports",
      "description": "Reports & Analysis endpoints"
    }
  ],
  "paths": {
    "/collections/{id}/subscription_preferences": {
      "delete": {
        "tags": [
          "Reports"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "delete-report-subscription-preferences",
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
        "summary": "Delete subscription from a report"
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

← [Check subscription preferences from a report](get-report-subscription-preferences.md) · [up](../README.md) · [Private Files](../../06-private-scanning/private-files.md) →

*Archived from <https://gtidocs.virustotal.com/reference/delete-report-subscription-preferences>.*
