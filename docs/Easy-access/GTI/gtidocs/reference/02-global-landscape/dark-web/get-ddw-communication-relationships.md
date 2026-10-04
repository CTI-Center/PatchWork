---
title: "Get objects related to a Dark Web Communication object"
source: https://gtidocs.virustotal.com/reference/get-ddw-communication-relationships
slug: get-ddw-communication-relationships
section: reference
group: "Global Landscape"
updatedAt: 2026-03-23T15:04:02.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Global Landscape](../README.md) › [Dark Web](../dark-web.md) › Get objects related to a Dark Web Communication object

---

# get-objects-related-to-a-dark-web-communication-object

This endpoint returns available relationships that are described in the Dark Web Communication object [Relationships](../../17-api-objects/dark-web-objects/dark-web-communication-object.md#relationships) section.

# openapi-definition

```json
{
  "info": {
    "title": "Threat Landscape",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "paths": {
    "/ddw_communications/{id}/{relationship}": {
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
            "description": "Dark Web Communication identifier."
          },
          {
            "in": "path",
            "name": "relationship",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Communications available relationships are listed _[here](https://gtidocs.readme.io/reference/dark-web-communication-object#relationships)_."
          },
          {
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            },
            "description": "Your API key.",
            "required": true
          },
          {
            "in": "query",
            "name": "limit",
            "schema": {
              "type": "string",
              "default": "10"
            },
            "description": "Maximum number of related objects to retrieve. The maximum value is 40."
          },
          {
            "in": "query",
            "name": "cursor",
            "schema": {
              "type": "string"
            },
            "description": "Continuation cursor."
          }
        ],
        "operationId": "get_ddw-communications-id-relationship"
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

← [Get a Dark Web Communication object](get-ddw-communication.md) · [up](../README.md) · [Get a Dark Web Communication Channel object](get-ddw-communication-channel.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-ddw-communication-relationships>.*
