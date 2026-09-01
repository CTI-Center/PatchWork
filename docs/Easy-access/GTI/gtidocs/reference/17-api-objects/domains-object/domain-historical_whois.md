---
title: "🔀 historical_whois"
source: https://gtidocs.virustotal.com/reference/domain-historical_whois
slug: domain-historical_whois
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T02:09:30.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Domains](../domains-object.md) › 🔀 historical_whois

---

# 🔀-historical_whois

All whois records that have been associated with the domain at some moment in time.

The *historical\_whois* relationship returns a list of whois entries that have been associated with the domain at some moment in time.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/domains-resolutions/domains-relationships.md). The response contains a list of [Whois](../whois-object.md) objects.

```json /domains/{domain}/historical_whois
{
  "data": [
    <WHOIS_OBJECT>,
    <WHOIS_OBJECT>,
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
                "first_seen_date": 1570097077,
                "last_updated": 1568043544,
                "registrar_name": "MarkMonitor Inc.",
                "whois_map": {
                    "Creation Date": "1997-09-15T04:00:00Z",
                    "DNSSEC": "unsigned",
                    "Domain Name": "FOO.COM",
                    "Domain Status": "clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited | clientTransferProhibited https://icann.org/epp#clientTransferProhibited | clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited | serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited | serverTransferProhibited https://icann.org/epp#serverTransferProhibited | serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited",
                    "Name Server": "NS1.FOO.COM | NS2.FOO.COM | NS3.FOO.COM | NS4.FOO.COM",
                    "Registrar": "MarkMonitor Inc.",
                    "Registrar Abuse Contact Email": "abusecomplaints@markmonitor.com",
                    "Registrar Abuse Contact Phone": "+1.2011815110",
                    "Registrar IANA ID": "292",
                    "Registrar URL": "http://www.markmonitor.com",
                    "Registrar WHOIS Server": "whois.markmonitor.com",
                    "Registry Domain ID": "2111511_DOMAIN_COM-VRSN",
                    "Registry Expiry Date": "2028-09-14T04:00:00Z",
                    "Updated Date": "2019-09-09T15:39:04Z"
                }
            },
            "id": "c84752a4b19aa80c1a05a180f1cd107413e42b13071f4a1d73d1aa51fba101eb",
            "links": {
                "self": "https://www.virustotal.com/api/v3/whois/c84752a4b19aa80c1a05a180f1cd107413e42b13071f4a1d73d1aa51fba101eb"
            },
            "type": "whois"
        }
    ],
    "links": {
        "self": "https://www.virustotal.com/api/v3/domains/foo.com/historical_whois?limit=10"
    },
    "meta": {
        "count": 1
    }
}
```

---

← [🔀 historical_ssl_certificates](domain-historical_ssl_certificates.md) · [up](../README.md) · [🔀 immediate_parent](immediate_parent.md) →

*Archived from <https://gtidocs.virustotal.com/reference/domain-historical_whois>.*
