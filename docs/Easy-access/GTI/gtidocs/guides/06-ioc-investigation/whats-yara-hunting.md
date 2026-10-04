---
title: "What's YARA Hunting?"
source: https://gtidocs.virustotal.com/docs/whats-yara-hunting
slug: whats-yara-hunting
section: guides
group: "IOC Investigation"
updatedAt: 2025-09-25T00:22:47.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [IOC Investigation](README.md) › What's YARA Hunting?

---

# what's-yara-hunting?

YARA Hunting is a service that leverages the power of [YARA](https://virustotal.github.io/yara-x/) over Google Threat Intelligence's dataset, it consists of three different components: [Livehunt](livehunt-guide.md), [Retrohunt](retrohunt-guide.md) and [DIFF](diff.md). If you have never used YARA before we recommend you to start by reading the [YARA documentation](https://virustotal.github.io/yara-x/docs/intro/getting-started/).

**[Livehunt](livehunt-guide.md)** allows you to hook into the stream of files submitted to Google Threat Intelligence and to get notified whenever one of them matches your rules. By matching the submitted files with YARA you should be able to (1) get a constant flow of malware files classified by family, (2) discover new malware flying under the industry's radar, (3) collect files written in a given language or packed with a specific run-time packer, (4) create heuristic rules to detect suspicious files, (5) track threat actors, and, in general, enjoy the benefits of YARA's versatility acting on the huge amount of files processed by Google Threat Intelligence every day.

Besides hunting for files in real time as they arrive to Google Threat Intelligence, you can also apply your YARA rules to the historical collection of files with **[Retrohunt](retrohunt-guide.md)**. A Retrohunt job takes around \~3-4 hours to complete and scans over 600TB of files sent to Google Threat Intelligence during the past year.

Last, **[DIFF](diff/how-does-diff-work.md)** eases the task of creating YARA rules. It allows you to provide a collection of hashes that you are interested in matching and a collection of hashes that you do not want to match at all and it will generate common binary subsequences that are shared by your selection. VTDIFF takes into account binary sequence prevalence across the entire Google Threat Intelligencel dataset in order to make sure it does not suggest noisy patterns that may produce false positives.

These hunting components can be automated using the [Google Threat Intelligence API v3](https://gtidocs.readme.io/reference/list-hunting-rulesets).

---

← [Saved Searches](saved-searches-guide.md) · [up](README.md) · [Livehunt](livehunt-guide.md) →

*Archived from <https://gtidocs.virustotal.com/docs/whats-yara-hunting>.*
