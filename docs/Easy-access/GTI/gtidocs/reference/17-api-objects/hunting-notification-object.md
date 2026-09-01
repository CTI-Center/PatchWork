---
title: "Hunting Notifications"
source: https://gtidocs.virustotal.com/reference/hunting-notification-object
slug: hunting-notification-object
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:43:23.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Hunting Notifications

---

# hunting-notifications

Generated notifications by matches in Hunting Rulesets

> ❗️ Important
>
> This object is no longer used by the web interface. Use [IoC-Stream Notifications](ioc-stream-notifications-object.md) instead.

A Hunting Notification object represents a notification generated when one of the YARA rules in a [Hunting Ruleset](hunting-ruleset-object.md) matches a file sent to Google Threat Intelligence. This object is only visible for the Hunting Ruleset's owner and any user the ruleset was shared with.

The object contains the following attributes:

* `date`: <*integer*> notification date as UTC timestamp.
* `match_in_subfile`: <*boolean*> whether the match was in a [subfile](file-object/file-object-bundled-files.md) or not.
* `rule_name`: <*string*> matched rule name.
* `rule_tags`: <*list of strings*> matched rule tags.
* `snippet`: <*string*> matched contents inside the file as hexdump. Contains `begin_highlight` and `end_highlight` substrings to indicate the part of the file that produced the match and give additional context about surrounding bytes in the match.
* `source_country`: <*string*> country where the matched file was uploaded from.
* `source_key`: <*string*> unique identifier for the source in ciphered form.
* `tags`: <*list of strings*> notification tags.

```json Hunting Notification object
{
  "data": {
    "attributes": {
      "date": <int>,
      "match_in_subfile": <bool>,
      "rule_name": "<string>",
      "rule_tags": [
        "<string>"
      ],
      "snippet": "<string>",
      "source_country": "<string>",
      "source_key": "<string>",
      "tags": [
        "<string>"
      ]
    },
    "id": "<string>",
    "links": {
      "self": "https://www.virustotal.com/api/v3/intelligence/hunting_notifications/<id>"
    },
    "type": "hunting_notification"
  }
}
```
```json Example
{
  "data": {
    "attributes": {
      "date": 1598953067,
      "match_in_subfile": false,
      "rule_name": "test_rule",
      "rule_tags": [],
      "snippet": "*begin_highlight*3E 74 65 62 39 10 74 40 7C 6F 3E 37 55 11 37 65*end_highlight*  *begin_highlight*<script language*end_highlight*\n*begin_highlight*3D 22 6A 61",
      "source_country": "GB",
      "source_key": "433a7343",
      "tags": [
        "malicious_javascripts",
        "test_rule",
        "c4c4d4f94f4404f14724ff4af49c4ed44841241d42407486414ca47a484444bf"
      ]
    },
    "id": "1557531515556553-5505015558550565-5758652515e55555ba5cd5c555f5d952",
    "links": {
      "self": "https://www.virustotal.com/api/v3/intelligence/hunting_notifications/1557531515556553-5505015558550565-5758652515e55555ba5cd5c555f5d952"
    },
    "type": "hunting_notification"
  }
}
```

---

← [🔀🧑‍💻 users](group-object/group-users.md) · [up](README.md) · [Hunting Rulesets](hunting-ruleset-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/hunting-notification-object>.*
