---
title: "Issues Severity Definitions and Examples"
source: https://gtidocs.virustotal.com/docs/issues-severity-definitions
slug: issues-severity-definitions
section: guides
group: "ASM"
updatedAt: 2025-09-25T02:27:54.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [ASM](../README.md) › [Issues](../issues-guide.md) › Issues Severity Definitions and Examples

---

# issues-severity-definitions-and-examples

# asm-issue-severity-definitions-and-examples-|-docs

This document describes how Attack Surface Management (ASM) determines the severity ratings for Issues.

## confidence-level-of-issues

ASM uses triage categories to determine whether an Issue needs further investigation or is ready for review.

* **Confirmed**: ASM has high confidence in the finding.
* **Potential**: There is a known vulnerability related to this Entity, but ASM cannot confirm that this is true in this case.

Google Threat Intelligence recommends prioritizing Confirmed Issues.

## prioritization-of-issues

Google TI recommends giving priority to the resolution of [Critical](#Critical) and [High](#High) severity Issues in order to strengthen the Entities associated with these Issues. As a customer, you iterate on the ASM program. You and other team members discuss how you can effectively triage [Medium](#Medium) and [Low](#Low) severity Issues over time. Discussions could be about a ticketing system or whether channels of communication are open to infrastructure or technology owners.

The following table, Issue Severity Definitions, outlines a common understanding of the risks of vulnerability, misconfiguration, and exposure.

| **Issue Severity** | **Definitions** | **Examples** |
| --- | --- | --- |
| <span id="Critical">Critical</span> | The asset has an increased risk of exploitation based on activity observed in the wild, or the potential exposure and data leakage will negatively affect the organization. Successful exploitation could allow a threat actor to achieve persistence, lateral movement, account compromise, or data exfiltration. A CVE [CVSS](https://nvd.nist.gov/vuln-metrics/cvss) 9.0-10.0 and a Critical Risk Rating from Mandiant validate the issue severity.<br/>Suggested Usage:<br/>-   Investigate within 24 Hours<br/>-   Remediate within 7 Days | <br/>-   Gitlab - Account Takeover via SCIM ([CVE-2022-1680](https://nvd.nist.gov/vuln/detail/cve-2022-1680))<br/>-   Atlassian Confluence Server - Arbitrary Code Execution ([CVE-2022-26134](https://nvd.nist.gov/vuln/detail/cve-2022-26134))<br/>-   vBulletin Unauthenticated Remote Code Execution ([CVE-2019-16759](https://nvd.nist.gov/vuln/detail/cve-2019-16759))<br/>-   Log4j aka Log4Shell Unauthenticated Remote Code Execution ([CVE-2021-44228](https://nvd.nist.gov/vuln/detail/cve-2021-44228)) |
| <span id="High">High</span> | The asset has a vulnerability, misconfiguration, or exposure that, when exploited or leveraged by a threat actor, can enable them to achieve persistence or lateral movement or perform unauthenticated actions. CVEs with a [CVSS](https://nvd.nist.gov/vuln-metrics/cvss) of 7.0-8.9 or a High Risk Rating from Mandiant Threat Intelligence generate high severity Issues.<br/>Suggested Usage:<br/>-   Investigate within 48 Hours<br/>-   Remediate within 14 Days | <br/>-   Exposed RDP or SMB<br/>-   [Command and Control (C2) Server](https://csrc.nist.gov/glossary/term/command_and_control) Identified<br/>-   World Writeable AWS S3 Bucket |
| <span id="Medium">Medium</span> | The asset is vulnerable; however, the affect of exploitation is offset by hardening methods such as MFA or additional access requirements that hinder a threat actor from achieving their mission.<br/>Suggested Usage:<br/>-   Investigate within 72 Hours<br/>-   Remediate within 21 Days | <br/>-   Exposed VPN Service<br/>-   Exposed Databases<br/>-   A 2FA which can be bypassed<br/> |
| <span id="Low">Low</span> | The asset has a vulnerability, misconfiguration, or exposure that can further a threat actor's reconnaissance effort, but does not pose an immediate risk.<br/>In some organizations, low severity Issues are considered acceptable.<br/>Suggested Usage:<br/>-   Investigate within 4 Days<br/>-   Remediate within 28 Days | <br/>-   World Readable AWS S3 Buckets<br/>-   Wildcard Certificates<br/>-   Security Headers Missing from URL |
| Informational | Security hygiene insights that do not require immediate attention but should be addressed during ongoing efforts to improve security posture. You may choose to delegate informational Issues to the appropriate team. <br/>Suggested Usage:<br/>-   Investigate within 1 Month<br/>-   Remediate within 3 Months | <br/>-   Self-signed Certificates<br/>-   Deprecated SSL/TLS Protocols<br/>-   Insecure Cookies |

## numeric-severity

A numeric severity system is used when configuring some [ASM outbound integrations](../outbound-integrations.md). The following table outlines the numbers associated with each Issue Severity level in ASM.

| **Issue Severity** | **Numeric representation** |
| ------------------ | -------------------------- |
| Critical           | 1                          |
| High               | 2                          |
| Medium             | 3                          |
| Low                | 4                          |
| Informational      | 5                          |

---

← [Create Issues from Inferred CVEs](issues-creation.md) · [up](../README.md) · [How Issues Work](how-issues-work.md) →

*Archived from <https://gtidocs.virustotal.com/docs/issues-severity-definitions>.*
