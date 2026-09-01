---
title: "🔀🧑‍💻 user_votes"
source: https://gtidocs.virustotal.com/reference/file-object-user-votes
slug: file-object-user-votes
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:42:17.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › 🔀🧑‍💻 user_votes

---

# 🔀🧑‍💻-user_votes

Votes for a given file made by the current user

The *votes* relationship returns a list ***containing the votes for a given file made by the current user***.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/files/files-relationships.md). The response contains a list of [Vote](../vote-object.md) objects.

```json /files/{file_hash}/user_votes
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
        "date": 1592125710,
        "verdict": "harmless",
        "value": 1
      },
      "type": "vote",
      "id": "f-87083882cc6015984eb0411a99d3981817f5dc5c90ba24f0940420c5548d82de-726b4272",
      "links": {
        "self": "https://www.virustotal.com/api/v3/votes/f-87083882cc6015984eb0411a99d3981817f5dc5c90ba24f0940420c5548d82de-726b4272"
      }
    }
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/files/87083882cc6015984eb0411a99d3981817f5dc5c90ba24f0940420c5548d82de/user_votes"
  }
}
```

---

← [lnk_info](file-object-lnk-info.md) · [up](../README.md) · [popular_threat_classification](file-object-popular-threat-classification.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-user-votes>.*
