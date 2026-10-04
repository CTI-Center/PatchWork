---
title: "🔀🧑‍💻 user_votes"
source: https://gtidocs.virustotal.com/reference/domains-object-user_votes
slug: domains-object-user_votes
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T01:02:37.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Domains](../domains-object.md) › 🔀🧑‍💻 user_votes

---

# 🔀🧑‍💻-user_votes

Domain's user votes.

The *votes* relationship returns a list ***containing the votes for a given domain made by the current user***.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/domains-resolutions/domains-relationships.md). The response contains a list of [Vote](../vote-object.md) objects.

```json /domains/{domain}/user_votes
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
    "count": 1
  },
  "data": [
    {
      "attributes": {
        "date": 1623254696,
        "verdict": "harmless",
        "value": 1
      },
      "type": "vote",
      "id": "d-www.virustotal.com-e6bc6708",
      "links": {
        "self": "https://www.virustotal.com/api/v3/votes/d-www.virustotal.com-e6bc6708"
      }
    }
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/domains/www.virustotal.com/user_votes"
  }
}
```

---

← [🔀 votes](domains-object-votes.md) · [up](../README.md) · [🔀 collections](domains-object-collections.md) →

*Archived from <https://gtidocs.virustotal.com/reference/domains-object-user_votes>.*
