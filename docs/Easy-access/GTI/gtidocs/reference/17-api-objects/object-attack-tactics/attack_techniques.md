---
title: "🔀 attack_techniques"
source: https://gtidocs.virustotal.com/reference/attack_techniques
slug: attack_techniques
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T01:01:16.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Attack Tactics](../object-attack-tactics.md) › 🔀 attack_techniques

---

# 🔀-attack_techniques

Attack tactic's techniques.

The *attack\_techniques* relationship returns the list of ***attack techniques belonging to the tactic***.

The relationship can be retrieved using the relationships API endpoint. The response contains a list of [Attack Technique](../object-attack-techniques.md) objects.

```json /attack_tactics/{id}/attack_techniques
{
  "data": [
    <ATTACK_TECHNIQUE_OBJECT>,
    <ATTACK_TECHNIQUE_OBJECT>,
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
    "count": 2
  },
  "data": [
    {
      "attributes": {
        "info": {
          "x_mitre_platforms": [
            "Android"
          ],
          "x_mitre_version": "1.1",
          "x_mitre_tactic_type": [
            "Post-Adversary Device Access"
          ],
          "x_mitre_old_attack_id": "MOB-T1030"
        },
        "revoked": false,
        "name": "Attack PC via USB Connection",
        "creation_date": 1508942893,
        "link": "https://attack.mitre.org/techniques/T1427/",
        "stix_id": "attack-pattern--a0464539-e1b7-4455-a355-12495987c300",
        "last_modification_date": 1549205479,
        "description": "With escalated privileges, an adversary could program the mobile device to impersonate USB devices such as input devices (keyboard and mouse), storage devices, and/or networking devices in order to attack a physically connected PC This technique has been demonstrated on Android. We are unaware of any demonstrations on iOS."
      },
      "type": "attack_technique",
      "id": "T1427",
      "links": {
        "self": "https://www.virustotal.com/api/v3/attack_techniques/T1427"
      }
    },
    {
      "attributes": {
        "info": {
          "x_mitre_platforms": [
            "Android",
            "iOS"
          ],
          "x_mitre_version": "1.0",
          "x_mitre_tactic_type": [
            "Post-Adversary Device Access"
          ],
          "x_mitre_old_attack_id": "MOB-T1031"
        },
        "revoked": false,
        "name": "Exploit Enterprise Resources",
        "creation_date": 1508942893,
        "link": "https://attack.mitre.org/techniques/T1428/",
        "stix_id": "attack-pattern--22379609-a99f-4a01-bd7e-70f3e105859d",
        "last_modification_date": 1539735260,
        "description": "Adversaries may attempt to exploit enterprise servers, workstations, or other resources over the network. This technique may take advantage of the mobile device's access to an internal enterprise network either through local connectivity or through a Virtual Private Network (VPN)."
      },
      "type": "attack_technique",
      "id": "T1428",
      "links": {
        "self": "https://www.virustotal.com/api/v3/attack_techniques/T1428"
      }
    }
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/attack_tactics/TA0033/attack_techniques?limit=10"
  }
}
```

---

← [Attack Tactics](../object-attack-tactics.md) · [up](../README.md) · [Attack Techniques](../object-attack-techniques.md) →

*Archived from <https://gtidocs.virustotal.com/reference/attack_techniques>.*
