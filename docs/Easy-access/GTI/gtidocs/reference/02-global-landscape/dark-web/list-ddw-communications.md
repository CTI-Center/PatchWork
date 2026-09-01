---
title: "List Dark Web Communications"
source: https://gtidocs.virustotal.com/reference/list-ddw-communications
slug: list-ddw-communications
section: reference
group: "Global Landscape"
updatedAt: 2026-03-23T15:04:02.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Global Landscape](../README.md) › [Dark Web](../dark-web.md) › List Dark Web Communications

---

# list-dark-web-communications

Use this endpoint to list [Dark Web Communication](../../17-api-objects/dark-web-objects/dark-web-communication-object.md) objects, which are the smallest communication unit ingested in our dark web dataset.

# filters

Available filters for Dark Web Communication objects are detailed in the [Dark Web Advanced Searches](https://gtidocs.readme.io/docs/dark-web-guide#dark-web-advanced-searches)  section of the [Dark Web](https://gtidocs.readme.io/docs/dark-web-guide)  guide. These modifiers support complex queries using parentheses `(`,`)` and Boolean operators (`AND`, `OR`, `NOT`). See the **Examples** section for request syntax.

# examples

Search for 10 communication of paste type with any mention to DDoS attacks.

```python
import requests

filter = "type:paste content:DDoS"

url = f"https://www.virustotal.com/api/v3/ddw_communications?filter={filter}"

headers = {
    "accept": "application/json",
    "x-apikey": <api-key>
}

response = requests.get(url, headers=headers)
```

Search for 6 communications where the channel name or description contains 'Data Leak', or the subject contains 'bins'. Results must also include at least one of the following credit card BINs (403567, 403568, or 403642) and specifically mention 'credit card' within the body.

```python
import requests

filter = "(communication_channel.name:'Data Leak' OR communication_channel.description:'Data Leak' or subject:'bins') content:'credit card' (content:'403567' OR content:'403568' OR content:'403642')"
limit = 6

url = f"https://www.virustotal.com/api/v3/ddw_communications?filter={filter}&limit={limit}"

headers = {
    "accept": "application/json",
    "x-apikey": <api-key>
}

response = requests.get(url, headers=headers)
```

Retrieve the translated content, URL, and timestamp for 20 communications from the user 'bob' on Telegram.

```python
import requests

filter = "author.name:bob service.name:telegram"
limit = 20
attributes = "content_translated,origin_url,timestamp"

url = f"https://www.virustotal.com/api/v3/ddw_communications?filter={filter}&limit={limit}&attributes={attributes}"

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
    "/ddw_communications": {
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
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            },
            "description": "Your API key.\n",
            "required": true
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
          },
          {
            "in": "query",
            "name": "filter",
            "schema": {
              "type": "string"
            },
            "description": "Filter communications/objects by different properties as previously described."
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
        "operationId": "get_ddw-communications"
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

← [Dark Web](../dark-web.md) · [up](../README.md) · [Get a Dark Web Communication object](get-ddw-communication.md) →

*Archived from <https://gtidocs.virustotal.com/reference/list-ddw-communications>.*
