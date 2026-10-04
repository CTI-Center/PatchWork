---
title: "password_info"
source: https://gtidocs.virustotal.com/reference/file-object-password-info
slug: file-object-password-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:26.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › password_info

---

# password_info

Information from password protected files

`password_info` returns hashcat data from Microsoft Office files. It contains the following attributes:

* `type`: <*string*> type of returned value. It can only be "hashcat".
* `value`: <*string*> hashcat value.

```json password information
{
  "data": {
        ...
    "attributes" : {
      ...
      "password_info": {
        "type": "<string>",
        "value": "<string>"
      }
    }
  }
}
```
```json Example
{
  "data": {
    "attributes": {
      "password_info": {
        "type": "hashcat",
        "value": "$office$*2007*20*128*16*56c7195598b191101f3721dbf1ebe367*131bf49e0b5315f0c2c387d1a62c3360*e820170b1338525454b1ee95ddf9f2c40ae5111d"
      }
    }
  }
}
```

---

← [dot_net_guids](file-object-dot-net-guids.md) · [up](../README.md) · [nsrl_info](file-object-nsrl-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-password-info>.*
