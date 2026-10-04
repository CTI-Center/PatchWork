---
title: "Get objects related to an IP address"
source: https://gtidocs.virustotal.com/reference/ip-relationships
slug: ip-relationships
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T00:34:49.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [IP addresses](../ip-addresses.md) › Get objects related to an IP address

---

# get-objects-related-to-an-ip-address

IP addresses have number of relationships to other objects. As mentioned in the [Relationships](../../01-api-introduction/api-responses/introduction-relationships.md) section, those related objects can be retrieved by sending `GET` requests to the relationship URL.

All available relationships are documented in the [IP address](../../17-api-objects/ip-object.md) API object page.

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
      "name": "IP addresses"
    }
  ],
  "paths": {
    "/ip_addresses/{ip}/{relationship}": {
      "get": {
        "tags": [
          "IP addresses"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "ip-relationships",
        "parameters": [
          {
            "description": "IP address",
            "in": "path",
            "name": "ip",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Relationship name (see [table](https://gtidocs.readme.io/reference/ip-object#relationships))",
            "in": "path",
            "name": "relationship",
            "required": true,
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
          },
          {
            "description": "Maximum number of related objects to retrieve",
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
        "summary": "Get objects related to an IP address"
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

← [Add a vote to an IP address](ip-votes-post.md) · [up](../README.md) · [Domains & Resolutions](../domains-resolutions.md) →

*Archived from <https://gtidocs.virustotal.com/reference/ip-relationships>.*
