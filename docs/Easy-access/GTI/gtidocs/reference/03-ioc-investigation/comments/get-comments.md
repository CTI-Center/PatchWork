---
title: "Get latest comments"
source: https://gtidocs.virustotal.com/reference/get-comments
slug: get-comments
section: reference
group: "IoC Investigation"
updatedAt: 2026-02-05T12:43:34.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Comments](../comments.md) › Get latest comments

---

# get-latest-comments

This endpoint retrieves information about the latest comments added to Google Threat Intelligence.\
You can do some filtering over those comments, and get only those that contains a certain tag inside (e.g. filter=tag:malware).

```json Response example
{
  "meta": {
    "cursor": "Cs8BChEKBGRhdGUSCQiCnsTiupvwAhK1AWoRc352aXJ1c3RvdGFsY2xvdWRynwELEgNVUkwiQDAxMTkxNTk0MmRiNTU2YmJhYjUxMzdmNzYxZWZlNjFmZWQyYjAwNTk4ZmVhOTAwMzYwYjgwMGIxOTNhN2JmMzEMCxIHQ29tbWVudCJJMDExOTE1OTQyZGI1NTZiYmFiNTEzN2Y3NjFlZmU2MWZlZDJiMDA1OThmZWE5MDAzNjBiODAwYjE5M2E3YmYzMS1kOTRkN2M4YQwYACAB"
  },
  "data": [
    {
      "attributes": {
        "votes": {
          "positive": 0,
          "abuse": 0,
          "negative": 0
        },
        "tags": [
          "_:api",
          "_:public",
          "aicc",
          "monitorapp",
          "malware"
        ],
        "text": "#aicc #monitorapp #malware",
        "html": "#aicc #monitorapp #malware",
        "date": 1619424604
      },
      "type": "comment",
      "id": "u-011915942db556bbab5137f761efe61fed2b00598fea900360b800b193a7bf31-d94d7c8a",
      "links": {
        "self": "https://www.virustotal.com/api/v3/comments/u-011915942db556bbab5137f761efe61fed2b00598fea900360b800b193a7bf31-d94d7c8a"
      }
    }
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/comments?filter=tag%3Amalware&limit=1",
    "next": "https://www.virustotal.com/api/v3/comments?filter=tag%3Amalware&cursor=Cs8BChEKBGRhdGUSCQiCnsTiupvwAhK1AWoRc352aXJ1c3RvdGFsY2xvdWRynwELEgNVUkwiQDAxMTkxNTk0MmRiNTU2YmJhYjUxMzdmNzYxZWZlNjFmZWQyYjAwNTk4ZmVhOTAwMzYwYjgwMGIxOTNhN2JmMzEMCxIHQ29tbWVudCJJMDExOTE1OTQyZGI1NTZiYmFiNTEzN2Y3NjFlZmU2MWZlZDJiMDA1OThmZWE5MDAzNjBiODAwYjE5M2E3YmYzMS1kOTRkN2M4YQwYACAB&limit=1"
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
      "name": "Comments"
    }
  ],
  "paths": {
    "/comments": {
      "get": {
        "tags": [
          "Comments"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-comments",
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
            "description": "Number of items to retrieve",
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
            "description": "Filter returned elements",
            "in": "query",
            "name": "filter",
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
        "summary": "Get latest comments"
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

← [Comments](../comments.md) · [up](../README.md) · [Delete a comment](comment-id-delete.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-comments>.*
