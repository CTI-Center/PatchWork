---
title: "🔀 mx_records"
source: https://gtidocs.virustotal.com/reference/mx_records
slug: mx_records
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T02:09:41.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Domains](../domains-object.md) › 🔀 mx_records

---

# 🔀-mx_records

Records MX for the domain.

The *mx\_records* relationship returns a list of all domain's MX records. This relationship is only available for premium API users.

The relationship contains the following context attributes:

* `timestamp`: <*integer*> date when the relationship was created as UTC timestamp.
* `priority`: <*integer*> the domain's NX record priority
* `ttl`: <*integer*> time to live.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/domains-resolutions/domains-relationships.md). The response contains a list of [Domains](../domains-object.md) objects.

```json /domains/{domain}/mx_records
{
  "data": [
    {
      "attributes":  <DOMAIN_ATTRIBUTES>,
      "context_attributes": {
        "priority": <integer>,
        "timestamp": <integer>,
        "ttl": <integer>
      },...
    },...
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
        "categories": {
          "BitDefender": "computersandsoftware",
          "Forcepoint ThreatSeeker": "computer security"
        },
        "creation_date": 1032308169,
        "last_analysis_results": {
          "ADMINUSLabs": {
            "category": "harmless",
            "engine_name": "ADMINUSLabs",
            "method": "blacklist",
            "result": "clean"
          },
          "AegisLab WebGuard": {
            "category": "harmless",
            "engine_name": "AegisLab WebGuard",
            "method": "blacklist",
            "result": "clean"
          },
          "AlienVault": {
            "category": "harmless",
            "engine_name": "AlienVault",
            "method": "blacklist",
            "result": "clean"
          }
        },
        "last_analysis_stats": {
          "harmless": 75,
          "malicious": 0,
          "suspicious": 0,
          "timeout": 0,
          "undetected": 0
        },
        "last_dns_records": [
          {
            "ttl": 3599,
            "type": "A",
            "value": "94.23.253.72"
          }
        ],
        "last_dns_records_date": 1599544250,
        "last_modification_date": 1599544250,
        "last_update_date": 1597657021,
        "popularity_ranks": {},
        "registrar": "MarkMonitor Inc.",
        "reputation": 0,
        "tags": [],
        "total_votes": {
          "harmless": 0,
          "malicious": 0
        },
        "whois": "Creation Date: 2002-09-18T00:16:09Z\nDNSSEC: unsigned\nDomain Name: VIRUSTOTAL.COM\nDomain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited\nDomain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited\nDomain Status: clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited\nName Server: NS1.GOOGLE.COM\nName Server: NS2.GOOGLE.COM\nName Server: NS3.GOOGLE.COM\nName Server: NS4.GOOGLE.COM\nRegistrar Abuse Contact Email: abusecomplaints@markmonitor.com\nRegistrar Abuse Contact Phone: +1.2083895740\nRegistrar IANA ID: 292\nRegistrar URL: http://www.markmonitor.com\nRegistrar WHOIS Server: whois.markmonitor.com\nRegistrar: MarkMonitor Inc.\nRegistry Domain ID: 90372641_DOMAIN_COM-VRSN\nRegistry Expiry Date: 2021-09-18T00:16:13Z\nUpdated Date: 2020-08-17T09:37:01Z"
      },
      "context_attributes": {
        "priority": "20",
        "timestamp": 1564619990,
        "ttl": "599"
      },
      "id": "vtmail2.virustotal.com",
      "links": {
        "self": "http://www.virustotal.com/api/v3/domains/vtmail2.virustotal.com"
      },
      "type": "domain"
    }
  ],
  "links": {
    "next": "http://www.virustotal.com/api/v3/domains/virustotal.com/mx_records?cursor=eyJsaW1pdCI6IDEsICJvZmZzZXQiOiAxfQ%3D%3D%0A&limit=1",
    "self": "http://www.virustotal.com/api/v3/domains/virustotal.com/mx_records?limit=1"
  },
  "meta": {
    "count": 2,
    "cursor": "eyJsaW1pdCI6IDEsICJvZmZzZXQiOiAxfQ==\n"
  }
}
```

---

← [🔀 cname_records](cname_records.md) · [up](../README.md) · [🔀 ns_records](ns_records.md) →

*Archived from <https://gtidocs.virustotal.com/reference/mx_records>.*
