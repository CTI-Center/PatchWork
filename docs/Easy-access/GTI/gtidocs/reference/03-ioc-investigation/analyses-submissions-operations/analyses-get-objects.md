---
title: "Get objects related to an analysis"
source: https://gtidocs.virustotal.com/reference/analyses-get-objects
slug: analyses-get-objects
section: reference
group: "IoC Investigation"
updatedAt: 2026-05-27T07:37:16.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Analyses, Submissions & Operations](../analyses-submissions-operations.md) › Get objects related to an analysis

---

# get-objects-related-to-an-analysis

As mentioned in the [Relationships](../../01-api-introduction/api-responses/introduction-relationships.md) section, those related objects can be retrieved by sending `GET` requests to the relationship URL.

Available relationships are described in the [generic analysis](../../17-api-objects/analyses-object.md) and [URL analysis](../../17-api-objects/url-analysis-object.md#relationships) objects and documentation.

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
    "/analyses/{id}/{relationship}": {
      "get": {
        "tags": [
          "Analyses, Submissions & Operations"
        ],
        "description": "",
        "operationId": "analyses-get-objects",
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
              "default": "10",
              "format": "int32"
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
        "summary": "Get objects related to an analysis"
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

← [Get object descriptors related to an analysis](analyses-get-descriptors.md) · [up](../README.md) · [Get a submission object](get-submission.md) →

*Archived from <https://gtidocs.virustotal.com/reference/analyses-get-objects>.*
