---
title: "🔀 parent_technique"
source: https://gtidocs.virustotal.com/reference/parent_technique
slug: parent_technique
section: reference
group: "API OBJECTS"
updatedAt: 2025-12-01T16:15:51.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Attack Techniques](../object-attack-techniques.md) › 🔀 parent_technique

---

# 🔀-parent_technique

Attack technique's parent technique.

The *parent\_technique* relationship returns the ***technique's parent technique***.

This relationship can be retrieved using the [relationships API](../../03-ioc-investigation/attack-techniques/attack_techniqueidrelationship.md) endpoint. The response contains a [Attack Technique](../object-attack-techniques.md) object (or none if the technique is not a sub-technique).

```json /attack_techniques/{id}/parent_technique
{
  "data": <ATTACK_TECHNIQUE_OBJECT>,
  "links": {
    "self": <string>
  },
  "meta": {
    "count": <int>
  }
}
```
```json Example
{
  "meta": {
    "count": 1
  },
  "data": {
    "attributes": {
      "info": {
        "x_mitre_platforms": [
          "Linux",
          "macOS",
          "Windows"
        ],
        "x_mitre_is_subtechnique": false,
        "x_mitre_permissions_required": [
          "Administrator",
          "User"
        ],
        "x_mitre_version": "1.0",
        "x_mitre_data_sources": [
          "Windows Registry",
          "File monitoring",
          "Process command-line parameters",
          "API monitoring",
          "Process monitoring"
        ],
        "x_mitre_detection": "Monitor the file system for files that have the setuid or setgid bits set. Also look for any process API calls for behavior that may be indicative of Process Injection and unusual loaded DLLs through DLL Search Order Hijacking, which indicate attempts to gain access to higher privileged processes. On Linux, auditd can alert every time a user's actual ID and effective ID are different (this is what happens when you sudo).\nConsider monitoring for /usr/libexec/security_authtrampoline executions which may indicate that AuthorizationExecuteWithPrivileges is being executed. MacOS system logs may also indicate when AuthorizationExecuteWithPrivileges is being called. Monitoring OS API callbacks for the execution can also be a way to detect this behavior but requires specialized security tooling.\nOn Linux, auditd can alert every time a user's actual ID and effective ID are different (this is what happens when you sudo). This technique is abusing normal functionality in macOS and Linux systems, but sudo has the ability to log all input and output based on the LOG_INPUT and LOG_OUTPUT directives in the /etc/sudoers file.\nThere are many ways to perform UAC bypasses when a user is in the local administrator group on a system, so it may be difficult to target detection on all variations. Efforts should likely be placed on mitigation and collecting enough information on process launches and actions that could be performed before and after a UAC bypass is performed. Some UAC bypass methods rely on modifying specific, user-accessible Registry settings. Analysts should monitor Registry settings for unauthorized changes."
      },
      "revoked": false,
      "name": "Abuse Elevation Control Mechanism",
      "creation_date": 1580392694,
      "link": "https://attack.mitre.org/techniques/T1548/",
      "stix_id": "attack-pattern--67720091-eee3-4d2d-ae16-8264567f6f5b",
      "last_modification_date": 1595453812,
      "description": "Adversaries may circumvent mechanisms designed to control elevate privileges to gain higher-level permissions. Most modern systems contain native elevation control mechanisms that are intended to limit privileges that a user can perform on a machine. Authorization has to be granted to specific users in order to perform tasks that can be considered of higher risk. An adversary can perform several methods to take advantage of built-in control mechanisms in order to escalate privileges on a system."
    },
    "type": "attack_technique",
    "id": "T1548",
    "links": {
      "self": "https://www.virustotal.com/api/v3/attack_techniques/T1548"
    }
  },
  "links": {
    "self": "https://www.virustotal.com/api/v3/attack_techniques/T1548.001/parent_technique"
  }
}
```

---

← [🔀 attack_tactics](attack_tactics.md) · [up](../README.md) · [🔀 revoking_technique](revoking_technique.md) →

*Archived from <https://gtidocs.virustotal.com/reference/parent_technique>.*
