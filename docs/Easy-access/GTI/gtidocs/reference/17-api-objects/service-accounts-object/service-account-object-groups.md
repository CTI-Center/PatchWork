---
title: "🔀🧑‍💻 groups"
source: https://gtidocs.virustotal.com/reference/service-account-object-groups
slug: service-account-object-groups
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:44:39.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Service Accounts](../service-accounts-object.md) › 🔀🧑‍💻 groups

---

# 🔀🧑‍💻-groups

Groups for which the user is a member.

The *groups* relationship returns a list of ***all groups for which a given Service Account is a member***. This relationship is only visible for the group's admins.

The relationship can be retrieved by using the [relationships API endpoint](../../11-users-and-group-management/user-management/users-relationships.md) and its response contains a list of [Groups](../group-object.md) objects.

```json /users/{user_id}/groups
{
  "data": [
    <GROUP_OBJECT>,
    <GROUP_OBJECT>,
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
        }
    ],
    "links": {
        "self": "https://www.virustotal.com/api/v3/users/spellman/groups?limit=10"
    },
    "meta": {
        "count": 1
    }
}
```

---

← [🔀 comments](service-account-object-comments.md) · [up](../README.md) · [🔀🧑‍💻 intelligence_quota_group](service-account-object-intelligence-quota-group.md) →

*Archived from <https://gtidocs.virustotal.com/reference/service-account-object-groups>.*
