---
title: "Analyzing SSL/TLS Issues"
source: https://gtidocs.virustotal.com/docs/analyzing-ssltls-issues
slug: analyzing-ssltls-issues
section: guides
group: "ASM"
updatedAt: 2025-09-25T01:59:32.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [ASM](../README.md) › [Guides](../guides.md) › Analyzing SSL/TLS Issues

---

# analyzing-ssl/tls-issues

For SSL/TLS vulnerability analysis in Attack Surface Management (ASM), two Issues are available:

* **Deprecated SSL/TLS Protocol Configured**: A vulnerability results when a server is configured to allow a deprecated SSL/TLS protocol.
* **Weak SSL/TLS Ciphers Enabled**: A vulnerability results when a server is configured to support a SSL/TLS cipher with a known low-sequence of encryption.

## ssl/tls-vulnerabilities-in-the-issue-definition-library

These Issues are defined in the Issue Definition Library. To locate both definitions, go to **Projects and Settings** > **Library**. From there, select **[Issue Definitions](https://asm.advantage.mandiant.com/explorer/issues)**. Once the page comes up, enter **SSL** in the **Search for issues** bar.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_guides_analyzing_ssl_issues_library_20241015.png)

## access-ssl/tls-issues

To access specific Issues classified under either of these Issue Definitions, select the **Issues** tab in ASM. Add **SSL** to the search bar and click **Enter**. Select **Issue** from the **Grouped by** drop down to cluster all SSL/TLS vulnerabilities that are present. 

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_guides_analyzing_ssl_issue_20241015.png)

Click the **Expand** button to view a list of individual issues within each category.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_guides_analyzing_ssl_expand_20241015.png)

Choose one of the URLs from this list to explore more detailed **Description**, **References**, **Proof**, and **Raw (JSON)** information.

## examples

### example-1

In this example, the **Proof** for a **Deprecated SSL/TLS Protocol Detected** Issue shows that `version 1` of SSL protocol is enabled in the source.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_guides_analyzing_ssl_example1_20241015.png)

## example-2

In this example, the **Proof** for a **Weak** **SSL/TLS Ciphers Enabled** Issue shows that known-weak SSL/TLS ciphers, `TLSv1.2`, is present in the source.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_guides_analyzing_ssl_example2_20241015.png)

---

← [Bulk Select](bulk-select.md) · [up](../README.md) · [Search Syntax for Attack Surface Management](asm-search-syntax.md) →

*Archived from <https://gtidocs.virustotal.com/docs/analyzing-ssltls-issues>.*
