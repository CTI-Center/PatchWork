---
title: "lnk_info"
source: https://gtidocs.virustotal.com/reference/file-object-lnk-info
slug: file-object-lnk-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:42:16.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › lnk_info

---

# lnk_info

information about Microsoft Windows LNK files

`lnk_info` shows information about [LNK files](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-shllink/16cb4ca1-9339-4d0c-a68d-bf1d6cc0f943).

* `creation_date`: <*string*> date in ISO8601 format.
* `access_date`: <*string*> date in ISO8601 format.
* `modification_date`: <*string*> date in ISO8601 format.
* `link_flags`: <*list of strings*> basic properties of the LNK file.
* `target_path`: <*string*> (optional) target path from Link Target Identifier fields.
* `icon_location`: <*string*> (optional) path to the icon location.
* `mac_address`: <*string*> (optional) network MAC address.
* `mac_vendor_name`: <*string*> (optional) network vendor name from MAC address.
* `machine_id`: <*string*> (optional) computer name.
* `working_directory`: <*string*> (optional) target working directory.
* `relative_path`: <*string*> (optional) target file relative path.
* `command_line_arguments`: <*string*> (optional).
* `volume_serial_number`: <*string*> (optional) disk volume serial number.
* `volume_label`: <*string*> (optional) disk volume label.
* `local_path`: <*string*> (optional).
* `common_path`: <*string*> (optional).
* `network_share_name`: <*string*> (optional).
* `extra_data`:
  * `dlt_properties`: <*dictionary*> dlt properties of the LNK file.
    * `birth_droid_file_id`: <*string*>,
    * `droid_file_id`: <*string*>,
    * `birth_droid_volume_id`: <*string*>,
    * `droid_volume_id`: <*string*>
* `link_target_id_list`: <*list of dictionaries*> Every entry contains the following fields:
  * `clsid`: <*string*>,
  * `item_type`: <*integer*>,
  * `item_type_str`: <*string*>
* `header`: <*dictionary*>.
  * `show_window`: <*integer*>,
  * `show_window_str`: <*string*>,
  * `hot_key`: <*string*>,
  * `file_size`: <*integer*>

```json LNK files
{
  "data": {
        ...
    "attributes" : {
      ...
      "lnkcheck": {
        "creation_date": "<string:ISO8601>", 
        "access_date": "<string:ISO8601>", 
        "modification_date": "<string:ISO8601>", 
        "link_flags": ["<string>",...],
        "target_path": "<string>",
        "icon_location": "<string>",
        "mac_address": "<string>",
        "mac_vendor_name": "<string>",
        "machine_id": "<string>",
        "working_directory": "<string>",
        "relative_path": "<string>",
        "command_line_arguments": "<string>",
        "volume_serial_number": "<string>",
        "volume_label": "<string>", 
        "local_path": "<string>",
        "common_path": "<string>",
        "network_share_name": "<string>"
        "extra_data": {
          "dlt_properties": {
            "birth_droid_file_id": "<string>", 
            "droid_file_id": "<string>", 
            "birth_droid_volume_id": "<string>", 
            "droid_volume_id": "<string>"
          }
        }
        "shell_item": {
          "clsid": "<string>",
          "item_type": "<integer>",
          "item_type_str":"<string>"
        }
        "header": {
          "show_window": "<integer>", 
          "show_window_str": "<string>", 
          "hot_key": "<string>", 
          "file_size": "<integer>"
        },
    }
  }
}
```
```json Example
{
  "data": {
    "attributes": {
      "lnkcheck": {
        "common_path": "C:\\Program Files\\Greenrain\\Submission\\unins000.exe", 
        "machine_id": "445817", 
        "modification_date": "2016-07-27T18:25:43.570251Z", 
        "link_flags": [
          "HasLinkInfo", 
          "HasRelativePath", 
          "IsUnicode", 
          "HasWorkingDir", 
          "HasExprString", 
          "EnableTargetMetadata"
        ], 
        "vhash": "1234567890", 
        "network_share_name": "\\\\USER\\HTMLQA", 
        "creation_date": "2016-06-28T21:49:46.108805Z", 
        "header": {
          "show_window": 1, 
          "show_window_str": "SW_NORMAL", 
          "hot_key": "(0+0)", 
          "file_size": 6486
        }, 
        "relative_path": "..\\..\\..\\..\\..\\..\\Program Files\\Greenrain\\Submission\\unins000.exe", 
        "local_path": "C:\\Program Files\\Greenrain\\Submission\\unins000.exe", 
        "working_directory": "C:\\Program Files\\Greenrain\\Submission", 
        "mac_address": "00:50:56:a0:09:e3", 
        "access_date": "2016-06-28T21:49:46.108805Z", 
        "extra_data": {
          "dlt_properties": {
            "birth_droid_file_id": "33a6be73-453c-11e6-9444-00155d0b8406", 
            "droid_file_id": "33a6be73-453c-11e6-9444-00155d0b8406", 
            "birth_droid_volume_id": "85cdf8e2-5f07-4f3a-a953-67709a1e8150", 
            "droid_volume_id": "85cdf8e2-5f07-4f3a-a953-67709a1e8150"
          }
        }, 
        "mac_vendor_name": "VMware, Inc."
      } 
    }
  }
}
```

---

← [known_distributors](file-object-known-distributors.md) · [up](../README.md) · [🔀🧑‍💻 user_votes](file-object-user-votes.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-lnk-info>.*
