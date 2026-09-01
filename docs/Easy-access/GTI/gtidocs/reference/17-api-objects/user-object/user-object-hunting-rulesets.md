---
title: "🔀🧑‍💻 hunting_rulesets"
source: https://gtidocs.virustotal.com/reference/user-object-hunting-rulesets
slug: user-object-hunting-rulesets
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:45:49.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Users](../user-object.md) › 🔀🧑‍💻 hunting_rulesets

---

# 🔀🧑‍💻-hunting_rulesets

Hunting rulesets editable by the user.

The *hunting\_rulesets* relationship returns a list of ***all hunting rulesets editable by a given user***. This relationship is only visible for the account's owner.

This relationship can be retrieved by using the [relationships API endpoint](../../11-users-and-group-management/user-management/users-relationships.md) and it returns a list of [Hunting Rulesets](../hunting-ruleset-object.md) objects.

```json /users/{id}/hunting_rulesets
{
  "data": [
    <HUNTING_RULESET_OBJECT>,
    <HUNTING_RULESET_OBJECT>,
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
        "creation_date": 1594997826,
        "enabled": false,
        "limit": 100,
        "modification_date": 1597394885,
        "name": "test",
        "notification_emails": [],
        "number_of_rules": 1,
        "rule_names": [
          "yara_template"
        ],
        "rules": "/*\n    Template YARA ruleset\n*/\nrule yara_template\n{\n    strings:\n        $a = \"VirusTotal\"\n    condition:\n        all of them\n}"
      },
      "id": "0000000000000000",
      "links": {
        "self": "https://www.virustotal.com/api/v3/intelligence/hunting_rulesets/0000000000000000"
      },
      "type": "hunting_ruleset"
    }
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/users/spellman/hunting_rulesets?limit=10"
  },
  "meta": {
    "count": 1
  }
}
```

---

← [🔀🧑‍💻 groups](user-object-groups.md) · [up](../README.md) · [🔀🧑‍💻 hunting_notifications](user-object-hunting-notifications.md) →

*Archived from <https://gtidocs.virustotal.com/reference/user-object-hunting-rulesets>.*
