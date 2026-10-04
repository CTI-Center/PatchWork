---
title: "Retrohunt"
source: https://gtidocs.virustotal.com/docs/retrohunt-guide
slug: retrohunt-guide
section: guides
group: "IOC Investigation"
updatedAt: 2026-02-11T11:27:49.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [IOC Investigation](README.md) › Retrohunt

---

# retrohunt

Retrohunt allows you to scan the files sent to Google Threat Intelligence in the past 12 months with your YARA rules (the 12 months limit applies to users of Hunting Pro, for standard users the limit is 3 months). Files that are larger than 100MB are not scanned by Retrohunt at all. A Retrohunt job scans a corpus of more than 500M files (\~680TB worth of data) in 2-3 hours and reports you the files that matches your rules. However, the matches are limited to 10.000 per job. 

Also, you can scan a fixed and smaller corpus composed of about 1 million files that are known to be goodware, which is handy when you are testing your YARA rules, as it can help you to spot false-positives. These jobs usually finish in less than a minute.

Retrohunt jobs can't have more than 300 YARA rules and the total size of the rules in text form can not exceed 1MB. A limit of 10 concurrent jobs per user is also enforced.

The standard YARA modules currently supported by Retrohunt are:

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

**Important:** In addition to the standard modules enumerated above, you can also the **vt** module, module. This module has been specifically created for Livehunt and Retrohunt and exposes additional information about the file being scanned. You can find more details about this in the following [article](livehunt-guide/writing-yara-rules-for-livehunt.md).

# creating-a-retrohunt-job

1.  On the homepage, click on the **Retrohunt** option in the **IoC Investigation** menu in the toolbar:

![Retrohunt menu](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/retrohunt_menu_icon_20240325.png)

 2.  Then click on the **New retrohunt job**.

![Retrohunt new job](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/retrohunt_new_20240325.png)

3.  A window will be opened with a text editor in which you can write your YARA rules and control its settings. The image below illustrates the usage of this window.

![Retrohunt editor](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/retrohunt_editor_20240325.png)

 

1. Return to retrohunt dashboard.
2. You can use different templates or you can use a known file to create rules based on its attributes.
3. YARA rules.
4. Create job button.
5. Corpus that is going to be scanned with your rules.
6. Time range (referred to last submission date).
7. Notification email.
8. You can run tests of the ruleset among a list of specific hashes.

 

# retrohunt-results

![Retrohunt results](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/retrohunt_results_20240417.png)

1. Progress indicator.
2. Job status: Starting, Running, Aborted or Finished.
3. Number of matches found. Click on the number to see the files.
4. Button to download list of matches.
5. Cancel/Delete job.

If you don't have Hunting Pro, you'll see the number of additional matches that you would be able to see with it (i.e. matches on files that have been submitted to Google Threat Intelligence more than 3 months ago).

---

← [Legacy variables](livehunt-guide/hunting-legacy-variables.md) · [up](README.md) · [IoC Stream](ioc-stream-guide.md) →

*Archived from <https://gtidocs.virustotal.com/docs/retrohunt-guide>.*
