---
title: "Delete a Saved Search"
source: https://gtidocs.virustotal.com/reference/delete-saved-searches
slug: delete-saved-searches
section: reference
group: "IoC Investigation"
updatedAt: 2025-12-09T11:46:35.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Saved Searches](../saved-searches.md) › Delete a Saved Search

---

# delete-a-saved-search

Use this endpoint to delete a certain [saved search](../../17-api-objects/saved-search-object.md) .

This endpoint is **restricted** to use by the **owner** of the saved search only. Upon deletion, the search is permanently removed and will no longer be accessible to any users with whom it was previously shared.

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
      "delete": {
        "description": "",
        "operationId": "delete_saved_searches{id}",
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
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            },
            "description": "Your API Key.",
            "required": true
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

← [Update a Saved Search](update-saved-searches.md) · [up](../README.md) · [Revoke access to a Saved Search](revoke-saved-searches-access.md) →

*Archived from <https://gtidocs.virustotal.com/reference/delete-saved-searches>.*
