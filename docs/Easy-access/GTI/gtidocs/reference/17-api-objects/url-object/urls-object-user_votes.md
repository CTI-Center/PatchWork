---
title: "🔀🧑‍💻 user_votes"
source: https://gtidocs.virustotal.com/reference/urls-object-user_votes
slug: urls-object-user_votes
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T01:07:09.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [URLs](../url-object.md) › 🔀🧑‍💻 user_votes

---

# 🔀🧑‍💻-user_votes

Votes for a given URL made by the current user

The *votes* relationship returns a list ***containing the votes for a given URL made by the current user***.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/urls/urls-relationships.md). The response contains a list of [Vote](../vote-object.md) objects.

```json /urls/{url_id}/user_votes
{
  "data": [
  	<VOTE_OBJECT>
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
  "meta": {
    "count": 1,
  },
  "data": [
    {
      "attributes": {
        "date": 1624356005,
        "verdict": "harmless",
        "value": 1
      },
      "type": "vote",
      "id": "u-d0e196a0c25d35dd0a84593cbae0f38333aa58529936444ea26453eab28dfc86-b6f95068",
      "links": {
        "self": "https://www.virustotal.com/api/v3/votes/u-d0e196a0c25d35dd0a84593cbae0f38333aa58529936444ea26453eab28dfc86-b6f95068"
      }
    }
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/urls/d0e196a0c25d35dd0a84593cbae0f38333aa58529936444ea26453eab28dfc86/user_votes"
  }
}
```

---

← [🔀 votes](votes.md) · [up](../README.md) · [🔀 collections](urls-object-collections.md) →

*Archived from <https://gtidocs.virustotal.com/reference/urls-object-user_votes>.*
