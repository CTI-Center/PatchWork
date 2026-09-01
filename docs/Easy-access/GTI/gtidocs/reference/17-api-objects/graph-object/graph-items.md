---
title: "🔀 items"
source: https://gtidocs.virustotal.com/reference/graph-items
slug: graph-items
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T02:12:21.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Graphs](../graph-object.md) › 🔀 items

---

# 🔀-items

Contained objects in the graph

The *items* relationship returns all ***objects contained in a given graph***.

It can be fetched using the [relationships API endpoint](../../10-threat-graph/threat-graphs/graphs-relationships.md) and it returns a list of [File](../../03-ioc-investigation/files.md), [URL](../url-object.md), [IP address](../ip-object.md) and [Domain](../domains-object.md) objects.

```json /graphs/{id}/items
{
  "data": [
    <URL_OBJECT>,
    <DOMAIN_OBJECT>,
    <FILE_OBJECT>,
    <IP_ADDRESS_OBJECT>,
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
        "bundle_info": {
          "extensions": {
            "css": 124,
            "db": 10,
            "eot": 10,
            "gif": 3,
            "ico": 3,
            "jpg": 34,
            "js": 284,
            "map": 1,
            "md": 5,
            "otf": 3,
            "png": 129,
            "psd": 3,
            "rtf": 1,
            "svg": 12,
            "ttf": 22,
            "txt": 9
          },
          "file_types": {
            "GIF": 3,
            "HTML": 117,
            "JPG": 34,
            "JSON": 1,
            "JavaScript": 22,
            "Microsoft Office": 10,
            "PNG": 129,
            "RTF": 1,
            "XML": 12,
            "unknown": 671
          },
          "highest_datetime": "2015-03-08 01:21:02",
          "lowest_datetime": "2012-03-28 01:58:32",
          "num_children": 2469,
          "type": "RAR",
          "uncompressed_size": 28394761
        },
        "downloadable": true,
        "exiftool": {
          "ArchivedFileName": "blablabla",
          "CompressedSize": "1216",
          "FileType": "RAR",
          "FileTypeExtension": "rar",
          "MIMEType": "application/x-rar-compressed",
          "ModifyDate": "2014:12:27 07:51:11",
          "OperatingSystem": "Win32",
          "PackingMethod": "Stored",
          "UncompressedSize": "1150"
        },
        "first_seen_itw_date": 1433004916,
        "first_submission_date": 1442272417,
        "last_analysis_date": 1442272417,
        "last_analysis_results": {
          "ALYac": {
            "category": "undetected",
            "engine_name": "ALYac",
            "engine_update": "20150914",
            "engine_version": "1.0.1.4",
            "method": "blacklist",
            "result": null
          },
          "AVG": {
            "category": "undetected",
            "engine_name": "AVG",
            "engine_update": "20150914",
            "engine_version": "16.0.0.4419",
            "method": "blacklist",
            "result": null
          }
        },
        "last_analysis_stats": {
          "confirmed-timeout": 0,
          "failure": 0,
          "harmless": 0,
          "malicious": 1,
          "suspicious": 0,
          "timeout": 0,
          "type-unsupported": 0,
          "undetected": 55
        },
        "last_submission_date": 1442272417,
        "magic": "RAR archive data, v14, os: Win32",
        "md5": "3c2f2405db6b7cc0199c4f1696dfc55f",
        "meaningful_name": "verymal.rar",
        "names": [
          "verymal.rar"
        ],
        "packers": {
          "F-PROT": "maxorder, appended, UTF-8, eval"
        },
        "reputation": 0,
        "sha1": "29668adf86fd64a5a6e81a97eea40c0ce74819e2",
        "sha256": "197b4185f51ab60c6407d6a55cccfb6e83de9e250f940e25bf42e4a1f1a8ef83",
        "size": 40770845,
        "ssdeep": "444608:94D341M434I4S4B474W4F4p4+k494v44j:94E4H4B4AW4L4040",
        "tags": [
          "rar"
        ],
        "times_submitted": 1,
        "total_votes": {
          "harmless": 0,
          "malicious": 0
        },
        "trid": [
          {
            "file_type": "RAR Archive",
            "probability": 83.3
          },
          {
            "file_type": "REALbasic Project",
            "probability": 16.6
          }
        ],
        "type_description": "RAR",
        "type_tag": "rar",
        "unique_sources": 1,
        "vhash": "e4c9484b4c404e54d47e414e464d4744"
      },
      "id": "197b4185f51ab60c6407d6a55cccfb6e83de9e250f940e25bf42e4a1f1a8ef83",
      "links": {
        "self": "https://www.virustotal.com/api/v3/files/197b4185f51ab60c6407d6a55cccfb6e83de9e250f940e25bf42e4a1f1a8ef83"
      },
      "type": "file"
    }
  ],
  "links": {
    "next": "https://www.virustotal.com/api/v3/files/g0538d03053194c338643183e315b134ec3463a392330430938033934f3be3f37/items?cursor=STEKLg%3D%3D&limit=1",
    "self": "https://www.virustotal.com/api/v3/files/g0538d03053194c338643183e315b134ec3463a392330430938033934f3be3f37/items?limit=1"
  },
  "meta": {
    "count": 37,
    "cursor": "STEKLg=="
  }
}
```

---

← [🔀 group](graph-group.md) · [up](../README.md) · [🔀 owner](graph-owner.md) →

*Archived from <https://gtidocs.virustotal.com/reference/graph-items>.*
