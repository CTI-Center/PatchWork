---
title: "🔀🧑‍💻 matching_files"
source: https://gtidocs.virustotal.com/reference/retrohunt-job-matching-files
slug: retrohunt-job-matching-files
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:44:32.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Retrohunt Jobs](../retrohunt-job-object.md) › 🔀🧑‍💻 matching_files

---

# 🔀🧑‍💻-matching_files

Files matching the Retrohunt job.

The *matching\_files* relationship returns ***all files matched by a given Retrohunt job***. This relationship is only visible for the account's owner.

This relationship can be retrieved by using the relationships API endpoint and returns a list of [File](../file-object.md) objects. In addition, it includes the following context attributes:

* `match_in_subfile`: <*boolean*> whether the match was in a [subfile](../file-object/file-object-bundled-files.md) or not.
* `rule_name`: <*string*> matched rule name.

```json /intelligence/retrohunt_jobs/{id}/matching_files
{
  "data": [
    {
      "attributes": <FILE_OBJECT>,
      "context_attributes": {
        "match_in_subfile": <boolean>,
        "rule_name": "<string>"
      },
      "id": "<sha256>",
      "links": {
        "self": "https://www.virustotal.com/api/v3/files/<id>"
      },
      "type": "file"
    }
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
        "downloadable": true,
        "exiftool": {
          "FileType": "TXT",
          "FileTypeExtension": "txt",
          "LineCount": "1",
          "MIMEEncoding": "us-ascii",
          "MIMEType": "text/plain",
          "Newlines": "(none)",
          "WordCount": "2"
        },
        "first_submission_date": 1598962601,
        "last_analysis_date": 1598962601,
        "last_analysis_results": {
          "ALYac": {
            "category": "undetected",
            "engine_name": "ALYac",
            "engine_update": "20200901",
            "engine_version": "1.1.1.5",
            "method": "blacklist",
            "result": null
          },
          "APEX": {
            "category": "type-unsupported",
            "engine_name": "APEX",
            "engine_update": "20200901",
            "engine_version": "6.66",
            "method": "blacklist",
            "result": null
          },
          "AVG": {
            "category": "undetected",
            "engine_name": "AVG",
            "engine_update": "20200901",
            "engine_version": "18.4.3895.0",
            "method": "blacklist",
            "result": null
          },
          "Acronis": {
            "category": "type-unsupported",
            "engine_name": "Acronis",
            "engine_update": "20200806",
            "engine_version": "1.1.1.77",
            "method": "blacklist",
            "result": null
          }
        },
        "last_analysis_stats": {
          "confirmed-timeout": 0,
          "failure": 0,
          "harmless": 0,
          "malicious": 0,
          "suspicious": 0,
          "timeout": 0,
          "type-unsupported": 2,
          "undetected": 2
        },
        "last_modification_date": 1598962633,
        "last_submission_date": 1598962601,
        "magic": "ASCII text, with very long lines, with no line terminators",
        "md5": "54004e164da4148b43974e94044b4094",
        "meaningful_name": "blablabla",
        "names": [
          "blablabla"
        ],
        "reputation": 0,
        "sha1": "5105a15c25155c5058f505b535658585c6545855",
        "sha256": "95554c5e6b5f755f59c5af53351750655540553525e75a5b55e45b75515e9565",
        "size": 410,
        "ssdeep": "12:S474d4/4664gM4+4s4vJ4c4cJ4Zf44A40n44X+49b:404r474g434S4d4+49b",
        "tags": [
          "text"
        ],
        "times_submitted": 1,
        "total_votes": {
          "harmless": 0,
          "malicious": 0
        },
        "type_description": "Text",
        "type_tag": "text",
        "unique_sources": 1
      },
      "context_attributes": {
        "match_in_subfile": false,
        "rule_name": "maze_ransomware"
      },
      "id": "95554c5e6b5f755f59c5af53351750655540553525e75a5b55e45b75515e9565",
      "links": {
        "self": "https://www.virustotal.com/api/v3/files/95554c5e6b5f755f59c5af53351750655540553525e75a5b55e45b75515e9565"
      },
      "type": "file"
    }
  ],
  "links": {
    "next": "https://www.virustotal.com/api/v3/intelligence/retrohunt_jobs/spellman-1598966772/matching_files?cursor=STEwCi4%3D&limit=1",
    "self": "https://www.virustotal.com/api/v3/intelligence/retrohunt_jobs/spellman-1598966772/matching_files?limit=1"
  },
  "meta": {
    "count": 88,
    "cursor": "STEwCi4="
  }
}
```

---

← [Retrohunt Jobs](../retrohunt-job-object.md) · [up](../README.md) · [🔀🧑‍💻 owner](retrohunt-job-owner.md) →

*Archived from <https://gtidocs.virustotal.com/reference/retrohunt-job-matching-files>.*
