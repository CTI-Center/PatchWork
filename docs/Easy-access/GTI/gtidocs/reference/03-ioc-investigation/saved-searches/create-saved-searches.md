---
title: "Create a Saved Search"
source: https://gtidocs.virustotal.com/reference/create-saved-searches
slug: create-saved-searches
section: reference
group: "IoC Investigation"
updatedAt: 2025-12-05T10:53:58.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Saved Searches](../saved-searches.md) › Create a Saved Search

---

# create-a-saved-search

Use this endpoint to save a search or query and you will automatically become the **owner** of the [saved search](../../17-api-objects/saved-search-object.md). This is an example request body:

```json Request body example
{
    "data": {
        "type": "saved_search",
        "attributes": {
            "name": "saved search's name",
            "description": "saved search's description",
            "search_query": "saved search's query/logic",
            "private": true,
            "tags": ["saved search's associated tags"]
        }
    }
}
```

The `private` field determines the search's accessibility:

* if set to `false` (public), the saved search is viewable by all Google Threat Intelligence users.
* if set to `true` (private), access is restricted to the owner and any specific users/groups with whom the owner has individually shared the search.

To update the `private` field check out this [endpoint](update-saved-searches.md) .

To share a saved search with certain users or the owner's entire group, check out this [endpoint](share-saved-searches.md) .

# examples

```python
import requests

url = f"https://www.virustotal.com/api/v3/saved_searches"
payload = {
    "data": {
        "type": "saved_search",
        "attributes": {
            "name": "Potential Gamaredon-related document activity",
            "description": "This Intelligence search query is designed to find files that match a specific set of characteristics, generally indicative of a particular type of malware or activity.",
            "search_query": "(type:document) and (behavior_processes:*.ru* and behavior_processes:*DavSetCookie* and behavior_processes:*http*) and (behavior_network:*.ru* or embedded_domain:*.ru* or embedded_url:*.ru*)",
            "private": True,
            "tags": ["FILE", "Gamaredon", "Behaviour"]
        }
    }
}
headers = {"accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"}
response = requests.post(url, json=payload, headers=headers)
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
    "/saved_searches": {
      "post": {
        "description": "",
        "operationId": "post_saved_searches",
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
            "required": true,
            "description": "Your AP Key."
          },
          {
            "in": "query",
            "name": "relationships",
            "schema": {
              "type": "string"
            },
            "description": "Provides additional information about the saved search as [_relationships_](https://gtidocs.readme.io/reference/saved-search-object#relationships)"
          },
          {
            "in": "query",
            "name": "attributes",
            "schema": {
              "type": "string"
            },
            "description": "A comma-separated list of the [_saved search attributes_](https://gtidocs.readme.io/reference/saved-search-object#object-attributes) to be returned. (All attributes are returned by default.)"
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "data": {
                    "type": "object",
                    "description": "Payload to post.",
                    "properties": {
                      "type": {
                        "type": "string"
                      },
                      "attributes": {
                        "type": "object",
                        "properties": {
                          "name": {
                            "type": "string",
                            "description": "Saved search's name"
                          },
                          "description": {
                            "type": "string",
                            "description": "Saved search's description"
                          },
                          "search_query": {
                            "type": "string",
                            "description": "Saved search's query/logic"
                          },
                          "private": {
                            "type": "boolean",
                            "description": "Search's accesibility"
                          },
                          "tags": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            },
                            "description": "Saved search's associated tags"
                          }
                        },
                        "required": [
                          "name",
                          "description",
                          "search_query"
                        ]
                      }
                    },
                    "required": [
                      "type",
                      "attributes"
                    ]
                  }
                },
                "required": [
                  "data"
                ]
              }
            }
          }
        }
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

← [Get a Saved Search](get-saved-searches.md) · [up](../README.md) · [Share a Saved Search](share-saved-searches.md) →

*Archived from <https://gtidocs.virustotal.com/reference/create-saved-searches>.*
