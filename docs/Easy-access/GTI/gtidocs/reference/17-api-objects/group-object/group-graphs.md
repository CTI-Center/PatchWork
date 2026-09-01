---
title: "🔀🧑‍💻 graphs"
source: https://gtidocs.virustotal.com/reference/group-graphs
slug: group-graphs
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T01:05:12.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Groups](../group-object.md) › 🔀🧑‍💻 graphs

---

# 🔀🧑‍💻-graphs

VT Graphs the group is owner/editor/viewer of.

The *graphs* relationship returns all ***graphs a given group has access to***. This relationship is only visible for the groups members.

It can be fetched using the [relationships API endpoint](../../11-users-and-group-management/group-management/groups-relationships.md) and it returns a list of [Graph](../graph-object.md) objects.

```json /groups/{id}/graphs
{
  "data": [
    <GRAPH_OBJECT>,
    <GRAPH_OBJECT>,
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
                "comments_count": 0,
                "creation_date": 1588969624,
                "graph_data": {
                    "description": "demo",
                    "version": "5.0.0"
                },
                "last_modified_date": 1588969632,
                "links": [
                    {
                        "connection_type": "itw_urls",
                        "source": "467e3e24d9ee6b87decea6c635ef4fef5ecbc0d3ee7a43ef6cbe205e4e00befd",
                        "target": "relationships_itw_urls_467e3e24d9ee6b87decea6c635ef4fef5ecbc0d3ee7a43ef6cbe205e4e00befd"
                    },
                    {
                        "connection_type": "itw_urls",
                        "source": "relationships_itw_urls_467e3e24d9ee6b87decea6c635ef4fef5ecbc0d3ee7a43ef6cbe205e4e00befd",
                        "target": "ea16e95d87eb70b0e914badbe7450e8f7cd1bec97e655aee8c8343e59bf56cde"
                    },
                    {
                        "connection_type": "itw_urls",
                        "source": "relationships_itw_urls_467e3e24d9ee6b87decea6c635ef4fef5ecbc0d3ee7a43ef6cbe205e4e00befd",
                        "target": "ea16e95d87eb70b0e914badbe7450e8f7cd1bec97e655aee8c8343e59bf56cde"
                    }
                ],
                "nodes": [
                    {
                        "entity_attributes": {
                            "has_detections": true,
                            "type_tag": "peexe"
                        },
                        "entity_id": "467e3e24d9ee6b87decea6c635ef4fef5ecbc0d3ee7a43ef6cbe205e4e00befd",
                        "index": 0,
                        "text": "467e3e24d9ee6b87dece...",
                        "type": "file",
                        "x": 94.88241748841389,
                        "y": 327.76366686430765
                    },
                    {
                        "entity_attributes": {},
                        "entity_id": "relationships_itw_urls_467e3e24d9ee6b87decea6c635ef4fef5ecbc0d3ee7a43ef6cbe205e4e00befd",
                        "index": 1,
                        "text": "",
                        "type": "relationship",
                        "x": 142.92298071493295,
                        "y": 397.8464815957372
                    },
                    {
                        "entity_attributes": {
                            "has_detections": true
                        },
                        "entity_id": "ea16e95d87eb70b0e914badbe7450e8f7cd1bec97e655aee8c8343e59bf56cde",
                        "index": 2,
                        "text": "",
                        "type": "url",
                        "x": 133.3581112394535,
                        "y": 438.52755880543987
                    },
                    {
                        "entity_attributes": {
                            "has_detections": true
                        },
                        "entity_id": "53f28ee8a9f78e6870b9a78ba6065652259ffe984d38ea256e8beb47cf8997ae",
                        "index": 3,
                        "text": "",
                        "type": "url",
                        "x": 184.8662498984155,
                        "y": 397.76440630912066
                    }
                ],
                "views_count": 1
            },
            "id": "ge312b9e4a9534ec09c3e99b08ef139ef060eb0fe0d6e474eb19e22f3e6de362e",
            "links": {
                "self": "https://www.virustotal.com/api/v3/graphs/ge312b9e4a9534ec09c3e99b08ef139ef060eb0fe0d6e474eb19e22f3e6de362e"
            },
            "type": "graph"
        }
    ],
    "links": {
        "self": "https://www.virustotal.com/api/v3/groups/spellmans/graphs?limit=10"
    },
    "meta": {
        "count": 1
    }
}
```

---

← [🔀🧑‍💻 administrators](group-administrators.md) · [up](../README.md) · [🔀🧑‍💻 users](group-users.md) →

*Archived from <https://gtidocs.virustotal.com/reference/group-graphs>.*
