---
title: "Get votes on a domain"
source: https://gtidocs.virustotal.com/reference/domains-votes-get
slug: domains-votes-get
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T02:03:43.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Domains & Resolutions](../domains-resolutions.md) › Get votes on a domain

---

# get-votes-on-a-domain

Returns a list of [Vote](../../17-api-objects/vote-object.md) objects.

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
    "/domains/{domain}/votes": {
      "get": {
        "tags": [
          "Domains & Resolutions"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "domains-votes-get",
        "parameters": [
          {
            "in": "path",
            "name": "domain",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Your API key",
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
        "summary": "Get votes on a domain"
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

← [Get object descriptors related to a domain](domains-relationships-ids.md) · [up](../README.md) · [Add a vote to a domain](domain-votes-post.md) →

*Archived from <https://gtidocs.virustotal.com/reference/domains-votes-get>.*
