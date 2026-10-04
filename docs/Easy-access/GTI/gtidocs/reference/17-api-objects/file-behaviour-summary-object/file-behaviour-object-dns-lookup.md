---
title: "dns_lookups"
source: https://gtidocs.virustotal.com/reference/file-behaviour-object-dns-lookup
slug: file-behaviour-object-dns-lookup
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:43:05.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files Behaviour](../file-behaviour-summary-object.md) › dns_lookups

---

# dns_lookups

DNS queries

`dns_lookups` attribute contains a list of **domain name resolutions performed** by a given file. It is a *list of dictionaries*, each one containing the following fields:

* `hostname` <*string*>: hostname of DNS query.
* `resolved_ips` <*list of strings*>: all resolved IP addresses, may be empty on NX domain.

```json DNS lookups
{
    "data": {
        "attributes": {
            "dns_lookups": [
                {
                    "hostname": "<string>",
                    "resolved_ips": [
                        "<string>",...
                    ]
                },...
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
                    "hostname": "blablabla.com",
                    "resolved_ips": [
                        "66.66.66.66"
                    ]
                },
                {
                    "hostname": "example.com",
                }
            ]
        }
    }
}
```

---

← [http_conversations](file-behaviour-object-http-conversations.md) · [up](../README.md) · [ip_traffic](file-behaviour-object-ip-traffic.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-behaviour-object-dns-lookup>.*
