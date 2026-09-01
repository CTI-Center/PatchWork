---
title: "javascript_info"
source: https://gtidocs.virustotal.com/reference/file-object-javascript-info
slug: file-object-javascript-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:14.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › javascript_info

---

# javascript_info

Information extracted out of Javascript files

`javascript_info` returns information about [Javascript files](https://en.wikipedia.org/wiki/JavaScript). It contains the following fields:

* `tags`: <*list of strings*> interesting elements in the code. Can be any of:
  * `aes-encoded`
  * `Aes.Ctr.decrypt`
  * `charAt`
  * `charCodeAt`
  * `document.getElementById`
  * `document.write`
  * `eval`
  * `eval+unescape`
  * `fromCharCode`
  * `location`
  * `malformed`
  * `Math`
  * `obfuscated`
  * `ParseInt`
  * `replace`
  * `substr`
  * `unescape`
  * `write`
  * `write+unescape`

```json Javascript information
{
  "data": {
    "attributes": {
      "javascript_info": {
        "tags": ["<string>", ...]
      }
    }
  }
}
```
```json Example
{
  "data": {
    "attributes": {
      "javascript_info": {
        "tags": [
          "document.getElementById",
          "unescape",
          "charAt",
          "charCodeAt",
          "replace",
          "write",
          "substr",
          "location",
          "eval",
          "Math",
          "fromCharCode"
        ]
      }
    }
  }
}
```

---

← [jar_info](file-object-jar-info.md) · [up](../README.md) · [macho_info](file-object-macho-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-javascript-info>.*
