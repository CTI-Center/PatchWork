---
title: "Private Analyses"
source: https://gtidocs.virustotal.com/reference/private-analyses-object
slug: private-analyses-object
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:44:16.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Private Analyses

---

# private-analyses

Private file's analyses

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

A *Private Analysis* object represents an analysis of a private file submitted to Google Threat Intelligence. This analysis can only be seen by the user that submitted it.

## object-attributes

A Private Analysis object contains the following attributes:

* `date`: <*integer*> analysis date (UTC timestamp).
* `status`: <*string*> analysis status. Possible values are:
  * "queued" (the analysis is waiting to be analysed).
  * "in-progress" (the analysis is currently in progress).
  * "completed" (the analysis is finished).
* `pending_stages`: <*dictionary*> stages of the analysis currently running. The values of the dictionary contains an explanation of the stage name, for example:

```json
{
  "Zenbox": "Sandbox analysis from Zenbox (queued)",
  "tools": "File's tools"
}
```

* `sandbox_configuration`: <*dictionary*> sandbox parameters specified for the analysis (enable\_internet and command\_line).
* `sandbox_status`: <*dictionary*> similar to `pending_stages` but includes a detailed status of the sandboxes executions triggered by the analysis. These statuses can give more info as well about failed sandbox executions due to a missing dependency or if the file is an incompatible file type. An example of `sandbox_status` is:

```json
{
  "Zenbox": {
    "in_progress_percent": 2,
    "status": "enqueueing"
  },
  "VirusTotal Jujubox": {
    "status": "unsupported file type",
    "message": "incompatible file",
    "in_progress_percent": 100
  },
  "VirusTotal R2DBox": {
    "status": "finished",
    "in_progress_percent": 100
  }
}
```

## meta

Additionally, once the analysis is processed you can get additional information about the enqueued file along with the analysis:

* `file_info`: <*dictionary*> it contains the following keys:
  * `size`: <*integer*> size of the file in bytes.
  * `sha256`: <*string*> file's SHA-256 hash.
  * `sha1`: <*string*> file's SHA-1 hash.
  * `md5`: <*string*> file's MD-5 hash.

```json Private analysis object
{
  "meta": {
    "file_info": {
      "size": <int>,
      "sha256": <string>,
      "sha1": <string>,
      "md5": <string>
    }
  },
  "data": {
    "attributes": {
      "date": <int:timestamp>,
      "status": <string>,
      "pending_stages": <dict>,
      "sandbox_configuration": <dict>,
      "sandbox_status": <dict>
    },
    "type": "private_analysis",
    "id": <string>,
    "links": {
      "self": "https://virustotal.com/api/v3/private/analyses/<id>"
    }
  }
}
```
```json Example
{
  "meta": {
    "file_info": {
      "size": 16919681,
      "sha256": "164119838acc214005e0cc37481a6f900ea535afe8d1074b7927d7b23bac4770",
      "sha1": "f6b8703a7776663950199aefbf6a03aed26e61ba",
      "md5": "63192984ec708025aeb51b69ec4c91e4"
    }
  },
  "data": {
    "attributes": {
      "date": 1659364670,
      "sandbox_configuration": {
        "enable_internet": true,
        "command_line": "calc.exe"
      },
      "sandbox_status": {
        "Zenbox": {
          "status": "queued",
          "in_progress_percent": 8
        }
      },
      "status": "in-progress",
      "pending_stages": {
        "Zenbox": "Sandbox analysis from Zenbox (queued)",
        "tools": "File's tools"
      }
    },
    "type": "private_analysis",
    "id": "NTJjNTM1MThmMzhiNWRiNGE1ZWQ5ZDhiZjQyNWY2NzM6NjMxOTI5ODRlYzcwODAyNWFlYjUxYjY5ZWM0YzkxZTQ6MTY1OTM2NDY3MA==",
    "links": {
      "item": "https://www.virustotal.com/api/v3/private/files/164119838acc214005e0cc37481a6f900ea535afe8d1074b7927d7b23bac4770",
      "self": "https://www.virustotal.com/api/v3/private/analyses/NTJjNTM1MThmMzhiNWRiNGE1ZWQ5ZDhiZjQyNWY2NzM6NjMxOTI5ODRlYzcwODAyNWFlYjUxYjY5ZWM0YzkxZTQ6MTY1OTM2NDY3MA=="
    }
  }
}
```

## relationships

In addition to the previously described attributes, private analyses objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../01-api-introduction/api-responses/introduction-relationships.md)  section.

The following table shows a summary of available relationships.

| Relationship | Return object type                                |
| :----------- | :------------------------------------------------ |
| item         | A single [private file](private-files-object.md) |
| submitter    | A single [user](user-object.md)                  |

---

← [Operations](operation-object.md) · [up](README.md) · [🔀 item](private-analyses-object/private-analyses-object-item.md) →

*Archived from <https://gtidocs.virustotal.com/reference/private-analyses-object>.*
