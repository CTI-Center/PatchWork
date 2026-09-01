---
title: "office_info"
source: https://gtidocs.virustotal.com/reference/file-object-office-info
slug: file-object-office-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:16.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › office_info

---

# office_info

Microsoft Office files structure information.

`office_info` returns information about Microsoft Office files (before Office 2007). This includes (Word) .doc, .dot, .wbk, (Excel) .xls, .xlt, .xlm, (PowerPoint) .pot, .pps. This data is only available for Premium API users.

* `documment_summary_info`: <*dictionary*> some of the metadata about the office file is here.
  * `characters_with_spaces`: <*integer*> number of characters including spaces.
  * `code_page`: <*string*> character set used for this document.
  * `company`: <*string*> company name.
  * `hyperlinks_changed`: <*boolean*> one or more hyperlinks in this part were updated exclusively in this part by a producer.
  * `line_count`: <*integer*> number of lines.
  * `links_dirty`: <*boolean*> whether the custom links are hampered by excessive noise, for all applications.
  * `paragraph_count`: <*integer*> number of paragraphs.
  * `scale`: <*boolean*> true if scaling of thumbnail is required, False to use cropping.
  * `shared_document`: <*boolean*> note if is a shared document.
  * `version`: <*integer*> identifier of Microsoft Office application.
* `entries`: <*list of dictionaries*> contains OLE objects in the document. Every item in the list contains the following fields:
  * `clsid`: <*string*> application unique identifier.
  * `clsid_literal`: <*string*> readable version of clsid.
  * `name`: <*string*> object name.
  * `sid`: <*integer*> index of the entry in the OLE directory.
  * `size`: <*integer*> object size in bytes.
  * `type_literal`: <*string*> object type.
* `ole`: <*dictionary*> like macros found in the OLE directory.
  * `macros`: <*list of dictionaries*> details of macros found.
    * `lengh`: <*integer*> macro length.
    * `patterns`: <*list of strings*> interesting patterns found ("exe-pattern", "url-pattern", etc.).
    * `properties`: <*list of strings*> interesting properties ("obfuscated", "run-file", etc.).
    * `stream_path`: <*string*> path in the OLE strorage tree.
    * `vba_code`: <*string*> macro code.
    * `vba_filename`: <*string*> name of the macro.
  * `num_macros`: <*integer*> number of found macros.
* `summary_info`: <*dictionary*> other set of metadata about the office file is here. Depending on the type of Office file, some fields may appear or not.
  * `application_name`: <*string*> specific Office application (i.e. "Microsoft PowerPoint").
  * `author`: <*string*> original user who created the file.
  * `character_count`: <*integer*> number of characters in the document.
  * `code_page`: <*string*> character set used for this document (i.e. "Latin I").
  * `creation_datetime`: <*string*> date of creation in `%Y-%m-%d %H:%M:%S` [format](http://strftime.org/).
  * `edit_time`: <*integer*> time spent editing the document, in seconds.
  * `last_author`: <*string*> last user who edited the file.
  * `last_printed`: <*string*> date of last printing in `%Y-%m-%d %H:%M:%S` [format](http://strftime.org/).
  * `last_saved`: <*string*> date of last saving, in `%Y-%m-%d %H:%M:%S` [format](http://strftime.org/).
  * `page_count`: <*integer*> number of pages of the document.
  * `revision_number`: <*integer*> document revision number.
  * `security`: <*integer*> 0 if no password.
  * `template`: <*string*> template use to create this file.
  * `title`: <*string*> document title.
  * `word_count`: <*integer*> number of words in the document.

```json Microsoft Office files structure info
{
  "data": {
		...
    "attributes" : {
      ...
      "office_info": {
        "documment_summary_info": {
          "scale": <boolean>,
          "links_dirty": <boolean>,
          "line_count": <int>,
          "hyperlinks_changed": <boolean>,
          "characters_with_spaces": <int>,
          "version": <int>,
          "shared_document": <boolean>,
          "paragraph_count": <int>,
          "company": "<string>",
          "code_page": "<string>"
        },
        "entries": [
          {
            "clsid": "<string>",
            "clsid_literal": "<string>",
            "name": "<string>",
            "type_literal": "<string>",
            "sid": <int>,
            "size": <int>,
          } ...
        ],
        "ole": {
          "macros": [
            {
              "vba_code": "<string>",
              "stream_path": "<string>",
              "vba_filename": "<string>",
              "patterns": ["<strings>"],
              "length": <int>,
              "properties": ["<strings>"]
            }, ...
          ],
          "num_macros": <int>
        },
        "summary_info": {
          "last_author": "<string>",
          "creation_datetime": "<string:%Y-%m-%d %H:%M:%S>",
          "template": "<string>",
          "author": "<string>", 
          "page_count": <int>, 
          "last_saved": "<string:%Y-%m-%d %H:%M:%S>", 
          "edit_time": <int>, 
          "word_count": <int>, 
          "revision_number": "<string>", 
          "last_printed": "<string:%Y-%m-%d %H:%M:%S>", 
          "application_name": "<string>", 
          "title": "<string>",
          "character_count": <int>,
          "security": <int>,
          "code_page": "<string>"
        }
      }
    }
  }
}
```
```json Example (doc)
{
    "data": {
        "attributes": {
            "office_info": {
                "document_summary_info": {
                    "characters_with_spaces": 132,
                    "code_page": "Latin I",
                    "hyperlinks_changed": false,
                    "line_count": 1,
                    "links_dirty": false,
                    "paragraph_count": 1,
                    "scale": false,
                    "shared_document": false,
                    "version": 1048576
                },
                "entries": [
                    {
                        "clsid": "00020906-0000-0000-c000-000000000046",
                        "clsid_literal": "MS Word",
                        "name": "Root Entry",
                        "sid": 0,
                        "size": 1216,
                        "type_literal": "root"
                    },
                    {
                        "name": "\u0001CompObj",
                        "sid": 13,
                        "size": 114,
                        "type_literal": "stream"
                    },
                    {
                        "name": "\u0005DocumentSummaryInformation",
                        "sid": 5,
                        "size": 4096,
                        "type_literal": "stream"
                    },
                    {
                        "name": "\u0005SummaryInformation",
                        "sid": 4,
                        "size": 4096,
                        "type_literal": "stream"
                    }
                ],
                "ole": {
                    "macros": [
                        {
                            "length": 28230,
                            "patterns": [
                                "exe-pattern"
                            ],
                            "properties": [
                                "run-dll"
                            ],
                            "stream_path": "Macros/VBA/ThisDocument",
                            "vba_code": "#If VBA7 Then\n    Private Declare blablabla Function",
                            "vba_filename": "blablabla.cls"
                        }
                    ],
                    "num_macros": 1
                },
                "summary_info": {
                    "application_name": "Microsoft Office Word",
                    "author": "blablabla",
                    "character_count": 114,
                    "code_page": "Latin I",
                    "creation_datetime": "2020-05-16 17:58:00",
                    "edit_time": 180,
                    "last_author": "blablabla",
                    "last_saved": "2020-06-09 16:16:00",
                    "page_count": 1,
                    "revision_number": "8",
                    "security": 0,
                    "template": "Normal.dotm",
                    "word_count": 19
                }
            }
        }
    }
}
```
```json Example (ppt)
{
    "data": {
        "attributes": {
            "office_info": {
                "document_summary_info": {
                    "byte_count": 825825,
                    "code_page": "Hebrew",
                    "hidden_count": 0,
                    "hyperlinks_changed": false,
                    "links_dirty": false,
                    "multimedia_clip_count": 0,
                    "note_count": 0,
                    "paragraph_count": 31,
                    "presentation_format": "\u00e4\u00f6\u00e2\u00e4 \u00f2\u00ec \u00e4\u00ee\u00f1\u00ea",
                    "scale": false,
                    "shared_document": false,
                    "slide_count": 20,
                    "version": 730895
                },
                "entries": [
                    {
                        "clsid": "64818d10-4f9b-11cf-86ea-00aa00b929e8",
                        "clsid_literal": "MS PowerPoint",
                        "name": "Root Entry",
                        "sid": 0,
                        "size": 0,
                        "type_literal": "root"
                    },
                    {
                        "name": "\u0005DocumentSummaryInformation",
                        "sid": 5,
                        "size": 4096,
                        "type_literal": "stream"
                    },
                    {
                        "name": "\u0005SummaryInformation",
                        "sid": 3,
                        "size": 44448,
                        "type_literal": "stream"
                    }
                ],
                "summary_info": {
                    "application_name": "Microsoft Office PowerPoint",
                    "author": "blablabla",
                    "code_page": "Hebrew",
                    "creation_datetime": "2011-10-19 18:22:34",
                    "edit_time": 24,
                    "last_author": "blabla",
                    "last_saved": "2011-10-19 18:22:59",
                    "revision_number": "1",
                    "title": "blabla",
                    "word_count": 339
                }
            }
        }
    }
}
```
```json Example (xls)
{
    "data": {
        "attributes": {
            "office_info": {
                "document_summary_info": {
                    "code_page": "Latin I",
                    "hyperlinks_changed": false,
                    "links_dirty": false,
                    "scale": false,
                    "shared_document": false,
                    "version": 1048576
                },
                "entries": [
                    {
                        "clsid": "00020820-0000-0000-c000-000000000046",
                        "clsid_literal": "MS Excel",
                        "name": "Root Entry",
                        "sid": 0,
                        "size": 0,
                        "type_literal": "root"
                    },
                    {
                        "name": "\u0005DocumentSummaryInformation",
                        "sid": 3,
                        "size": 4096,
                        "type_literal": "stream"
                    },
                    {
                        "name": "\u0005SummaryInformation",
                        "sid": 2,
                        "size": 4096,
                        "type_literal": "stream"
                    },
                    {
                        "name": "Workbook",
                        "sid": 1,
                        "size": 274587,
                        "type_literal": "stream"
                    }
                ],
                "summary_info": {
                    "application_name": "Microsoft Excel",
                    "author": "Administrator",
                    "code_page": "Latin I",
                    "creation_datetime": "2020-06-18 10:19:37",
                    "last_author": "Administrator",
                    "last_saved": "2020-06-18 10:19:39",
                    "security": 0
                }
            }
        }
    }
}
```

---

← [macho_info](file-object-macho-info.md) · [up](../README.md) · [openxml_info](file-object-openxml-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-office-info>.*
