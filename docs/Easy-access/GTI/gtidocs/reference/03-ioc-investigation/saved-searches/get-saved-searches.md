---
title: "Get a Saved Search"
source: https://gtidocs.virustotal.com/reference/get-saved-searches
slug: get-saved-searches
section: reference
group: "IoC Investigation"
updatedAt: 2025-12-09T13:00:54.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Saved Searches](../saved-searches.md) › Get a Saved Search

---

# get-a-saved-search

This endpoint returns a [Saved Search](../../17-api-objects/saved-search-object.md) object.

# examples

Get only the name, description and tags of the saved search 0a49acd622a44982b1986984ba31c15b.

```python
import requests

object_id = "0a49acd622a44982b1986984ba31c15b"
attributes = "name,description,tags"

url = f"https://www.virustotal.com/api/v3/saved_searches/{object_id}?attributes={attributes}"

headers = {"accept": "application/json","x-apikey": <api-key>}

response = requests.get(url, headers=headers)
```

Retrieve the saved search with ID 0a49acd622a44982b1986984ba31c15b, including its owner and all editors.

```python
import requests

object_id = "0a49acd622a44982b1986984ba31c15b"
relationships = "owner,editors"

url = f"https://www.virustotal.com/api/v3/saved_searches/{object_id}?relationships={relationships}"

headers = {"accept": "application/json","x-apikey": <api-key>}

response = requests.get(url, headers=headers)
```

# openapi-definition

```json
{
  "info": {
    "title": "IoC Investigation",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "paths": {
    "/saved_searches/{id}": {
      "get": {
        "description": "",
        "operationId": "get_saved_searches{saved_search_id}",
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
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
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          }
        },
        "parameters": [
          {
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            },
            "description": "Your API Key.",
            "required": true
          },
          {
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Saved Search's ID."
          },
          {
            "in": "query",
            "name": "attributes",
            "schema": {
              "type": "string"
            },
            "description": "A comma-separated list of the [_saved search attributes_](https://gtidocs.readme.io/reference/saved-search-object#object-attributes) to be returned. (All attributes are returned by default.)"
          },
          {
            "in": "query",
            "name": "relationships",
            "schema": {
              "type": "string"
            },
            "description": "Provides additional information about the saved search as [_relationships_](https://gtidocs.readme.io/reference/saved-search-object#relationships)"
          }
        ]
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

← [List Saved Searches](list-saved-searches.md) · [up](../README.md) · [Create a Saved Search](create-saved-searches.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-saved-searches>.*
