---
title: "Get objects related to a Dark Web Service object"
source: https://gtidocs.virustotal.com/reference/get-ddw-service-relationships
slug: get-ddw-service-relationships
section: reference
group: "Global Landscape"
updatedAt: 2026-03-23T15:04:02.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Global Landscape](../README.md) › [Dark Web](../dark-web.md) › Get objects related to a Dark Web Service object

---

# get-objects-related-to-a-dark-web-service-object

This endpoint returns available relationships that are described in the Dark Web Service object [Relationships](../../17-api-objects/dark-web-objects/dark-web-service-object.md#relationships) section.

# openapi-definition

```json
{
  "info": {
    "title": "Threat Landscape",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "paths": {
    "/ddw_services/{id}/{relationship}": {
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
            "description": "Dark Web Service identifier."
          },
          {
            "in": "path",
            "name": "relationship",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Dark Web Service available relationships are listed _[here](https://gtidocs.readme.io/reference/dark-web-service-object#relationships)_."
          },
          {
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Your API key."
          }
        ],
        "operationId": "get_ddw-services-id-relationship"
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

← [Get a Dark Web Service object](get-ddw-service.md) · [up](../README.md) · [Get Next Communication in a Thread](get-ddw-thread-next-communications.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-ddw-service-relationships>.*
