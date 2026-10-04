---
title: "Sigma Analyses"
source: https://gtidocs.virustotal.com/reference/sigma-analyses-object
slug: sigma-analyses-object
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:44:43.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Sigma Analyses

---

# sigma-analyses

Sigma analyses run in sandbox generated sysmon logs.

> 🚧 DEPRECATED
>
> Sigma analyses metadata is now included in both the File and File behaviour objects.

In order to increment our detecting capabilities, we analyse sandbox generated Sysmon logs using [Sigma](https://github.com/SigmaHQ/sigma).

## object-attributes

A sigma analysis object's ID is the SHA256 from the file it's analyzing and contains the following attributes:

* `analysis_date`: <*integer*> analysis date as UTC timestamp.
* `last_modification_date`: <*integer*> analysis' last modification date as UTC timestamp.
* `rule_matches`: <*list of dictionaries*> contains a summary of matched rules. Every item contains the following subfields:
  * `match_context`: <*string*> matched strings from the log file.
  * `rule_author`: <*string*> rule authors separated by commas.
  * `rule_description`: <*string*> brief summary about what the rule detects.
  * `rule_id`: <*string*> rule ID in Google Threat Intelligence's database.
  * `rule_level`: <*string*> rule severity. Can be "low", "medium", "high" or "critical".
  * `rule_source`: <*string*> ruleset where the rule belongs.
  * `rule_title`: <*string*> rule title.
* `severity_stats`: <*dictionary*> stats matched rules by severity:
  * `critical`: <*integer*> number of matched rules having a "critical" severity.
  * `high`: <*integer*> number of matched rules having a "high" severity.
  * `low`: <*integer*> number of matched rules having a "low" severity.
  * `medium`: <*integer*> number of matched rules having a "medium" severity.
* `source_severity_stats`: <*dictionary*> same as `severity_stats` but grouping stats by ruleset. Keys are ruleset names as *string* and values are stats in a *dictionary*.

```json Sigma analysis
{
    "data": {
        "attributes": {
            "analysis_date": <int:timestamp>,
            "last_modification_date": <int:timestamp>,
            "rule_matches": [
                {
                    "match_context": "<string>",
                    "rule_author": "<string>",
                    "rule_description": "<string>",
                    "rule_id": "<string>",
                    "rule_level": "<string>",
                    "rule_source": "<string>",
                    "rule_title": "<string>"
                }
            ],
            "severity_stats": {
                "critical": <int>,
                "high": <int>,
                "low": <int>,
                "medium": <int>
            },
            "source_severity_stats": {
                "<string>": {
                    "critical": <int>,
                    "high": <int>,
                    "low": <int>,
                    "medium": <int>
                }
            }
        },
        "id": "<string>",
        "links": {
            "self": "https://www.virustotal.com/api/v3/sigma_analyses/<id>"
        },
        "type": "sigma_analysis"
    }
}
```
```json Example
{
    "data": {
        "attributes": {
            "analysis_date": 1593522810,
            "last_modification_date": 1593522811,
            "rule_matches": [
                {
                    "match_context": "$CommandLine: 'attrib  +H monitor.bak', $EventID: '1', $Image: 'C:\\Windows\\System32\\attrib.exe', $ParentCommandLine: 'C:\\Windows\\system32\\cmd.exe /c attrib +H monitor.bak'",
                    "rule_author": "Rick Sanchez",
                    "rule_description": "Detects usage of attrib.exe to hide files from users.",
                    "rule_id": "5c3ea6806114163b8cdf5735aeb07e702ab63e0e486f721df84cf675e2b0a04b",
                    "rule_level": "low",
                    "rule_source": "Sigma Integrated Rule Set (GitHub)",
                    "rule_title": "Hiding Files with Attrib.exe"
                },
                {
                    "match_context": "$CommandLine: 'attrib  +H window_texts.txt', $EventID: '1', $Image: 'C:\\Windows\\System32\\attrib.exe', $ParentCommandLine: 'C:\\Windows\\system32\\cmd.exe /c attrib +H window_texts.txt'",
                    "rule_author": "Rick Sanchez",
                    "rule_description": "Detects usage of attrib.exe to hide files from users.",
                    "rule_id": "5c3ea6806114163b8cdf5735aeb07e702ab63e0e486f721df84cf675e2b0a04b",
                    "rule_level": "low",
                    "rule_source": "Sigma Integrated Rule Set (GitHub)",
                    "rule_title": "Hiding Files with Attrib.exe"
                },
                {
                    "match_context": "$CommandLine: 'attrib  +H 676886ed8c6f48c5b5476d796a6353be.png', $EventID: '1', $Image: 'C:\\Windows\\System32\\attrib.exe', $ParentCommandLine: 'C:\\Windows\\system32\\cmd.exe /c attrib +H 676886ed8c6f48c5b5476d796a6353be.png'",
                    "rule_author": "Rick Sanchez",
                    "rule_description": "Detects usage of attrib.exe to hide files from users.",
                    "rule_id": "5c3ea6806114163b8cdf5735aeb07e702ab63e0e486f721df84cf675e2b0a04b",
                    "rule_level": "low",
                    "rule_source": "Sigma Integrated Rule Set (GitHub)",
                    "rule_title": "Hiding Files with Attrib.exe"
                },
                {
                    "match_context": "$CommandLine: '\"schtasks.exe\" /create /f /tn \"UPNP Monitor\" /xml \"C:\\Users\\admin\\AppData\\Local\\Temp\\tmpF033.tmp\"', $EventID: '1', $Image: 'C:\\Windows\\SysWOW64\\schtasks.exe', $User: 'work\\admin'",
                    "rule_author": "Rick Sanchez",
                    "rule_description": "Detects the creation of scheduled tasks in user session",
                    "rule_id": "3bc9d14114a6b67367a24df21134d0564d6f08a0ad903d68f9b25e9d8b7f0790",
                    "rule_level": "low",
                    "rule_source": "Sigma Integrated Rule Set (GitHub)",
                    "rule_title": "Scheduled Task Creation"
                }
            ],
            "severity_stats": {
                "critical": 0,
                "high": 0,
                "low": 4,
                "medium": 0
            },
            "source_severity_stats": {
                "Sigma Integrated Rule Set (GitHub)": {
                    "critical": 0,
                    "high": 0,
                    "low": 4,
                    "medium": 0
                }
            }
        },
        "id": "c885691ab568bd5bff581555e1d15ef82558c5a655c9c51ae5bd554b85fc7424",
        "links": {
            "self": "https://www.virustotal.com/api/v3/sigma_analyses/c885691ab568bd5bff581555e1d15ef82558c5a655c9c51ae5bd554b85fc7424"
        },
        "type": "sigma_analysis"
    }
}
```

## relationships

In addition to the previously described attributes, Sigma Analysis objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../01-api-introduction/api-responses/introduction-relationships.md) section.

The following table shows a summary of available relationships for Sigma analysis objects.

| Relationship | Description                          | Accessibility | Return object type                              |
| :----------- | :----------------------------------- | :------------ | :---------------------------------------------- |
| rules        | Sigma rules that matched an analysis | Everyone      | A list of [Sigma Rules](sigma-rule-object.md). |

These relationships are detailed in the subsections below.

---

← [🔀 mentions](service-accounts-object/service-account-object-mentions.md) · [up](README.md) · [🔀 rules](sigma-analyses-object/sigma-analyses-object-rules.md) →

*Archived from <https://gtidocs.virustotal.com/reference/sigma-analyses-object>.*
