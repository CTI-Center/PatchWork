---
title: "August 12th, 2026 — Agentic Flows & API, and Threat Actor Naming Updates"
source: https://gtidocs.virustotal.com/changelog/august-5th-2026-agentic-flows-api-and-threat-actor-naming-updates
slug: august-5th-2026-agentic-flows-api-and-threat-actor-naming-updates
section: changelog
group: "Changelog"
retrieved: 2026-09-01
---

[gtidocs](../README.md) › [Changelog](README.md) › [Changelog](README.md) › August 12th, 2026 — Agentic Flows & API, and Threat Actor Naming Updates

---

# august-12th,-2026-—-agentic-flows-&-api,-and-threat-actor-naming-updates

### 🌊-public-preview:-google-ti-flows

Google TI Flows is a scheduled orchestration engine that automates recurring investigations by executing natural language prompts (with optional email delivery) and advanced saved searches (delivered to your IoC Stream) on a schedule.

**Key Capabilities:**

* **Scheduled Natural Language Prompts:** Schedule complex multi-step AI agent investigations (e.g., "Summarize all new ransomware infrastructure targeting healthcare in the last 24 hours") to execute periodically.
* **Scheduled Advanced Saved Searches:** Run recurring advanced saved searches (e.g., active campaign indicators, brand impersonation domains) automatically on a schedule and receive the results directly on your IoC Stream.
* **Automated Email Reports:** Configure prompt-based flows to automatically format and dispatch the results of your prompts—such as structured reports or summaries—directly to team email distribution lists.

![](https://files.readme.io/3d84106a5b95c02aafb42ae5e32e7d806201fe562dd6f32990154ff0106c1881-Screenshot_2026-08-12_at_12.27.28.png)

**Example Use Cases:**

* **Automated Daily Executive Threat Digest:** A Flow executes a daily prompt to summarize threat actor activity and malware campaigns for a specific sector, emailing a clean executive summary directly to security leadership every morning.
* **Continuous Campaign Threat Hunting:** A Flow executes an advanced VTI saved search query at set intervals for new samples matching your query, automatically flagging and sending newly identified samples to the IoC Stream.

**Documentation:** [Google TI Flows Guide](https://gtidocs.virustotal.com/docs/flows-guide)

### 🤖-public-preview:-agentic-api-&-flows-api

The Agentic API is now live in Public Preview for Enterprise, Enterprise Plus, and Integration Advanced users. It provides programmatic REST API access to specialized AI threat intelligence agents, shifting threat intelligence from manual lookups to continuous, autonomous AI-driven defense.

**Key Capabilities:**

* **Programmatic Intelligence:** Utilize direct REST API endpoints to trigger specialized AI agents for deep IOC triage, threat actor profiling, dark web monitoring, malware analysis, and automated YARA rule generation.
* **Flows API:** Programmatically orchestrate your investigations with full CRUD access, enabling you to create, execute, and monitor automated flows directly from your internal systems.
* **Seamless SOC Integration:** Embed Google TI’s agentic intelligence natively into your SIEM, SOAR, or custom security pipelines to eliminate manual toil and significantly accelerate incident response times.

**Example Use Case — SOAR Automated Alert Enrichment:** When a SIEM/SOAR triggers an alert for an unknown malicious IP or file hash, a playbook can call the Agentic API to execute deep IOC triage, gather dark web chatter, and draft YARA detection rules automatically, attaching high-context notes before an analyst even begins review.

**Documentation:** [Agentic API Reference](../reference/16-agentic/sessions.md) | [Flows API Reference](../reference/16-agentic/flows.md)

### 👤-threat-actors:-new-naming-convention

We are rolling out a new, unified threat actor naming schema to standardize tracking across all systems and make our threat intelligence more intuitive and actionable. As the threat landscape expands, relying on sequential numbers (e.g., APT44, FIN11) has become an exercise in memorization rather than intuition.

**The Cryptonym-Based Approach**
We are transitioning from numerical identifiers to a cryptonym-based approach. Each distinct threat actor will now be identified by a memorable two-word combination:

* **First Word:** A unique, memorable term representing the specific actor.
* **Second Word:** Categorizes the actor by its primary motivation, origin, or activity type (e.g., *RELIC* for Russia, *NEPTUNE* for North Korea, or *COMET* for cybercriminals).

![](https://files.readme.io/d58d6d7a5011b52b57bb388ac3f60be9c332b9dea46501ebe126a0c35f359cfb-Screenshot_2026-08-12_at_12.31.37.png)

**A Work in Progress**<br />We have initially prioritized renaming several dozen of the most active groups, and will continue this process on a rolling basis. Previous names will remain indexed and searchable in the Google Threat Intelligence platform, with MITRE ATT\&CK mappings and other vendor aliases preserved, see Figure 1.

---

← [August 26th, 2026 — Google Insights, Agentic Updates, and Detection Highlights](august-26th-2026-google-insights-agentic-updates-and-detection-highlights.md) · [up](README.md) · [July 21st, 2026 — Agentic URL Scanning 2.0 Integration, Target Technology Watchlists, and Sharper Domain Reputation](july-21st-2026-agentic-url-scanning-20-integration-target-technology-watchlists-and-sharper-domain-reputation.md) →

*Archived from <https://gtidocs.virustotal.com/changelog/august-5th-2026-agentic-flows-api-and-threat-actor-naming-updates>.*
