---
title: "🔀 submissions"
source: https://gtidocs.virustotal.com/reference/file-object-submissions
slug: file-object-submissions
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:55.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › 🔀 submissions

---

# 🔀-submissions

File submissions

The *submissions* relationship returns a list ***containing the submissions for a given file***. The relationship is only available for Premium API users.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/files/files-relationships.md). The response contains a list of [Submission](../submission-object.md) objects.

```json /files/{file_hash}/submissions
{
  "data": [
  	<SUBMISSION_OBJECT>,
    <SUBMISSION_OBJECT>
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
                "city": "paris",
                "country": "FR",
                "date": 1593590610,
                "interface": "api",
                "name": "WallpaperHdInstaller_FR_V4",
                "source_key": "f89ef1ec"
            },
            "id": "f-45e545fd64795da21e54f3a55cf9da25cd6b5e07152c65905515dac518fac417-1593590610",
            "links": {
                "self": "https://www.virustotal.com/api/v3/submissions/f-45e545fd64795da21e54f3a55cf9da25cd6b5e07152c65905515dac518fac417-1593590610"
            },
            "type": "submission"
        }
    ],
    "links": {
        "next": "https://www.virustotal.com/api/v3/files/45e545fd64795da21e54f3a55cf9da25cd6b5e07152c65905515dac518fac417/submissions?cursor=CuABC4KBGRhdGUSCQiAy9mZ6KfqAhLGAWoRc352aXJ1c3RvdGFsY2xvdWRysAELEgZTYW1wbGUiQDQyZTU0NGZ4NjQ3OTdkYTIxZWE0ZjNhNWNjZjlkYTJlY2Q2YmFlMDcxOTJjNjY5MDU5MWNkYWNmMThmYWM0MTcMCxIK43Vi4bWlzc2lvbiJUNDJlNTQ0ZmQ2NDc5N2RhMjFlYTRmM2E1Y2NmOWRhMmVjZDZiYWUwNzE5MmM2NjkwNTkx2RhY4YxOGZhYzQxNy0yMDIwLTA2LTI5VDIwOjAwOjM4DBgAIAE%3D&limit=1",
        "self": "https://www.virustotal.com/api/v3/files/42e544fd64797da21ea4f3a5ccf9da2ecd6bae07192c6690591cdacf18fac417/submissions?limit=1"
    },
    "meta": {
        "count": 200,
        "cursor": "CuABC4KBGRhdGUSCQiAy9mZ6KfqAhLGAWoRc352aXJ1c3RvdGFsY2xvdWRysAELEgZTYW1wbGUiQDQyZTU0NGZ4NjQ3OTdkYTIxZWE0ZjNhNWNjZjlkYTJlY2Q2YmFlMDcxOTJjNjY5MDU5MWNkYWNmMThmYWM0MTcMCxIK43Vi4bWlzc2lvbiJUNDJlNTQ0ZmQ2NDc5N2RhMjFlYTRmM2E1Y2NmOWRhMmVjZDZiYWUwNzE5MmM2NjkwNTkx2RhY4YxOGZhYzQxNy0yMDIwLTA2LTI5VDIwOjAwOjM4DBgAIAE="
    }
}
```

---

← [🔀 sigma_analysis](file-object-sigma-analysis.md) · [up](../README.md) · [snort](file-object-snort.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-submissions>.*
