---
title: "🔀🧑‍💻 users"
source: https://gtidocs.virustotal.com/reference/group-users
slug: group-users
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T01:05:13.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Groups](../group-object.md) › 🔀🧑‍💻 users

---

# 🔀🧑‍💻-users

Group members

The *users* relationship returns all ***users belonging to a given group***. This relationship is only visible for the groups members.

It can be fetched using the [relationships API endpoint](../../11-users-and-group-management/group-management/groups-relationships.md) and it returns a list of [User](../user-object.md) objects.

```json /groups/{id}/users
{
  "data": [
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
				"apikey": "3333333t33333333333333r333333f333333g33333333c3333333f333333333a",
				"email": "blabla@blabla.com",
				"first_name": "Sabrina",
				"has_2fa": true,
				"last_login": 1598966628,
				"last_name": "Spellman",
				"preferences": {
					"graph": {
						"last_visit": 1597683192814,
						"main_walkthrough_version_seen": "1.0.0"
					},
					"ui": {
						"last_read_notification_date": 1598436845
					}
				},
				"privileges": {
					"cases": {
						"granted": false
					},
					"dogfooder": {
						"granted": false
					},
					"downloads-tier-1": {
						"granted": false
					},
					"downloads-tier-2": {
						"expiration_date": 1601510400,
						"granted": true,
						"inherited_from": "spellmans",
						"inherited_via": "api_quota_group"
					}
				},
				"profile_phrase": "",
				"quotas": {
					"api_requests_daily": {
						"allowed": 1000000000,
						"used": 101
					},
					"api_requests_hourly": {
						"allowed": 60000000000,
						"used": 0
					},
					"api_requests_monthly": {
						"allowed": 1000000000,
						"used": 1433
					},
					"cases_creation_monthly": {
						"allowed": 20,
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
		{
			"attributes": {
				"first_name": "Salem",
				"last_name": "Spellman",
				"profile_phrase": "Meow",
				"reputation": 1,
				"status": "active",
				"user_since": 1557214525
			},
			"id": "salem",
			"links": {
				"self": "https://www.virustotal.com/api/v3/users/salem"
			},
			"type": "user"
		}
	],
	"links": {
		"self": "https://www.virustotal.com/api/v3/groups/spellmans/users?limit=10"
	},
	"meta": {
		"count": 2
	}
}
```

---

← [🔀🧑‍💻 graphs](group-graphs.md) · [up](../README.md) · [Hunting Notifications](../hunting-notification-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/group-users>.*
