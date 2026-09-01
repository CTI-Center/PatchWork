---
title: "bundle_info"
source: https://gtidocs.virustotal.com/reference/file-object-bundle-info
slug: file-object-bundle-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:06.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › bundle_info

---

# bundle_info

information about compressed files.

`bundle_info` gives information about compressed files (ZIP, RAR, GZIP, etc).

* `beginning:` <*string*> decompressed head of the file for some file formats: ZLIB and GZIP.
* `error`: <*string*> error message when attempting to decompress the bundle.
* `extensions`: <*dictionary*> contains file extensions as key and how many of each one there is inside the bundle as value.
* `file_types`: <*dictionary*> contains file types as key and how many of each one there is inside the bundle as value.
* `highest_datetime`: <*string*> most recent date in contained files, in `%Y-%m-%d %H:%M:%S` [format](http://strftime.org/).
* `lowest_datetime`: <*string*> oldest date in contained files, in `%Y-%m-%d %H:%M:%S` [format](http://strftime.org/).
* `num_children`: <*integer*> how many files and directories there are inside the bundle.
* `password`: <*string*> password to decrypt the bundle, if found.
* `type`: <*string*> bundle type: "ZIP", "RAR", "ZLIB", "TAR", "BZIP" and "GZIP"
* `uncompressed_size`: <*integer*> uncompressed size of content inside the compressed file.

```json Compressed files information
{
  "data": {
		...
    "attributes" : {
      ...
      "bundle_info": {
        "beginning": "<string>",
        "error": "<string>",
        "extensions": {
          	"<string>": <int>, ...
        },
        "file_types": {
          	"<string>": <int>, ...
        },
        "highest_datetime": "<string:%Y-%m-%d %H:%M:%S>",
        "lowest_datetime": "<string:%Y-%m-%d %H:%M:%S>",
        "num_children": <int>,
        "password": "<string>",
        "type": "<string>",
        "uncompressed_size": <int>
      }
    }
  }
}
```
```json Example (ZIP)
{
    "data": {
        "attributes": {
            "bundle_info": {
                "extensions": {
                    "exe": 1
                },
                "file_types": {
                    "Portable Executable": 1,
                    "XML": 1
                },
                "highest_datetime": "2017-06-07 09:07:38",
                "lowest_datetime": "1980-01-00 00:00:00",
                "num_children": 2,
                "password": "infected",
                "type": "ZIP",
                "uncompressed_size": 222702
            }
        }
    }
}
```
```json Example (Corrupted GZIP)
{
    "data": {
        "attributes": {
            "bundle_info": {
                "beginning": "PK\u0003\u0004\u0014\u0000\u0000\u0000\b\u0000\u000fh0P\ufffdr\f\u0012\ufffd\u0010\u0000\u0000\ufffdO\u0000\u0000\u0013\u0000\u0000\u0000AndroidManifest.xml\ufffdZk\ufffd\\\u0551\ufffd\ufffd\ufffd\ufffd\ufffd\u0018{\ufffd\u001d0\ufffd\ufffd`\ufffd\u0006\ufffd\ufffd1\ufffd\u0018\ufffd\ufffd\ufffd=\u001e\ufffd\ufffd\ufffd\u0003p\u0018\ufffd\ufffdb\ufffdn\ufffd\ufffdy9\ufffd$\ufffd$\ufffd\ufffdU~$\u0011\ufffd\ufffd\ufffd@\ufffd\rJ\ufffd(R\ufffd]\ufffd",
                "error": "CRC check failed 0x3e8059d7 != 0x1add145aL",
                "num_children": 1,
                "type": "GZIP",
                "uncompressed_size": 3646766
            }
        }
    }
}
```

---

← [class_info](file-object-class-info.md) · [up](../README.md) · [deb_info](file-object-deb-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-bundle-info>.*
