---
title: "Get a Service Account object"
source: https://gtidocs.virustotal.com/reference/get-a-service-account-object
slug: get-a-service-account-object
section: reference
group: "Users and group management"
updatedAt: 2025-09-25T02:07:30.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Users and group management](../README.md) › [Service Account Management](../service-account-management.md) › Get a Service Account object

---

# get-a-service-account-object

Get the information about a [Service Account](../../17-api-objects/service-accounts-object.md) object.

# openapi-definition

```json
{
  "info": {
    "title": "Users and group management",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Service Account Management"
    }
  ],
  "paths": {
    "/service_accounts/{id}": {
      "get": {
        "tags": [
          "Service Account Management"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-a-service-account-object",
        "parameters": [
          {
            "description": "Format: groupId_serviceAccountId. Example: mygroup_myserviceaccount",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Your API Key.",
            "in": "header",
            "name": "x-apikey",
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
        "summary": "Get a Service Account object"
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

← [Create a new Service Account](create-a-new-service-account.md) · [up](../README.md) · [Audit Logs](../audit-logs.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-a-service-account-object>.*
