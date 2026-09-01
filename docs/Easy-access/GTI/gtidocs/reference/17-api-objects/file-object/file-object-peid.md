---
title: "packers"
source: https://gtidocs.virustotal.com/reference/file-object-peid
slug: file-object-peid
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:20.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › packers

---

# packers

identification of packers used by files.

`packers` identifies packers used on Windows PE files by several tools and AVs. Keys are tool names and values are identified packers, both strings.

```json PEiD packer identifier
{
  "data": {
		...
    "attributes" : {
      ...
      "packers": {
        	"<string>": "<string>", ...
      }
    }
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "packers": {
                "F-PROT": "UPX",
                "PEiD": "UPX v0.89.6 - v1.02 / v1.05 -v1.22 (Delphi) stub"
            }
        }
    }
}
```

---

← [pdf_info](file-object-pdf-info.md) · [up](../README.md) · [rtf_info](file-object-rtf-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-peid>.*
