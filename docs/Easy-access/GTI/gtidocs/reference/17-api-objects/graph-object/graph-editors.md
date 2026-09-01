---
title: "🔀 editors"
source: https://gtidocs.virustotal.com/reference/graph-editors
slug: graph-editors
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T01:05:05.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Graphs](../graph-object.md) › 🔀 editors

---

# 🔀-editors

Users that can edit a graph

The *editors* relationship returns all ***users and groups that can edit a given graph***.

It can be fetched using the [relationships API endpoint](../../10-threat-graph/threat-graphs/graphs-relationships.md) and it returns a list of [User](../user-object.md) and [Group](../group-object.md) objects.

```json /graphs/{id}/editors
{
  "data": [
    <GROUP_OBJECT>,
    <USER_OBJECT>,
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
                "auto_add_users": [],
                "country": "United States",
                "country_iso": "US",
                "domain_name": "blabla.com",
                "industry": "IT",
                "organization": "Company",
                "organization_legal_name": "Company Inc",
                "privileges": {
                    "admin": {
                        "granted": false
                    },
                    "allinfo": {
                        "granted": false
                    },
                    "big-files": {
                        "expiration_date": 1601510400,
                        "granted": true
                    },
                    "cases": {
                        "granted": false
                    },
                    "click_to_accept": {
                        "granted": false
                    }
                },
                "quota_usage_by_user": {},
                "quotas": {
                    "api_requests_daily": {
                        "allowed": 1000,
                        "used": 13
                    },
                    "api_requests_hourly": {
                        "allowed": 60000,
                        "used": 1
                    },
                    "api_requests_monthly": {
                        "allowed": 30000,
                        "used": 104
                    }
                }
            },
            "id": "blabla",
            "links": {
                "self": "https://www.virustotal.com/api/v3/groups/blabla"
            },
            "type": "group"
        },
    ],
    "links": {
        "self": "https://www.virustotal.com/api/v3/graphs/g0538d03053194c338643183e315b134ec3463a392330430938033934f3be3f37/editors?limit=10"
    },
    "meta": {
        "count": 1
    }
}
```

---

← [🔀 comments](graph-comments.md) · [up](../README.md) · [🔀 group](graph-group.md) →

*Archived from <https://gtidocs.virustotal.com/reference/graph-editors>.*
