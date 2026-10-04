---
title: "Update a Saved Search"
source: https://gtidocs.virustotal.com/reference/update-saved-searches
slug: update-saved-searches
section: reference
group: "IoC Investigation"
updatedAt: 2025-12-05T10:53:32.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Saved Searches](../saved-searches.md) › Update a Saved Search

---

# update-a-saved-search

Use this endpoint to modify the attributes of an existing [saved search](../../17-api-objects/saved-search-object.md). This is an example request body:

```json Request body example
{
    "data": {
        "type": "saved_search",
        "attributes": {
            "name": "new saved search's name",
            "description": "new saved search's description",
            "search_query": "new saved search's query/logic",
            "private": false,
            "tags": ["saved search's associated tags"]
        }
    }
}
```

The `private` field determines the search's accessibility:

* if set to `false` (public), the saved search is viewable by all Google Threat Intelligence users.
* if set to `true` (private), access is restricted to the owner and any specific users/groups with whom the owner has individually shared the search.

> 🚧
>
> **Important Note on Updating Tags:** To modify the tag list using this endpoint (adding or removing a subset of tags), you must first  [_retrieve_](https://gtidocs.readme.io/reference/get-saved-search) the current full list of tags.
>
> * **To Delete All Tags:** use this endpoint with an empty list of tags (`[]`).
> * **To Add a New Tags:** [_retrieve_](https://gtidocs.readme.io/reference/get-saved-search) the current list, append the new tags, and submit the resulting list.
> * **To Remove a Subset of Tags:** [_retrieve_](https://gtidocs.readme.io/reference/get-saved-search) the current list, filter out the tags to be removed, and submit the remaining list.

This endpoint is **restricted** to use by the **owner** and **editors** of the saved search only.

To share a saved search with certain users or the owner's entire group, check out this [endpoint](share-saved-searches.md)

# examples

Change the name and the description of the saved search with ID f60631d600b44a91a8b20cef8c77aeac.

```python
import requests

object_id = "f60631d600b44a91a8b20cef8c77aeac"

url = f"https://www.virustotal.com/api/v3/saved_searches/{object_id}"

payload = {
    "data": {
        "type": "saved_search",
        "attributes": {
            "name": "This is the new name of the saved search",
            "description": "This is the new description of the saved search"
        }
    }
}
headers = {"accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"}
response = requests.patch(url, json=payload, headers=headers)
```

Share the saved search with ID f60631d600b44a91a8b20cef8c77aeac with the entire community.

```python
import requests

object_id = "f60631d600b44a91a8b20cef8c77aeac"

url = f"https://www.virustotal.com/api/v3/saved_searches/{object_id}"

payload = {
    "data": {
        "type": "saved_search",
        "attributes": {
            "private": False
        }
    }
}
headers = {"accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"}
response = requests.patch(url, json=payload, headers=headers)
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
      "patch": {
        "description": "",
        "operationId": "patch_saved_searches{id}",
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
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Saved Search's ID."
          },
          {
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            },
            "description": "Your AP Key.",
            "required": true
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
                    "description": "Payload to patch.",
                    "properties": {}
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

← [Share a Saved Search](share-saved-searches.md) · [up](../README.md) · [Delete a Saved Search](delete-saved-searches.md) →

*Archived from <https://gtidocs.virustotal.com/reference/update-saved-searches>.*
