---
title: "Get IoC Collections associated with a Hunting ruleset"
source: https://gtidocs.virustotal.com/reference/get-related-ioc-collections
slug: get-related-ioc-collections
section: reference
group: "YARA Hunting"
updatedAt: 2025-09-25T00:36:24.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [Livehunt](../livehunt.md) › Get IoC Collections associated with a Hunting ruleset

---

# get-ioc-collections-associated-with-a-hunting-ruleset

Use this endpoint to list descriptors of [IoC Collections](../../17-api-objects/ioc-collection-object.md) associated with a certain Hunting ruleset.

These associations can be [added](add-ioc-collections-relationship.md) and also [deleted](delete-ioc-collections-relationship.md) by objects' **owners** and **editors**.

## examples

Get descriptors of all IoC Collections that are associated with the Hunting ruleset with 20899097850 identifier.

```python
import requests

id = "20899097850"
url = f"https://www.virustotal.com/api/v3/intelligence/hunting_rulesets/{id}/relationships/associations"
headers = {"accept": "application/json","x-apikey": <api-key>}
response = requests.get(url, headers=headers)
```

Get descriptors of 3 IoC Collections that are associated with the Hunting ruleset with 20899097850 identifier.

```python
import requests

id = "20899097850"
url = f"https://www.virustotal.com/api/v3/intelligence/hunting_rulesets/{id}/relationships/associations"
headers = {"accept": "application/json","x-apikey": <api-key>}
response = requests.get(url, headers=headers)
```

# openapi-definition

```json
{
  "info": {
    "title": "YARA Hunting",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Livehunt"
    }
  ],
  "paths": {
    "/intelligence/hunting_rulesets/{id}/relationships/associations": {
      "get": {
        "tags": [
          "Livehunt"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-related-ioc-collections",
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
            "description": "Ruleset identifier",
            "in": "path",
            "name": "id",
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
        "summary": "Get IoC Collections associated with a Hunting ruleset"
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

← [Delete IoC Collections association from Hunting ruleset](delete-ioc-collections-relationship.md) · [up](../README.md) · [Add IoC Collectios association to a Hunting ruleset](add-ioc-collections-relationship.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-related-ioc-collections>.*
