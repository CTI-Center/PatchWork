---
title: "🔀 revoking_technique"
source: https://gtidocs.virustotal.com/reference/revoking_technique
slug: revoking_technique
section: reference
group: "API OBJECTS"
updatedAt: 2025-12-01T16:15:59.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Attack Techniques](../object-attack-techniques.md) › 🔀 revoking_technique

---

# 🔀-revoking_technique

Attack technique's revoking technique.

The *revoking\_technique* relationship returns the ***attack technique revoking a technique***.

This relationship can be retrieved using the [relationships API](../../03-ioc-investigation/attack-techniques/attack_techniqueidrelationship.md) endpoint. The response contains a [Attack Technique](../object-attack-techniques.md) object (or none if the technique is not revoked).

```json /attack_techniques/{id}/revoking_technique
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
          "macOS"
        ],
        "x_mitre_is_subtechnique": true,
        "x_mitre_permissions_required": [
          "User",
          "Administrator"
        ],
        "x_mitre_version": "1.0",
        "x_mitre_data_sources": [
          "Process use of network",
          "Process command-line parameters",
          "Process monitoring",
          "File monitoring"
        ],
        "x_mitre_detection": "While users may customize their ~/.bashrc and ~/.bash_profile files , there are only certain types of commands that typically appear in these files. Monitor for abnormal commands such as execution of unknown programs, opening network sockets, or reaching out across the network when user profiles are loaded during the login process."
      },
      "revoked": false,
      "name": ".bash_profile and .bashrc",
      "creation_date": 1579875225,
      "link": "https://attack.mitre.org/techniques/T1546/004/",
      "stix_id": "attack-pattern--b63a34e8-0a61-4c97-a23b-bf8a2ed812e2",
      "last_modification_date": 1585067284,
      "description": "Adversaries may establish persistence by executing malicious content triggered by a user’s shell. ~/.bash_profile and ~/.bashrc are shell scripts that contain shell commands. These files are executed in a user's context when a new shell opens or when a user logs in so that their environment is set correctly.\n~/.bash_profile is executed for login shells and ~/.bashrc is executed for interactive non-login shells. This means that when a user logs in (via username and password) to the console (either locally or remotely via something like SSH), the ~/.bash_profile script is executed before the initial command prompt is returned to the user. After that, every time a new shell is opened, the ~/.bashrc script is executed. This allows users more fine-grained control over when they want certain commands executed. These shell scripts are meant to be written to by the local user to configure their own environment.\nThe macOS Terminal.app is a little different in that it runs a login shell by default each time a new terminal window is opened, thus calling ~/.bash_profile each time instead of ~/.bashrc.\nAdversaries may abuse these shell scripts by inserting arbitrary shell commands that may be used to execute other binaries to gain persistence. Every time the user logs in or opens a new shell, the modified ~/.bash_profile and/or ~/.bashrc scripts will be executed."
    },
    "type": "attack_technique",
    "id": "T1546.004",
    "links": {
      "self": "https://www.virustotal.com/api/v3/attack_techniques/T1546.004"
    }
  },
  "links": {
    "self": "https://www.virustotal.com/api/v3/attack_techniques/T1156/revoking_technique"
  }
}
```

---

← [🔀 parent_technique](parent_technique.md) · [up](../README.md) · [🔀 subtechniques](subtechniques.md) →

*Archived from <https://gtidocs.virustotal.com/reference/revoking_technique>.*
