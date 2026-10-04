---
title: "Revoke access to a Saved Search"
source: https://gtidocs.virustotal.com/reference/revoke-saved-searches-access
slug: revoke-saved-searches-access
section: reference
group: "IoC Investigation"
updatedAt: 2025-12-09T11:46:53.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Saved Searches](../saved-searches.md) › Revoke access to a Saved Search

---

# revoke-access-to-a-saved-search

<br />

Use this endpoint to revoke [saved search](../../17-api-objects/saved-search-object.md)  access for a specific user or the owner's entire group.

This endpoint is **restricted** to use by the **owner** and **editors** of the saved search only.

> 🚧
>
> **Important:** This endpoint requires a request body, even when utilizing the **DELETE** method.

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

# examples

Revoke viewer privileges for all members of my group from the saved search with ID f60631d600b44a91a8b20cef8c77aeac.

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
response = requests.delete(url, json=payload, headers=headers)
```

Revoke editor privileges for ana and alex from the saved search with ID f60631d600b44a91a8b20cef8c77aeac.

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
response = requests.delete(url, json=payload, headers=headers)
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
      "delete": {
        "description": "",
        "operationId": "delete_saved_searches{id}relationship{access}",
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
                "editors",
                "viewers"
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

← [Delete a Saved Search](delete-saved-searches.md) · [up](../README.md) · [Get object descriptors related to a Saved Search](get-saved-searches-related-descriptors.md) →

*Archived from <https://gtidocs.virustotal.com/reference/revoke-saved-searches-access>.*
