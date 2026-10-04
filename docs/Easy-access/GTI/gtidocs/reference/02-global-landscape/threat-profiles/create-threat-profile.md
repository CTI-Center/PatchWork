---
title: "Create a Threat Profile"
source: https://gtidocs.virustotal.com/reference/create-threat-profile
slug: create-threat-profile
section: reference
group: "Global Landscape"
updatedAt: 2026-06-05T14:42:35.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Global Landscape](../README.md) › [Threat Profiles](../threat-profiles.md) › Create a Threat Profile

---

# create-a-threat-profile

Use this endpoint to create a new [**Threat Profile**](../../17-api-objects/threat-profile-object.md). All threat profiles are visible to all the members of your group, but only **owners** and **editors** can edit them.

You can share the Threat Profiles with other users and groups and [give them **viewer** or **editor** privileges](add-threat-profile-relationships.md).

In the request body, send a threat profile object containing its name and **interests** as follows:

```json
{
    "data":
    {
        "type": "threat_profile",
        "attributes":
        {
            "name": "<_string_> Threat Profile name",
            "interests":
            {
                "INTEREST_TYPE_TARGETED_INDUSTRY": "<_list of strings_> list of targeted industries. Existing options: Aerospace & Defense, Agriculture, Automotive, Chemicals & Materials, Civil Society & Non-Profits, Construction & Engineering, Education, Energy & Utilities, Financial Services, Government, Healthcare, Hospitality, Insurance, Legal & Professional Services, Manufacturing, Media & Entertainment, Multi-sector, Oil & Gas, Other, Pharmaceuticals, Retail, Technology, Telecommunications, Transportation, Unknown.",
                "INTEREST_TYPE_TARGETED_REGION":"<_list of strings_> list of targeted countries by their ISO-3166 code",
                "INTEREST_TYPE_SOURCE_REGION": "<_list of strings_> list of threats origins by their ISO-3166 country code",
                "INTEREST_TYPE_MALWARE_ROLE": "<_list of strings_> list of malware roles of interest. Existing options: Archiver, ATM Malware, Backdoor - Botnet, Backdoor - Webshell, Backdoor, Bootkit, Builder, Controller, Credential Stealer, Cryptocurrency Miner, Data Miner, Decoder, Disruption Tool, Downloader, Dropper - Memory Only, Dropper, Exploit Builder, Exploit, File Infector, Framework, Installer, Keylogger, Lateral Movement Tool, Launcher, Lightweight Backdoor, Module, Point-of-Sale Malware, Privilege Escalation Tool, Ransomware, Reconnaissance Tool, Remote Control and Administration Tool, Remote Exploitation Tool, Rootkit, Screen Capture Tool, Sniffer, Spambot, Tunneler, Uploader, Utility.",
                "INTEREST_TYPE_ACTOR_MOTIVATION": "<_list of strings_> list of actors’ motivations. Existing options: Attack / Destruction, Espionage, Financial Gain, Hacktivism, Influence, Notoriety, Nuisance, Penetration Testing, Surveillance, Opportunistic."
            }
        }
    }
}
```

## examples

Create a new private Threat Profile to track threat activity generated from Spain with Attack / Destruction and Financial Gain motivations, targeting the Spanish Energy & Utilities and Government institutions via Ransomware campaigns or vulnerability Exploitation.

```python
import requests

url = "https://www.virustotal.com/api/v3/threat_profiles"

payload = {
    "data":
    {
        "type": "threat_profile",
        "attributes":
        {
            "name": "Spanish threat activity",
            "interests":
            {
                "INTEREST_TYPE_TARGETED_INDUSTRY":
                [
                    "Energy & Utilities", "Government"
                ],
                "INTEREST_TYPE_TARGETED_REGION":
                [
                    "ES"
                ],
                "INTEREST_TYPE_SOURCE_REGION":
                [
                    "ES"
                ],
                "INTEREST_TYPE_MALWARE_ROLE":
                [
                    "Exploit", "Ransomware"
                ],
                "INTEREST_TYPE_ACTOR_MOTIVATION":
                [
                    "Attack / Destruction", "Financial Gain"
                ]
            }
        }
    }
}
headers = {
    "accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"
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
    "/threat_profiles": {
      "post": {
        "tags": [
          "Threat Profiles"
        ],
        "description": "",
        "operationId": "create-threat-profile",
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
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "properties": {
                  "data": {
                    "description": "Threat Profile object",
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
                    "value": "{\n    \"data\":\n    {\n        \"id\": \"f05d5de69f044d3bb8533ea43ad75c87\",\n        \"type\": \"threat_profile\",\n        \"links\":\n        {\n            \"self\": \"https://www.virustotal.com/api/v3/threat_profiles/f05d5de69f044d3bb8533ea43ad75c87\"\n        },\n        \"attributes\":\n        {\n            \"interests\":\n            {\n                \"INTEREST_TYPE_TARGETED_INDUSTRY\":\n                [\n                    \"Energy & Utilities\",\n                    \"Government\"\n                ],\n                \"INTEREST_TYPE_TARGETED_REGION\":\n                [\n                    \"ES\"\n                ],\n                \"INTEREST_TYPE_SOURCE_REGION\":\n                [\n                    \"ES\"\n                ],\n                \"INTEREST_TYPE_MALWARE_ROLE\":\n                [\n                    \"Exploit\",\n                    \"Ransomware\"\n                ],\n                \"INTEREST_TYPE_ACTOR_MOTIVATION\":\n                [\n                    \"Attack / Destruction\",\n                    \"Financial Gain\"\n                ]\n            },\n            \"last_modification_date\": 1744787777,\n            \"creation_date\": 1744787775,\n            \"private\": true,\n            \"recommendation_config\":\n            {\n                \"max_recs_per_type\": 10,\n                \"min_categories_matched\": 1,\n                \"max_days_since_last_seen\": 180\n            },\n            \"enable_recommendations\": true,\n            \"name\": \"Spanish threat activity\"\n        },\n        \"context_attributes\":\n        {\n            \"shared_with_me\": false,\n            \"role\": \"owner\"\n        }\n    }\n}"
                  }
                },
                "schema": {
                  "properties": {
                    "data": {
                      "properties": {
                        "attributes": {
                          "properties": {
                            "name": {
                              "type": "string"
                            },
                            "creation_date": {
                              "type": "integer"
                            },
                            "last_modification_date": {
                              "type": "integer"
                            },
                            "private": {
                              "type": "boolean"
                            },
                            "enable_recommendations": {
                              "default": true,
                              "type": "boolean"
                            },
                            "interests": {
                              "properties": {
                                "INTEREST_TYPE_TARGETED_INDUSTRY": {
                                  "items": {
                                    "type": "string"
                                  },
                                  "type": "array"
                                },
                                "INTEREST_TYPE_TARGETED_REGION": {
                                  "items": {
                                    "type": "string"
                                  },
                                  "type": "array"
                                },
                                "INTEREST_TYPE_SOURCE_REGION": {
                                  "items": {
                                    "type": "string"
                                  },
                                  "type": "array"
                                },
                                "INTEREST_TYPE_MALWARE_ROLE": {
                                  "items": {
                                    "type": "string"
                                  },
                                  "type": "array"
                                },
                                "INTEREST_TYPE_ACTOR_MOTIVATION": {
                                  "items": {
                                    "type": "string"
                                  },
                                  "type": "array"
                                }
                              },
                              "type": "object"
                            },
                            "recommendation_config": {
                              "properties": {
                                "max_recs_per_type": {
                                  "default": 10,
                                  "type": "integer"
                                },
                                "min_categories_matched": {
                                  "default": 1,
                                  "type": "integer"
                                },
                                "max_days_since_last_seen": {
                                  "default": 180,
                                  "type": "integer"
                                }
                              },
                              "type": "object"
                            }
                          },
                          "type": "object"
                        },
                        "context_attributes": {
                          "properties": {
                            "shared_with_me": {
                              "type": "boolean"
                            },
                            "role": {
                              "type": "string"
                            }
                          },
                          "type": "object"
                        },
                        "id": {
                          "type": "string"
                        },
                        "links": {
                          "properties": {
                            "self": {
                              "type": "string"
                            }
                          },
                          "type": "object"
                        },
                        "type": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    }
                  },
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
        "summary": "Create a Threat Profile"
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

← [List Threat Profiles](list-threat-profiles.md) · [up](../README.md) · [Get a Threat Profile](get-threat-profile.md) →

*Archived from <https://gtidocs.virustotal.com/reference/create-threat-profile>.*
