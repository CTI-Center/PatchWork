---
title: "Subscribe to a report"
source: https://gtidocs.virustotal.com/reference/create-report-subscription-preferences
slug: create-report-subscription-preferences
section: reference
group: "Reports & Analysis"
updatedAt: 2025-09-25T00:36:49.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Reports & Analysis](../README.md) › [Reports](../reports.md) › Subscribe to a report

---

# subscribe-to-a-report

> 🚧 Special privileges required
>
> Reports & Analysis are only available to users with the Google Threat Intelligence (Google TI) Enterprise or Enterprise Plus licenses.

Use this endpoint to subscribe to a certain [Report](../../17-api-objects/report-object.md) and receive IoC Stream (and email) notifications when new IoCs are added to it. This endpoint can be used to update the subscription preferences as well.

It requires a subscription descriptor as follows:

```json
{
    "data":
    {
        "type": "subscription_preferences",
        "attributes":
        {
            "notification_emails": "<_list of strings_> list of email addresses where notifications are sent. An empty list means that email notifications are not enabled, and only IoC Stream notifications are generated",
            "daily_email": "<_boolean_> whether email notifications are sent by IoC or as a daily digest"
        }
    }
}
```

## examples

Subscribe to the Report with report--25-10029825 identifier, to get only IoC Stream notifications.

```python
import requests

object_id = "report--25-10029825"
url = f"https://www.virustotal.com/api/v3/collections/{object_id}/subscription_preferences"
payload = {
    "data": {
        "attributes": {
            "notification_emails": [],
            "daily_email": False
        },
        "type": "subscription_preferences"
    }
}
headers = {
    "accept": "application/json","x-apikey": <api-key>, "content-type": "application/json"
}
response = requests.post(url, json=payload,headers=headers)
```

Update your subscription to the Report with report--25-10029825 identifier to also receive daily digest email notifications (you and one of your colleagues).

```python
import requests

object_id = "report--25-10029825"
email_address_1 = "your_email_address"
email_address_2 = "your_colleague_email_address"
url = f"https://www.virustotal.com/api/v3/collections/{object_id}/subscription_preferences"
payload = {
    "data": {
        "attributes": {
            "notification_emails": [email_address_1,email_address_2],
            "daily_email": True
        },
        "type": "subscription_preferences"
    }
}
headers = {
    "accept": "application/json","x-apikey": <api-key>, "content-type": "application/json"
}
response = requests.post(url, json=payload,headers=headers)
```

Subscribe to the Report with report--25-10029825 identifier, to get IoC Stream notifications and email notifications every time a new IoC is added to it.

```python
import requests

object_id = "report--25-10029825"
email_address = "your_email_address"
url = f"https://www.virustotal.com/api/v3/collections/{object_id}/subscription_preferences"
payload = {
    "data": {
        "attributes": {
            "notification_emails": [email_address],
            "daily_email": False
        },
        "type": "subscription_preferences"
    }
}
headers = {
    "accept": "application/json","x-apikey": <api-key>, "content-type": "application/json"
}
response = requests.post(url, json=payload,headers=headers)
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
      "post": {
        "tags": [
          "Reports"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "create-report-subscription-preferences",
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
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "properties": {
                  "data": {
                    "description": "Subscription preferences",
                    "format": "json",
                    "type": "string"
                  }
                },
                "required": [
                  "data"
                ],
                "type": "object"
              }
            }
          }
        },
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
        "summary": "Subscribe to a report"
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

← [Download a Report](download-report.md) · [up](../README.md) · [Check subscription preferences from a report](get-report-subscription-preferences.md) →

*Archived from <https://gtidocs.virustotal.com/reference/create-report-subscription-preferences>.*
