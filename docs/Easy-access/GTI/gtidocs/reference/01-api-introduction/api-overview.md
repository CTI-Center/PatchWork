---
title: "Google Threat Intelligence API Overview"
source: https://gtidocs.virustotal.com/reference/api-overview
slug: api-overview
section: reference
group: "API Introduction"
updatedAt: 2025-09-25T00:33:23.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API Introduction](README.md) › Google Threat Intelligence API Overview

---

# google-threat-intelligence-api-overview

> 🚧 Commonly missed
>
> **Looking for more API quota and additional threat context?**\
> [Contact us](https://www.virustotal.com/gui/contact-us/premium-services) to learn more.
>
> **Looking for your Google Threat Intelligence API key?**\
> Jump to [your personal API key](https://www.virustotal.com/gui/my-apikey) view while signed in to Google TI.
>
> **Do you want to integrate into Splunk, Cortex XSOAR or other technologies?**\
> Enrich your security events, automatically triage alerts and boost detection confidence leveraging our ubiquitous integrations in 3rd-party platforms such as [Splunk SIEM](https://splunkbase.splunk.com/app/7351), [Cortex XSOAR Google Threat Intelligence](https://xsoar.pan.dev/docs/reference/integrations/google-threat-intelligence), [Cortex XSOAR Google Threat Intelligence IoC Stream Feed](https://xsoar.pan.dev/docs/reference/integrations/google-threat-intelligence-io-c-stream-feed), [MISP Google Threat Intelligence](https://misp.github.io/misp-modules/expansion/#google_threat_intelligence) and others ([see more](https://gtidocs.readme.io/docs/technology-integrations-list)).

Our API was designed with ease of use and uniformity in mind and it is inspired in the <http://jsonapi.org/> specification. It follows the [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) principles and has predictable, resource-oriented URLs. It uses JSON for requests and responses, including errors.

API exposes rich data in terms of: IoC relationships, sandbox dynamic analysis information, static information for files, YARA Livehunt & Retrohunt management, crowdsourced detection details, etc.

## most-popular-api-endpoints

* [Upload a file for scanning](../03-ioc-investigation/files/files-scan.md): analysis your file with 70+ antivirus products, 10+ dynamic analysis sandboxes and a myriad of other security tools to produce a threat score and relevant context to understand it.
* [Get a file report by hash](../03-ioc-investigation/files/file-info.md): given a \{md5, sha1, sha256} hash, retrieves the pertinent analysis report including threat reputation and context produced by 70+ antivirus products, 10+ dynamic analysis sandboxes and a myriad of other security tools and datasets.
* [Scan URL](../03-ioc-investigation/urls/scan-url.md): analysis your URL with 70+ antivirus products/blocklists and a myriad of other security tools to produce a threat score and relevant context to understand it.
* [Get a URL analysis report](../03-ioc-investigation/urls/url-info.md): given a URL, retrieves the pertinent analysis report including threat reputation and context produced by 70+ antivirus products/blocklists and a myriad of other security tools and datasets.
* [Get a domain report](../03-ioc-investigation/domains-resolutions/domain-info.md): given a domain, retrieves the pertinent analysis report including threat reputation and context produced by 70+ antivirus products/blocklists and a myriad of other security tools and datasets.
* [Get an IP address report](../03-ioc-investigation/ip-addresses/ip-info.md): given an IP address, retrieves the pertinent analysis report including threat reputation and context produced by 70+ antivirus products/blocklists and a myriad of other security tools and datasets.

---

[up](README.md) · [API responses](api-responses.md) →

*Archived from <https://gtidocs.virustotal.com/reference/api-overview>.*
