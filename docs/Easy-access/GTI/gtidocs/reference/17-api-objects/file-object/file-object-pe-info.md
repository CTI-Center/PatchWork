---
title: "pe_info"
source: https://gtidocs.virustotal.com/reference/file-object-pe-info
slug: file-object-pe-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:40:59.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › pe_info

---

# pe_info

Microsoft Windows Portable Executable file format info.

`pe_info` returns information about the structure of [Microsoft Windows PE files](https://docs.microsoft.com/en-us/windows/desktop/debug/pe-format) (that is exes, dlls, drivers, etc): sections, entry point, resources, imports, exports, etc.

**To avoid immense reports, we limit the number of entries to 256.**

* `debug`: <*list of dictionaries*> debug information if present. Every item contains the following fields:
  * `codeview`: <*dictionary*> CodeView debug info if present.
    * `age`: <*integer*> always-incrementing value.
    * `guid`: <*string*> unique identifier. Only returned if signature is "RSDS".
    * `name`: <*string*> path of the PDB file.
    * `offset`: <*integer*>  set to 0. Only returned if signature is "NB10".
    * `signature`: <*string*> can be "RSDS" or "NB10".
    * `timestamp`: <*string*> DBG file timestamp. Only returned in signature is "NB10".
  * `fpo`: <*dictionary*> present when the type is `IMAGE_DEBUG_TYPE_FPO`.
    * `functions`: <*integer*> contains the number of FP0 data records.
  * `misc`: <*dictionary*> Present when the type is `IMAGE_DEBUG_TYPE_MISC`.
    * `datatype`: <*integer*> always set to 1 (\`IMAGE\_DEBUG\_MISC\_EXENAME).
    * `length`: <*integer*> total length of the record, rounded to four byte multiple.
    * `unicode`: <*integer*> 1 if data is a unicode string.
    * `data`: <*string*> actual data.
    * `reserved`: <*string*> reserved bytes.
  * `offset`: <*integer*> location of this debug information.
  * `reserved10`: <*dictionary*> present when the type is `IMAGE_DEBUG_TYPE_RESERVED10`.
    * `value`: <*string*> it only contains 4 bytes, which value is stored in hex format.
  * `size`: <*integer*> size of this debug information chunk.
  * `timestamp`: <*string*> date in `%a %b %d %H:%M:%S %Y` [format](http://strftime.org/).
  * `type`: <*integer*> debug type information.
  * `type_str`: <*string*> human-readable version of debug type information.
* `entry_point`: <*integer*> executable entry point.
* `exports`: <*list of strings*> exported functions. It usually appears in DLLs but not in PEs.
* `imphash`: <*string*> hash based on imports.
* `import_list`: <*list of dictionaries*> contains all imported functions. Every item is a dictionary containing the following fields:
  * `imported_functions`: <*list of strings*> imported function names.
  * `library_name`: <*string*> DLL name.
* `machine_type`: <*integer*> platform for this executable.
* `overlay`: <*dictionary*> if the PE file contains info appended to the end, some info about that content.
  * `chi2`: <*float*> chi-squared test value of bytes from overlay content.
  * `entropy`: <*float*> entropy value of bytes from overlay content.
  * `filetype`: <*string*> if we're able to identify a specific file format, it is mentioned here.
  * `md5`: <*string*> hash of the overlay content.
  * `offset`: <*integer*> location of the overlay start.
  * `size`: <*integer*> in number of bytes.
* `resource_details`: <*list of dictionaries*> if the PE contains resources, some info about them.
  * `chi2`: <*float*> chi-squared test of resource content.
  * `entropy`: <*float*> entropy value of resource content.
  * `filetype`: <*string*> noted if we're able to identify a specific file format.
  * `lang`: <*string*> language of the resource.
  * `sha256`: <*string*> hash of the resource content.
  * `type`: <*string*> type or resource.
* `resource_langs`: <*dictionary*> digest of languages found in resources. Key is language (as *string*) and value is how many resources there are having that language (as *integer*).
* `resource_types`: <*dictionary*> digest of resource types. Key is resource type (as *string*) and value is how many resources there are of that specific type (as *integer*).
* `sections`: <*list of dictionaries*> information about PE sections:
  * `entropy`: <*float*> entropy value of section content.
  * `md5`: <*string*> hash of the section.
  * `name`: <*string*> section name.
  * `raw_size`: <*integer*> size of the initialized data on disk, in bytes.
  * `virtual_address`: <*integer*> address of the first byte of the section when loaded into memory, relative to the image base.
  * `virtual_size`: <*string*> total size of the section when loaded into memory, in bytes.
* `timestamp`: <*string*> compilation time in Unix Epoch format.

```json Microsoft Windows Portable Executable files
{
  "data": {
		...
    "attributes" : {
      ...
      "pe_info": {
        "debug": [
          {
            "codeview": {
              "age": <int>,
              "guid": "<string>",
              "name": "<string>",
              "offset": <int>,
              "signature": "<string>",
              "timestamp": "<string>"
            },
            "fpo": {
            	"functions": <int>
            },
            "misc": {
            	"datatype": <int>,
              	"length": <int>,
              	"unicode": <int>,
              	"data": "<string>",
              	"reserved": "<string>"
            },
            "offset": <int>,
            "reserved10": {
            	"value": "<string>"
          	},
            "size": <int>,
            "timedatestamp": "<string:%a %b %d %H:%M:%S %Y>",
            "type": <int>,
            "type_str": "<string>"
          }, ...
        ],
        "entry_point": <int>,
        "exports": ["<string>", ... ],
        "imphash": "<string>",
        "import_list": [
          {
            "imported_functions": [
              "<string>"
            ],
            "library_name": "<string>"
        ],
        "machine_type": <int>,
        "overlay": {
          "chi2": <float>,
          "filetype": "<string>",
          "entropy": <float>,
          "offset": <int>,
          "md5": "<string>",
          "size": <int>
        },
        "resource_details": [
          {
            "chi2": <float>,
            "entropy": <float>,
            "filetype": "<string>",
            "lang": "<string>",
            "sha256": "<string>",
            "type": "<string>"
          }, ...
        ],
        "resource_langs": {
          "<string>": <int>, ...
        },
        "resource_types": {
          "<string>": <int>, ...
        },
        "sections": [
          {
            "entropy": <float>,
            "md5": "<string>",
            "name": "<string>",
            "raw_size": <int>,
            "virtual_address": <int>,
            "virtual_size": <int>
          }, ...
        ],
        "timestamp": <int>
      }
    }
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "pe_info": {
                "debug": [
                    {
                        "codeview": {
                            "age": 1,
                            "guid": "e48addf6-fd27-4a9c-815c-bf60afa7566a",
                            "name": "E:\\987.pdb",
                            "signature": "RSDS"
                        },
                        "offset": 1409712,
                        "size": 35,
                        "timestamp": "Thu May 28 05:53:24 2020",
                        "type": 2,
                        "type_str": "IMAGE_DEBUG_TYPE_CODEVIEW"
                    },
                    {
                        "offset": 1409748,
                        "size": 20,
                        "timestamp": "Thu May 28 05:53:24 2020",
                        "type": 12,
                        "type_str": "12"
                    }
                ],
                "entry_point": 75832,
                "exports": [
                    "ssl",
                    "new_buffer_ssl_connect",
                    "new_ssl",
                    "new_ssl_connect",
                    "ssl_copy_session_id",
                    "ssl_shutdown",
                    "client_method",
                    "method"
                ],
                "imphash": "d91a5c8505be054a5d51c5205c5185f7",
                "import_list": [
                    {
                        "imported_functions": [
                            "RegOpenKeyExA",
                            "RegSetValueExA",
                            "RegQueryValueExA",
                            "RegCloseKey",
                            "RegOpenKeyA"
                        ],
                        "library_name": "advapi32.dll"
                    },
                    {
                        "imported_functions": [
                            "GetLastError",
                            "GetStdHandle",
                            "EnterCriticalSection",
                            "FileTimeToDosDateTime",
                            "lstrlenA",
                            "WaitForSingleObject",
                            "FreeLibrary"
                        ],
                        "library_name": "kernel32.dll"
                    }
                ]
                "machine_type": 332,
                "overlay": {
                    "chi2": 164886880.0,
                    "entropy": 0.0,
                    "filetype": "ASCII text",
                    "md5": "26195dcf5b5ea5905dc5c154b5858527",
                    "offset": 219648,
                    "size": 646613
                },
                "resource_details": [
                    {
                        "chi2": 40609.63671875,
                        "entropy": 3.079699754714966,
                        "filetype": "Data",
                        "lang": "NEUTRAL",
                        "sha256": "87ab855ab53879e5b1a7e59e7958e22512440c50627115ae5758f5f5f5685e79",
                        "type": "RT_ICON"
                    },
                    {
                        "chi2": 22370.37890625,
                        "entropy": 2.9842348098754883,
                        "filetype": "Data",
                        "lang": "NEUTRAL",
                        "sha256": "60457334b5385635e2d6d5edc75619dd5dcd5b7f015d7653ab5a37520a52f5c4",
                        "type": "RT_ICON"
                    },
                    {
                        "chi2": 27408.888671875,
                        "entropy": 2.968428611755371,
                        "filetype": "ASCII text",
                        "lang": "NEUTRAL",
                        "sha256": "a67c8c551025a684511bd5932b5ad7575b352653135326587054532d5e58ab2b",
                        "type": "RT_STRING"
                    }
                ],
                "resource_langs": {
                    "NEUTRAL": 14
                },
                "resource_types": {
                    "RT_GROUP_ICON": 1,
                    "RT_ICON": 2,
                    "RT_RCDATA": 3,
                    "RT_STRING": 7,
                    "RT_VERSION": 1
                },
                "sections": [
                    {
                        "chi2": 1321483.75,
                        "entropy": 6.41,
                        "flags": "rw",
                        "md5": "6538f057456685d65d058f216c5c15f",
                        "name": "CODE",
                        "raw_size": 163840,
                        "virtual_address": 4096,
                        "virtual_size": 163840
                    },
                    {
                        "chi2": 90206.38,
                        "entropy": 3.94,
                        "flags": "rw",
                        "md5": "f67da686417fe266f26129d5d2f260be",
                        "name": "DATA",
                        "raw_size": 1536,
                        "virtual_address": 167936,
                        "virtual_size": 4096
                    },
                    {
                        "chi2": -1.0,
                        "entropy": 0.0,
                        "flags": "rw",
                        "md5": "d4158cd98500b254e9850958ec58457e",
                        "name": "BSS",
                        "raw_size": 0,
                        "virtual_address": 172032,
                        "virtual_size": 4096
                    },
                    {
                        "chi2": 72104.12,
                        "entropy": 4.82,
                        "flags": "rw",
                        "md5": "de82f536e74352ec94564bb5c5b50634",
                        "name": ".idata",
                        "raw_size": 3072,
                        "virtual_address": 176128,
                        "virtual_size": 4096
                    }
                ],
                "timestamp": 708992537
            }
        }
    }
}
```

---

← [trid](file-object-trid.md) · [up](../README.md) · [signature_info](file-object-signature-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-pe-info>.*
