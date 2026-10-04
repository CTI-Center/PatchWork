---
title: "Get objects related to a private URL"
source: https://gtidocs.virustotal.com/reference/private-get-objects-related-to-a-url
slug: private-get-objects-related-to-a-url
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:37:18.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private URLs](../private-urls.md) › Get objects related to a private URL

---

# get-objects-related-to-a-private-url

> 📘
>
> See [URL identifiers](../private-urls.md#url-identifiers) from more information about how to generate a valid URL identifier for a URL.

URL objects have number of relationships to other URLs and objects. As mentioned in the [Relationships](../../01-api-introduction/api-responses/introduction-relationships.md) section, those related objects can be retrieved by sending `GET` requests to the relationship URL.

Some relationships are accessible only to users who have access to VirusTotal Enterprise package.

The relationships supported by URL objects are documented in the [URL](../../17-api-objects/private-urls-object.md) API object page.

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
      "name": "Private URLs"
    }
  ],
  "paths": {
    "/urls/{id}/{relationship}": {
      "get": {
        "tags": [
          "Private URLs"
        ],
        "summary": "Get objects related to a private URL",
        "description": "",
        "operationId": "private-get-objects-related-to-a-url",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "URL identifier",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "relationship",
            "in": "path",
            "description": "Relationship name (see [table](https://gtidocs.readme.io/reference/private-urls-object#relationships))",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "x-apikey",
            "in": "header",
            "description": "Your API key",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Maximum number of related objects to retrieve",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 10,
              "maximum": 40,
              "minimum": 0
            }
          },
          {
            "name": "cursor",
            "in": "query",
            "description": "Continuation cursor",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
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
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          }
        },
        "deprecated": false,
        "security": []
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

← [Get a URL analysis report](get-a-private-url-analysis-report.md) · [up](../README.md) · [Get object descriptors related to a private URL](private-get-object-descriptors-related-to-a-url.md) →

*Archived from <https://gtidocs.virustotal.com/reference/private-get-objects-related-to-a-url>.*
