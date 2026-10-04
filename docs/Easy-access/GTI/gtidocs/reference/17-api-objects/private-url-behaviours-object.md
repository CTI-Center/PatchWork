---
title: "Private URLs Behaviours"
source: https://gtidocs.virustotal.com/reference/private-url-behaviours-object
slug: private-url-behaviours-object
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:44:29.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Private URLs Behaviours

---

# private-urls-behaviours

Information about private URL behaviours

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

Private URL behaviours are identical to [URL behaviours](https://gtidocs.readme.io/reference/url-behaviour-summary-object), but they summarize the behaviour of a [private URL](private-urls-object.md). They can be only seen by the users who uploaded the original URL.

## additional-attributes

* `expiration`: <*integer*> the date when the report will no longer be available.

## relationships

Additionally, private URL behaviour objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../01-api-introduction/api-responses/introduction-relationships.md) section.

The following table shows a summary of available relationships.

| Relationship       | Return object type                                      |
| :----------------- | :------------------------------------------------------ |
| analyses           | List of [Private Analyses](private-analyses-object.md) |
| http\_transactions | List of [HTTP Transactions](https://gtidocs.readme.io/reference/http-transactions)      |

---

← [Private URLs](private-urls-object.md) · [up](README.md) · [Report](report-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/private-url-behaviours-object>.*
