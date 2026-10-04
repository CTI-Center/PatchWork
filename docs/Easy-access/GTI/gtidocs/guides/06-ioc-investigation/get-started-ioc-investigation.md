---
title: "Get started with IOC Investigation"
source: https://gtidocs.virustotal.com/docs/get-started-ioc-investigation
slug: get-started-ioc-investigation
section: guides
group: "IOC Investigation"
updatedAt: 2025-09-25T02:35:31.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [IOC Investigation](README.md) › Get started with IOC Investigation

---

# get-started-with-ioc-investigation

## introduction

Google Threat Intelligence has a vast repository containing millions of files (malware, clean software, documents, etc.), urls, ips, domains and its associated behavior and metadata collected from various sources. This wealth of data provides a valuable resource for threat hunters and security researchers to discover new threats, track threat evolution and develop detection rules. IOC Investigation provides a suite of tools and features to help you navigate and analyze its corpus.

## brief-overview:-how-ioc-investigation-works

Everyday, users around the world upload millions of files, urls, ips and domains for checking, this artifacts are analyzed, metadata and relationships extracted, and top security vendors give their verdict on its maliciousness. This information is gathered into reports that show all the information related to them, where users can assess it and act in consecuence.

![file report example](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/file_report_20240723.png)

## ioc-analysis

To know the basics on checking on individual files, URLs, IPs, or domains and get a report on them, you can follow this **[documentation.](check-vt.md)** More advanced searches are called **[Intelligence](intelligence/file-search-modifiers.md)**, where you use search modifiers to filter on metadata, relationships, behavior, content and much more.

![intelligence search](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/file_search_modifiers_bar_20240423.png)

Clicking on the filters icon expands on helpful modifiers that help creating complex searches.

![intelligece modifiers](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/intelligence_search_20240723.png)

## hunting

Another way of searching for specific characteristics of malware or malware related artifacts is with [YARA rules](https://virustotal.github.io/yara-x/docs/intro/getting-started/). YARA is a tool developed by VirusTotal that helps create descriptions of an artifact based on text and binary patterns. The power of YARA is amplified through community collaboration. Files in the platform are checked against opensource crowdsourced YARA rules repositories, fostering a collective effort to detect and identify emerging threats.

Custom rules can be created within Google Threat Intelligence and used to monitor new submissions of IOCs into the platform for matches, this is called **[Livehunt](livehunt-guide.md)**.

![livehunt yara editor](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/livehunt_20240723.png)

If you are more interested in searching into the historical data than monitoring new occurrences, YARA rules can be used in a **[Retrohunt](retrohunt-guide.md)**, this is a search on the corpus that will help you uncover past infections.

The **[IOC Stream](ioc-stream-guide.md)** centralizes notifications from your active Livehunt rules, subscribed collections, and threat actors. This provides a consolidated list of IOCs and their sources, valuable for continuous signature updates within your security tools via the API. This streamlines threat intelligence monitoring and response, keeping you informed of the latest malware activity you're tracking.

![ioc-stream example](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/ioc_stream_20240723.png)

A useful tool to assist you in creating YARA rules is **[Diff](diff.md)**, by selecting a group of files, DIFF compares them and identify optimal patterns shared by most of them. These patterns are uncommon enough to avoid generating excessive false positives, ensuring more accurate and effective detection rules.

By combining these tools, you can effectively investigate IOCs, identify malware, and understand their behavior for improved threat detection and response.

---

← [Mandiant Techniques and Key Events on the Timeline](../05-global-landscape/mandiant-techniques-and-key-events-on-the-timeline.md) · [up](README.md) · [Check with VirusTotal](check-vt.md) →

*Archived from <https://gtidocs.virustotal.com/docs/get-started-ioc-investigation>.*
