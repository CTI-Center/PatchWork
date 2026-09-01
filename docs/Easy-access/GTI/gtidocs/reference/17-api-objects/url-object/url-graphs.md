---
title: "🔀 graphs"
source: https://gtidocs.virustotal.com/reference/url-graphs
slug: url-graphs
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T01:06:57.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [URLs](../url-object.md) › 🔀 graphs

---

# 🔀-graphs

The *graphs* relationship returns a list of **graphs containing the given URL**.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/urls/urls-relationships.md). The response contains a list of [Graph](../graph-object.md) objects.

```json /urls/{url_id}/graphs
{
  "data": [
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
        "self": "https://www.virustotal.com/api/v3/urls/ea16d95de77b7eb0d91ebadb0e4503ef7cdebec9ee655eec8e834305ebf5ecd8/graphs?limit=10"
    },
    "meta": {
        "count": 1
    }
}
```

---

← [🔀 downloaded_files](url-downloaded_files.md) · [up](../README.md) · [🔀 last_serving_ip_address](url-last_serving_ip_address.md) →

*Archived from <https://gtidocs.virustotal.com/reference/url-graphs>.*
