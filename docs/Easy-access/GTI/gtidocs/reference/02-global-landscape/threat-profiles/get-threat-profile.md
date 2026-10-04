---
title: "Get a Threat Profile"
source: https://gtidocs.virustotal.com/reference/get-threat-profile
slug: get-threat-profile
section: reference
group: "Global Landscape"
updatedAt: 2026-06-05T14:42:43.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Global Landscape](../README.md) › [Threat Profiles](../threat-profiles.md) › Get a Threat Profile

---

# get-a-threat-profile

Use this endpoint to get a certain [Threat Profile](../../17-api-objects/threat-profile-object.md) object.

Next to the Threat Profile object, you'll see a parameter specifying your relationship to it, structured as follows:

```json
"context_attributes":
{
  "shared_with_me": "<_boolean_> if the Threat Profile has been shared with ('true') or created by the user ('false').",
  "role": "<_string_> user's role or privileges regarding the Threat Profile as 'viewer','owner' or 'editor'."
}
```

## examples

Get my Threat Profiles with 54c06160a3cf4578878f68f0df2bf877 identifier.

```python
import requests

profile_id = "54c06160a3cf4578878f68f0df2bf877"
url = f"https://www.virustotal.com/api/v3/threat_profiles/{profile_id}"
headers = {
    "accept": "application/json","x-apikey": <api-key>
}
response = requests.get(url, headers=headers)
```

<br />

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
    "/threat_profiles/{profile_id}": {
      "get": {
        "tags": [
          "Threat Profiles"
        ],
        "description": "",
        "operationId": "get-threat-profile",
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
            "description": "Threat Profile's ID",
            "in": "path",
            "name": "profile_id",
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
        "summary": "Get a Threat Profile"
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

← [Create a Threat Profile](create-threat-profile.md) · [up](../README.md) · [Update a Threat Profiles](update-threat-profile.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-threat-profile>.*
