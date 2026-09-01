---
title: "Get Next Communication in a Channel"
source: https://gtidocs.virustotal.com/reference/get-ddw-channel-next-communications
slug: get-ddw-channel-next-communications
section: reference
group: "Global Landscape"
updatedAt: 2026-03-23T15:04:02.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Global Landscape](../README.md) › [Dark Web](../dark-web.md) › Get Next Communication in a Channel

---

# get-next-communication-in-a-channel

Fetches the next chronological records in a [Communication Channel](../../17-api-objects/dark-web-objects/dark-web-communication-channel-object.md), using a provided Communication ID as the reference point. This endpoint returns a list of [Communication](../../17-api-objects/dark-web-objects/dark-web-communication-object.md) objects.

# examples

Retrieve the content and content\_translated attributes for the 10 communications immediately following ID 5f5c625e-c262-440e-8d11-54f96fc78f96 within channel f0fb347760e42d9177466ae0429f2dfb72d53597bd253655c78dfb16fddb1504.

```python
import requests

id = "f0fb347760e42d9177466ae0429f2dfb72d53597bd253655c78dfb16fddb1504"
communication_id = "5f5c625e-c262-440e-8d11-54f96fc78f96"
attributes = "content,content_translated"
limit = 10

url = f"https://www.virustotal.com/api/v3/ddw_communication_channels/{id}/next_communications/{communication_id}?attributes={attributes}&limit={limit}"

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
    "/ddw_communication_channels/{id}/next_communications/{communication_id}": {
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
            "description": "Dark Web Communication Channel identifier."
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
            "in": "header",
            "name": "x-apykey",
            "schema": {
              "type": "string"
            },
            "description": "Your API key.",
            "required": true
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
              "type": "integer",
              "format": "int32",
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
          }
        ],
        "operationId": "get_ddw-communication-channels-id-next-communications-communication-id"
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

← [Get a Dark Web Communication Channel object](get-ddw-communication-channel.md) · [up](../README.md) · [Get Previous Communication in a Channel](get-ddw-channel-previous-communications.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-ddw-channel-next-communications>.*
