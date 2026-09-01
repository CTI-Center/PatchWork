---
title: "Add IoC Collectios association to a Hunting ruleset"
source: https://gtidocs.virustotal.com/reference/add-ioc-collections-relationship
slug: add-ioc-collections-relationship
section: reference
group: "YARA Hunting"
updatedAt: 2026-05-22T07:46:43.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [Livehunt](../livehunt.md) › Add IoC Collectios association to a Hunting ruleset

---

# add-ioc-collectios-association-to-a-hunting-ruleset

Use this endpoint to add associations between [IoC Collections](../../17-api-objects/ioc-collection-object.md) and a certain Hunting ruleset.

This endpoint requires the user to be the **owner** or an **editor** of involved objects, and IOC Collections' descriptors as follows:

```json
{
	"data": [
		{
            "id": "<_string_> IoC Collection identifier",
            "type": "collection"
        }
	]
}
```

To find your IoC Collections identifiers, navigate to your **Profile** from the user menu in the top-right corner of the [web interface](https://www.virustotal.com/gui/home), then go to the **COLLECTIONS** tab and open the specific collections you're interested in. You'll find the IoC Collection identifier in the URL.

## examples

Create new associations between 20899097850 Hunting ruleset and ab622fb5f4e6382109fe89ed466aafbaef1b79c31cb2c7e1d1f59ffde772715f and 27b2351c8da7419a80cbeb108ac3ac91406af5e33c7158df4e2f2be54809ef64 IoC Collections.

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
response = requests.post(url, json=payload, headers=headers)
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
      "post": {
        "tags": [
          "Livehunt"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "add-ioc-collections-relationship",
        "parameters": [
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
            "description": "Your API key",
            "in": "header",
            "name": "x-apikey",
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
        "summary": "Add IoC Collectios association to a Hunting ruleset"
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

← [Get IoC Collections associated with a Hunting ruleset](get-related-ioc-collections.md) · [up](../README.md) · [Grant Livehunt ruleset edit permissions for a user or group](edit-hunting-ruleset-relationship.md) →

*Archived from <https://gtidocs.virustotal.com/reference/add-ioc-collections-relationship>.*
