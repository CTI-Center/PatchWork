---
title: "Get SAML configuration details of a group."
source: https://gtidocs.virustotal.com/reference/groups-get-samlconfig
slug: groups-get-samlconfig
section: reference
group: "Users and group management"
updatedAt: 2025-09-25T01:37:42.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Users and group management](../README.md) › [Group Management](../group-management.md) › Get SAML configuration details of a group.

---

# get-saml-configuration-details-of-a-group.

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
      "name": "Group Management"
    }
  ],
  "paths": {
    "/groups/{id}/saml_config": {
      "get": {
        "tags": [
          "Group Management"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "groups-get-samlconfig",
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
            "description": "Group ID",
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
                    "value": ""
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
        "security": [],
        "summary": "Get SAML configuration details of a group."
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

← [Get objects related to a group](groups-relationships.md) · [up](../README.md) · [Update SAML configuration of a group.](groups-patch-samlconfig.md) →

*Archived from <https://gtidocs.virustotal.com/reference/groups-get-samlconfig>.*
