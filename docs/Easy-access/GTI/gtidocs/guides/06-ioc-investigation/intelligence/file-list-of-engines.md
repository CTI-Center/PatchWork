---
title: "File - List of Engines"
source: https://gtidocs.virustotal.com/docs/file-list-of-engines
slug: file-list-of-engines
section: guides
group: "IOC Investigation"
updatedAt: 2025-09-26T10:25:44.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [IOC Investigation](../README.md) › [Intelligence / Web searching](../intelligence.md) › File - List of Engines

---

# file---list-of-engines

The main [search box](https://www.virustotal.com/gui/home/search) also allows you to specify a full or partial malware family name ([Backdoor.Win32.PcClient!IK](https://www.virustotal.com/gui/search/%2522Backdoor.Win32.PcClient!IK%2522/files), [Sality](https://www.virustotal.com/gui/search/sality/files), [Mydoom.R](https://www.virustotal.com/gui/search/Mydoom.R)), or any other text you want to find inside the antivirus reports. However, this kind of search will look at all indexed fields for the file, it will not only focus on the antivirus results. In order to focus exclusively on the antivirus results (no matter which particular engine produced the output), you should use the *engines* prefix. For example: [engines:"Trojan.Isbar"](https://www.virustotal.com/gui/search/engines%253A%2522Trojan.Isbar%2522/files) or [engines:"zbot"](https://www.virustotal.com/gui/search/engines%253A%2522zbot%2522).

<img
  src="https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/intelligence/images/identifyingantivirus_engines_20240503.png"
  alt="Identifying Antivirus Engines"
  style={{ display: 'block', margin: '0 auto' }}
/>

If you are looking for files detected by some specific antivirus vendor you can make use of vendor prefixes. These prefixes should precede your keyword in order to restrict the scope of the search to a particular antivirus solution, for example: [symantec:infostealer](https://www.virustotal.com/gui/search/symantec%253Ainfostealer/files), [mcafee:rahack](https://www.virustotal.com/gui/search/mcafee%253Arahack/files), [f-secure:virut](https://www.virustotal.com/gui/search/f-secure%253Avirut/files).

<img
  src="https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/intelligence/images/identifyingantivirus_symantec_20240503.png"
  alt="Identifying Antivirus Symantec"
  style={{ display: 'block', margin: '0 auto' }}
/>

By using vendor prefixes you can also search for all files detected by a given vendor, independently of the malware name. To do this you must write the vendor prefix followed by the special keyword *infected*, e.g. [ESET-NOD32:infected](https://www.virustotal.com/gui/search/ESET-NOD32%253Ainfected/files). In this case, the word infected does not necessarily have to be present in the antivirus signature, it is just indicating that the file must be detected. Similarly, you can list all files not detected by some antivirus by using the keyword *clean*. For example: [ESET-NOD32:clean](https://www.virustotal.com/gui/search/ESET-NOD32%253Aclean/files).

<img
  src="https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/intelligence/images/identifyingantivirus_clean_20240503.png"
  alt="Identifying Antivirus Clean"
  style={{ display: 'block', margin: '0 auto' }}
/>

This is the full list of allowed vendor prefixes:

|                   |                  |                       |                       |
| :---------------- | :--------------- | :-------------------- | :-------------------- |
| acronis           | ad\_aware        | aegislab              | ahnlab                |
| ahnlab\_v3        | alibaba          | alibabacloud          | alyac                 |
| antivir           | antivir7         | antiy\_avl            | apex                  |
| arcabit           | avast            | avast\_mobile         | avg                   |
| avira             | avware           | babable               | baidu                 |
| bitdefender       | bitdefenderfalx  | bitdefendertheta      | bkav                  |
| bkav\_pro         | cat\_quickheal   | clamav                | cmc                   |
| commtouch         | comodo           | crowdstrike           | cybereason            |
| cylance           | cynet            | cyren                 | deepinstinct          |
| drweb             | egambit          | elastic               | emsisoft              |
| endgame           | escan            | eset\_nod32           | f\_prot               |
| f\_secure         | fireeye          | fortinet              | gdata                 |
| google            | gridinsoft       | ikarus                | invincea              |
| jiangmin          | k7antivirus      | k7gw                  | kaspersky             |
| kingsoft          | lionic           | malwarebytes          | max                   |
| maxsecure         | mcafee           | mcafee\_gw\_edition   | microsoft             |
| microworld\_escan | nano\_antivirus  | nod32                 | nprotect              |
| paloalto          | panda            | prevx1                | qihoo\_360            |
| rising            | sangfor          | sentinelone           | sophos                |
| sunbelt           | superantispyware | symantec              | symantecmobileinsight |
| tachyon           | tencent          | thehacker             | totaldefense          |
| trapmine          | trendmicro       | trendmicro\_housecall | trustlook             |
| varist            | vba32            | vipre                 | virit                 |
| virobot           | webroot          | whitearmor            | yandex                |
| zillya            | zonealarm        | zoner                 |                       |

The list is subject to changes as new antivirus solutions are integrated in Google Threat Intelligence and existing ones change names so do not forget to visit it every once in a while.

[Back to Top](#top)

---

← [Full list of Google Threat Intelligence behaviour_tags modifier](full-list-of-google-threat-intelligence-behaviour_tags-modifier.md) · [up](../README.md) · [Reports search modifiers](reports-search-modifiers.md) →

*Archived from <https://gtidocs.virustotal.com/docs/file-list-of-engines>.*
