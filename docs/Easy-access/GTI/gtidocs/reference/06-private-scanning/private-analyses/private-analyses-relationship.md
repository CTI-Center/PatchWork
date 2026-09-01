---
title: "Get objects related to a private analysis"
source: https://gtidocs.virustotal.com/reference/private-analyses-relationship
slug: private-analyses-relationship
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:37:14.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private Analyses](../private-analyses.md) › Get objects related to a private analysis

---

# get-objects-related-to-a-private-analysis

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

As mentioned in the [Relationships](../../01-api-introduction/api-responses/introduction-relationships.md) section, those related objects can be retrieved by sending `GET` requests to the relationship URL.

Available relationships are described in the [private analysis](../../17-api-objects/private-analyses-object.md) object documentation.

# openapi-definition

```json
{
  "info": {
    "title": "Private Scanning",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Private Analyses"
    }
  ],
  "paths": {
    "/analyses/{id}/{relationship}": {
      "get": {
        "tags": [
          "Private Analyses"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "private-analyses-relationship",
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
            "description": "Analysis identifier",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Relationship name (see [table](https://gtidocs.readme.io/reference/private-analyses-object#relationships))",
            "in": "path",
            "name": "relationship",
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
        "summary": "Get objects related to a private analysis"
      }
    }
  },
  "security": [],
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3/private"
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

← [Get object descriptors related to a private analysis](private-analyses-relationships-descriptor.md) · [up](../README.md) · [Private URLs](../private-urls.md) →

*Archived from <https://gtidocs.virustotal.com/reference/private-analyses-relationship>.*
