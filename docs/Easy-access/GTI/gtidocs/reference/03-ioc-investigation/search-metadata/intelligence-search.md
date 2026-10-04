---
title: "Advanced corpus search"
source: https://gtidocs.virustotal.com/reference/intelligence-search
slug: intelligence-search
section: reference
group: "IoC Investigation"
updatedAt: 2026-02-05T12:43:34.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Search & Metadata](../search-metadata.md) › Advanced corpus search

---

# advanced-corpus-search

> 🚧 Searches using a fuzzy hash (ssdeep, TLSH, ...) are throttled due to performance reasons. The typical throttler is 15 searches / minute.

This endpoint allows to search for files in the Google Threat Intelligence's dataset, using the same query syntax that you would use in the Google TI user interface, where you can use this [full list of modifiers](https://gtidocs.readme.io/docs/full-list-of-google-threat-intelligence-search-modifiers)   **URL Safe encoding must be used when using this endpoint programatically.**

The result from this endpoint is a collection of file objects that match the given query. If the `descriptors_only` parameter is set to `true`, the resulting collection will contain only the object descriptors. This is useful if you are interested in getting only the SHA-256 of the matching files. In those cases you better set `descriptors_only=true` for reducing the latency of your requests.

> 🚧 Content searches can not be sorted
>
> If your query contains content search the order parameter will make no effect.

The `order` parameter defines the order in which results are returned. They can be followed by a plus (`+`) or minus (`-`) sign for indicating ascending or descending order respectively (i.e: `<order>+`, `<order>-`). If no ascending/descending order is specified it's assumed to be ascending, so `<order>` and `<order>+` are equivalent. If the `order` parameter is not provided, items are returned in a default order. The following table shows supported and default orders for every kind of entity:

| Entity type | Supported orders                                                                     | Default order             |
| :---------- | :----------------------------------------------------------------------------------- | :------------------------ |
| file        | first\_submission\_date, last\_submission\_date, positives, times\_submitted, size   | last\_submission\_date-   |
| url         | first\_submission\_date, last\_submission\_date, positives, times\_submitted, status | last\_submission\_date-   |
| domain      | creation\_date, last\_modification\_date, last\_update\_date, positives              | last\_modification\_date- |
| ip          | ip, last\_modification\_date, positives                                              | last\_modification\_date- |

This request returns a list of API objects ([files](../files.md), [URLs](../../17-api-objects/url-object.md), [IP addresses](../../17-api-objects/ip-object.md) or [domains](../../17-api-objects/domains-object.md)).

Also, some context attributes are added in certain searches:

* When searching files by `content`. These context attributes are:
  * `confidence`: <*float*>  match confidence.
  * `match_in_subfile`: <*boolean*> whether the content match was found in a [subfile](../../17-api-objects/file-object/file-object-bundled-files.md) or not.
  * `snippet`: <*string*> snippet ID. This ID can be later used in `/intelligence/search/snippets/{id}` endpoint.

* When doing a hash similarity search:
  * `similarity_score`: <*float*> number between 0 and 1 indicating the percentage of the fuzzy hash that matched. For example, `1.0` indicates the hash is the same as the specified; `0.5` that half of the hash matches the one given.

```json Example response (search by file content)
{
  "data": [
    {
      "context_attributes": {
        "confidence": 1,
        "match_in_subfile": false,
        "snippet": "L3Z0c2FtcGxlcy8zODIzMzkzNjNhOTM2NDM2ZDM2MDM1MzFkM2IzOGEzMmUzMTUzNzM3MTM4MzY3MzBlM2Q2MzQ4MzY1M2MzYzNhfHw3MTg1Mzk2OjExfHwxNTk5NDY0OTQ3fHwzODIzMzkzNjNhOTM2NDM2ZDM2MDM1MzFkM2IzOGEzMmUzMTUzNzM3MTM4MzY3MzBlM2Q2MzQ4MzY1M2MzYzNh"
      },
      "id": "382339363a936436d3603531d3b38a32e315373713836730e3d63483653c3c3a",
      "type": "file"
    }
  ],
  "links": {
    "next": "https://www.virustotal.com/api/v3/intelligence/search?cursor=H4sI...A&query=content%3A+%22hello+world%22&limit=1&descriptors_only=true",
    "self": "https://www.virustotal.com/api/v3/intelligence/search?query=content%3A%20%22hello%20world%22&descriptors_only=true&limit=1"
  },
  "meta": {
    "cursor": "H4sIAAA...",
    "days_back": 365
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
    "/intelligence/search": {
      "get": {
        "tags": [
          "Search & Metadata"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "intelligence-search",
        "parameters": [
          {
            "description": "Your API key",
            "in": "header",
            "name": "x-apikey",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Search query using URL Safe encoding",
            "in": "query",
            "name": "query",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Sort order (see table in the description above)",
            "in": "query",
            "name": "order",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Maximum number of results per page (Max. 300)",
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
            "description": "Continuation cursor",
            "in": "query",
            "name": "cursor",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Whether to return full object information or just object descriptors.",
            "in": "query",
            "name": "descriptors_only",
            "schema": {
              "default": false,
              "type": "boolean"
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
        "summary": "Advanced corpus search"
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

← [Search & Metadata](../search-metadata.md) · [up](../README.md) · [Get file content search snippets](intelligence-search-snippets.md) →

*Archived from <https://gtidocs.virustotal.com/reference/intelligence-search>.*
