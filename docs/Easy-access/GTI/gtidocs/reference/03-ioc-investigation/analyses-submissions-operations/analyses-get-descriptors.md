---
title: "Get object descriptors related to an analysis"
source: https://gtidocs.virustotal.com/reference/analyses-get-descriptors
slug: analyses-get-descriptors
section: reference
group: "IoC Investigation"
updatedAt: 2026-05-27T07:33:31.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Analyses, Submissions & Operations](../analyses-submissions-operations.md) › Get object descriptors related to an analysis

---

# get-object-descriptors-related-to-an-analysis

This endpoint is the same as [/analyses/\{id}/\{relationship}](analyses-get-objects.md) except it returns just the related object's descriptors (ID and context attributes, if any) instead of returning all attributes.

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
      "name": "Analyses, Submissions & Operations"
    }
  ],
  "paths": {
    "/analyses/{id}/relationships/{relationship}": {
      "get": {
        "tags": [
          "Analyses, Submissions & Operations"
        ],
        "description": "",
        "operationId": "analyses-get-descriptors",
        "parameters": [
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
            "description": "Your API key",
            "in": "header",
            "name": "x-apikey",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Relationship name (see [generic table](https://gtidocs.readme.io/reference/analyses-object#relationships) and [URLs table](https://gtidocs.readme.io/reference/url-analysis-object#relationships))",
            "in": "path",
            "name": "relationship",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "limit",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": "10"
            },
            "description": "The maximum number of items per page. Max value 40."
          },
          {
            "in": "query",
            "name": "cursor",
            "schema": {
              "type": "string"
            },
            "description": "Pagination cursor returned by the previous request."
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
        "summary": "Get object descriptors related to an analysis"
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

← [Get a URL / file analysis](analysis.md) · [up](../README.md) · [Get objects related to an analysis](analyses-get-objects.md) →

*Archived from <https://gtidocs.virustotal.com/reference/analyses-get-descriptors>.*
