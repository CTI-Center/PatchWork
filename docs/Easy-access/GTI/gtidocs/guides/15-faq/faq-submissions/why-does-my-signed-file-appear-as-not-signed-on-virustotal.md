---
title: "Why does my signed file appear as \"not signed\" on VirusTotal?"
source: https://gtidocs.virustotal.com/docs/why-does-my-signed-file-appear-as-not-signed-on-virustotal
slug: why-does-my-signed-file-appear-as-not-signed-on-virustotal
section: guides
group: "FAQ"
updatedAt: 2026-02-17T09:05:10.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [FAQ](../README.md) › [File/URL Submissions](../faq-submissions.md) › Why does my signed file appear as "not signed" on VirusTotal?

---

# why-does-my-signed-file-appear-as-"not-signed"-on-virustotal?

I have a file that appears to be digitally signed on my Windows system, but VirusTotal's "Details" tab reports it as "File is not signed." Why is there a discrepancy?

There are two primary reasons why a file might appear signed locally but unsigned on VirusTotal:

#### **1.-the-use-of-windows-catalog-files**

Windows has the capability to use "catalog files" (`.cat`) to verify the digital signature of a file. In these cases, the signature is not embedded directly within the file's Authenticode section as usual; instead, the file's hash is stored in a separate catalog file on your system that declares the file as trusted.

Since VirusTotal analyzes the file in isolation, it does not have access to the specific catalog files present on your local machine, and thus cannot verify signatures that are not embedded directly in the binary.

#### **2.-stricter-authenticode-verification**

VirusTotal enforces a stricter Windows Authenticode signature verification process than some local tools . This means that if a signed file is malformed or has been tampered with, VirusTotal will report it as "File is not signed" to ensure security and integrity.

**How can I verify this myself?**

You can use the **Sigcheck** utility from Microsoft Sysinternals to investigate the signature status of your file.

1. Download [Sigcheck](https://learn.microsoft.com/en-us/sysinternals/downloads/sigcheck).
2. Run the following command in your terminal:
   ```powershell
   sigcheck.exe -i <path_to_your_file>
   ```
3. Check the output:
   * If you see a **"Catalog:"** line in the output pointing to a `.cat` file (e.g., `Catalog: C:\Windows\system32\CatRoot\...`), the signature is external and not embedded in the file.
   * If the file is reported as **"Unsigned"** or **"Verified: Unsigned"** despite appearing signed in Windows Explorer, it may be due to the file being malformed or failing strict verification checks.

---

← [I accidentally uploaded a file with confidential or sensitive information to Google TI, can you please delete it?](accidental-upload.md) · [up](../README.md) · [What type of compressed files are supported?](compressed-files.md) →

*Archived from <https://gtidocs.virustotal.com/docs/why-does-my-signed-file-appear-as-not-signed-on-virustotal>.*
