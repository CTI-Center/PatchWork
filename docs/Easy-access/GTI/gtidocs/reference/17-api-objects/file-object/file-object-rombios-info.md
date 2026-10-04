---
title: "rombios_info"
source: https://gtidocs.virustotal.com/reference/file-object-rombios-info
slug: file-object-rombios-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:04.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › rombios_info

---

# rombios_info

information about BIOS, EFI, UEFI and related archives.

`rombios_info` shows information about firmware files.

* `acpi_tables`: <*list of strings*> Advanced Configuration and Power Interface tables present in this image.
* `apple_metadata`: <*dictionary*> metadata from Apple EFI firmware files. presented as a list of tuples, with key and values. some typical keys and values are:
  * `Board ID`: <*string*> build identificator.
  * `Built by`: <*string*> name of builder of the file.
  * `Date`: <*string*> file creation date in `%a %b %m %H:%M:%S %Z %Y` [format](http://strftime.org/).
  * `Revision`: <*string*> build revision.
  * `ROM Version`: <*string*> ROM version.
  * `Buildcave ID`: <*string*> buildcave identificator.
* `bios_information`: <*dictionary*> some details about the BIOS file.
  * `bios_release`: <*string*> release version.
  * `characteristics`: <*list of strings*> BIOS characteristics like "PCI supported", "8042 keyboard supported", etc.
  * `release_date`: <*string*> release date in `%m/%d/%Y` [format](http://strftime.org/).
  * `rom_size`: <*string*> ROM size in easy-reading format (i.e. "2MB").
  * `runtime_size`: <*string*> size of runtime in easy-reading format (i.e. "64.0KB").
  * `starting_address_segment`: <*string*> in hexadecimal format.
  * `vendor`: <*string*> BIOS vendor.
  * `version`: <*string*> full version of this BIOS file.
* `certs`: <*list of dictionaries*> certificates found in the firmware file.
  * `issuer`: <*string*> issuer RDNs and values.
  * `subject`: <*string*> subject RDNs and values.
  * `valid_from`: <*string*> cert validity start in in `%Y-%m-%d %H:%M%S` [format](http://strftime.org/).
  * `valid_to`: <*string*> cert validity end in in `%Y-%m-%d %H:%M%S` [format](http://strftime.org/).
* `contained_hash`: <*string*> composed hash idenfying all PE binaries to help find other firmwares with the same file contents.
* `executable_files`: <*integer*> number of executable files found in the bundle.
* `extra`: <*string*> extra information about suspicious volumes that was not directly parsed.
* `firmware_volumes`: <*integer*> number of firmware volumes found.
* `format`: <*string*> bundle format (i.e. "ROMFLASH\_HEADER").
* `manufacturer_strings`: <*dictionary*> references to BIOS manufactures. Key is the manufacturer name as *string* and value is the number of references as *integer*.
* `max_tree_level`: <*integer*> maximum tree depth in the bundle.
* `nvar_variable_names`: <*list of strings*> found NVAR variables.
* `option_roms`: <*list of dictionaries*> an option ROM is a piece of firmware that resides in BIOS or on an expansion card, which gets shadowed into memory and executed to initialise the device and register it with the BIOS. It is essentially a driver that interfaces between BIOS services and hardware. Every subitem contains the following fields:
  * `entrypoint`: <*string*> option ROM entrypoint in hex format.
  * `manufacturer`: <*string*> manufacturer name.
  * `product`: <*string*> product name.
  * `sha256`: <*string*> option ROM content SHA256.
  * `size`: <*integer*> option ROM size in bytes.
  * `type`: <*string*> type defined in the firmware (legacy, pci, pnp...).
* `raw_objects`: <*integer*> number of raw objects.
* `raw_sections`: <*integer*> number of raw sections.
* `sections`: <*integer*> number of sections.
* `smbios_data`: <*dictionary*> SMBIOS version and structures information.
  * `version`: <*string*> version of the file.
  * `table_address`: <*string*> file table address.
  * `table_length`: <*integer*> file table length.
  * `structures_count`: <*integer*> number of structures.
* `system_information`: <*dictionary*> information about the platform for this file.
  * `family`: <*string*> identifies the family to which a particular computer belongs. A family refers to a set of computers that are similar but not identical from a hardware or software point of view.
  * `manufacturer`: <*string*> BIOS manufacturer.
  * `product_name`: <*string*> product name.
  * `serial_number`: <*string*> product serial number.
  * `sku`: <*string*> identifies a particular computer configuration for sale. It is sometimes also called a product ID or purchase order number.
  * `uuid`: <*string*> unique identifier.
  * `version`: <*string*> product version.

```json Firmware images
{
  "data": {
		...
    "attributes" : {
      ...
      "rombios_info": {
        "acpi_tables": [
            "<strings>"
        ],
        "apple_metadata": {
        		"<string>": "<string>
        },
        "bios_information": {
            "bios_release": "<string>",
            "characteristics": ["<strings>"],
            "rom_size": "<string>",
            "release_date": "<string:%m/%d/%Y>",
            "runtime_size": "<string>",
            "starting_address_segment": "<string>",
            "vendor": "<string>",
            "version": "<string>"
        },
        "certs":[
            {
                "issuer": "<string>",
                "subject": "<string>",
                "valid_from": "<string:%Y-%m-%d %H:%M:%S>",
                "valid_to": "<string:%Y-%m-%d %H:%M:%S>"
            }, ...
        ],
        "executable_files": <int>,
        "firmware_volumes": <int>,
        "format": "<string>",
        "manufacturer_strings": {
            "<string>": <int>, ...
        },
        "nvar_variable_names": [
            "<strings>"
        ],
        "option_roms": [
          	{
            	"entrypoint": "<string>,
              	"manufacturer": "<string>",
              	"product": "<string>",
              	"sha256": "<string>",
              	"size": <int>,
              	"type": "<string>
            },
        ],
        "raw_objects": <int>,
        "sections": <int>,
        "smbios_data": {
            "<string>": "<string>", ...
        },
        "system_information": {
            "family": "<string>",
            "fanufacturer": "<string>",
            "product_name": "<string>",
            "sku": "<string>",
            "serial_number": "<string>",
            "uuid": "<string>",
            "version": "<string>"
        }
      }
    }
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "rombios_info": {
                "acpi_tables": [
                    "DSDT",
                    "SSDT"
                ],
                "bios_information": {
                    "bios_release": "5.16",
                    "characteristics": [
                        "PCI supported",
                        "BIOS upgradeable",
                        "BIOS shadowing allowed",
                        "Boot from CD supported",
                        "Selectable boot supported",
                        "BIOS ROM socketed",
                        "EDD supported",
                        "5.25\"/1.2MB floppy supported"
                    ],
                    "release_date": "03/19/2020",
                    "rom_size": "16.0MB",
                    "runtime_size": "64.0KB",
                    "starting_address_segment": "0xf0000",
                    "vendor": "blablabla Inc.",
                    "version": "5.16"
                },
                "certs": [
                    {
                        "issuer": "CN=blabla Certificate",
                        "subject": "CN=blabla Certificate",
                        "valid_from": "2015-12-29 06:18:20",
                        "valid_to": "2031-12-22 04:18:19"
                    },
                    {
                        "issuer": "CN=blabla",
                        "subject": "CN=blabla",
                        "valid_from": "2014-12-24 05:18:35",
                        "valid_to": "2031-12-22 05:18:34"
                    }
                ],
                "contained_hash": "8e7073511a1b5f279f533997e5ec499f25a566d53960252dc71595525024f214",
                "executable_files": 261,
                "extra": "0x800 (EFI_FIRMWARE_FILESYSTEM2_GUID); 0x748800 (EFI_FIRMWARE_FILESYSTEM2_GUID); 0xd00800 (EFI_FIRMWARE_FILESYSTEM2_GUID) - '\\x8b\\xa6<J#'",
                "firmware_volumes": 4,
                "format": "SUSPICIOUS_VOLUME_HEADERS",
                "manufacturer_strings": {
                    "ASUSTeK": 1,
                    "Intel": 2,
                    "Lenovo": 4
                },
                "max_tree_level": 13,
                "nvar_variable_names": [
                    "AMITSESetup",
                    "NetworkStackVar",
                    "PCI_COMMON",
                    "PlatformLang"
                ],
                "raw_objects": 2,
                "raw_sections": 140,
                "sections": 1176,
                "smbios_data": {
                    "structures_count": 16,
                    "version": "3.2"
                },
                "system_information": {
                    "family": "Default string",
                    "manufacturer": "blablabla Inc.",
                    "product_name": "Default string",
                    "serial_number": "Default string",
                    "sku": "Default string",
                    "uuid": "03000200-0400-0500-0006-000700080009",
                    "version": "Default string"
                },
                "win32_files": 2
            }
        }
    }
}
```
```json Example (apple)
{
    "data": {
        "attributes": {
            "rombios_info": {
                "acpi_tables": [
                    "APIC",
                    "DMAR",
                    "DSDT",
                    "FACP"
                ],
                "apple_metadata": {
                    "Build Type": "Official Build, Release",
                    "Built by": "blablabla",
                    "Compiler": "Apple clang version 3.0 (tags/Apple/clang-211.10.1) (based on LLVM 3.0svn)",
                    "Date": "Thu Jun 13 20:45:31 PDT 2019",
                    "EFI Version": "287.0.0.0.0",
                    "Model": "IM131",
                    "ROM Version": "F000_B00",
                    "Revision": "287 (B&I)"
                },
                "certs": [
                    {
                        "issuer": "OU=Master Certificate, O=NVIDIA Corp., L=Santa Clara, ST=California, C=US",
                        "subject": "OU=Partner Certificate, O=Apple, L=Cupertino, ST=CA, C=US",
                        "valid_from": "2012-06-05 01:57:41",
                        "valid_to": "2012-12-02 01:57:41"
                    },
                    {
                        "issuer": "OU=Root Certificate, O=NVIDIA Corp., L=Santa Clara, ST=California, C=US",
                        "subject": "OU=Master Certificate, O=NVIDIA Corp., L=Santa Clara, ST=California, C=US",
                        "valid_from": "2011-10-07 23:03:57",
                        "valid_to": "2021-10-06 23:03:57"
                    }
                ],
                "contained_hash": "7b99355c891d53e6d459501ee2825a9db695587ea55c6845384db2df5bc866cd",
                "executable_files": 252,
                "firmware_volumes": 11,
                "format": "EFI_CAPSULE",
                "manufacturer_strings": {
                    "Intel": 1
                },
                "max_tree_level": 25,
                "option_roms": [
                    {
                        "entrypoint": "JMP 0xdfce",
                        "sha256": "73413d143f72ef4776746f4ad7c7bd420dd6b40d65564b3ab54a12454c1c4e6c",
                        "size": 65536,
                        "type": "pci"
                    },
                    {
                        "entrypoint": "JMP 0x50",
                        "sha256": "9ec4c3fef9428902449b98424c313004908a4a34ae444385f49dd94456749447",
                        "size": 90112,
                        "type": "pci"
                    },
                    {
                        "entrypoint": "JMP 0x50",
                        "sha256": "c148aeb1466bcb4085b142c9d24948abf484138549d3cb422b3f417704a1d4b4",
                        "size": 90112,
                        "type": "pci"
                    }
                ],
                "raw_objects": 1,
                "raw_sections": 281,
                "sections": 1258,
                "smbios_data": {
                    "version": "2.4"
                }
            }
        }
    }
}
```

---

← [asf_info](file-object-asf-info.md) · [up](../README.md) · [class_info](file-object-class-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-rombios-info>.*
