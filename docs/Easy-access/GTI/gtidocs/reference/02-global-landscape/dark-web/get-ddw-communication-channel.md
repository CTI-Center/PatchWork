---
title: "Get a Dark Web Communication Channel object"
source: https://gtidocs.virustotal.com/reference/get-ddw-communication-channel
slug: get-ddw-communication-channel
section: reference
group: "Global Landscape"
updatedAt: 2026-03-23T15:04:02.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Global Landscape](../README.md) › [Dark Web](../dark-web.md) › Get a Dark Web Communication Channel object

---

# get-a-dark-web-communication-channel-object

Use this endpoint to retrieve a [Dark Web Communication Channel](../../17-api-objects/dark-web-objects/dark-web-communication-channel-object.md) object by its unique identifier.

# examples

Retrieve the communication channel object with ID 5061d4801dcb13de593b4257734193eeb9f61595eccd99e7cc311c57e70833a1.

```python
import requests

id = "5061d4801dcb13de593b4257734193eeb9f61595eccd99e7cc311c57e70833a1"

url = f"https://www.virustotal.com/api/v3/ddw_communication_channels/{id}"

headers = {
    "accept": "application/json",
    "x-apikey": <api-key>
}

response = requests.get(url, headers=headers)
```

Retrieve only the URL and description attributes for communication channel with ID 5118255fbf18cf3bd85182016101efaa2f6e286e73fde3b0fa2c84c2fee27de1.

```python
import requests

id = "5118255fbf18cf3bd85182016101efaa2f6e286e73fde3b0fa2c84c2fee27de1"
attributes = "url,description"

url = f"https://www.virustotal.com/api/v3/ddw_communication_channels/{id}?attributes={attributes}"

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
    "/ddw_communication_channels/{id}": {
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
            "in": "header",
            "name": "x-apikey",
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
            "description": "A comma-separated list of the _[communication channel attributes](https://gtidocs.readme.io/reference/dark-web-communication-channel-object)_ to be returned. (All attributes are returned by default.)"
          }
        ],
        "operationId": "get_ddw-communication-channels-id"
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

← [Get objects related to a Dark Web Communication object](get-ddw-communication-relationships.md) · [up](../README.md) · [Get Next Communication in a Channel](get-ddw-channel-next-communications.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-ddw-communication-channel>.*
