---
title: "Overview"
source: https://gtidocs.virustotal.com/reference/alert-documents-overview
slug: alert-documents-overview
section: reference
group: "GTI Alerts"
updatedAt: 2026-03-06T12:09:47.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [GTI Alerts](../README.md) › [Alert Documents](../alert-documents.md) › Overview

---

# overview

## resource:-alertdocument

A document that is associated with an alert.

```json JSON representation
{
  "name": string,
  "content": string,
  "author": string,
  "createTime": string,
  "languageCode": string,
  "title": string,
  "aiSummary": string,
  "translation": {
    object (AlertDocumentTranslation)
  },
  "source": string,
  "sourceUri": string,
  "ingestTime": string,
  "collectionTime": string,
  "sourceUpdateTime": string
}
```

<br />

| Fields             |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`             | `string`<br /><br />Identifier. Server generated name for the alert document. format is projects/\{project}/alerts/\{alert}/documents/\{document}                                                                                                                                                                                                                                                                                                        |
| `content`          | `string`<br /><br />Output only. The content of the document.                                                                                                                                                                                                                                                                                                                                                                                            |
| `author`           | `string`<br /><br />Output only. The author of the document.                                                                                                                                                                                                                                                                                                                                                                                             |
| `createTime`       | `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) ` format)`<br /><br />Output only. The time the document was created.<br /><br />Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.                  |
| `languageCode`     | `string`<br /><br />Output only. The language code of the document.                                                                                                                                                                                                                                                                                                                                                                                      |
| `title`            | `string`<br /><br />Output only. The title of the document, if available.                                                                                                                                                                                                                                                                                                                                                                                |
| `aiSummary`        | `string`<br /><br />Output only. AI summary of the finding.                                                                                                                                                                                                                                                                                                                                                                                              |
| `translation`      | `object (`[AlertDocumentTranslation](#alertdocumenttranslation) `)`<br /><br />Output only. The translation of the document, if available.                                                                                                                                                                                                                                                                                                               |
| `source`           | `string`<br /><br />Output only. Source of the intel item, e.g. DarkMarket.                                                                                                                                                                                                                                                                                                                                                                              |
| `sourceUri`        | `string`<br /><br />Output only. URI of the intel item from the source.                                                                                                                                                                                                                                                                                                                                                                                  |
| `ingestTime`       | `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) ` format)`<br /><br />Output only. Time when GTI received the intel.<br /><br />Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.                   |
| `collectionTime`   | `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) ` format)`<br /><br />Output only. Time when the origin source collected the intel.<br /><br />Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.    |
| `sourceUpdateTime` | `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) ` format)`<br /><br />Output only. Time when the intel was last updated by the source.<br /><br />Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |

## alertdocumenttranslation

The translation of an alert document.

```json JSON representation
{
  "translatedTitle": string,
  "translatedContent": string
}
```

<br />

| Fields              |                                                                          |
| ------------------- | ------------------------------------------------------------------------ |
| `translatedTitle`   | `string`<br /><br />Output only. The translated title of the document.   |
| `translatedContent` | `string`<br /><br />Output only. The translated content of the document. |

### methods

|                               |                                                    |
| ----------------------------- | -------------------------------------------------- |
| [get](get-alert-document.md) | Gets a specific document associated with an alert. |

<br />

---

← [Alert Documents](../alert-documents.md) · [up](../README.md) · [Get Document](get-alert-document.md) →

*Archived from <https://gtidocs.virustotal.com/reference/alert-documents-overview>.*
