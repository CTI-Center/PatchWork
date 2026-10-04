---
title: "Share a Saved Search"
source: https://gtidocs.virustotal.com/reference/share-saved-searches
slug: share-saved-searches
section: reference
group: "IoC Investigation"
updatedAt: 2025-12-05T14:28:05.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Saved Searches](../saved-searches.md) › Share a Saved Search

---

# share-a-saved-search

<br />

Use this endpoint to grant **viewer** or **editor** permissions to a certain [saved search](../../17-api-objects/saved-search-object.md)  for:

* individual **users**
* owner's **group**

This endpoint is **restricted** to use by the **owner** and **editors** of the saved search only.

> 🚧
>
> Note that **editor** privileges can **only be granted to members belonging to the same group as the owner** of the saved search.

This is an example request body:

```json Request body example
{
    "data": [
        {
            "id": "user id",
            "type": "user"
        },
        {
            "id": "group id",
            "type": "group"
        }
    ]
}
```

To revoke the access to a saved search check out this [endpoint](https://gtidocs.readme.io/reference/revoke-saved-search-access).

# examples

Grant view access to all members of my group for the saved search with ID f60631d600b44a91a8b20cef8c77aeac.

```python
import requests
object_id = "f60631d600b44a91a8b20cef8c77aeac"
access = "viewers"

url = f"https://www.virustotal.com/api/v3/saved_searches/{object_id}/relationship/{access}"

payload = {
    "data": [
        {
            "id": "my_group_id",
            "type": "group"
        }
    ]
}
headers = {"accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"}
response = requests.post(url, json=payload, headers=headers)
```

Grant edit access to ana and alex for the saved search with ID f60631d600b44a91a8b20cef8c77aeac.

```python
import requests
object_id = "f60631d600b44a91a8b20cef8c77aeac"
access = "editors"

url = f"https://www.virustotal.com/api/v3/saved_searches/{object_id}/relationship/{access}"

payload = {
    "data": [
        {
            "id": "ana",
            "type": "user"
        },
        {
            "id": "alex",
            "type": "user"
        }
    ]
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
    "/saved_searches/{id}/relationship/{access}": {
      "post": {
        "description": "",
        "operationId": "post_saved_searches{id}relationship{access}",
        "responses": {
          "200": {
            "description": "200"
          },
          "400": {
            "description": "400",
            "content": {}
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
            "in": "path",
            "name": "access",
            "schema": {
              "type": "string",
              "enum": [
                "viewers",
                "editors"
              ]
            },
            "required": true,
            "description": "Access level."
          },
          {
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Your API Key."
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "data": {
                    "type": "array",
                    "items": {
                      "properties": {
                        "id": {
                          "type": "string"
                        },
                        "type": {
                          "type": "string"
                        }
                      },
                      "type": "object",
                      "required": [
                        "id",
                        "type"
                      ]
                    }
                  }
                }
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

← [Create a Saved Search](create-saved-searches.md) · [up](../README.md) · [Update a Saved Search](update-saved-searches.md) →

*Archived from <https://gtidocs.virustotal.com/reference/share-saved-searches>.*
