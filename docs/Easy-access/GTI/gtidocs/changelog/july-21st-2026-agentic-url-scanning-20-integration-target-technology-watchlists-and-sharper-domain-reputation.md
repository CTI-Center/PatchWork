---
title: "July 21st, 2026 — Agentic URL Scanning 2.0 Integration, Target Technology Watchlists, and Sharper Domain Reputation"
source: https://gtidocs.virustotal.com/changelog/july-21st-2026-agentic-url-scanning-20-integration-target-technology-watchlists-and-sharper-domain-reputation
slug: july-21st-2026-agentic-url-scanning-20-integration-target-technology-watchlists-and-sharper-domain-reputation
section: changelog
group: "Changelog"
retrieved: 2026-09-01
---

[gtidocs](../README.md) › [Changelog](README.md) › [Changelog](README.md) › July 21st, 2026 — Agentic URL Scanning 2.0 Integration, Target Technology Watchlists, and Sharper Domain Reputation

---

# july-21st,-2026-—-agentic-url-scanning-2.0-integration,-target-technology-watchlists,-and-sharper-domain-reputation

### 🤖-agentic-url-scanning-2.0-integration&#x20;

Agentic now leverages VirusTotal's sandboxed browser execution to analyze suspicious URLs dynamically.

**Capabilities:**

* **Runtime Telemetry:** Captures dynamic DOM modifications, network requests, and global JavaScript variables.
* **Campaign Mapping:** Fingerprints phishing kits (e.g. pivoting on `__jwrAuth` variables) to map related threat infrastructure.

**URLs that are not in the public corpus of Google Threat Intelligence are analyzed privately using Private Scanning.**

> **Example Prompt:** *"Investigate hxxps\://t-mobile.zyhqxp.top/pay/ and find other URLs from the same campaign using its JS footprint. Then create a campaign collection."*<br />**[View this conversation in Agentic →](https://www.virustotal.com/gui/agentic/shared/gAAAAABqXjzi-ArM2j-esWBrMYJBxWiOSBLb1zRgl94Yg7juZDajXBnxczgM_w0I_d-OSfn_fhfxVr4M13gSYK2WN6SmAkCxAWe11hz3jTBDjqlLj9d86O1_bNLP2FWWqgdWaN06F-SUAN64QUFX65F21lC4mbKosfw9IkuNkWgl7TIhqQ31qU3yw0-tsXlitAErXYIWwSLH)**

![](https://files.readme.io/510fa5ceeefc90019e4d405d6627f1e19b78b06aaa48d252a06eab2e743e0558-Screenshot_2026-07-21_at_14.56.18.png)

### 🛡️-public-preview:-target-technology-watchlists

Target Technology Watchlists are now in Public Preview for GTI customers. This capability allows you to easily track relevant intelligence based on your specific technology stack, driving focus to the threats that truly matter most.

**Key Benefits:**

* **Flexible Inputs:** Simply drop a list of technologies or CPEs into your [threat scenario](https://gtidocs.virustotal.com/docs/my-landscape-threat-scenarios) to immediately get vulnerability intelligence [alerts](https://gtidocs.virustotal.com/docs/alerts) through the alert section in the [org profile](https://gtidocs.virustotal.com/docs/organization-profile).
* **Customizable Alerts:**&#x52;eceive notifications specifically for CVEs affecting the organization's tech stack.
* **Rich Vulnerability Details:** Every alert is enriched with full exploit context, including assigned priority, vulnerability Risk Rating, real-world Exploitation State, and more.
* **Intelligence Context:** Leverage direct integration with GTI vulnerability intelligence for full exploit context.
* **Unified View & API Access:** Access a unified alerts stream, fully available via API for programmatic and agentic workflows.

![](https://files.readme.io/91eadbb5ba2b365357f9da89bc2f44ef89ace941bad04ed657e02401f5e945bf-Screenshot_2026-07-21_at_15.42.22.png)

For more information, please refer to the documentation on [Threat Scenarios](https://gtidocs.virustotal.com/docs/my-landscape-threat-scenarios), [Organization Profiles](https://gtidocs.virustotal.com/docs/organization-profile), and [Alerts](https://gtidocs.virustotal.com/docs/alerts).

### 🌐-sharper-domain-reputation-(mitigating-expired-domain-abuse)

Threat actors frequently purchase abandoned, previously popular domains to host malware C2 servers or DGA infrastructure, a tactic known as **expired domain abuse**. This is a known technique used to bypass security scanners by exploiting the domain's artificially high historical popularity.

To counter this, we have further enhanced our behavior-based detection for C2 and DGA domains to more strictly discount obsolete popularity metrics. This ensures that a domain's historical fame can no longer shield it from accurate threat scoring, effectively neutralizing this evasion tactic.

---

← [August 12th, 2026 — Agentic Flows & API, and Threat Actor Naming Updates](august-5th-2026-agentic-flows-api-and-threat-actor-naming-updates.md) · [up](README.md) · [July 14th, 2026 — URL Scanning 2.0, RBAC for Service Accounts, and Invitations Page Improvements](july-14th-2026-url-scanning-20-rbac-for-service-accounts-and-audit-log-updates.md) →

*Archived from <https://gtidocs.virustotal.com/changelog/july-21st-2026-agentic-url-scanning-20-integration-target-technology-watchlists-and-sharper-domain-reputation>.*
