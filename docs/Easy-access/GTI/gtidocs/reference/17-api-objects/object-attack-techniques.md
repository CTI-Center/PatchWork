---
title: "Attack Techniques"
source: https://gtidocs.virustotal.com/reference/object-attack-techniques
slug: object-attack-techniques
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:39:43.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Attack Techniques

---

# attack-techniques

Information about attack techniques

An attack technique object represents a MITRE ATT\&CK's adversary technique.\
The ID of these objects are equivalent to their corresponding ATT\&CK Technique's ID (e.g. [T1110](https://attack.mitre.org/techniques/T1110/) , [T1110.001](https://attack.mitre.org/techniques/T1110/001/))

## object-attributes

An Attack Technique object contains the following attributes:

* `creation_date`: <*integer*> creation date of the attack technique (UTC timestamp).
* `description`: <*string*> technique's description.
* `info`: <*dictionary*> technique's additional info. The possible fields inside the dictionary are:
  * `x_mitre_detection`: <*string*> strategies for identifying if a technique has been used by an adversary.
  * `x_mitre_platforms`: <*list of strings*> list of platforms that apply to the technique.
  * `x_mitre_data_sources`: <*list of strings*> sources of information that may be used to identify the action or result of the action being performed.
  * `x_mitre_is_subtechnique`: <*boolean*> if true, this technique has sub-techniques. Refer to the subtechniques relationship for more information.
  * `x_mitre_system_requirements`: <*string*> additional information on requirements the adversary needs to meet or about the state of the system (software, patch level, etc.) that may be required for the technique to work.
  * `x_mitre_tactic_type`: <*string*> "Post-Adversary Device Access", "Pre-Adversary Device Access", or "Without Adversary Device Access".
  * `x_mitre_permissions_required`: <*list of strings*> the lowest level of permissions the adversary is required to be operating within to perform the technique on a system.
  * `x_mitre_effective_permissions`: <*list of strings*> the level of permissions the adversary will attain by performing the technique.
  * `x_mitre_defense_bypassed`: <*list of strings*> list of defensive tools, methodologies, or processes the technique can bypass.
  * `x_mitre_remote_support`: <*boolean*> if true, the technique can be used to execute something on a remote system.
  * `x_mitre_impact_type`: <*list of strings*> denotes if the technique can be used for integrity or availability attacks.
  * `x_mitre_version`: <*string*> the version of the object in format major.minor where major and minor are integers. ATT\&CK increments this version number when the object content is updated.
  * `x_mitre_contributors`: <*list of strings*> people and organizations who have contributed to the object.
  * `x_mitre_deprecated`: <*boolean*> marked as deprecated. There is not a revoking technique replacing this one.
  * `x_mitre_old_attack_id`: <*string*> old ATT\&CK ID.
  * `x_mitre_network_requirements`: <*boolean*> requires network to execute the technique.
* `last_modification_date`: <*integer*> date when the technique's was last updated (UTC timestamp).
* `link`: <*string*> URL of the technique on MITRE's website.
* `name`: <*string*> technique's name.
* `revoked`: <*boolean*> indicates if the technique has been revoked. If a technique has been revoked you can retrieve the new technique using the [revoking\_technique](object-attack-techniques/revoking_technique.md) relationship.
* `stix_id`: <*string*> technique's STIX ID.

```json Attack technique object
{
  "data": {
    "attributes": {
      "info": <dictionary>,
      "revoked": <boolean>,
      "name": <string>,
      "creation_date": <int:timestamp>,
      "link": <string>,
      "stix_id": <string>,
      "last_modification_date": <int:timestamp>,
      "description": <string>,
    },
    "type": "attack_technique",
    "id": <string>,
    "links": {
      "self": "https://www.virustotal.com/api/v3/attack_techniques/<id>"
    }
  }
}
```
```json Example
{
  "data": {
    "attributes": {
      "info": {
        "x_mitre_contributors": [
          "Blake Strom, Microsoft 365 Defender"
        ],
        "x_mitre_platforms": [
          "Windows",
          "Azure AD"
        ],
        "x_mitre_is_subtechnique": true,
        "x_mitre_permissions_required": [
          "Administrator"
        ],
        "x_mitre_version": "1.0",
        "x_mitre_data_sources": [
          "Windows event logs",
          "PowerShell logs",
          "Azure activity logs"
        ],
        "x_mitre_detection": "Monitor for modifications to domain trust settings, such as when a user or application modifies the federation settings on the domain or updates domain authentication from Managed to Federated via ActionTypes Set federation settings on domain and Set domain authentication. This may also include monitoring for Event ID 307 which can be correlated to relevant Event ID 510 with the same Instance ID for change details.\nMonitor for PowerShell commands such as: Update-MSOLFederatedDomain –DomainName: \"Federated Domain Name\", or Update-MSOLFederatedDomain –DomainName: \"Federated Domain Name\" –supportmultipledomain."
      },
      "revoked": false,
      "name": "Domain Trust Modification",
      "creation_date": 1609192742,
      "link": "https://attack.mitre.org/techniques/T1484/002/",
      "stix_id": "attack-pattern--24769ab5-14bd-4f4e-a752-cfb185da53ee",
      "last_modification_date": 1610389280,
      "description": "Adversaries may add new domain trusts or modify the properties of existing domain trusts to evade defenses and/or elevate privileges. Domain trust details, such as whether or not a domain is federated, allow authentication and authorization properties to apply between domains for the purpose of accessing shared resources. These trust objects may include accounts, credentials, and other authentication material applied to servers, tokens, and domains.\nManipulating the domain trusts may allow an adversary to escalate privileges and/or evade defenses by modifying settings to add objects which they control. For example, this may be used to forge SAML Tokens, without the need to compromise the signing certificate to forge new credentials. Instead, an adversary can manipulate domain trusts to add their own signing certificate."
    },
    "type": "attack_technique",
    "id": "T1484.002",
    "links": {
      "self": "https://www.virustotal.com/api/v3/attack_techniques/T1484.002"
    }
  }
}
```

## relationships

In addition to the previously described attributes, attack technique objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../01-api-introduction/api-responses/introduction-relationships.md)  section.

The following table shows a summary of available relationships.

| Relationship        | Return object type                                                   |
| :------------------ | :------------------------------------------------------------------- |
| attack\_tactics     | List of [Attack Tactics](../03-ioc-investigation/attack-tactics.md)                         |
| parent\_technique   | A single [Attack Technique](object-attack-techniques.md)            |
| revoking\_technique | A single [Attack Technique](object-attack-techniques.md)            |
| subtechniques       | List of [Attack Techniques](object-attack-techniques.md)            |
| threat\_actors      | List of collections of type [Threat Actors](threat-actor-object.md) |

---

← [🔀 attack_techniques](object-attack-tactics/attack_techniques.md) · [up](README.md) · [🔀 attack_tactics](object-attack-techniques/attack_tactics.md) →

*Archived from <https://gtidocs.virustotal.com/reference/object-attack-techniques>.*
