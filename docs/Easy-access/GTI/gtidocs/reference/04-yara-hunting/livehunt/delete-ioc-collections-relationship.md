---
title: "Delete IoC Collections association from Hunting ruleset"
source: https://gtidocs.virustotal.com/reference/delete-ioc-collections-relationship
slug: delete-ioc-collections-relationship
section: reference
group: "YARA Hunting"
updatedAt: 2025-09-25T00:36:23.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [Livehunt](../livehunt.md) › Delete IoC Collections association from Hunting ruleset

---

# delete-ioc-collections-association-from-hunting-ruleset

Use this endpoint to delete existing associations between [IoC Collections](../../17-api-objects/ioc-collection-object.md) and a certain Hunting ruleset.\
This endpoint requires the user to be the **owner** or an **editor** of involved objects, and IoC Collections' descriptors as follows:

```json
{
	"data": [
		{
            "id": "<_string_>IoC Collection identifier",
            "type": "collection"
        }
	]
}
```

To get the IoC Collections identifiers, you can first [list](get-related-ioc-collections.md) the IoC Collections associated with the Hunting ruleset of your interest.

## examples

Delete associations between 20899097850 Hunting ruleset and ab622fb5f4e6382109fe89ed466aafbaef1b79c31cb2c7e1d1f59ffde772715f and 27b2351c8da7419a80cbeb108ac3ac91406af5e33c7158df4e2f2be54809ef64 IoC Collections.

```python
import requests

payload = {
    "data":
    [
		{
            "id": "ab622fb5f4e6382109fe89ed466aafbaef1b79c31cb2c7e1d1f59ffde772715f",
            "type": "collection"
        },
		{
            "id": "27b2351c8da7419a80cbeb108ac3ac91406af5e33c7158df4e2f2be54809ef64",
            "type": "collection"
        }
	]
}
id = "20899097850"
url = f"https://www.virustotal.com/api/v3/intelligence/hunting_rulesets/{id}/relationships/associations"
headers = {
    "accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"
}
response = requests.delete(url, json=payload, headers=headers)
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
      "delete": {
        "tags": [
          "Livehunt"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "delete-ioc-collections-relationship",
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
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "properties": {
                  "data": {
                    "description": "A list of IoC Collection objects descriptors",
                    "format": "json",
                    "type": "string"
                  }
                },
                "type": "object"
              }
            }
          }
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": ""
                  }
                }
              }
            },
            "description": "200"
          }
        },
        "security": [],
        "summary": "Delete IoC Collections association from Hunting ruleset"
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

← [Update a Livehunt ruleset](modify-hunting-ruleset.md) · [up](../README.md) · [Get IoC Collections associated with a Hunting ruleset](get-related-ioc-collections.md) →

*Archived from <https://gtidocs.virustotal.com/reference/delete-ioc-collections-relationship>.*
