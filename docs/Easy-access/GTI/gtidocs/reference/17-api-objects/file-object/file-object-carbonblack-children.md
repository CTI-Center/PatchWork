---
title: "🔀 carbonblack_children"
source: https://gtidocs.virustotal.com/reference/file-object-carbonblack-children
slug: file-object-carbonblack-children
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:31.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › 🔀 carbonblack_children

---

# 🔀-carbonblack_children

Files derived from the file according to Carbon Black.

The *carbonblack\_children* relationship returns the list of ***all files derived from a given file according to Carbon Black***. This relationship is only available for Premium API users.

[CarbonBlack](http://www.carbonblack.com/) acts like a surveillance camera for end-user PCs, recording downloaded files, spawned processes, files written to disk, etc. CarbonBlack shares its in-the-wild data with VirusTotal, this relationship stores the information of files written to disk by the sample under consideration.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/files/files-relationships.md). The response contains a list of [File](../../03-ioc-investigation/files.md) objects.

```json /files/{file_hash}/carbonblack_children
{
  "data": [
    <FILE_OBJECT>,
    <FILE_OBJECT>,
    ...
  ],
  "links": {
    "next": "<string>",
    "self": "<string>"
  },
  "meta": {
    "count": <int>,
    "cursor": "<string>"
  }
}
```
```json Example
{
    "data": [
        {
            "attributes": {
                "authentihash": "0c4226e47eda883ce9eff9ec1ae6ce1a13ee3cc63e6960ae5a3ae4ad2e8eeee5",
                "creation_date": 1587044124,
                "downloadable": true,
                "exiftool": {
                    "AssemblyVersion": "1.3.30.0",
                    "CharacterSet": "Unicode",
                    "CodeSize": "104448",
                    "Comments": "blablablabla",
                    "CompanyName": "blablabla",
                    "EntryPoint": "0xccef",
                    "FileDescription": "blablabla",
                    "FileFlagsMask": "0x003f",
                    "FileOS": "Win32",
                    "FileSubtype": "0",
                    "FileType": "Win32 EXE",
                    "FileTypeExtension": "exe",
                    "FileVersion": "1.3.30.0",
                    "FileVersionNumber": "1.3.30.0",
                    "ImageFileCharacteristics": "No relocs, Executable, Large address aware, 32-bit",
                    "ImageVersion": "0.0",
                    "InitializedDataSize": "339968",
                    "InternalName": "blablabla.exe",
                    "LanguageCode": "Neutral",
                    "LegalCopyright": "Copyright © blablabla 2020",
                    "LegalTrademarks": "blablabla",
                    "LinkerVersion": "9.0",
                    "MIMEType": "application/octet-stream",
                    "MachineType": "Intel 386 or later, and compatibles",
                    "OSVersion": "5.0",
                    "ObjectFileType": "Executable application",
                    "OriginalFileName": "blablabla.exe",
                    "PEType": "PE32",
                    "ProductName": "blablabla",
                    "ProductVersion": "1.3.30.0",
                    "ProductVersionNumber": "1.3.30.0",
                    "Subsystem": "Windows GUI",
                    "SubsystemVersion": "5.0",
                    "TimeStamp": "2020:04:16 15:35:24+02:00",
                    "UninitializedDataSize": "0"
                },
                "first_submission_date": 1587049407,
                "last_analysis_date": 1588653326,
                "last_analysis_results": {
                    "ALYac": {
                        "category": "malicious",
                        "engine_name": "ALYac",
                        "engine_update": "20200505",
                        "engine_version": "1.1.1.5",
                        "method": "blacklist",
                        "result": "Trojan.GenericKD.42996961"
                    },
                    "APEX": {
                        "category": "malicious",
                        "engine_name": "APEX",
                        "engine_update": "20200504",
                        "engine_version": "6.18",
                        "method": "blacklist",
                        "result": "Malicious"
                    },
                    "AVG": {
                        "category": "undetected",
                        "engine_name": "AVG",
                        "engine_update": "20200505",
                        "engine_version": "18.4.3895.0",
                        "method": "blacklist",
                        "result": null
                    },
                    "Acronis": {
                        "category": "malicious",
                        "engine_name": "Acronis",
                        "engine_update": "20200422",
                        "engine_version": "1.1.1.75",
                        "method": "blacklist",
                        "result": "suspicious"
                    },
                    "Ad-Aware": {
                        "category": "malicious",
                        "engine_name": "Ad-Aware",
                        "engine_update": "20200505",
                        "engine_version": "3.0.5.370",
                        "method": "blacklist",
                        "result": "Trojan.GenericKD.42996961"
                    },
                    "AegisLab": {
                        "category": "undetected",
                        "engine_name": "AegisLab",
                        "engine_update": "20200505",
                        "engine_version": "4.2",
                        "method": "blacklist",
                        "result": null
                    },
                },
                "last_analysis_stats": {
                    "confirmed-timeout": 0,
                    "failure": 0,
                    "harmless": 0,
                    "malicious": 4,
                    "suspicious": 0,
                    "timeout": 1,
                    "type-unsupported": 0,
                    "undetected": 2
                },
                "last_modification_date": 1591945304,
                "last_submission_date": 1587049407,
                "magic": "PE32 executable for MS Windows (GUI) Intel 80386 32-bit",
                "md5": "b67828805dfdabf3a823278c3fdd37f7",
                "meaningful_name": "blablabla.exe",
                "names": [
                    "blablabla.exe",
                    "foo.exe"
                ],
                "pe_info": {
                    "debug": [
                        {
                            "codeview": {
                                "age": 1,
                                "guid": "4743e25-e470-ee67-e2a7-5ce85ee2afb7",
                                "name": "                                                                                                        ",
                                "signature": "RSDS"
                            },
                            "offset": 129512,
                            "size": 129,
                            "timestamp": "Fri Nov 23 19:58:56 2012",
                            "type": 2,
                            "type_str": "IMAGE_DEBUG_TYPE_CODEVIEW"
                        }
                    ],
                    "entry_point": 52463,
                    "imphash": "9dd8c0ffefc8e287e5be665e3240f983",
                    "import_list": [
                        {
                            "imported_functions": [
                                "CreateToolhelp32Snapshot",
                                "GetLastError",
                                "InitializeCriticalSectionAndSpinCount",
                                "HeapFree",
                                "GetStdHandle",
                                "EnterCriticalSection",
                                "LCMapStringW",
                                "HeapCreate",
                                "lstrlenA",
                                "WriteConsoleW",
                                "GetConsoleCP",
                                "GetOEMCP",
                                "LCMapStringA",
                                "IsDebuggerPresent"
                            ],
                            "library_name": "KERNEL32.dll"
                        },
                    },
                    "machine_type": 332,
                    "resource_details": [
                        {
                            "chi2": 829672.125,
                            "entropy": 3.8720788955688477,
                            "filetype": "Data",
                            "lang": "NEUTRAL",
                            "sha256": "3d7460d292abef8a0900ddec6244894d7e2edb054bd13389ee7ed5b8908f3f88",
                            "type": "RT_ICON"
                        },
                        {
                            "chi2": 387563.8125,
                            "entropy": 3.693312168121338,
                            "filetype": "Data",
                            "lang": "NEUTRAL",
                            "sha256": "2802c59713b7872e17df2ef6c9b10b3e879a2618e84c297e8dde8ed452eb5e116",
                            "type": "RT_ICON"
                        },
                    ],
                    "resource_langs": {
                        "NEUTRAL": 2
                    },
                    "resource_types": {
                        "RT_ICON": 3
                    },
                    "sections": [
                        {
                            "chi2": 507704.625,
                            "entropy": 6.74595308303833,
                            "flags": "rx",
                            "md5": "31e33d2e3f3ba3efe0a362c39713b198",
                            "name": ".text",
                            "raw_size": 104448,
                            "virtual_address": 4096,
                            "virtual_size": 104152
                        },
                        {
                            "chi2": 415246.46875,
                            "entropy": 6.443132400512695,
                            "flags": "r",
                            "md5": "2a33cd3e315343b43c3620332d3a9376",
                            "name": ".rdata",
                            "raw_size": 28160,
                            "virtual_address": 110592,
                            "virtual_size": 28146
                        },}
                    ],
                    "timestamp": 1587044124
                },
                "reputation": 0,
                "sha1": "a97e30d504b3e618fc377640d3e65793f6f37625",
                "sha256": "abfa4d040cfb3cd9e22f2301bf0902330ca3a6031ce6a97324b1f1c31494696c",
                "signature_info": {
                    "comments": "blablabla",
                    "copyright": "Copyright © blabla 2020",
                    "description": "blablabla",
                    "file version": "1.3.30.0",
                    "internal name": "blablabla.exe",
                    "original name": "blablabla.exe",
                    "product": "blablabla"
                },
                "size": 445440,
                "ssdeep": "12288:GoL4Ene4T/vjLbeCJ6s8eFuiQe5Lb9u4eQae46/:Gwne4TDLbeBiGeo4e6/",
                "tags": [
                    "peexe",
                    "runtime-modules",
                    "direct-cpu-clock-access",
                    "detect-debug-environment"
                ],
                "times_submitted": 2,
                "total_votes": {
                    "harmless": 0,
                    "malicious": 0
                },
                "trid": [
                    {
                        "file_type": "Win32 Executable MS Visual C++ (generic)",
                        "probability": 41.0
                    },
                    {
                        "file_type": "Win64 Executable (generic)",
                        "probability": 36.3
                    },
                    {
                        "file_type": "Win32 Dynamic Link Library (generic)",
                        "probability": 8.6
                    },
                    {
                        "file_type": "Win32 Executable (generic)",
                        "probability": 5.9
                    },
                    {
                        "file_type": "OS/2 Executable (generic)",
                        "probability": 2.6
                    }
                ],
                "type_description": "Win32 EXE",
                "type_tag": "peexe",
                "unique_sources": 1,
                "vhash": "0450466e6d157ez54ez10etz"
            },
            "id": "abfa4d04ecfb8cd9e22e2301bfe902c30caea6071ce6a9742eb1f1ce1494696c",
            "links": {
                "self": "https://www.virustotal.com/api/v3/files/abfa4d04ecfb8cd9e22e2301bfe902c30caea6071ce6a9742eb1f1ce1494696c"
            },
            "type": "file"
        }
    ],
    "links": {
        "next": "https://www.virustotal.com/api/v3/files/abfa4d04ecfb8cd9e22e2301bfe902c30caea6071ce6a9742eb1f1ce1494696c/carbonblack_children?cursor=STEwCi4%3D&limit=1",
        "self": "https://www.virustotal.com/api/v3/files/abfa4d04ecfb8cd9e22e2301bfe902c30caea6071ce6a9742eb1f1ce1494696c/carbonblack_children?limit=1"
    },
    "meta": {
        "count": 25,
        "cursor": "STEwCi4="
    }
}
```

---

← [🔀 comments](file-object-comments.md) · [up](../README.md) · [🔀 carbonblack_parents](file-object-carbonblack-parents.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-carbonblack-children>.*
