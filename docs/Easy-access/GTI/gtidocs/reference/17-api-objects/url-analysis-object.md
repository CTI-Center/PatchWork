---
title: "URL Analyses"
source: https://gtidocs.virustotal.com/reference/url-analysis-object
slug: url-analysis-object
section: reference
group: "API OBJECTS"
updatedAt: 2026-07-29T13:28:45.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › URL Analyses

---

# url-analyses

A *URL Analysis* object represents a single visit performed by Google TI's browser to a URL, at a specific point in time. It is a specialised variant of the generic [Analyses](analyses-object.md) object: it carries everything a regular analysis exposes (`date`, `results`, `stats`, `status`) plus a rich set of URL-specific attributes captured during the visit (final URL after redirects, response code and headers, screenshot/DOM artifacts, trackers, cookies, web technologies, TLS information, etc.).

> 📘
>
> ### File vs URL analyses
>
> This page documents the **URL** variant. For analyses of submitted files see [File Analyses](file-analysis-object.md); for the structure shared by both see [Analyses](analyses-object.md).

URL Analyses are created when a URL is submitted via [POST /urls](../03-ioc-investigation/urls/scan-url.md) and are retrievable through [GET /analyses/{id}](../03-ioc-investigation/analyses-submissions-operations/analysis.md). The same analysis ID is exposed by the `analyses` relationship of the corresponding [URL object](url-object.md).

## object-attributes

These attributes describe what Google TI's browser observed *during this specific visit*. They are not aggregated; the URL object only carries the latest-seen equivalents.

### analysis-identification-and-verdict

* `date`: <*integer*> Unix epoch UTC time (seconds) when the analysis was performed.
* `status`: <*string*> analysis status. Possible values:
  * `queued` — the URL is waiting to be analysed; `results`/`stats` are empty.
  * `in-progress` — the URL is being analysed; `results`/`stats` may be partial.
  * `completed` — the analysis is finished.
* `stats`: <*dictionary*> summary of the engine `results`. Same shape as in the generic [Analyses](analyses-object.md) object (`harmless`, `malicious`, `suspicious`, `timeout`, `undetected`).
* `results`: <*dictionary*> per-engine verdicts. Same shape as in the generic [Analyses](analyses-object.md) object (`category`, `engine_name`, `method`, `result`).
* `url`: <*string*> URL originally submitted to be scanned.
* `tags`: <*list of strings*> tags attached to the analysis (e.g. `downloads`, `redirects`, `phishing-suspect`).
* `gti_assessment`: <*dictionary*> Google Threat Intelligence assessment for the URL at the time of the analysis (score, severity, verdict, contributing factors). `null` when the assessment is not available. Only returned to GTI customers.
* `finished_stages`: <*list of strings*> analysis pipeline stages that have already completed for this visit.

### per-visit-browser-instrumentation

* `browser_stats`: <*dictionary*> coarse counters about what the browser did during the visit (requests issued, DOM nodes, console errors, …).
* `console_messages`: <*list of dictionaries*> messages emitted to the browser's developer console during the visit (level, text, source).
* `javascript_variables`: <*list of dictionaries*> global JavaScript variables captured at the end of the visit (name, type, value).
* `metrics`: <*dictionary*> performance metrics gathered by the browser (timings, transfer sizes, layout/paint counters).
* `resources`: <*list of dictionaries*> network resources fetched while rendering the page. Each entry includes the resource URL, the chain of redirects it went through, the SHA-256 of its body when available, and basic timing information.
* `device`: <*string*> device profile emulated by the browser (e.g. `DESKTOP`, `MOBILE_IOS`, `MOBILE_ANDROID`).
* `tls`: <*list of dictionaries*> TLS metadata for the HTTPS endpoints contacted during the visit (certificate chain, JA3, ALPN, version, etc.).
* `filename`: <*string*> file name suggested by `Content-Disposition` (or derived from the URL path) for the downloaded resource, if any.
* `dom_sha256`: <*string*> SHA-256 of the rendered DOM captured during the visit. The DOM itself is retrievable through the [`dom`](../03-ioc-investigation/analyses-submissions-operations/analysis-dom.md) / [`dom_url`](../03-ioc-investigation/analyses-submissions-operations/analysis-dom-url.md) endpoints.

### per-visit-url-fields-(shape-shared-with-the-url-object)

The following attributes capture per-visit values for fields whose schema lives on the [URL object](url-object.md). The URL object exposes the *last-seen aggregate* of each (under the same name, or with a `last_` prefix for HTTP-response fields); the URL Analysis exposes the value *for this single visit*:

| URL Analysis attribute | URL object counterpart                |
| ---------------------- | ------------------------------------- |
| `final_url`            | `last_final_url`                      |
| `redirection_chain`    | `redirection_chain`                   |
| `response_code`        | `last_http_response_code`             |
| `response_headers`     | `last_http_response_headers`          |
| `content_length`       | `last_http_response_content_length`   |
| `title`                | `title`                               |
| `html_meta`            | `html_meta`                           |
| `favicon`              | `favicon`                             |
| `cookies`              | `last_http_response_cookies`          |
| `cookies_extended`     | `last_http_response_cookies_extended` |
| `trackers`             | `trackers`                            |
| `identified_brands`    | `identified_brands`                   |
| `main_brand`           | `main_brand`                          |
| `targeted_brand`       | `targeted_brand`                      |
| `web_technologies`     | `web_technologies`                    |
| `web_category`         | `web_category`                        |
| `partner_categories`   | `categories`                          |
| `user_agent`           | `user_agent`                          |
| `proxy_country`        | `proxy_country`                       |

Refer to the [URL object reference](url-object.md) for the schema, value semantics and ACL requirements of each.

## relationships

URL Analyses expose the following relationships, retrievable via [GET /analyses/{id}/{relationship}](https://gtidocs.readme.io/reference/analysis-relationships) (full objects) and [GET /analyses/{id}/relationships/{relationship}](https://gtidocs.readme.io/reference/analysis-relationships) (descriptors only):

| Relationship         | Cardinality | Returns                                                                                                                                        |
| -------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `item`               | one-to-one  | The [URL object](url-object.md) this analysis was performed for.                                                                              |
| `serving_ip_address` | one-to-one  | The [IP object](ip-object.md) that served `final_url`.                                                                                        |
| `http_transactions`  | one-to-many | A list of [URL objects](url-object.md) for every resource fetched during the visit, with the resource metadata exposed as context attributes. |
| `downloaded_file`    | one-to-one  | The [File object](file-object.md) corresponding to the file downloaded from `final_url`, when the visit downloaded one.                       |
| `outgoing_links`     | one-to-many | A list of [URL objects](url-object.md) seen in the DOM that point to a different domain than the URL being analysed.                          |
| `contacted_domains`  | one-to-many | A list of [Domain objects](domains-object.md) contacted during the visit.                                                                     |
| `contacted_ips`      | one-to-many | A list of [IP objects](ip-object.md) contacted during the visit.                                                                              |

## identifiers

URL Analysis IDs use the form `u-<sha256-of-canonical-url>-<suffix>` (e.g. `u-acbd18db4cc2f85cedef654fccc4a4d8-abdfe`). The substring between the two dashes is the corresponding [URL object](url-object.md) ID — you can extract it client-side to navigate between the two without an extra round-trip.

## example

```json URL Analysis object
{
  "data": {
    "id": "u-<sha256>-<suffix>",
    "type": "analysis",
    "attributes": {
      "date": 1716115200,
      "status": "completed",
      "stats": {
        "harmless": 71,
        "malicious": 2,
        "suspicious": 0,
        "timeout": 0,
        "undetected": 21
      },
      "results": {
        "<engine_name>": {
          "category": "harmless",
          "engine_name": "<engine_name>",
          "method": "blacklist",
          "result": "clean"
        }
      },
      "url": "https://example.com/",
      "final_url": "https://www.example.com/landing",
      "title": "Example Domain",
      "redirection_chain": [
        "https://example.com/",
        "https://www.example.com/landing"
      ],
      "response_code": 200,
      "response_headers": {
        "content-type": "text/html; charset=UTF-8",
        "server": "nginx"
      },
      "content_length": 14580,
      "html_meta": {
        "viewport": ["width=device-width, initial-scale=1"],
        "description": ["Illustrative example domain"]
      },
      "favicon": {
        "dhash": "<dhash>",
        "raw_md5": "<md5>"
      },
      "cookies": {
        "sessionid": "<value>"
      },
      "cookies_extended": [
        {
          "name": "sessionid",
          "value": "<value>",
          "domain": ".example.com",
          "path": "/",
          "expires": 1716200000,
          "secure": true,
          "http_only": true,
          "same_site": "Lax",
          "partitioned": false
        }
      ],
      "trackers": {
        "google-analytics": [
          {"id": "G-XXXXXXX", "url": "https://www.googletagmanager.com/gtag/js"}
        ]
      },
      "identified_brands": {},
      "main_brand": "google",
      "targeted_brand": {},
      "tls": [
        {
          "ja3": "<ja3>",
          "version": "TLSv1.3",
          "subject": "CN=www.example.com",
          "issuer": "CN=Example CA"
        }
      ],
      "web_technologies": [
        {"name": "nginx", "version": "1.25.4", "categories": ["Web servers"]}
      ],
      "browser_stats": {
        "requests": 14,
        "dom_nodes": 312,
        "console_errors": 0
      },
      "web_category": "business",
      "partner_categories": {
        "<partner>": "business"
      },
      "resources": [
        {
          "url": "https://www.example.com/main.js",
          "sha256": "<sha256>",
          "redirects": []
        }
      ],
      "javascript_variables": [
        {"name": "dataLayer", "type": "object", "value": "[]"}
      ],
      "console_messages": [],
      "metrics": {
        "navigation_duration_ms": 812,
        "transfer_size_bytes": 14580
      },
      "user_agent": "Mozilla/5.0 ...",
      "proxy_country": "US",
      "device": "DESKTOP",
      "tags": [],
      "gti_assessment": null
    }
  }
}
```

<br />

---

← [File Analyses](file-analysis-object.md) · [up](README.md) · [Users](user-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/url-analysis-object>.*
