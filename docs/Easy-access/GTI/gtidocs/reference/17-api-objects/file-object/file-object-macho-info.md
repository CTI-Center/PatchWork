---
title: "macho_info"
source: https://gtidocs.virustotal.com/reference/file-object-macho-info
slug: file-object-macho-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:15.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › macho_info

---

# macho_info

information about Apple MachO files.

`macho_info` returns information about [Apple MachO file format](https://en.wikipedia.org/wiki/Mach-O). Tt is a list, with items for every 'app' contained, each item of the list contains the following attributes:

* `commands`: <*list of dictionaries*> list of load commands. Every entry contains the following fields:
  * `type`: <*string*> command type.
* `info`: <*dictionary*> some basic file attributes about the file.
  * `sha256`: <*string*>.
  * `filename`: <*string*>.
* `headers`: <*dictionary*> some descriptive metadata about the file.
  * `cpu_subtype`: <*string*> processor subtype (i.e. "I386\_ALL").
  * `cpu_type`: <*string*> general type of processor (i.e. "i386").
  * `file_type`: <*string*> file type (i.e. "dynamically bound shared library").
  * `flags`: <*list of strings*> file flags (i.e. "DYLDLINK", "NOUNDEFS").
  * `magic`: <*string*> magic identifier of this app in hex format.
  * `num_cmds`: <*integer*> number of commands.
  * `size_cmds`: <*integer*> commands size.
* `libs`: <*list of strings*> libraries used by the file.
* `segments`: <*list of dictionaries*> list of segments of the file. Every entry contains the following fields:
  * `fileoff`: <*string*> segment phisical address in hex format.
  * `filesize`: <*string*> segment size in hex format.
  * `name`: <*string*> segment name.
  * `sections`: <*list of dictionaries*> sections of the segment. Every entry contains the following fields:
    * `flags`: <*list of strings*> section flags (i.e. "S\_8BYTE\_LITERALS").
    * `name`: <*string*> section name.
    * `type`: <*string*> section type.
  * `vmaddr`: <*string*> virtual address in hex format.
  * `vmsize`: <*string*> virtual address size in hex format.

```json Apple MachO file format
{
  "data": {
		...
    "attributes" : {
      ...
      "macho_info": [
        {
          "libs": ["<strings>"],
          "info": {
            "sha256": "<string>",
            "filename": "<string>"
          },
          "headers": {
            "cpu_subtype": "<string>",
            "magic": "<string>",
            "size_cmds": <int>,
            "file_type": "<string>",
            "num_cmds": <int>,
            "flags": ["<strings>"],
            "cpu_type": "<string>"
          },
          "commands": [
            {
              "type": "<string>"
            }, ...
          ],
          "segments": [
            {
              "name": "<string>",
              "fileoff": "<string>",
              "vmsize": "<string>",
              "filesize": "<string>",
              "vmaddr": "<string>",
              "sections": [
                {
                  "type": "<string>",
                  "flags": ["<strings>"],
                  "name": "<string>"
                }, ...
              ]
            }, ... 
          ]
        ]
      }
    }
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "macho_info": [
                {
                    "commands": [
                        {
                            "type": "LC_UUID"
                        },
                        {
                            "type": "LC_DYLD_INFO_ONLY"
                        },
                        {
                            "type": "LC_SYMTAB"
                        },
                        {
                            "type": "LC_DYSYMTAB"
                        },
                        {
                            "type": "LC_LOAD_DYLIB"
                        }
                    ],
                    "headers": {
                        "cpu_subtype": "I386_ALL",
                        "cpu_type": "i386",
                        "file_type": "dynamically bound bundle file",
                        "flags": [
                            "DYLDLINK",
                            "NOUNDEFS",
                            "TWOLEVEL"
                        ],
                        "magic": "0xfe4d4ace",
                        "num_cmds": 8,
                        "size_cmds": 1008
                    },
                    "libs": [
                        "/usr/lib/libSystem.B.dylib"
                    ],
                    "segments": [
                        {
                            "fileoff": "0x0",
                            "filesize": "0x6000",
                            "name": "__TEXT",
                            "sections": [
                                {
                                    "flags": [
                                        "SECTION_ATTRIBUTES_USR",
                                        "SECTION_ATTRIBUTES_SYS"
                                    ],
                                    "name": "__text",
                                    "type": "S_REGULAR"
                                },
                                {
                                    "flags": [],
                                    "name": "__cstring",
                                    "type": "S_CSTRING_LITERALS"
                                }
                            ],
                            "vmaddr": "0x0",
                            "vmsize": "0x6000"
                        }
                    ]
                }
            ]
        }
    }
}
```

---

← [javascript_info](file-object-javascript-info.md) · [up](../README.md) · [office_info](file-object-office-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-macho-info>.*
