---
title: "Sigma Rules"
source: https://gtidocs.virustotal.com/reference/sigma-rule-object
slug: sigma-rule-object
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T02:14:48.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Sigma Rules

---

# sigma-rules

Sigma rules matched in Sigma analyses

A Sigma rule object contains a Sigma rule used during a [Sigma Analysis](sigma-analyses-object.md). For more information check the [Sigma wiki](https://github.com/SigmaHQ/sigma/wiki/Rule-Creation-Guide). It contains the following attributes:

* `description`: <*string*>: brief description about what the rule is detecting.
* `detections`: <*dictionary*> defines detection patterns and conditions.
* `false_positives`: <*list of strings*>: list of known false positives.
* `fields`: <*list of strings*>: fields that are helpful in the evaluation of a certain event.
* `level`: <*string*> can be either "low", "medium", "high" or "critical".
* `log_source`: <*string*> rule's log source.
* `references`: <*list of strings*>: external links to get more context about what is the rule detecting.
* `source`: <*string*> ruleset source.
* `status`: <*string*>: can be either "experimental" for new rules or "stable" for rules that have been running in production for a couple of months.
* `tags`: <*string*> rule tags.
* `title`: <*string*> rule title.

```json Sigma rule objects
{
  "data": {
    "attributes": {
      "description": "<string>",
      "detection": {
        "condition": "<string>",
        "details": {
          "<string>": "<string>"
        }
      },
      "false_positives": [
        "<string>"
      ],
      "fields": [
        "<string>"
      ],
      "level": "<string>",
      "log_source": {
        "category": "<string>",
        "definition": "<string>",
        "product": "<string>",
        "service": "<string>"
      },
      "references": [
        "<string>"
      ],
      "source": "<string>",
      "status": "<string>",
      "tags": [
        "<string>"
      ],
      "title": "<string>"
    },
    "id": "<string>",
    "links": {
      "self": "https://www.virustotal.com/api/v3/sigma_rules/<id>"
    },
    "type": "sigma_rule"
  }
}
```
```json Example
{
  "data": {
    "attributes": {
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
    "id": "5c3ea6806114163b8cdf5735aeb07e702ab63e0e486f721df84cf675e2b0a04b",
    "links": {
      "self": "https://www.virustotal.com/api/v3/sigma_rules/5c3ea6806114163b8cdf5735aeb07e702ab63e0e486f721df84cf675e2b0a04b"
    },
    "type": "sigma_rule"
  }
}
```

---

← [🔀 rules](sigma-analyses-object/sigma-analyses-object-rules.md) · [up](README.md) · [Software and Toolkit](software-toolkit-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/sigma-rule-object>.*
