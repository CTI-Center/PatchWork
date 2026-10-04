---
title: "May 25th, 2026 - Advanced HTA & Office Document Analysis + Persistent File System in Agentic, macOS CDHash Extraction, 3rd-Party Integrations, Threat Profiles Bulk IoC Downloads, Collections Expansion, and more"
source: https://gtidocs.virustotal.com/changelog/may-25th-2026-advanced-hta-office-document-analysis-persistent-file-system-in-agentic-macos-cdhash-extraction-3rd-party-integrations-threat-profiles-bulk-ioc-downloads-collections-expansion-and-more
slug: may-25th-2026-advanced-hta-office-document-analysis-persistent-file-system-in-agentic-macos-cdhash-extraction-3rd-party-integrations-threat-profiles-bulk-ioc-downloads-collections-expansion-and-more
section: changelog
group: "Changelog"
retrieved: 2026-09-01
---

[gtidocs](../README.md) › [Changelog](README.md) › [Changelog](README.md) › May 25th, 2026 - Advanced HTA & Office Document Analysis + Persistent File System in Agentic, macOS CDHash Extraction, 3rd-Party Integrations, Threat Profiles Bulk IoC Downloads, Collections Expansion, and more

---

# may-25th,-2026---advanced-hta-&-office-document-analysis-+-persistent-file-system-in-agentic,-macos-cdhash-extraction,-3rd-party-integrations,-threat-profiles-bulk-ioc-downloads,-collections-expansion,-and-more

📢 **Google TI Mondays.** Quick reminder to  Follow the **Google TI Mondays** series across our social platforms every week for quick, actionable practitioner tips and product adoption advice designed to enhance your efficiency. These actionable tips are essential. **#GoogleTIMondays**

* [Scale Your Hunt: IoT Malware exploration with Google TI](https://www.linkedin.com/posts/google-threat-intelligence-monday-tips-ugcPost-7462185284185690112-MmAZ/?utm_source=share\&utm_medium=member_desktop\&rcm=ACoAABEcph8B68ZDxb6nvjnCwxDhnva9lalo1r4)

💪 **Detection Highlights**. The [Google Threat Intelligence Group](https://cloud.google.com/blog/topics/threat-intelligence?e=48754805) and [FLARE team](https://cloud.google.com/security/flare?e=48754805) continuously develop and update Google Threat Intelligence's YARA rules to defend against emerging threats. This week, we released YARA rules covering 3 newly tracked malware families. Our detection updates prioritize malware families actively observed in Mandiant incident response engagements, Google SecOps customer environments, and top Google Threat Intelligence search trends.

As we identify new malware families through our research, we build and deploy detection signatures. Some recent examples include:

* [SALATSTEALER](https://www.virustotal.com/gui/collection/malware--bb5effff-8c9f-55fe-93eb-ea5e2c2021f5): a Go-based crypto stealer that targets Windows browsers, cryptocurrency wallets, and Telegram clients (specifically Telegram Desktop and Kotatogram). It is capable of hijacking webcams and microphones to stream data directly to a C2 server.
* [SCARLETSMASHER](https://www.virustotal.com/gui/collection/malware--b822862e-aef2-5e47-9afd-34c9c986f32a): a Downloader used to download, compile and execute C# .NET code. See its [curated YARA detection rule](https://www.virustotal.com/gui/collection/malware--b822862e-aef2-5e47-9afd-34c9c986f32a/rules).
* [LAGUNARAT](https://www.virustotal.com/gui/collection/malware--d832c9cf-e8d0-591d-ba15-c7c151a9b3ad): a .NET-based Remote Access Trojan (RAT)  backdoor designed to execute PowerShell commands, manipulate files on the host communicating with C2. See its [curated YARA detection rule](https://www.virustotal.com/gui/collection/malware--d832c9cf-e8d0-591d-ba15-c7c151a9b3ad/rules).

In addition to providing detection rules for new and emerging threats, we continue to update our YARA rules for existing threats like [VIDAR](https://www.virustotal.com/gui/collection/malware--33210862-613c-5089-a565-c9fb1cc4adfc), [EMPIRE](https://www.virustotal.com/gui/collection/malware--2c61638a-d5b0-53ae-a009-922395861239), and [EVILPUFFIN](https://www.virustotal.com/gui/collection/malware--e8e67ea7-ec15-5959-8f1e-d5d8beb311f6). These updates ensure you have the latest coverage against active and evolving campaigns.

[See latest malware family profiles](https://www.virustotal.com/gui/threat-landscape/malware-and-tools?filter%253D%252528origin%2525253A%25252522Google%2525252520Threat%2525252520Intelligence%25252522%252529%2526order%253Dcreation_date-) added to the knowledge base and the complete list of [curated YARA rules](https://www.virustotal.com/gui/hunting/rulesets?order=modification_date-\&filter=owner%25253AMandiant) in our database.

💪 **New Threat Profiles Option: Bulk Download IoCs**. [**Threat Profiles**](https://gtidocs.virustotal.com/docs/manage-threat-profiles) provides a personalized, dynamic lens that filters Google Threat Intelligence’s vast datasets to highlight the specific Threat Actors, Campaigns, Malware, etc, most relevant to your organization based on your custom risk criteria. By tailoring these recommendations, security teams can filter out the noise and focus on the most critical exposures.

To help teams move faster from raw visibility to active enforcement, we have introduced a new feature to bulk-export Indicators of Compromise (IoCs) directly from your personalized profile recommendations. Exports are available in **JSON, CSV, or STIX** formats, with the option to include or exclude **IoC** metadata.

You can also automate this data retrieval via two newly introduced [API endpoints](../reference/02-global-landscape/threat-profiles/threat-profile-download.md):

* **`GET /threat_profiles/{id}/download`**: Exports a package containing all actionable IoCs linked to a specific Threat Profile.
* **`GET /threat_profiles/{id}/download_url`**: Retrieves the download URL to export packages exceeding 32MB.

![](https://files.readme.io/12e6bb300acb3e5fae8d5a7ecfd0a64b0c671c2d068c23b5d82be1e72f45224d-image.png)

💪**Improved MacOS File Reports: `self-signed` Tag & CDHash Extraction.** Our platform's `codesign` parser helps security analysts evaluate the validity and trustworthiness of a file's digital signature. By exposing structural traits like certificate chains, validity periods, and issuer details directly inside the file report, it allows teams to quickly triage files, isolate spoofed signatures, and understand code execution rights without needing to reverse-engineer binaries locally.

* **New `self-signed` Tag:** The codesign report now explicitly flags macOS binaries that are signed using self-issued certificates. This joins our existing suite of signature status indicators, such as `invalid-signature` and `revoked-cert`.
* **CDHash Extraction:** The parser now extracts and displays the Code Directory Hash (**CDHash**)—the unique 20-byte cryptographic identifier used by Apple’s operating systems to verify the integrity and authenticity of a code-signed binary or bundle.

See search [example](https://www.virustotal.com/gui/search?query=entity%3Afile+tag%3Aself-signed+sigcheck%3Ae7060994e5b95dc8bb23e7e45e1a7cf4efbf0ddb\&type=files): `entity:file tag:self-signed sigcheck:e7060994e5b95dc8bb23e7e45e1a7cf4efbf0ddb`

![](https://files.readme.io/e2d193f7b14d77a55ba57bc566a4d07f60bc0cff2292ba0c30d27046ec1600f1-image.png)

🔄 **Expanded Collections: Create your Actors, Malware,Toolkits, Campaigns and Reports**. Google Threat Intelligence organizes the global threat landscape using high-level tracking entities, collectively referred to as threat objects or structural collections. These specifically include **Threat Actors, Malware Families, Software Toolkits, Campaigns, IoC Collections, and Reports**. They serve as the analytical glue that contextualizes indicators into structured global profiles elevating security investigations from disjointed forensic indicators to an overarching strategic narrative.

We have expanded our collections framework to allow users to natively create their own **Threat Actors**, **Campaign**, **Malware Families**,  **Software Toolkits** and **Report** entities directly within the platform, rather than being limited to IoC Collections only. All user-created objects default to **private**, ensuring strict data privacy while remaining fully shareable with specific teammates or your entire group directory.

Creating these entities allows teams to blend localized incidents with Google’s global dataset, mapping out zero-day behaviors and custom attacker profiles instantly rather than waiting for vendor attribution. This standardizes threat documentation across the organization while accelerating hunting attribution by automatically linking incoming infrastructure to custom-defined adversary groups.

![](https://storage.googleapis.com/gtidocresources/changelog/images/gtichangelog_may25_privatecollections_20260604.png)

💪 **New 3rd-party integrations**. Integrations are vital to operationalizing Google Threat Intelligence, converting raw security insights into immediate, effective defensive action. These crucial integrations help organizations eliminate siloed data and dramatically enhance their security ecosystem, boosting efficiency and accelerating Mean Time to Resolution (MTTR).

New integrations released:

* [Analyst1](https://docs.analyst1.com/help/activate-the-google-threat-intelligence-evidence-source)
* [Fortinet FortiGuard](https://docs.fortinet.com/document/fortisoar/3.1.1/fortinet-fortiguard-threat-intelligence/598/fortinet-fortiguard-threat-intelligence-v3-1-1)
* [AWS GuardDuty](https://github.com/VirusTotal/gti-aws-GuardDuty/blob/main/README.md)
* [Cyware Intel Exchange](https://techdocs.cyware.com/ctix/en/google-threat-intelligence.html#google-threat-intelligence-946214)
* [Sumo Logic](https://www.sumologic.com/help/docs/send-data/hosted-collectors/cloud-to-cloud-integration-framework/google-threat-intel-source/)
* [Crowdstrike](https://marketplace.crowdstrike.com/listings/google-threat-intelligence-soar-actions/)
* [TheHive](https://github.com/TheHive-Project/Cortex-Analyzers/blob/master/analyzers/GoogleThreatIntelligence/README.md)
* [ServiceNow](https://store.servicenow.com/store/app/07f781de4798bed4392d3369126d4370#linksAndDocuments)
* [Fortinet FortiSOAR](https://docs.fortinet.com/document/fortisoar/1.0.0/google-threat-intelligence/100)
* [SecOps](https://github.com/chronicle/ingestion-scripts/tree/main/google_threat_intelligence)
* [Jira Cloud](https://github.com/crestdatasystems/gti-for-jira-cloud/blob/main/ReleaseDocumentationAndUserGuide.pdf)
* [Mimecast](https://integrations.mimecast.com/tech-partners/google-threat-intelligence/)

See all available 3rd-party integrations [here](https://gtidocs.virustotal.com/docs/technology-integrations-list).

🆕 **Agentic Updates: Persistent File System for Autonomous Malware Analysis**. [**Agentic**](https://gtidocs.virustotal.com/docs/agentic-platform) is the AI-powered conversational interface within Google Threat Intelligence designed to automate complex investigative workflows and accelerate threat hunting. By leveraging specialized AI agents with direct access to extensive GTI datasets and underlying analysis engines, it eliminates manual pivoting and automates multi-step investigations. Using natural language prompt templates, Agentic seamlessly translates raw indicator data and summarizes intricate malicious logic, transforming how security analysts interact with complex threat contexts.

We are introducing advanced autonomous malware analysis capabilities powered by a new persistent, stateful File System integration for the Agentic platform. Moving beyond traditional, transactional per-prompt analysis, this update provisions the agent with an isolated environment during its session, enabling it to autonomously explore directories, read configuration files, and extract intermediate code. By carrying evidence forward across an extended, multi-stage timeline, the agent can now execute comprehensive, deep-dive investigations into complex malware behaviors seamlessly.

![](https://files.readme.io/4504152ba63e445112b97cc639aca0abb77e27283ce2d5b3b23c096a6cb99370-image.png)

💪 **HTA Analysis and De-obfuscation in Agentic**. [Agentic](https://gtidocs.virustotal.com/docs/agentic-platform) now features specialized support for analyzing and de-obfuscating HTML Application (HTA) files which are frequent initial access vectors used by threat actors to execute malicious code via trusted Windows utilities like mshta.exe. This enhancement allows the agent to dissect complex, heavily obfuscated HTA files while automatically filtering out noise to prevent context overload.\
During analysis, the agent automatically extracts critical indicators, providing:

* **Advanced Evasion Detection**: The agent immediately spots malware attempting to evade detection by masquerading as legitimate software (e.g., fraudulent NVIDIA updates).
* **Deep Code De-obfuscation**: It natively decodes complex, custom encryption schemes (such as XOR layers) to reveal the underlying malicious script.
* **Full Attack Chain Visibility**: It automatically extracts hidden secondary payloads and identifies Command & Control (C2) infrastructure, giving analysts a complete picture of the threat vector.

![](https://files.readme.io/4c6fc7c80f171929bc05581ab1775eef4f71cbb2022877f20a59c948189a4cb6-image.png)

💪  **Advanced Office Document Analysis in Agentic**. We have implemented a highly structured, decision-tree-based approach for analyzing Microsoft Office documents (Word, Excel, RTF) to reliably identify malicious macros, exploits, and embedded objects. This update allows the agent to systematically run specialized analysis tools, evaluate the results against embedded expert rules, and deliver a definitive verdict (**BENIGN**, **SUSPICIOUS**, or **MALICIOUS**).

Key Capabilities:

* **Macro Heuristics & De-obfuscation:** Automatically detects and analyzes suspicious VBA and Excel 4.0 macros, peeling back obfuscation layers to reveal hidden payloads.
* **Exploit Detection:** Identifies known exploit patterns and initial access techniques, such as Equation Editor overflows and malicious remote template injections.
* **Structured Reporting:** Generates a clean, analyst-ready report complete with a clear logical reasoning chain and raw supporting evidence.

![](https://files.readme.io/9d2f7941359babe17093bdc6db26ab685bf3298ffb2d47a4f77871b261de7adf-image.png)

---

← [June 18th, 2026 — Crowdsourced AI += Knostic, Self-Service API Key Rotation, domain_exact: Search Modifier, and Advanced Agentic Disassembly & Relationship Mapping](june-22nd-2026-crowdsourced-ai-knostic-self-service-api-key-rotation-domain_exact-search-modifier-and-advanced-agentic-disassembly-relationship-mapping.md) · [up](README.md) · [May 18th, 2026 - Automated Package Sandbox Detonation, Advanced Attribute Pivoting, Expanded Collections & Deep Malware Format Analysis in Agentic, CAPA Binary Enhancements, and more](may-18th-2026-automated-package-sandbox-detonation-advanced-attribute-pivoting-expanded-collections-deep-malware-format-analysis-in-agentic-capa-binary-enhancements-and-more.md) →

*Archived from <https://gtidocs.virustotal.com/changelog/may-25th-2026-advanced-hta-office-document-analysis-persistent-file-system-in-agentic-macos-cdhash-extraction-3rd-party-integrations-threat-profiles-bulk-ioc-downloads-collections-expansion-and-more>.*
