---
title: "magic"
source: https://gtidocs.virustotal.com/reference/file-object-magic
slug: file-object-magic
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:08.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › magic

---

# magic

identification of files via magic number.

`magic` gives a guess of the file type, based on a popular parsing tool from unix.

```json File type guess based on "magic" tool
{
  "data": {
		...
    "attributes" : {
      ...
      "magic": "<string>",
    }
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "magic": "Mach-O fat file with 2 architectures"
        }
    }
}
```

---

← [deb_info](file-object-deb-info.md) · [up](../README.md) · [dmg_info](file-object-dmg-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-magic>.*
