---
title: "Create a new Service Account"
source: https://gtidocs.virustotal.com/reference/create-a-new-service-account
slug: create-a-new-service-account
section: reference
group: "Users and group management"
updatedAt: 2025-09-25T02:07:29.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Users and group management](../README.md) › [Service Account Management](../service-account-management.md) › Create a new Service Account

---

# create-a-new-service-account

Create a new Service Account inside your Google Threat Intelligence group by only providing a descriptive identifier which must be unique inside your group.

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
      "post": {
        "tags": [
          "Service Account Management"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "create-a-new-service-account",
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
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "properties": {
                  "data": {
                    "description": "List of Unique Service Account objects (only 'id' param is needed) within your group.",
                    "format": "json",
                    "type": "string"
                  }
                },
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
        "summary": "Create a new Service Account"
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

← [Get Service Accounts of a group](get-service-accounts-of-a-group.md) · [up](../README.md) · [Get a Service Account object](get-a-service-account-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/create-a-new-service-account>.*
