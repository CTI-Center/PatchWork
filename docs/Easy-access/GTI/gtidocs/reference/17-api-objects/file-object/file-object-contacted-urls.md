---
title: "🔀 contacted_urls"
source: https://gtidocs.virustotal.com/reference/file-object-contacted-urls
slug: file-object-contacted-urls
section: reference
group: "API OBJECTS"
updatedAt: 2026-07-29T13:28:45.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › 🔀 contacted_urls

---

# 🔀-contacted_urls

URL addresses contacted by a given file

The *contacted\_urls* relationship returns the list of ***all URL addresses which were detected as contacted by the given file***.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/files/files-relationships.md). The response contains a list of [URLs](../url-object.md) objects.

```json /files/{file_hash}/contacted_urls
{
  "data": [
    <URL_OBJECT>,
    <URL_OBJECT>,
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
                "categories": {},
                "first_submission_date": 1539838768,
                "has_content": false,
                "html_meta": {},
                "last_analysis_date": 1539838768,
                "last_analysis_results": {
                    "ADMINUSLabs": {
                        "category": "harmless",
                        "engine_name": "ADMINUSLabs",
                        "method": "blacklist",
                        "result": "clean"
                    },
                    "AegisLab WebGuard": {
                        "category": "harmless",
                        "engine_name": "AegisLab WebGuard",
                        "method": "blacklist",
                        "result": "clean"
                    },
                    "AlienVault": {
                        "category": "harmless",
                        "engine_name": "AlienVault",
                        "method": "blacklist",
                        "result": "clean"
                    },
                    "Antiy-AVL": {
                        "category": "harmless",
                        "engine_name": "Antiy-AVL",
                        "method": "blacklist",
                        "result": "clean"
                    },
                    "AutoShun": {
                        "category": "undetected",
                        "engine_name": "AutoShun",
                        "method": "blacklist",
                        "result": "unrated"
                    }
                },
                "last_analysis_stats": {
                    "harmless": 4,
                    "malicious": 0,
                    "suspicious": 0,
                    "timeout": 0,
                    "undetected": 1
                },
                "last_final_url": "http://www.foo.com/sorry/index?continue=http://www.foo.com/&q=EgQju4QqGKWmoN4FIhkAfafDS8sfxEOcnf92ZCfaAqfGCDfmf_HyfgFy",
                "last_http_response_code": 503,
                "last_http_response_content_length": 2794,
                "last_http_response_content_sha256": "07f934e830ced400ee63eefc75ce7050e14e3e11ee4262ebb7aedc5ae8abe7eb",
                "last_http_response_headers": {
                    "cache-control": "no-store, no-cache, must-revalidate",
                    "content-length": "2794",
                    "content-type": "text/html",
                    "date": "Thu, 18 Oct 2018 04:59:29 GMT",
                    "expires": "Fri, 01 Jan 1990 00:00:00 GMT",
                    "pragma": "no-cache",
                    "server": "HTTP server (unknown)",
                    "x-xss-protection": "1; mode=block"
                },
                "last_modification_date": 1539838779,
                "last_submission_date": 1539838768,
                "reputation": 0,
                "tags": [],
                "main_brand": "google",
                "targeted_brand": {},
                "times_submitted": 1,
                "total_votes": {
                    "harmless": 0,
                    "malicious": 0
                },
                "trackers": {},
                "url": "http://www.foo.com/sorry/index?continue=http://www.foo.com/&q=EgQju4QqGKWmoN4FIhkAfafDS8sfxEOcnf92ZCfaAqfGCDfmf_HyfgFy"
            },
            "id": "c0390ef058c9e4607c19e215d8aefd3adef382ee27a6e7ec21e898e2e9f1ebd4",
            "links": {
                "self": "https://www.virustotal.com/api/v3/urls/c0390ef058c9e4607c19e215d8aefd3adef382ee27a6e7ec21e898e2e9f1ebd4"
            },
            "type": "url"
        }
    ],
    "links": {
        "self": "https://www.virustotal.com/api/v3/files/cf4b367e4ebf0b2e041c6f06ef4aa19fecfe3ec8d5abc0617343d1ae6c6ae6f5/contacted_urls?limit=10"
    },
    "meta": {
        "count": 1
    }
}
```

---

← [🔀 compressed_parents](file-object-compressed-parents.md) · [up](../README.md) · [🔀 email_attachments](file-object-email-attachments.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-contacted-urls>.*
