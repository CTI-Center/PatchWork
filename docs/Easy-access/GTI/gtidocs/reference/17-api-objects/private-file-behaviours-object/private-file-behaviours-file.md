---
title: "🔀 file"
source: https://gtidocs.virustotal.com/reference/private-file-behaviours-file
slug: private-file-behaviours-file
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:44:26.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Private Files Behaviours](../private-file-behaviours-object.md) › 🔀 file

---

# 🔀-file

Private file behaviour's file.

The *file* relationship returns the ***file for a given behaviour report***.

This relationship can be retrieved using the [relationships API endpoint](../../06-private-scanning/private-files-behaviours/privatefile-behaviourssandbox-idrelationship.md). The response contains a [private file](../private-files-object.md) object.

```json /private/file_behaviours/{id}/file
{
  "data": <PRIVATE_FILE>,
  "links": {
    "self": <string>
  },
  "meta": {
    "count": <int>,
  }
}
```
```json Example
{
  "meta": {
    "count": 1
  },
  "data": {
    "attributes": {
      "type_description": "Android",
      "tlsh": "T1EF861292F3CCF916D577C03396A30627698A4C488B06E7561B18F37C9AF7AD04E46BC9",
      "vhash": "9f5dce0c8a94230798f5316d2b949c63",
      "exiftool": {
        "ZipRequiredVersion": "0",
        "MIMEType": "application/zip",
        "ZipCRC": "0xf573acfd",
        "FileType": "ZIP",
        "ZipCompression": "Deflated",
        "ZipUncompressedSize": "10276",
        "ZipCompressedSize": "2485",
        "FileTypeExtension": "zip",
        "ZipFileName": "AndroidManifest.xml",
        "ZipBitFlag": "0",
        "ZipModifyDate": "1980:00:00 00:00:00"
      },
      "trid": [
        {
          "file_type": "Android Package",
          "probability": 51.6
        },
        {
          "file_type": "Java Archive",
          "probability": 18.1
        },
        {
          "file_type": "Sweet Home 3D design (generic)",
          "probability": 14.0
        },
        {
          "file_type": "Mozilla Archive Format (gen)",
          "probability": 9.3
        },
        {
          "file_type": "ZIP compressed archive",
          "probability": 5.3
        }
      ],
      "type_tag": "android",
      "size": 7927753,
      "sha256": "1d5156ab08b6a193b8326c246847dcf14f7afcdff560729bee11b682b748ba75",
      "type_extension": "apk",
      "tags": [
        "obfuscated",
        "reflection",
        "telephony",
        "runtime-modules",
        "crypto",
        "mysql-communication",
        "apk",
        "clipboard",
        "android"
      ],
      "sha1": "9733cd39998576ef4f4a4c342f21b0542b578f25",
      "ssdeep": "196608:rhhZd9eKsLCxPX+oJi5M2wD6rqztYN6Cjr8fok+:DZ7ekPlbcQyn8foH",
      "bundle_info": {
        "highest_datetime": "1980-00-00 00:00:00",
        "lowest_datetime": "1980-00-00 00:00:00",
        "num_children": 1196,
        "extensions": {
          "xml": 172,
          "dex": 2,
          "MF": 1,
          "RSA": 1,
          "ttf": 1,
          "txt": 128,
          "SF": 1,
          "png": 674
        },
        "file_types": {
          "XML": 171,
          "unknown": 153,
          "DEX": 2,
          "PNG": 674
        },
        "type": "APK",
        "uncompressed_size": 15796683
      },
      "md5": "c1b653edcb6c03e90ffe3b2493854994",
      "magic": "Zip archive data",
      "main_icon": {
        "raw_md5": "260d5710e1e27ff5400ca82d93f79edc",
        "dhash": "82c0e2e8cccce830"
      }
    },
    "type": "private_file",
    "id": "1d5156ab08b6a193b8326c246847dcf14f7afcdff560729bee11b682b748ba75",
    "links": {
      "self": "https://www.virustotal.com/api/v3/private/files/1d5156ab08b6a193b8326c246847dcf14f7afcdff560729bee11b682b748ba75"
    }
  },
  "links": {
    "self": "https://www.virustotal.com/api/v3/private/file_behaviours/1d5156ab08b6a193b8326c246847dcf14f7afcdff560729bee11b682b748ba75_VirusTotal R2DBox-12345/file"
  }
}
```

---

← [Private Files Behaviours](../private-file-behaviours-object.md) · [up](../README.md) · [🔀 attack_techniques](private-file-behaviours-attack_techniques.md) →

*Archived from <https://gtidocs.virustotal.com/reference/private-file-behaviours-file>.*
