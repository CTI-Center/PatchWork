---
title: "dmg_info"
source: https://gtidocs.virustotal.com/reference/file-object-dmg-info
slug: file-object-dmg-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:09.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › dmg_info

---

# dmg_info

information about mountable macOS disk images.

`dmg_info` reports data about [Apple .dmg file](https://en.wikipedia.org/wiki/Apple_Disk_Image) structure. much data comes from internal metadata files that may appear in some files but other don't.

* `blkx`: <*list of dictionaries*> each item on the list represents a BLKX block in the DMG image and contains the following fields:
  * `attributes`: <*string*> in hex format.
  * `name`: <*string*> block name.
* `data_fork_length`: <*integer*> size of data fork.
* `data_fork_offset`: <*integer*> data fork offset (usually 0).
* `dmg_version`: <*integer*> DMG file version.
* `gtp`: <*dictionary*> information about [GPT header](https://wiki.osdev.org/GPT). Contains the following subfields:
  * `alternate_lba`: <*integer*> the LBA of the alternate GPT header.
  * `disk_uuid`: <*string*> GUID of the disk.
  * `entries_crc32`: <*integer*> CRC32 of the Partition Entry array.
  * `entries_lba`: <*integer*> starting LBA of the GUID Parition Entry array.
  * `first_usable_lba`: <*integer*> the first usable block that can be contained in a GPT entry.
  * `header_crc32`: <*integer*> CRC32 checksum of the GPT header.
  * `last_usable_lba`: <*integer*> the last usable block that can be contained in a GPT entry.
  * `my_lba`: <*integer*> the LBA containing this header.
  * `number_of_entries`: <*integer*> number of Parition Entries.
  * `partitions`: <*list of dictionaries*> contains details about each partition. Every entry contains the following subfields:
    * `attrs_flags`: <*integer*> attributes
    * `ending_lba`: <*integer*> ending LBA.
    * `name`: <*string*> partition name.
    * `starting_lba`: <*integer*> starting LBA.
    * `type_guid`: <*string*> partition Type GUID (zero means unused entry).
    * `unique_guid`: <*string*> unique Partition GUID.
  * `revision`: <*string*> GPT Revision.
  * `signature`: <*string*> signature, can be identified by 8 bytes magic "EFI PART" (45h 46h 49h 20h 50h 41h 52h 54h).
  * `size`: <*integer*> header size.
  * `size_of_entry`: <*integer*> size (in bytes) of each entry in the Parition Entry array - must be a multiple of 8.
* `hfs`: <*dictionary*> information about HFS elements. Depending on each case, different fields may appear or not.
  * `info_plist`: <*dictionary*> block's plist (`Info.plist` file) content. Keys and values are strings.
  * `main_executable`: <*dictionary*> block's main executable. Contains the following subfields:
    * `id`: <*string*> identifier.
    * `path`: <*string*> path inside the package.
    * `sha256`: <*string*> content hash.
    * `size`: <*integer*> file size in bytes.
  * `num_files`: <*integer*> number of files.
  * `unreadable_files`: <*integer*> number of unreadable files.
  * `timeout`: <*boolean*> whether the block's processing took too long or not.
* `iso`: <*dictionary*> information about ISO elements. Depending on each case, different fields may appear or not.
  * `info_plist`: <*dictionary*> block's plist (`Info.plist` file) content. Keys and values are strings.
  * `main_executable`: <*dictionary*> block's main executable. Contains the following subfields:
    * `id`: <*string*> identifier.
    * `path`: <*string*> path inside the package.
    * `sha256`: <*string*> content hash.
    * `size`: <*integer*> file size in bytes.
  * `num_files`: <*integer*> number of files.
  * `unreadable_files`: <*integer*> number of unreadable files.
  * `timeout`: <*boolean*> whether the block's processing took too long or not.
  * `volume_data`: <*dictionary*> ISO volume data. Check [isoimage\_info](file-object-isoimage-info.md) output to know its structure.
* `plst`: <*list of dictionaries*> contains configuration information for the application, such as its bundle ID, version number, and display name. Each entry contains two keys:
  * `attributes`: <*string*> in hex format.
  * `name`: <*string*> attribute name.
* `plst_context`: <*list of strings*> contains extracted interesting strings from a list, such as SLAs.
* `plst_keys`: <*list of strings*> keys of the plst entry.
* `running_data_fork_offset`: <*integer*> specifies where the running data fork starts, usually 0.
* `resourcefork_keys`: <*list of strings*> keys found in the resource fork.
* `rsrc_fork_length`: <*integer*> resource fork length.
* `rsrc_fork_offset`: <*integer*> resource fork offset.
* `xml_lenght`: <*integer*> lenght of property list in DMG.
* `xml_offset`: <*integer*> offset of property list in DMG.

```json Apple .dmg file
{
  "data": {
		...
    "attributes" : {
      ...
      "dmg_info": {
        "blkx": [
          {
            "attributes": "<string>",
            "name": "<string>"
          }, ...
        ],
        "data_fork_length": <int>,
        "data_fork_offset": <int>,
        "dmg_version": <int>,
        "gpt": {
          "alternate_lba": <int>,
          "disk_uuid": "<string>",
          "entries_lba": <int>,
          "first_usable_lba": <int>,
          "header_crc32": <int>,
          "last_usable_lba": <int>,
          "my_lba": <int>,
          "number_of_entries": <int>,
          "partitions": [
          	{
          		"attrs_flags": <int>,
          		"ending_lba": <int>,
          		"name": "<string>",
          		"starting_lba": <int>,
          		"type_guid": "<string>",
          		"unique_guid": "<string>"
          	},...
          ],
          "revision": "<string>",
          "signature": "<string>",
          "size": <int>,
          "size_of_entry": <int>
        },
        "hfs": {
          "info_plist": {
            "<string>": "<string>", ...
          },
          "main_executable": {
            "id": <int>,
            "path": "<string>",
            "sha256": "<string>",
            "size": <int>
          },
          "num_files": <int>,
          "unreadable_files": <int>,
          "timeout": <bool>,
        },
        "iso": {
          "info_plist": {
            "<string>": "<string>", ...
          },
          "main_executable": {
            "id": <int>,
            "path": "<string>",
            "sha256": "<string>",
            "size": <int>
          },
          "num_files": <int>,
          "unreadable_files": <int>,
          "timeout": <bool>,
          "volume_data": <isoimage_info>
        },
        "plst": [
          {
            "attributes": "<string>",
            "name": "<string>"
          }
        ],
		"plst_context": ["<strings>",...],
        "plst_keys": ["<strings>"],
        "running_data_fork_offset": <int>,
        "resourcefork_keys": ["<strings>"],
        "rsrc_fork_length": <int>,
        "rsrc_fork_offset": <int>,
        "xml_length": <int>,
        "xml_offset": <int>
      }
    }
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "dmg_info": {
                "blkx": [
                    {
                        "attributes": "0x0050",
                        "name": "whole disk (Apple_HFS : 0)"
                    }
                ],
                "data_fork_length": 2811866,
                "data_fork_offset": 0,
                "dmg_version": 4,
                "gpt": {
                    "alternate_lba": 1,
                    "disk_uuid": "453d595d-a580-455c-8158-5d5850f54579",
                    "entries_crc32": 3948022686,
                    "entries_lba": 16414,
                    "first_usable_lba": 34,
                    "header_crc32": 1111275827,
                    "last_usable_lba": 16413,
                    "my_lba": 16446,
                    "number_of_entries": 128,
                    "partitions": [
                        {
                            "attrs_flags": 0,
                            "ending_lba": 16407,
                            "name": "disk image",
                            "starting_lba": 40,
                            "type_guid": "48455350-0500-51aa-5a11-50356545ecac",
                            "unique_guid": "e5005611-561f-45b6-5659-84565150f5f2"
                        }
                    ],
                    "revision": "0x100",
                    "signature": "EFI PART",
                    "size": 92,
                    "size_of_entry": 128
                },
                "hfs": {
                    "info_plist": {
                        "BuildMachineOSBuild": "18G5033",
                        "CFBundleDevelopmentRegion": "English",
                        "CFBundleExecutable": "Blablabla",
                        "CFBundleHelpBookFolder": "help",
                        "CFBundleHelpBookName": "BLablabla blablabla blablabla",
                        "CFBundleIconFile": "app.icns",
                        "CFBundleIdentifier": "com.nchsoftware.blablabla-free",
                        "CFBundleInfoDictionaryVersion": "6.0",
                        "CFBundleLongVersionString": "8.14, Copyright BBB Software",
                        "CFBundleName": "Blablabla",
                        "CFBundlePackageType": "APPL",
                        "CFBundleShortVersionString": "8.14",
                        "CFBundleSignature": "bbbbb",
                        "CFBundleSupportedPlatforms": "['MacOSX']",
                        "CFBundleVersion": "8.14",
                        "CFExecutableName": "Blablabla",
                        "CSResourcesFileMapped": "True",
                        "DTCompiler": "com.apple.compilers.llvm.clang.1_0",
                        "DTPlatformBuild": "11C504",
                        "DTPlatformVersion": "GM",
                        "DTSDKBuild": "13C64",
                        "DTSDKName": "macosx10.9",
                        "DTXcode": "1130",
                        "DTXcodeBuild": "11C504",
                        "LSApplicationCategoryType": "public.app-category.business",
                        "LSMinimumSystemVersion": "10.9",
                        "NSAppleEventsUsageDescription": "Please give access to System Events to execute Apple Script",
                        "NSAppleScriptEnabled": "YES",
                        "NSHighResolutionCapable": "True",
                        "NSMainNibFile": "cocoamain.nib",
                        "NSPrincipalClass": "NSApplication"
                    },
                    "main_executable": {
                        "path": "/ExpressInvoice.app/Contents/MacOS/blablabla",
                        "sha256": "b8cb282df06482cf6a749b04c779dabdd07e384494b2b443d4748f4b02454414",
                        "size": 5413968
                    },
                    "num_files": 171,
                    "unreadable_files": 0
                },
                "iso": {
                    "info_plist": {
                        "BuildMachineOSBuild": "14A389",
                        "CFBundleDevelopmentRegion": "en",
                        "CFBundleExecutable": "agent",
                        "CFBundleIdentifier": "com.someproduct.agent",
                        "CFBundleInfoDictionaryVersion": "6.0",
                        "CFBundleName": "agent",
                        "CFBundlePackageType": "APPL",
                        "CFBundleShortVersionString": "1.0",
                        "CFBundleSignature": "????",
                        "CFBundleVersion": "1",
                        "DTCompiler": "com.apple.compilers.llvm.clang.1_0",
                        "DTPlatformBuild": "5B1008",
                        "DTPlatformVersion": "GM",
                        "DTSDKBuild": "11E52",
                        "DTSDKName": "macosx10.7",
                        "DTXcode": "0511",
                        "DTXcodeBuild": "5B1008",
                        "LSMinimumSystemVersion": "10.7",
                        "LSUIElement": true,
                        "NSHumanReadableCopyright": "Copyright b 2014 . All rights reserved.",
                        "NSPrincipalClass": "NSApplication"
                    },
                    "main_executable": {
                        "datetime": "2014-12-31 13:56:12",
                        "path": "blabla.app/Contents/MacOS/Installer",
                        "sha256": "b6d7a1a1767bbf4a8e132e752c6b276ec3a673114eece7f3be07e177985be1b5",
                        "size": 282576,
                        "type": "Mac OS X Executable"
                    },
                    "num_files": 94,
                    "volume_data": {
                        "application_id": "blabla",
                        "created": "2015-02-04 10:45:28",
                        "effective": "2015-02-04 10:45:28",
                        "expires": "0000-00-00 00:00:00",
                        "file_structure_version": 1,
                        "max_date": "2015-02-04 11:45:28",
                        "min_date": "2014-12-31 13:56:12",
                        "modified": "2015-02-04 10:45:28",
                        "num_files": 94,
                        "system_id": "LINUX",
                        "total_size": 4169592,
                        "type_code": "CD001",
                        "volume_id": "blabla"
                    }
                },
                "plst": [
                    {
                        "attributes": "0x0050",
                        "name": "ID:0"
                    }
                ],
                "plst_context": [
                    "Default Language IDDWRD CountOCNT ****LSTC sys lang IDDWRD local res ID (offset from 5000DWRD 2-byte language?DWRD ****LSTE",
                    "Fran ais Accepter Refuser Imprimer Enregistrer... Si vous acceptez les termes de la pr sente licence, cliquez sur \"Accepter\" afin d\\'installer le logiciel. Si vous n\\' tes pas d\\'accord avec les terme",
                    "Deutsch Akzeptieren Ablehnen Drucken Sichern... Klicken Sie in  Akzeptieren , wenn Sie mit den Bestimmungen des Software-Lizenzvertrags einverstanden sind. Falls nicht, bitte  Ablehnen  anklicken. Sie",
                    "English Agree Disagree Print Save...{If you agree with the terms of this license, press \"Agree\" to install the software.  If you do not agree, press \"Disagree\".",
                    "Espa ol Aceptar No aceptar Imprimir Guardar... Si est  de acuerdo con los t rminos de esta licencia, pulse \"Aceptar\" para instalar el software. En el supuesto de que no est  de acuerdo con los t rmino",
                    "Fran ais Accepter Refuser Imprimer Enregistrer... Si vous acceptez les termes de la pr sente licence, cliquez sur \"Accepter\" afin d\\'installer le logiciel. Si vous n\\' tes pas d\\'accord avec les terme",
                    "Italiano Accetto Rifiuto Stampa Registra... Se accetti le condizioni di questa licenza, fai clic su \"Accetto\" per installare il software. Altrimenti fai clic su \"Rifiuto\"."
                ],
                "plst_keys": [
                    "resource-fork"
                ],
                "resourcefork_keys": [
                    "TMPL",
                    "blkx",
                    "plst",
                    "TEXT",
                    "STR#",
                    "LPic"
                ],
                "rsrc_fork_length": 10864,
                "rsrc_fork_offset": 2831884,
                "running_data_fork_offset": 0,
                "xml_length": 20018,
                "xml_offset": 2811866
            }
        }
    }
}
```

---

← [magic](file-object-magic.md) · [up](../README.md) · [elf_info](file-object-elf-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-dmg-info>.*
