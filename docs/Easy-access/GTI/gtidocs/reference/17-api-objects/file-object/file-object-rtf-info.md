---
title: "rtf_info"
source: https://gtidocs.virustotal.com/reference/file-object-rtf-info
slug: file-object-rtf-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:21.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › rtf_info

---

# rtf_info

information about Microsoft Rich Text Format files.

`rtf_info` returns information about [Microsoft RTF files](https://en.wikipedia.org/wiki/Rich_Text_Format). This information is only available for Premium API users.

* `document_properties`: <*dictionary*> structural metadata about the document.
  * `custom_xml_data_properties`: <*integer*> number of custom XML data objects.
  * `default_ansi_codepage`: <*string*> used codepage (i.e. "Western European").
  * `default_character_set`: <*string*> character set used (i.e. "ANSI").
  * `default_languages`: <*list of strings*> languages detected in the document.
  * `dos_stubs`: <*integer*> number of found DOS stubs.
  * `embedded_drawings`: <*integer*> number of contained drawings.
  * `embedded_pictures`: <*integer*> number of embedded pictures.
  * `longest_hex_string`: <*integer*> longest hexadecimal string found in the document.
  * `non_ascii_characters`: <*integer*> number of non-ASCII characters in the document.
  * `objects`: <*list of dictionaries*> list of objects contained. Every item on the list contains the following fields:
    * `class`: <*string*> object class.
    * `type`: <*string*> object type.
  * `read_only_protection`: <*boolean*> noting if file is for read only.
  * `rtf_header`: <*string*> RTF header (i.e. "rtf1").
  * `user_protection`: <*boolean*> user protection.
* `summary_info`: <*dictionary*> other document properties. Additional subfields may be returned, but the most common ones are:
  * `author`: <*string*> document author.
  * `company`: <*string*> document's author's company name.
  * `creation_time`: <*string*> date of creation in in `%Y-%m-%d %H:%M:%S` [format](http://strftime.org/).
  * `editing_time`: <*integer*> total editing time in minutes.
  * `number_of_characters`: <*integer*> number of characters in the document.
  * `number_of_non_whitespace_characters`: <*integer*> non-whitespace characters found.
  * `number_of_pages`: <*integer*> number of pages in the document.
  * `number_of_words`: <*integer*> number of words in the document.
  * `operator`: <*string*> document creator username.
  * `print_time`: <*string*> date of last printing in `%Y-%m-%d %H:%M:%S` [format](http://strftime.org/).
  * `revision_time`: <*string*> date of last revision in `%Y-%m-%d %H:%M:%S` [format](http://strftime.org/).
  * `title`: <*string*> document title.
  * `version`: <*integer*> RTF version stated in the document.
  * `version_number`: <*integer*> document version number.

```json Microsoft RTF files
{
  "data": {
		...
    "attributes" : {
      ...
      "rtf_info": {
        "document_properties": {
            "custom_xml_data_properties": <int>, 
            "default_ansi_codepage": "<string>", 
            "default_character_set": "<string>", 
            "default_languages": [
                "<strings>"
            ],
            "dos_stubs": <int>, 
            "embedded_drawings": <int>,
            "embedded_pictures": <int>, 
            "longest_hex_string": <int>,
            "non_ascii_characters": <int>,
            "objects": [
                {
                    "class": "<string>",
                    "type": "<string>"
                } ...
            ],
            "read_only_protection": <boolean>, 
            "rtf_header": "<string>", 
            "user_protection": <boolean>,
        },
        "summary_info": {
            "author": "<string>",
            "company": "<string>",
            "creation_time": "<string:%Y-%m-%d %H:%M:%S>",
            "editing_time": <int>,
            "number_of_characters": <int>,
            "number_of_non_whitespace_characters": <int>,
            "number_of_pages": <int>,
            "number_of_words": <int>,
            "operator": "<string>",
            "print_time": "<string:%Y-%m-%d %H:%M:%S>",
            "revision_time": "<string:%Y-%m-%d %H:%M:%S>",
            "title": "<string>",
            "version": <int>,
            "version_number": <int>,
            "<string>": <value>
        }
      }
    }
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "rtf_info": {
                "document_properties": {
                    "custom_xml_data_properties": 1,
                    "default_ansi_codepage": "Western European",
                    "default_character_set": "ANSI",
                    "default_languages": [
                        "German - Germany",
                        "Arabic - Saudi Arabia"
                    ],
                    "dos_stubs": 0,
                    "embedded_drawings": 21,
                    "embedded_pictures": 2,
                    "longest_hex_string": 77114,
                    "non_ascii_characters": 0,
                    "objects": [
                        {
                            "class": "Package",
                            "type": "OLE embedded"
                        }
                    ],
                    "read_only_protection": false,
                    "rtf_header": "rtf1",
                    "user_protection": false
                },
                "summary_info": {
                    "author": "blablablabla",
                    "company": "blablablabla",
                    "creation_time": "2020-06-24 17:43:00",
                    "editing_time": 0,
                    "number_of_characters": 1935,
                    "number_of_non_whitespace_characters": 2238,
                    "number_of_pages": 2,
                    "number_of_words": 307,
                    "operator": "blablabla",
                    "print_time": "2020-01-08 18:30:00",
                    "revision_time": "2020-06-24 17:57:00",
                    "title": "blablabla",
                    "version": 3,
                    "version_number": 1
                }
            }
        }
    }
}
```

---

← [packers](file-object-peid.md) · [up](../README.md) · [swf_info](file-object-swf-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-rtf-info>.*
