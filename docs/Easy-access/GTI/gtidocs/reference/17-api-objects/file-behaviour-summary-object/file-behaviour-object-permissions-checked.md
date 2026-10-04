---
title: "permissions_checked"
source: https://gtidocs.virustotal.com/reference/file-behaviour-object-permissions-checked
slug: file-behaviour-object-permissions-checked
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:43:03.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files Behaviour](../file-behaviour-summary-object.md) › permissions_checked

---

# permissions_checked

Records a query to see whether a given component/package/process/service has a particular permission.

`permissions_checked` contains a list of **Android permissions that the app checks to see if they are granted.**

It is a list of dictionaries, every item in the list contains the following fields:

* `owner`: <*string*> name of the application that has been granted the checked permission.
* `permission`: <*string*> example: android.permission.INTERNET.

```json Checked permissions
{
    "data": {
        "attributes": {
            "permissions_checked": [
                {
                    "owner": "<string>",
                    "permission": "<string>"
                },...
            ]
        }
    }
}
```
```json Example
{
    "data": {
        "attributes": {
            "permissions_checked": [
                {
                    "owner": "blablabla",
                    "permission": "android.permission.INTERNET"
                },
                {
                    "owner": "blablabla",
                    "permission": "android.permission.ACCESS_NETWORK_STATE"
                }
            ]
        }
    }
}
```

---

← [files_copied](file-behaviour-object-files-copied.md) · [up](../README.md) · [http_conversations](file-behaviour-object-http-conversations.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-behaviour-object-permissions-checked>.*
