---
title: "Check subscription preferences from a report"
source: https://gtidocs.virustotal.com/reference/get-report-subscription-preferences
slug: get-report-subscription-preferences
section: reference
group: "Reports & Analysis"
updatedAt: 2025-09-25T00:36:50.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Reports & Analysis](../README.md) › [Reports](../reports.md) › Check subscription preferences from a report

---

# check-subscription-preferences-from-a-report

> 🚧 Special privileges required
>
> Reports & Analysis are only available to users with the Google Threat Intelligence (Google TI) Enterprise or Enterprise Plus licenses.

Use this endpoint to check subscription preferences on a certain [Report](../../17-api-objects/report-object.md):

```json
{
    "links":
    {
        "self": "<_string_> subscription URL"
    },
    "meta":
    {
        "count": "<_boolean_> 0 if subscription is not active, 1 if subscription is active"
    },
    "data":
    {
        "id": "<_string_> subscription identifier",
        "type": "subscription_preferences",
        "attributes":
        {
            "last_modification_date": "<_integer_> subscription last modification date (UTC timestamp)",
            "creation_date": "<_integer_> subscription creation date (UTC timestamp)",
            "notification_emails": "<_list of strings_> list of email addresses where notifications are sent. An empty list means that email notifications are not enabled, and only IoC Stream notifications are generated",
            "daily_email": "<_boolean_> whether email notifications are sent by IoC or as a daily digest"
        }
    }
}
```

## examples

Check subscription preferences for the Report with report--25-10029825 identifier.

```python
import requests

object_id = "report--25-10029825"
url = f"https://www.virustotal.com/api/v3/collections/{object_id}/subscription_preferences"
headers = {
    "accept": "application/json","x-apikey": <api-key>
}
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
    "/collections/{id}/subscription_preferences": {
      "get": {
        "tags": [
          "Reports"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-report-subscription-preferences",
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
        "summary": "Check subscription preferences from a report"
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

← [Subscribe to a report](create-report-subscription-preferences.md) · [up](../README.md) · [Delete subscription from a report](delete-report-subscription-preferences.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-report-subscription-preferences>.*
