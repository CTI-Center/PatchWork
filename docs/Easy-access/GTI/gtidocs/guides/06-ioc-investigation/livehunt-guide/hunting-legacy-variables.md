---
title: "Legacy variables"
source: https://gtidocs.virustotal.com/docs/hunting-legacy-variables
slug: hunting-legacy-variables
section: guides
group: "IOC Investigation"
updatedAt: 2025-09-25T02:41:38.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [IOC Investigation](../README.md) › [Livehunt](../livehunt-guide.md) › Legacy variables

---

# legacy-variables

## legacy-variables-(deprecated)

YARA offers a mechanism for [defining custom variables](https://virustotal.github.io/yara-x/docs/writing_rules/external-global-variables/) that has been used in Livehunt for providing additional information about the file being scanned. These variables are now deprecated in favor of our **vt**, they will continue to work as always for backward compatibility. You can find list of variables defined by Livehunt below, but we highly encourage you to start using the **vt** module instead.

| Deprecated Variable | vt.metadata mapping                   |                                                                                                                                                                 |
| ------------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| file\_name          | vt.metadata.file\_name                |                                                                                                                                                                 |
| file\_type          | vt.metadata.file\_type                | string becomes a [reference](hunting-reference.md#file-types), to replicate previous functionality for "doc" you could use vt.FileType.DOC                     |
| imphash             | vt.metadata.imphash                   |                                                                                                                                                                 |
| md5                 | vt.metadata.md5                       |                                                                                                                                                                 |
| new\_file           | vt.metadata.new\_file                 |                                                                                                                                                                 |
| positives           | vt.metadata.analysis\_stats.malicious |                                                                                                                                                                 |
| sha256              | vt.metadata.sha256                    |                                                                                                                                                                 |
| sha1                | vt.metadata.sha1                      |                                                                                                                                                                 |
| signatures          | vt.metadata.signatures                | string becomes a dictionary, to replicate previous functionality you could use: for any engine, signature in vt.metadata.signatures : ( signature contains "x") |
| submissions         | vt.metadata.times\_submitted          |                                                                                                                                                                 |
| ssdeep              | vt.metadata.ssdeep                    |                                                                                                                                                                 |
| tags                | vt.metadata.tags                      | string becomes a dictionary, to replicate previous functionality you could use: for any tag in vt.metadata.tags : ( tag == "signed" )                           |
| vhash               | vt.metadata.vhash                     |                                                                                                                                                                 |

[Back to top](#legacy-variables)

---

← [Reference](hunting-reference.md) · [up](../README.md) · [Retrohunt](../retrohunt-guide.md) →

*Archived from <https://gtidocs.virustotal.com/docs/hunting-legacy-variables>.*
