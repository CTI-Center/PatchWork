---
title: "files_dropped"
source: https://gtidocs.virustotal.com/reference/file-behaviour-object-files-dropped
slug: file-behaviour-object-files-dropped
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:43:01.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files Behaviour](../file-behaviour-summary-object.md) › files_dropped

---

# files_dropped

Interesting files written to disk during execution.

`files_dropped` contains a list of all **files are files specifically created and written to during an execution recording**. These might be the result of downloading content from the Internet and writing it to a file, unpacking a given file from the execution subject's body, dumping some content to a file, etc.

The object contains a *list of dictionaries*, each one containing the following subfields:

* `path ` <*string*> required. Full path, file name included.
* `sha256` <*string*> required.  File's SHA-256 hash.

```json Dropped files
{
    "data": {
        "attributes": {
            "files_dropped": [
                {
                    "path": "<string>",
                    "sha256": "<string>"
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
            "files_dropped": [
                {
                    "path": "C:\\Users\\FD1HVy\\AppData\\Roaming\\33D770D0-06BC-47C5-8714-222CDAC43A71\\run.dat",
                    "sha256": "120a4d5404d43646744c849425741a42f4d0b444541245df4d4c44654c44e3e1"
                },
                {
                    "path": "C:\\Program Files (x86)\\blablabla\\blablabla.exe",
                    "sha256": "c88c5915b968b51bff55155c51d15ef85558c65655c5c31a59bd565b85f57424"
                }
            ]
        }
    }
}
```

---

← [verdicts](file-behaviour-object-verdicts.md) · [up](../README.md) · [files_copied](file-behaviour-object-files-copied.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-behaviour-object-files-dropped>.*
