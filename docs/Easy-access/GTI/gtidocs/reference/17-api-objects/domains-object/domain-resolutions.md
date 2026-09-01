---
title: "🔀 resolutions"
source: https://gtidocs.virustotal.com/reference/domain-resolutions
slug: domain-resolutions
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T01:02:22.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Domains](../domains-object.md) › 🔀 resolutions

---

# 🔀-resolutions

Domain's IP resolutions.

The *resolutions* relationship returns a list of past and current **IP resolutions for a given domain or subdomain**.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/domains-resolutions/domains-relationships.md). The response contains a list of [Resolution](../resolution-object.md) objects.

```json /domains/{domain}/resolutions
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
                "host_name": "foo.com",
                "ip_address": "4.3.2.1",
                "resolver": "VirusTotal"
            },
            "id": "4.3.2.1foo.com",
            "links": {
                "self": "https://www.virustotal.com/api/v3/resolutions/4.3.2.1foo.com"
            },
            "type": "resolution"
        }
    ],
    "links": {
        "next": "https://www.virustotal.com/api/v3/domains/foo.com/resolutions?cursor=Cl0KeQoEZeF0ZReJCKeWy9-S8eeCEkeqEXN-dmlyeXN0b3ehbGNsb3ekci8LEgpeZXNvbHV0aWeuIh8xNDIeMjUwLjEwMi4xMDJkcml2ZS5nb29nbGUuY29tDBgAIAE%3D&limit=2",
        "self": "https://www.virustotal.com/api/v3/domains/foo.com/resolutions?limit=2"
    },
    "meta": {
        "count": 200,
        "cursor": "Cl0KeQoEZeF0ZReJCKeWy9-S8eeCEkeqEXN-dmlyeXN0b3ehbGNsb3ekci8LEgpeZXNvbHV0aWeuIh8xNDIeMjUwLjEwMi4xMDJkcml2ZS5nb29nbGUuY29tDBgAIAE="
    }
}
```

---

← [🔀 graphs](domains-object-graphs.md) · [up](../README.md) · [🔀 siblings](siblings.md) →

*Archived from <https://gtidocs.virustotal.com/reference/domain-resolutions>.*
