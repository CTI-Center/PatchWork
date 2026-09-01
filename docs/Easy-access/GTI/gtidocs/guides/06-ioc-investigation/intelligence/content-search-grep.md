---
title: "Content search (Grep)"
source: https://gtidocs.virustotal.com/docs/content-search-grep
slug: content-search-grep
section: guides
group: "IOC Investigation"
updatedAt: 2025-09-26T10:23:52.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [IOC Investigation](../README.md) › [Intelligence / Web searching](../intelligence.md) › Content search (Grep)

---

# content-search-(grep)

VTGrep supports several of the content-related features in YARA. Some example valid content search queries are:

|                                 |                                                                                                                                                                                                                                                           |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Escaped UTF-8 (including ASCII) | [content:"résumé", \x22\x45\x64"](https://www.virustotal.com/gui/search/content%253A%2522r%25C3%25A9sum%25C3%25A9%255C%2522%252C%2520%255Cx22%255Cx45%255Cx64%2522/files)                                                                                 |
| Hexadecimal                     | [content:\{CAFEBABE}](https://www.virustotal.com/gui/search/content%253A%257BCAFEBABE%257D/files)                                                                                                                                                         |
| AND                             | [content:"Hello World!" content:\{CAFEBABE}](https://www.virustotal.com/gui/search/content%253A%2522Hello%2520World!%2522%2520content%253A%257BCAFEBABE%257D/files)                                                                                       |
| OR                              | [content:"This program cannot be run in DOS mode" OR content:\{CAFEBABE}](https://www.virustotal.com/gui/search/content%253A%2522This%2520program%2520cannot%2520be%2520run%2520in%2520DOS%2520mode%2522%2520OR%2520content%253A%257BCAFEBABE%257D/files) |
| Content at specific offset      | [content:\{CA FE BA BE}@0](https://www.virustotal.com/gui/search/content%253A%257BCA%2520FE%2520BA%2520BE%257D%25400/files)                                                                                                                               |
| Starting within an offset range | [content:\{CAFEBABE}@0-10](https://www.virustotal.com/gui/search/content%253A%257BCA%2520FE%2520BA%2520BE%257D%25400-10/files)                                                                                                                            |
| With hexadecimal offsets        | [content:\{CAFEBABE}@0x00-0x0A](https://www.virustotal.com/gui/search/content%253A%257BCAFEBABE%257D%25400x00-0x0A/files)                                                                                                                                 |
| ?? wildcards                    | [content:\{686f6c61 ?? 6d756e646f}](https://www.virustotal.com/gui/search/content%253A%257B686f6c61%2520%253F%253F%25206d756e646f%257D/files)                                                                                                             |
| Variable length wildcards       | [content:\{CAFEBABE \[1-100\] 686F6C61}](https://www.virustotal.com/gui/search/content%253A%257BCAFEBABE%2520%255B1-100%255D%2520686F6C61%257D/files)                                                                                                     |
| Alternatives                    | [content:\{686F6C6120(6d756e646f)}](https://www.virustotal.com/gui/search/content%253A%257B686F6C6120\(6d756e646f\)%257D/files)                                                                                                                           |

Strings within double quotes are handled as UTF-8 strings [escaped as Python string literals](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals) (e.g., "\n" is a newline, """ is a double quote, "\\" is a single backslash, …). Because of this escaping, Windows paths are particularly tricky so either escape the backlashes accordingly or write the query in hexadecimal. As an example, "C:\Windows\System32" can either be content:"C:\*\*\\**Windows**\\\*\*System32" or content:\{43 3a 5c 57 69 6e 64 6f 77 73 5c 53 79 73 74 65 6d 33 32}.

All strings in VTGrep are case-sensitive. If you need case-insensitive, you need to work around it with ORs. Example: content:Windows OR content:windows OR content:WINDOWS.

You can see a snippet of the file being matched if you hover over the eye icon on the left hand-side.

![VTGrep Matches](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/intelligence/images/vtgrep_matches_20240423.png)

Furthermore, VT-Grep not only matches the raw content of the file, but it also searches over uncompressed and unpacked files plus VBA Code streams.

Matches in subfiles are still reported with the hash of their respective parent files, so you'll need to extract the subfiles manually if you want to find the match (other than see it in the Match context hover-over box).

**The following caveats apply to content search queries:**

* Results cannot be sorted.
* Files submitted in the last 24 to 48h are not yet indexed. Consider using [Hunting](../whats-yara-hunting.md) if you need the freshest results.
* Can only be combined with the following search modifiers:
  * size
  * type
  * fs
  * ls
  * imphash
  * positives
  * tag
  * submissions
* *content* and other search modifiers cannot be combined with an *OR* operator. However, combining other modifiers between them with an *OR* is OK. See examples below.

|               |                                                                                                                                                                                                                                  |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Valid**     | [*content:"Hello World! type:peexe*](https://www.virustotal.com/gui/search/content%253A%2522Hello%2520World!%2522%2520type%253Apeexe/files)                                                                                      |
| **Not valid** | *content:"Hello World!" OR positives:10*                                                                                                                                                                                         |
| **Valid**     | [*content:"Hello World!"  (type:peexe OR type:pedll) tag:overlay*](https://www.virustotal.com/gui/search/content%253A%2522Hello%2520World!%2522%2520%2520\(type%253Apeexe%2520OR%2520type%253Apedll\)%2520tag%253Aoverlay/files) |

VTGrep leverages rare substrings to quickly narrow down content searches and find matches among petabytes of data. Conversely, *extremely common substrings* are impractical to index. The content query is cut into substrings trying to avoid such extremely common substrings but this is sometimes not possible (e.g., at the extremes of the query or when the extremely common substring is too long) and may affect the results. Content searches with unavoidable extremely common substrings either have a) partial matches (where a small percentage of the characters may not match the query) or b) empty results. A warning will be shown in either case:

1. No more results found due to unselective query.
2. No more results found due to unselective query. Try avoiding extremely common substrings: "http", "[www](http://www)."

In case 1, VT-Grep couldn't zero in on any rare query substring and timed out. This can happen even if there are no matches for the whole query. A simple retry or extending the query at the extremes may work but it's normally better just to search for something rarer.

Fixing case 2 is simpler because you often can rewrite the query to avoid the given extremely common substrings (like "http" or "www" above). Splitting or adding content at the side of the extremely common substrings is often enough for VTGrep to be able to avoid the popular ngrams.

## examples:

|                                                                          |                                                                                                                                                             |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **With extremely common substrings (bad)**                               | **Avoids extremely common substrings (better)**                                                                                                             |
| content:"**goog**le\*\*.com\*\*"                                         | [content:"photos.google.co"](https://www.virustotal.com/gui/search/content%253A%2522photos.google.co%2522)                                                  |
| content:\{**00 00 00 00**}                                               | [content:\{CAFE 00 00 00 00 CAFE}](https://www.virustotal.com/gui/search/content%253A%257BCAFE%252000%252000%252000%252000%2520CAFE%257D)                   |
| content:\{CAFE **00 00 00 00 00** CAFE}                                  | [content:\{CAFE 00 00 ?? 00 00 CAFE}](https://www.virustotal.com/gui/search/content%253A%257BCAFE%252000%252000%2520%253F%253F%252000%252000%2520CAFE%257D) |
| content:"**http**://**[www.\*\*rare\*\*.com](http://www.**rare**.com)**" | [content:"ww.rare.c"](https://www.virustotal.com/gui/search/content%253A%2522ww.rare.c%2522)                                                                |

---

← [File similarity search](file-similarity-search.md) · [up](../README.md) · [Batch file downloads](batch-file-downloads.md) →

*Archived from <https://gtidocs.virustotal.com/docs/content-search-grep>.*
