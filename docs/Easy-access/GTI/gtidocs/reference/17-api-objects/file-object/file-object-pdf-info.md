---
title: "pdf_info"
source: https://gtidocs.virustotal.com/reference/file-object-pdf-info
slug: file-object-pdf-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:19.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › pdf_info

---

# pdf_info

information about Adobe PDF files.

`pdf_info` returns information about [PDF file](https://en.wikipedia.org/wiki/PDF) structure.

* `acroform`: <*integer*> count of `/AcroForm` tags found in the document. An *AcroForm* is an interactive form.
* `autoaction`: <*integer*> number of `/AA` tags found in the document. An *AutoAction* defines an action to be taken in response to various trigger events affecting the document as a whole.
* `embedded_file`: <*integer*> number of `/EmbeddedFile` tags found in the document. An embedded file makes the PDF file self-contained, since it allows to work with the PDF and the files it references as a single entity.
* `encrypted`: <*integer*> whether the document is encrypted or not, this is defined by the `/Encrypt` tag.
* `flash`: <*integer*> number of `/RichMedia` tags found in the PDF. This tag allows to attach Flash applications, audio, video and other multimedia in the PDF file.
* `header`: <*string*> PDF version (i.e. "%PDF-1.7").
* `javascript`: <*integer*> number of `/JavaScript` tags found in the PDF. This tag is used to define Javascript actions. It must be used with the `/S` tag in order to specify the type of action.
* `jbig2_compression`: <*integer*> number of `/JBIG2Decode` tags found in the PDF. This tag is used to decompress data encoded using the JBIG2 standard, reproducing the original monochrome (1 bit per pixel) image data.
* `js`: <*integer*> number of `/JS` tags found in the PDF. This tag is used with the `/JavaScript` one to add in-line javascript code when defining the object. In normal situations, `js` and `javascript` values should be the same (as they are used in pairs).
* `num_endobj`: <*integer*> number of objects definitions (`endobj` keyword). This should have the same value as `num_obj` field.
* `num_endstream`:  <*integer*> number of defined *stream* objects (`endstream` keyword). This should have the same value as `num_stream` field.
* `num_launch_actions`: <*integer*> number of `/Launch` tags found in the PDF. This tag defines a *Launch Action* which is used to launch an application, open or print a document.
* `num_obj`: <*integer*> number of objects definitions (`obj` keyword).
* `num_object_streams`: <*integer*> number of object streams. An *object stream* is a stream that contains a sequence of PDF objects.
* `num_pages`: <*integer*> number of pages.
* `num_stream`: <*integer*> Number of defined *stream* objects (`stream` keyword).
* `openaction`: <*integer*> number of `/OpenAction` tags found in the PDF. An *OpenAction* is a value specifying a destination that shall be displayed or an action that shall be performed when the document is opened. If empty, the document will be opened at the top of the first page at the default magnification factor.
* `startxref`: <*integer*> number of `startxref` keywords in the document. This keyword is used to indicate the offset of a cross reference table or stream.
* `suspicious_colors`: <*integer*> number of colors expressed with more than 3 bytes (CVE-2009-3459).
* `trailer`: <*integer*> number of `trailer` keywords in the document. The trailer of a PDF enables a conforming reader to quickly find the cross-reference table and certain special objects.
* `xfa`: <*integer*> number of `\XFA` tags found in the PDF. *XFA* stands for *Adobe XML Forms Architecture* and gives support for interactive forms inside the document.
* `xref`: <*integer*> Number of `xref` keywords in the document. That keyword is used to define the cross-reference table, which contains information that permits random access to indirect objects within the file so that the entire file need not be read to locate any particular object.

```json Acrobat PDF files structure info
{
  "data": {
		...
    "attributes" : {
      ...
      "pdf_info": {
         "acroform": <int>,
         "autoaction": <int>,
         "embedded_file": <int>,
         "encrypted": <int>,
         "flash": <int>,
         "header": "<string>",
         "javascript": <int>,
         "jbig2_compression": <int>,
         "js": <int>,
         "num_endobj": <int>,
         "num_endsctream": <int>,
         "num_launch_actions": <int>,
         "num_obj": <int>,
         "num_object_streams": <int>,
         "num_pages": <int>,
         "num_stream": <int>,
         "openaction": <int>,
         "startxref": <int>,
         "suspicious_colors": <int>,
         "trailer": <int>,
         "xfa": <int>,
         "xref": <int>
      }
    }
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "pdf_info": {
                "acroform": 1,
                "autoaction": 0,
                "embedded_file": 0,
                "encrypted": 0,
                "flash": 0,
                "header": "%PDF-1.6",
                "javascript": 0,
                "jbig2_compression": 0,
                "js": 0,
                "num_endobj": 29,
                "num_endstream": 25,
                "num_launch_actions": 0,
                "num_obj": 29,
                "num_object_streams": 1,
                "num_pages": 2,
                "num_stream": 25,
                "openaction": 0,
                "startxref": 1,
                "suspicious_colors": 0,
                "trailer": 0,
                "xfa": 0,
                "xref": 0
            }
        }
    }
}
```

---

← [openxml_info](file-object-openxml-info.md) · [up](../README.md) · [packers](file-object-peid.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-pdf-info>.*
