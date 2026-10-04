---
title: "Get Livehunt rulesets"
source: https://gtidocs.virustotal.com/reference/list-hunting-rulesets
slug: list-hunting-rulesets
section: reference
group: "YARA Hunting"
updatedAt: 2025-09-25T00:36:19.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [Livehunt](../livehunt.md) › Get Livehunt rulesets

---

# get-livehunt-rulesets

This endpoint returns the Google Threat Intelligence Hunting Livehunt rulesets viewable by the user making the request. A ruleset is viewable by a user either if it was created by the user or if it was shared with him by someone else. This endpoint is equivalent to `GET /users/{user}/hunting_rulesets`, where `{user}` is the username of the user owning the API key. In fact, if you look carefully at the example response below you'll notice that the `self` and `next` links do not point to `/intelligence/hunting_rulesets` but to `/users/{user}/hunting_rulesets`

```json Example response
{
  "data": [
    {
      "type": "hunting_ruleset",
      "id": "{id}",
      "links": {
      	"self": "https://www.virustotal.com/api/v3/intelligence/hunting_rulesets/{id}"
      },
      "attributes": {
        "creation_date": 1523635880,
        "enabled": true,
        "limit": 1000,
        "modification_date": 1525263069,
        "name": "foo",
        "notification_emails": [],
        "rules": "rule foo {condition: false}"
      }
    },
    { .. ruleset 2 .. },
    { .. ruleset 3 .. },
    { .. ruleset 4 .. },
  ],
  "meta": {
    "cursor": "Cu0FCsACCpIC9xuRl9v..."
  },
  "links": {
    "self": "https://www.virustotal.com/api/v3/users/{user}/hunting_rulesets",
    "next": "https://www.virustotal.com/api/v3/users/{user}/hunting_rulesets?cursor=Cu0FCsACCpIC9xuRl9v..."
  }
}
```

The `filter` parameter allows to filter the rulesets according to the values of certain attributes. For example you can get only the enabled rulesets with `enabled:true`. With `name:foo` and `rules:foo` you can search for rulesets having the word "foo" in their names or in the YARA rules respectively. Notice however that this only works with full words (words delimited by non-alphanumeric characters), if the ruleset's name is "foobar" it won't appear if you filter with `name:foo`. You can also filter the rulesets with the same tag, by using for example `filter=tag:auto`.

You can combine multiple filters separating them with spaces, for example: `filter=enabled:true name:foo`.

The `order` parameters control the order in which rulesets are returned, accepted orders are: `name`, `creation_date` and `modification_date`. You can prepend `+` and `-` suffixes to specify ascending and descending orders (examples: `name-`, `creation_date+`, ). If not suffix is specified the order is ascending by default.

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
    "/intelligence/hunting_rulesets": {
      "get": {
        "tags": [
          "Livehunt"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "list-hunting-rulesets",
        "parameters": [
          {
            "description": "Maximum number of rulesets to retrieve",
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
            "description": "Return the rulesets matching the given criteria only",
            "in": "query",
            "name": "filter",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Sort order",
            "in": "query",
            "name": "order",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Continuation cursor",
            "in": "query",
            "name": "cursor",
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
        "summary": "Get Livehunt rulesets"
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

← [Remove all Livehunt rulesets](delete-all-hunting-rulesets.md) · [up](../README.md) · [Create a new Livehunt ruleset](create-hunting-ruleset.md) →

*Archived from <https://gtidocs.virustotal.com/reference/list-hunting-rulesets>.*
