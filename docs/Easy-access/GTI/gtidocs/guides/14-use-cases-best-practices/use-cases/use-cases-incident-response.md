---
title: "Incident Response"
source: https://gtidocs.virustotal.com/docs/use-cases-incident-response
slug: use-cases-incident-response
section: guides
group: "Use Cases & Best Practices"
updatedAt: 2026-01-14T14:15:35.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [Use Cases & Best Practices](../README.md) › [Use cases and other resources](../use-cases.md) › Incident Response

---

# incident-response

When an incident occurs, security teams need to move fast—triaging alerts, understanding the scope of the attack, and uncovering how it unfolded. Whether you're responding to a live threat or conducting post-incident forensic analysis, access to timely and relevant intelligence is critical.

Google Threat Intelligence (Google TI) helps teams go beyond surface-level investigation. By combining curated frontline intelligence, vast crowd sourced data, and global infrastructure visibility, Google TI enables analysts to triage efficiently, pivot across related indicators, and reconstruct the full picture of an attack—all within a single platform.

## how-can-google-threat-intelligence-help?

Google TI supports every phase of incident response, from initial triage to post-incident action:

**Investigation & Triage**

* Pivot from a single IoC (file hash, domain, IP, or URL) to discover related infrastructure and campaigns.
* Visualize relationships between indicators using the interactive Threat Graph.
* Access intelligence on malware families, threat actors, and campaign reports.
* Use YARA rules and Retrohunt to discover files across the dataset that exhibit similar structure or behavior to known malware.
* Map TTPs observed in the incident to better understand attacker behavior.
* Correlate with exploited CVEs using vulnerability intelligence to prioritize remediation.

**Operationalizing Intelligence**

* Feed high-confidence IoCs into SIEM, SOAR, and EDR tools to block ongoing activity.
* Update detection rules and blocklists across firewalls, proxies, DNS, etc.
* Use findings to guide threat hunting and detect similar activity in your environment.
* Improve policies and controls based on observed attacker TTPs and infrastructure.

## use-cases

### from-a-phishing-email-to-uncovering-a-targeted-campaign

An employee reports a suspicious email. Your goal: analyze the attachment to uncover whether it’s part of a larger campaign—and if so, who’s behind it.

**How to do it**

| 1. Search the file using [Private Scanning](../../09-private-scanning/private-scanning.md) in Google TI.<br />2. Open the [Threat Graph](../../08-threat-graph/get-started-threat-graph.md) to explore relationships between the file and associated URLs, domains, and infrastructure.<br />3. Investigate related indicators in the Relations tab—e.g., other URLs hosting the same file, or similar attachments.<br />4. Use TTP Investigation to identify techniques and behaviors associated with the file or campaign.<br />5. Correlate with known actors or campaigns to understand attribution, targeting, and intent.<br /> | [From a Phishing Email to Uncovering a Targeted Campaign](https://www.youtube.com/watch?v=dVW2TPU-4XE) |
| --- | --- |

---

← [Advanced Hunting](use-cases-advanced-hunting.md) · [up](../README.md) · [Phishing & Brand Monitoring](use-cases-phishing-brand-monitoring.md) →

*Archived from <https://gtidocs.virustotal.com/docs/use-cases-incident-response>.*
