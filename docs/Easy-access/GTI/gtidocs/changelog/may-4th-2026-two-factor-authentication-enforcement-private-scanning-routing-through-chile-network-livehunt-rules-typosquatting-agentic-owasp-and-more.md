---
title: "May 4th, 2026 - Two-Factor Authentication Enforcement, Private Scanning Routing through Chile, Network Livehunt Rules + Typosquatting, Agentic + OWASP, and more"
source: https://gtidocs.virustotal.com/changelog/may-4th-2026-two-factor-authentication-enforcement-private-scanning-routing-through-chile-network-livehunt-rules-typosquatting-agentic-owasp-and-more
slug: may-4th-2026-two-factor-authentication-enforcement-private-scanning-routing-through-chile-network-livehunt-rules-typosquatting-agentic-owasp-and-more
section: changelog
group: "Changelog"
retrieved: 2026-09-01
---

[gtidocs](../README.md) › [Changelog](README.md) › [Changelog](README.md) › May 4th, 2026 - Two-Factor Authentication Enforcement, Private Scanning Routing through Chile, Network Livehunt Rules + Typosquatting, Agentic + OWASP, and more

---

# may-4th,-2026---two-factor-authentication-enforcement,-private-scanning-routing-through-chile,-network-livehunt-rules-+-typosquatting,-agentic-+-owasp,-and-more

📢 **Google TI Mondays.** Quick reminder to  Follow the **Google TI Mondays** series across our social platforms every week for quick, actionable practitioner tips and product adoption advice designed to enhance your efficiency. These actionable tips are essential. **#GoogleTIMondays**

* [Make the most out of Code Insight](https://www.linkedin.com/posts/google-threat-intelligence-monday-tips-ugcPost-7449879197931646977-O-42?utm_source=share\&utm_medium=member_desktop\&rcm=ACoAABEcph8B68ZDxb6nvjnCwxDhnva9lalo1r4)
* [Hunting PowerShell & VBS with Google TI](https://www.linkedin.com/posts/google-threat-intelligence-monday-tips-ugcPost-7454627987896967168-KIY3?utm_source=share\&utm_medium=member_desktop\&rcm=ACoAABEcph8B68ZDxb6nvjnCwxDhnva9lalo1r4)

📢 **Mastering the Hunt: New Practitioner-Oriented Content.** Monitoring cybercrime actors on the dark web is a complex, labor-intensive process, constantly disrupted by forum seizures and the rapid emergence of new platforms. To help you navigate this shifting landscape, our latest blog post demonstrates how to leverage Agentic and the new Deep and Dark Web (DDW) module to streamline your investigations. We showcase real-world use cases and internal hunting techniques that utilize natural language and new search modifiers to pivot through diverse data sources, eliminating the need to manually track fragmented forums.

* [Active dark web monitoring with Google Threat Intelligence and Agentic TI](https://security.googlecloudcommunity.com/community-blog-42/active-dark-web-monitoring-with-google-threat-intelligence-and-agentic-ti-7366)

💪 **Detection Highlights**. The [Google Threat Intelligence Group](https://cloud.google.com/blog/topics/threat-intelligence?e=48754805) and [FLARE team](https://cloud.google.com/security/flare?e=48754805) continue to expand Google TI’s detection surface by developing custom YARA rules and malware configuration extractors. This week, our researchers focused on updating our existing detections for many popular malware families. A few examples include:

* [SQUIDSLEEP](https://www.virustotal.com/gui/collection/malware--86ab357d-6860-5da1-bfa7-90b3e63481cb): This family was updated to include the latest indicators observed in recent campaigns and threat actor activity. See its [curated YARA detection rules](https://www.virustotal.com/gui/collection/malware--86ab357d-6860-5da1-bfa7-90b3e63481cb/rules).
* [HAVOCDEMON](https://www.virustotal.com/gui/collection/malware--3e1f3bd1-07ad-5e43-b6fb-be34bd5c5b4a): Updates to this family include expanded malware configuration extraction to better identify command-and-control infrastructure.See its [curated YARA detection rules](https://www.virustotal.com/gui/collection/malware--3e1f3bd1-07ad-5e43-b6fb-be34bd5c5b4a/rules).
* [ZIGZAG](https://www.virustotal.com/gui/collection/malware--e4e0db82-1f5e-513f-be88-156a9211544a): We have refined the YARA signatures for this family based on new samples identified through our research into active campaigns. See its [curated YARA detection rules](https://www.virustotal.com/gui/collection/malware--e4e0db82-1f5e-513f-be88-156a9211544a/rules).

[See latest malware family profiles](https://www.virustotal.com/gui/threat-landscape/malware-and-tools?filter%253D%252528origin%2525253A%25252522Google%2525252520Threat%2525252520Intelligence%25252522%252529%2526order%253Dcreation_date-) added to the knowledge base and the complete list of [curated YARA rules](https://www.virustotal.com/gui/hunting/rulesets?order=modification_date-\&filter=owner%25253AMandiant) in our database.

🔄 **Enhanced Security Control: Two-Factor Authentication (2FA) Enforcement**. The Group Management suite within the Google Threat Intelligence platform allows administrators to oversee their organization's users, service accounts, and settings. It provides a centralized interface to ensure that access to the platform aligns with corporate security policies.

The Group Administrators can now [mandate Two-Factor Authentication (2FA) for all members of their group](https://gtidocs.virustotal.com/docs/admins-guide#223-two-factor-authentication-enforcement). When enabled, this group-level setting prevents users from accessing Google Threat Intelligence features until they have configured a secondary authentication method (such as an authenticator app or offline code) on their individual accounts.

This safeguards sensitive data against credential theft while maintaining administrative control. If a user loses their 2FA device, [administrators can perform a secure reset](https://gtidocs.virustotal.com/docs/admins-guide#125-resetting-two-factor-authentication-for-a-user) to facilitate seamless re-enrollment without impacting the user's existing collections or research.

![](https://files.readme.io/00b035bfedcb32d4e2815f3258cd07fdc97701ea4e15f09796299cbb1db24d7c-image.png)

🔄 **Private Scanning Network Control: New Regional Routing through Chile**.  [**Private Scanning**](https://gtidocs.virustotal.com/docs/private-scanning) is a core capability within Google Threat Intelligence that allows organizations to analyze suspicious files and URLs in a completely isolated environment. This ensures that the analysis remains confidential and that no data is shared with the public community or third parties.\
We are expanding our global egress infrastructure by introducing **Chile** as a new routing option for Private Scanning. This marks our first network exit point in Latin America, allowing users to route the network traffic generated during dynamic analysis through a localized Chilean IP space.\
The new Chilean egress node enables **Localized Evasion Testing**, allowing analysts to bypass "geo-fencing" by observing how threats interact specifically with users in the LATAM region.

![](https://files.readme.io/6ccd2b3cfaa4db4ea08ffc88e93e23eb6fb6acedcabc3b6ce1bc18881b9b10e4-image.png)

💡 **Remember! Network Livehunt Rules + Typosquatting.** YARA is the de facto pattern-matching tool for threat intel and malware research. Google Threat Intelligence extends YARA beyond file content matching to include incoming URLs, domains, and IP addresses. By configuring [Livehunt](https://gtidocs.virustotal.com/docs/livehunt-guide) rulesets, researchers can define complex behavioral indicators to identify emerging threats and receive real-time detection notifications before they impact their environment.

Remember that now instead of manually listing dozens of permutations for a single domain, analysts can use a specific syntax to flag domains that are visually or typographically similar to their target brand or high-value infrastructure via the `vt.net.domain.permutation_of` module to specify a "distance" or "similarity" score.\
Fine-tune your detections by applying flags for specific techniques:

* `vt.Domain.Permutation.TYPO`: Detects common keyboard misspellings.
* `vt.Domain.Permutation.HOMOGLYPH`: Flags look-alike characters (e.g., using "0" for "o").
* `vt.Domain.Permutation.HYPHENATION`: Identifies unauthorized additions of hyphens.
* `vt.Domain.Permutation.SUBDOMAIN`: Spots brand names repurposed as subdomains.
* `vt.Domain.Permutation.BITSQUATTING`: Detects domains resulting from single-bit errors in hardware memory.

![](https://files.readme.io/43c9a96e442a020f3e9a19976b53814f1684a163cb6343f982c94623922be703-image.png)

💪 **Enriched Mitigations in Agentic via OWASP Integration**. [**Agentic**](https://gtidocs.virustotal.com/docs/agentic-platform) is an AI-powered analysis interface built to automate complex investigative workflows. By leveraging specialized agents with direct access to **Google Threat Intelligence** datasets and analysis engines, users can rapidly summarize threats and pivot through malicious infrastructure.

We have integrated [**OWASP**](https://owasp.org/) **(Open Worldwide Application Security Project) documentation** directly into Agentic to streamline your defense strategy. While investigating potential threats, you can now ask for mitigation advice and receive standard-aligned security guidance and best practices based on the OWASP framework.

![](https://files.readme.io/f062de3d31c731dc15cbf0162494698f7385f7328c1a28a9a474a8f2524ddc1e-image.png)

💪 **Enhanced Agentic Interaction for Dark Web Saved Searches**. We’ve improved how [**Agentic**](https://gtidocs.virustotal.com/docs/agentic-platform) handles [Saved Searches](https://gtidocs.virustotal.com/docs/saved-searches-guide) for the [Dark Web](https://gtidocs.virustotal.com/docs/dark-web-guide). You can now request an intelligence digest using natural language, prompting the agent to cross-reference forums, pastes, etc, to deliver actionable insights based on your specific saved logic.

![](https://files.readme.io/4c72b3bf15038c42d43d7e8433b5e460c83d6eb00b336df82f7e5ac5d3e986a5-image.png)

💪**Enhanced Visibility in Agentic: Data Visualization and Real-time Analysis Tracking**. We have introduced two major visibility upgrades to Google TI’s Agentic tool:

* **We’ve added a live progress indicator for background malware analyses**. Users can now see the progress of background Malware Analysis in real-time.

![](https://files.readme.io/d63a2fdd5b3210d6c8cb737a499e55481cc6390ea2bcf87caf25cda82a07a695-image.png)

* **We've upgraded how you interpret threat data with the addition of automated chart generation**. When requesting statistical breakdowns, the platform now renders **Pie Charts, Bar Charts, and World Maps** directly in the UI, delivering an immediate, 'at-a-glance' understanding of data trends.

![](https://files.readme.io/a48f95e2febe41515d37b8bbe9c07c1b32ecb391a5df8128bde1209ccea08464-image.png)

---

← [May 18th, 2026 - Automated Package Sandbox Detonation, Advanced Attribute Pivoting, Expanded Collections & Deep Malware Format Analysis in Agentic, CAPA Binary Enhancements, and more](may-18th-2026-automated-package-sandbox-detonation-advanced-attribute-pivoting-expanded-collections-deep-malware-format-analysis-in-agentic-capa-binary-enhancements-and-more.md) · [up](README.md) · [April 13th, 2026 - Visual Insights and Saved Search Integration in Agentic, SCIM Token Updates, and more](visual-insights-and-saved-search-integration-in-agentic-scim-token-updates-and-more.md) →

*Archived from <https://gtidocs.virustotal.com/changelog/may-4th-2026-two-factor-authentication-enforcement-private-scanning-routing-through-chile-network-livehunt-rules-typosquatting-agentic-owasp-and-more>.*
