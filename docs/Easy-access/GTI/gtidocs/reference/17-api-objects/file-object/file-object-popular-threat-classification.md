---
title: "popular_threat_classification"
source: https://gtidocs.virustotal.com/reference/file-object-popular-threat-classification
slug: file-object-popular-threat-classification
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:42:17.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › popular_threat_classification

---

# popular_threat_classification

Human readable names extracted from the AV verdicts and clustering hashes

`popular_threat_classification` extracts human readable names extracted from AV verdicts and clustering hashes. It contains the following fields:

* `popular_threat_name`: <*list of dictionaries*> dictionaries where 'value' is a token and 'count' is how many AV engines had said token. The dictionaries are sorted in decreasing frequency.
* `popular_threat_category`: <*list of dictionaries*> similar to popular\_threat\_name but these tokens are considered more generic or, in other words, categories of malware, instead of individual families. Unlike popular\_threat\_name, popular\_threat\_category is somewhat normalized. E.g.: 'ransom' becomes 'ransomware'.
* `suggested_threat_label`: <*string*> a string combining part of popular\_threat\_category and popular\_threat\_name.

```json Popular threat classification
{
	"data": {
		...
		"attributes": {
			...
			"popular_threat_classification": {
				"suggested_threat_label": <string>,
				"popular_threat_category": [
					{
						"count": <int>,
						"value": <string>
					},
					...
				],
				"popular_threat_name": [
					{
						"count": <int>,
						"value": <string>
					},
					...
				]
			},
		}
	}
}
```
```json Example
{
	"data": {
		...
		"attributes": {
			...
			"popular_threat_classification": {
				"suggested_threat_label": "adware.jatift/machaer",
				"popular_threat_category": [
					{
						"count": 8,
						"value": "adware"
					}
				],
				"popular_threat_name": [
					{
						"count": 8,
						"value": "jatift"
					},
					{
						"count": 7,
						"value": "machaer"
					},
					{
						"count": 4,
						"value": "mailru"
					}
				]
			}
		}
	}
}
```

---

← [🔀🧑‍💻 user_votes](file-object-user-votes.md) · [up](../README.md) · [🔀 collections](file-object-collections.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-popular-threat-classification>.*
