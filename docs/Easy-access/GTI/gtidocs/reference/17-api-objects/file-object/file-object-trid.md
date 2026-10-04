---
title: "trid"
source: https://gtidocs.virustotal.com/reference/file-object-trid
slug: file-object-trid
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:40:58.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › trid

---

# trid

file type identification tool.

`trid`: [TrID](http://mark0.net/soft-trid-e.html) is a utility designed to identify file types from their binary signatures. It may give several detections, ordered by higher to lower probability of file format identification (given as percentage).

```json TRiD
{
  "data": {
		...
    "attributes" : {
      ...
      "trid": [
        {"file_type": "<string>", "probability": <float>}, ... 
      ]
    }
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "trid": [
                {
                    "file_type": "iOS Application",
                    "probability": 39.6
                },
                {
                    "file_type": "Sweet Home 3D design (generic)",
                    "probability": 20.7
                },
                {
                    "file_type": "Mozilla Firefox browser extension",
                    "probability": 15.8
                },
                {
                    "file_type": "Mozilla Archive Format (gen)",
                    "probability": 13.8
                },
                {
                    "file_type": "ZIP compressed archive",
                    "probability": 7.9
                }
            ]
        }
    }
}
```

---

← [authentihash](file-object-authentihash.md) · [up](../README.md) · [pe_info](file-object-pe-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-trid>.*
