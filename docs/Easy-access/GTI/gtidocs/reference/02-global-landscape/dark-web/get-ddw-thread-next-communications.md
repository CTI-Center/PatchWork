---
title: "Get Next Communication in a Thread"
source: https://gtidocs.virustotal.com/reference/get-ddw-thread-next-communications
slug: get-ddw-thread-next-communications
section: reference
group: "Global Landscape"
updatedAt: 2026-03-23T15:04:02.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Global Landscape](../README.md) › [Dark Web](../dark-web.md) › Get Next Communication in a Thread

---

# get-next-communication-in-a-thread

Fetches the next chronological records in a [Dark Web Conversation Thread](../../17-api-objects/dark-web-objects/dark-web-conversation-thread-object.md), using a provided Communication ID as the reference point. This endpoint returns a list of [Communication](../../17-api-objects/dark-web-objects/dark-web-communication-object.md) objects.

# examples

Retrieve the content and content\_translated attributes for the 3 communications immediately following ID c954b4fc-bdfe-4214-8386-614e70ed7670 within thread 39d927da5fef18b43456075e75e3c42378ef63958e59af04181bdf77f61ed249

```python
import requests

id = "39d927da5fef18b43456075e75e3c42378ef63958e59af04181bdf77f61ed249"
communication_id = "c954b4fc-bdfe-4214-8386-614e70ed7670"
attributes = "content,content_translated"
limit = 3

url = f"https://www.virustotal.com/api/v3/ddw_conversation_threads/{id}/next_communications/{communication_id}?attributes={attributes}&limit={limit}"

headers = {
    "accept": "application/json",
    "x-apikey": <api-key>
}

response = requests.get(url, headers=headers)
```

# openapi-definition

```json
{
  "info": {
    "title": "Threat Landscape",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "paths": {
    "/ddw_conversation_threads/{id}/next_communications/{communication_id}": {
      "get": {
        "description": "",
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
            "description": "Dark Web Conversation Thread identifier."
          },
          {
            "in": "path",
            "name": "communication_id",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Dark Web Communication identifier."
          },
          {
            "in": "query",
            "name": "attributes",
            "schema": {
              "type": "string"
            },
            "description": "A comma-separated list of the _[communications attributes](https://gtidocs.readme.io/reference/dark-web-communication-object)_ to be returned. (All attributes are returned by default.)"
          },
          {
            "in": "query",
            "name": "limit",
            "schema": {
              "type": "string",
              "default": "10"
            },
            "description": "Maximum number of communications to retrieve (max 40)."
          },
          {
            "in": "query",
            "name": "cursor",
            "schema": {
              "type": "string"
            },
            "description": "Continuation cursor."
          },
          {
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            },
            "description": "Your API key.",
            "required": true
          }
        ],
        "operationId": "get_ddw-conversation-threads-id-next-communications-communication-id"
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

← [Get objects related to a Dark Web Service object](get-ddw-service-relationships.md) · [up](../README.md) · [Get Previous Communication in a Thread](get-ddw-thread-previous-communications.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-ddw-thread-next-communications>.*
