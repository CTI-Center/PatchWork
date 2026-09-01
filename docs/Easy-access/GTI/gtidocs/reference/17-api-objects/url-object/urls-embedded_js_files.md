---
title: "🔀 embedded_js_files"
source: https://gtidocs.virustotal.com/reference/urls-embedded_js_files
slug: urls-embedded_js_files
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:45:36.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [URLs](../url-object.md) › 🔀 embedded_js_files

---

# 🔀-embedded_js_files

Found javascript scripts in the URL's HTML response

The *embedded\_js\_files* relationship returns a list of all found JS scripts in the URL's HTML response. This relationship is only available for premium users.

The relationship can be retrieved by using the [relationships API endpoint](../../03-ioc-investigation/urls/urls-relationships.md). The response contains a list of [File](../../03-ioc-investigation/files.md) objects.  The relationship contains the same context attributes as described in [🔀🔒 urls\_for\_embedded\_js](../file-object/file-object-urls-for-embedded-js.md)

```json /urls/{url_id}/embedded_js_files
{
  "data": [
    {
    	"attributes": <FILE_OBJ>,
      "context_attributes": {
        "url": "<string>",
        "timestamp": <int:timestamp>,
        "embedded": <bool>,
        "download_url": "<string>",
        "filename": "<string>"
      }
    }
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
          "LineCount": "5",
          "MIMEEncoding": "us-ascii",
          "MIMEType": "text/plain",
          "Newlines": "Unix LF",
          "WordCount": "1154"
        },
        "first_submission_date": 1606336764,
        "javascript_info": {
          "tags": [
            "substr",
            "unescape",
            "location",
            "replace"
          ]
        },
        "last_analysis_date": 1606336764,
        "last_analysis_results": {
          "ALYac": {
            "category": "undetected",
            "engine_name": "ALYac",
            "engine_update": "20201125",
            "engine_version": "1.1.1.5",
            "method": "blacklist",
            "result": null
          },
          "APEX": {
            "category": "type-unsupported",
            "engine_name": "APEX",
            "engine_update": "20201125",
            "engine_version": "6.101",
            "method": "blacklist",
            "result": null
          },
          "AVG": {
            "category": "undetected",
            "engine_name": "AVG",
            "engine_update": "20201125",
            "engine_version": "20.10.5736.0",
            "method": "blacklist",
            "result": null
          }
        },
        "last_analysis_stats": {
          "confirmed-timeout": 0,
          "failure": 0,
          "harmless": 0,
          "malicious": 0,
          "suspicious": 0,
          "timeout": 0,
          "type-unsupported": 1,
          "undetected": 2
        },
        "last_modification_date": 1611744026,
        "last_submission_date": 1606336764,
        "magic": "ASCII English text, with very long lines",
        "md5": "9451b17966df8a80945a410d1de9191f",
        "meaningful_name": "myscript.js",
        "names": [
          "myscript.js",
          "file.js"
        ],
        "reputation": 0,
        "sha1": "73733d325f370731032c23e9e3903773e4343761",
        "sha256": "3339251c3b90fb36ca3db6f36634f9c32501a09348d36469eb3391823e345372",
        "size": 20638,
        "ssdeep": "192:OfLC199kn2iQQ72qCbXEnz2rKvM8y2qQk2bgKmC2doQp22oCk+Gm26Y12dh42tOo:2f2hkK2vAb2Zoo2IIo",
        "tags": [
          "javascript"
        ],
        "times_submitted": 1,
        "tlsh": "T1B491F7117987123D1A1360F815A74716213F78018198491AF7C8A1991FF741DC8131AC",
        "total_votes": {
          "harmless": 0,
          "malicious": 0
        },
        "type_description": "JavaScript",
        "type_extension": "js",
        "type_tag": "javascript",
        "unique_sources": 1,
        "vhash": "e5db53481a5a0f845332059bc5e51520"
      },
      "id": "3339251c3b90fb36ca3db6f36634f9c32501a09348d36469eb3391823e345372",
      "context_attributes": {
        "timestamp": 1618886645,
        "embedded": true
      }
      "links": {
        "self": "https://www.virustotal.com/api/v3/files/3339251c3b90fb36ca3db6f36634f9c32501a09348d36469eb3391823e345372"
      },
      "type": "file"
    }
  ],
  "links": {
    "next": "https://www.virustotal.com/api/v3/urls/24625c552d60e55877b85e27e5d5aa5ab546750b5a22565eb1b5e82bc269132c/embedded_js_files?cursor=eyJsaW1pdCI6IDEsICJvZmZzZXQiOiA0fQ%3D%3D&limit=1",
    "self": "https://www.virustotal.com/api/v3/urls/24625c552d60e55877b85e27e5d5aa5ab546750b5a22565eb1b5e82bc269132c/embedded_js_files?limit=1"
  },
  "meta": {
    "count": 8,
    "cursor": "eyJsaW1pdCI6IDEsICJvZmZzZXQiOiA0fQ=="
  }
}
```

---

← [🔀 submissions](url-submissions.md) · [up](../README.md) · [🔀 referrer_files](urls-referrer_files.md) →

*Archived from <https://gtidocs.virustotal.com/reference/urls-embedded_js_files>.*
