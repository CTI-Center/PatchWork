---
title: "Generate a personal Authorization Token"
source: https://gtidocs.virustotal.com/reference/get-auth-token
slug: get-auth-token
section: reference
group: "Categorised Threat Lists"
updatedAt: 2025-09-25T00:39:32.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Categorised Threat Lists](../README.md) › [Threat Lists](../threat-lists.md) › Generate a personal Authorization Token

---

# generate-a-personal-authorization-token

Although the default Google Threat Intelligence API authorization method is via API keys, Threat Lists endpoints allow authorization tokens via query parameters for users whose integrations do not allow the `X-Apikey` custom header implemented for all endpoints.

## examples

Generate a new authorization token.

```python
import requests

url = "https://www.virustotal.com/api/v3/auth/auth_token"
headers = {"accept": "application/json","x-apikey": <api-key>}
response = requests.post(url, headers=headers)
print(response.text)
```

```curl
curl -X POST https://www.virustotal.com/api/v3/auth/auth_token -H "X-Apikey: <api-key>"
```

Retrieve the latest Ransomware threat list via authorization token

```python
import requests

auth_token = "<newly generated token>"
url = f"https://www.virustotal.com/api/v3/threat_lists/ransomware/latest?auth_token={auth_token}"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)
print(response.text)
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
    "/auth/auth_token": {
      "post": {
        "tags": [
          "Threat Lists"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-auth-token",
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
        "summary": "Generate a personal Authorization Token"
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

← [Threat Lists](../threat-lists.md) · [up](../README.md) · [List provisioned Categorised Threat Lists](list-provisioned-threat-lists.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-auth-token>.*
