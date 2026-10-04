---
title: "List Threat Profiles"
source: https://gtidocs.virustotal.com/reference/list-threat-profiles
slug: list-threat-profiles
section: reference
group: "Global Landscape"
updatedAt: 2026-06-05T14:42:13.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Global Landscape](../README.md) › [Threat Profiles](../threat-profiles.md) › List Threat Profiles

---

# list-threat-profiles

This endpoint returns the list of user's [Threat Profiles](../../17-api-objects/threat-profile-object.md).

Next to each Threat Profile object, you'll see a parameter specifying user's relationship to it, structured as follows:

```json
"context_attributes":
{
  "shared_with_me": "<_boolean_> if the Threat Profile has been shared with ('true') or created by the user ('false').",
  "role": "<_string_> user's role or privileges regarding the Threat Profile as 'viewer','owner' or 'editor'."
}
```

## examples

Get my first 5 of my Threat Profiles.

```python
import requests

limit = 5
url = f"https://www.virustotal.com/api/v3/threat_profiles?limit={limit}"
headers = {
    "accept": "application/json","x-apikey": <api-key>
}
response = requests.get(url, headers=headers)
```

Get my complete list of my Threat Profiles.

```python
import requests

url = f"https://www.virustotal.com/api/v3/threat_profiles"
headers = {
    "accept": "application/json","x-apikey": <api-key>
}
while url: # pagination
  response = requests.get(url, headers=headers)
  response = response.json()
  url = response["links"].get("next",None) # pagination
```

# openapi-definition

```json
{
  "info": {
    "title": "Threat Landscape",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Threat Profiles"
    }
  ],
  "paths": {
    "/threat_profiles": {
      "get": {
        "tags": [
          "Threat Profiles"
        ],
        "description": "",
        "operationId": "list-threat-profiles",
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
            "description": "Maximum number of Threat Profiles to retrieve (max 40)",
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
        "summary": "List Threat Profiles"
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

← [Threat Profiles](../threat-profiles.md) · [up](../README.md) · [Create a Threat Profile](create-threat-profile.md) →

*Archived from <https://gtidocs.virustotal.com/reference/list-threat-profiles>.*
