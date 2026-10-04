---
title: "Get Service Accounts of a group"
source: https://gtidocs.virustotal.com/reference/get-service-accounts-of-a-group
slug: get-service-accounts-of-a-group
section: reference
group: "Users and group management"
updatedAt: 2025-09-25T02:07:28.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Users and group management](../README.md) › [Service Account Management](../service-account-management.md) › Get Service Accounts of a group

---

# get-service-accounts-of-a-group

Get all the Service Accounts belonging to your Google Threat Intelligence group.

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
    "/groups/{id}/relationships/service_accounts": {
      "get": {
        "tags": [
          "Service Account Management"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-service-accounts-of-a-group",
        "parameters": [
          {
            "description": "Group ID",
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
        "summary": "Get Service Accounts of a group"
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

← [Service Account Management](../service-account-management.md) · [up](../README.md) · [Create a new Service Account](create-a-new-service-account.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-service-accounts-of-a-group>.*
