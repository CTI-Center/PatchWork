---
title: "Get object descriptors related to a Saved Search"
source: https://gtidocs.virustotal.com/reference/get-saved-searches-related-descriptors
slug: get-saved-searches-related-descriptors
section: reference
group: "IoC Investigation"
updatedAt: 2026-02-05T12:43:34.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Saved Searches](../saved-searches.md) › Get object descriptors related to a Saved Search

---

# get-object-descriptors-related-to-a-saved-search

This endpoint is the same as [/saved\_searches/\{id}/\{relationship}](get-saved-searches-relationships.md)  except it returns just the related object's descriptor instead of returning all attributes.

Available relationships are described in the Saved Search object [Relationships](../../17-api-objects/saved-search-object.md#relationships)  section.

# openapi-definition

```json
{
  "info": {
    "title": "IoC Investigation",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "paths": {
    "/saved_searches/{id}/relationship/{relationship}": {
      "get": {
        "description": "",
        "operationId": "get_saved_searches{id}relationship{relationship}",
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
            "in": "path",
            "name": "relationship",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Saved search available relationships are listed [_here_](https://gtidocs.readme.io/reference/saved-search-object#relationships)"
          },
          {
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Your API Key."
          },
          {
            "in": "query",
            "name": "limit",
            "schema": {
              "type": "string",
              "default": "10"
            },
            "description": "Maximum number of related objects to retrieve. The maximum value is 40."
          },
          {
            "in": "query",
            "name": "cursor",
            "schema": {
              "type": "string"
            },
            "description": "Continuation cursor."
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

← [Revoke access to a Saved Search](revoke-saved-searches-access.md) · [up](../README.md) · [Get objects related to a Saved Search](get-saved-searches-relationships.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-saved-searches-related-descriptors>.*
