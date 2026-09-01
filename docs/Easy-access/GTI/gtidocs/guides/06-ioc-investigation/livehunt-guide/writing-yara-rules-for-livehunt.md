---
title: "Writing YARA rules for Livehunt"
source: https://gtidocs.virustotal.com/docs/writing-yara-rules-for-livehunt
slug: writing-yara-rules-for-livehunt
section: guides
group: "IOC Investigation"
updatedAt: 2025-09-25T02:39:58.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [IOC Investigation](../README.md) › [Livehunt](../livehunt-guide.md) › Writing YARA rules for Livehunt

---

# writing-yara-rules-for-livehunt

Livehunt uses an up-to-date version of YARA, which means that the [latest YARA documentation](https://virustotal.github.io/yara-x/docs/intro/getting-started/) is usually the place to go for a detailed description\
of the language and its features. However, there are a few things that you need to know while creating YARA rules specifically tailored for Livehunt.

* Rules for which YARA raise performance warnings are not accepted by Livehunt. Such rules are usually very slow and degrade the service both for you and the rest of the users.
* You can not use **include** statements in your rules.
* Standard modules currently supported are:
  * [**pe**](https://virustotal.github.io/yara-x/docs/modules/pe/)
  * [**elf**](https://virustotal.github.io/yara-x/docs/modules/elf/)
  * [**dotnet**](https://virustotal.github.io/yara-x/docs/modules/dotnet/)
  * [**lnk**](https://virustotal.github.io/yara-x/docs/modules/lnk/)
  * [**macho**](https://virustotal.github.io/yara-x/docs/modules/macho/)
  * [**math**](https://virustotal.github.io/yara-x/docs/modules/math/)
  * [**magic**](https://yara.readthedocs.io/en/latest/modules/magic.html)
  * [**hash**](https://virustotal.github.io/yara-x/docs/modules/hash/)
  * [**string**](https://virustotal.github.io/yara-x/docs/modules/string/)
  * [**time**](https://virustotal.github.io/yara-x/docs/modules/time/)

## the-*vt*-module

In order to expose all the information that Google Threat Intelligence have about the file being scanned we have created a custom YARA module named **vt**. This module contains metadata like antivirus signatures, file type, file behavior, submitter, etc. The **vt** module replaces the previous mechanism for exposing file's metadata based in custom variables like **signatures**, **positives**, **file\_name**, and so on. These variables have been deprecated and you can migrate to the vt module using the [legacy variables guide](hunting-legacy-variables.md).

> ⚠️
>
> The vt module always matches the last submission, i.e. the one that generated the YARA matching event.

```cplusplus
import "vt"
rule new_infected_pe {
  condition:
    vt.metadata.new_file and
    vt.metadata.analysis_stats.malicious > 1 and
    vt.metadata.file_type == vt.FileType.PE_EXE
}
```

```cplusplus
import "vt"
rule behavior_evasion {
  condition:
    for any catalog in vt.behaviour.mbc: (
      catalog.behavior == "Dynamic Analysis Evasion"
    )
}
```

```cplusplus
import "vt"
rule LilithBot {
  condition:
    vt.net.url.raw matches /\/gate\/.{60}\/registerBot/ or
    vt.net.url.raw matches /\/gate\/.{60}\/getFile\?name=admin_settings_plugin\.json/ or
    vt.net.url.raw matches /\/gate\/.{60}\/uploadFile\?name/
}
```

From the examples above you probably already got the idea. The **vt** module has a lot of information about the file or network resource being scanned, and that information can be used in your Livehunt rules for filtering unwanted files or network analyses and focusing in what you are really looking for. You are not limited to creating rules based on file content alone, there is a lot of metadata at your disposal.

The **vt** module is divided in three submodules that allows you to create rules that expose most of information that can be found in the platform:

* [vt.metadata](hunting-metadata.md) for file metadata
* [vt.behaviour](hunting-behavior.md) for file behaviour
* [vt.net](nethunt.md) for URLs, Domains and IP addresses

---

← [Livehunt](../livehunt-guide.md) · [up](../README.md) · [File hunting](hunting-metadata.md) →

*Archived from <https://gtidocs.virustotal.com/docs/writing-yara-rules-for-livehunt>.*
