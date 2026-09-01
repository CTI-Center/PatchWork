---
title: "Get a Threat Profile's timeline associations"
source: https://gtidocs.virustotal.com/reference/get-threat-profile-timeline-associations
slug: get-threat-profile-timeline-associations
section: reference
group: "Global Landscape"
updatedAt: 2026-06-05T14:44:17.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Global Landscape](../README.md) › [Threat Profiles](../threat-profiles.md) › Get a Threat Profile's timeline associations

---

# get-a-threat-profile's-timeline-associations

Use this endpoint to list a Threat Profile’s timeline associations, with following format:

```json
{
    "data": /* <_list of dictionaries_> list of timeline associations. */
    [
        {
            "id": "<_string_> identifier of the timeline association.",
            "type": "timeline_event",
            "attributes": /* <_dictionary_> attributes of the timeline association. */
            {
                "event_type": "<_string_> the type of the timeline association such as Alias, Motivation, Malware, Actor, Toolkit, Report, Campaign, etc. Available values are listed in the Events filter section below.",
                "event_entity": "<_string_> the name or value of the timeline association like another alias of the main threat actor object associated with a threat profile, or the new motivation of the main threat actor object associated with a threat profile.",
                "first_seen": "<_integer_> Unix epoch UTC time (seconds) when the association between the object and the threat profile was made.",
                "last_seen": "<_integer_> Unix epoch UTC time (seconds) of most recent observed relationship between the object and the threat profile.",
                "name": "<_string_> name of the object directly associated with the threat profile.",
                "link": "<_string_> URL of the object directly associated with the threat profile."
            },
            "context_attributes":
            {
                "collection":
                {
                    "id": "<_string_> identifier of the object directly associated with the threat profile.",
                    "name": "<_string_> name of the object directly associated with the threat profile.",
                    "collection_type": "<_string_> type of the object directly associated with the threat profile.",
                    "origin": "Google Threat Intelligence"
                }
            },
            "links":
            {
                "self": "<_string_> URL to the timeline association."
            },
        },
    ]
}
```

## events-filter

Available events for filtering a Threat Profile’s timeline associations:

**Direct associations**

* Actor - Object associated with the Threat Profile
* Campaign - Object associated with the Threat Profile
* Malware - Object associated with the Threat Profile
* Report - Object associated with the Threat Profile
* Toolkit - Object associated with the Threat Profile
* Vulnerability - Object associated with the Threat Profile

**Indirect associations**

* Merged Actor - Subgroups of the Threat Profile's associated larger Actor groups.

* Suspected Group - Subgroups that are suspected to belong to the Threat Profile's associated larger Actor groups.

* Alias - Aleases of Actors associated with the Threat Profile

* Available Exploit - Available Exploits for Vulnerabilities associated with the Threat Profile

* Exploit State - Exploit State of Vulnerabilities associated with the Threat Profile

* Vulnerability Score - Vulnerability Score of Vulnerabilities associated with the Threat Profile

* Key Event - Key Events of Campaigns associated with the Threat Profile

* Motivation - Motivations of threats associated with the Threat Profile

* Source Region - Source Regions of threats associated with the Threat Profile

* Targeted Region - Targeted Regions by threats associated with the Threat Profile

* Targeted Industry - Targeted Industries by threats associated with the Threat Profile

* Curated Rule - Curated Rules detecting malicious behaviours of threats associated with the Threat Profile

* Hunting Ruleset - Hunting Ruleset detecting malicious behaviours of threats associated with the Threat Profile

* TTP - TTPs of objects associated with the Threat Profile

* X509 - X509 certificates related with threats associated with the Threat Profile

Several event types can be grouped together, separated only by commas (',').

## examples

Get the list of timeline events associated with Threat Profile 332e02da667746f180a9740e94a3ec98.

```python
import requests

profile_id = "332e02da667746f180a9740e94a3ec98"

url = f"https://www.virustotal.com/api/v3/threat_profiles/{profile_id}/timeline/associations"
headers = {
    "accept": "application/json","x-apikey": <api-key>
}
response = requests.get(url, headers=headers)
```

Get 5 timeline events associated with Threat Profile 332e02da667746f180a9740e94a3ec98 between 2024-01-01 and 2025-01-01 UTC.

```python
import requests

profile_id = "332e02da667746f180a9740e94a3ec98"
limit = 5
later_than = 1704067200
before_than = 1735689600

url = f"https://www.virustotal.com/api/v3/threat_profiles/{profile_id}/timeline/associations?limit={limit}&later_than={later_than}&before_than={before_than}"
headers = {
    "accept": "application/json","x-apikey": <api-key>
}
response = requests.get(url, headers=headers)
```

Get only Actor and Motivation timeline events associated with Threat Profile 332e02da667746f180a9740e94a3ec98.

```python
import requests

profile_id = "332e02da667746f180a9740e94a3ec98"
events = "Actor,Motivation,Merged Actor"

url = f"https://www.virustotal.com/api/v3/threat_profiles/{profile_id}/timeline/associations?events={events}"
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
    "/threat_profiles/{profile_id}/timeline/associations": {
      "get": {
        "tags": [
          "Threat Profiles"
        ],
        "description": "",
        "operationId": "get-threat-profile-timeline-associations",
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
            "description": "Threat Prfile's ID",
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
            "description": "Filter timeline associations generated after the specified date (UTC timestamp)",
            "in": "query",
            "name": "later_than",
            "schema": {
              "type": "integer"
            }
          },
          {
            "description": "Filter timeline associations generated before the specified date (UTC timestamp)",
            "in": "query",
            "name": "before_than",
            "schema": {
              "type": "integer"
            }
          },
          {
            "description": "Filter by the type of events of timeline associations",
            "in": "query",
            "name": "events",
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
        "summary": "Get a Threat Profile's timeline associations"
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

← [Add or update relationships between a Threat Profile and other objects](add-threat-profile-relationships.md) · [up](../README.md) · [Export IoCs](threat-profile-download.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-threat-profile-timeline-associations>.*
