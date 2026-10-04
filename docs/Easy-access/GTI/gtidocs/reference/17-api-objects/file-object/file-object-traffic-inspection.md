---
title: "traffic_inspection"
source: https://gtidocs.virustotal.com/reference/file-object-traffic-inspection
slug: file-object-traffic-inspection
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:58.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › traffic_inspection

---

# traffic_inspection

Traffic notions extracted from PCAP network captures.

`traffic_inspection` contains extracted notions, mainly HTTP requests, from PCAP captures.

The object contains a `http` key, which value is a list of dictionaries, each one containing the following fields:

* `binary_hash`: <*string*> downloaded content SHA256.
* `binary_magic`: <*string*> downloaded content file type.
* `datetime`: <*string*> download date in `%Y-%m-%d %H:%M:%S.%f` [format](http://strftime.org/).
* `interesting_magic`: <*integer*>
* `method`: <*string*> HTTP request method.
* `remote_host`: <*string*> request destination, including IP and port.
* `response_code`: <*string*> HTTP response code.
* `response_size`: <*integer*> in bytes.
* `url`: <*string*> request URL.
* `user-agent`: <*string*> client user agent.

```json Traffic inspection info
{
    "data": {
        "attributes": {
            "traffic_inspection": {
                "http": [
                    {
                        "binary_hash": "<string>",
                        "binary_magic": "<string>",
                        "datetime": "<string:%Y-%m-%d %H:%M:%S.%f>",
                        "interesting_magic": <int>,
                        "method": "<string>",
                        "remote_host": "<string>",
                        "response_code": "<string>",
                        "response_size": <int>,
                        "url": "<string>",
                        "user-agent": "<string>"
                    }
                ]
            }
        }
    }
}
```
```json Example
{
    "data": {
        "attributes": {
            "traffic_inspection": {
                "http": [
                    {
                        "binary_hash": "0e735aab56c55e954405cef52a5d9e59935c4a5ea151b85eb5a1cf5b25a50505",
                        "binary_magic": "ASCII text, with very long lines, with no line terminators",
                        "datetime": "2020-06-03 22:56:01.449486",
                        "interesting_magic": 0,
                        "method": "GET",
                        "remote_host": "66.66.66.66:80",
                        "response_code": "200",
                        "response_size": 226132,
                        "url": "http://blablabla.com/blablabla.jpg",
                        "user-agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1)"
                    },
                    {
                        "binary_hash": "0e73f4ab6645649e4402ce452a4d9eb9431c4adea141b8b4b3a14fbb24a20e05",
                        "binary_magic": "ASCII text, with very long lines, with no line terminators",
                        "datetime": "2020-06-03 22:56:32.097305",
                        "interesting_magic": 0,
                        "method": "GET",
                        "remote_host": "66.66.66.66:80",
                        "response_code": "200",
                        "response_size": 226132,
                        "url": "http://blablabla.com/blablabla2.jpg",
                        "user-agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1)"
                    }
                ]
            }
        }
    }
}
```

---

← [suricata](file-object-suricata.md) · [up](../README.md) · [wireshark](file-object-wireshark.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-traffic-inspection>.*
