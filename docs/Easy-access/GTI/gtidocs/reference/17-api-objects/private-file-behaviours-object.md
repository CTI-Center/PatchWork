---
title: "Private Files Behaviours"
source: https://gtidocs.virustotal.com/reference/private-file-behaviours-object
slug: private-file-behaviours-object
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:44:25.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Private Files Behaviours

---

# private-files-behaviours

Information about private file behaviours

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

Private file behaviours are identical to [file behaviours](file-behaviour-summary-object.md), but they summarize the behaviour of a [private file](private-files-object.md). They can be only seen by the users who uploaded the original file.

## additional-attributes

* `html_report_link`: <*string*> download URL of the reports's HTML report (if present).
* `pcap_link`: <*string*> download URL of the report's PCAP file (if present).
* `evtx_link`: <*string*> download URL of the report's EVTX file (if present).
* `memdump_link`: <*string*> download URL of the report's memdump file (if present).

## relationships

In addition to the previously described attributes, private file behaviour objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../01-api-introduction/api-responses/introduction-relationships.md) section.

The following table shows a summary of available relationships.

| Relationship       | Return object type                                        |
| :----------------- | :-------------------------------------------------------- |
| attack\_techniques | List of [Attack Techniques](object-attack-techniques.md) |
| file               | A single [Private File](private-files-object.md)         |

---

← [🔀 embedded_ips](private-files-object/embedded_ips.md) · [up](README.md) · [🔀 file](private-file-behaviours-object/private-file-behaviours-file.md) →

*Archived from <https://gtidocs.virustotal.com/reference/private-file-behaviours-object>.*
