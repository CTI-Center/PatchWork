---
title: "Get a Threat Profile's recommendations descriptors"
source: https://gtidocs.virustotal.com/reference/get-threat-profile-recommendations-descriptors
slug: get-threat-profile-recommendations-descriptors
section: reference
group: "Global Landscape"
updatedAt: 2026-06-05T14:43:11.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Global Landscape](../README.md) › [Threat Profiles](../threat-profiles.md) › Get a Threat Profile's recommendations descriptors

---

# get-a-threat-profile's-recommendations-descriptors

This endpoint is the same as [/threat\_profiles/{profile\_id}/recommendations](get-threat-profile-recommendations.md) except it returns just the list of objects descriptors instead of returning complete objects with their attributes.

## examples

Get 10 objects descriptors associated to the Threat Profile 332e02da667746f180a9740e94a3ec98.

```python
import requests

profile_id = "332e02da667746f180a9740e94a3ec98"
url = f"https://www.virustotal.com/api/v3/threat_profiles/{profile_id}/relationships/recommendations?limit=10"
headers = {"accept": "application/json","x-apikey": <api-key>}

response = requests.get(url, headers=headers)
```

Get only descriptors of automatically generated recommendations of the Threat Profile 332e02da667746f180a9740e94a3ec98.

```python
import requests

profile_id = "332e02da667746f180a9740e94a3ec98"
filter = "recommendation_source:SOURCE_RECOMMENDATION"
url = f"https://www.virustotal.com/api/v3/threat_profiles/{profile_id}/relationships/recommendations?filter={filter}"
headers = {"accept": "application/json","x-apikey": <api-key>}

response = requests.get(url, headers=headers)
```

Get only objects descriptors added by users to the Threat Profile 332e02da667746f180a9740e94a3ec98.

```python
import requests

profile_id = "332e02da667746f180a9740e94a3ec98"
filter = "recommendation_source:SOURCE_DIRECT_FOLLOW"
url = f"https://www.virustotal.com/api/v3/threat_profiles/{profile_id}/relationships/recommendations?filter={filter}"
headers = {"accept": "application/json","x-apikey": <api-key>}

response = requests.get(url, headers=headers)
```

Get only objects descriptors observed by your connector to the Threat Profile 332e02da667746f180a9740e94a3ec98.

```python
import requests

profile_id = "332e02da667746f180a9740e94a3ec98"
filter = "recommendation_source:SOURCE_OBSERVED"
url = f"https://www.virustotal.com/api/v3/threat_profiles/{profile_id}/relationships/recommendations?filter={filter}"
headers = {"accept": "application/json","x-apikey": <api-key>}

response = requests.get(url, headers=headers)
```

Get only malware fammilies descriptors associated to the Threat Profile 332e02da667746f180a9740e94a3ec98.

```python
import requests

profile_id = "332e02da667746f180a9740e94a3ec98"
filter = "collection_type:malware-family"
url = f"https://www.virustotal.com/api/v3/threat_profiles/{profile_id}/relationships/recommendations?filter={filter}"
headers = {"accept": "application/json","x-apikey": <api-key>}

response = requests.get(url, headers=headers)
```

Get only automatically generated recommendations descriptors of threat actors of the Threat Profile 332e02da667746f180a9740e94a3ec98.

```python
import requests

profile_id = "332e02da667746f180a9740e94a3ec98"
filter = "recommendation_source:SOURCE_RECOMMENDATION AND collection_type:threat-actor"
url = f"https://www.virustotal.com/api/v3/threat_profiles/{profile_id}/relationships/recommendations?filter={filter}"
headers = {"accept": "application/json","x-apikey": <api-key>}

response = requests.get(url, headers=headers)
```

Get only vulnerabilities and campaign descriptors associated to the Threat Profile 332e02da667746f180a9740e94a3ec98.

```python
import requests

profile_id = "332e02da667746f180a9740e94a3ec98"
filter = "collection_type:report OR collection_type:vulnerability"
url = f"https://www.virustotal.com/api/v3/threat_profiles/{profile_id}/relationships/recommendations?filter={filter}"
headers = {"accept": "application/json","x-apikey": <api-key>}

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
    "/threat_profiles/{profile_id}/relationships/recommendations": {
      "get": {
        "tags": [
          "Threat Profiles"
        ],
        "description": "",
        "operationId": "get-threat-profile-recommendations-descriptors",
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
            "description": "Maximum number of objects to retrieve (max 40)",
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
            "description": "Filter threats / objects by different properties",
            "in": "query",
            "name": "filter",
            "schema": {
              "type": "string"
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
        "summary": "Get a Threat Profile's recommendations descriptors"
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

← [Get recommendations of a Threat Profile](get-threat-profile-recommendations.md) · [up](../README.md) · [Delete objects from a Threat Profile](delete-threat-profile-recommendations.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-threat-profile-recommendations-descriptors>.*
