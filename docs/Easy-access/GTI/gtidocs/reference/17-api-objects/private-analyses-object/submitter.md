---
title: "🔀 submitter"
source: https://gtidocs.virustotal.com/reference/submitter
slug: submitter
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:44:17.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Private Analyses](../private-analyses-object.md) › 🔀 submitter

---

# 🔀-submitter

User who submitted the analysis

The *submitter* relationship returns the ***user who submitted the analysis***.

This relationship can be retrieved by using the [relationships API endpoint](../../06-private-scanning/private-analyses/private-analyses-relationship.md). The response contains a [users](../user-object.md) object.

```json /analyses/{analysis_id}/submitter
{
  "data": {
    <OBJECT>
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
	"meta": {
		"count": 1
	},
	"data": {
		"attributes": {
			"status": "active",
			"first_name": "Wile E.",
			"profile_phrase": "",
			"last_name": "Coyote",
			"reputation": 1
		},
		"type": "user",
		"id": "wcoyote",
		"links": {
			"self": "https://www.virustotal.com/api/v3/users/wcoyote"
		}
	},
	"links": {
		"self": "https://www.virustotal.com/api/v3/private/analyses/ZmI5Y2VmNGJmZDIwZTkzNmQ5MzY0NTcwMGI2Nzc2M2Q6Y2Y1MjY5YjZkMThlMWUwNWUyNGU0ZTBhN2M2ZjdlOWU6MTY2NjE3MDIyMg==/submitter"
	}
}
```

---

← [🔀 item](private-analyses-object-item.md) · [up](../README.md) · [Private Files](../private-files-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/submitter>.*
