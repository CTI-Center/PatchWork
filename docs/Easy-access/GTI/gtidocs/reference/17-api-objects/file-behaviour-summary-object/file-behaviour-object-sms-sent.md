---
title: "sms_sent"
source: https://gtidocs.virustotal.com/reference/file-behaviour-object-sms-sent
slug: file-behaviour-object-sms-sent
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:43:08.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files Behaviour](../file-behaviour-summary-object.md) › sms_sent

---

# sms_sent

Sent SMSs during the execution of the file under study.

`sms_sent` contains a list of **sent SMSs during the execution of a given file.**

It is a list, every item on the list containing the following fields:

* `body`<*string*> message text itself.
* `destination` <*string*> telephone number to which the SMS is sent.

```json Sent SMSs
{
    "data": {
        "attributes": {
            "sms_sent": [
                {
                    "body": "<string>",
                    "destination": "<string>"
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
            "sms_sent": [
                {
                    "body": "40659+3079+123636+x+a",
                    "destination": "3865"
                },
                {
                    "body": "40659+3079+123636+x+a",
                    "destination": "2865"
                },
                {
                    "body": "40659+3079+123636+x+a",
                    "destination": "4865"
                },
            ]
        }
    }
}
```

---

← [processes_tree](file-behaviour-object-processes-tree.md) · [up](../README.md) · [🔀 file](file-behaviour-object-file.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-behaviour-object-sms-sent>.*
