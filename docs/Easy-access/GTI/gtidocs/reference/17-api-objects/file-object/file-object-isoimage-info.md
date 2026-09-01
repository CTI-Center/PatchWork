---
title: "isoimage_info"
source: https://gtidocs.virustotal.com/reference/file-object-isoimage-info
slug: file-object-isoimage-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:23.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › isoimage_info

---

# isoimage_info

information about ISO image files.

`isoimage_info` returns information about the structure of [ISO files](https://en.wikipedia.org/wiki/ISO_image).

* `abstract_file_id`: <*string*> filename of a file in the root directory that contains abstract information for this volume set.
* `application_id`: <*string*> application used to create the file.
* `bibliographic_file_id`: <*string*> filename of a file in the root directory that contains bibliographic information for this volume set.
* `copyright_file_id`: <*string*> filename of a file in the root directory that contains copyright information for this volume set.
* `created`: <*string*> file creation time in `%Y-%m-%d %H:%M:%S` [format](http://strftime.org/).
* `data_preparer_id`: <*string*> the identifier of the person(s) who prepared the data for this volume.
* `effective`: <*string*> volume effective date in `%Y-%m-%d %H:%M:%S` [format](http://strftime.org/).
* `expires`: <*string*> volume expiration date in `%Y-%m-%d %H:%M:%S` [format](http://strftime.org/).
* `file_structure_version`: <*integer*> file structure version.
* `max_date`: <*string*> most recent contained file date in `%Y-%m-%d %H:%M:%S` [format](http://strftime.org/).
* `min_date`: <*string*> oldest contained file date in `%Y-%m-%d %H:%M:%S` [format](http://strftime.org/).
* `modified`: <*string*> last modification date in `%Y-%m-%d %H:%M:%S` [format](http://strftime.org/).
* `num_files`: <*integer*> number of files contained.
* `publisher_id`: <*string*> volume publisher.
* `system_id`: <*string*> name of the system that can act on initial sectors (i.e. "Win32").
* `total_size`: <*integer*> the size of the set in this logical volume.
* `type_code`: <*string*> format type code (i.e. "CD001").
* `volume_id`: <*string*> volume identifier.
* `volume_set_id`: <*string*> volume set identifier.

```json ISO image files
{
  "data": {
		...
    "attributes" : {
      ...
      "isoimage_info": {
        "abstract_file_id": "<string>",
        "application_id": "<string>",
        "bibliographic_file_id": "<string>",
        "copyright_file_id": "<string>",
        "created": "<string:%Y-%m-%d %H:%M:%S>",
        "data_preparer_id": "<string>",
        "effective": "<string:%Y-%m-%d %H:%M:%S>",
        "expires": "<string:%Y-%m-%d %H:%M:%S>",
        "file_structure_version": <int>,
        "max_date": "<string:%Y-%m-%d %H:%M:%S>",
        "min_date": "<string:%Y-%m-%d %H:%M:%S>",
        "modified": "<string:%Y-%m-%d %H:%M:%S>",
        "num_files": <int>,
        "publisher_id": "<string>",
        "system_id": "<string>",
        "total_size": <int>,
        "type_code": "<string>",
        "volume_id": "<string>",
        "volume_set_id": "<string>"
      }
    }
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "isoimage_info": {
                "application_id": "CDIMAGE 2.56 (01/01/2005 TM)",
                "created": "2012-10-04 17:00:00",
                "data_preparer_id": "MICROSOFT CORPORATION, ONE MICROSOFT WAY, REDMOND WA 98052, (425) 882-8080",
                "effective": "0000-00-00 00:00:00",
                "expires": "0000-00-00 00:00:00",
                "file_structure_version": 1,
                "max_date": "2012-10-04 06:34:35",
                "min_date": "2011-12-13 22:04:47",
                "modified": "0000-00-00 00:00:00",
                "num_files": 127,
                "publisher_id": "MICROSOFT CORPORATION",
                "total_size": 5086954,
                "type_code": "CD001",
                "volume_id": "15.0.4420.1017",
                "volume_set_id": "15.0.4420.1017"
            }
        }
    }
}
```

---

← [swf_info](file-object-swf-info.md) · [up](../README.md) · [dot_net_assembly](file-object-dot-net-assembly.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-isoimage-info>.*
