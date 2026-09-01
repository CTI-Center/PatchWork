---
title: "Service Accounts"
source: https://gtidocs.virustotal.com/reference/service-accounts-object
slug: service-accounts-object
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:44:37.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Service Accounts

---

# service-accounts

Information about a Google Threat Intelligence Service Account

## object-attributes

* `apikey`: <*string*> Service Account's Google Threat Intelligence API key. Only visible for the administrators of the group the Service Account belongs to.
* `email`: <*string*> email-like identifier of the Service Account. Can be used to get the object using the API.
* `first_name`: <*string*> Identifier the person who created the service account provided while adding it to the group.
* `privileges`: <*dictionary*> Service Account's granted privileges. Each dictionary key is a *string* representing the privilege's name and each *dictionary* value is a dictionary having the following fields:
  * `expiration_date`: <*integer*> privilege's expiration date as UTC timestamp.
  * `granted`: <*boolean*> whether that privilege is granted or not.
  * `inherited_from`: <*string*> group name the permission is inherited from.
  * `inherited_via`: <*string*> quota group where the permission is.
* `quotas`: <*dictionary*> Service Account's quota details. Each dictionary key is a *string* representing quota name and each dictionary value is a *dictionary* containing the following fields:
  * `allowed`: <*integer*> maximum allowed quota.
  * `used`: <*integer*> consumed quota.
* `reputation`: <*integer*> Service Account's community reputation.
* `status`: <*string*> Service Account's status.
* `user_since`: <*integer*> Service Account's creation date as UTC timestamp.

```json Service Account object
{
    "data": {
        "attributes": {
            "apikey": "<string>",
            "email": "<string>",
            "first_name": "<string>",
            "preferences": {
                "<string>": {}
            },
            "privileges": {
                "<string>": {
                    "expiration_date": <int>,
                    "granted": <bool>,
                    "inherited_from": "<string>",
                    "inherited_via": "<string>"
                }
            },
            "quotas": {
                "<string>": {
                    "allowed": <int>,
                    "used": <int>
                }
            },
            "reputation": <int>,
            "status": "<string>",
            "user_since": <int>
        },
        "id": "<string>",
        "links": {
            "self": "https://www.virustotal.com/api/v3/users/<id>"
        },
        "type": "service_account"
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
                    "used": 5
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
    }
}
```

## relationships

In addition to the previously described attributes, Service Account objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../01-api-introduction/api-responses/introduction-relationships.md) section.

The following table shows a summary of available relationships for Service Account objects.

| Relationship               | Description                                                       | Accessibility | Return object type                         |
| :------------------------- | :---------------------------------------------------------------- | :------------ | :----------------------------------------- |
| api\_quota\_group          | Group from which the Service Account consumes API quota.          | Group Admin   | A single [Group](group-object.md) object. |
| comments                   | Comments posted by the Service Account.                           | Everyone.     | A list of [Comments](../03-ioc-investigation/comments.md).        |
| groups                     | Groups the Service Account belongs to.                            | Group Admin.  | A list of [Groups](group-object.md).      |
| intelligence\_quota\_group | Group from which the Service Account consumes intelligence quota. | Group Admin   | A single [Group](group-object.md) object. |
| mentions                   | Comments mentioning the user.                                     | Everyone.     | A list of [Comments](../03-ioc-investigation/comments.md).        |

These relationships are detailed in the subsections below.

---

← [Screenshots](screenshots-object.md) · [up](README.md) · [🔀🧑‍💻 api_quota_group](service-accounts-object/service-account-object-api-quota-group.md) →

*Archived from <https://gtidocs.virustotal.com/reference/service-accounts-object>.*
