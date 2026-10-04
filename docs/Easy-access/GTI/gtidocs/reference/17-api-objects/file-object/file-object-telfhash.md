---
title: "telfhash"
source: https://gtidocs.virustotal.com/reference/file-object-telfhash
slug: file-object-telfhash
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:42:11.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › telfhash

---

# telfhash

File's Trend Micro ELF Hash (aka telfhash)

`telfhash` is a hash used by [Trend Micro](https://www.trendmicro.com/en_ca/research/20/j/virustotal-now-supports-trend-micro-elf-hash.html) to cluster and find similar ELF files.

```json Telfhash attribute
{
  "data": {
        ...
    "attributes" : {
      ...
      "telfhash": "<string>",
    }
  }
}
```
```json Example
{
  "data": {
    "attributes": {
      "telfhash": "t1ac5148049e7447b45a342b294a314bc4006f8492b47a94084f64cc440094884f154d4f"
    }
  }
}
```

---

← [🔀  pe_resource_children](file-object-pe-resource-children.md) · [up](../README.md) · [tlsh](file-object-tlsh.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-telfhash>.*
