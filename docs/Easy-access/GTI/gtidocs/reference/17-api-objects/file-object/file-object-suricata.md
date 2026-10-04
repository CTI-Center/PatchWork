---
title: "suricata"
source: https://gtidocs.virustotal.com/reference/file-object-suricata
slug: file-object-suricata
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:57.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › suricata

---

# suricata

Matched suricata alerts for PCAP network captures.

`suricata` contains a list of matched [Suricata](https://suricata-ids.org/) alerts (Emerging Threats ETPro ruleset) for PCAP network captures.

This object is a dictionary whose keys are the rule name and value is a dictionary containing details about the alert:

* `alert`: <*string*> brief summary about what the alert is detecting.
* `classification`: <*string*> traffic classification (i.e. "Potentially Bad Traffic").
* `destinations`: <`list of strings`> strings in the network captured that matched the rule. Strings start with a date in `%Y-%m-%d %H:%M:%S.%f` [format](http://strftime.org/).

```json Suricata alerts
{
    "data": {
        "attributes": {
            "suricata": {
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
            "suricata": {
                "2002752": {
                    "alert": "ET POLICY Reserved Internal IP Traffic",
                    "classification": "Potentially Bad Traffic",
                    "destinations": [
                        "2020-06-29 12:10:27.000677 {TCP} 192.168.248.10:24268 -> 192.168.70.10:25",
                        "2020-06-29 12:10:27.000687 {TCP} 172.24.70.10:25 -> 192.168.248.10:24268"
                    ]
                },
                "2100527": {
                    "alert": "GPL SCAN same SRC/DST",
                    "classification": "Potentially Bad Traffic",
                    "destinations": [
                        "2020-06-29 12:10:27.000687 [**] [Raw pkt: 00 50 56 89 26 D2 34 0A 98 D4 42 CA 08 00 45 00 00 8E 1C 5C 40 00 7F 06 48 C8 AC 18 46 0A AC 18 ] [pcap file packet: 4]",
                        "2020-06-29 12:10:27.000687 [**] [Raw pkt: 00 00 5E 00 01 1A 00 50 56 89 26 D2 81 00 0F 3C 08 00 45 00 00 45 59 00 40 00 40 06 4B 6D AC 18 ] [pcap file packet: 6]",
                        "2020-06-29 12:10:27.000687 [**] [Raw pkt: 00 50 56 89 26 D2 34 0A 98 D4 42 CA 08 00 45 00 01 29 1C 5D 40 00 7F 06 48 2C AC 18 46 0A AC 18 ] [pcap file packet: 7]",
                        "2020-06-29 12:10:27.000687 [**] [Raw pkt: 00 00 5E 00 01 1A 00 50 56 89 26 D2 81 00 0F 3C 08 00 45 00 00 78 59 01 40 00 40 06 4B 39 AC 18 ] [pcap file packet: 8]",
                        "2020-06-29 12:10:27.000687 [**] [Raw pkt: 00 50 56 89 26 D2 34 0A 98 D4 42 CA 08 00 45 00 00 3D 1C 5E 40 00 7F 06 49 17 AC 18 46 0A AC 18 ] [pcap file packet: 9]",
                        "2020-06-29 12:10:27.000687 [**] [Raw pkt: 00 50 56 89 26 D2 34 0A 98 D4 42 CA 08 00 45 00 00 3D 1C 5E 40 00 7F 06 49 17 AC 18 46 0A AC 18 ] [pcap file packet: 9]"
                    ]
                }
            }
        }
    }
}
```

---

← [snort](file-object-snort.md) · [up](../README.md) · [traffic_inspection](file-object-traffic-inspection.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-suricata>.*
