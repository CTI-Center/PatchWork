---
title: "🔀 email_attachments"
source: https://gtidocs.virustotal.com/reference/file-object-email-attachments
slug: file-object-email-attachments
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:42:03.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › 🔀 email_attachments

---

# 🔀-email_attachments

Files attached to a given email file.

The *email\_attachments* relationship returns the list of ***all files contained in an email file as attachments***. Email attachments are files that were distributed through email as attachments. This relationship is only available for Premium API users.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/files/files-relationships.md). The response contains a list of [File](../../03-ioc-investigation/files.md) objects.

```json /files/{file_hash}/email_attachments
{
  "data": [
    <FILE_OBJECT>,
    <FILE_OBJECT>,
    ...
  ],
  "links": {
    "next": "<string>",
    "self": "<string>"
  },
  "meta": {
    "count": <int>,
    "cursor": "<string>"
  }
}
```
```json Example
{
  "data": [
    {
      "attributes": {
        "downloadable": true,
        "exiftool": {
          "FileType": "TXT",
          "FileTypeExtension": "txt",
          "LineCount": "26",
          "MIMEEncoding": "us-ascii",
          "MIMEType": "text/plain",
          "Newlines": "Unix LF",
          "WordCount": "127"
        },
        "first_submission_date": 1436769310,
        "last_analysis_date": 1598121563,
        "last_analysis_results": {
          "ALYac": {
            "category": "undetected",
            "engine_name": "ALYac",
            "engine_update": "20200822",
            "engine_version": "1.1.1.5",
            "method": "blacklist",
            "result": null
          },
          "APEX": {
            "category": "type-unsupported",
            "engine_name": "APEX",
            "engine_update": "20200822",
            "engine_version": "6.62",
            "method": "blacklist",
            "result": null
          },
          "AVG": {
            "category": "undetected",
            "engine_name": "AVG",
            "engine_update": "20200822",
            "engine_version": "18.4.3895.0",
            "method": "blacklist",
            "result": null
          },
          "Acronis": {
            "category": "type-unsupported",
            "engine_name": "Acronis",
            "engine_update": "20200806",
            "engine_version": "1.1.1.77",
            "method": "blacklist",
            "result": null
          }
        },
        "last_analysis_stats": {
          "confirmed-timeout": 0,
          "failure": 2,
          "harmless": 0,
          "malicious": 0,
          "suspicious": 0,
          "timeout": 0,
          "type-unsupported": 15,
          "undetected": 57
        },
        "last_modification_date": 1598121783,
        "last_submission_date": 1573674325,
        "magic": "ASCII English text",
        "md5": "778fc0056711b2ae504fbfb089f70609",
        "meaningful_name": "script.js",
        "names": [
          "script.js"
        ],
        "reputation": 0,
        "sha1": "0214c5e2bf1c32e1309b5afb152342aa86cb8d71",
        "sha256": "749826730c10676dc30ac2894a7eb48ff48d70ea92e586177043698772ab74a8",
        "size": 894,
        "ssdeep": "34:3v321c3y3bcM3C3Z1/A3WnA3k3Z23z3d23Zq/B3y9H3Z53Q3X3D:Q3Mq31L3v3M3K3v3E3Hf/j3JD",
        "tags": [
          "javascript",
          "attachment"
        ],
        "times_submitted": 7,
        "total_votes": {
          "harmless": 0,
          "malicious": 0
        },
        "type_description": "JavaScript",
        "type_tag": "javascript",
        "unique_sources": 4,
        "vhash": "3744b4d249414c4da464fd43444d9441"
      },
      "id": "749826730c10676dc30ac2894a7eb48ff48d70ea92e586177043698772ab74a8",
      "links": {
        "self": "https://www.virustotal.com/api/v3/files/749826730c10676dc30ac2894a7eb48ff48d70ea92e586177043698772ab74a8"
      },
      "type": "file"
    }
  ],
  "links": {
    "next": "https://www.virustotal.com/api/v3/files/ccd54c2ef3090e6e31918e9efa1c341f974e67b854fabb35bd3f08c3c4d3703a/email_attachments?cursor=eyJsaW1pd4I64DEs4CJv4mZ4ZXQ4Oi4xfQ%3D%3D%0A&limit=1",
    "self": "https://www.virustotal.com/api/v3/files/ccd54c2ef3090e6e31918e9efa1c341f974e67b854fabb35bd3f08c3c4d3703a/email_attachments?limit=1"
  },
  "meta": {
    "count": 19,
    "cursor": "eyJsaW1pd4I64DEs4CJv4mZ4ZXQ4Oi4xfQ==\n"
  }
}
```

---

← [🔀 contacted_urls](file-object-contacted-urls.md) · [up](../README.md) · [🔀 votes](file-object-votes.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-email-attachments>.*
