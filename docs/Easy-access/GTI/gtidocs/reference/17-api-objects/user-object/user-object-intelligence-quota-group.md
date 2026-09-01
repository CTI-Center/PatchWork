---
title: "🔀🧑‍💻 intelligence_quota_group"
source: https://gtidocs.virustotal.com/reference/user-object-intelligence-quota-group
slug: user-object-intelligence-quota-group
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:45:55.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Users](../user-object.md) › 🔀🧑‍💻 intelligence_quota_group

---

# 🔀🧑‍💻-intelligence_quota_group

Group which the user consumes Intelligence quota from.

The *intelligence\_quota\_group* relationship returns ***the group which the user consumes Intelligence quota from.*** This relationship is only visible to the account's owner and their group's admin.

This relationship can be retrieved by using the [relationships API endpoint](../../11-users-and-group-management/user-management/users-relationships.md) and contains a [Group](../group-object.md) object.

```json /users/{user_id}/intelligence_quota_group
{
  "data": <GROUP_OBJECT>,
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
    "data": {
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
            "self": "https://www.virustotal.com/api/v3/groups/spellmans"
        },
        "type": "group"
    },
    "links": {
        "self": "https://www.virustotal.com/api/v3/users/spellman/intelligence_quota_group"
    },
    "meta": {
        "count": 1
    }
}
```

---

← [🔀🧑‍💻 api_quota_group](user-object-api-quota-group.md) · [up](../README.md) · [🔀 collections](user-object-collections.md) →

*Archived from <https://gtidocs.virustotal.com/reference/user-object-intelligence-quota-group>.*
