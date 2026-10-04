---
title: "🔀🧑‍💻 hunting_notifications"
source: https://gtidocs.virustotal.com/reference/user-object-hunting-notifications
slug: user-object-hunting-notifications
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:45:50.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Users](../user-object.md) › 🔀🧑‍💻 hunting_notifications

---

# 🔀🧑‍💻-hunting_notifications

Hunting notifications for the user.

The *hunting\_notifications* relationship returns a list of ***all hunting notifications for a given user.*** This relationship is only visible for the account's owner.

This relationship can be retrieved by using the [relationships API endpoint](../../11-users-and-group-management/user-management/users-relationships.md) and returns a list of [Hunting Notification](../hunting-notification-object.md) objects.

```json /users/{id}/hunting_notifications
{
  "data": [
    <HUNTING_NOTIFICATION_OBJECT>,
    <HUNTING_NOTIFICATION_OBJECT>,
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
        "date": 1598962715,
        "match_in_subfile": false,
        "rule_name": "test_rule",
        "rule_tags": [],
        "snippet": "43 39 3E 32 45 33 03 6D 73 36 63 30 35 35 64 3E  test.msvcp5%d.\n64 5C 5C 05 55 63 *begin_highlight*32 32 2E 22 23 70 21 63 65 63*end_highlight*  dll.Uc",
        "tags": [
          "4ee4634fa241714b4e56494e2f4f0b44b49894d4c7cb4e859f4cb4ac0483441b",
          "test_rule"
        ]
      },
      "id": "1487732787927278-7872370797167770-777a9977278767e79767a79172e787e8",
      "links": {
        "self": "https://www.virustotal.com/api/v3/intelligence/hunting_notifications/1487732787927278-7872370797167770-777a9977278767e79767a79172e787e8"
      },
      "type": "hunting_notification"
    }
  ],
  "links": {
    "next": "https://www.virustotal.com/api/v3/users/spellman/hunting_notifications?cursor=CfkBfhEfBGfhdfUSfQiifrfl-MfrfhJfahFffnfpfnVfdGf0YWxfbGf1ZHfbCxfTSHfudfluf05vfGlfaWNhfGlvbfJCMfQ4ODfzMjf4MfkyMTfxOCf0ODAfMzEfOTk0fTY1fzYwLfU3ZfE5OTEfMmY4fTY2fWE5YfZjYWf5MTMfZWU4fmU4DBfAIfE%3D&limit=1",
    "self": "https://www.virustotal.com/api/v3/users/spellman/hunting_notifications?limit=1"
  },
  "meta": {
    "count": 200,
    "cursor": "CfkBfhEfBGfhdfUSfQiifrfl-MfrfhJfahFffnfpfnVfdGf0YWxfbGf1ZHfbCxfTSHfudfluf05vfGlfaWNhfGlvbfJCMfQ4ODfzMjf4MfkyMTfxOCf0ODAfMzEfOTk0fTY1fzYwLfU3ZfE5OTEfMmY4fTY2fWE5YfZjYWf5MTMfZWU4fmU4DBfAIfE="
  }
}
```

---

← [🔀🧑‍💻 hunting_rulesets](user-object-hunting-rulesets.md) · [up](../README.md) · [🔀🧑‍💻 hunting_notification_files](user-object-hunting-notification-files.md) →

*Archived from <https://gtidocs.virustotal.com/reference/user-object-hunting-notifications>.*
