---
title: "🔀 attack_techniques"
source: https://gtidocs.virustotal.com/reference/file-behaviour-object-attack-techniques
slug: file-behaviour-object-attack-techniques
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:43:10.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files Behaviour](../file-behaviour-summary-object.md) › 🔀 attack_techniques

---

# 🔀-attack_techniques

File behaviour's ATT&CK techniques

The *attack\_techniques* relationship returns the ***attack techniques observed in the behaviour report***.

This relationship can be retrieved by using the [relationships API endpoint](../../03-ioc-investigation/files-behaviours/file_behaviourssandbox_idrelationship.md). The response contains a list of [attack technique](../object-attack-techniques.md) objects.

Additionally, each related item contains the following context attributes:

* `signatures`: <*list of dictionaries*> behaviours observed in the file where this technique applies. Each of these signatures contains the following subfields:
  * `severity`: <*string*> severity of the behaviour (UNKNOWN, INFO, LOW, MEDIUM or HIGH).
  * `description`: <*string*> description of the behaviour.

```json /file_behaviours/{id}/attack_techniques
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
          "x_mitre_contributors": [
            "Praetorian"
          ],
          "x_mitre_platforms": [
            "Windows",
            "IaaS",
            "Linux",
            "macOS"
          ],
          "x_mitre_is_subtechnique": false,
          "x_mitre_permissions_required": [
            "User"
          ],
          "x_mitre_version": "2.2",
          "x_mitre_data_sources": [
            "Instance: Instance Metadata",
            "Process: Process Creation",
            "Command: Command Execution",
            "Process: OS API Execution"
          ],
          "x_mitre_detection": "System and network discovery techniques normally occur throughout an operation as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities based on the information obtained.\nMonitor processes and command-line arguments for actions that could be taken to gather system and network information. Remote access tools with built-in features may interact directly with the Windows API to gather information. Information may also be acquired through Windows system management tools such as Windows Management Instrumentation and PowerShell.\nIn cloud-based systems, native logging can be used to identify access to certain APIs and dashboards that may contain system information. Depending on how the environment is used, that data alone may not be useful due to benign use during normal operations."
        },
        "revoked": false,
        "name": "System Information Discovery",
        "creation_date": 1496266264,
        "link": "https://attack.mitre.org/techniques/T1082/",
        "stix_id": "attack-pattern--354a7f88-63fb-41b5-a801-ce3b377b36f1",
        "last_modification_date": 1615199581,
        "description": "An adversary may attempt to get detailed information about the operating system and hardware, including version, patches, hotfixes, service packs, and architecture. Adversaries may use the information from System Information Discovery during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.\nTools such as Systeminfo can be used to gather detailed system information. A breakdown of system data can also be gathered through the macOS systemsetup command, but it requires administrative privileges.\nInfrastructure as a Service (IaaS) cloud providers such as AWS, GCP, and Azure allow access to instance and virtual machine information via APIs. Successful authenticated API calls can return data such as the operating system platform and status of a particular instance or the model view of a virtual machine."
      },
      "type": "attack_technique",
      "id": "T1082",
      "links": {
        "self": "https://www.virustotal.com/api/v3/attack_techniques/T1082"
      },
      "context_attributes": {
        "signatures": [
          {
            "description": "Reads software policies",
            "severity": "INFO"
          }
        ]
      }
    },
    {
      "attributes": {
        "info": {
          "x_mitre_contributors": [
            "Deloitte Threat Library Team",
            "Sunny Neo"
          ],
          "x_mitre_defense_bypassed": [
            "Anti-virus",
            "Host forensic analysis",
            "Signature-based detection",
            "Static File Analysis"
          ],
          "x_mitre_platforms": [
            "Windows",
            "macOS",
            "Linux"
          ],
          "x_mitre_is_subtechnique": false,
          "x_mitre_version": "1.2",
          "x_mitre_data_sources": [
            "Process: Process Creation",
            "Command: Command Execution",
            "Process: OS API Execution"
          ],
          "x_mitre_detection": "Virtualization, sandbox, user activity, and related discovery techniques will likely occur in the first steps of an operation but may also occur throughout as an adversary learns the environment. Data and events should not be viewed in isolation, but as part of a chain of behavior that could lead to other activities, such as lateral movement, based on the information obtained. Detecting actions related to virtualization and sandbox identification may be difficult depending on the adversary's implementation and monitoring required. Monitoring for suspicious processes being spawned that gather a variety of system information or perform other forms of Discovery, especially in a short period of time, may aid in detection."
        },
        "revoked": false,
        "name": "Virtualization/Sandbox Evasion",
        "creation_date": 1555539744,
        "link": "https://attack.mitre.org/techniques/T1497/",
        "stix_id": "attack-pattern--82caa33e-d11a-433a-94ea-9b5a5fbef81d",
        "last_modification_date": 1619018170,
        "description": "Adversaries may employ various means to detect and avoid virtualization and analysis environments. This may include changing behaviors based on the results of checks for the presence of artifacts indicative of a virtual machine environment (VME) or sandbox. If the adversary detects a VME, they may alter their malware to disengage from the victim or conceal the core functions of the implant. They may also search for VME artifacts before dropping secondary or additional payloads. Adversaries may use the information learned from Virtualization/Sandbox Evasion during automated discovery to shape follow-on behaviors. \nAdversaries may use several methods to accomplish Virtualization/Sandbox Evasion such as checking for security monitoring tools (e.g., Sysinternals, Wireshark, etc.) or other system artifacts associated with analysis or virtualization. Adversaries may also check for legitimate user activity to help determine if it is in an analysis environment. Additional methods include use of sleep timers or loops within malware code to avoid operating within a temporary sandbox."
      },
      "type": "attack_technique",
      "id": "T1497",
      "links": {
        "self": "https://www.virustotal.com/api/v3/attack_techniques/T1497"
      },
      "context_attributes": {
        "signatures": [
          {
            "description": "May sleep (evasive loops) to hinder dynamic analysis",
            "severity": "INFO"
          }
        ]
      }
    }
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/file_behaviours/00002ead3aa654709a15279462e3ad24fd531d642dd44865af51a5bbf1bc2518_VirusTotal ZenBox/attack_techniques?limit=10"
  }
}
```

---

← [🔀 file](file-behaviour-object-file.md) · [up](../README.md) · [tags](file-behaviour-object-tags.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-behaviour-object-attack-techniques>.*
