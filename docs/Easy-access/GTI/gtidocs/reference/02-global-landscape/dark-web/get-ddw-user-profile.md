---
title: "Get a Dark Web User Profile"
source: https://gtidocs.virustotal.com/reference/get-ddw-user-profile
slug: get-ddw-user-profile
section: reference
group: "Global Landscape"
updatedAt: 2026-03-23T15:04:02.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Global Landscape](../README.md) › [Dark Web](../dark-web.md) › Get a Dark Web User Profile

---

# get-a-dark-web-user-profile

Use this endpoint to retrieve a [Dark Web User Profile](../../17-api-objects/dark-web-objects/dark-web-user-profile-object.md) object by its unique identifier.

<br />

# openapi-definition

```json
{
  "info": {
    "title": "Threat Landscape",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "paths": {
    "/ddw_user_profiles/{id}": {
      "get": {
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
            "description": "Dark Web User Profile identifier."
          },
          {
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Your API key."
          },
          {
            "in": "query",
            "name": "param",
            "schema": {
              "type": "string"
            },
            "description": "A comma-separated list of the _[user profile attributes](https://gtidocs.readme.io/reference/dark-web-user-profile-object)_ to be returned. (All attributes are returned by default.)"
          }
        ],
        "operationId": "get_ddw-user-profiles-id"
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

← [Get Previous Communication in a Channel](get-ddw-channel-previous-communications.md) · [up](../README.md) · [Get a Dark Web Service object](get-ddw-service.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-ddw-user-profile>.*
