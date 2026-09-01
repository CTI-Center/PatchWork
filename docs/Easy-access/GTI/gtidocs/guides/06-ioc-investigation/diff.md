---
title: "Diff"
source: https://gtidocs.virustotal.com/docs/diff
slug: diff
section: guides
group: "IOC Investigation"
updatedAt: 2025-09-25T02:41:47.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [IOC Investigation](README.md) › Diff

---

# diff

DIFF helps threat analysts in creating YARA rules by automating the identification optimal patterns to detect groups of files (malware families, threat campaigns, threat actor toolset). These patterns can be used in [Livehunt](livehunt-guide.md) YARA rules, [Retrohunt](retrohunt-guide.md) jobs and [GREP](intelligence/content-search-grep.md) content searches. 

**What do you mean by optimal?** DIFF takes into account binary sequence prevalence across the entire Google Threat Intelligence dataset in order to make sure it does not suggest patterns that are shared by a large number of files, e.g. the DOS stub in portable executables: "*The program Cannot be run in DOS mode*". In other words, DIFF tries to generate patterns that will not produce false positives. 

Answers to other frequently asked questions can be found in the [Diff FAQ](diff/how-does-diff-work.md) section.

# accessing-diff

DIFF has two main entry points. Given a **Enterprise file search, you can select a group of files** by acting on their checkboxes, this will activate the DIFF button in the tools menu:

![Diff send](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/vtdiff_send_20240402.png)

You can also get to DIFF by using the **left navigation bar** in Enterprise:

![Diff navigation bar](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/vtdiff_navigationbar_20240402.png)

This will then take you to your historical DIFFs view, where you can set up a new session:

![Diff new session](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/vtdiff_newsession_20240402.png)

A session modal will open up allowing you to specify a list of hashes to match and also a list of hashes to exclude, that will fine tune your job:

![Diff send](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/vtdiff_createsession_20240402.png)

# enterprise-search-list-workflow

Let’s imagine our starting point is a single hash, a malicious document that drops second stage payload via macros. The hash is:

[45cfff04a95b3c40e2e8ee4b9c9ae1e75448f27eb119c079973e8a4b4459c930](https://www.virustotal.com/gui/file/45cfff04a95b3c40e2e8ee4b9c9ae1e75448f27eb119c079973e8a4b4459c930/detection)

In order to be able to build an optimal rule to detect this file and other variants of the same campaign/family we first need to identify a collection of files belonging to such family. 

We can pinpoint other variants by making use of the different clustering mechanisms that Google Threat Intelligence provides ([vhash, imphash, ssdeep, icon/thumbnail vizhash, antivirus labels, distinctive static properties, etc.](intelligence/file-search-modifiers.md)). In this case we are going to pivot to other documents with the exact same visual layout by clicking on the file’s thumbnail:

![VTDiff thumbnail](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/vtdiff_thumbnail_20240402.png)

This will trigger the following search:

<https://www.virustotal.com/gui/search/main_icon_dhash:7e12021282222000/files>

By hovering over the detection ratio you will see that the antivirus labels do indeed confirm that the matches belong to the same malware family. Similarly, the thumbnail of the files in the list clearly indicate that they have the very same visual layout. 

Select the first 8 matches:

![Diff checkboxes](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/vtdiff_checkboxes_20240402.png)

When you do so, the DIFF icon in the tools menu bar activates itself:

![Diff send](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/vtdiff_send2_20240402.png)

Click on it in order to set up a DIFF session for those hashes. Commonly abused file types such as documents do not require you to provide a list of hashes to exclude, the backend will set up an exclusion list automatically. **If you want to refine the DIFF session and avoid false positives produced in previous DIFF jobs, you can use the exclusion list**.

![Diff exclusion list](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/vtdiff_exclusion_20240402.png)

Launch the session. A DIFF job generally takes under a minute to conclude. Note that this is a heavy process, DIFF will iterate over all files provided with sliding windows of different sizes, checking whether binary subsequences are common to the selection and whether these are not too noisy when considering the entire Google Threat Intelligence dataset.

A list of binary patterns will be produced:

![Diff patterns](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/vtdiff_patterns_20240402.png)

Note that you can click on the search icon next to each binary pattern in order to trigger an n-gram [content search](intelligence/content-search-grep.md) for it:

![Diff vtgrep](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/vtdiff_vtgrep_20240402.png)

This will allow you to understand the kind of files that match each pattern and whether they are prone to false positives. You can also easily search for an AND combination of some of them, which will probably be far more effective than an individual search. Select the first three patterns and click on the 'Launch a GREP content search' option in the Tools menu bar:

![Diff patterns search](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/vtdiff_patternssearch_20240402.png)

That will trigger for files that contain those 3 binary patterns. Google Threat Intelligence maintains a 5PB n-gram index to power lightning-fast content searches:

<https://www.virustotal.com/gui/search/content:%7BF95F6482C9A84C7ECF0E2ACF43E422397578580CBA4D5BA8A23CD76E1DA9105538BA68249AB0CC2D359E76AF9A164392EBDBAF6543A5DAEBA8E72183BA84119A%7D%20AND%20content:%7B62463C65465A7A464C66467C6827446746%7D%20AND%20content:%7B776F72642F6D656469612F696D616765312E746966%7D>

![VTDiff thumbnails](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/vtdiff_thumbnails_20240405.png)

Judging by the thumbnails, sizes, antivirus results, tags, etc. it is clear that those three binary patterns have done a good job at finding other variants of the family/campaign. It is now clear that these patterns can be used to build a YARA rule or Retrohunt to either be notified of any new future file upload that belongs to this family or to map out the entire historical campaign. Livehunt YARA rules and Retrohunt jobs can also be set up using the top actions menu in DIFF listings:

![VTDiff hunting](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/vtdiff_hunting_20240403.png)

One last word, note that the top actions menu also allows you to filter the patterns in order to focus exclusively on certain categories:

![VTDiff filter](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/vtdiff_filter_20240403.png)

 

# hash-list-workflow

Sometimes you might want to create a DIFF session based on a list of pre-existing hashes, your starting point will no longer be a Google Threat Intelligence search. In these cases you will use the navigation sidebar to access directly access DIFF:

![Diff navbar](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/vtdiff_navbar_20240403.png)

The landing page allows you to create a new DIFF session. This requires you to copy\&paste the list of hashes to match in the inclusion text area.

![Diff hashes](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/images/vtdiff_hashes_20240403.png)

**Exclusion hash lists will only be needed for less prevalent file types, however, even if exclusions are not required, you might often want to set up your own selection in order to filter out files that match previous iterations of a DIFF job that caused false positives.**

Note that the DIFF landing site lists the historical DIFF jobs that you launched in the past, this allows you to continue working with the identified patterns at a later stage and can come in handy if you mistakenly closed the browser tab.

From this point onward the workflow is exactly the same as the one described in the [previous section](#vt-enterprise-search-list-workflow).

To learn more about DIFF please refer to the [Frequently Asked Questions](diff/how-does-diff-work.md).

---

← [Sources Subscriptions](ioc-stream-guide/sources-subscriptions.md) · [up](README.md) · [How does Diff work?](diff/how-does-diff-work.md) →

*Archived from <https://gtidocs.virustotal.com/docs/diff>.*
