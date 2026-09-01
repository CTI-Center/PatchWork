---
title: "class_info"
source: https://gtidocs.virustotal.com/reference/file-object-class-info
slug: file-object-class-info
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:05.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › class_info

---

# class_info

information about Java .class bytecode files.

`class_info` gives information about Java bytecode files.

* `constants`: <*list of strings*> used constants in this class.
* `extends`: <*string*> class that this one inherits.
* `implements`: <*list of strings*> implemented interfaces.
* `methods`: <*list of strings*> methods belonging to the class.
* `name`: <*string*> class name.
* `platform`: <*string*> platform as a string, derived from major and minor version number.
* `provides`: <*list of strings*> provided classes, fields and methods.
* `requires`: <*list of strings*> required classes, fields and methods.

```json Java class
{
  "data": {
		...
    "attributes" : {
      ...
      "class_info": {
        "constants": ["<strings>"],
        "extends": "<string>",
        "implements": ["<strings>"],
        "methods": ["<strings>"],
        "name": "<string>",
        "platform": "<string>",
        "provides": ["<strings>"],
        "requires": ["<strings>"]
      }
    }
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "class_info": {
                "constants": [
                    "StackMap",
                    "equals",
                    "getCurrent",
                    "getTime",
                    "java/lang/Exception",
                    "java/lang/Object",
                    "java/util/Date",
                    "javax/microedition/lcdui/Command",
                    "jimm/Jimm",
                    "setTime",
                    "toString"
                ],
                "extends": "java.lang.Object",
                "implements": [
                    "javax.blabla.blabla.CommandListener"
                ],
                "methods": [
                    "<init>",
                    "a",
                    "a",
                    "commandAction"
                ],
                "name": "al",
                "platform": "1.0.2",
                "provides": [
                    "al.a",
                    "al.commandAction",
                    "al.<init>",
                    "al.a"
                ],
                "requires": [
                    "java.lang.StringBuffer.<init>():void",
                    "java.lang.StringBuffer.toString():java.lang.String",
                    "java.util.Date.<init>():void",
                    "v.a():void",
                    "bz.a(java.lang.String):java.lang.String",
                    "cg",
                    "bb.a(int):java.lang.String",
                    "bb.b:int"
                ]
            }
        }
    }
}
```

---

← [rombios_info](file-object-rombios-info.md) · [up](../README.md) · [bundle_info](file-object-bundle-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-class-info>.*
