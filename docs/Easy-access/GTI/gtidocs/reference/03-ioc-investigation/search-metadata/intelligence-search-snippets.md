---
title: "Get file content search snippets"
source: https://gtidocs.virustotal.com/reference/intelligence-search-snippets
slug: intelligence-search-snippets
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T02:04:51.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Search & Metadata](../search-metadata.md) › Get file content search snippets

---

# get-file-content-search-snippets

This request returns file content snippets that matched a query in the [`/search`](intelligence-search.md) endpoint. The response is a list of strings containing both content hexdump and plain text. Matched content is found between `*` characters, more file content is returned to provide additional context about the match.

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
    "/intelligence/search/snippets/{snippet}": {
      "get": {
        "tags": [
          "Search & Metadata"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "intelligence-search-snippets",
        "parameters": [
          {
            "description": "Extracted snippet from context attributes at [/search](https://gtidocs.readme.io/reference/intelligence-search) endpoint.",
            "in": "path",
            "name": "snippet",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Your API key.",
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
                    "value": "{\n  \"data\": [\n    \"01CEE0A0: 09 20 2A 0A 09 20 2A 20  45 78 61 6D 70 6C 65 3A  . *.. * Example:\\n01CEE0B0: 0A 09 20 2A 0A 09 20 2A  20 20 20 20 20 35\u001c 68 65\u001d  .. *.. *     5\u001che\u001d\\n01CEE0C0: \u001c6C 6C 6F 20 77 6F 72 6C  64\u001d 0A 09 20 2A 20 20 20  \u001cllo world\u001d.. *   \",\n    \"01CEF650: 6D 70 6C 65 3A 0A 09 20  2A 0A 09 20 2A 20 20 20  mple:.. *.. *   \\n01CEF660: 20 20 31 31 3A \u001c68 65 6C  6C 6F 20 77 6F 72 6C 64\u001d    11:\u001chello world\u001d\\n01CEF670: 32 3A 68 69 0A 09 20 2A  0A 09 20 2A 20 49 66 20  2:hi.. *.. * If \",\n    \"01D22020: 5C 6E 20 2A 20 45 78 61  6D 70 6C 65 3A 5C 6E 20  \\\\n * Example:\\\\n \\n01D22030: 2A 5C 6E 20 2A 20 20 20  20 20 35\u001c 68 65 6C 6C 6F\u001d  *\\\\n *     5\u001chello\u001d\\n01D22040: \u001c20 77 6F 72 6C 64 \u001d5C 6E  20 2A 20 20 20 20 20 33  \u001c world\u001d\\\\n *     3\",\n    \"02C29AB0: 6C 6F 67 28 68 65 6C 6C  6F 2C 20 27 77 6F 72 6C  log(hello, 'worl\\n02C29AC0: 64 27 29 3B 0A 20 2A 20  27\u001c 68 65 6C 6C 6F 20 77\u001d  d');. * '\u001chello w\u001d\\n02C29AD0: \u001c6F 72 6C 64 \u001d27 0A 20 2A  2F 0A 65 78 70 6F 72 74  \u001corld\u001d'. */.export\",\n    \"02C643E0: 28 68 65 6C 6C 6F 2C 20  27 77 6F 72 6C 64 27 29  (hello, 'world')\\n02C643F0: 3B 0A 20 2A 20 27 \u001c68 65  6C 6C 6F 20 77 6F 72 6C\u001d  ;. * '\u001chello worl\u001d\\n02C64400: \u001c64 \u001d27 0A 20 2A 2F 0A 76  61 72 20 6C 6F 67 20 3D  \u001cd\u001d'. */.var log =\"\n  ]\n}"
                  }
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
                    "value": "{\n  \"error\": {\n    \"code\": \"BadRequestError\",\n    \"message\": \"Invalid token\"\n  }\n}"
                  }
                },
                "schema": {
                  "properties": {
                    "error": {
                      "properties": {
                        "code": {
                          "type": "string"
                        },
                        "message": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    }
                  },
                  "type": "object"
                }
              }
            },
            "description": "400"
          }
        },
        "security": [],
        "summary": "Get file content search snippets"
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

← [Advanced corpus search](intelligence-search.md) · [up](../README.md) · [Get Google Threat Intel metadata](metadata.md) →

*Archived from <https://gtidocs.virustotal.com/reference/intelligence-search-snippets>.*
