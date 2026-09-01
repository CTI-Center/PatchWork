---
title: "April 13th, 2026 - Visual Insights and Saved Search Integration in Agentic, SCIM Token Updates, and more"
source: https://gtidocs.virustotal.com/changelog/visual-insights-and-saved-search-integration-in-agentic-scim-token-updates-and-more
slug: visual-insights-and-saved-search-integration-in-agentic-scim-token-updates-and-more
section: changelog
group: "Changelog"
retrieved: 2026-09-01
---

[gtidocs](../README.md) › [Changelog](README.md) › [Changelog](README.md) › April 13th, 2026 - Visual Insights and Saved Search Integration in Agentic, SCIM Token Updates, and more

---

# april-13th,-2026---visual-insights-and-saved-search-integration-in-agentic,-scim-token-updates,-and-more

📢 **Google TI Mondays**. Quick reminder to  Follow the **Google TI Mondays** series across our social platforms every week for quick, actionable practitioner tips and product adoption advice designed to enhance your efficiency. These actionable tips are essential. **#GoogleTIMondays**

* [The Relevance System](https://www.linkedin.com/posts/googlecloudsecurity_google-threat-intelligence-monday-tips-activity-7446980092586708994-Hm4a?utm_source=share\&utm_medium=member_desktop\&rcm=ACoAABEcph8B68ZDxb6nvjnCwxDhnva9lalo1r4)

💪 **Detection Highlights**. The [Google Threat Intelligence Group](https://cloud.google.com/blog/topics/threat-intelligence?e=48754805) and [FLARE team](https://cloud.google.com/security/flare?e=48754805) continue to expand Google TI’s detection surface by developing custom YARA rules and malware configuration extractors. This week, our researchers have released detection content for 35 newly tracked malware families and updated protections for 49 existing threats. We prioritize our detection engineering efforts based on the latest malware identified during Mandiant incident response engagements, telemetry from Google SecOps customer environments, and high-interest Google TI search trends.

As we identify new threats through our research, we develop and deploy dedicated detection signatures. Some recent examples of newly tracked families include:

* [UDADOS](https://www.virustotal.com/gui/collection/malware--92d0cbea-594a-5401-b0ca-84d16ca8b212): a Windows executable written in C++ that connects to a command-and-control (C2 or C\&C) server to receive commands to perform distributed denial-of-service (DDoS) attacks against victims. It can receive C2 server updates by abusing various third-party services (GitHub, Bitbucket, Dropbox) and can also receive C2 updates via the Ethereum blockchain as URLs hidden inside transactions. See its [curated YARA detection rules](https://www.virustotal.com/gui/collection/malware--92d0cbea-594a-5401-b0ca-84d16ca8b212/rules).
* [SIDEFOX](https://www.virustotal.com/gui/collection/malware--c50e54bd-75d0-5158-9af5-48aea1991a3f): a specialized infostealer that harvests passwords, credit cards, and session tokens. By injecting code into browsers and targeting apps like Discord, Steam, and Telegram, it allows attackers to bypass user protections and hijack accounts almost instantly. See its [curated YARA detection rules](https://www.virustotal.com/gui/collection/malware--c50e54bd-75d0-5158-9af5-48aea1991a3f/rules).
* [SANTASTEAL](https://www.virustotal.com/gui/collection/malware--7761bab2-fd90-5b6b-bd85-670c12d6f5e5): a C-based malware-as-a-service (MaaS) designed for stealth, operating entirely in memory to bypass traditional detection. Functioning as a rebranding of the Blueline Stealer project, it harvests sensitive data from browsers, crypto wallets, and messaging platforms like Discord and Telegram. See its [curated YARA detection rules](https://www.virustotal.com/gui/collection/malware--7761bab2-fd90-5b6b-bd85-670c12d6f5e5/rules).
* [NULLTAP](https://www.virustotal.com/gui/collection/malware--1cfebe2e-1339-566c-8768-e7121aa2dbfe): a ransomware written in Rust capable of using a hybrid cryptographic scheme to encrypt files. The encryption logic is largely implemented via third-party crates. Extended capabilities may include updating the current desktop background. See its [curated YARA detection rules](https://www.virustotal.com/gui/collection/malware--1cfebe2e-1339-566c-8768-e7121aa2dbfe/rules).

In addition to tracking emerging threats, we consistently refine our detections for established malware to account for evolving variants. This week, we updated our YARA rules and configuration extraction capabilities for several prominent threats, including [SYSTEMBC](https://www.virustotal.com/gui/collection/malware--17784955-af55-5462-877f-feaba0c8d80a), [ARECHCLIENT2](https://www.virustotal.com/gui/collection/malware--8ec4fd10-a491-584b-b036-d48c2b6f256f), and [HAVOCDEMON](https://www.virustotal.com/gui/collection/malware--3e1f3bd1-07ad-5e43-b6fb-be34bd5c5b4a). These updates ensure that our systems can continue to extract critical indicators of compromise even as threat actors modify their tools.

[See latest malware family profiles](https://www.virustotal.com/gui/threat-landscape/malware-and-tools?filter%253D%252528origin%2525253A%25252522Google%2525252520Threat%2525252520Intelligence%25252522%252529%2526order%253Dcreation_date-) added to the knowledge base and the complete list of [curated YARA rules](https://www.virustotal.com/gui/hunting/rulesets?order=modification_date-\&filter=owner%25253AMandiant) in our database.

💪 **Visual Insights: Enhanced Industry and Country Reporting in Agentic**. [**Agentic**](https://gtidocs.virustotal.com/docs/agentic-platform) is the conversational AI platform for Google Threat Intelligence that orchestrates specialized security agents to automate complex investigative workflows. By grounding its responses in Google’s massive security dataset, it allows analysts to move from raw data to finished intelligence through natural language.

Agentic now supports **Visual Dashboards** for **Country** and **Industry** profiles, automatically populating reports with key visual insights such as:

* **World Maps:** Visualizing the geographic distribution of threat activity.
* **Geographical and Industrial Breakdowns:** Instant visualization of which sectors and regions are being targeted.
* **Categorical Charts:** Breaking down threats by motivation, malware family, actor group, etc.

This update transforms text-heavy intelligence into actionable, "at-a-glance" visual data. Analysts can now immediately identify geographical hotspots and industry-specific trends, making it easier to communicate risks to stakeholders and prioritize defense strategies based on visual density and frequency of threats.

![](https://files.readme.io/1ea24d904de61ec3edfc87742db8e4481c8d6e3109b524c23edd0f1f611a9424-image.png)

💪 **Agentic Integration for Saved Searches**. We have expanded [**Agentic**](https://gtidocs.virustotal.com/docs/agentic-platform)**’s** capabilities to include native support for [**Saved Searches**](https://gtidocs.virustotal.com/docs/saved-searches-guide). This integration allows the agent to list, filter, and execute the custom queries you and your organization have already built within the Google Threat Intelligence environment.

By operationalizing saved searches through natural language, security teams can significantly reduce "time-to-insight." Analysts can instantly generate intelligence digests based on proven query logic, ensuring high-priority threats are never overlooked during an AI session. This automation allows Agentic to process and summarize results on the fly, accelerating your investigative workflow.

**Prompt examples:**

* *"What are my saved searches?"*
* *"Show me the saved searches shared with my organization."*
* *"Run my 'Critical Log4j' saved search and summarize the findings from the last 24 hours."*

🔄 **Update to SCIM Authentication Token Format**. Following feedback and requests from our customers to align with industry-standard authentication protocols, we have updated the format of the [**SCIM Secret Token**](https://gtidocs.virustotal.com/docs/sso-authentication#scim-integration).\
The token is now provided with the `Bearer` prefix: `Bearer <token>`\
This update ensures that the configuration within your Identity Provider matches the standard Authorization header requirements.

---

← [May 4th, 2026 - Two-Factor Authentication Enforcement, Private Scanning Routing through Chile, Network Livehunt Rules + Typosquatting, Agentic + OWASP, and more](may-4th-2026-two-factor-authentication-enforcement-private-scanning-routing-through-chile-network-livehunt-rules-typosquatting-agentic-owasp-and-more.md) · [up](README.md)

*Archived from <https://gtidocs.virustotal.com/changelog/visual-insights-and-saved-search-integration-in-agentic-scim-token-updates-and-more>.*
