---
title: "Analyses"
source: https://gtidocs.virustotal.com/reference/analyses-object
slug: analyses-object
section: reference
group: "API OBJECTS"
updatedAt: 2026-06-28T18:23:02.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Analyses

---

# analyses

Partner contributors' analyses for files and URLs.

An *Analysis* object represents an analysis of a URL or file submitted to Google Threat Intelligence, against all our [partnered contributors](https://support.virustotal.com/hc/en-us/articles/115002146809-Contributors).

> 📘 Two kinds of analysis
>
> Files and URLs both produce an analysis object and share the common structure documented on this page (`date`, `results`, `stats`, `status`). The set of returned fields differs by item type:
>
> * [File Analyses](file-analysis-object.md) — analyses of submitted **files**. Some fields (`engine_version`, `engine_update`, and the `confirmed-timeout` / `failure` / `type-unsupported` categories and stats) are only returned for files.
> * [URL Analyses](url-analysis-object.md) — analyses of submitted **URLs**. They add a rich set of per-visit browser-instrumentation attributes (final URL, response headers, screenshot/DOM artifacts, trackers, cookies, TLS, web technologies, etc.).
>
> This page documents the shared structure; see each specialised page for the type-specific fields.

Its attributes are:

* `date`:  <*integer*> Unix epoch UTC time (seconds).
* `results`: <*dictionary*> dictionary having the engine's name as key and its result as value. Its subfields are:
  * `category`: <*string*> normalised result. Possible values are:
    * "confirmed-timeout" (AV reached a timeout when analysing that file. Only returned in file analyses.)
    * "timeout" (AV reached a timeout when analysing that file.)
    * "failure" (AV failed when analysing this file. Only returned in file analyses).
    * "harmless" (AV thinks the file is not malicious),
    * "undetected" (AV has no opinion about this file),
    * "suspicious" (AV thinks the file is suspicious),
    * "malicious" (AV thinks the file is malicious).
    * "type-unsupported" (AV can't analyse that file. Only returned in file analyses).
  * `engine_name`: <*string*> the engine's name.
  * `engine_update`: <*string*> the engine's update date in `%Y%M%D` format. Only returned in file analyses.
  * `engine_version`: <*string*> the engine's version. Only returned in file analyses.
  * `method`: <*string*> detection method.
  * `result`: <*string*> engine result. If there's no verdict available, it can be `null`.
* `stats`: <*dictionary*> summary of the `results` field. It's subfields are:
  * `confirmed-timeout`: <*integer*> number of AV engines that reach a timeout when analysing that file.
  * `failure`: <*integer*>  number of AV engines that fail when analysing that file.
  * `harmless`: <*integer*> number of reports saying that is harmless.
  * `malicious`: <*integer*> number of reports saying that is malicious.
  * `suspicious`: <*integer*> number of reports saying that is suspicious.
  * `timeout`: <*integer*> number of timeouts when analysing this URL/file.
  * `type-unsupported`: <*integer*> number of AV engines that don't support that type of file.
  * `undetected`: <*integer*> number of reports saying that is undetected.
* `status`: <*string*> analysis status. Possible values are:
  * "completed" (the analysis is finished).
  * "queued" (the item is waiting to be analysed, the analysis object has empty results and stats).
  * "in-progress" (the file is being analysed, the analysis object has partial analysis results and stats).

```json Analysis object
{
  "data": {
    "attributes": {
    	 "date": <int:timestamp>,
       	"results": {
          	"<string>": {
            	"category": "<string>",
            	"engine_name": "<string>",
            	"engine_version": "<string>",
            	"engine_update": "<string>",
            	"method": "<string>",
            	"result": "<string>"
        	},
        	"stats": {
            	"confirmed-timeout": <int>,
           		"failure": <int>,
          		"harmless": <int>,
          		"malicious": <int>,
          		"suspicious": <int>,
          		"timeout": <int>,
           		"type-unsupported": <int>,
          		"undetected": <int>
        	},
        	"status": "<string>"      
    },
    "id": "<string>",
    "type": "analysis"
  }
}
```
```json File analysis example
{
    "data": {
        "attributes": {
            "date": 1591701363,
            "results": {
                "ALYac": {
                    "category": "malicious",
                    "engine_name": "ALYac",
                    "engine_update": "20200609",
                    "engine_version": "1.1.1.5",
                    "method": "blacklist",
                    "result": "Dialer.Webdialer.F"
                },
                "Avast": {
                    "category": "malicious",
                    "engine_name": "Avast",
                    "engine_update": "20200609",
                    "engine_version": "18.4.3895.0",
                    "method": "blacklist",
                    "result": "Win32:Dh-A [Heur]"
                },
                "Avast-Mobile": {
                    "category": "undetected",
                    "engine_name": "Avast-Mobile",
                    "engine_update": "20200609",
                    "engine_version": "200609-00",
                    "method": "blacklist",
                    "result": null
                },
                "CAT-QuickHeal": {
                    "category": "malicious",
                    "engine_name": "CAT-QuickHeal",
                    "engine_update": "20200609",
                    "engine_version": "14.00",
                    "method": "blacklist",
                    "result": "Trojan.Webdial"
                },
                "ClamAV": {
                    "category": "malicious",
                    "engine_name": "ClamAV",
                    "engine_update": "20200608",
                    "engine_version": "0.102.3.0",
                    "method": "blacklist",
                    "result": "Win.Trojan.Dialer-83"
                },
                "Comodo": {
                    "category": "malicious",
                    "engine_name": "Comodo",
                    "engine_update": "20200608",
                    "engine_version": "32518",
                    "method": "blacklist",
                    "result": "Malware@#1o6vtbly4swmm"
                }
            },
            "stats": {
                "confirmed-timeout": 0,
                "failure": 0,
                "harmless": 0,
                "malicious": 5,
                "suspicious": 0,
                "timeout": 0,
                "type-unsupported": 0,
                "undetected": 1
            },
            "status": "in-progress"
        },
        "id": "8zc5dTFiYmMxOTEpNzMzZWZmODE1ND7mYjU1ZjY5Npk6MTU5MlcwMTM2Mw==",
        "type": "analysis"
    }
}
```
```json URL analysis example
{
    "data": {
        "attributes": {
            "date": 1591701032,
            "results": {
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
                "Artists Against 419": {
                    "category": "harmless",
                    "engine_name": "Artists Against 419",
                    "method": "blacklist",
                    "result": "clean"
                },
                "AutoShun": {
                    "category": "undetected",
                    "engine_name": "AutoShun",
                    "method": "blacklist",
                    "result": "unrated"
                },
                "Avira": {
                    "category": "harmless",
                    "engine_name": "Avira",
                    "method": "blacklist",
                    "result": "clean"
                },
                "BADWARE.INFO": {
                    "category": "harmless",
                    "engine_name": "BADWARE.INFO",
                    "method": "blacklist",
                    "result": "clean"
                }
            },
            "stats": {
                "harmless": 7,
                "malicious": 0,
                "suspicious": 0,
                "timeout": 0,
                "undetected": 1
            },
            "status": "completed"
        },
        "id": "u-9d11db1b0q1200ba75016e4c010bc93836366881d021a658ua7f85a8b65c3c1e-1591701032",
        "type": "analysis"
    }
}
```

## relationships

In addition to the previously described attributes, analyses objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../01-api-introduction/api-responses/introduction-relationships.md)  section.

The following table shows a summary of available relationships.

| Relationship | Return object type                                  |
| :----------- | :-------------------------------------------------- |
| item         | A single [file](../03-ioc-investigation/files.md) or [URL](url-object.md) |

---

← [SeverityAnalysis](alerts-object/severityanalysis-object.md) · [up](README.md) · [🔀 item](analyses-object/item.md) →

*Archived from <https://gtidocs.virustotal.com/reference/analyses-object>.*
