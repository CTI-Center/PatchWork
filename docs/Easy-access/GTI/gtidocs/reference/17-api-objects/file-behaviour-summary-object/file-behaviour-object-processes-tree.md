---
title: "processes_tree"
source: https://gtidocs.virustotal.com/reference/file-behaviour-object-processes-tree
slug: file-behaviour-object-processes-tree
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:43:07.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files Behaviour](../file-behaviour-summary-object.md) › processes_tree

---

# processes_tree

Created processes during the execution of a given file.

`processes_tree` contains al list of **created processes structured in a recursive way allowing to build a process tree.**.

It is a list, every item of the list containing the following attributes:

* `children`: <*list of dictionaries*> contains processes created by a given process. Every subfield contains the same fields (`children`, `name`, `process_id` and `time_offset`) allowing to build a recursive process tree.
* `name`: <*string*> process name.
* `process_id`: <*string*> ID of the process.
* `time_offset`: <*integer*> first observed. Seconds since execution start.

```json Process tree
{
    "data": {
        "attributes": {
            "processes_tree": [
                {
                    "children": [
                        {
                            "children": [...],
                            "name": "<string>",
                            "process_id": "<string>",
                            "time_offset": <int>
                        },...
                    ],
                    "name": "<string>",
                    "process_id": "<string>",
                    "time_offset": <int>
                }
            ]
        }
    }
}
```
```json Example
{
    "data": {
        "attributes": {
            "processes_tree": [
                {
                    "children": [
                        {
                            "name": "com.blabla.blabla",
                            "process_id": "15530"
                        },
                        {
                            "name": "com.blabla.blabla",
                            "process_id": "15623"
                        }
                    ],
                    "name": "blabla",
                    "process_id": "8145"
                }
            ]
        }
    }
}
```

---

← [ip_traffic](file-behaviour-object-ip-traffic.md) · [up](../README.md) · [sms_sent](file-behaviour-object-sms-sent.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-behaviour-object-processes-tree>.*
