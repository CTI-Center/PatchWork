---
title: "Get a summary of all MITRE ATT&CK techniques observed in a file"
source: https://gtidocs.virustotal.com/reference/get-summary-all-mitre-attack-techniques-observed-in-a-file
slug: get-summary-all-mitre-attack-techniques-observed-in-a-file
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:37:09.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private Files Behaviours](../private-files-behaviours.md) › Get a summary of all MITRE ATT&CK techniques observed in a file

---

# get-a-summary-of-all-mitre-att&ck-techniques-observed-in-a-file

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

This endpoint returns a summary of MITRE ATT\&CK tactics and techniques observed in each of the behaviour reports of a file.

The resulting structure is the following one:

```json
{
  sandbox_name: {
    "tactics": [
      {
        "id": tactic_id,
        "name": tactic_name,
        "description": tactic_description,
        "link": tactic_mitre_url,
        "techniques": [
          {
            "id": technique_id,
            "name": technique_name,
            "description": technique_description,
            "link": technique_mitre_url,
            "signatures": [
              {
                "severity": severity ("HIGH" / "MEDIUM" / "LOW" / "INFO" / "UNKNOWN"),
                "description": signature_description
              }, ...
            ]
          }, ...
        ]
      }, ...
    ]
  }, ...  
}
```

```json Example response
{
	"data": {
		"VirusTotal Observer": {
			"tactics": []
		},
		"Zenbox": {
			"tactics": [
				{
					"description": "The adversary is trying to figure out your environment.\n\nDiscovery consists of techniques an adversary may use to gain knowledge about the system and internal network. These techniques help adversaries observe the environment and orient themselves before deciding how to act. They also allow adversaries to explore what they can control and what’s around their entry point in order to discover how it could benefit their current objective. Native operating system tools are often used toward this post-compromise information-gathering objective. ",
					"techniques": [
						{
							"description": "An adversary may attempt to get detailed information about the operating system and hardware, including version, patches, hotfixes, service packs, and architecture. Adversaries may use the information from System Information Discovery during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.\nTools such as Systeminfo can be used to gather detailed system information. If running with privileged access, a breakdown of system data can be gathered through the systemsetup configuration tool on macOS. As an example, adversaries with user-level access can execute the df -aH command to obtain currently mounted disks and associated freely available space. Adversaries may also leverage a Network Device CLI on network devices to gather detailed system information. System Information Discovery combined with information gathered from other forms of discovery and reconnaissance can drive payload development and concealment.\nInfrastructure as a Service (IaaS) cloud providers such as AWS, GCP, and Azure allow access to instance and virtual machine information via APIs. Successful authenticated API calls can return data such as the operating system platform and status of a particular instance or the model view of a virtual machine.",
							"signatures": [
								{
									"severity": "INFO",
									"description": "Reads software policies"
								}
							],
							"link": "https://attack.mitre.org/techniques/T1082/",
							"id": "T1082",
							"name": "System Information Discovery"
						},
						{
							"description": "Adversaries may enumerate files and directories or may search in specific locations of a host or network share for certain information within a file system. Adversaries may use the information from File and Directory Discovery during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.\nMany command shell utilities can be used to obtain this information. Examples include dir, tree, ls, find, and locate. Custom tools may also be used to gather file and directory information and interact with the Native API. Adversaries may also leverage a Network Device CLI on network devices to gather file and directory information.",
							"signatures": [
								{
									"severity": "INFO",
									"description": "Reads ini files"
								}
							],
							"link": "https://attack.mitre.org/techniques/T1083/",
							"id": "T1083",
							"name": "File and Directory Discovery"
						}
					],
					"link": "https://attack.mitre.org/tactics/TA0007/",
					"id": "TA0007",
					"name": "Discovery"
				},
				{
					"description": "The adversary is trying to avoid being detected.\n\nDefense Evasion consists of techniques that adversaries use to avoid detection throughout their compromise. Techniques used for defense evasion include uninstalling/disabling security software or obfuscating/encrypting data and scripts. Adversaries also leverage and abuse trusted processes to hide and masquerade their malware. Other tactics’ techniques are cross-listed here when those techniques include the added benefit of subverting defenses. ",
					"techniques": [
						{
							"description": "Adversaries may inject code into processes in order to evade process-based defenses as well as possibly elevate privileges. Process injection is a method of executing arbitrary code in the address space of a separate live process. Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via process injection may also evade detection from security products since the execution is masked under a legitimate process. \nThere are many different ways to inject code into a process, many of which abuse legitimate functionalities. These implementations exist for every major OS but are typically platform specific. \nMore sophisticated samples may perform multiple process injections to segment modules and further evade detection, utilizing named pipes or other inter-process communication (IPC) mechanisms as a communication channel. ",
							"signatures": [
								{
									"severity": "INFO",
									"description": "Spawns processes"
								}
							],
							"link": "https://attack.mitre.org/techniques/T1055/",
							"id": "T1055",
							"name": "Process Injection"
						},
						{
							"description": "Adversaries may attempt to manipulate features of their artifacts to make them appear legitimate or benign to users and/or security tools. Masquerading occurs when the name or location of an object, legitimate or malicious, is manipulated or abused for the sake of evading defenses and observation. This may include manipulating file metadata, tricking users into misidentifying the file type, and giving legitimate task or service names.\nRenaming abusable system utilities to evade security monitoring is also a form of Masquerading.",
							"signatures": [
								{
									"severity": "INFO",
									"description": "Creates files inside the user directory"
								}
							],
							"link": "https://attack.mitre.org/techniques/T1036/",
							"id": "T1036",
							"name": "Masquerading"
						},
						{
							"description": "Adversaries may delete files left behind by the actions of their intrusion activity. Malware, tools, or other non-native files dropped or created on a system by an adversary (ex: Ingress Tool Transfer) may leave traces to indicate to what was done within a network and how. Removal of these files can occur during an intrusion, or as part of a post-intrusion process to minimize the adversary's footprint.\nThere are tools available from the host operating system to perform cleanup, but adversaries may use other tools as well. Examples of built-in Command and Scripting Interpreter functions include del on Windows and rm or unlink on Linux and macOS.",
							"signatures": [
								{
									"severity": "INFO",
									"description": "Deletes files inside the Windows folder"
								}
							],
							"link": "https://attack.mitre.org/techniques/T1070/004/",
							"id": "T1070.004",
							"name": "File Deletion"
						}
					],
					"link": "https://attack.mitre.org/tactics/TA0005/",
					"id": "TA0005",
					"name": "Defense Evasion"
				},
				{
					"description": "The adversary is trying to gain higher-level permissions.\n\nPrivilege Escalation consists of techniques that adversaries use to gain higher-level permissions on a system or network. Adversaries can often enter and explore a network with unprivileged access but require elevated permissions to follow through on their objectives. Common approaches are to take advantage of system weaknesses, misconfigurations, and vulnerabilities. Examples of elevated access include: \n\n* SYSTEM/root level\n* local administrator\n* user account with admin-like access \n* user accounts with access to specific system or perform specific function\n\nThese techniques often overlap with Persistence techniques, as OS features that let an adversary persist can execute in an elevated context.  ",
					"techniques": [
						{
							"description": "Adversaries may inject code into processes in order to evade process-based defenses as well as possibly elevate privileges. Process injection is a method of executing arbitrary code in the address space of a separate live process. Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via process injection may also evade detection from security products since the execution is masked under a legitimate process. \nThere are many different ways to inject code into a process, many of which abuse legitimate functionalities. These implementations exist for every major OS but are typically platform specific. \nMore sophisticated samples may perform multiple process injections to segment modules and further evade detection, utilizing named pipes or other inter-process communication (IPC) mechanisms as a communication channel. ",
							"signatures": [
								{
									"severity": "INFO",
									"description": "Spawns processes"
								}
							],
							"link": "https://attack.mitre.org/techniques/T1055/",
							"id": "T1055",
							"name": "Process Injection"
						}
					],
					"link": "https://attack.mitre.org/tactics/TA0004/",
					"id": "TA0004",
					"name": "Privilege Escalation"
				}
			]
		},
		"VirusTotal Jujubox": {
			"tactics": []
		}
	},
	"links": {
		"self": "https://www.virustotal.com/api/v3/private/files/bb04b55bc87b4bb4d2543bf50ff46ec840d653ca9311e9b40d9933e484719a91/behaviour_mitre_trees"
	}
}
```

# openapi-definition

```json
{
  "info": {
    "title": "Private Scanning",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Private Files Behaviours"
    }
  ],
  "paths": {
    "/files/{id}/behaviour_mitre_trees": {
      "get": {
        "tags": [
          "Private Files Behaviours"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-summary-all-mitre-attack-techniques-observed-in-a-file",
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
            "description": "File's SHA-256",
            "in": "path",
            "name": "id",
            "required": true,
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
        "summary": "Get a summary of all MITRE ATT&CK techniques observed in a file"
      }
    }
  },
  "security": [],
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3/private"
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

← [Get objects related to a private file's behaviour report](privatefile-behaviourssandbox-idrelationship.md) · [up](../README.md) · [Get a summary of all behavior reports for a file](privatefilesidbehaviour-summary.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-summary-all-mitre-attack-techniques-observed-in-a-file>.*
