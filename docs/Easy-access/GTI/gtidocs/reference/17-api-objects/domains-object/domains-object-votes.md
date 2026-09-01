---
title: "🔀 votes"
source: https://gtidocs.virustotal.com/reference/domains-object-votes
slug: domains-object-votes
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T01:02:36.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Domains](../domains-object.md) › 🔀 votes

---

# 🔀-votes

Domain's votes.

The *votes* relationship returns a list ***containing the votes for a given domain***.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/domains-resolutions/domains-relationships.md). The response contains a list of [Vote](../vote-object.md) objects.

```json /domains/{domain}/votes
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
    "count": 42,
    "cursor": "CmkKEQoEZGF0ZRIJCNPCz-7cpPACElBqEXN-dmlydXN0b3RhbGNsb3VkcjsLEgZEb21haW4iDnd3dy5nb29nbGUuY29tDAsSBFZvdGUiF3d3dy5nb29nbGUuY29tLTQzNTIyOTkzDBgAIAE="
  },
  "data": [
    {
      "attributes": {
        "date": 1624137540,
        "verdict": "malicious",
        "value": -1
      },
      "type": "vote",
      "id": "d-www.google.com-5c711e45",
      "links": {
        "self": "https://www.virustotal.com/api/v3/votes/d-www.google.com-5c711e45"
      }
    },
    {
      "attributes": {
        "date": 1619742994,
        "verdict": "harmless",
        "value": 1
      },
      "type": "vote",
      "id": "d-www.google.com-43522993",
      "links": {
        "self": "https://www.virustotal.com/api/v3/votes/d-www.google.com-43522993"
      }
    }
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/domains/www.google.com/votes?limit=2",
    "next": "https://www.virustotal.com/api/v3/domains/www.google.com/votes?cursor=CmkKEQoEZGF0ZRIJCNPCz-7cpPACElBqEXN-dmlydXN0b3RhbGNsb3VkcjsLEgZEb21haW4iDnd3dy5nb29nbGUuY29tDAsSBFZvdGUiF3d3dy5nb29nbGUuY29tLTQzNTIyOTkzDBgAIAE%3D&limit=2"
  }
}
```

---

← [🔀 soa_records](soa_records.md) · [up](../README.md) · [🔀🧑‍💻 user_votes](domains-object-user_votes.md) →

*Archived from <https://gtidocs.virustotal.com/reference/domains-object-votes>.*
