---
title: "ssdeep"
source: https://gtidocs.virustotal.com/reference/file-object-ssdeep
slug: file-object-ssdeep
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:40:56.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › ssdeep

---

# ssdeep

CTPH hash of the file content.

`ssdeep` is a program for computing [Context Triggered Piecewise Hashes](https://ssdeep-project.github.io/ssdeep/index.html). Also called fuzzy hashes, it allows identifying similar files by comparing (via Edit Distance) their hashes.

```json ssdeep
{
  "data": {
		...
    "attributes" : {
      ...
      "ssdeep": "<string>"
    }
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "ssdeep": "98504:G5j6i51u5gM0P5kv5GzH5AY5NfrL5sZte5vw5CA:e5AA5i5vw"
        }
    }
}
```

---

← [exiftool](file-object-exiftool.md) · [up](../README.md) · [authentihash](file-object-authentihash.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-ssdeep>.*
