---
title: "jar_info"
source: https://gtidocs.virustotal.com/reference/file-object-jar-info
slug: file-object-jar-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:13.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › jar_info

---

# jar_info

information about Java Archive files.

`jar_info` returns information about [Java jar files](https://en.wikipedia.org/wiki/JAR_\(file_format\)).

* `filenames`: <*list of strings*> names of contained files.
* `files_by_type`: <*dictionary*> types and amount of each contained file type. Keys are file types and values are how many of each file type there is.
* `manifest`: <*string*> Jar manifest file content.
* `max_date`: <*string*> oldest contained file date in `%Y-%m-%d %H:%M:%S` [format](http://strftime.org/).
* `max_depth`: <*integer*> package's maximum directory depth.
* `min_date`: <*string*> most recent contained file date in `%Y-%m-%d %H:%M:%S` [format](http://strftime.org/).
* `packages`: <*list of strings*> guess of packages used in the package `.class` files.
* `strings`: <*list of strings*> interesting strings found in the package `.class` files.
* `total_dirs`: <*integer*> number of directories in the package.
* `total_files`: <*integer*> number of files in the package.

```json Java .jar files
{
  "data": {
		...
    "attributes" : {
      ...
      "jar_info": {
        "filenames": ["<strings>"],
        "files_by_type": {"<string>": <int>, ... },
        "manifest": "<string>",
        "max_date": "<string:%Y-%m-%d %H:%M:%S>",
        "max_depth": <int>,
        "min_date": "<string:%Y-%m-%d %H:%M:%S>",
        "packages": ["<strings>"],
        "strings": ["<strings>"],
        "total_dirs": <int>,
        "total_files": <int>
      }
    }
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "jar_info": {
                "filenames": [
                    "META-INF/MANIFEST.MF",
                    "net/blabla/blabla/blabla/blabla.class",
                    "net/blabla/blabla/blabla/blabla2.class",
                    "net/blabla/blabla/blabla/blabla3.class"
                ],
                "files_by_type": {
                    "ascii": 490,
                    "binary": 16,
                    "class": 760,
                    "jpg": 2,
                    "ogg": 3,
                    "png": 441
                },
                "manifest": "Manifest-Version: 1.0",
                "max_date": "2020-06-18 20:46:02",
                "max_depth": 5,
                "min_date": "2020-06-18 20:45:58",
                "packages": [
                    "java.io",
                    "java.lang",
                    "java.lang.Comparable<Lnet.blabla.blabla",
                    "java.lang.annotation",
                    "java.lang.invoke",
                    "java.lang.reflect",
                    "java.util",
                    "java.util.HashMap<Ljava.lang"
                ],
                "strings": [
                    ",,,,,,",
                    ",/execute",
                    ",Ljava/util/Set<Lnet/blabla/block/Block",
                    ",Lnet/blabla/client/entity/blabla",
                    ",Lnet/blabla/entity/player/blabla2"
                "total_dirs": 36,
                "total_files": 1712
            }
        }
    }
}
```

---

← [ipa_info](file-object-ipa-info.md) · [up](../README.md) · [javascript_info](file-object-javascript-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-jar-info>.*
