---
title: "Delete a Threat Profile"
source: https://gtidocs.virustotal.com/reference/delete-threat-profile
slug: delete-threat-profile
section: reference
group: "Global Landscape"
updatedAt: 2026-06-05T14:43:03.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Global Landscape](../README.md) › [Threat Profiles](../threat-profiles.md) › Delete a Threat Profile

---

# delete-a-threat-profile

Use this endpoint to delete a certain [Threat Profile](../../17-api-objects/threat-profile-object.md) object.

Only **owners** and **editors** can delete a threat profile, although [users privileges can be changed](add-threat-profile-relationships.md) by other owners or editors of the Threat Profile.

## examples

Delete my Threat Profiles with 451b02d448354f08ba5f179998f336e2 identifier.

```python
import requests

profile_id = "451b02d448354f08ba5f179998f336e2"
url = f"https://www.virustotal.com/api/v3/threat_profiles/{profile_id}"
headers = {
    "accept": "application/json","x-apikey": <api-key>
}
response = requests.delete(url, headers=headers)
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
      "delete": {
        "tags": [
          "Threat Profiles"
        ],
        "description": "",
        "operationId": "delete-threat-profile",
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
        "summary": "Delete a Threat Profile"
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

← [Update a Threat Profiles](update-threat-profile.md) · [up](../README.md) · [Get recommendations of a Threat Profile](get-threat-profile-recommendations.md) →

*Archived from <https://gtidocs.virustotal.com/reference/delete-threat-profile>.*
