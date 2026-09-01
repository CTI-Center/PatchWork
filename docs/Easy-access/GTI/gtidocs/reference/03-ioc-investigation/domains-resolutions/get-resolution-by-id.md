---
title: "Get a DNS resolution object"
source: https://gtidocs.virustotal.com/reference/get-resolution-by-id
slug: get-resolution-by-id
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T02:03:46.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Domains & Resolutions](../domains-resolutions.md) › Get a DNS resolution object

---

# get-a-dns-resolution-object

This endpoint retrieves a [Resolution](../../17-api-objects/resolution-object.md) object by its ID. A resolution object ID is made by appending the IP and the domain it resolves to together.

# openapi-definition

```json
{
  "info": {
    "title": "IoC Investigation",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Domains & Resolutions"
    }
  ],
  "paths": {
    "/resolutions/{id}": {
      "get": {
        "tags": [
          "Domains & Resolutions"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-resolution-by-id",
        "parameters": [
          {
            "description": "Resolution object ID.",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Your API key.",
            "in": "header",
            "name": "x-apikey",
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
        "summary": "Get a DNS resolution object"
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

← [Get objects related to a domain](domains-relationships.md) · [up](../README.md) · [Files](../files.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-resolution-by-id>.*
