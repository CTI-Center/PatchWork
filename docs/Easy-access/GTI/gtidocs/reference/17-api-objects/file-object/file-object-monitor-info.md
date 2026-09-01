---
title: "monitor_info"
source: https://gtidocs.virustotal.com/reference/file-object-monitor-info
slug: file-object-monitor-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:42:06.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › monitor_info

---

# monitor_info

Information from VT monitor

> 🚧 Deprecated
>
> This field is deprecated. Use [known\_distributors](file-object-known-distributors.md) instead.
>
> The field will be removed from the API on January 1st 2022.

`monitor_info` contains information extracted from our VT Monitor service. Indicates that this file is present in a VirusTotal Monitor collection.

* `filenames`: <*list of strings*> all different filenames the file has been submitted under.
* `organizations`: <*list of strings*> organization names who uploaded the file.

```json monitor_info
{
  "data": {
    "attributes": {
      "monitor_info": {
        "filenames": [
          "<strings>"
        ],
        "organizations": [
          "<strings>"
        ]
      }
    }
}
```
```json Example
{
  "data": {
    "attributes": {
      "monitor_info": {
        "filenames": [
          "testfilename"
        ],
        "organizations": [
          "Example Inc."
        ]
      },
    }
}
```

---

← [🔀 votes](file-object-votes.md) · [up](../README.md) · [html_info](file-object-html-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-monitor-info>.*
