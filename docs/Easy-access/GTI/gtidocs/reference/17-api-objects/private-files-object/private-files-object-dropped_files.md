---
title: "🔀 dropped_files"
source: https://gtidocs.virustotal.com/reference/private-files-object-dropped_files
slug: private-files-object-dropped_files
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T02:14:13.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Private Files](../private-files-object.md) › 🔀 dropped_files

---

# 🔀-dropped_files

Files dropped during the file's execution

The *dropped\_files* relationship returns the list of ***all files dropped during the execution of the given private file***. Each of the files returned also contains contextual information (paths where the file was dropped and file type).

This relationship can be retrieved using the [relationships API endpoint](../../06-private-scanning/private-files/private-files-relationships.md). The response contains a list of [private files](../private-files-object.md) objects.

```json /private/files/{sha256}/dropped_files
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
		"count": 167,
		"cursor": "STEKLg=="
	},
	"data": [
		{
			"attributes": {
				...
			},
			"type": "private_file",
			"id": "7a8c0b2d05f1d104837bc5fa31d936f608691c5937bcd2ccf05553d1a6bf4f87",
			"links": {
				"self": "https://www.virustotal.com/api/v3/private/files/7a8c0b2d05f1d104837bc5fa31d936f608691c5937bcd2ccf05553d1a6bf4f87"
			},
			"context_attributes": {
				"paths": [
					"C:\\Users\\user\\AppData\\Local\\Microsoft\\Teams\\Update.exe",
					"C:\\Users\\user\\AppData\\Local\\SquirrelTemp\\Update.exe"
				],
				"type": "Win32 EXE"
			}
		}
	],
	"links": {
		"self": "https://www.virustotal.com/api/v3/private/files/7354b30f2e7ff0166dd73be94ec6d33b8b12f614798a6c735ede0d9e26a2b36f/dropped_files?limit=1",
		"next": "https://www.virustotal.com/api/v3/private/files/7354b30f2e7ff0166dd73be94ec6d33b8b12f614798a6c735ede0d9e26a2b36f/dropped_files?cursor=STEKLg%3D%3D&limit=1"
	}
}
```

---

← [🔀 behaviours](behaviours.md) · [up](../README.md) · [🔀 execution_parents](execution_parents.md) →

*Archived from <https://gtidocs.virustotal.com/reference/private-files-object-dropped_files>.*
