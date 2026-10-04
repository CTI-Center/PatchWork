---
title: "When is an analysis included in the feeds?"
source: https://gtidocs.virustotal.com/docs/when-analysis-feeds
slug: when-analysis-feeds
section: guides
group: "FAQ"
updatedAt: 2025-09-25T00:33:14.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [FAQ](README.md) › When is an analysis included in the feeds?

---

# when-is-an-analysis-included-in-the-feeds?

The Google Threat Intelligence feeds include entries for it resources (files, URLs, domains or sandboxes, depending on the specific feed) based on the following events:

1. Initial Submission: A resource generates an entry in the feed when it is first submitted to Google Threat Intelligence for analysis. This initial entry contains the analysis results and the fundamental properties of the resource.

2. Re-analysis: A resource generates a new entry in the feed each time it is subsequently re-analyzed by Google Threat Intelligence.

When a resource entry appears due to re-analysis, it contains the updated information gathered from this latest analysis. Importantly, this entry also includes the original, unchanging basic properties of the resource, consistent with the first time it was seen.

Notice however that submitter is not present in all entries, it will be absent when resources are submitted via the web interface without triggering a new analysis due to recent submissions, or when resources are re-analyzed by Google Threat Intelligence without being submitted by some external user.

---

← [Understanding Partial Files](partial-files.md) · [up](README.md) · [My Landscape](my-landscape-faq.md) →

*Archived from <https://gtidocs.virustotal.com/docs/when-analysis-feeds>.*
