---
title: "File Analyses"
source: https://gtidocs.virustotal.com/reference/file-analysis-object
slug: file-analysis-object
section: reference
group: "API OBJECTS"
updatedAt: 2026-06-28T18:23:02.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › File Analyses

---

# file-analyses

A *File Analysis* object represents the result of analysing a **file** submitted to Google Threat Intelligence against our [partnered antivirus contributors](https://support.virustotal.com/hc/en-us/articles/115002146809-Contributors), at a specific point in time. It is a specialised variant of the generic [Analyses](analyses-object.md) object that only exposes the fields produced when the analysed item is a file.

File Analyses are created when a file is submitted (see the file submission endpoints) and are retrievable through [GET /analyses/\{id}](../03-ioc-investigation/analyses-submissions-operations/analysis.md). The same analysis IDs are also exposed by the [`analyses`](file-object/file-object-analyses.md) relationship of the corresponding [File object](file-object.md).

> 📘 File vs URL analyses
>
> Files and URLs both produce an analysis object, but the set of returned fields differs. This page documents the **file** variant; for the per-visit browser instrumentation returned when analysing a URL see [URL Analyses](url-analysis-object.md). The shared structure common to both is documented in [Analyses](analyses-object.md).

## object-attributes

* `date`: <*integer*> Unix epoch UTC time (seconds) when the analysis was performed.
* `status`: <*string*> analysis status. Possible values:
  * `queued` — the file is waiting to be analysed; `results`/`stats` are empty.
  * `in-progress` — the file is being analysed; `results`/`stats` may be partial.
  * `completed` — the analysis is finished.
* `results`: <*dictionary*> dictionary keyed by the engine's name. Each value has the following sub-fields:
  * `category`: <*string*> normalised result. Possible values:
    * `confirmed-timeout` — the AV reached a timeout when analysing the file (file analyses only).
    * `timeout` — the AV reached a timeout when analysing the file.
    * `failure` — the AV failed when analysing the file (file analyses only).
    * `harmless` — the AV thinks the file is not malicious.
    * `undetected` — the AV has no opinion about the file.
    * `suspicious` — the AV thinks the file is suspicious.
    * `malicious` — the AV thinks the file is malicious.
    * `type-unsupported` — the AV can't analyse this type of file (file analyses only).
  * `engine_name`: <*string*> the engine's name.
  * `engine_version`: <*string*> the engine's version (file analyses only).
  * `engine_update`: <*string*> the engine's signature update date in `%Y%m%d` format (file analyses only).
  * `method`: <*string*> detection method.
  * `result`: <*string*> engine result. `null` when there is no verdict.
* `stats`: <*dictionary*> summary of the `results` field:
  * `confirmed-timeout`: <*integer*> number of AV engines that reached a confirmed timeout (file analyses only).
  * `failure`: <*integer*> number of AV engines that failed (file analyses only).
  * `harmless`: <*integer*> number of reports saying the file is harmless.
  * `malicious`: <*integer*> number of reports saying the file is malicious.
  * `suspicious`: <*integer*> number of reports saying the file is suspicious.
  * `timeout`: <*integer*> number of timeouts when analysing the file.
  * `type-unsupported`: <*integer*> number of AV engines that don't support this type of file (file analyses only).
  * `undetected`: <*integer*> number of reports saying the file is undetected.

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
                "Avast-Mobile": {
                    "category": "undetected",
                    "engine_name": "Avast-Mobile",
                    "engine_update": "20200609",
                    "engine_version": "200609-00",
                    "method": "blacklist",
                    "result": null
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

## relationships

File Analyses expose the relationships of the generic [Analyses](analyses-object.md) object. In particular:

* `item`: the analysed [File object](file-object.md). Retrievable through [GET /analyses/\{id}/item](../03-ioc-investigation/analyses-submissions-operations/analyses-get-objects.md).

---

← [🔀 related_threat_actors](url-object/urls-object-related_threat_actors.md) · [up](README.md) · [URL Analyses](url-analysis-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-analysis-object>.*
