---
title: "wireshark"
source: https://gtidocs.virustotal.com/reference/file-object-wireshark
slug: file-object-wireshark
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:59.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › wireshark

---

# wireshark

Metadata produced by Wireshark when acting on the file.

`wireshark` contains metadata produced by the [Wireshark](https://www.wireshark.org/) tool when acting on the file. Only available for PCAP network captures.

The object contains the following fields:

* `dns`: <*list of lists*> list containing DNS requests and their resolutions. Every sublist contains two items:
  * <*string*> domain name to resolve
  * <*list of strings*> IP addresses to which the domain resolved.
* `pcap`: PCAP capture metadata:
  * `Capture duration`: <*string*> duration in seconds.
  * `Data size`: <*string*> human readable size of the PCAP file.
  * `End time`: <*string*> date when the capture was stopped in `%Y-%m-%d %H:%M:%S` [format](http://strftime.org/).
  * `File encapsulation`: <*string*> file encapsulation.
  * `File type`: <*string*> file type (usually `pcap`).
  * `Number of packets`: <*string*> human readable number of packets in the network capture.
  * `Start time`: <*string*> date when the capture was started in `%Y-%m-%d %H:%M:%S` [format](http://strftime.org/).

```json Wireshark metadata
{
    "data": {
        "attributes": {
            "wireshark": {
                "dns": [
                    [
                        "<string>",
                        [
                            "<string>",...
                        ]
                    ],...
                ],
                "pcap": {
                    "Capture duration": "<string>",
                    "Data size": "<string>",
                    "End time": "<string:%Y-%m-%d %H:%M:%S>",
                    "File encapsulation": "<string>",
                    "File type": "<string>",
                    "Number of packets": "<string>",
                    "Start time": "<string:%Y-%m-%d %H:%M:%S>"
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
            "wireshark": {
                "dns": [
                    [
                        "nonexistent.com",
                        []
                    ],
                    [
                        "blablabla.com",
                        [
                            "66.66.66.666",
                            "222.222.222.222"
                        ]
                    ],
                    [
                        "example.com",
                        [
                            "55.66.77.88"
                        ]
                    ]
                ],
                "pcap": {
                    "Capture duration": "3599.812545 seconds",
                    "Data size": "29 MB",
                    "End time": "2020-06-03 23:55:31",
                    "File encapsulation": "Ethernet",
                    "File type": "pcap",
                    "Number of packets": "30 k",
                    "Start time": "2020-06-03 22:55:31"
                }
            }
        }
    }
}
```

---

← [traffic_inspection](file-object-traffic-inspection.md) · [up](../README.md) · [vba_info](file-object-vba-info.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-wireshark>.*
