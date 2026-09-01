---
title: "Threat Intelligence objects search modifiers"
source: https://gtidocs.virustotal.com/docs/threat-intelligence-objects-modifiers-values
slug: threat-intelligence-objects-modifiers-values
section: guides
group: "IOC Investigation"
updatedAt: 2026-04-09T11:06:35.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [IOC Investigation](../README.md) › [Intelligence / Web searching](../intelligence.md) › Threat Intelligence objects search modifiers

---

# threat-intelligence-objects-search-modifiers

Some advanced search modifiers for threat intelligence objects, such as Threat Actors, Malware Families, Software or Tools, Campaigns, IoC Collections, Reports, and Vulnerabilities, only accept specific **case-sensitive** values:

* **collection\_type**:
  * Threat Actors: "threat-actor"
  * Malware Families: "malware-family"
  * Software or Tools: "software-toolkit"
  * Campaigns: "campaign"
  * IoC Collections: "collection"
  * Reports: "report"
  * Vulnerabilities: "vulnerability"
* **origin**:
  * Threat Actors, Malware Families, Software or Tools: "Google Threat Intelligence", "Partner".
  * Campaigns: "Google Threat Intelligence".
  * IoC Collections: "Crowdsourced", "Google Threat Intelligence", "Partner".
  * Reports: "Crowdsourced", "Google Threat Intelligence".
* **source\_region**: ISO country code, "Global", "Africa", "America", "Asia", "Europe", "Oceania", "Eastern Africa", "Northern Africa", "Southern Africa", "Central America", "Northern America", "South America", "Central Asia", "Eastern Asia", "South-eastern Asia", "Southern Asia", "Western Asia", "Western Africa", "Eastern Europe", "Northern Europe", "Southern Europe", "Western Europe", "Australia and New Zealand".
* **targeted\_region**: ISO country code, "Global", "Africa", "America", "Asia", "Europe", "Oceania", "Eastern Africa", "Northern Africa", "Southern Africa", "Central America", "Northern America", "South America", "Central Asia", "Eastern Asia", "South-eastern Asia", "Southern Asia", "Western Asia", "Western Africa", "Eastern Europe", "Northern Europe", "Southern Europe", "Western Europe", "Australia and New Zealand".
* **targeted\_industry**: "Defense", "Aerospace", "Agriculture", "Food", "Automotive", "Chemical", "Steel", "Activists", "Citizens", "Civil society", "NGO", "Political party", "Religion", "Construction", "Engineering", "Industrial", "Academia - University", "Education", "Higher education", "Electric", "Energy", "Infrastructure", "Bank", "Cryptocurrency", "Finance", "Investment", "Payment", "eCommerce", "Diplomacy", "Government", "Administration", "Trade", "Health", "Hospitality", "Hotels", "Travel", "Insurance", "Consulting", "Employment", "Legal", "Logistic", "Research - Innovation", "Manufacturing", "Casino", "Game", "Journalist", "News - Media", "Streaming service", "Multi-sector", "Oil and Gas", "Pharmacy", "Retail", "Electronic", "High tech", "IT - Security", "Social networks", "Technology", "Communication equipment", "IT", "IT - ISP", "Telecoms", "Civil Aviation", "Maritime", "Shipping", "Transport", "Unknown".
* **targeted\_industry\_group**: "Aerospace & Defense", "Agriculture", "Automotive", "Chemicals & Materials", "Civil Society & Non-Profits", "Construction & Engineering", "Education", "Energy & Utilities", "Financial Services", "Government", "Healthcare", "Hospitality", "Insurance", "Legal & Professional Services", "Manufacturing", "Media & Entertainment", "Multi-sector", "Oil & Gas", "Pharmaceuticals", "Retail", "Technology", "Telecommunications", "Transportation", "Unknown".
* **operating\_system**: "Android", "BSD", "FreeBSD", "Linux", "Mac", "Unix", "VMkernel", "Windows", "ios".
* **malware\_role**: "Archiver", "ATM Malware", "Backdoor - Botnet", "Backdoor - Webshell", "Backdoor", "Bootkit", "Builder", "Controller", "Credential Stealer", "Cryptocurrency Miner", "Data Miner", "Decoder", "Disruption Tool", "Downloader", "Dropper - Memory Only", "Dropper", "Exploit Builder", "Exploit", "File Infector", "Framework", "Installer", "Keylogger", "Lateral Movement Tool", "Launcher", "Lightweight Backdoor", "Module", "Point-of-Sale Malware", "Privilege Escalation Tool", "Ransomware", "Reconnaissance Tool", "Remote Control and Administration Tool", "Remote Exploitation Tool", "Rootkit", "Screen Capture Tool", "Sniffer", "Spambot", "Tunneler", "Uploader", "Utility".
* **motivation**: "Attack / Destruction", "Espionage", "Financial Gain", "Hacktivism", "Influence", "Surveillance", "Opportunistic".
* **report\_type** (for Reports only): "Actor Overview", "Actor Profile", "Country Profile", "Event Coverage/Implication", "Executive Perspective", "FireEye Labs Research", "Futures Scenario", "Horizons", "ICS Security Roundup", "Industry Intelligence Quarterly", "Industry Reporting", "Malicious Activity Report", "Malware Overview", "Malware Profile", "Net Assessment", "Network Activity Reports", "News Analysis", "OSINT Article", "Patch Report", "TTP Deep Dive", "Tactical Threat Report", "Threat Activity Alert", "Threat Activity Report", "Trends and Forecasting", "Technical Intelligence", "Threat Intelligence", "Weekly Vulnerability Exploitation Report".

---

← [Reports search modifiers](reports-search-modifiers.md) · [up](../README.md) · [IoC Reports](../results-reports.md) →

*Archived from <https://gtidocs.virustotal.com/docs/threat-intelligence-objects-modifiers-values>.*
