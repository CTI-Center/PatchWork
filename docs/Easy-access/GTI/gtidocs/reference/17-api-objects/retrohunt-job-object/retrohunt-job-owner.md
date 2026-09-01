---
title: "🔀🧑‍💻 owner"
source: https://gtidocs.virustotal.com/reference/retrohunt-job-owner
slug: retrohunt-job-owner
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T01:06:26.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Retrohunt Jobs](../retrohunt-job-object.md) › 🔀🧑‍💻 owner

---

# 🔀🧑‍💻-owner

Retrohunt job's owner

The *owner* relationship returns ***a Retrohunt job's owner***. This relationship is only visible for the account's owner.

This relationship can be retrieved by using the relationships API endpoint and returns an [User](../user-object.md) object.

```json /intelligence/retrohunt_jobs/{id}/owner
{
  "data": {
    <USER_OBJECT>
  },
  "links": {
    "self": "<string>"
  },
  "meta": {
    "count": 1
  }
}
```
```json Example
{
  "data": {
    "attributes": {
      "apikey": "3333333t33333333333333r333333f333333g33333333c3333333f333333333a",
      "email": "blabla@blabla.com",
      "first_name": "Sabrina",
      "has_2fa": true,
      "last_login": 1594718163,
      "last_name": "Spellman",
      "preferences": {
        "graph": {
          "dashboard_walkthrough_version_seen": "1.0.0",
          "last_visit": 1594136453392,
          "main_walkthrough_version_seen": "1.0.0",
          "search_tooltip_version_seen": "1.0.0"
        },
        "ui": {
          "last_read_notification_date": 1594640566
        }
      },
      "privileges": {
        "admin": {
          "granted": false
        },
        "allinfo": {
          "granted": false
        },
        "big-files": {
          "expiration_date": 1601510400,
          "granted": true,
          "inherited_from": "blablabla_group",
          "inherited_via": "api_quota_group"
        },
        "cases": {
          "granted": true,
          "inherited_from": "blablabla_group",
          "inherited_via": "intelligence_quota_group"
        },
        "click_to_accept": {
          "granted": false
        }
      },
      "profile_phrase": "It's witching hour!",
      "quotas": {
        "api_requests_daily": {
          "allowed": 1000000000,
          "used": 4
        },
        "api_requests_hourly": {
          "allowed": 60000000000,
          "used": 4
        },
        "api_requests_monthly": {
          "allowed": 1000000000,
          "used": 113
        },
        "cases_creation_monthly": {
          "allowed": 20,
          "used": 0
        },
        "intelligence_downloads_monthly": {
          "allowed": 0,
          "used": 0
        }
      },
      "reputation": 1,
      "status": "active",
      "user_since": 1557214525
    },
    "id": "spellman",
    "links": {
      "self": "https://www.virustotal.com/api/v3/users/spellman"
    },
    "type": "user"
  },
  "links": {
    "self": "https://www.virustotal.com/api/v3/intelligence/retrohunt_jobs/spellman-1598966772/owner"
  },
  "meta": {
    "count": 1
  }
}
```

---

← [🔀🧑‍💻 matching_files](retrohunt-job-matching-files.md) · [up](../README.md) · [Resolutions](../resolution-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/retrohunt-job-owner>.*
