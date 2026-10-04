---
title: "🔀 votes"
source: https://gtidocs.virustotal.com/reference/ip-object-votes
slug: ip-object-votes
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T01:05:51.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [IP addresses](../ip-object.md) › 🔀 votes

---

# 🔀-votes

IP address' votes.

The *votes* relationship returns a list ***containing the votes for a given IP address***.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/ip-addresses/ip-relationships.md). The response contains a list of [Vote](../vote-object.md) objects.

```json /ip_addresses/{ip_address}/votes
{
  "data": [
  	<VOTE_OBJECT>,
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
    "count": 66,
    "cursor": "Cl4KEQoEZGF0ZRIJCPy8qrv4qvECEkVqEXN-dmlydXN0b3RhbGNsb3VkcjALEglJcEFkZHJlc3MiBzguOC44LjgMCxIEVm90ZSIQOC44LjguOC02YjY5OTk3NQwYACAB"
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
    },
    {
      "attributes": {
        "date": 1624354608,
        "verdict": "harmless",
        "value": 1
      },
      "type": "vote",
      "id": "i-8.8.8.8-6b699975",
      "links": {
        "self": "https://www.virustotal.com/api/v3/votes/i-8.8.8.8-6b699975"
      }
    }
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/ip_addresses/8.8.8.8/votes?limit=2",
    "next": "https://www.virustotal.com/api/v3/ip_addresses/8.8.8.8/votes?cursor=Cl4KEQoEZGF0ZRIJCPy8qrv4qvECEkVqEXN-dmlydXN0b3RhbGNsb3VkcjALEglJcEFkZHJlc3MiBzguOC44LjgMCxIEVm90ZSIQOC44LjguOC02YjY5OTk3NQwYACAB&limit=2"
  }
}
```

---

← [🔀 related_comments](ip-object-related-comments.md) · [up](../README.md) · [🔀🧑‍💻 user_votes](ip-object-user-votes.md) →

*Archived from <https://gtidocs.virustotal.com/reference/ip-object-votes>.*
