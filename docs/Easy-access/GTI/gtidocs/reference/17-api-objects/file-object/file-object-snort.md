---
title: "snort"
source: https://gtidocs.virustotal.com/reference/file-object-snort
slug: file-object-snort
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:56.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › snort

---

# snort

Matched Snort alerts in PCAP network captures.

`snort` shows matched [Snort](https://www.snort.org/) (Sourcefire VRT ruleset) alerts in PCAP network captures.

This object is a dictionary whose keys are the rule name and value is a dictionary containing details about the alert:

* `alert`: <*string*> brief summary about what the alert is detecting.
* `classification`: <*string*> traffic classification (i.e. "Potentially Bad Traffic").
* `destinations`: <*list of strings*> strings in the network captured that matched the rule. Strings start with a date in `%Y-%m-%d %H:%M:%S.%f` [format](http://strftime.org/).

```json Snort alerts
{
    "data": {
        "attributes": {
            "snort": {
                "<string>": {
                    "alert": "<string>",
                    "classification": "<string>",
                    "destinations": [
                        "<%Y-%m-%d %H:%M:%S.%f> <string>",...
                    ]
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
            "snort": {
                "1325": {
                    "alert": "INDICATOR-SHELLCODE ssh CRC32 overflow filler",
                    "classification": "Executable code was detected",
                    "destinations": [
                        "2020-06-30 04:34:16.973498 {TCP} 192.168.1.3:61131 -> 10.147.25.123:443"
                    ]
                },
                "25329": {
                    "alert": "BROWSER-IE Microsoft Internet Explorer CSS style memory corruption attempt",
                    "classification": "Attempted User Privilege Gain",
                    "destinations": [
                        "2020-06-30 04:34:15.946482 {TCP} 10.147.25.123:80 -> 192.168.1.3:61123"
                    ]
                },
                "41742": {
                    "alert": "POLICY-OTHER external admin access attempt",
                    "classification": "Attempted Administrator Privilege Gain",
                    "destinations": [
                        "2020-06-30 04:34:14.851956 {TCP} 192.168.1.3:61123 -> 10.147.25.123:80",
                        "2020-06-30 04:34:16.860239 {TCP} 192.168.1.3:61128 -> 10.147.25.123:80"
                    ]
                }
            }
        }
    }
}
```

---

← [🔀 submissions](file-object-submissions.md) · [up](../README.md) · [suricata](file-object-suricata.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-snort>.*
