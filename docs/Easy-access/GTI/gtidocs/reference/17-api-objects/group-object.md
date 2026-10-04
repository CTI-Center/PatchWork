---
title: "Groups"
source: https://gtidocs.virustotal.com/reference/group-object
slug: group-object
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:43:19.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Groups

---

# groups

Groups of users in Google Threat Intelligence

The Group objects describes groups of users in Google Threat Intelligence. Groups are used to share API privileges between a set of users, for example, users belonging to the same company.

## object-attributes

A Group object contains the following attributes:

* `auto_add_users`: <*list of strings*> contains a list of emails that will be automatically added to this group when they create a Google Threat Intelligence account. Patterns can be used too. Only visible for the group's admins.
* `country`: <*string*> group's country. Only visible for the group's members and admins.
* `country_iso`: <*string*> group's country ISO code. Only visible for the group's members and admins.
* `domain_name`: <*string*> group's domain name. Only visible for the group's members and admins.
* `industry`: <*string*> group's industry. Only visible for the group's members and admins.
* `agreement_signed_date`: <*integer*> agreement signed date as UTC timestamp. Only visible for the group's members and admins.
* `organization`: <*string*> company name.
* `organization_legal_name`: <*string*> company legal name.
* `preferences`: <*dictionary*> Google Threat Intelligence group's preferences. Only visibile for the group's members and admins. Every subitem is a dictionary having a string as key.
* `privileges`: <*dictionary*> group's granted privileges. Only visibile for the group's members and admins. Each dictionary key is a *string* representing the privilege's name and each value is a *dictionary* having the following fields:
  * `expiration_date`: <*integer*> privilege's expiration date as UTC timestamp.
  * `granted`: <*boolean*> whether that privilege is granted or not.
* `quotas`: <*dictionary*> group's quota details. Only visible for the group's members and admins. Each dictionary key is a *string* representing quota name and each *value* is a dictionary containing the following fields:
  * `allowed`: <*integer*> maximum allowed quota.
  * `used`: <*integer*> consumed quota.

```json Group object
{
    "data": {
        "attributes": {
            "auto_add_users": ["<string>"],
            "contact_emails": [
                "<string>"
            ],
            "country": "<string>",
            "country_iso": "<string>",
            "domain_name": "<string>",
            "organization": "<string>",
            "organization_legal_name": "<string>",
            "preferences": {
                "<string>": {}
            },
            "privileges": {
                "<string>": {
                    "expiration_date": <integer>,
                    "granted": <boolean>
                }
            },
            "quotas": {
                "<string>": {
                    "allowed": <integer>,
                    "used": <integer>
                }
            }
        },
        "context_attributes": {
            "role": "<string>"
        },
        "id": "<string>",
        "links": {
            "self": "https://www.virustotal.com/api/v3/groups/<id>"
        },
        "type": "group"
    }
}
```
```json Example
{
    "data": {
        "attributes": {
            "auto_add_users": [
                "*@blabla.com"
            ],
            "country": "United States",
            "country_iso": "US",
            "domain_name": "blablabla.com",
            "organization": "Company Inc.",
            "preferences": {},
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
            "quotas": {
                "api_requests_daily": {
                    "allowed": 1000,
                    "used": 0
                },
                "api_requests_hourly": {
                    "allowed": 60000,
                    "used": 0
                },
                "api_requests_monthly": {
                    "allowed": 30000,
                    "used": 68
                },
                "cases_creation_monthly": {
                    "allowed": 20,
                    "used": 0
                }
            }
        },
        "context_attributes": {
            "role": "user"
        }
        "id": "company",
        "links": {
            "self": "https://www.virustotal.com/api/v3/groups/company"
        },
        "type": "group"
    }
}
```

## relationships

In addition to the previously described attributes, Group objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../01-api-introduction/api-responses/introduction-relationships.md)  section.

The following table shows a summary of available relationships for group objects.

| Relationship      | Description                     | Accessibility | Return object type                                      |
| :---------------- | :------------------------------ | :------------ | :------------------------------------------------------ |
| administrators    | Group administrators            | Group Members | List of [Users](user-object.md)                        |
| graphs            | Graphs created by group members | Group Members | List of [Graphs](graph-object.md)                      |
| users             | Group members                   | Group Members | List of [Users](user-object.md)                        |
| service\_accounts | Group service accounts          | Group Members | List of [Service Accounts](service-accounts-object.md) |

These relationships are detailed in the subsections below.

---

← [🔀 viewers](graph-object/graph-viewers.md) · [up](README.md) · [🔀🧑‍💻 administrators](group-object/group-administrators.md) →

*Archived from <https://gtidocs.virustotal.com/reference/group-object>.*
