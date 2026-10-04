---
title: "Key concepts"
source: https://gtidocs.virustotal.com/reference/introduction-key-concepts
slug: introduction-key-concepts
section: reference
group: "API Introduction"
updatedAt: 2025-09-25T00:33:26.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API Introduction](../README.md) › [API responses](../api-responses.md) › Key concepts

---

# key-concepts

The Google Threat Intelligence API revolves around three key concepts: [objects](introduction-objects.md), [collections](introduction-collections.md) and [relationships](introduction-relationships.md).

An object is any item that can be retrieved or manipulated using the API. Files, URLs, domain names and Hunting rulesets are some of the object types exposed by the API.

A collection is a set of objects. Objects in a collection are usually of the same type, but there are a few exceptions to that rule. Some API operations are performed on objects, while some others are performed on collections.

Relationships are links between objects, for example: a file can be related to another file because one of them is a ZIP that contains the other, a URL can be related to a file because the file was downloaded from the URL, a domain name is related to all the URLs on that domain.

---

← [API responses](../api-responses.md) · [up](../README.md) · [Objects](introduction-objects.md) →

*Archived from <https://gtidocs.virustotal.com/reference/introduction-key-concepts>.*
