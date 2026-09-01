---
title: "🔀 rules"
source: https://gtidocs.virustotal.com/reference/sigma-analyses-object-rules
slug: sigma-analyses-object-rules
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:44:44.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Sigma Analyses](../sigma-analyses-object.md) › 🔀 rules

---

# 🔀-rules

Matched rules in a Sigma analysis.

> 🚧 DEPRECATED
>
> Sigma analyses metadata is now included in both the File and File behaviour objects.

The *rules* relationship returns a list of ***all matched rules for a given analysis***.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/files/files-relationships.md) and contains a list of [Sigma Rule](../sigma-rule-object.md) objects.

```json Sigma analysis
{
  "data": [
    <SIGMA_RULE_OBJECT>,
    <SIGMA_RULE_OBJECT>,
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
                "action": "",
                "author": "Sami Ruohonen",
                "description": "Detects usage of attrib.exe to hide files from users.",
                "detection": {
                    "condition": "selection and not (ini or intel)",
                    "details": {
                        "ini": "{\"CommandLine\":\"*\\\\desktop.ini *\"}",
                        "intel": "{\"CommandLine\":\"+R +H +S +A \\\\\\\\*.cui\",\"ParentCommandLine\":\"C:\\\\WINDOWS\\\\system32\\\\\\\\*.bat\",\"ParentImage\":\"*\\\\cmd.exe\"}",
                        "selection": "{\"CommandLine\":\"* +h *\",\"Image\":\"*\\\\attrib.exe\"}"
                    }
                },
                "false_positives": [
                    "igfxCUIService.exe hiding *.cui files via .bat script (attrib.exe a child of cmd.exe and igfxCUIService.exe is the parent of the cmd.exe)",
                    "msiexec.exe hiding desktop.ini"
                ],
                "fields": [
                    "CommandLine",
                    "ParentCommandLine",
                    "User"
                ],
                "level": "low",
                "log_source": {
                    "category": "process_creation",
                    "definition": "",
                    "product": "windows",
                    "service": ""
                },
                "references": [],
                "source": "Sigma Integrated Rule Set (GitHub)",
                "status": "experimental",
                "tags": [],
                "title": "Hiding Files with Attrib.exe"
            },
            "context_attributes": {
                "match": "$CommandLine: 'attrib  +H monitor.bak', $EventID: '1', $Image: 'C:\\Windows\\System32\\attrib.exe', $ParentCommandLine: 'C:\\Windows\\system32\\cmd.exe /c attrib +H monitor.bak'"
            },
            "id": "5c3ea6806114163b8cdf5735aeb07e702ab63e0e486f721df84cf675e2b0a04b",
            "links": {
                "self": "https://www.virustotal.com/api/v3/sigma_rules/5c3ea6806114163b8cdf5735aeb07e702ab63e0e486f721df84cf675e2b0a04b"
            },
            "type": "sigma_rule"
        },
        {
            "attributes": {
                "action": "",
                "author": "Sami Ruohonen",
                "description": "Detects usage of attrib.exe to hide files from users.",
                "detection": {
                    "condition": "selection and not (ini or intel)",
                    "details": {
                        "ini": "{\"CommandLine\":\"*\\\\desktop.ini *\"}",
                        "intel": "{\"CommandLine\":\"+R +H +S +A \\\\\\\\*.cui\",\"ParentCommandLine\":\"C:\\\\WINDOWS\\\\system32\\\\\\\\*.bat\",\"ParentImage\":\"*\\\\cmd.exe\"}",
                        "selection": "{\"CommandLine\":\"* +h *\",\"Image\":\"*\\\\attrib.exe\"}"
                    }
                },
                "false_positives": [
                    "igfxCUIService.exe hiding *.cui files via .bat script (attrib.exe a child of cmd.exe and igfxCUIService.exe is the parent of the cmd.exe)",
                    "msiexec.exe hiding desktop.ini"
                ],
                "fields": [
                    "CommandLine",
                    "ParentCommandLine",
                    "User"
                ],
                "level": "low",
                "log_source": {
                    "category": "process_creation",
                    "definition": "",
                    "product": "windows",
                    "service": ""
                },
                "references": [],
                "source": "Sigma Integrated Rule Set (GitHub)",
                "status": "experimental",
                "tags": [],
                "title": "Hiding Files with Attrib.exe"
            },
            "context_attributes": {
                "match": "$CommandLine: 'attrib  +H window_texts.txt', $EventID: '1', $Image: 'C:\\Windows\\System32\\attrib.exe', $ParentCommandLine: 'C:\\Windows\\system32\\cmd.exe /c attrib +H window_texts.txt'"
            },
            "id": "5c3ea6806114163b8cdf5735aeb07e702ab63e0e486f721df84cf675e2b0a04b",
            "links": {
                "self": "https://www.virustotal.com/api/v3/sigma_rules/5c3ea6806114163b8cdf5735aeb07e702ab63e0e486f721df84cf675e2b0a04b"
            },
            "type": "sigma_rule"
        }
    ],
    "links": {
        "next": "https://www.virustotal.com/api/v3/sigma_analyses/c88c691ab968bd1bff58155ce1d18ef82558c6a655c9c31ae9bd564b8bfc7424/rules?cursor=STIKLg%3D%3D&limit=2",
        "self": "https://www.virustotal.com/api/v3/sigma_analyses/c88c691ab968bd1bff58155ce1d18ef82558c6a655c9c31ae9bd564b8bfc7424/rules?limit=2"
    },
    "meta": {
        "count": 4,
        "cursor": "STIKLg=="
    }
}
```

---

← [Sigma Analyses](../sigma-analyses-object.md) · [up](../README.md) · [Sigma Rules](../sigma-rule-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/sigma-analyses-object-rules>.*
