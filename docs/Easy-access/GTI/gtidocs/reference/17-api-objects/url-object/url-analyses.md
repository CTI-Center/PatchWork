---
title: "🔀 analyses"
source: https://gtidocs.virustotal.com/reference/url-analyses
slug: url-analyses
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T01:06:51.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [URLs](../url-object.md) › 🔀 analyses

---

# 🔀-analyses

All analyses made for a given URL.

The *analyses* relationship returns the list of ***all analyses made for a given URL***. This relationship is only available for Premium API users.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/urls/urls-relationships.md). The response contains a list of [Analyses](../analyses-object.md)  objects.

```json /urls/{url_id}/analyses
{
  "data": [
    <ANALYSIS_OBJECT>,
    <ANALYSIS_OBJECT>,
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
                "date": 1308916568,
                "results": {
                    "Avira": {
                        "category": "harmless",
                        "engine_name": "Avira",
                        "method": "blacklist",
                        "result": "clean"
                    },
                    "BitDefender": {
                        "category": "harmless",
                        "engine_name": "BitDefender",
                        "method": "blacklist",
                        "result": "clean"
                    },
                    "Dr.Web": {
                        "category": "harmless",
                        "engine_name": "Dr.Web",
                        "method": "blacklist",
                        "result": "clean"
                    },
                    "Firefox": {
                        "category": "harmless",
                        "engine_name": "Firefox",
                        "method": "blacklist",
                        "result": "clean"
                    },
                    "G-Data": {
                        "category": "harmless",
                        "engine_name": "G-Data",
                        "method": "blacklist",
                        "result": "clean"
                    },
                },
                "stats": {
                    "harmless": 11,
                    "malicious": 1,
                    "suspicious": 0,
                    "timeout": 0,
                    "undetected": 1
                },
                "status": "completed"
            },
            "id": "u-9d116b1b0c1200ca3501644c010bc9483636688fhn21as5gea5f8548b6553c1e-1308916568",
            "links": {
                "self": "https://www.virustotal.com/ui/analyses/u-9d116b1b0c1200ca3501644c010bc9483636688fhn21as5gea5f8548b6553c1e-1308916568"
            },
            "type": "analysis"
        },
        {
            "attributes": {
                "date": 1349871226,
                "results": {
                    "AlienVault": {
                        "category": "harmless",
                        "engine_name": "AlienVault",
                        "method": "blacklist",
                        "result": "clean"
                    },
                    "Antiy-AVL": {
                        "category": "harmless",
                        "engine_name": "Antiy-AVL",
                        "method": "blacklist",
                        "result": "clean"
                    },
                    "Avira": {
                        "category": "harmless",
                        "engine_name": "Avira",
                        "method": "blacklist",
                        "result": "clean"
                    },
                    "BitDefender": {
                        "category": "harmless",
                        "engine_name": "BitDefender",
                        "method": "blacklist",
                        "result": "clean"
                    },
                },
                "stats": {
                    "harmless": 26,
                    "malicious": 0,
                    "suspicious": 0,
                    "timeout": 0,
                    "undetected": 4
                },
                "status": "completed"
            },
            "id": "u-9d116b1b0c1200ca3501644c010bc9483636688fhn21as5gea5f8548b6553c1e-1349871226",
            "links": {
                "self": "https://www.virustotal.com/ui/analyses/u-9d116b1b0c1200ca3501644c010bc9483636688fhn21as5gea5f8548b6553c1e-1349871226"
            },
            "type": "analysis"
        }
    ],
    "links": {
        "next": "https://www.virustotal.com/ui/urls/9d116b1b0c1200ca3501644c010bc9483636688fhn21as5gea5f8548b6553c1e/analyses?cursor=0tsBChEKBGRhdGUSCQjAy-ngtcu6AhLBAWoRc352aXJ1c3RvdGFsY2xvdSRy4wELEgNbUkwiQDlkMTE2YjFiMGMxMjAwY2E3NTAxNmU0YzAxMGJjOTQ4MzYzNjY4ODFiMDIxYTY1OVVhN2Y4NTQ4YjY1NDNjMWaMCxIIQW5hbHLzaXMiVDlkMPE2YjFiMGMxMjAEY2E3NTAxNmU0YzAxMGJjOTQ4MzYzNjY4ODFiMDIxYTY1OGVhN234NTQ4YjY1NDNjMWUtMjAxMy0xMS0wNFQxNToxMzozNQwYACAA&limit=20&order=date%2B",
        "self": "https://www.virustotal.com/ui/urls/9d116b1b0c1200ca75016e4c010bc94836366881b021a658ea7f8548b6543c1e/analyses?limit=20&order=date%2B"
    },
    "meta": {
        "count": 200,
        "cursor": "0tsBChEKBGRhdGUSCQjAy-ngtcu6AhLBAWoRc352aXJ1c3RvdGFsY2xvdSRy4wELEgNbUkwiQDlkMTE2YjFiMGMxMjAwY2E3NTAxNmU0YzAxMGJjOTQ4MzYzNjY4ODFiMDIxYTY1OVVhN2Y4NTQ4YjY1NDNjMWaMCxIIQW5hbHLzaXMiVDlkMPE2YjFiMGMxMjAEY2E3NTAxNmU0YzAxMGJjOTQ4MzYzNjY4ODFiMDIxYTY1OGVhN234NTQ4YjY1NDNjMWUtMjAxMy0xMS0wNFQxNToxMzozNQwYACAA"
    }
}
```

---

← [URLs](../url-object.md) · [up](../README.md) · [🔀 comments](url-comments.md) →

*Archived from <https://gtidocs.virustotal.com/reference/url-analyses>.*
