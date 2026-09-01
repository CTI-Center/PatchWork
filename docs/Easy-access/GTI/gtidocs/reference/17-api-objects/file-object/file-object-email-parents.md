---
title: "🔀 email_parents"
source: https://gtidocs.virustotal.com/reference/file-object-email-parents
slug: file-object-email-parents
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:38.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › 🔀 email_parents

---

# 🔀-email_parents

Email files containing the file.

The *email\_parents* relationship returns the list of ***all email files containing a given file***. This relationship is only available for Premium API users.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/files/files-relationships.md). The response contains a list of [File](../../03-ioc-investigation/files.md) objects.

```json /files/{file_hash}/email_parents
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
                    "LineCount": 28077,
                    "MIMEEncoding": "us-ascii",
                    "MIMEType": "text/plain",
                    "Newlines": "Windows CRLF",
                    "WordCount": 59539
                },
                "first_submission_date": 1587049407,
                "last_analysis_date": 1588653326,
                "last_analysis_results": {
                    "ALYac": {
                        "category": "malicious",
                        "engine_name": "ALYac",
                        "engine_update": "20200505",
                        "engine_version": "1.1.1.5",
                        "method": "blacklist",
                        "result": "Trojan.GenericKD.42996961"
                    },
                    "APEX": {
                        "category": "malicious",
                        "engine_name": "APEX",
                        "engine_update": "20200504",
                        "engine_version": "6.18",
                        "method": "blacklist",
                        "result": "Malicious"
                    },
                    "AVG": {
                        "category": "undetected",
                        "engine_name": "AVG",
                        "engine_update": "20200505",
                        "engine_version": "18.4.3895.0",
                        "method": "blacklist",
                        "result": null
                    },
                    "Acronis": {
                        "category": "malicious",
                        "engine_name": "Acronis",
                        "engine_update": "20200422",
                        "engine_version": "1.1.1.75",
                        "method": "blacklist",
                        "result": "suspicious"
                    },
                    "Ad-Aware": {
                        "category": "malicious",
                        "engine_name": "Ad-Aware",
                        "engine_update": "20200505",
                        "engine_version": "3.0.5.370",
                        "method": "blacklist",
                        "result": "Trojan.GenericKD.42996961"
                    },
                    "AegisLab": {
                        "category": "undetected",
                        "engine_name": "AegisLab",
                        "engine_update": "20200505",
                        "engine_version": "4.2",
                        "method": "blacklist",
                        "result": null
                    },
                },
                "last_analysis_stats": {
                    "confirmed-timeout": 0,
                    "failure": 0,
                    "harmless": 0,
                    "malicious": 4,
                    "suspicious": 0,
                    "timeout": 1,
                    "type-unsupported": 0,
                    "undetected": 2
                },
                "last_modification_date": 1591945304,
                "last_submission_date": 1587049407,
                "magic": "news or mail text",
                "md5": "b67828805dfdabf3a823278c3fdd37f7",
                "meaningful_name": "blablabla.eml",
                "names": [
                    "blablabla.eml"
                ],
                "packers": {
                    "F-PROT": "qp, maxorder, appended, UTF-8"
                },
                "reputation": 0,
                "sha1": "a97e30d504b3e618fc377640d3e65793f6f37625",
                "sha256": "abfa4d040cfb3cd9e22f2301bf0902330ca3a6031ce6a97324b1f1c31494696c",
                "signature_info": {
                    "comments": "blablabla",
                    "copyright": "Copyright © blabla 2020",
                    "description": "blablabla",
                    "file version": "1.3.30.0",
                    "internal name": "blablabla.exe",
                    "original name": "blablabla.exe",
                    "product": "blablabla"
                },
                "size": 1564805,
                "ssdeep": "24576:kI9m552sO95L27K5bbZAR5tCZq53SM557ZP5hO5jZV:k59mK5i45Pi5tCZ5S3SM55r",
                "tags": [
                    "email"
                ],
                "times_submitted": 2,
                "total_votes": {
                    "harmless": 0,
                    "malicious": 0
                },
                "trid": [
                    {
                        "file_type": "MIME HTML archive format",
                        "probability": 88.8
                    },
                    {
                        "file_type": "E-Mail message (Var. 2)",
                        "probability": 11.1
                    }
                ],
                "type_description": "Email",
                "type_tag": "email",
                "unique_sources": 1
            },
            "id": "abfa4d04ecfb8cd9e22e2301bfe902c30caea6071ce6a9742eb1f1ce1494696c",
            "links": {
                "self": "https://www.virustotal.com/api/v3/files/abfa4d04ecfb8cd9e22e2301bfe902c30caea6071ce6a9742eb1f1ce1494696c"
            },
            "type": "file"
        }
    ],
    "links": {
        "self": "https://www.virustotal.com/api/v3/files/abfa4d04ecfb8cd9e22e2301bfe902c30caea6071ce6a9742eb1f1ce1494696c/email_parents"
    },
    "meta": {
        "count": 1
    }
}
```

---

← [🔀 dropped_files](file-object-dropped-files.md) · [up](../README.md) · [🔀 embedded_domains](file-object-embedded-domains.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-email-parents>.*
