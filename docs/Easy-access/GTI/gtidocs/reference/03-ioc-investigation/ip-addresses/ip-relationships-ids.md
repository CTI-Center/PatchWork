---
title: "Get object descriptors related to an IP address"
source: https://gtidocs.virustotal.com/reference/ip-relationships-ids
slug: ip-relationships-ids
section: reference
group: "IoC Investigation"
updatedAt: 2026-02-05T12:43:34.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [IP addresses](../ip-addresses.md) › Get object descriptors related to an IP address

---

# get-object-descriptors-related-to-an-ip-address

This endpoint is the same as [/ip\_addresses/\{ip}/\{relationship}](ip-relationships.md) except it returns just the related object's IDs (and context attributes, if any) instead of returning all attributes.

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
    "/ip_addresses/{ip}/relationships/{relationship}": {
      "get": {
        "tags": [
          "IP addresses"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "ip-relationships-ids",
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
            "description": "Maximum number of related objects to retrieve",
            "in": "query",
            "name": "limit",
            "schema": {
              "default": "10",
              "type": "string"
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
        "summary": "Get object descriptors related to an IP address"
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

← [Add a comment to an IP address](ip-comments-post.md) · [up](../README.md) · [Get votes on an IP address](ip-votes.md) →

*Archived from <https://gtidocs.virustotal.com/reference/ip-relationships-ids>.*
