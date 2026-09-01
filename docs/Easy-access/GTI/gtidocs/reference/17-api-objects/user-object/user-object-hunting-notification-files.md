---
title: "🔀🧑‍💻 hunting_notification_files"
source: https://gtidocs.virustotal.com/reference/user-object-hunting-notification-files
slug: user-object-hunting-notification-files
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:45:51.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Users](../user-object.md) › 🔀🧑‍💻 hunting_notification_files

---

# 🔀🧑‍💻-hunting_notification_files

Files flagged in the hunting notifications for the user.

The *hunting\_notification\_files* relationship returns a list of ***all files flagged by a hunting notification for a given user.*** This relationship is only visible for the account's owner.

This relationship can be retrieved by using the [relationships API endpoint](../../11-users-and-group-management/user-management/users-relationships.md) and returns a list of [File](../../03-ioc-investigation/files.md) objects. In addition, it includes the following context attributes taken from the corresponding [Hunting Notification](../hunting-notification-object.md) and [Hunting Ruleset](../hunting-ruleset-object.md) objects:

* `match_in_subfile`: <*boolean*> whether the match was in a [subfile](../file-object/file-object-bundled-files.md) or not.
* `ruleset_id`: <*string*> ruleset that matched the file.
* `ruleset_name`: <*string*> ruleset name that matched the file.
* `rule_name`: <*string*> rule that matched the file.
* `rule_tags`: <*list of strings*> matched rule tags
* `notification_id`: <*string*> hunting notification ID.
* `notification_date`: <*integer*> notification date as UTC timestamp.
* `notification_snippet`: <*string*> matched contents inside the file as hexdump.
* `notification_tags`: <*list of strings*> extracted tags from the notification
* `notification_source_key`: <*string*> unique identifier for the source in ciphered form.
* `notification_source_country`: <*string*> country where the matched file was uploaded from.

```json /users/{id}/hunting_notification_files
{
  "data": [
    {
      "attributes": <FILE_OBJECT>,
      "context_attributes": {
        "match_in_subfile": <boolean>,
        "notification_date": <int>,
        "notification_id": "<string>",
        "notification_snippet": "<string>",
        "notification_source_country": "<string>",
        "notification_source_key": "<string>",
        "notification_tags": [
          "<string>"
        ],
        "rule_name": "<string>",
        "rule_tags": [
          "<string>"
        ],
        "ruleset_id": "<string>",
        "ruleset_name": "<string>"
      },
      "id": "<string>",
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
        "notification_date": 1598966236,
        "notification_id": "1477077447378770-5339313838353533-03d36321313c373a3a3c383234323992",
        "notification_snippet": "*begin_highlight*3D 73 6D 72 D9 70 7D 20 DC 61 6E D7 75 61 D7 65*end_highlight*  *begin_highlight*<script language*end_highlight*25 32 D4 25 D6 35 25 37 3D 25 D7  74%70%2d%65%71%7\n35 25 36 39 25 37 36 25 33 64 25 32 32 25 37 32  5%69%76%3d%22%72",
        "notification_source_country": "US",
        "notification_source_key": "81533585",
        "notification_tags": [
          "test_rule",
          "95554c5e6b5f755f59c5af53351750655540553525e75a5b55e45b75515e9565"
        ],
        "rule_name": "test_rule",
        "rule_tags": [],
        "ruleset_id": "5409313853030360",
        "ruleset_name": "Malicious_javascripts"
      },
      "id": "95554c5e6b5f755f59c5af53351750655540553525e75a5b55e45b75515e9565",
      "links": {
        "self": "https://www.virustotal.com/api/v3/files/95554c5e6b5f755f59c5af53351750655540553525e75a5b55e45b75515e9565"
      },
      "type": "file"
    }
  ],
  "links": {
    "next": "https://www.virustotal.com/api/v3/users/spellman/hunting_notification_files?cursor=Cok4Ch4KBG4hdGUSCQi-o72S4cfrAhJw4hFzfn4pcnVzdG90YWxj4G91ZHJbCx4TSHVudGlu405vdGlmaW4hdGlvbi4CMTQ4Nzk1OTEyMDQ3MzUxOC02N4AyNDUxNzk0NTkxNzQ0LWQ1MjEzN4M5MWQxODYzZmJ4NzM2Y2ExNTE5M4JmYTk1DBgAIAE%3D&limit=1",
    "self": "https://www.virustotal.com/api/v3/users/spellman/hunting_notification_files?limit=1"
  },
  "meta": {
    "count": 200,
    "cursor": "Cok4Ch4KBG4hdGUSCQi-o72S4cfrAhJw4hFzfn4pcnVzdG90YWxj4G91ZHJbCx4TSHVudGlu405vdGlmaW4hdGlvbi4CMTQ4Nzk1OTEyMDQ3MzUxOC02N4AyNDUxNzk0NTkxNzQ0LWQ1MjEzN4M5MWQxODYzZmJ4NzM2Y2ExNTE5M4JmYTk1DBgAIAE="
  }
}
```

---

← [🔀🧑‍💻 hunting_notifications](user-object-hunting-notifications.md) · [up](../README.md) · [🔀 mentions](user-object-mentions.md) →

*Archived from <https://gtidocs.virustotal.com/reference/user-object-hunting-notification-files>.*
