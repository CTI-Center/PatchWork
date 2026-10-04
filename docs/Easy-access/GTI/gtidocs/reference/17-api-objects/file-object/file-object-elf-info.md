---
title: "elf_info"
source: https://gtidocs.virustotal.com/reference/file-object-elf-info
slug: file-object-elf-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:10.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › elf_info

---

# elf_info

information about Unix ELF files.

`elf_info` returns information about [Unix ELF file format](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format).

* `export_list`: <*list of dictionaries*> contains exported elements. Each dictionary contains:
  * `name`: <*string*> The exported item's name.
  * `type`: <*string*> The exported item's type.
* `header`: <*dictionary*> some descriptive metadata about the file.
  * `type`: <*string*> human readable type of file (i.e. "EXEC (Executable file)").
  * `hdr_version`: <*string*> header version.
  * `num_prog_headers`: <*integer*> number of entries in the program header.
  * `os_abi`: <*string*> human readable application binary interface type (i.e. "UNIX - Linux").
  * `obj_version`: <*string*> "0x1" for original ELF files.
  * `machine`: <*string*> platform (ie. "Advanced Micro Devices X86-64").
  * `entrypoint`: <*integer*> executable entry point.
  * `num_section_headers`: <*string*> number of section headers.
  * `abi_version`: <*integer*> application binary interface version.
  * `data`: <*string*> data alignment in memory (i.e. "little endian".)
  * `class`: <*string*> file class (i.e. "ELF32").
* `import_list`: <*list of dictionaries*> contains imported elements. Each dictionary contains:
  * `name`: <*string*> The imported item's name.
  * `type`: <*string*> The imported item's type.
* `packers`: <*list of strings*> contains the executable's packers, if any.
* `section_list`: <*list of dictionaries*> sections of the ELF file. Every item contains the following fields:
  * `name`: <*string*> section name.
  * `virtual_address`: <*integer*> section virtual address.
  * `flags`: <*string*> section flags.
  * `physical_offset`: <*integer*> section physical offset.
  * `section_type`: <*string*> type of section.
  * `size`: <*integer*> size of section in bytes.
* `segment_list`: <*list of dictionaries*> aka Program Headers. each dictionary contains:
  * `segment_type` <*string*> The segment type.
  * `resources` <*list of strings*> A list of resources involved in that segment.
* `shared_libraries`: <*list of strings*> contains shared libraries used by this executable.

```json ELF File format
{
  "data": {
		...
    "attributes" : {
      ...
      "elf_info": {
        "export_list": [{
          "name": "<string>",
          "type": "<string>"
        }, ...],
        "header": {
          "type": "<string>",
          "hdr_version": "<string>",
          "num_prog_headers": <int>,
          "os_abi": "<string>",
          "obj_version": "<string>",
          "machine": "<string>",
          "entrypoint": <int>,
          "num_section_headers" <int>,
          "abi_version": 0,
          "data": "<string>",
          "class": "<string>"
        },
        "import_list": [{
          "name": "<string>",
          "type": "<string>"
        }, ...],
        "packers": ["<string>",...],
        "section_list": [
          {
            "name": "<string>",
            "virtual_address": <int>,
            "flags": "<string>",
            "physical_offset": <int>,
            "section_type": "<string>",
            "size": <int>
          }, ... 
        ],
        "segment_list": [
          {
          	"segment_type": <string>,
            "resources": ["<strings>"]
          }, ...
        ],
        "shared_libraries": ["<strings>"]
      }
    }
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "elf_info": {
                "export_list": [
                    {
                        "name": "__aeabi_unwind_cpp_pr0",
                        "type": "FUNC"
                    },
                    {
                        "name": "JNI_OnLoad",
                        "type": "FUNC"
                    },
                    {
                        "name": "__aeabi_unwind_cpp_pr1",
                        "type": "FUNC"
                    },
                    {
                        "name": "__aeabi_idivmod",
                        "type": "FUNC"
                    }
                ],
                "header": {
                    "abi_version": 0,
                    "class": "ELF64",
                    "data": "2's complement, little endian",
                    "entrypoint": 6374704,
                    "hdr_version": "1 (current)",
                    "machine": "Advanced Micro Devices X86-64",
                    "num_prog_headers": 2,
                    "num_section_headers": 0,
                    "obj_version": "0x1",
                    "os_abi": "UNIX - Linux",
                    "type": "EXEC (Executable file)"
                },
                "import_list": [
                    {
                        "name": "__cxa_finalize",
                        "type": "FUNC"
                    },
                    {
                        "name": "__cxa_atexit",
                        "type": "FUNC"
                    },
                    {
                        "name": "strlen",
                        "type": "FUNC"
                    },
                    {
                        "name": "_Znaj",
                        "type": "FUNC"
                    },
                    {
                        "name": "__stack_chk_fail",
                        "type": "FUNC"
                    }
                ],
                "packers": [
                    "upx"
                ],
                "section_list": [
                    {
                        "virtual_address": 0,
                        "flags": "",
                        "name": "",
                        "physical_offset": 0,
                        "size": 0,
                        "section_type": "NULL"
                    },
                    {
                        "virtual_address": 308,
                        "flags": "A",
                        "name": ".note.gnu.build-id",
                        "physical_offset": 308,
                        "size": 36,
                        "section_type": "NOTE"
                    },
                    {
                        "virtual_address": 344,
                        "flags": "A",
                        "name": ".dynsym",
                        "physical_offset": 344,
                        "size": 1232,
                        "section_type": "DYNSYM"
                    }
                ],
                "segment_list": [
                    {
                        "segment_type": "PHDR",
                        "resources": []
                    },
                    {
                        "segment_type": "LOAD",
                        "resources": [
                            ".note.gnu.build-id",
                            ".dynsym",
                            ".dynstr",
                            ".hash",
                            ".gnu.version",
                            ".gnu.version_d",
                            ".gnu.version_r",
                            ".rel.dyn",
                            ".rel.plt",
                            ".plt",
                            ".text",
                            ".ARM.extab",
                            ".ARM.exidx",
                            ".rodata"
                        ]
                    },
                    {
                        "segment_type": "LOAD",
                        "resources": [
                            ".fini_array",
                            ".data.rel.ro",
                            ".init_array",
                            ".dynamic",
                            ".got",
                            ".data",
                            ".bss"
                        ]
                    }
                ],
                "shared_libraries": [
                    "liblog.so",
                    "libstdc++.so",
                    "libc.so",
                    "libm.so",
                    "libdl.so"
                ]
            }
        }
    }
}
```

---

← [dmg_info](file-object-dmg-info.md) · [up](../README.md) · [image_code_injections](file-object-image-code-injections.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-elf-info>.*
