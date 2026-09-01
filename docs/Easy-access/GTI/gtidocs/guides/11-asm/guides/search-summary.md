---
title: "Search Summary"
source: https://gtidocs.virustotal.com/docs/search-summary
slug: search-summary
section: guides
group: "ASM"
updatedAt: 2025-09-25T01:59:30.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [ASM](../README.md) › [Guides](../guides.md) › Search Summary

---

# search-summary

The Search Summary feature in Attack Surface Management (ASM) provides a high-level summary of the current search, helping you to understand the scope of the search. This is significant, especially if you are searching within a large number of Collections. 

> ℹ️
>
> The **Search Summary** pane only exists when viewing **Entities**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_search_summary_summary_20241003.png)

The count listed beside each category represents the number of associated results. Most categories are ranked in descending order of result count. However, **Issue Count By Severity** is ranked by severity, irrespective of the count. You can expand the list for any category by clicking the **Show More** option.

Summary categories include:

* **Entity Type**
* **Issue Count by Severity**
* Geographical **Location** (empty if no data exists)
* **Network** (empty if no data exists)
* **Technologies** (empty if no data exists)

## filter-the-search-summary

You can filter Entities by selecting attributes in any categories listed in the **Search Summary** pane. As an example, follow these steps:

 In the **Search Summary** pane:

* Click **IpAddress** from the **Entity Type** category.
* Click **United States** from the **Location** category.

These two filters are automatically applied. Both filters appear in the search bar and are reflected in the **Filters** count within the **Search Summary** pane.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_search_summary_search_20241003.png)

You can clear the selected filters by clicking **Clear All** in the **Search Summary** pane, or **Clear** in the search bar.

---

← [Manage Project Membership](manage-project-membership.md) · [up](../README.md) · [Bulk Select](bulk-select.md) →

*Archived from <https://gtidocs.virustotal.com/docs/search-summary>.*
