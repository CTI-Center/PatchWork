---
title: "🔀 urls_for_embedded_js"
source: https://gtidocs.virustotal.com/reference/file-object-urls-for-embedded-js
slug: file-object-urls-for-embedded-js
section: reference
group: "API OBJECTS"
updatedAt: 2026-07-29T13:28:45.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › 🔀 urls_for_embedded_js

---

# 🔀-urls_for_embedded_js

URLs where a given JS file is embedded

The *urls\_for\_embedded\_js* relationship returns a list of ***URLs where a given JS script is embedded.***. This relationship is only available for Premium API users.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/files/files-relationships.md). The response contains a list of [URL](../url-object.md) objects. The relationship contains the following context attributes:

* `url`: <*string*> the URL is added as context attribute in case it's missing in the VirusTotal dataset.
* `timestamp`: <*integer*> date when the relationship was created as UTC timestamp.
* `embedded`: <*boolean*> whether the script was embedded in the URL's response body or it was linked as an external script.
* `download_url`: <*string*> only shown when `embedded` is false. URL from which the script was downloaded.
* `filename`: <*string*> only shown when `embedded` is false. Filename the script was downloaded with.

```json /files/{id}/urls_for_embedded_js
{
  "data": [
    {
      "attributes": <URL_OBJECT>,
      "context_attributes": {
        "url": "<string>",
        "timestamp": <int:timestamp>,
        "embedded": <bool>,
        "download_url": "<string>",
        "filename": "<string>"
      }
    },
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
                "last_final_url": "http://blablabla.com/attachments/701482853654053456/513583585475550504/blablabla",
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
                "tags": [
                    "downloads-pe"
                ],
                "main_brand": "google",
                "targeted_brand": {},
                "times_submitted": 1,
                "total_votes": {
                    "harmless": 0,
                    "malicious": 0
                },
                "trackers": {},
                "url": "http://blablabla.com/attachments/701482853654053456/513583585475550504/blablabla"
            },
            "context_attributes": {
                "url": "http://blablabla.com/attachments/701482853654053456/513583585475550504/blablabla"
                "timestamp": 1630107550,
                "embedded": false,
                "download_url": "http://test.com/js.js",
                "filename": "js.js"
            },
            "id": "c0390ef058c9e4607c19e215d8aefd3adef382ee27a6e7ec21e898e2e9f1ebd4",
            "links": {
                "self": "https://www.virustotal.com/api/v3/urls/c0390ef058c9e4607c19e215d8aefd3adef382ee27a6e7ec21e898e2e9f1ebd4"
            },
            "type": "url"
        }
    ],
    "links": {
        "self": "https://www.virustotal.com/api/v3/files/cf4b367e4ebf0b2e041c6f06ef4aa19fecfe3ec8d5abc0617343d1ae6c6ae6f5/urls_for_embedded_js?limit=10"
    },
    "meta": {
        "count": 1
    }
}
```

---

← [tlsh](file-object-tlsh.md) · [up](../README.md) · [known_distributors](file-object-known-distributors.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-urls-for-embedded-js>.*
