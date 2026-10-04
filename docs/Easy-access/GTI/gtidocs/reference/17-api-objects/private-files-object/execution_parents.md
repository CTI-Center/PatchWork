---
title: "🔀 execution_parents"
source: https://gtidocs.virustotal.com/reference/execution_parents
slug: execution_parents
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T02:14:14.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Private Files](../private-files-object.md) › 🔀 execution_parents

---

# 🔀-execution_parents

Files dropping the file during its execution

The *execution\_parents* relationship returns the list of ***all files dropping the given file during its execution***. Each of the files returned also contains contextual information (paths where the file was dropped and file type).

This relationship can be retrieved using the [relationships API endpoint](../../06-private-scanning/private-files/private-files-relationships.md). The response contains a list of [private files](../private-files-object.md) objects.

```json /private/files/{sha256}/execution_parents
{
  "data": [
    {
      "attributes": {
        ...
      },
      "context_attributes": {
        "paths": [<string>, ...],
        "type": <string>
      }
      "type": "private_file",
      "id": <string>
    }  ,
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
		"count": 1
	},
	"data": [
		{
			"attributes": {
				...
			},
			"type": "private_file",
			"id": "7354b30f2e7ff0166dd73be94ec6d33b8b12f614798a6c735ede0d9e26a2b36f",
			"links": {
				"self": "https://www.virustotal.com/api/v3/private/files/7354b30f2e7ff0166dd73be94ec6d33b8b12f614798a6c735ede0d9e26a2b36f"
			},
			"context_attributes": {
				"paths": [
					"C:\\Users\\user\\AppData\\Local\\Microsoft\\Teams\\Update.exe"
				],
				"type": "Win32 EXE"
			}
		}
	],
	"links": {
		"self": "https://www.virustotal.com/api/v3/private/files/7a8c0b2d05f1d104837bc5fa31d936f608691c5937bcd2ccf05553d1a6bf4f87/execution_parents?limit=10"
	}
}
```

---

← [🔀 dropped_files](private-files-object-dropped_files.md) · [up](../README.md) · [🔀 embedded_urls](embedded_urls.md) →

*Archived from <https://gtidocs.virustotal.com/reference/execution_parents>.*
