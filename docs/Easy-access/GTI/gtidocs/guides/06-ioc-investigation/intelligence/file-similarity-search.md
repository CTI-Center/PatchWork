---
title: "File similarity search"
source: https://gtidocs.virustotal.com/docs/file-similarity-search
slug: file-similarity-search
section: guides
group: "IOC Investigation"
updatedAt: 2025-09-25T02:38:12.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [IOC Investigation](../README.md) › [Intelligence / Web searching](../intelligence.md) › File similarity search

---

# file-similarity-search

For the time being the main file similarity search is based on a structural feature hash developed in-house at Google Threat Intelligence for the following file types: Portable Executables, PDFs, Office documents, RTFs and Flash SWF files. This hash has not been computed for the whole sample collection, it was introduced in August 2012 starting with portable executables and so only samples sent from then onwards will be searcheable via this feature. Ssdeep similarity search is also available, allowing you to parametrize the similarity threshold, please refer to the [modifiers table](full-list-of-google-threat-intelligence-search-modifiers.md) to learn more about it.

![File Similarity Search Icon](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/intelligence/images/similaritysearch_icon_20240502.png)

You can click on the waves icon on a given search result sample row in order to search samples similar to the one under consideration.

Please note that this feature is only available if the file has the structural feature hash available. We plan to continue developing a similar hash for other file types.

---

← [Collection search modifiers](collection-search-modifiers.md) · [up](../README.md) · [Content search (Grep)](content-search-grep.md) →

*Archived from <https://gtidocs.virustotal.com/docs/file-similarity-search>.*
