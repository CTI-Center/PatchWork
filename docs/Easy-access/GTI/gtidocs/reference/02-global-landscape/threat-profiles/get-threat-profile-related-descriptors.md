---
title: "Get object descriptors related to a Threat Profile"
source: https://gtidocs.virustotal.com/reference/get-threat-profile-related-descriptors
slug: get-threat-profile-related-descriptors
section: reference
group: "Global Landscape"
updatedAt: 2026-06-05T14:43:41.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Global Landscape](../README.md) › [Threat Profiles](../threat-profiles.md) › Get object descriptors related to a Threat Profile

---

# get-object-descriptors-related-to-a-threat-profile

This endpoint is the same as [/threat\_profiles/{profile\_id}/{relationship}](get-threat-profile-relationships.md) except it returns just the related object's descriptor instead of returning all attributes.

Available relationships are described in the [Threat Profiles](../../17-api-objects/threat-profile-object.md#relationships) object **Relationships** section.

This endpoint requires the user to be the **owner** or an **editor** of the Threat Profile to be able to see users and groups with access to the Threat Profile.

## examples

Get the descriptors of 3 users and groups that have edition privileges on my Threat Profile with 332e02da667746f180a9740e94a3ec98 identifier.

```python
import requests

profile_id = "332e02da667746f180a9740e94a3ec98"
relationship = "editors"
limit = 3

url = f"https://www.virustotal.com/api/v3/threat_profiles/{profile_id}/relationships/{relationship}?limit={limit}"
headers = {
    "accept": "application/json","x-apikey": <api-key>
}
response = requests.get(url, headers=headers)
```

Get the descriptors of all users and groups that have viewer privileges on my Threat Profile with 332e02da667746f180a9740e94a3ec98 identifier.

```python
import requests

profile_id = "332e02da667746f180a9740e94a3ec98"
relationship = "viewers"

url = f"https://www.virustotal.com/api/v3/threat_profiles/{profile_id}/relationships/{relationship}"
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
    "/threat_profiles/{profile_id}/relationships/{relationship}": {
      "get": {
        "tags": [
          "Threat Profiles"
        ],
        "description": "",
        "operationId": "get-threat-profile-related-descriptors",
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
          },
          {
            "description": "Relationship name from [threat profile](https://gtidocs.readme.io/reference/threat-profile-object#relationships) relationships section",
            "in": "path",
            "name": "relationship",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Maximum number of related objects to retrieve (max 40)",
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
        "summary": "Get object descriptors related to a Threat Profile"
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

← [Get objects related to a Threat Profile](get-threat-profile-relationships.md) · [up](../README.md) · [Delete items from a Threat Profile](delete-threat-profile-relationships.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-threat-profile-related-descriptors>.*
