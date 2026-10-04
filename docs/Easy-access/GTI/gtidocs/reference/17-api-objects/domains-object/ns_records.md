---
title: "🔀 ns_records"
source: https://gtidocs.virustotal.com/reference/ns_records
slug: ns_records
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T02:09:42.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Domains](../domains-object.md) › 🔀 ns_records

---

# 🔀-ns_records

Records NS for the domain.

The *ns\_records* relationship returns a list of all domain's NS records. This relationship is only available for premium API users.

The relationship contains the following context attributes:

* `timestamp`: <*integer*> date when the relationship was created as UTC timestamp.
* `ttl`: <*integer*> time to live.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/domains-resolutions/domains-relationships.md). The response contains a list of [Domains](../domains-object.md) objects.

```json /domains/{domain}/ns_records
{
  "data": [
    {
      "attributes":  <DOMAIN_ATTRIBUTES>,
      "context_attributes": {
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
          "BitDefender": "searchengines",
          "Comodo Valkyrie Verdict": "media sharing",
          "Forcepoint ThreatSeeker": "search engines and portals",
          "sophos": "search engines"
        },
        "creation_date": 874296000,
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
          "harmless": 83,
          "malicious": 0,
          "suspicious": 0,
          "timeout": 0,
          "undetected": 9
        },
        "last_dns_records": [
          {
            "ttl": 21599,
            "type": "AAAA",
            "value": "2001:4860:4802:32::a"
          },
          {
            "ttl": 21599,
            "type": "A",
            "value": "216.239.32.10"
          }
        ],
        "last_dns_records_date": 1601701667,
        "last_modification_date": 1602085156,
        "last_update_date": 1568043544,
        "popularity_ranks": {
          "Cisco Umbrella": {
            "rank": 17779,
            "timestamp": 1602084961
          }
        },
        "registrar": "MarkMonitor Inc.",
        "reputation": -41,
        "tags": [],
        "total_votes": {
          "harmless": 0,
          "malicious": 1
        },
        "whois": "Admin Country: US\nAdmin Organization: Google LLC\nAdmin State/Province: CA\nCreation Date: 1997-09-15T00:00:00-0700\nCreation Date: 1997-09-15T04:00:00Z\nDNSSEC: unsigned\nDomain Name: GOOGLE.COM\nDomain Name: google.com\nDomain Status: clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)\nDomain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited\nDomain Status: clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)\nDomain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited\nDomain Status: clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)\nDomain Status: clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited\nDomain Status: serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)\nDomain Status: serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited\nDomain Status: serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)\nDomain Status: serverTransferProhibited https://icann.org/epp#serverTransferProhibited\nDomain Status: serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)\nDomain Status: serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited\nName Server: NS1.GOOGLE.COM\nName Server: NS2.GOOGLE.COM\nName Server: NS3.GOOGLE.COM\nName Server: NS4.GOOGLE.COM\nName Server: ns1.google.com\nName Server: ns2.google.com\nName Server: ns3.google.com\nName Server: ns4.google.com\nRegistrant Country: US\nRegistrant Email: ca4484b9e50182bds@\nRegistrant Organization: 3307059bbb3149c4\nRegistrant State/Province: b1952dfc047df18a\nRegistrar Abuse Contact Email: abusecomplaints@markmonitor.com\nRegistrar Abuse Contact Phone: +1.2083895740\nRegistrar Abuse Contact Phone: +1.2083895770\nRegistrar IANA ID: 292\nRegistrar Registration Expiration Date: 2028-09-13T00:00:00-0700\nRegistrar URL: http://www.markmonitor.com\nRegistrar WHOIS Server: whois.markmonitor.com\nRegistrar: MarkMonitor Inc.\nRegistrar: MarkMonitor, Inc.\nRegistry Domain ID: 2138514_DOMAIN_COM-VRSN\nRegistry Expiry Date: 2028-09-14T04:00:00Z\nTech Country: US\nTech Organization: Google LLC\nTech State/Province: CA\nUpdated Date: 2019-09-09T08:39:04-0700\nUpdated Date: 2019-09-09T15:39:04Z"
      },
      "context_attributes": {
        "timestamp": 1564619990,
        "ttl": "21599"
      },
      "id": "ns1.google.com",
      "links": {
        "self": "http://www.virustotal.com/api/v3/domains/ns1.google.com"
      },
      "type": "domain"
    }
  ],
  "links": {
    "next": "http://www.virustotal.com/api/v3/domains/virustotal.com/ns_records?cursor=eyJsaW1pdCI6IDEsICJvZmZzZXQiOiAxfQ%3D%3D%0A&limit=1",
    "self": "http://www.virustotal.com/api/v3/domains/virustotal.com/ns_records?limit=1"
  },
  "meta": {
    "count": 4,
    "cursor": "eyJsaW1pdCI6IDEsICJvZmZzZXQiOiAxfQ==\n"
  }
}
```

---

← [🔀 mx_records](mx_records.md) · [up](../README.md) · [🔀 soa_records](soa_records.md) →

*Archived from <https://gtidocs.virustotal.com/reference/ns_records>.*
