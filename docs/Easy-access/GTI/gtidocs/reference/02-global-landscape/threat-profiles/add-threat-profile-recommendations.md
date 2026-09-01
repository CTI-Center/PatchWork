---
title: "Add objects to a Threat Profile"
source: https://gtidocs.virustotal.com/reference/add-threat-profile-recommendations
slug: add-threat-profile-recommendations
section: reference
group: "Global Landscape"
updatedAt: 2026-06-05T14:43:26.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Global Landscape](../README.md) › [Threat Profiles](../threat-profiles.md) › Add objects to a Threat Profile

---

# add-objects-to-a-threat-profile

Use this endpoint to add Threat objects ([Threat Actors](../../17-api-objects/threat-actor-object.md), [Malware Families](../../17-api-objects/malware-family-object.md), [Software or Toolkits](../../17-api-objects/software-toolkit-object.md), [Campaigns](../../17-api-objects/campaign-object.md), [IoC Collections](../../17-api-objects/ioc-collection-object.md), [Reports](../../17-api-objects/report-object.md) and [Vulnerabilities](../../17-api-objects/vulnerability-object.md)) to a certain Threat Profile.

This endpoint requires objects' descriptors and the user to be the **owner** or an **editor** of the Threat Profile.

## examples

Add the IoC collection with alienvault\_6603ebc9f7d8b30ccfe70c54 identifier and the cve-2024-11820 vulnerability to the 332e02da667746f180a9740e94a3ec98 Threat Profile.

```python
import requests

profile_id = "332e02da667746f180a9740e94a3ec98"
payload = {
    "data":[
        {
            "type": "collection",
            "id": "alienvault_6603ebc9f7d8b30ccfe70c54"},
        {
            "type": "collection",
            "id": "vulnerability--cve-2024-11820"}
    ]
}
url = f"https://www.virustotal.com/api/v3/threat_profiles/{profile_id}/relationships/recommendations"
headers = {
    "accept": "application/json",
    "x-apikey": <api-key>, 
    "content-type": "application/json"
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
    "/threat_profiles/{profile_id}/relationships/recommendations": {
      "post": {
        "tags": [
          "Threat Profiles"
        ],
        "description": "",
        "operationId": "add-threat-profile-recommendations",
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
        "summary": "Add objects to a Threat Profile"
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

← [Delete objects from a Threat Profile](delete-threat-profile-recommendations.md) · [up](../README.md) · [Get objects related to a Threat Profile](get-threat-profile-relationships.md) →

*Archived from <https://gtidocs.virustotal.com/reference/add-threat-profile-recommendations>.*
