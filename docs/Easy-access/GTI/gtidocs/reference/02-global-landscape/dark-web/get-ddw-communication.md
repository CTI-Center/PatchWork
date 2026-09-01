---
title: "Get a Dark Web Communication object"
source: https://gtidocs.virustotal.com/reference/get-ddw-communication
slug: get-ddw-communication
section: reference
group: "Global Landscape"
updatedAt: 2026-03-23T15:04:02.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Global Landscape](../README.md) › [Dark Web](../dark-web.md) › Get a Dark Web Communication object

---

# get-a-dark-web-communication-object

Use this endpoint to retrieve a [Dark Web Communication](../../17-api-objects/dark-web-objects/dark-web-communication-object.md) object by its unique identifier.

# examples

Retrieve the communication object with ID 616a132d-f942-4165-b132-60eca4348c54.

```python
import requests

id = "616a132d-f942-4165-b132-60eca4348c54"

url = f"https://www.virustotal.com/api/v3/ddw_communications/{id}"

headers = {"accept": "application/json","x-apikey": <api-key>}

response = requests.get(url, headers=headers)
```

Retrieve only the content and content\_translated attributes for communication ID 4a65a7e7-9f3f-4d1c-8b93-e85fc356b780.

```python
import requests

id = "4a65a7e7-9f3f-4d1c-8b93-e85fc356b780"
attributes = "content,content_translated"

url = f"https://www.virustotal.com/api/v3/ddw_communications/{id}?attributes={attributes}"

headers = {"accept": "application/json","x-apikey": <api-key>}

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
    "/ddw_communications/{id}": {
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
            "description": "Dark Web Communication identifier."
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
            "description": "A comma-separated list of the _[communications attributes](https://gtidocs.readme.io/reference/dark-web-communication-object)_ to be returned. (All attributes are returned by default.)"
          }
        ],
        "operationId": "get_ddw-communications-id"
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

← [List Dark Web Communications](list-ddw-communications.md) · [up](../README.md) · [Get objects related to a Dark Web Communication object](get-ddw-communication-relationships.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-ddw-communication>.*
