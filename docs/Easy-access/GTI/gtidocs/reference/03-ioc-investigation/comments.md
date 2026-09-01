---
title: "Comments"
source: https://gtidocs.virustotal.com/reference/comments
slug: comments
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T02:04:29.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [IoC Investigation](README.md) › Comments

---

# comments

Google Threat Intelligence users can post comments to give additional context about a file, domain, IP address, graph or URL. These comments can be retrieved using our API.

## comment-identifiers

Comment IDs have three main parts divided by a `-` character:

* A character representing the item where the comment is posted. This can be one of:
  * `d` if the comment is posted in a domain.
  * `f` if the comment is posted in a file.
  * `g` is the comment is posted in a graph.
  * `i` if the comment is posted in a IP address.
  * `u` if the comment is posted in a URL.
* The item's ID.
* A random string.

All comment identifiers returned by the API can be used in subsequent API calls that require a comment identifier.

---

← [Get the URL for a URL's latest analysis DOM](urls/urls-dom-url.md) · [up](README.md) · [Get latest comments](comments/get-comments.md) →

*Archived from <https://gtidocs.virustotal.com/reference/comments>.*
