---
title: "Understanding Partial Files"
source: https://gtidocs.virustotal.com/docs/partial-files
slug: partial-files
section: guides
group: "FAQ"
updatedAt: 2025-09-25T00:33:13.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [FAQ](README.md) › Understanding Partial Files

---

# understanding-partial-files

## introduction

Google Threat Intelligence consolidates threat information from a vast network of sources. This includes not only public submissions but also data derived from processing within other Google security systems and teams, such as Google's internal Anti-Virus engines, Mandiant Incident Response engagements, and other proprietary sources.

Sometimes, Google Threat Intelligence becomes aware of a file and possesses certain metadata about it because it has been processed by one of these internal Google sources. However, the file's actual content might **not** have been added to the generally accessible Google Threat Intelligence file corpus, often due to privacy policies, customer confidentiality agreements, or data handling constraints. The representation of such a file within the Google Threat Intelligence platform – where metadata exists internally but the file isn't broadly shared – is another scenario referred to as a **Partial File**. This article explains this specific type.

## report-characteristics:-limited-public-details

When you view the Google Threat Intelligence report for such a file hash, you will notice specific characteristics:

* **Existence Confirmation:** The report confirms that Google TI systems are aware of this file hash.
* **Metadata Present:** Some metadata fields derived from internal processing will be populated.
* **Limited Technical Details:** There will be a noticeable lack of comprehensive technical analysis results compared to a fully public file. Most significantly, **detection verdicts from the broad ecosystem of security vendors will likely be missing or incomplete.**
* **Reason for Limitation:** The absence of widespread vendor verdicts is because the file content was not distributed through the standard Google Threat Intelligence pipeline to these external security partners due to its non-public, restricted status.

## example-scenario:-file-00000...6558

Let's consider the file with SHA-256 hash `00000007becb1e19e488b5fd8dced93086deb2c383ee15b1c1f22aaae9626558` as an illustrative example of this type of partial file.

**1. Web Report:**

You can view its report page here:\
[`https://www.virustotal.com/gui/file/00000007becb1e19e488b5fd8dced93086deb2c383ee15b1c1f22aaae9626558`](https://www.virustotal.com/gui/file/00000007becb1e19e488b5fd8dced93086deb2c383ee15b1c1f22aaae9626558)

![Partial File example](https://storage.googleapis.com/gtidocresources/guides/faq/images/partial_files_example_20250411.png)

*Observation (Typical State)*: If this file represents a partial entry due to internal processing without public sharing, you would typically see:\
*Basic file properties (hash, size, type).\&#xA;* **Crucially, the "Detections" tab would show very few, or possibly zero, verdicts from the standard list of security vendors.** This contrasts sharply with reports for publicly submitted files.

*(Note: The current live state of any report can change if the file is submitted publicly after its initial internal processing.)*

**2. API Response (`/files/{id}` Endpoint):**

Querying the Google Threat Intelligence API for this file hash (using the endpoint documented at [`https://gtidocs.virustotal.com/reference/file-info`](https://gtidocs.virustotal.com/reference/file-info)) would yield a response that reflects its limited state. A representative JSON snippet might look like this:

```
{
  "data": {
    "id": "00000007becb1e19e488b5fd8dced93086deb2c383ee15b1c1f22aaae9626558",
    "type": "file",
    "links": {
      "self": "https://www.virustotal.com/api/v3/files/00000007becb1e19e488b5fd8dced93086deb2c383ee15b1c1f22aaae9626558"
    },
    "attributes": {
      "last_analysis_stats": {
        "malicious": 0,
        "suspicious": 0,
        "undetected": 0,
        "harmless": 0,
        "timeout": 0,
        "confirmed-timeout": 0,
        "failure": 0,
        "type-unsupported": 0
      },
      "tags": [],
      "type_tags": [],
      "last_modification_date": 1744380110,
      "last_analysis_results": {},
      "type_description": "unknown",
      "downloadable": false,
      "sha256": "00000007becb1e19e488b5fd8dced93086deb2c383ee15b1c1f22aaae9626558"
    },
    "context_attributes": {
      "type": "partial_file"
    }
  }
}
```

Interpretation: This example JSON shows:

* Basic attributes (size, sha256, type\_description, example meaningful\_name, example tags).
* Crucially, last\_analysis\_stats shows 0 across malicious, suspicious, and undetected. This indicates that results from the public pool of scanners are not present for this file hash in the Google Threat Intelligence system at this time.
* The detailed last\_analysis\_results object (which lists each vendor's verdict) would likely be missing or mostly empty in a real response for such a file.

## how-full-analysis-details-become-available

The limited report for this type of partial file can be enriched with full technical details, including external security vendor verdicts, if the complete file is submitted to Google Threat Intelligence and analyzed according to standard Google TI policies.

Unless and until the file is shared publicly via one of these routes, the associated Google Threat Intelligence report will retain its limited, metadata-focused state.

---

← [Why can't I see the gti_assessment attribute in the JSON response?](missing-gti-asssessment.md) · [up](README.md) · [When is an analysis included in the feeds?](when-analysis-feeds.md) →

*Archived from <https://gtidocs.virustotal.com/docs/partial-files>.*
