---
title: "Advanced Hunting"
source: https://gtidocs.virustotal.com/docs/use-cases-advanced-hunting
slug: use-cases-advanced-hunting
section: guides
group: "Use Cases & Best Practices"
updatedAt: 2026-01-14T14:15:42.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [Use Cases & Best Practices](../README.md) › [Use cases and other resources](../use-cases.md) › Advanced Hunting

---

# advanced-hunting

Threat hunting stands apart from traditional security methods by being proactive, not reactive. While most security tools wait for an alert, threat hunting actively seeks out threats and suspicious activity that may have slipped past your defenses. This approach is essential for:

* Finding new and unknown threats before they cause damage.
* Spotting suspicious anomalies that might signal a cybercriminal at work.
* Discovering additional malicious artifacts associated with known attackers.

## how-can-google-threat-intelligence-help?

Google Threat Intelligence provides a powerful platform for threat hunters, fueled by a massive, continuously updated database. This data comes from our security partners and, most importantly, our global community. Our hunting capabilities help you:

* Find new, unknown malicious activity and threat actors.
* Spot suspicious anomalies that might be abused by cybercriminals.
* Find additional malicious artifacts used by known attackers.

**LiveHunt** is a service that allows you to monitor the real-time stream of files submitted to Google Threat Intelligence. You can create your own YARA rules, and when a file matches a rule, you'll be notified instantly. This lets you classify new threats by family, discover new malicious IoCs that antivirus engines might have missed, and find files, URLs, IPs or domains with specific properties.

LiveHunt leverages the immense scale of Google's data with the flexibility of YARA, providing the perfect tool for monitoring any new suspicious activity based on your own custom criteria. All matches from the job will appear in your IOC Stream, giving you an immediate view of the results. You can also download matched files for further study, and the entire process can be automated using our [REST API](https://gtidocs.readme.io/reference/ioc-stream).

**RetroHunt** allows you to apply a YARA rule to our extensive historical dataset to discover older versions of attacks. A single RetroHunt job scans over 600 TB of files from the past year, helping you understand how a threat has evolved over time.

You can find detailed information about the creation of YARA rules in the [YARA documentation](https://yara.readthedocs.io/en/latest/writingrules.html).

## use-case

### hunting-for-malware-behavior

Once found suspicious behavior in a malware’s analysis, we can create a YARA rule that matches against it. Use the structure tool to help writing the rule faster, and learn how to tune your rule to reduce noise or false positives.

**How to do it**

| 1. Navigate to the [ruleset creation section](https://yara-editor.virustotal.com/livehunt/new?match_object_type=file) within Google Threat Intelligence.<br>2. Use the **Structure tool** on the left menu, enter a hash of a file you previously analyzed and click on the behaviors you want to match.<br>3. Each click will create a new rule, combine them together to form a comprehensive one.<br>4. Use the Test tool to ensure a match with the original file while excluding any known false positives.<br>5. Save and activate your Livehunt rule. You will receive notifications in IoC Stream and email addresses (if configured), when new samples matching your criteria are observed.<br>```yara<br>import "vt"<br>rule remcos_persistence {<br>condition:<br>for any ips in vt.behaviour.ip_traffic: (<br>ips.destination_ip == "87.120.186.37"<br>) and<br>for any reg_keys in vt.behaviour.registry_keys_set: (<br>reg_keys.key contains "\\Microsoft\\Windows\\CurrentVersion\\Run\"<br>)<br>}<br>```<br>This YARA rule triggers if a file communicates with the selected IP address and modifies a registry whose path contains the specified string. | [GTI Use Case - Hunting for malware behavior](https://www.youtube.com/watch?v=zAyIgg-gVUA) |
| --- | --- |

### uncovering-post-exploitation-threats

Following a patch, it's crucial to check for pre-patch exploitation. Use threat intelligence and detection rules to find indicators of compromise and prevent attackers from maintaining access to your systems.

**How to do it**

| 1. Navigate to the [Campaigns section](https://www.virustotal.com/gui/threat-landscape/campaigns) in Google Threat intelligence<br>2. Search for the software’s name and select a Campaign from the results<br>3. From the campaign's Associations section, pivot to an associated malware family by clicking on it.<br>4. Examine the malware family's infrastructure by checking the Commonalities section in the IOCs tab to find malicious contacted domains.<br>5. Review the detection rules in the Rules tab, which can be imported into your security tools for continuous monitoring or to Livehunt to be notified of new IoCs uploaded to the platform. | [Google TI Use case - Uncovering Post-Exploitation threats](https://www.youtube.com/watch?v=E-QvAEVa_Bk) |
| --- | --- |

---

← [Use cases and other resources](../use-cases.md) · [up](../README.md) · [Incident Response](use-cases-incident-response.md) →

*Archived from <https://gtidocs.virustotal.com/docs/use-cases-advanced-hunting>.*
