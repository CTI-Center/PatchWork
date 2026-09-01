---
title: "Search for files, URLs, domains, IPs and comments"
source: https://gtidocs.virustotal.com/reference/api-search
slug: api-search
section: reference
group: "IoC Investigation"
updatedAt: 2026-02-05T12:43:34.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Search & Metadata](../search-metadata.md) › Search for files, URLs, domains, IPs and comments

---

# search-for-files,-urls,-domains,-ips-and-comments

This endpoint searches any of the following:

* A file hash - Returns a [File](../../17-api-objects/file-object.md) object.
* A URL - Returns a [URL](../../17-api-objects/url-object.md) object.
* A domain - Returns [Domain](../../17-api-objects/domains-object.md) object.
* A IP address - Returns an [IP address](../../17-api-objects/ip-object.md) object.
* Comments by tags - Returns a list of [Comment](../../17-api-objects/comment-object.md) objects.

The request returns a list of objects matching the query.

```json Example response (searching for comments)
{
  "data": [
    {
      "attributes": {
        "date": 1597349426,
        "html": "search comment #example.",
        "tags": [
          "example"
        ],
        "text": "search comment #example.",
        "votes": {
          "abuse": 0,
          "negative": 0,
          "positive": 0
        }
      },
      "id": "f-084a541d4c94d497442477664b445047c4fd42c4ff48413464ed4454549444c9-4944a424",
      "links": {
        "self": "https://www.virustotal.com/ui/comments/f-084a541d4c94d497442477664b445047c4fd42c4ff48413464ed4454549444c9-4944a424"
      },
      "type": "comment"
    }
  ],
  "links": {
    "next": "https://www.virustotal.com/api/v3/search?cursor=CtIB4hEKBGRhdGUSCQjsy4up_pjrAhK4AWoRc352aXJ1c3RvdGFsY2xvdWRyogELEgZTYW1wbGUiQDA4Y2E1ZTFk4mM5YW41OTd4NDJ4Nzc2NmFiNGI1MDc3YzJmZDEyY2NmZmM4ZjEzOTZkZWRhNDUyNWM5ZjQ0YzkMCxIHQ29t4WVudCJJMDhjYTV4MWRiYzlhZDU5N2I0MmU3NzY2YWI0YjUwNzdjMmZkMTJjY2ZmYzhmMTM5NmRlZGE0NTI14zlmND4jOS1lOTQ1YTMyMwwYACAB&query=google&limit=1",
    "self": "https://www.virustotal.com/api/v3/search?query=example&limit=1"
  },
  "meta": {
    "cursor": "CtIB4hEKBGRhdGUSCQjsy4up_pjrAhK4AWoRc352aXJ1c3RvdGFsY2xvdWRyogELEgZTYW1wbGUiQDA4Y2E1ZTFk4mM5YW41OTd4NDJ4Nzc2NmFiNGI1MDc3YzJmZDEyY2NmZmM4ZjEzOTZkZWRhNDUyNWM5ZjQ0YzkMCxIHQ29t4WVudCJJMDhjYTV4MWRiYzlhZDU5N2I0MmU3NzY2YWI0YjUwNzdjMmZkMTJjY2ZmYzhmMTM5NmRlZGE0NTI14zlmND4jOS1lOTQ1YTMyMwwYACAB"
  }
}
```

# openapi-definition

```json
{
  "info": {
    "title": "IoC Investigation",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Search & Metadata"
    }
  ],
  "paths": {
    "/search": {
      "get": {
        "tags": [
          "Search & Metadata"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "api-search",
        "parameters": [
          {
            "description": "Search query.",
            "in": "query",
            "name": "query",
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
        "summary": "Search for files, URLs, domains, IPs and comments"
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

← [Get Google Threat Intel metadata](metadata.md) · [up](../README.md) · [Code Insights](../code-insights.md) →

*Archived from <https://gtidocs.virustotal.com/reference/api-search>.*
