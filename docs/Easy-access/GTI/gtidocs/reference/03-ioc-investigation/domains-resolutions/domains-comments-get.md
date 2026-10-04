---
title: "Get comments on a domain"
source: https://gtidocs.virustotal.com/reference/domains-comments-get
slug: domains-comments-get
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T02:03:40.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Domains & Resolutions](../domains-resolutions.md) › Get comments on a domain

---

# get-comments-on-a-domain

Returns a list of [Comment](../../17-api-objects/comment-object.md) objects.

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
    "/domains/{domain}/comments": {
      "get": {
        "tags": [
          "Domains & Resolutions"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "domains-comments-get",
        "parameters": [
          {
            "description": "Domain name",
            "in": "path",
            "name": "domain",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Maximum number of comments to retrieve",
            "in": "query",
            "name": "limit",
            "schema": {
              "default": 10,
              "format": "int32",
              "type": "integer",
              "maximum": 40,
              "minimum": 0
            }
          },
          {
            "description": "Continuation cursor",
            "in": "query",
            "name": "cursor",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Your API key",
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
        "summary": "Get comments on a domain"
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

← [Get a domain report](domain-info.md) · [up](../README.md) · [Request a domain (re)scan](domains-rescan.md) →

*Archived from <https://gtidocs.virustotal.com/reference/domains-comments-get>.*
