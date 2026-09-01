---
title: "🔀 threat_actors"
source: https://gtidocs.virustotal.com/reference/attack-techniques-threat_actors
slug: attack-techniques-threat_actors
section: reference
group: "API OBJECTS"
updatedAt: 2025-12-01T16:16:16.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Attack Techniques](../object-attack-techniques.md) › 🔀 threat_actors

---

# 🔀-threat_actors

Attack technique's threat actors

The *threat\_actors* relationship returns the list of ***all threat actors where this technique appears***.

This relationship can be retrieved using the [relationships API](../../03-ioc-investigation/attack-techniques/attack_techniqueidrelationship.md) endpoint. The response contains a list of [Threat Actor](../threat-actor-object.md) objects.

```json /attack_techniques/{id}/threat_actors
{
  "data": [
    <THREAT_ACTOR_OBJECT>,
    <THREAT_ACTOR_OBJECT>,
    ...
  ],
  "links": {
    "next": <string>,
    "self": <string>
  },
  "meta": {
    "count": <int>,
    "cursor": <string>
  }
}
```
```json Example
{
  "meta": {
    "count": 2,
    "cursor": "eyJsaW1pdCI6IDEsICJvZmZzZXQiOiAxfQ=="
  },
  "data": [
    {
      "attributes": {
        "info": {
          "synonyms": [
            "Palmetto Fusion",
            "Allanite"
          ],
          "since": "2017",
          "refs": [
            "https://dragos.com/adversaries.html",
            "https://dragos.com/blog/20180510Allanite.html"
          ],
          "victimology": "Electric utilities, US and UK",
          "mode-of-operation": "Watering-hole and phishing leading to ICS recon and screenshot collection",
          "capabilities": "Powershell scripts, THC Hydra, SecretsDump, Inveigh, PSExec"
        },
        "link": "https://www.misp-project.org/galaxy.html#_allanite",
        "uuid": "a9000eaf-2b75-4ec7-8dcf-fe1bb5c77470",
        "name": "ALLANITE",
        "description": "Adversaries abusing ICS (based on Dragos Inc adversary list).\nALLANITE accesses business and industrial control (ICS) networks, conducts reconnaissance, and gathers intelligence in United States and United Kingdom electric utility sectors. Dragos assesses with moderate confidence that ALLANITE operators continue to maintain ICS network access to: (1) understand the operational environment necessary to develop disruptive capabilities, (2) have ready access from which to disrupt electric utilities.\nALLANITE uses email phishing campaigns and compromised websites called watering holes to steal credentials and gain access to target networks, including collecting and distributing screenshots of industrial control systems. ALLANITE operations limit themselves to information gathering and have not demonstrated any disruptive or damaging capabilities.\nALLANITE conducts malware-less operations primarily leveraging legitimate and available tools in the Windows operating system."
      },
      "type": "threat_actor",
      "id": "allanite",
      "links": {
        "self": "https://www.virustotal.com/api/v3/threat_actors/allanite"
      }
    }
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/attack_techniques/T1548/threat_actors?limit=10"
  }
}
```

---

← [🔀 subtechniques](subtechniques.md) · [up](../README.md) · [Campaign](../campaign-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/attack-techniques-threat_actors>.*
