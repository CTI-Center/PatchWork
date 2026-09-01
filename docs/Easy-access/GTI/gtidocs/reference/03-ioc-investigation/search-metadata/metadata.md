---
title: "Get Google Threat Intel metadata"
source: https://gtidocs.virustotal.com/reference/metadata
slug: metadata
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T02:04:52.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Search & Metadata](../search-metadata.md) › Get Google Threat Intel metadata

---

# get-google-threat-intel-metadata

This endpoint returns a dictionary with metadata related to Google Threat Intelligence, which includes a full list of engines in use, a list of existing privileges, etc.

```json Example
{
  "data": {
    "engines": {
      "ALYac": {},
      "APEX": {},
      "AVG": {},
      "AVware": {},
      "Acronis": {},
      "Ad-Aware": {},
      "AegisLab": {},
      "AhnLab-V3": {},
      "Alibaba": {},
      "Antiy-AVL": {},
      "Arcabit": {},
      "Avast": {},
      "Avast-Mobile": {},
      "Avira": {},
      "Babable": {},
      "Baidu": {}
    },
    "privileges": [
      "cases",
      "click_to_accept",
      "creditcards",
      "dogfooder",
      "file-behaviour-feed",
      "downloads-tier-1",
      "downloads-tier-2"
    ],
    "relationships": {
      "analysis": [
        {
          "description": "File or URL the analysis belongs to.",
          "name": "item"
        }
      ],
      "async_search_job": [
        {
          "description": "Objects that match the search.",
          "name": "matches"
        }
      ],
      "case": [
        {
          "description": "Returns the files objects in the case.",
          "name": "files"
        },
        {
          "description": "Returns the graphs objects in the case.",
          "name": "graphs"
        }
      ],
      "code_block": [
        {
          "description": "Files that contain the code block.",
          "name": "files"
        }
      ],
      "comment": [
        {
          "description": "Object to which the comment belongs to.",
          "name": "item"
        },
        {
          "description": "User who wrote the comment.",
          "name": "author"
        }
      ],
      "domain": [
        {
          "description": "Votes for the file/URL.",
          "name": "votes"
        },
        {
          "description": "Comments for the Domain or IP's related entities.",
          "name": "related_comments"
        },
        {
          "description": "Parent domain.",
          "name": "parent"
        }
      ]
    }
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
    "/metadata": {
      "get": {
        "tags": [
          "Search & Metadata"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "metadata",
        "parameters": [
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
        "summary": "Get Google Threat Intel metadata"
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

← [Get file content search snippets](intelligence-search-snippets.md) · [up](../README.md) · [Search for files, URLs, domains, IPs and comments](api-search.md) →

*Archived from <https://gtidocs.virustotal.com/reference/metadata>.*
