---
title: "🔀 votes"
source: https://gtidocs.virustotal.com/reference/user-object-votes
slug: user-object-votes
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:45:57.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Users](../user-object.md) › 🔀 votes

---

# 🔀-votes

Votes posted by a certain user

The *votes* relationship returns a list of ***all votes posted by a certain user***.

This relationship can be retrieved by using the [relationships API endpoint](../../11-users-and-group-management/user-management/users-relationships.md) and contains a list of [Vote](../vote-object.md) objects.

```json /users/{user_id}/votes
{
  "data": [
    <VOTE_OBJECT>
    ...
  ],
  "links": {
    "next": <string>,
    "self": <string>
  },
  "meta": {
    "count": <int>,
    "cursor": <string>
  }
}
```
```json Example
{
	"meta": {
		"count": 3,
		"cursor": "Cl4SWGoRc352aXJ1c3RvdGFsY2xvdWRyQwsSBkRvbWFpbiISd3d3LnZpcnVzdG90YWwuY29tDAsSBFZvdGUiG3d3dy52aXJ1c3RvdGFsLmNvbS1lNmJjNjcwOAwYACAA"
	},
	"data": [
		{
			"attributes": {
				"date": 1623250000,
				"verdict": "harmless",
				"value": 1
			},
			"type": "vote",
			"id": "d-www.virustotal.com-abcdef012",
			"links": {
				"self": "https://www.virustotal.com/api/v3/votes/d-www.virustotal.com-abcdef012"
			}
		}
	],
	"links": {
		"self": "https://www.virustotal.com/api/v3/users/wcoyote/votes?limit=1",
		"next": "https://www.virustotal.com/api/v3/users/wcoyote/votes?cursor=Cl4SWGoRc352aXJ1c3RvdGFsY2xvdWRyQwsSBkRvbWFpbiISd3d3LnZpcnVzdG90YWwuY29tDAsSBFZvdGUiG3d3dy52aXJ1c3RvdGFsLmNvbS1lNmJjNjcwOAwYACAA&limit=1"
	}
}
```

---

← [🔀 collections](user-object-collections.md) · [up](../README.md) · [Votes](../vote-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/user-object-votes>.*
