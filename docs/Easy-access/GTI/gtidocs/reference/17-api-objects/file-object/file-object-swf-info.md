---
title: "swf_info"
source: https://gtidocs.virustotal.com/reference/file-object-swf-info
slug: file-object-swf-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:22.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › swf_info

---

# swf_info

Information about Adobe Shockwave Flash files.

`swf_info` returns information about [Shockwave Flash/Small Web Format files](https://en.wikipedia.org/wiki/SWF).

* `compression`: <*string*> used compression type (i.e. "zlib").
* `duration`: <*float*> length of the media in seconds.
* `file_attributes`: <*list of strings*> specific attributes (i.e. "ActionScript3", "UseGPU").
* `flash_packages`: <*list of strings*> list of used Flash packages.
* `frame_count`: <*integer*> number of frames.
* `frame_size`: <*string*> size of frames in pixels.
* `metadata`: <*string*> content of file XML metadata file.
* `num_swf_tags`: <*string*> number of SWF tags.
* `num_unrecognized_tags`: <*string*> number of unrecognized tags.
* `suspicious_strings`: <*list of strings*> list of found suspicious strings.
* `suspicious_urls`: <*list of strings*> list of found suspicious URLs.
* `version`: <*integer*> SWF version.

```json SWF files
{
  "data": {
		...
    "attributes" : {
      ...
      "swf_info": {
        "compression": "<string>",
        "duration": <float>,
        "file_attributes": ["<strings>"],
        "flash_packages": ["<strings>"],
        "frame_count": <int>,
        "frame_size": "<string>",
        "metadata": "<string>",
        "num_swf_tags": <int>,
        "num_unrecognized_tags": <int>,
        "suspicious_strings": ["<strings>"],
        "suspicious_urls": ["<strings>"],
        "tags": ["<strings>"],
        "version": <int>
      }
    }
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "swf_info": {
                "compression": "zlib",
                "duration": 0.03333333333333333,
                "file_attributes": [
                    "HasMetadata",
                    "ActionScript3",
                    "UseNetwork"
                ],
                "flash_packages": [
                    "flash.accessibility",
                    "flash.display",
                    "flash.errors",
                    "flash.events",
                    "flash.external",
                    "flash.filters"
                ],
                "frame_count": 2,
                "frame_size": "660.0x420.0",
                "metadata": "<rdf:RDF xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'><rdf:Description rdf:about='' xmlns:dc='http://blablabla.org/xxx/elements/1.1'><dc:format>application/x-shockwave-flash</dc:format><dc:title>blablabla</dc:title><dc:description>blablabla</dc:description><dc:publisher>unknown</dc:publisher><dc:creator>unknown</dc:creator><dc:language>EN</dc:language><dc:date>Nov 21, 2009</dc:date></rdf:Description></rdf:RDF>",
                "num_swf_tags": 371,
                "num_unrecognized_tags": 2,
                "suspicious_strings": [
                    "<iframe src=http://www.blablabla.com/count/blabla.ap?id=all width=0 height=0>"
                ],
                "suspicious_urls": [
                    "http://www.blablabla.net/blablabla/index.php"
                ],
                "version": 10
            }
        }
    }
}
```

---

← [rtf_info](file-object-rtf-info.md) · [up](../README.md) · [isoimage_info](file-object-isoimage-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-swf-info>.*
