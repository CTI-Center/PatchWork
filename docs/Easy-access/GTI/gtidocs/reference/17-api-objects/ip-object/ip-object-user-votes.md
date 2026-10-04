---
title: "🔀🧑‍💻 user_votes"
source: https://gtidocs.virustotal.com/reference/ip-object-user-votes
slug: ip-object-user-votes
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:43:40.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [IP addresses](../ip-object.md) › 🔀🧑‍💻 user_votes

---

# 🔀🧑‍💻-user_votes

IP address' user votes.

The *votes* relationship returns a list ***containing the votes for a given IP address made by the current user***.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/ip-addresses/ip-relationships.md). The response contains a list of [Vote](../vote-object.md) objects.

```json /ip_addresses/{ip_address}/user_votes
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
        "date": 1624368057,
        "verdict": "harmless",
        "value": 1
      },
      "type": "vote",
      "id": "i-8.8.8.8-2fa03e13",
      "links": {
        "self": "https://www.virustotal.com/api/v3/votes/i-8.8.8.8-2fa03e13"
      }
    }
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/ip_addresses/8.8.8.8/user_votes",
  }
}
```

---

← [🔀 votes](ip-object-votes.md) · [up](../README.md) · [🔀 collections](ip-object-collections.md) →

*Archived from <https://gtidocs.virustotal.com/reference/ip-object-user-votes>.*
