---
title: "🔀 resolutions"
source: https://gtidocs.virustotal.com/reference/ip-object-resolutions
slug: ip-object-resolutions
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:43:36.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [IP addresses](../ip-object.md) › 🔀 resolutions

---

# 🔀-resolutions

Domain resolutions for a IP address.

The *resolutions* relationship returns a list of past and current **domain resolutions for a IP address**.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/ip-addresses/ip-relationships.md). The response contains a list of [Resolution](../resolution-object.md) objects.

```json /ip_addresses/{ip_address}/resolutions
{
  "data": [
    <RESOLUTION_OBJECT>,
    <RESOLUTION_OBJECT>,
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
                "date": 1591813960,
                "host_name": "foo.com",
                "ip_address": "1.2.3.4",
                "resolver": "VirusTotal"
            },
            "id": "1.2.3.4foo.com",
            "links": {
                "self": "https://www.virustotal.com/api/v3/resolutions/1.2.3.4foo.com"
            },
            "type": "resolution"
        },
        {
            "attributes": {
                "date": 1591787179,
                "host_name": "bar.foo.com",
                "ip_address": "1.2.3.4",
                "resolver": "VirusTotal"
            },
            "id": "1.2.3.4bar.foo.com",
            "links": {
                "self": "https://www.virustotal.com/api/v3/resolutions/1.2.3.4bar.foo.com"
            },
            "type": "resolution"
        }
    ],
    "links": {
        "next": "https://www.virustotal.com/api/v3/ip_addresses/1.2.3.4/resolutions?cursor=Cl0KeQoEZeF0ZReJCKeWy9-S8eeCEkeqEXN-dmlyeXN0b3ehbGNsb3ekci8LEgpeZXNvbHV0aWeuIh8xNDIeMjUwLjEwMi4xMDJkcml2ZS5nb29nbGUuY29tDBgAIAE%3D&limit=2",
        "self": "https://www.virustotal.com/api/v3/ip_addresses/1.2.3.4/resolutions?limit=2"
    },
    "meta": {
        "count": 200,
        "cursor": "Cl0KeQoEZeF0ZReJCKeWy9-S8eeCEkeqEXN-dmlyeXN0b3ehbGNsb3ekci8LEgpeZXNvbHV0aWeuIh8xNDIeMjUwLjEwMi4xMDJkcml2ZS5nb29nbGUuY29tDBgAIAE="
    }
}
```

---

← [🔀 referrer_files](ip-object-referrer-files.md) · [up](../README.md) · [🔀 urls](ip-object-urls.md) →

*Archived from <https://gtidocs.virustotal.com/reference/ip-object-resolutions>.*
