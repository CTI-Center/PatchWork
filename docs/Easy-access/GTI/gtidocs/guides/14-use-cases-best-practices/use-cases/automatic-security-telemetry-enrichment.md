---
title: "Automatic Security Telemetry Enrichment"
source: https://gtidocs.virustotal.com/docs/automatic-security-telemetry-enrichment
slug: automatic-security-telemetry-enrichment
section: guides
group: "Use Cases & Best Practices"
updatedAt: 2026-02-13T14:57:32.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [Use Cases & Best Practices](../README.md) › [Use cases and other resources](../use-cases.md) › Automatic Security Telemetry Enrichment

---

# automatic-security-telemetry-enrichment

Security teams are often overwhelmed by a flood of data from various tools that lacks the external context needed to prioritize threats. By integrating real-world threat intelligence into your existing security systems, you can transform these raw alerts into clear, actionable insights. This shift allows analysts to move away from simply reacting to data and instead focus on making faster decisions and automating responses to sophisticated attacks.

## how-can-google-threat-intelligence-help?

Google TI is designed to integrate directly into your security ecosystem, enriching your internal telemetry in real-time. By leveraging our API, you can automate the process of adding deep, multi-angular context to your alerts, empowering your team to work more efficiently and make more confident decisions directly within their existing workflows.

**Alert Triage & Prioritization** provides immediate context for raw alerts, such as verdicts and actor profiles, allowing analysts to focus on the most critical threats without switching between tools.

This process transitions into **Automated Investigation & Response**, where that same intelligence is used to automatically enrich data in your SIEM or SOAR and trigger pre-set playbooks. By integrating high-confidence IoCs and vulnerability data directly into your security controls, you can operationalize threat data at machine speed and automate responses to real-world attacks.

## use-cases

### enriching-alerts-in-secops

A high volume of alerts is flooding your security tools. You need to cut through the noise and quickly identify which alerts represent a genuine, high-priority threat.

**How to do it?**

| 1. Navigate to the **SecOps Marketplace** and search for the **Google TI integration**.<br>2. Install the integration and configure your [API key](../../01-introduction/how-get-gti-api-keys.md) in it.<br>3. Create a Playbook including the **IOC enrichment action**.<br>4. Configure the trigger of the playbook to be executed on every new case that contains IOCs, or trigger it manually on each case. | [Google Threat Intelligence Use Case: Enriching Alerts in SecOps](https://www.youtube.com/embed/6CN-Tc04nKc?si=6TUzxNMrZZv9Uq5i) |
| --- | --- |

---

← [Vulnerability Management](use-cases-vulnerability-management.md) · [up](../README.md) · [Frequently Asked Questions](../../15-faq/frequently-asked-questions.md) →

*Archived from <https://gtidocs.virustotal.com/docs/automatic-security-telemetry-enrichment>.*
