---
title: "🔀 analyses"
source: https://gtidocs.virustotal.com/reference/file-object-analyses
slug: file-object-analyses
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:29.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › 🔀 analyses

---

# 🔀-analyses

All analyses made for a given file.

The *analyses* relationship returns the list of ***all analyses made for a given file***. This relationship is only available for Premium API users.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/files/files-relationships.md). The response contains a list of [Analysis](../analyses-object.md) objects.

```json /files/{file_hash}/analyses
{
  "data": [
    <ANALYSIS_OBJECT>,
    <ANALYSIS_OBJECT>,
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
                "date": 1593157207,
                "results": {
                    "ALYac": {
                        "category": "undetected",
                        "engine_name": "ALYac",
                        "engine_update": "20200626",
                        "engine_version": "1.1.1.5",
                        "method": "blacklist",
                        "result": null
                    },
                    "APEX": {
                        "category": "type-unsupported",
                        "engine_name": "APEX",
                        "engine_update": "20200625",
                        "engine_version": "6.41",
                        "method": "blacklist",
                        "result": null
                    },
                    "AVG": {
                        "category": "undetected",
                        "engine_name": "AVG",
                        "engine_update": "20200626",
                        "engine_version": "18.4.3895.0",
                        "method": "blacklist",
                        "result": null
                    },
                    "Acronis": {
                        "category": "type-unsupported",
                        "engine_name": "Acronis",
                        "engine_update": "20200603",
                        "engine_version": "1.1.1.76",
                        "method": "blacklist",
                        "result": null
                    }
                },
                "stats": {
                    "confirmed-timeout": 0,
                    "failure": 0,
                    "harmless": 0,
                    "malicious": 0,
                    "suspicious": 0,
                    "timeout": 0,
                    "type-unsupported": 2,
                    "undetected": 2
                },
                "status": "completed"
            },
            "id": "f-7b55b959cf56525ab528a5cb53e35a81545a5b54559955e5a6575f5085855db8-1593157207",
            "links": {
                "self": "https://www.virustotal.com/api/v3/analyses/f-7b55b959cf56525ab528a5cb53e35a81545a5b54559955e5a6575f5085855db8-1593157207"
            },
            "type": "analysis"
        }
    ],
    "links": {
        "self": "https://www.virustotal.com/ui/files/7b5cb939cf3652bab028a4cbb3e3ba81c45a4b54a999c5e3a6576f508585adb8/analyses?limit=20&order=date%2B"
    },
    "meta": {
        "count": 1
    }
}
```

---

← [malware_config](file-object-malware-config.md) · [up](../README.md) · [🔀 comments](file-object-comments.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-analyses>.*
