---
title: "Add a comment to a report"
source: https://gtidocs.virustotal.com/reference/create-report-comment
slug: create-report-comment
section: reference
group: "Reports & Analysis"
updatedAt: 2025-09-25T00:36:42.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Reports & Analysis](../README.md) › [Reports](../reports.md) › Add a comment to a report

---

# add-a-comment-to-a-report

> 🚧 Special privileges required
>
> Reports & Analysis are only available to users with the Google Threat Intelligence (Google TI) Enterprise or Enterprise Plus licenses.

With this endpoint you can post a comment for a given [Report](../../17-api-objects/report-object.md). The body for the `POST` request must be the JSON representation of a comment object. Notice however that you don't need to provide an ID for the object, as they are automatically generated for new comments.

Any word starting with # in your comment's text will be considered a tag, and added to the comment's tag attribute.

```json Example request
{
  "data": {
    "type": "comment",
    "attributes": {
    	"text": "Lorem #ipsum dolor sit ..."
    }
  }
}
```

```json Example response
{
  "data": {
    "type": "comment",
    "id": "<comment's ID>",
    "links": {
      "self": "https://www.virustotal.com/api/v3/comments/<comment's ID>"
    },
    "attributes": {
      "date": 1521725475,
      "tags": ["ipsum"],
      "html": "Lorem #ipsum dolor sit ...",
      "text": "Lorem #ipsum dolor sit ...",
      "votes": {
        "abuse": 0,
        "negative": 0,
        "positive": 0
      }
    }
  }
}
```

## examples

Add a comment on a report.

```python
import requests
import urllib

object_id = "report--24-10074016"
url = f"https://www.virustotal.com/api/v3/collections/{object_id}/comments"
payload = { "data": {
        "type": "comment",
        "attributes": { "text": "Lorem #ipsum dolor sit ..." }
    } }
headers = {"accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"}
response = requests.post(url, json=payload, headers=headers)
```

# openapi-definition

```json
{
  "info": {
    "title": "Reports & Analysis",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Reports",
      "description": "Reports & Analysis endpoints"
    }
  ],
  "paths": {
    "/collections/{id}/comments": {
      "post": {
        "tags": [
          "Reports"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "create-report-comment",
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
            "description": "Report's ID",
            "in": "path",
            "name": "id",
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
                    "description": "A comment object",
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
        "summary": "Add a comment to a report"
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

← [Get comments from a report](get-report-comments.md) · [up](../README.md) · [Get MITRE tactics and techniques associated with a report](get-report-mitre-tree.md) →

*Archived from <https://gtidocs.virustotal.com/reference/create-report-comment>.*
