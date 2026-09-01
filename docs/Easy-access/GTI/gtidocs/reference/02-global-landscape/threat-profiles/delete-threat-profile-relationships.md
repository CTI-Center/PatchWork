---
title: "Delete items from a Threat Profile"
source: https://gtidocs.virustotal.com/reference/delete-threat-profile-relationships
slug: delete-threat-profile-relationships
section: reference
group: "Global Landscape"
updatedAt: 2026-06-05T14:43:48.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Global Landscape](../README.md) › [Threat Profiles](../threat-profiles.md) › Delete items from a Threat Profile

---

# delete-items-from-a-threat-profile

This endpoint deletes objects that are related to a Threat Profile. Available relationships are described in the [Threat Profiles](../../17-api-objects/threat-profile-object.md#relationships) object **Relationships** section. This endpoint requires objects' descriptors and the user to be the **owner** or an **editor** of the Threat Profile.

You can also [add new or update existing](add-threat-profile-relationships.md) relationships between a Threat Profile and other objects.

Another **editor** or the **owner** of the Threat Profile can [modify a user's privileges for it](add-threat-profile-relationships.md).

## examples

Remove access of user1 and user2 editors to the Threat Profile with 332e02da667746f180a9740e94a3ec98 identifier.

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
            "type": "user",
            "id": "user2"}
    ]
}
url = f"https://www.virustotal.com/api/v3/threat_profiles/{profile_id}/relationships/{relationship}"
headers = {
    "accept": "application/json","x-apikey": <api-key>
}
response = requests.delete(url, json=payload, headers=headers)
```

Revoke access for members of group1 and group2 with editor privilege to the Threat Profile identified as 332e02da667746f180a9740e94a3ec98.

```python
import requests

profile_id = "332e02da667746f180a9740e94a3ec98"
relationship = "editors"
payload = {
    "data":[
        {
            "type": "group",
            "id": "group1"},
        {
            "type": "group",
            "id": "group2"}
    ]
}
url = f"https://www.virustotal.com/api/v3/threat_profiles/{profile_id}/relationships/{relationship}"
headers = {
    "accept": "application/json","x-apikey": <api-key>
}
response = requests.delete(url, json=payload, headers=headers)
```

Remove access of user1 and members of group1 with viewer privilege to the Threat Profile with 332e02da667746f180a9740e94a3ec98 identifier.

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
response = requests.delete(url, json=payload, headers=headers)
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
      "delete": {
        "tags": [
          "Threat Profiles"
        ],
        "description": "",
        "operationId": "delete-threat-profile-relationships",
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
        "summary": "Delete items from a Threat Profile"
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

← [Get object descriptors related to a Threat Profile](get-threat-profile-related-descriptors.md) · [up](../README.md) · [Add or update relationships between a Threat Profile and other objects](add-threat-profile-relationships.md) →

*Archived from <https://gtidocs.virustotal.com/reference/delete-threat-profile-relationships>.*
