---
title: "June 30th, 2026 — Splunk Observed Threats, GTI Score Explainability, and Private Scanning Access Control Lists (ACLs)"
source: https://gtidocs.virustotal.com/changelog/june-29th-2026-splunk-observed-threats-gti-score-explainability-and-private-scanning-access-control-lists-acls
slug: june-29th-2026-splunk-observed-threats-gti-score-explainability-and-private-scanning-access-control-lists-acls
section: changelog
group: "Changelog"
retrieved: 2026-09-01
---

[gtidocs](../README.md) › [Changelog](README.md) › [Changelog](README.md) › June 30th, 2026 — Splunk Observed Threats, GTI Score Explainability, and Private Scanning Access Control Lists (ACLs)

---

# june-30th,-2026-—-splunk-observed-threats,-gti-score-explainability,-and-private-scanning-access-control-lists-(acls)

# june-29th,-2026-—-splunk-observed-threats,-gti-score-explainability,-and-private-scanning-access-control-lists-(acls)

## 🚀-new-capabilities

### 📊-google-threat-intelligence-score-explainability

We are thrilled to announce **GTI Score Explainability**. Historically, threat intelligence scoring has functioned as an unverified "black box." This launch delivers a major milestone in threat transparency by revealing the exact logic, signal age-offs, and analyst overrides behind every score.

* **Diagnostic Explainability Cards:** The GTI Indicator Score now includes Explainability Cards — diagnostic cards in the UI and API that break down the "why" behind any score into 11 clear categories (such as Human Verified Ground Truth, Technical Evidence, Machine Learning Models, and Mitigating Factors).

* **Signal Age-Off & Score Decay:** Every contributing threat signal carries an expiration timestamp. When signals expire without new corroborating activity, the verdict and score automatically decay, ensuring teams aren't chasing stale indicators.

* **Multi-Channel Accessibility:** This transparent scoring data can be consumed seamlessly via both the GUI and our API.

![](https://files.readme.io/abddf0d38f10b35b5b85762d683be287eb05c13897fc3edb28ce9e33b6137544-image.png)

![](https://files.readme.io/bd11760657e2558189cfcac2455386d563be4af245b41e75bc5058ded098845d-image.png)

*Read our full guide on threat scores and explainability [here](https://gtidocs.virustotal.com/docs/google-threat-intelligence-indicator-score).*

***

### 🛡️-private-scanning-access-control-lists-(acls)

We are excited to announce **Private Scanning Access Control Lists (ACLs)**. Previously, any user with access to your organization's private scanning could view all uploaded files. Administrators can now restrict access to specific sensitive binaries.

* **Granular Sharing Options:** Files remain visible to your broader organization by default (maintaining backward compatibility), but editors can now explicitly restrict visibility to specific individuals.
* **How to Manage Access:** Editors (the user who submitted the file) will see a new "Share" action in the Private Scanning tab, allowing them to manage per-user access and view the persistent sharing list.

![](https://files.readme.io/db053e656afb845c9d03ba6b3add7be9c20f0b2bff6c853fef536a3cab06a912-image.png)

***

### 🔌-splunk-observed-threats

**Splunk Observed Threats** are now available in Google Threat Intelligence. This feature brings Splunk-observed telemetry directly into your GTI Threat Profiles, helping CTI and SOC teams prioritize threats that are actively present in their environment over abstract indicators.

* **Automated Threat Intel Derivation:** Splunk IoC matches are automatically mapped to structured threat objects (Threat Actors, Malware Families, Software Toolkits, and Campaigns) within your Threat Profile.
* **Clear Visibility:** Synchronized entities appear in your Threat Profile tagged as "Observed" and "Splunk," and can be filtered using the Recommendation Source field.
* **How to Get Started:** Configuration is done directly within your Splunk instance by enabling Threat Profile synchronization and linking your GTI Threat Profile ID.

  ![](https://files.readme.io/dfaedd7aa99cfc47f65bbba43c0222769941e4b41932e181108134faa727bd97-image.png)

  Read the full configuration guide [here](https://gtidocs.virustotal.com/docs/splunk-threat-profile-guide).

### 👥-clearer-group-member-filtering

Group administrators can now search and filter members more easily in the Group Management tab.

* **Organized Filter Sections:** User and service account filters are now grouped into clearer sections, including Private Scanning and a new Fine-Grained Permissions area, making it easier to locate and manage specific members.
* **Plan-Specific Filtering:** Filters that don't apply to your group's plan or active privileges are automatically hidden, keeping the interface uncluttered.

![](https://files.readme.io/716ea6ea40bcc07c47ab65cd8c6a0e6890ad807834a9e59044c40de1c0ab178c-ad43e54a-f178-4790-84c1-abcbd9123a7f.jpeg)

<br />

---

← [July 14th, 2026 — URL Scanning 2.0, RBAC for Service Accounts, and Invitations Page Improvements](july-14th-2026-url-scanning-20-rbac-for-service-accounts-and-audit-log-updates.md) · [up](README.md) · [June 18th, 2026 — Crowdsourced AI += Knostic, Self-Service API Key Rotation, domain_exact: Search Modifier, and Advanced Agentic Disassembly & Relationship Mapping](june-22nd-2026-crowdsourced-ai-knostic-self-service-api-key-rotation-domain_exact-search-modifier-and-advanced-agentic-disassembly-relationship-mapping.md) →

*Archived from <https://gtidocs.virustotal.com/changelog/june-29th-2026-splunk-observed-threats-gti-score-explainability-and-private-scanning-access-control-lists-acls>.*
