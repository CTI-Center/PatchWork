---
title: "Create a new Livehunt ruleset"
source: https://gtidocs.virustotal.com/reference/create-hunting-ruleset
slug: create-hunting-ruleset
section: reference
group: "YARA Hunting"
updatedAt: 2025-09-25T00:36:20.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [YARA Hunting](../README.md) › [Livehunt](../livehunt.md) › Create a new Livehunt ruleset

---

# create-a-new-livehunt-ruleset

This endpoint creates a new Google Threat Intelligence Hunting Livehunt ruleset. The request's body must have the following structure:

```json Example request
{
  "data": {
    "type": "hunting_ruleset",
    "attributes": {
      "name": "foobar",
      "enabled": true,
      "limit": 100,
      "rules": "rule foobar { strings: $ = \"foobar\" condition: all of them }",
      "notification_emails": ["wcoyte@acme.com", "rrunner@acme.com"],
      "match_object_type": "file"
    }
  }
}
```

Use the `match_object_type` to specify the expected entity kind to match with this ruleset. Allowed values are `file`, `url`, `domain` and `ip`.

The `name` and `rules` attributes are required, the remaining ones are optional.

```json Example response
{
  "type": "hunting_ruleset",
  "id": "{id}",
  "links": {
    "self": "https://www.virustotal.com/api/v3/intelligence/hunting_ruleset/{id}"
  },
  "data": {
    "attributes": {
      "name": "foobar",
      "enabled": true,
      "limit": 100,
      "creation_date": 1521016318,
      "modification_date": 1521016318,
      "number_of_rules": 1,
      "rules": "rule foobar { strings: $ = \"foobar\" condition: all of them }",
      "notification_emails": ["notifications@acme.com"],
      "match_object_type": "file"
    }
  }
}
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
    "/intelligence/hunting_rulesets": {
      "post": {
        "tags": [
          "Livehunt"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "create-hunting-ruleset",
        "parameters": [
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
                    "default": "{     \"type\": \"hunting_ruleset\",     \"attributes\": {       \"name\": \"Test ruleset\",       \"enabled\": true,       \"limit\": 100,       \"rules\": \"rule foobar { strings: $ = \\\"foobar\\\" condition: all of them }\",       \"notification_emails\": [],       \"match_object_type\": \"file\"     }   }",
                    "description": "A Malware Hunting ruleset",
                    "format": "json",
                    "type": "string"
                  }
                },
                "required": [
                  "data"
                ],
                "type": "object"
              }
            }
          }
        },
        "security": [],
        "summary": "Create a new Livehunt ruleset"
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

← [Get Livehunt rulesets](list-hunting-rulesets.md) · [up](../README.md) · [Delete a Livehunt ruleset](delete-hunting-ruleset.md) →

*Archived from <https://gtidocs.virustotal.com/reference/create-hunting-ruleset>.*
