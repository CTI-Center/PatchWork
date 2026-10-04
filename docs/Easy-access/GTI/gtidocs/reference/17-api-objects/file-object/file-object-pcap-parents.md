---
title: "🔀 pcap_parents"
source: https://gtidocs.virustotal.com/reference/file-object-pcap-parents
slug: file-object-pcap-parents
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:52.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › 🔀 pcap_parents

---

# 🔀-pcap_parents

PCAP files that contain the file.

The *pcap\_parents* relationship returns a list of ***PCAP files containing a given file***. This relationship is only available for Premium API users.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/files/files-relationships.md). The response contains a list of [File](../../03-ioc-investigation/files.md) objects.

```json /files/{file_hash}/pcap_parents
{
  "data": [
    <FILE_OBJECT>,
    <FILE_OBJECT>
    ...
  ],
  "links": {
    "next": "<string>",
    "self": "<string>"
  },
  "meta": {
    "count": <int>,
    "cursor": "<string>"
  }
}
```
```json Example
{
    "data": [
        {
            "attributes": {
                "creation_date": 1587044124,
                "downloadable": true,
                "first_submission_date": 1587049407,
                "last_analysis_date": 1588653326,
                "last_analysis_results": {
                    "ALYac": {
                        "category": "undetected",
                        "engine_name": "ALYac",
                        "engine_update": "20200505",
                        "engine_version": "1.1.1.5",
                        "method": "blacklist",
                        "result": "Trojan.GenericKD.42996961"
                    },
                    "APEX": {
                        "category": "type-unsupported",
                        "engine_name": "APEX",
                        "engine_update": "20200504",
                        "engine_version": "6.18",
                        "method": "blacklist",
                        "result": "Malicious"
                    },
                    "AVG": {
                        "category": "undetected",
                        "engine_name": "AVG",
                        "engine_update": "20200505",
                        "engine_version": "18.4.3895.0",
                        "method": "blacklist",
                        "result": null
                    },
                    "Acronis": {
                        "category": "undetected",
                        "engine_name": "Acronis",
                        "engine_update": "20200422",
                        "engine_version": "1.1.1.75",
                        "method": "blacklist",
                        "result": "suspicious"
                    },
                    "Ad-Aware": {
                        "category": "type-unsupported",
                        "engine_name": "Ad-Aware",
                        "engine_update": "20200505",
                        "engine_version": "3.0.5.370",
                        "method": "blacklist",
                        "result": "Trojan.GenericKD.42996961"
                    },
                    "AegisLab": {
                        "category": "undetected",
                        "engine_name": "AegisLab",
                        "engine_update": "20200505",
                        "engine_version": "4.2",
                        "method": "blacklist",
                        "result": null
                    },
                },
                "last_analysis_stats": {
                    "confirmed-timeout": 0,
                    "failure": 0,
                    "harmless": 0,
                    "malicious": 0,
                    "suspicious": 0,
                    "timeout": 1,
                    "type-unsupported": 2,
                    "undetected": 4
                },
                "last_modification_date": 1591945304,
                "last_submission_date": 1587049407,
                "magic": "tcpdump capture file (little-endian) - version 2.4 (Ethernet, capture length 65535)",
                "md5": "b67828805dfdabf3a823278c3fdd37f7",
                "meaningful_name": "blablabla.pcap",
                "names": [
                    "blablabla.pcap"
                ],
                "packers": {
                    "F-PROT": "CAB, embedded"
                },
                "reputation": 0,
                "sha1": "a97e30d504b3e618fc377640d3e65793f6f37625",
                "sha256": "abfa4d040cfb3cd9e22f2301bf0902330ca3a6031ce6a97324b1f1c31494696c",
                "size": 445440,
                "snort": {
                    "1": {
                        "alert": "(spp_sdf) SDF Combination Alert",
                        "classification": "Senstive Data",
                        "destinations": [
                            "2020-06-26 19:38:37.675293 {PROTO:254} 134.121.111.41 -> 11.3.56.11",
                            "2020-06-26 19:50:24.883513 {PROTO:254} 35.469.582.216 -> 14.6.16.10"
                        ]
                    },
                    "11192": {
                        "alert": "FILE-EXECUTABLE download of executable content",
                        "classification": "Potential Corporate Privacy Violation",
                        "destinations": [
                            "2020-06-26 19:38:35.938402 {TCP} 112.114.441.41:80 -> 16.12.36.10:49591"
                        ]
                    }
                },
                "ssdeep": "12288:GoL4Ene4T/vjLbeCJ6s8eFuiQe5Lb9u4eQae46/:Gwne4TDLbeBiGeo4e6/",
                "suricata": {
                    "2001117": {
                        "alert": "ET DNS Standard query response, Name Error",
                        "classification": "Not Suspicious Traffic",
                        "destinations": [
                            "2020-06-26 20:02:28.173281 {UDP} 14.4.24.1:53 -> 13.3.23.101:58697",
                            "2020-06-26 20:02:29.622088 {UDP} 14.4.24.1:53 -> 13.3.23.101:60726",
                            "2020-06-26 20:02:31.030388 {UDP} 14.4.24.1:53 -> 13.3.23.101:54013",
                            "2020-06-26 20:18:26.441699 {UDP} 14.4.24.1:53 -> 13.3.23.101:64220",
                            "2020-06-26 20:18:26.600937 {UDP} 14.4.24.1:53 -> 13.3.23.101:52739",
                            "2020-06-26 20:18:26.600937 {UDP} 14.4.24.1:53 -> 13.3.23.101:52739"
                        ]
                    }
                },
                "tags": [
                    "cap",
                    "shellcode",
                    "malware",
                    "trojan"
                ],
                "times_submitted": 2,
                "total_votes": {
                    "harmless": 0,
                    "malicious": 0
                },
                "traffic_inspection": {
                    "http": [
                        {
                            "binary_filename": "blablabla.exe",
                            "binary_hash": "cbfg4f04hcfg8cdfe2he2301rfer02r30cvava6s71cfefa9f42eb1f1ce1494696c",
                            "binary_magic": "PE32 executable (DLL) (GUI) Intel 80386, for MS Windows",
                            "datetime": "2020-06-26 19:38:35.590121",
                            "interesting_magic": 1,
                            "method": "GET",
                            "remote_host": "111.1.321.41:80",
                            "response_code": "200",
                            "response_size": 208384,
                            "url": "http://blablabla.com/blabla.exe",
                            "user-agent": "Mozilla/4.0 (compatible; Win32; WinHttp.WinHttpRequest.5)"
                        }
                    ]
                },
                "trid": [
                    {
                        "file_type": "TCPDUMP's style capture (little-endian)",
                        "probability": 100.0
                    }
                ],
                "type_description": "Network capture",
                "type_tag": "cap",
                "unique_sources": 1,
                "wireshark": {
                    "dns": [
                        [
                            "blablabla.com",
                            [
                                "15.23.531.16"
                            ]
                        ],
                        [
                            "22wedz-crate.com",
                            []
                        ],
                        [
                            "48boden-flow.com",
                            []
                        ],
                        [
                            "81spdi-tick.com",
                            []
                        ],
                        [
                            "support.apple.com",
                            [
                                "104.95.64.77"
                            ]
                        ]
                    ],
                    "pcap": {
                        "Capture duration": "3900.204600 seconds",
                        "Data size": "5576 kB",
                        "End time": "2020-06-26 20:43:35",
                        "File encapsulation": "Ethernet",
                        "File type": "pcap",
                        "Number of packets": "6916",
                        "Start time": "2020-06-26 19:38:35"
                    }
                }
            },
            "id": "abfa4d04ecfb8cd9e22e2301bfe902c30caea6071ce6a9742eb1f1ce1494696c",
            "links": {
                "self": "https://www.virustotal.com/api/v3/files/abfa4d04ecfb8cd9e22e2301bfe902c30caea6071ce6a9742eb1f1ce1494696c"
            },
            "type": "file"
        }
    ],
    "links": {
        "self": "https://www.virustotal.com/api/v3/files/cbfg4f04hcfg8cdfe2he2301rfer02r30cvava6s71cfefa9f42eb1f1ce1494696c/pcap_parents?limit=2"
    },
    "meta": {
        "count": 1
    }
}
```

---

← [🔀 overlay_parents](file-object-overlay-parents.md) · [up](../README.md) · [🔀 pe_resource_parents](file-object-pe-resource-parents.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-pcap-parents>.*
