---
title: "authentihash"
source: https://gtidocs.virustotal.com/reference/file-object-authentihash
slug: file-object-authentihash
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:40:57.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › authentihash

---

# authentihash

hash to verify PE files.

`authentihash` is a sha256 hash [used by Microsoft](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/authenticode) to verify that the relevant sections of a PE image file have not been altered. This specific type of hash is used by Microsoft AppLocker.

```json Authentihash attribute
{
  "data": {
		...
    "attributes" : {
      ...
      "authentihash": "<string>",
    }
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "authentihash": "6b9740557544535e594ba5e6585d78e6724be0bed40350211909d3cd97d8be1e",
        }
    }
}
```

---

← [ssdeep](file-object-ssdeep.md) · [up](../README.md) · [trid](file-object-trid.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-authentihash>.*
