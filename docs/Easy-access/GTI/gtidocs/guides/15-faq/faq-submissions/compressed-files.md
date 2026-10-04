---
title: "What type of compressed files are supported?"
source: https://gtidocs.virustotal.com/docs/compressed-files
slug: compressed-files
section: guides
group: "FAQ"
updatedAt: 2026-04-23T10:44:50.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [FAQ](../README.md) › [File/URL Submissions](../faq-submissions.md) › What type of compressed files are supported?

---

# what-type-of-compressed-files-are-supported?

You can submit any compressed file that is supported by the 7z software. If successfully decompressed, contained files appear as bundled files in the relationships tab of the archive file report. If it is password protected, the tools uses standard known passwords as "infected" or "password".

If it is a password protected ZIP file and includes just one single compressed file, the web interface will request a password. If you are using the API, the "password" parameter can be used for this purpose. VirusTotal will generate a report for the bundled file and not the ZIP file, but for this case the size limit is 3MBs. If the ZIP file is bigger than 3MBs, we will generate a report for the ZIP file itself.

---

← [Why does my signed file appear as "not signed" on VirusTotal?](why-does-my-signed-file-appear-as-not-signed-on-virustotal.md) · [up](../README.md) · [Why can't I see the gti_assessment attribute in the JSON response?](../missing-gti-asssessment.md) →

*Archived from <https://gtidocs.virustotal.com/docs/compressed-files>.*
