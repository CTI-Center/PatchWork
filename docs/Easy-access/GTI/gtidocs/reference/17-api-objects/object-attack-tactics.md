---
title: "Attack Tactics"
source: https://gtidocs.virustotal.com/reference/object-attack-tactics
slug: object-attack-tactics
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:39:40.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Attack Tactics

---

# attack-tactics

Information about attack tactics

An attack tactic object represents a MITRE ATT\&CK's adversary tactic.\
The ID of these objects are equivalent to their corresponding ATT\&CK Tactic's ID (e.g. [TA0043](https://attack.mitre.org/tactics/TA0043/))

## object-attributes

An Attack Tactic object contains the following attributes:

* `creation_date`: <*integer*> creation date of the tactic (UTC timestamp).
* `description`: <*string*> tactic's description.
* `last_modification_date`: <*integer*> date when the tactic was last updated (UTC timestamp).
* `link`: <*string*>: URL of the tactic on MITRE's website.
* `name`: <*string*>: Tactic's name.
* `stix_id`: <*string*>: Tactic's STIX ID.

```json Attack tactic object
{
  "data": {
    "attributes": {
      "description": <string>,
      "creation_date": <int:timestamp>,
      "link": <string>,
      "stix_id": <string>,
      "last_modification_date": <int:timestamp>,
      "name": <string>
    },
    "type": "attack_tactic",
    "id": <string>,
    "links": {
      "self": "https://www.virustotal.com/api/v3/attack_tactics/{id}"
    }
  }
}
```
```json Example
{
  "data": {
    "attributes": {
      "description": " The adversary is trying to gain higher-level permissions.\n\nPrivilege escalation includes techniques that allow an attacker to obtain a higher level of permissions on the mobile device. Attackers may enter the mobile device with very limited privileges and may be required to take advantage of a device weakness to obtain higher privileges necessary to successfully carry out their mission objectives.",
      "creation_date": 1539735260,
      "link": "https://attack.mitre.org/tactics/TA0029/",
      "stix_id": "x-mitre-tactic--3e962de5-3280-43b7-bc10-334fbc1d6fa8",
      "last_modification_date": 1580133829,
      "name": "Privilege Escalation"
    },
    "type": "attack_tactic",
    "id": "TA0029",
    "links": {
      "self": "https://www.virustotal.com/api/v3/attack_tactics/TA0029"
    }
  }
}
```

## relationships

In addition to the previously described attributes, attack tactic objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../01-api-introduction/api-responses/introduction-relationships.md) section.

The following table shows a summary of available relationships.

| Relationships      | Return object type                                 |
| :----------------- | :------------------------------------------------- |
| attack\_techniques | List of [Attack Techniques](../03-ioc-investigation/attack-techniques.md) |

---

← [🔀 item](analyses-object/item.md) · [up](README.md) · [🔀 attack_techniques](object-attack-tactics/attack_techniques.md) →

*Archived from <https://gtidocs.virustotal.com/reference/object-attack-tactics>.*
