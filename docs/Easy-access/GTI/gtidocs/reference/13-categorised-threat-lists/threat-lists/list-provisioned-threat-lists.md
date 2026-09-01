---
title: "List provisioned Categorised Threat Lists"
source: https://gtidocs.virustotal.com/reference/list-provisioned-threat-lists
slug: list-provisioned-threat-lists
section: reference
group: "Categorised Threat Lists"
updatedAt: 2025-09-25T00:39:33.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Categorised Threat Lists](../README.md) › [Threat Lists](../threat-lists.md) › List provisioned Categorised Threat Lists

---

# list-provisioned-categorised-threat-lists

This endpoint displays the Categorized Threat Lists that are available to the user, based on the user's Google Threat Intelligence license, as follows:

```json
{
    "data": \<_list of dictionaries_> the list of provisioned threat lists.
    [
        {
            "id": \<_string_> the identifier os the provisioned type of threat list (Ex: cryptominer, ransomware, malicious-network-infrastructure, malware, threat-actor, etc).
            "type": "threat_list",
            "links":
            {
                "self": \<_string_> the endpoint of the threat list.
            },
            "attributes": \<_dictionary_> attributes of the threat list.
            {
                "description": \<_string_> description of the threat list.
                "name": \<_string_> name of the threat list.
            }
        },
    ]
}
```

## example-response

```json
{
    "data":
    [
        {
            "id": "cryptominer",
            "type": "threat_list",
            "links":
            {
                "self": "https://www.virustotal.com/api/v3/threat_lists/cryptominer"
            },
            "attributes":
            {
                "description": "Cryptominer Threat List",
                "name": "cryptominer"
            }
        },
        {
            "id": "first-stage-delivery-vectors",
            "type": "threat_list",
            "links":
            {
                "self": "https://www.virustotal.com/api/v3/threat_lists/first-stage-delivery-vectors"
            },
            "attributes":
            {
                "description": "First Stage Delivery Vector Threat List",
                "name": "first-stage-delivery-vectors"
            }
        }
    ]
}
```

## examples

List my provisioned/enabled Threat Lists.

```python
import requests

url = "https://www.virustotal.com/api/v3/threat_lists"
headers = {"accept": "application/json","x-apikey": <api-key>}
response = requests.get(url, headers=headers)
print(response.text)
```

```curl
curl -X GET https://www.virustotal.com/api/v3/threat_lists -H "X-Apikey: <api-key>"
```

# openapi-definition

```json
{
  "components": {
    "securitySchemes": {
      "sec0": {
        "in": "header",
        "name": "x-apikey",
        "type": "apiKey"
      },
      "sec1": {
        "type": "http",
        "scheme": "custom",
        "description": "Custom authentication token. The token must be provided in the query string via \"auth_token\" parameter if you don't use the apiKey method."
      }
    }
  },
  "info": {
    "title": "Categorised Threat Lists",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Threat Lists"
    }
  ],
  "paths": {
    "/threat_lists": {
      "get": {
        "tags": [
          "Threat Lists"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "list-provisioned-threat-lists",
        "parameters": [
          {
            "description": "Your API key",
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
        "summary": "List provisioned Categorised Threat Lists"
      }
    }
  },
  "security": [
    {
      "sec0": [],
      "sec1": []
    }
  ],
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

← [Generate a personal Authorization Token](get-auth-token.md) · [up](../README.md) · [Get the latest Threat List](get-latest-threat-list.md) →

*Archived from <https://gtidocs.virustotal.com/reference/list-provisioned-threat-lists>.*
