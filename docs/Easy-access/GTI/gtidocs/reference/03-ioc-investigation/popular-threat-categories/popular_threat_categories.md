---
title: "Get a list of popular threat categories"
source: https://gtidocs.virustotal.com/reference/popular_threat_categories
slug: popular_threat_categories
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T02:04:45.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Popular Threat Categories](../popular-threat-categories.md) › Get a list of popular threat categories

---

# get-a-list-of-popular-threat-categories

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
      "name": "Popular Threat Categories"
    }
  ],
  "paths": {
    "/popular_threat_categories": {
      "get": {
        "tags": [
          "Popular Threat Categories"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "popular_threat_categories",
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\"data\": [\n  \"adware\", \"banker\", \"downloader\",\n  \"dropper\", \"fakeav\", \"hacktool\",\n  \"miner\", \"phising\", \"pua\",\n  \"ransomware\", \"spyware\", \"trojan\",\n  \"virus\", \"worm\"]}"
                  }
                },
                "schema": {
                  "properties": {
                    "data": {
                      "items": {
                        "type": "string"
                      },
                      "type": "array"
                    }
                  },
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
        "summary": "Get a list of popular threat categories"
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

← [Popular Threat Categories](../popular-threat-categories.md) · [up](../README.md) · [Zipping files](../zipping-files.md) →

*Archived from <https://gtidocs.virustotal.com/reference/popular_threat_categories>.*
