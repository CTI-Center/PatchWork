---
title: "asf_info"
source: https://gtidocs.virustotal.com/reference/file-object-asf-info
slug: file-object-asf-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:02.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › asf_info

---

# asf_info

information about Microsoft Advanced Streaming/Systems Format (ASF) files.

`asf_info` shows information about Microsoft ASF files (.asf, .wma, .wmv).

* `content_encryption_object`: information about how the file has been encrypted.
  * `key_id`: key ID used.
  * `license_url`: url of the license of the file.
  * `protection_type`: type of protection used (i.e. "DRM").
  * `secret_data`: bytes containing secret data.
* `extended_content_encryption_object`: more information about how the file has been encrypted.
  * `CHECKSUM`: data checksum.
  * `KID`: key ID used.
  * `EncodeType`: type of encoding.
  * `LAINFO`: license agreement info.
  * `DRMHeader`: header of the DRM used.
* `script_command_objects`: scripts used in the file.
  * `action`: action to be performed (i.e. a URL).
  * `type`: type of action (i.e. URL, FILENAME, EVENT).
  * `trigger_time`: script activation time.

> 🚧 Deprecated
>
> This field is deprecated, only kept in old files. No recently scanned files will contain this information.

```json Microsoft ASF files
{
  "data": {
		...
    "attributes" : {
      ...
      "asf_info": {
        "content_encryption_object": {"key_id": "<string>",
                                      "license_url": "<string>",
                                      "protection_type": "<string>",
                                      "secret_data": "<string>"},
        "extended_content_encryption_object": {"CHECKSUM": "<string>",
                                               "DRMHeader": "<string>",
                                               "EncodeType": "<string>",
                                               "KID": "<string>",
                                               "LAINFO":"<string>"},
        "script_command_objects": [{"action": "<string>",
                                    "trigger_time": <int>,
                                    "type":"URL"}, ... ]}
    }
  }
}
```

---

← [androguard](file-object-androguard.md) · [up](../README.md) · [rombios_info](file-object-rombios-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-asf-info>.*
