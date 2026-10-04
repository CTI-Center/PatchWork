---
title: "Request a URL rescan (re-analyse)"
source: https://gtidocs.virustotal.com/reference/urls-analyse
slug: urls-analyse
section: reference
group: "IoC Investigation"
updatedAt: 2026-02-05T12:43:34.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [URLs](../urls.md) › Request a URL rescan (re-analyse)

---

# request-a-url-rescan-(re-analyse)

> 📘 See [URL identifiers](../urls.md#url-identifiers) from more information about how to generate a valid URL identifier for a URL.

Returns a [Analysis](../../17-api-objects/analyses-object.md) object descriptor which can be used in the [GET/analyses/\{id}](../analyses-submissions-operations/analysis.md) API endpoint to get further information about the analysis status.

```json Example response
{
    "data": {
        "id": "u-a354494a73382ea0b4bc47f4c9e8d6c578027cd4598196dc88f05a22b5817293-1604933101",
        "type": "analysis"
    }
}
```

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
      "name": "URLs"
    }
  ],
  "paths": {
    "/urls/{id}/analyse": {
      "post": {
        "tags": [
          "URLs"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "urls-analyse",
        "parameters": [
          {
            "description": "URL identifier",
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
        "summary": "Request a URL rescan (re-analyse)"
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

← [Get a URL report](url-info.md) · [up](../README.md) · [Get comments on a URL](urls-comments-get.md) →

*Archived from <https://gtidocs.virustotal.com/reference/urls-analyse>.*
