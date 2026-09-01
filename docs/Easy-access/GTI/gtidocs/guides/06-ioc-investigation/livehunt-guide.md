---
title: "Livehunt"
source: https://gtidocs.virustotal.com/docs/livehunt-guide
slug: livehunt-guide
section: guides
group: "IOC Investigation"
updatedAt: 2025-09-25T02:39:54.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [IOC Investigation](README.md) › Livehunt

---

# livehunt

Livehunt allows you to hook into the stream of files analyzed by Google Threat Intelligence (Google TI) and get notified whenever one of them matches a certain rule written in the [YARA](https://virustotal.github.io/yara-x/) language. By applying YARA rules to the files analyzed by Google Threat Intelligence you should be able to get a constant flow of malware files classified by family, discover new malware files not detected by antivirus engines, collect files written in a given language or packed with a specific run-time packer, create heuristic rules to detect suspicious files, and, in general, enjoy the benefits of YARA's versatility acting on the huge amount of files processed by Google Threat Intelligence every day.

Livehunt applies your YARA rules to every file analyzed by Google Threat Intelligence, both when the file is submitted by some user, and when a file is re-analyzed. The difference between a submission and a re-analysis is that in the former case the user is in possession of the file and is uploading it to Google Threat Intelligence (not necessarily for the first time), in the latter case some existing file is being analyzed again. A submission always triggers an analysis, but files can be re-analyzed later without being submitted by a user.

If the file is a Portable Executable (PE) packed with some kind of run-time packer, it is unpacked and both the packed and unpacked versions of the file are scanned with YARA. When some file matches one of your rules, a notification is generated with details about the file and the matching rule.

Files that are larger than 100MB are not scanned by Livehunt at all.

# creating-livehunt-rules

Livehunt rules are organized into rulesets, which are simply a collection of YARA rules that share common settings, the total size of the rules in text form can not exceed 1MB. In order to create a new ruleset follow these steps:

1.  On the homepage, click on the **Livehunt** option in the **IoC Investigation** menu in the toolbar:

![Livehunt menu](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/livehunt_menu_icon_20240322.png)

2.  Then click on the **New Livehunt Ruleset** and choose the matching entity among files, URLs, IPs or domains:

![Livehunt New Ruleset](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/livehunt_new_20240322.png)

3.  A window will be opened with a text editor in which you can write your YARA rules and control its settings. The image below illustrates the usage of this window.

![Livehunt Editor](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/livehunt_editor_20240322.png)

1. Ruleset name.
2. You can use different templates or you can use a known file to create rules based on its attributes.
3. YARA rules
4. The matching entity.
5. You can share the ruleset to other members of the Google Threat Intelligence community.
6. The save rule button.
7. Enable/disable the ruleset. If the ruleset is disabled you won't receive any notifications from it.
8. Maximum number of notifications that you will receive from this ruleset in any given 24 hours period.
9. Add email addresses to receive notifications by email (one per line).
10. You can create a retrohunt job using this rule.
11. You can run tests of the ruleset among a list of specific hashes.

[Back to top](#top)

# livehunt-notifications

The [IOC Stream view](ioc-stream-guide.md) is an evolution to the previous Livehunt Notifications view. This view allows users to digest the incoming VT flux into relevant threat feeds that you can study here or easily export to improve detection in your security technologies.

You will see different tabs for different Threat Feeds. Please check our [IOC Stream view](ioc-stream-guide.md) for more details.

[Back to top](#top)

# writing-yara-rules-for-livehunt

Livehunt uses an up-to-date version of YARA, which means that the [latest YARA documentation](https://virustotal.github.io/yara-x/docs/intro/getting-started/) is usually the place to go for a detailed description of the language and its features. However, there are a few things that you need to know while creating YARA rules specifically tailored for Livehunt.

* Rules for which YARA raise performance warnings are not accepted by Livehunt. Such rules are usually very slow and degrade the service both for you and the rest of the users.
* You can not use **include** statements in your rules.
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
* **Important:** In addition to the standard modules enumerated above, you can also use the **vt** module. This module has been specifically created for Livehunt and Retrohunt and exposes additional information about the file being scanned. You can find more details about this in the following [article](livehunt-guide/writing-yara-rules-for-livehunt.md).

In the next links you will find more information on how to leverage the **vt** module for threat hunting:

> ⚠️
>
> The vt module always matches the last submission, i.e. the one that generated the YARA matching event.

* [File hunting](livehunt-guide/hunting-metadata.md)
* [Behavior hunting](livehunt-guide/hunting-behavior.md)
* [Network hunting](livehunt-guide/nethunt.md) ([examples](livehunt-guide/nethunt-examples.md))
* [Legacy vars](livehunt-guide/hunting-legacy-variables.md)
* [Reference](livehunt-guide/hunting-reference.md)

[Back to top](#top)

---

← [What's YARA Hunting?](whats-yara-hunting.md) · [up](README.md) · [Writing YARA rules for Livehunt](livehunt-guide/writing-yara-rules-for-livehunt.md) →

*Archived from <https://gtidocs.virustotal.com/docs/livehunt-guide>.*
