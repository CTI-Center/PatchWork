---
title: "openxml_info"
source: https://gtidocs.virustotal.com/reference/file-object-openxml-info
slug: file-object-openxml-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:18.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › openxml_info

---

# openxml_info

Microsoft OpenXML files information.

`openxml_info` returns information about structure of Microsoft Office Open XML files (Office 2007+). This includes (Word) .docx, .docm, .dotx, .dotm, (Excel) .xlsx, .xlsm, .xltx, .xltm, (PowerPoint) .pptx, .pptm, .potx, .potm, .ppam, .ppsx, .ppsm, .sldx, .sldm. This information is only available for Premium API users.

* `content_types`: <*list of strings*> MIME type information for parts of the package.
* `docprops_app`: <*dictionary*> some properties of the file, fields may vary depending file type.
  * `AppVersion`: <*string*> application version (in a numeric form).
  * `Application`: <*string*> application name (i.e. "Microsoft Office Word").
  * `Characters`: <*string*> number of characters without spaces.
  * `CharactersWithSpaces`: <*string*> number of characters with spaces.
  * `Company`: <*string*> company name.
  * `DocSecurity`: <*string*> "0" if no password.
  * `HyperlinksChanged`: <*string*> one or more hyperlinks in this part were updated exclusively in this part by a producer.
  * `Lines`: <*string*> number of lines.
  * `LinksUpToDate`: <*string*> "true" to indicate that hyperlinks are updated, "false" otherwise.
  * `Pages`: <*string*> number of pages.
  * `Paragraphs`: <*string*> number of paragraphs.
  * `ScaleCrop`: <*string*> thumbnail display mode.
  * `SharedDoc`: <*string*> note if is a shared document.
  * `Template`: <*string*> name of template used in the document.
  * `TotalTime`: <*string*> document total edit time.
  * `Words`:  <*string*> number of words.
* `docprops_core`: <*dictionary*> core properties for any Office Open XML document
  * `cp:lastModifiedBy`: <*string*> user that made the last modification.
  * `cp:lastPrinted`: <*string*> last time document was printed in `%Y-%m-%dT%H:%M:%SZ` [format](http://strftime.org/).
  * `cp:revision`: <*string*> document revision.
  * `dc:creator`: <*string*> document creator.
  * `dcterms:created`: <*string*> date of creation in `%Y-%m-%dT%H:%M:%SZ` [format](http://strftime.org/).
  * `dcterms:modified`: <*string*> last modification date in `%Y-%m-%dT%H:%M:%SZ` [format](http://strftime.org/).
* `file_type`: <*string*> file type, extension style ("docx", "pptx", etc.).
* `ole`: <*dictionary*> macros found in OLE content.
  * `macros`: <*list of dictionaries*> details of found macros. Every item in the list contains the following fields:
    * `lengh`: <*integer*> macro length.
    * `patterns`: <*list of strings*> interesting patterns found ("exe-pattern", "url-pattern", etc.).
    * `properties`: <*list of strings*> interesting properties found ("obfuscated", "run-file", etc.).
    * `stream_path`: <*string*> path in the OLE strorage tree.
    * `subfilename`: <*string*> macro subfilename.
    * `vba_code`: <*string*> macro code.
    * `vba_filename`: <*string*> name of the macro.
  * `num_macros`: <*integer*> number of macros found.
* `rels`: <*list of strings*> relationships for the files within the package.
* `type_content`: <*dictionary*> information specific to each file format.
  * (Word, PowerPoint)
    * `languages`: <*dictionary*> references to found languages. Key is the language code and value is how many references there are.
  * (Excel):
    * `codifications`: <*list of lists*> references to used code pages. Every item in the list contains two values:
      * <*string*> first one is the code page name.
      * <*integer*> second one is how many times that codepage was referenced.
    * `language_guess`: <*list of lists*> guess of used languages. Every item in the list contains two values:
      * <*string*> first one is the language code.
      * <*integer*> second one is how many times that language was referenced.
    * `workbook`: <*dictionary*> info about the workbook.
      * `calcPr`: <*string*> version of Excel.
      * `lastEdited`: <*string*> last edited version.
      * `lowestEdited`: <*string*> lowest edited version.
      * `oleSize`: <*string*> size of OLE object.
      * `relationships`: <*list of strings*>
      * `rupBuild`: <*string*> build version.
      * `sheets`: <*integer*> number of sheets.
  * (Excel, PowerPoint)
    * `printers`: <*list of strings*> contains printers names used to print this document.

```json Microsoft Office openxml info
{
  "data": {
		...
    "attributes" : {
      ...
      "openxml_info": {
        "content_types": ["<strings>"],
        "docprops_app": {
            "TotalTime": "<string>", 
            "Words": "<string>", 
            "ScaleCrop": "<string>", 
            "SharedDoc": "<string>", 
            "Company": "<string>", 
            "Lines": "<string>", 
            "AppVersion": "<string>", 
            "LinksUpToDate": "<string>", 
            "Pages": "<string>", 
            "Application": "<string>", 
            "CharactersWithSpaces": "<string>", 
            "Characters": "<string>", 
            "Paragraphs": "<string>", 
            "Template": "<string>", 
            "DocSecurity": "<string>", 
            "HyperlinksChanged": "<string>"
        },
        "docprops_core": {
            "dc:creator": "<string>", 
            "cp:revision": "<string>", 
            "dcterms:created": "<string>", 
            "dcterms:modified": "<string>", 
            "cp:lastModifiedBy": "<string>", 
            "cp:lastPrinted": "<string>"
        },
        "file_type": "<string>",
        "ole": {
            "macros": [
                {
                    "vba_code": "<string>",
                    "stream_path": "<string>", 
                    "subfilename": "<string>", 
                    "vba_filename": "<string>", 
                    "patterns": ["<strings>"], 
                    "length": <int>, 
                    "properties": ["<strings>"]
                }, ...
            ],
            "num_macros": <int>
        },
        "rels": ["<strings>"],
        "tags": ["<strings>"],
        "type_content": {
            "languages": {
                "<string>": <int>, ...
            },
            "codifications" : [
                ["<string>", <int>] ...
            ],
            "workbook": {
                "sheets": <int>, 
                "lowestEdited": "<string>", 
                "calcPr": "<string>", 
                "lastEdited": "<string>", 
                "rupBuild": "<string>"
            },
            "language_guess": [
                ["<string>", <int>], ...
            ],
            "printers": ["<strings>"]
        }
      }
    }
  }
}
```
```json Example (docx)
{
    "data": {
        "attributes": {
            "openxml_info": {
                "content_types": [
                    "rels",
                    "xml",
                    "jpg",
                    "bin"
                ],
                "docprops_app": {
                    "AppVersion": "16.0000",
                    "Application": "Microsoft Office Word",
                    "Characters": "0",
                    "CharactersWithSpaces": "0",
                    "DocSecurity": "0",
                    "HyperlinksChanged": "false",
                    "Lines": "0",
                    "LinksUpToDate": "false",
                    "Pages": "1",
                    "Paragraphs": "0",
                    "ScaleCrop": "false",
                    "SharedDoc": "false",
                    "Template": "Single spaced (blank).dotx",
                    "TotalTime": "1",
                    "Words": "0",
                    "vt:i4": "1",
                    "vt:lpstr": "Title"
                },
                "docprops_core": {
                    "cp:lastModifiedBy": "blablabla",
                    "cp:revision": "2",
                    "dc:creator": "blablabla",
                    "dcterms:created": "2020-06-02T16:22:00Z",
                    "dcterms:modified": "2020-06-02T16:31:00Z"
                },
                "file_type": "docx",
                "ole": {
                    "macros": [
                        {
                            "length": 1614,
                            "patterns": [
                                "exe-pattern"
                            ],
                            "properties": [
                                "create-ole",
                                "environ",
                                "obfuscated",
                                "run-file"
                            ],
                            "stream_path": "VBA/ThisDocument",
                            "subfilename": "word/vbaProject.bin",
                            "vba_code": "Public Sub Document_Open()\nCreateObject(\"Excel.Application\").Wait (Now + TimeValue(\"00:00:01\"))\nShell (blablabalablablalabalalaldksdk)   End Function",
                            "vba_filename": "ThisDocument.cls"
                        }
                    ],
                    "num_macros": 1
                },
                "rels": [
                    "word/document.xml",
                    "docProps/custom.xml",
                    "docProps/app.xml",
                    "docProps/core.xml"
                ],
                "type_content": {
                    "languages": {
                        "ar-sa": 1,
                        "en-us": 2
                    }
                }
            }
        }
    }
}
```
```json Example (xlsx)
{
    "data": {
        "attributes": {
            "openxml_info": {
                "content_types": [
                    "bin",
                    "xml",
                    "vml",
                    "emf",
                    "rels",
                    "png"
                ],
                "docprops_app": {
                    "AppVersion": "16.0300",
                    "DocSecurity": "0",
                    "HyperlinksChanged": "false",
                    "LinksUpToDate": "false",
                    "ScaleCrop": "false",
                    "SharedDoc": "false",
                    "vt:i4": "1",
                    "vt:lpstr": "   "
                },
                "docprops_core": {
                    "dcterms:created": "2020-05-20T11:02:45Z",
                    "dcterms:modified": "2020-05-20T11:04:58Z"
                },
                "file_type": "xlsx",
                "ole": {
                    "macros": [
                        {
                            "length": 592,
                            "patterns": [],
                            "properties": [
                                "create-ole",
                                "run-file"
                            ],
                            "stream_path": "VBA/Sheet1",
                            "subfilename": "xl/vbaProject.bin",
                            "vba_code": "Sub FinishView()\nMsgBox \"\": FormsButton\nEnd Sub\nFunction Private1(textv As String) As String\ndebug_0 = 2: Private1 = Mid(textv, debug_0, 1)\nEnd Function\n\nFinishView\nEnd Sub",
                            "vba_filename": "Sheet1.cls"
                        }
                    ],
                    "num_macros": 2
                },
                "rels": [
                    "docProps/app.xml",
                    "docProps/core.xml",
                    "xl/workbook.xml"
                ],
                "type_content": {
                    "codifications": [
                        [
                            "Basic Latin",
                            2885
                        ]
                    ],
                    "language_guess": [
                        [
                            "ro",
                            38
                        ],
                        [
                            "fr",
                            31
                        ],
                        [
                            "de",
                            11
                        ]
                    ],
                    "workbook": {
                        "calcPr": "181029",
                        "lastEdited": "7",
                        "lowestEdited": "7",
                        "rupBuild": "22730",
                        "sheets": 1
                    }
                }
            }
        }
    }
}
```
```json Example (pptx)
{
    "data": {
        "attributes": {
            "openxml_info": {
                "content_types": [
                    "bin",
                    "rels",
                    "jpeg",
                    "xml"
                ],
                "docprops_app": {
                    "AppVersion": "16.0000",
                    "Application": "Microsoft Office PowerPoint",
                    "HiddenSlides": "0",
                    "HyperlinksChanged": "false",
                    "LinksUpToDate": "false",
                    "MMClips": "0",
                    "Notes": "0",
                    "Paragraphs": "0",
                    "PresentationFormat": "Widescreen",
                    "ScaleCrop": "false",
                    "SharedDoc": "false",
                    "Slides": "1",
                    "TotalTime": "0",
                    "Words": "0",
                    "vt:i4": "1",
                    "vt:lpstr": "PowerPoint Presentation"
                },
                "docprops_core": {
                    "cp:lastModifiedBy": "10",
                    "cp:revision": "2",
                    "dc:creator": "10",
                    "dc:title": "PowerPoint Presentation",
                    "dcterms:created": "2020-03-28T16:05:53Z",
                    "dcterms:modified": "2020-03-28T16:07:17Z"
                },
                "file_type": "pptx",
                "ole": {
                    "macros": [
                        {
                            "length": 350,
                            "patterns": [
                                "exe-pattern",
                                "url-pattern"
                            ],
                            "properties": [
                                "auto-open",
                                "run-file"
                            ],
                            "stream_path": "VBA/Module1",
                            "subfilename": "ppt/vbaProject.bin",
                            "vba_code": "Sub Auto_Open()\n    ' balbalalabalbal\nEnd Sub",
                            "vba_filename": "Module1.bas"
                        }
                    ],
                    "num_macros": 1
                },
                "rels": [
                    "docProps/thumbnail.jpeg",
                    "ppt/presentation.xml",
                    "docProps/app.xml",
                    "docProps/core.xml"
                ],
                "type_content": {
                    "languages": {
                        "en-us": 1
                    },
                    "printers": [
                      	"\\\\DATASRV\\Toshiba Inkoop (kleu"
                    ], 
                }
            }
        }
    }
}
```

---

← [office_info](file-object-office-info.md) · [up](../README.md) · [pdf_info](file-object-pdf-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-openxml-info>.*
