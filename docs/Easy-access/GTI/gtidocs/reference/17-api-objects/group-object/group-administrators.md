---
title: "🔀🧑‍💻 administrators"
source: https://gtidocs.virustotal.com/reference/group-administrators
slug: group-administrators
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T01:05:11.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Groups](../group-object.md) › 🔀🧑‍💻 administrators

---

# 🔀🧑‍💻-administrators

Users administrating the group

The *administrators* relationship returns all ***users administrating a given group***. This relationship is only visible for the groups members.

It can be fetched using the [relationships API endpoint](../../11-users-and-group-management/group-management/groups-relationships.md) and it returns a list of [User](../user-object.md) objects.

```json /groups/{id}/administrators
{
  "data": [
    <USER_OBJECT>,
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
        "first_name": "Salem",
        "last_name": "Spellman",
        "profile_phrase": "Meow",
        "reputation": 1,
        "status": "active",
        "user_since": 1557214525
      },
      "id": "salem",
      "links": {
        "self": "https://www.virustotal.com/api/v3/users/salem"
      },
      "type": "user"
    }
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/groups/spellmans/administrators?limit=10"
  },
  "meta": {
    "count": 1
  }
}
```

---

← [Groups](../group-object.md) · [up](../README.md) · [🔀🧑‍💻 graphs](group-graphs.md) →

*Archived from <https://gtidocs.virustotal.com/reference/group-administrators>.*
