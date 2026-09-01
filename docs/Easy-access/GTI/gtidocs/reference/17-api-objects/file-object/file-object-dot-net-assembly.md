---
title: "dot_net_assembly"
source: https://gtidocs.virustotal.com/reference/file-object-dot-net-assembly
slug: file-object-dot-net-assembly
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:24.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › dot_net_assembly

---

# dot_net_assembly

information about Microsoft .NET files.

`dot_net_assembly` shows information about [Microsoft .NET files](https://dotnet.microsoft.com/).

* `assembly_data`: <*dictionary*> basic data about the assembly manifest.
  * `buildnumber`: <*integer*> build number.
  * `culture`: <*string*> culture-specific information.
  * `flags`: <*integer*> specific characteristics of the assembly (i.e. x86, AMD64, etc.)
  * `flags_text`: <*string*> human-readable version of flags.
  * `hashalgid`: <*integer*> id of hash used when signed.
  * `majorversion`: <*integer*> major version.
  * `minorversion`: <*integer*> minor version.
  * `name`: <*string*> assembly name.
  * `pubkey`: <*string*> public key.
  * `revisionnumber`: <*integer*> revision number.
* `assembly_flags`: <*integer*> other flags regarding the assembly (i.e. requiring 32 bits, etc.)
* `assembly_flags_txt`: <*string*> human-readable version of `assembly_flags`.
* `assembly_name`: <*string*> assembly name.
* `clr_meta_version`: <*string*> version number of Common Language Runtime metadata.
* `clr_version`: <*string*> Common Language Runtime version.
* `entry_point_rva`: <*integer*> entry point Relative Virtual Address.
* `entry_point_token`: <*integer*> entry point of the program.
* `external_assemblies`: <*dictionary*> (optional) other assemblies used by this one, with name and version. Key is the assembly name and it has a dictionary as value with a `version` key.
* `exported_types`: <*list of dictionaries*> (optional) contains exported types, with name and name spaces:
  * `name`: <*string*> type name.
  * `namespace`: <*string*> type namespace.
* `external_files`: (optional) list of references to external files.
* `external_modules`: <*list of strings*> (optional) list of external modules used.
* `manifest_resource`: <*list of strings*> (optional) list of manifest resources.
* `metadata_header_rva`: <*integer*> metadata header Relative Virtual Address.
* `resources_va`: <*integer*> resources Virtual Address.
* `streams`: <*dictionary*> information about assembly streams, names and associated data. Key is the stream name and value is a dictionary having the following fields:
  * `chi2`: <*float*> chi-squared test value of stream data.
  * `entropy`: <*float*> entropy value of stream data.
  * `md5`: <*string*> md5 hash value of stream data.
  * `size`: <*integer*> size of stream.
* `strongname_va`: <*integer*> Relative Virtual Address of the strong name signature hash.
* `tables_present_map`: hex value of present tables bitmap.
* `tables_present`: <*integer*> number of tables present in the assembly.
* `tables_rows_map`: <*string*> hex representation of number of rows on each table.
* `tables_rows_map_log`: <*string*> simplified representation of tables\_rows\_map.
* `type_definition_list`: (optional) <*list of dictionaries*> every entry represents a type definition:
  * `namespace`: <*string*> defined types' namespace.
  * `type_definitions`: <*list of strings*> defined types.
* `unmanaged_method_list`: <*list of dictionaries*> (optional) list of methods from external modules. Every item in the list contains the following fields:
  * `methods`: <*list of strings*> method names.
  * `name`: <*string*> module name.

```json .NET file
{
  "data": {
    ...
    "attributes" : {
      ...
      "dot_net_assembly": {
        "assembly_data": {
          "buildnumber": <int>,
          "culture": "<string>",
          "flags": <int>,
          "flags_text": "<string>",
          "hashalgid": <int>,
          "majorversion": <int>,
          "minorversion": <int>,
          "name": "<string>",
          "pubkey": "<string>",
          "revisionnumber": <int>
        },
        "assembly_flags": <int>,
        "assembly_flags_txt": "<string>",
        "assembly_name": "<string>",
        "clr_meta_version": "<string>",
        "clr_version": "<string>",
        "entry_point_rva": <int>,
        "entry_point_token": <int>,
        "exported_types": [
         	{
            "name": "<string>",
            "namespace": "<string>"
          }, ...
        ],
        "external_assemblies": {
          "<string>": {
            "version": "<string>"
          }, ...
        },
        "external_files": ["<strings>"],
        "external_modules": ["<strings>"],
        "manifest_resource": ["<strings>"],
        "metadata_header_rva": <int>,
        "resources_va": <int>,
        "streams": {
          "<string>": {
            "chi2": <float>,
            "entropy": <float>,
            "md5": "<string>",
            "size": <int>
          }, ...
        },
        "strongname_va": <int>,
        "tables_present": <int>,
        "tables_present_map": "<string>",
        "tables_rows_map": "<string>",
        "tables_rows_map_log": "<string>",
        "type_definition_list": [
          {
          	"namespace": "<string>",
            "type_definitions": ["<strings>",..]
        	},...
        ],
        "unmanaged_method_list": [
          {
          	"methods": ["<strings>"],
          	"name": "<string>"
          },...
        ],
        "exported_types": {
          "<string>": ["<strings>"]
        },
      },
    ...
    }
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "dot_net_assembly": {
                "assembly_data": {
                    "buildnumber": 0,
                    "culture": "",
                    "flags": 0,
                    "flags_text": "afPA_None",
                    "hashalgid": 32772,
                    "majorversion": 0,
                    "minorversion": 4,
                    "name": "mxzIuI",
                    "pubkey": "",
                    "revisionnumber": 0
                },
                "assembly_flags": 3,
                "assembly_flags_txt": "COMIMAGE_FLAGS_ILONLY, COMIMAGE_FLAGS_32BITREQUIRED",
                "assembly_name": "blabla.exe",
                "clr_meta_version": "1.1",
                "clr_version": "v4.0.30319",
                "entry_point_rva": 143572,
                "entry_point_token": 100663553,
                "external_assemblies": {
                    "System": {
                        "version": "4.0.0.0"
                    },
                    "System.Drawing": {
                        "version": "4.0.0.0"
                    }
                },
                "external_modules": [
                    "user32.dll",
                    "kernel32",
                    "psapi.dll",
                    "user32",
                    "User32.dll",
                    "vaultcli.dll",
                    "Advapi32",
                    "bcrypt.dll"
                ],
                "manifest_resource": [
                    "CustomCastleCrawler.Properties.Resources.resources",
                    "CustomCastleCrawler.frmClassSelection.resources",
                    "CustomCastleCrawler.frmCombat.resources"
                ],
                "metadata_header_rva": 69496,
                "resources_va": 360888,
                "streams": {
                    "#Blob": {
                        "chi2": 27145.0,
                        "entropy": 5.43829870223999,
                        "md5": "c05920af6fec4f1cb210b91a0edfe80d",
                        "size": 2952
                    },
                    "#GUID": {
                        "chi2": 272.0,
                        "entropy": 3.875,
                        "md5": "af229c84a6d3f35be3c227fb35aa7fc0",
                        "size": 16
                    },
                    "#Strings": {
                        "chi2": 112163.703125,
                        "entropy": 5.011016845703125,
                        "md5": "ef647c108850c8c67ffd51c336c301e9",
                        "size": 10860
                    },
                    "#US": {
                        "chi2": 2140962.5,
                        "entropy": 3.9992733001708984,
                        "md5": "7800337a2c33f5745417e7a3b82ff7bd",
                        "size": 47392
                    },
                    "#~": {
                        "chi2": 354640.375,
                        "entropy": 5.539584159851074,
                        "md5": "b95a1f2f2ec66f2d70ae87bd7009190d",
                        "size": 12748
                    }
                },
                "strongname_va": 0,
                "tables_present": 21,
                "tables_present_map": "b0929a29d57L",
                "tables_rows_map": "18422014401130f101022ca002047000d0315e00f020010040000a3010",
                "tables_rows_map_log": "497999949486886445654",
                "type_definition_list": [
                    {
                        "namespace": "System.Security.Cryptography",
                        "type_definitions": [
                            "TripleDESCryptoServiceProvider",
                            "ICryptoTransform",
                            "KeySizes",
                            "SymmetricAlgorithm",
                            "CipherMode",
                            "PaddingMode"
                        ]
                    },
                    {
                        "namespace": "System.Reflection",
                        "type_definitions": [
                            "AssemblyTitleAttribute",
                            "AssemblyDescriptionAttribute",
                            "AssemblyConfigurationAttribute",
                            "AssemblyCompanyAttribute",
                            "AssemblyProductAttribute",
                            "AssemblyCopyrightAttribute",
                            "AssemblyTrademarkAttribute",
                            "AssemblyFileVersionAttribute",
                            "MethodInfo",
                            "Assembly",
                            "BindingFlags",
                            "Binder"
                        ]
                    },
                    {
                        "namespace": "System.Diagnostics",
                        "type_definitions": [
                            "DebuggableAttribute",
                            "DebuggerBrowsableState",
                            "DebuggerBrowsableAttribute",
                            "DebuggerNonUserCodeAttribute"
                        ]
                    }
                ],
                "unmanaged_method_list": [
                    {
                        "methods": [
                            "mciSendString"
                        ],
                        "name": "winmm.dll"
                    }
                ],
                "unmanaged_methods": {
                    "winmm.dll": [
                        "mciSendString"
                    ]
                }
            }
        }
    }
}
```

---

← [isoimage_info](file-object-isoimage-info.md) · [up](../README.md) · [dot_net_guids](file-object-dot-net-guids.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-dot-net-assembly>.*
