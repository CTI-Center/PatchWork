---
title: "🔀 sigma_analysis"
source: https://gtidocs.virustotal.com/reference/file-object-sigma-analysis
slug: file-object-sigma-analysis
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:55.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › 🔀 sigma_analysis

---

# 🔀-sigma_analysis

Last Sigma analysis results.

> 🚧 DEPRECATED
>
> Sigma Analyses metadata is now included in both File and File behaviour objects.

The *sigma\_analysis* relationship returns the results from the last [Sigma](https://github.com/SigmaHQ/sigma) analysis made for a given file.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/files/files-relationships.md). The response contains a [Sigma Analysis](../sigma-analyses-object.md) object.

```json /files/{file_hash}/sigma_analysis
{
  "data": <SIGMA_ANALYSIS_OBJECT>,
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
    "data": {
        "attributes": {
            "analysis_date": 1593522810,
            "last_modification_date": 1593522811,
            "rule_matches": [
                {
                    "match_context": "$CommandLine: 'attrib  +H blablabla.bak', $EventID: '1', $Image: 'C:\\Windows\\System32\\attrib.exe', $ParentCommandLine: 'C:\\Windows\\system32\\cmd.exe /c attrib +H blabalbla.bak'",
                    "rule_description": "Detects usage of attrib.exe to hide files from users.",
                    "rule_id": "5c3ea6806114163b8cdf5735aeb07e702ab63e0e486f721df84cf675e2b0a04b",
                    "rule_level": "low",
                    "rule_source": "Sigma Integrated Rule Set (GitHub)",
                    "rule_title": "Hiding Files with Attrib.exe"
                },
                {
                    "match_context": "$CommandLine: 'attrib  +H window_texts.txt', $EventID: '1', $Image: 'C:\\Windows\\System32\\attrib.exe', $ParentCommandLine: 'C:\\Windows\\system32\\cmd.exe /c attrib +H window_texts.txt'",
                    "rule_description": "Detects usage of attrib.exe to hide files from users.",
                    "rule_id": "5c3ea6806114163b8cdf5735aeb07e702ab63e0e486f721df84cf675e2b0a04b",
                    "rule_level": "low",
                    "rule_source": "Sigma Integrated Rule Set (GitHub)",
                    "rule_title": "Hiding Files with Attrib.exe"
                },
                {
                    "match_context": "$CommandLine: 'attrib  +H 676486e48c4f48c545446d49646353be.png', $EventID: '1', $Image: 'C:\\Windows\\System32\\attrib.exe', $ParentCommandLine: 'C:\\Windows\\system32\\cmd.exe /c attrib +H 676486e48c4f48c545446d49646353be.png'",
                    "rule_description": "Detects usage of attrib.exe to hide files from users.",
                    "rule_id": "5c3ea6806114163b8cdf5735aeb07e702ab63e0e486f721df84cf675e2b0a04b",
                    "rule_level": "low",
                    "rule_source": "Sigma Integrated Rule Set (GitHub)",
                    "rule_title": "Hiding Files with Attrib.exe"
                },
                {
                    "match_context": "$CommandLine: '\"blabla.exe\" /create /f /tn \"UPNP Monitor\" /xml \"C:\\Users\\admin\\AppData\\Local\\Temp\\tmp.tmp\"', $EventID: '1', $Image: 'C:\\Windows\\SysWOW64\\blabla.exe', $User: 'work\\admin'",
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
        "id": "c8846914b9644d1bff54155ce4d14ef82548c64655c9431ae94d56448bfc7424",
        "links": {
            "self": "https://www.virustotal.com/api/v3/sigma_analyses/c8846914b9644d1bff54155ce4d14ef82548c64655c9431ae94d56448bfc7424"
        },
        "type": "sigma_analysis"
    },
    "links": {
        "self": "https://www.virustotal.com/api/v3/files/c8846914b9644d1bff54155ce4d14ef82548c64655c9431ae94d56448bfc7424/sigma_analysis"
    },
    "meta": {
        "count": 1
    }
}
```

---

← [🔀 similar_files](file-object-similar-files.md) · [up](../README.md) · [🔀 submissions](file-object-submissions.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-sigma-analysis>.*
