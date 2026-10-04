---
title: "Add or update relationships between a Threat Profile and other objects"
source: https://gtidocs.virustotal.com/reference/add-threat-profile-relationships
slug: add-threat-profile-relationships
section: reference
group: "Global Landscape"
updatedAt: 2026-06-05T14:43:56.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Global Landscape](../README.md) › [Threat Profiles](../threat-profiles.md) › Add or update relationships between a Threat Profile and other objects

---

# add-or-update-relationships-between-a-threat-profile-and-other-objects

This endpoint adds new, or updates existing relationships between a Threat Profile and other objects. Available relationships are described in the [Threat Profiles](../../17-api-objects/threat-profile-object.md#relationships) object **Relationships** section. This endpoint requires objects' descriptors and the user to be the **owner** or an **editor** of the Threat Profile.

You can also [delete existing relationships](delete-threat-profile-relationships.md) between a Threat Profile.

## examples

Add user1 and members of group1 as new viewers to the Threat Profile with 332e02da667746f180a9740e94a3ec98 identifier.

```python
import requests

profile_id = "332e02da667746f180a9740e94a3ec98"
relationship = "viewers"
payload = {
    "data":[
        {
            "type": "user",
            "id": "user1"},
        {
            "type": "group",
            "id": "group1"}
    ]
}
url = f"https://www.virustotal.com/api/v3/threat_profiles/{profile_id}/relationships/{relationship}"
headers = {
    "accept": "application/json","x-apikey": <api-key>
}
response = requests.post(url, json=payload, headers=headers)
```

Change privileges of user1 and members of group1 from viewers to editors of the Threat Profile with 332e02da667746f180a9740e94a3ec98 identifier.

```python
import requests

profile_id = "332e02da667746f180a9740e94a3ec98"
relationship = "editors"
payload = {
    "data":[
        {
            "type": "user",
            "id": "user1"},
        {
            "type": "group",
            "id": "group1"}
    ]
}
url = f"https://www.virustotal.com/api/v3/threat_profiles/{profile_id}/relationships/{relationship}"
headers = {
    "accept": "application/json","x-apikey": <api-key>
}
response = requests.post(url, json=payload, headers=headers)
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
      "post": {
        "tags": [
          "Threat Profiles"
        ],
        "description": "",
        "operationId": "add-threat-profile-relationships",
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
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "properties": {
                  "data": {
                    "description": "List of objects descriptors",
                    "format": "json",
                    "type": "string"
                  }
                },
                "required": [
                  "data"
                ],
                "type": "object"
              }
            }
          }
        },
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
        "summary": "Add or update relationships between a Threat Profile and other objects"
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

← [Delete items from a Threat Profile](delete-threat-profile-relationships.md) · [up](../README.md) · [Get a Threat Profile's timeline associations](get-threat-profile-timeline-associations.md) →

*Archived from <https://gtidocs.virustotal.com/reference/add-threat-profile-relationships>.*
