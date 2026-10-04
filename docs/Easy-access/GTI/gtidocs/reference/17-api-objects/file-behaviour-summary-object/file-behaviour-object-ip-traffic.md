---
title: "ip_traffic"
source: https://gtidocs.virustotal.com/reference/file-behaviour-object-ip-traffic
slug: file-behaviour-object-ip-traffic
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:43:06.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files Behaviour](../file-behaviour-summary-object.md) › ip_traffic

---

# ip_traffic

Outgoing connections seen during the execution of the given file.

`ip_traffic` contains a list of **outgoing connections seen during the execution** of a given file. It is a list, every item on the list containing the following fields:

* `destination_ip`: <*string*> IP address.
* `destination_port`: <*integer*> Port number.
* `transport_layer_protocol`: <*string*> One of:
  * `ICMP`
  * `IGMP`
  * `TCP`
  * `UDP`
  * `ESP`
  * `AH`
  * `L2TP`
  * `SCTP`

```json IP traffic
{
    "data": {
        "attributes": {
            "dns_lookups": [
                {
                    "destination_ip": "<string>",
                    "destination_port": <int>,
                    "transport_layer_protocol": "<string>"
                }
            ]
        }
    }
}
```
```json Example
{
    "data": {
        "attributes": {
            "dns_lookups": [
                {
                    "destination_ip": "66.66.66.66",
                    "destination_port": 80,
                    "transport_layer_protocol": "TCP"
                }
            ]
        }
    }
}
```

---

← [dns_lookups](file-behaviour-object-dns-lookup.md) · [up](../README.md) · [processes_tree](file-behaviour-object-processes-tree.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-behaviour-object-ip-traffic>.*
