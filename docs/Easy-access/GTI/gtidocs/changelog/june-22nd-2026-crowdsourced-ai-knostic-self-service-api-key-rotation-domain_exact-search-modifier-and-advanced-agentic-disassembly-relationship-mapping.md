---
title: "June 18th, 2026 — Crowdsourced AI += Knostic, Self-Service API Key Rotation, domain_exact: Search Modifier, and Advanced Agentic Disassembly & Relationship Mapping"
source: https://gtidocs.virustotal.com/changelog/june-22nd-2026-crowdsourced-ai-knostic-self-service-api-key-rotation-domain_exact-search-modifier-and-advanced-agentic-disassembly-relationship-mapping
slug: june-22nd-2026-crowdsourced-ai-knostic-self-service-api-key-rotation-domain_exact-search-modifier-and-advanced-agentic-disassembly-relationship-mapping
section: changelog
group: "Changelog"
retrieved: 2026-09-01
---

[gtidocs](../README.md) › [Changelog](README.md) › [Changelog](README.md) › June 18th, 2026 — Crowdsourced AI += Knostic, Self-Service API Key Rotation, domain_exact: Search Modifier, and Advanced Agentic Disassembly & Relationship Mapping

---

# june-18th,-2026-—-crowdsourced-ai-+=-knostic,-self-service-api-key-rotation,-domain_exact:-search-modifier,-and-advanced-agentic-disassembly-&-relationship-mapping

## 🚀-crowdsourced-ai-expansion:-knostic.ai

We are excited to announce the addition of **knostic.ai** to our crowdsourced AI section. Using Knostic's **AgentMesh** engine, this integration provides a specialized AI-driven analysis stream for **Visual Studio Code extension (.VSIX)** files to identify critical vulnerabilities and deliberate backdoor behaviors.

Knostic assigns a clear scan verdict (**BENIGN**, **SUSPICIOUS**, or **MALICIOUS**) coupled with a risk level (such as **SAFE**, **MEDIUM**, or **CRITICAL**). Security analysts can now search and filter across these results in Intelligence search using the new [knostic\_ai\_verdict:](https://www.virustotal.com/gui/search?query=knostic_ai_verdict%3Amalicious\&type=files) and [knostic\_ai\_analysis:](https://www.virustotal.com/gui/search?query=knostic_ai_analysis%3A%22data+exfiltration%22\&type=files) operators.

**Example Analyses:**

* ​[cfdf72c510670341dce392ab250a5f5ff2a398d993d1106fb8026ec6397cb393](https://www.virustotal.com/gui/file/cfdf72c510670341dce392ab250a5f5ff2a398d993d1106fb8026ec6397cb393/detection)
* ​[3dc62e65586a9aeeb8521e7824d48abd59cec209d68b87f73a9bbadbd98dc51a](https://www.virustotal.com/gui/file/3dc62e65586a9aeeb8521e7824d48abd59cec209d68b87f73a9bbadbd98dc51a/detection)

![](https://files.readme.io/405a07b98d55254eb2cd56e634bfa4f5480889e5c1bb5580f0250e71eaa1830b-Screenshot_2026-06-18_at_14.29.02.png)

**About Knostic:** Knostic's Kirin platform governs how AI agents and developer extensions interact with internal systems, neutralizing supply-chain risks at the source.

### 🔍-advanced-search:-`domain_exact:`-modifier

Intelligence search now includes the `domain_exact:` modifier. This new tool allows for exact-domain matching, complementing the existing `domain:` (substring) and `domain_regex:` operators. It is specifically designed for targeting a single domain without the noise of partial matches.

See all advanced search modifiers [here](https://gtidocs.virustotal.com/docs/domain-search-modifiers)

### 🔑-self-service-api-key-rotation

Enterprise customers can now independently cycle their credentials directly from the user interface. This self-service functionality eliminates the need for support tickets for routine security updates.

* **What's New:** A "Rotate API Key" button is now live on the API key management page.

![](https://files.readme.io/1973f4051e3f9d688ad6c68b7795bdf056124bb635a816b7c6718ee7f5b07acf-Screenshot_2026-06-18_at_14.32.24.png)

* **Why It Matters:** Enables instant response to potential compromises and adherence to internal rotation policies.
* **Note:** Generating a new key instantly ***invalidates*** the previous one; ensure active tools are updated immediately.

### 🤖-google-ti-agentic-updates

#### declarative-relationship-mapping-(graphviz-&-mermaid)

The agent can now compile and natively render structural relationship diagrams using **Graphviz DOT** and **Mermaid** syntax. This is ideal for investigating complex infection chains or infrastructure overlaps directly in the chat.

* [🎥 Demo Session](https://www.virustotal.com/gui/agentic/shared/gAAAAABqKIIyuKo_Q0FQq8btRdugpRZhCv3_PsrSFptN572ptLwFn4WIrkvATSSRYZvBCad_DmUIvYC2kLow1eK0lTN1GAvpbaAdoeIOXIkhTUudS4PK6XjEziqt6-2Vd5MXSpVNJUARNNCopqSODOsxn2MLJOuVxrM4rEX_I2d6YC4xgkCvUf8iExMdWlKpNrgd0We_cMEs)

#### advanced-powershell-disassembly-&-speakeasy-cpu-emulation

Agent is now able to autonomously unpack, de-obfuscate, and dynamically emulate multi-stage Living-off-the-Land (LotL) PowerShell droppers using extended Speakeasy CPU emulation, dissecting embedded byte arrays and memory injection routines.

* [🎥 Demo Session](https://www.virustotal.com/gui/agentic/shared/gAAAAABqKH0W3kvTSH4MaM1iasxtr6TEvoaJCikrZ-KhJ3hAHXqFAujRqtQxVLeGctkV0uFW8ikRjKcl7yfdyGgZtAocva3FXMghfq-TEw2AFmVarbEes05KwRzH-kPtBjgTCUBxwUM0ahJj5Iu6NAk7jux2yvYt8myH6mTsnaVi7kNCyWsVxrniiuaMx1lNfSbVFSGjW2jz)

#### multi-platform-.net-disassembly-&-enriched-filesystem-navigation

Seamlessly bridge multi-platform infection handoffs. The agent navigates internal resources of **.NET executables** to mount embedded files and disassemble secondary Living-off-the-Land (LotL) payloads.

* [🎥 Demo Session](https://www.virustotal.com/gui/agentic/shared/gAAAAABqKIl3Vb5bxVdQ2eRQrBrOBBnuq9XFzblsknci0I1a4EKHRoVp7ss8LKmrmETE9dNLJN2g8UHzlVuBbk2p8vi993E4UhhlzdAFZ7KGEc0Q-pa9HYntsYy9Yx-3ZpypP5N4teead3bfE6EJH-suD9Ofxa6iew%3D%3D)

#### javascript-sandboxing-&-multi-pass-de-obfuscation

A dedicated analysis engine for heavily obfuscated **JavaScript threats** is now live. The agent performs multi-pass AST de-obfuscation via Restringer and evaluates routines inside an isolated sandbox.

* [🎥 Demo Session](https://www.virustotal.com/gui/agentic/shared/gAAAAABqKItUljMwxRXMEKuEPjNXF8GTsTfMZKY_qcs5lxmddwJKuu61moUehDnjFrWlEVMEWQj40pPl8dz5gvPJvQ0FNuZ6Y847-tv3iMv7McF8yLhmUeNEODz5fPw5Nj1s4-EzuN5mh3E53C26UO6n8EFV-lEINQ%3D%3D)

<br />

---

← [June 30th, 2026 — Splunk Observed Threats, GTI Score Explainability, and Private Scanning Access Control Lists (ACLs)](june-29th-2026-splunk-observed-threats-gti-score-explainability-and-private-scanning-access-control-lists-acls.md) · [up](README.md) · [May 25th, 2026 - Advanced HTA & Office Document Analysis + Persistent File System in Agentic, macOS CDHash Extraction, 3rd-Party Integrations, Threat Profiles Bulk IoC Downloads, Collections Expansion, and more](may-25th-2026-advanced-hta-office-document-analysis-persistent-file-system-in-agentic-macos-cdhash-extraction-3rd-party-integrations-threat-profiles-bulk-ioc-downloads-collections-expansion-and-more.md) →

*Archived from <https://gtidocs.virustotal.com/changelog/june-22nd-2026-crowdsourced-ai-knostic-self-service-api-key-rotation-domain_exact-search-modifier-and-advanced-agentic-disassembly-relationship-mapping>.*
