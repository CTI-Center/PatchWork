---
title: "🔀 related_threat_actors"
source: https://gtidocs.virustotal.com/reference/urls-object-related_threat_actors
slug: urls-object-related_threat_actors
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:45:45.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [URLs](../url-object.md) › 🔀 related_threat_actors

---

# 🔀-related_threat_actors

Related Threat Actors for a given URL.

The *related\_threat\_actors* relationship returns a list of ***threat actors related to the URL***.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/urls/urls-relationships.md). The response contains a list of [Threat Actors](../threat-actor-object.md) objects.

```json /urls/{url_id}/related_threat_actors
{
    "meta": {
        "count": <int>
    },
    "data": [
        {
            "attributes": {
								...
            },
            "type": "threat_actor",
            "id": <string>,
            "context_attributes": {
                "related_from": [
                    {
                        "type": <string>,
                        "id": <string>
                    }
                ]
            }
        },
        {
            "attributes": {
                ...
            },
            "type": "threat_actor",
            "id": <string>,
            "context_attributes": {
                "related_from": [
                    {
                        "type": <string>,
                        "id": <string>
                    }
                ]
            }
        }
    ],
}
```
```json Example
{
	"meta": {
		"count": 2
	},
	"data": [
		{
			"attributes": {
				"first_seen_date": 1176409557,
				"description": "GOLD CABIN is a financially motivated cybercriminal threat group operating a malware distribution service on behalf of numerous customers since 2018. GOLD CABIN uses malicious documents, often contained in password-protected archives, delivered through email to download and execute payloads. The second-stage payloads are most frequently Gozi ISFB (Ursnif) or IcedID (Bokbot), sometimes using intermediary malware like Valak. GOLD CABIN infrastructure relies on artificial appearing and frequently changing URLs created with a domain generation algorithm (DGA). The URLs host a PHP object that returns the malware as a DLL file.",
				"targeted_regions": [],
				"last_seen_date": 1658647885,
				"related_entities_count": 61207,
				"targeted_industries": [],
				"last_modification_date": 1658732412,
				"aliases": [
					"Shakthak",
					"TA551",
					"ATK236",
					"G0127",
					"Monster Libra",
					"GOLD CABIN",
					"Shathak"
				],
				"name": "GOLD CABIN"
			},
			"type": "threat_actor",
			"id": "36e8c848-4d20-47ea-9fc2-31aa17bf82d1",
			"links": {
				"self": "https://www.virustotal.com/api/v3/threat_actors/36e8c848-4d20-47ea-9fc2-31aa17bf82d1"
			},
			"context_attributes": {
				"related_from": [
					{
						"attributes": {
							"name": "Emotet"
						},
						"type": "collection",
						"id": "malpedia_win_emotet"
					}
				]
			}
		},
		{
			"attributes": {
				"first_seen_date": 1176409557,
				"description": "MUMMY SPIDER is a criminal entity linked to the core development of the malware most commonly known as Emotet or Geodo. First observed in mid-2014, this malware shared code with the Bugat (aka Feodo) banking Trojan. However, MUMMY SPIDER swiftly developed the malware’s capabilities to include an RSA key exchange for command and control (C2) communication and a modular architecture.\nMUMMY SPIDER does not follow typical criminal behavioral patterns. In particular, MUMMY SPIDER usually conducts attacks for a few months before ceasing operations for a period of between three and 12 months, before returning with a new variant or version.\nAfter a 10 month hiatus, MUMMY SPIDER returned Emotet to operation in December 2016 but the latest variant is not deploying a banking Trojan module with web injects, it is currently acting as a ‘loader’ delivering other malware packages. The primary modules perform reconnaissance on victim machines, drop freeware tools for credential collection from web browsers and mail clients and a spam plugin for self-propagation. The malware is also issuing commands to download and execute other malware families such as the banking Trojans Dridex and Qakbot.\n MUMMY SPIDER advertised Emotet on underground forums until 2015, at which time it became private. Therefore, it is highly likely that Emotet is operate",
				"targeted_regions": [],
				"last_seen_date": 1658495135,
				"related_entities_count": 55356,
				"targeted_industries": [],
				"last_modification_date": 1658732413,
				"aliases": [
					"TA542",
					"GOLD CRESTWOOD"
				],
				"name": "MUMMY SPIDER"
			},
			"type": "threat_actor",
			"id": "c93281be-f6cd-4cd0-a5a3-defde9d77d8b",
			"links": {
				"self": "https://www.virustotal.com/api/v3/threat_actors/c93281be-f6cd-4cd0-a5a3-defde9d77d8b"
			},
			"context_attributes": {
				"related_from": [
					{
						"attributes": {
							"name": "Emotet"
						},
						"type": "collection",
						"id": "malpedia_win_emotet"
					}
				]
			}
		}
	],
	"links": {
		"self": "https://www.virustotal.com/api/v3/urls/9a99a24b65c8336298d5dcd773303675c0fa79fd53f6ec19da03588ddb57836a/related_threat_actors?limit=10"
	}
}
```

---

← [🔀 collections](urls-object-collections.md) · [up](../README.md) · [File Analyses](../file-analysis-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/urls-object-related_threat_actors>.*
