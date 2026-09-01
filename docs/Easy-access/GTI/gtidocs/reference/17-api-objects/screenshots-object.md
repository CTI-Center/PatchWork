---
title: "Screenshots"
source: https://gtidocs.virustotal.com/reference/screenshots-object
slug: screenshots-object
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T02:14:39.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Screenshots

---

# screenshots

screenshot objects

Screenshots are screen capture images obtained during the file execution in a behavior analysis sandbox machine. This object contains attributes identifying where and when the screenshot was generated:

* `sandbox_name` name of the sandbox setup where the file was executed
* `date` Epoch when the capture was made (as unix timestamp)
* `link` URL pointing to the actual image
* `analysed_file_sha256` relationship pointing to the file object that was executed

```json Screenshot object
{
  "data": {
    "type": "screenshot",
    "id": "<SCREENSHOT_NAME>",
    "attributes" : {
      "sandbox_name": "<string>",
      "date": "<unix_timestamp>",
      "link": "<string>",
      "analysed_file_sha256": <object>
    }
  } 
}
```

---

← [Saved Searches](saved-search-object.md) · [up](README.md) · [Service Accounts](service-accounts-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/screenshots-object>.*
