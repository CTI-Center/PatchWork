---
title: "Google Threat Intelligence Indicator Score"
source: https://gtidocs.virustotal.com/docs/google-threat-intelligence-indicator-score
slug: google-threat-intelligence-indicator-score
section: guides
group: "IOC Investigation"
updatedAt: 2026-06-18T12:24:48.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [IOC Investigation](README.md) › Google Threat Intelligence Indicator Score

---

# google-threat-intelligence-indicator-score

Our threat scoring system is designed to help SecOps teams prioritize the most significant security threats. We calculate threat scores for various entities, including files, domains, IP addresses, and URLs. This document explains the logic behind our scoring system and provides guidance on interpreting those scores.

# overview:-demystifying-the-threat-score-"black-box"

Security operations teams are constantly inundated with security alerts, forcing analysts to make rapid, high-stakes decisions. To help your team prioritize effectively, Google Threat Intelligence features a native **Threat Score Explainability** framework.

This methodology is the direct **codification of expert Mandiant threat analyst triage logic**. By automating the analytical processes of seasoned threat hunters, Google TI evaluates files, IP addresses, domains, and URLs using a rich, continuously expanding library of **over 100+ unique threat telemetry signals and behavioral heuristics**. This pipeline undergoes **continuous manual and automated evaluation** to optimize precision (minimizing false positives) and recall (ensuring true threats are caught).

Rather than outputting an arbitrary, opaque number, GTI provides complete transparency by revealing the core contributing factors, signal age-offs, and analyst overrides behind every score.

To prevent ambiguity for analysts, a clear distinction must be made between two types of scores:

* **GTI Threat Score:** The final, user-facing numeric score (ranging from 0 to 100) that is determined by combining the indicator's Verdict, its Severity, and specific classification factors. The GTI Threat Score is a numeric representation of the likely impact a particular indicator (file, domain, IP address, or URL) may have if detected in an environment. Our scoring system leverages a wealth of threat intelligence data and codifies the expertise of Mandiant threat analysts to derive this score.
* **GTI IC Score (Indicator Confidence Score):** An internal, machine-learning-based confidence score that serves as one of the contributing factors to the final Verdict and GTI Threat Score.

# how-the-google-threat-intelligence-score-is-derived

The GTI Threat Score is a function of the Google TI Verdict and Severity, and leverages additional internal factors to generate the final score.

# core-concepts:-verdict-vs.-severity

The GTI Threat Score is synthesized directly from two distinct evaluation dimensions:

* **Verdict (Maliciousness):** How confident are we that this indicator is harmful?
* **Severity (Impact):** Categorizes the impact of malicious activities possible.

## what-is-a-verdict?-(confidence-of-maliciousness)

The Verdict represents our analytical confidence regarding whether an indicator is associated with malicious activity. GTI classifies indicators into five core verdicts:

* **Malicious:** Definitive evidence and high confidence that the indicator is part of active threat infrastructure, malware campaigns, or unauthorized actor activity.
* **Suspicious:** Anomalous indicators or suspicious behaviors are observed (e.g., suspicious sandbox behavior or Safe Browsing reports), but they lack definitive proof of targeted malicious intent. This category specifically includes:
  * **Inactive Historical Threats:** Malicious indicators suspected to be currently inactive. While the infrastructure may be dormant, historical threats can still carry high residual impact, making them critical for enterprise investigation.
  * **Dual-Use Infrastructure & Binaries:** Legitimate tools or administrative utilities frequently co-opted by adversaries. To minimize disruptive false positives, these are not classified as malicious outright, but they remain vital hunting leads for security teams.
* **Undetected:** No suspicious or malicious signals have been observed in our telemetry.
* **Benign:** Confirmed safe infrastructure, globally recognized trusted software, signed binaries, or clean domains/IPs.
* **Unknown:** Insufficient telemetry is available to make a valid assessment. This verdict only applies to [partial files](../15-faq/partial-files.md).

## what-is-severity?-(potential-impact)

Severity measures the **potential impact or damage** an indicator could cause to an organization. In other words, **should you care about this indicator?** It allows your analysts to ignore low-impact nuisances and focus on high-impact operational dangers:

* **High:** Associated with severe, business-disrupting threats that typically operate later in the attack lifecycle (e.g., the exploitation or actions-on-objectives phases). Examples include ransomware, active command-and-control (C2) servers, critical backdoor access, or credential stealers.
* **Medium:** Associated with infrastructure or tools that typically appear in the earlier stages of an intrusion (e.g., the distribution or delivery phases). Because it is technically unknown at this stage whether the distribution will succeed or what the ultimate payload will be, these are capped at medium. Examples include downloaders, droppers, exploits, keyloggers, obfuscation networks, or bulletproof hosts (which may ultimately traffic either low or high-severity threats).
* **Low:** Low-impact threats or nuisances that should have a limited blast radius if an organization's baseline security posture is strong. Examples include cryptocurrency miners, adware, spam, or vulnerability scanners. While opportunistic vulnerability scanning should be mitigated by standard patch management, these remain important to address if an organization has known underlying weaknesses.
* **None:** No risk identified (default for Undetected or Benign indicators).

# how-the-gti-threat-score-is-calculated

GTI combines the **Verdict** and **Severity** dimensions into a single numeric **Threat Score** ranging from **0 (completely benign) to 100 (highly malicious and severe)**.

The score maps directly to specific logic combinations to provide granular risk levels:

| Verdict        | Severity | Threat Score | Scoring Logic & Category Modifiers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| :------------- | :------- | :----------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Benign**     | None     | **0**        | Confirmed safe or explicitly allowlisted infrastructure (e.g., non-routable private IPs, known safe domains).                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Undetected** | None     | **1**        | Default clean state. No malicious markers observed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Suspicious** | Low      | **21**       | Mild anomalies with low potential impact (e.g., minor grayware or suspicious low-impact PUA behavior).                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Suspicious** | Medium   | **25**       | Suspicious behaviors tied to delivery-stage activity, obfuscation networks, bulletproof hosts, or dual-use utilities lacking confirmed threat actor pairing.                                                                                                                                                                                                                                                                                                                                                                               |
| **Suspicious** | High     | **29**       | **High-Impact, Low-Confidence Safety Cap:** Active severe threat signature (e.g., an enterprise-grade backdoor or command-and-control behavior) that has been structurally mitigated, muted, or degraded. <br/>Examples include: A known high-severity C2 domain that has been flagged as **hijacked or dormant** for over 30 days. A high-severity malware file that matches legitimate allow-list override rules. This cap allows analysts to remain aware of the high potential risk without triggering disruptive automated blockings. |
| **Malicious**  | Low      | **30 – 59**  | Confirmed threats with minor organizational impact: Examples include adware, generic spam. <br/>**Category Modifiers Include:** Cryptocurrency miners and banker trojans.                                                                                                                                                                                                                                                                                                                                                                  |
| **Malicious**  | Medium   | **60 – 79**  | Confirmed threats capable of initial intrusion or lateral movement: Examples include standard downloaders/droppers.<br/>**Category Modifiers Include:** Generic hacktools and being identified in verified frontline threat intelligence.                                                                                                                                                                                                                                                                                                  |
| **Malicious**  | High     | **80 – 100** | Severe, critical threats requiring immediate incident response: Examples include active C2 servers, ransomware.<br/>**Category Modifiers:** Associations with known, active threat actors, campaign or ransomware.                                                                                                                                                                                                                                                                                                                         |

## severity-and-technical-categories

The Severity level (`Low`, `Medium`, `High`) is directly related to the technical category of the indicator. Higher-risk categories (such as malicious implants and backdoors) dictate higher baseline severities, whereas lower-risk categories (such as adware or utilities) result in lower baseline severities.

# how-threat-scores-are-determined

Threat scores are determined by a comprehensive set of factors which are expanding and evolving. The exact score and weighting depends on whether we're assessing a file, domain, IP address, or URL.

## file-coverage

* **Verdict**
  * The file is ruled **Malicious** if it has been detected by trusted threat intelligence sources (Mandiant, Google, etc)
  * The file is ruled **Benign** if it is explicitly classified as legitimate by Google Threat Intelligence.

* **Severity**
  * Severity can be **None** if the verdict is "benign", or not malicious without any supporting evidence.
  * **Low** severity examples: adware, potentially unwanted applications (PUA), cryptominers, spam, fake antivirus.
  * **Medium** severity examples: files linked to financial threat intelligence sources, specific detection names indicating exploits, rootkits, or hack tools.
  * **High** severity examples: files linked to known malware or ransomware threats, or files exhibiting ransomware-like behavior based on antivirus detection patterns.

## domain-coverage

* **Verdict**
  * A domain is ruled **Benign** if popularity is high (top 10,000), or explicitly excluded by Mandiant.
  * A domain is ruled **Malicious** if it's rated highly malicious by Mandiant analytics or Google SafeBrowsing.
  * **Suspicious** verdicts occur when scores are above a threshold but lower than conclusive malicious ratings.
  * Several other factors can influence the verdict, including indications of domain hijacking.

* **Severity**
  * Severity is initially **None** if the verdict is "benign."
  * Severity depends on factors like category (adware, ransomware), threat intelligence sources, and indicators in downloaded and related files.

## ip-address-coverage

* **Verdict** and **Severity** follow a logic structure very similar to Domain Coverage, adjusting for the specific factors relevant to IP addresses.

## url-coverage

* **Verdict** and **Severity** logic is also similar to Domains and IP Addresses, tailored for the unique properties of URLs.

# explainability-cards-taxonomy

To provide context and answer the **"Why"** behind any given score, the GTI user interface (and API) displays diagnostic explainability cards. These cards translate raw backend scoring attributes into clear, logical groupings.

## the-11-card-categories

* **Highest Impact Factor:** Highlights the primary indicator or signal that most heavily influenced the verdict and final score.
* **Human Verified Ground Truth:** Shows determinations, manual overrides, and direct attributions made by threat analysts (e.g., Mandiant incident responders).
* **Mitigating Factors:** Identifies attributes that reduce the severity of the threat or suggest a benign nature (e.g., trusted metadata, allowlists, or high global popularity).
* **Threat Intelligence:** Collects attributions, campaign mappings, and reports from premium threat intelligence sources.
* **Technical Evidence:** Displays automated observations, such as sandbox runs, configuration extractions, and multi-engine detection agreements.
* **Tool Abuse:** Identifies instances where legitimate administrative, security, or dual-use tools are suspected of being abused in a threat context.
* **Propagated Factors:** Captures threat indicators that are inherited or associated via related assets (e.g., a URL hosted on known malicious infrastructure).
* **Collective Detections:** Groups collective signal feeds, blocklists, community YARA rules, and shared reputation indices.
* **Machine Learning Models:** Reflects determinations made by specialized ML classifiers.
* **Historical Context:** References past historical activity and signals that have aged off.
* **Undetected:** Represents the base clean/undetected state of the entity.

## ui-classification-examples

Below are a few examples of the explainability cards to their respective explainability classifications:

| Card Title / Signal                        | Category            | Description                                                                               |
| :----------------------------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| **Verified Malicious by Mandiant Analyst** | Human Verified      | Manual analyst verification during an active investigation.                               |
| **High Sandbox Detonation Malicious**      | Technical Evidence  | Automated detonation observed high-severity malicious actions.                            |
| **Matched Mandiant YARA Rule**             | Technical Evidence  | Matches high-fidelity Mandiant-authored signatures.                                       |
| **ML Malware Code Similarity Detection**   | Machine Learning    | ML model matched code structure to known malware families.                                |
| **Abused Legitimate Tool / Service**       | Tool Abuse          | Warns analysts that a safe administrative tool is being leveraged maliciously.            |
| **Redirects to Malicious Destination**     | Propagated Factors  | Traffic automatically routes users to an active infection node.                           |
| **Attributed to Mandiant Threat Actor**    | Threat Intelligence | Direct mapping to a tracked advanced persistent threat (APT) or UNC group.                |
| **Aged-Off Threat Signal**                 | Historical Context  | Shows that a historical signal has expired and no longer affects the score.               |
| **High Global Traffic Popularity**         | Mitigating Factors  | Domain enjoys high global traffic ranking, reducing likelihood of targeted maliciousness. |

## dynamic-card-association-limit

To maintain a clean, actionable UI layout and prevent "alert fatigue" or dashboard clutter, the explainability section limits the display of associated entities.

The UI enforces a **maximum of three** of each association type (such as associated threat actors, malware families, or rules/YARAs). If more than three associations exist, the UI displays the three highest-impact items and provides an option to view the complete list in the threat details drawer.

# key-contributing-factors

Our threat scoring system takes the following factors into account (among others):

* Number of detections
* Specific detection keywords
* Presence on reputable threat intelligence lists
* Classification categories (virus, ransomware, spam, etc.)
* Evidence of suspicious behavior in sandbox environments
* Links to known malicious files or threat infrastructure
* Domain reputation and popularity
* Safe browsing classifications (Google SafeBrowsing)
* Attributions (Actors, Malware, Campaigns, Collections etc)

# signals-age-off-&-score-decay

Threat infrastructure is highly volatile. A compromised IP address hosting a malicious loader today might be cleaned and reassigned to a legitimate business next week. To prevent security teams from chasing stale indicators, GTI employs a dynamic **Signal Age-Off** model.

## how-age-off-works

* **Expiration Deadlines:** Every contributing threat signal (e.g., a sandbox execution run, an AV signature detection, or third-party feeds) is assigned a strict expiration timestamp.
* **Age-Off Factors:** When a threat signal reaches its expiration deadline without any new corroborating malicious activity, it "ages off." The system retires these signals from current calculations but keeps them logged in the indicator's history as an age-off factor.
* **Automatic Score Decay:** If the primary signal that drove a malicious score ages off, the threat score is recalculated. This dynamically drops the indicator’s score back down to Suspicious or Undetected protecting your team from false positive alerts.

## impact-of-signal-expiration

* **Decay of the GTI Threat Score:** As active threat signals and contributing factors age off, the overall Verdict may transition (e.g., from Malicious to Suspicious), which in turn lowers the final GTI Threat Score.
* **Severity is Not Directly Affected by Decay:** The Severity level assigned to a specific category is constant and does not gradually decay or decrease over time. However, the threat categories associated with an indicator can age off entirely, which shifts the indicator to a different category or removes it.
* **Decay of Verdict:** When all active malicious signals expire, the indicator's Verdict decays over time. The system uses a grace period to transition indicators safely (e.g., holding them at Suspicious for a time) before letting the verdict decay completely back to Undetected.

# customer-guidance

Security teams should prioritize entities with "Malicious" verdicts and "High" severity scores. We recommend further investigation of "Suspicious" verdicts and careful monitoring of all entities with severity scores greater than "None."

We recommend aligning your SIEM/SOAR playbooks with the following score ranges:

* **80 to 100 (High Severity):** Block immediately and initiate high-priority investigation (Active C2, Ransomware, Targeted Attacks).
* **60 to 79 (Medium Severity):** Alert security analysts for active investigation (Intrusion tools, Droppers). Initiate proactive hunting sweeps across the network, as these indicators signify the enterprise is being targeted by an early-stage distribution campaign. Search logs for successful distribution.
* **30 to 59 (Low Severity):** Log the event and cross-reference your controls to ensure these commodity threats are fully covered by existing passive defenses. If a defensive gap is found that allows the threat to succeed, escalate the incident to a higher priority for immediate remediation.
* **Under 30 (Suspicious / Anomalous):** Treat as proactive hunting leads. Do not auto-block to avoid false positives, but monitor for correlation with other internal network events. **Hunting Tip:** If an internal asset interacts with a Score 25 (Dual-Use utility) followed shortly by a Score 29 (Dormant/Aged-off C2), escalate the investigation immediately, as this pattern potentially suggests a revived historical threat.

# threat-score-explainability:-user-experience-faq

### q:-why-did-this-specific-indicator-receive-this-score?

**A:** Every indicator page features a **Threat Score Explainer** card. This card functions as an "open ledger of evidence," showing the active contributing factors—such as specific YARA rule matches, connected Mandiant Finished Intelligence Reports, behavioral sandbox alerts, or reputation lists—that drove the verdict and severity calculations.

### q:-i-suspect-an-indicator-has-been-incorrectly-flagged-(false-positive).-how-can-i-verify-this?

**A:** Review the **Contributing Factors** listed on the Explainer card. If a manual correction is made by our teams (e.g., a Mandiant analyst marking an indicator as a false positive or using an bypass list), the system's "analyst mistake" or override logic will trigger. The Threat Score will immediately decay to its correct level, and the Explainer card will highlight the analyst intervention.

### q:-how-should-our-team-prioritize-incidents-using-the-threat-score?

**A:** See the score range recommendations in the **Customer Guidance** section above.

# key-points

* The GTI Threat Score is designed to reflect the potential impact of a threat. Higher scores indicate a greater risk to your environment, but risk can only be assessed by using customer derived factors.
* The verdict and severity classifications are the primary drivers of the GTI Threat Score.
* Specific categories, threat intelligence sources, and analyst expertise all contribute to the final score.
* The score is dynamic and is updated as new factors affecting the scoring are observed or as active signals age off.

---

← [IoC Reports](results-reports.md) · [up](README.md) · [Saved Searches](saved-searches-guide.md) →

*Archived from <https://gtidocs.virustotal.com/docs/google-threat-intelligence-indicator-score>.*
