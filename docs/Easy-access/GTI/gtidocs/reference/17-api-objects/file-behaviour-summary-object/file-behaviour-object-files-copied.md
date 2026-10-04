---
title: "files_copied"
source: https://gtidocs.virustotal.com/reference/file-behaviour-object-files-copied
slug: file-behaviour-object-files-copied
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:43:02.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files Behaviour](../file-behaviour-summary-object.md) › files_copied

---

# files_copied

Object that describes a file copy or move.

`files_copied` contains a list of files that were copied from one location to another. It is a list, every item of the list containing the following fields:

* `destination` <*string*> full path of the destination file.
* `source` <*string*> full path of the source file.

```json Copied files
{
    "data": {
        "attributes": {
            "files_copied": [
                {
                    "destination": "<string>",
                    "source": "<string>"
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
            "files_copied": [
                {
                    "destination": "C:\\Program Files (x86)\\blablabla\\blablabla.exe",
                    "source": "C:\\Users\\FD1HVy\\Downloads\\blablabla.exe"
                }
            ]
        }
    }
}
```

---

← [files_dropped](file-behaviour-object-files-dropped.md) · [up](../README.md) · [permissions_checked](file-behaviour-object-permissions-checked.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-behaviour-object-files-copied>.*
