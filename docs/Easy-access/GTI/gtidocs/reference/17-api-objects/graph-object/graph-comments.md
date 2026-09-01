---
title: "🔀 comments"
source: https://gtidocs.virustotal.com/reference/graph-comments
slug: graph-comments
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T01:05:04.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Graphs](../graph-object.md) › 🔀 comments

---

# 🔀-comments

Comments in a graph

The *comments* relationship lists all comments posted by the VirusTotal community for a given Graph.

This relationship can be retrieved using the [relationships API endpoint](../../10-threat-graph/threat-graphs/graphs-relationships.md). The response contains a list of [Comments](../comment-object.md) objects.

```json /graphs/{id}/comments
{
  "data": [
    <COMMENT_OBJECT>,
    <COMMENT_OBJECT>,
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
        "date": 1559094923,
        "html": "such malicious very malware <br />",
        "tags": [
          "_:api",
          "_:public"
        ],
        "text": "such malicious very malware \n",
        "votes": {
          "abuse": 0,
          "negative": 0,
          "positive": 0
        }
      },
      "id": "g-g0538d03053194c338643183e315b134ec3463a392330430938033934f3be3f37-4f424e4d",
      "links": {
        "self": "https://www.virustotal.com/api/v3/comments/g-g0538d03053194c338643183e315b134ec3463a392330430938033934f3be3f37-4f424e4d"
      },
      "type": "comment"
    }
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/graphs/g0538d03053194c338643183e315b134ec3463a392330430938033934f3be3f37/comments?limit=10"
  },
  "meta": {
    "count": 1
  }
}
```

---

← [Graphs](../graph-object.md) · [up](../README.md) · [🔀 editors](graph-editors.md) →

*Archived from <https://gtidocs.virustotal.com/reference/graph-comments>.*
