---
title: "🔀 caa_records"
source: https://gtidocs.virustotal.com/reference/caa_records
slug: caa_records
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T02:09:39.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Domains](../domains-object.md) › 🔀 caa_records

---

# 🔀-caa_records

Records CAA for the domain.

The *caa\_records* relationship returns a list of all domain's CAA records. This relationship is only available for premium API users.

The relationship contains the following context attributes:

* `timestamp`: <*integer*> date when the relationship was created as UTC timestamp.
* `flag`: <*integer*> An unsigned integer between 0-255.
* `tag`: <*string*>: property identifier represented by the record.
* `ttl:` <*integer*> time to live.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/domains-resolutions/domains-relationships.md). The response contains a list of [Domains](../domains-object.md) objects.

```json /domains/{domain}/caa_records
{
  "data": [
    {
      "attributes": <DOMAIN_ATTRIBUTES>,
      "context_attributes": {
        "timestamp": <integer>,
        "flag": <integer>,
        "tag": "<string>",
        "ttl": <integer>
      },...
    },
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
        "categories": {
          "BitDefender": "marketing",
          "Comodo Valkyrie Verdict": "mobile communications",
          "Forcepoint ThreatSeeker": "information technology",
          "sophos": "information technology"
        },
        "creation_date": 1037201127,
        "favicon": {
          "dhash": "0b4351139011312f",
          "raw_md5": "39059c3eec479771a3527fdf2260db6e"
        },
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
          "harmless": 86,
          "malicious": 0,
          "suspicious": 0,
          "timeout": 0,
          "undetected": 8
        },
        "last_dns_records": [
          {
            "ttl": 162,
            "type": "A",
            "value": "151.139.128.10"
          },
          {
            "ttl": 599,
            "type": "TXT",
            "value": "00d1n000002ljihuac"
          },
          {
            "ttl": 599,
            "type": "NS",
            "value": "ns1.as48447.net"
          },
          {
            "expire": 1814400,
            "minimum": 5400,
            "refresh": 1800,
            "retry": 1200,
            "rname": "hostmaster.comodoca.com",
            "serial": 2020081101,
            "ttl": 599,
            "type": "SOA",
            "value": "ns1.as48447.net"
          },
          {
            "ttl": 599,
            "type": "NS",
            "value": "ns3.as48447.net"
          },
          {
            "ttl": 599,
            "type": "TXT",
            "value": "google-site-verification=UE_67ZnSyfCyNcHGoDqJj4XX_sf5fRfKy1uKk4lU62Q"
          },
          {
            "ttl": 599,
            "type": "TXT",
            "value": "v=spf1 mx include:spf.protection.outlook.com include:spf1.comodo.com include:spf2.comodo.com include:spf3.comodo.com include:spf4.comodo.com ip4:168.245.38.113 include:spf.mandrillapp.com include:_spf.salesforce.com -all"
          },
          {
            "priority": 0,
            "ttl": 599,
            "type": "MX",
            "value": "comodoca-com.mail.protection.outlook.com"
          },
          {
            "ttl": 599,
            "type": "NS",
            "value": "ns2.as48447.net"
          }
        ],
        "last_dns_records_date": 1601816721,
        "last_https_certificate": {
          "cert_signature": {
            "signature": "531d8112443131486de87742c80cd4646e7ef5ac45d91b224639be5e7a759a03c790fef386fc4f6a1629b64c9a6deb97de0bfc19df498818a70f4589744dfd2c7ad98c707e305a75741e615a3c7118d0ecb73d378d2ca98774608d7308fb35564cefc7054471752ed37ba217c813b3fe1fdee7085000f0b84ca54fd471a32330dac38534ae147b960227605bc887f7e997b682e3828e00e6a08d0d668469745f059a7401542eeaf4a4ea8ce336be2d3df3f02bca4d479bfbd38af78ea2a418faccdc9b36073ee6eab065c80a7a9ab1efca4633e079a0e08a9de7cd5ee74f73d53ecd1f8fb139f28bec6939188cf55897da53292049def497af5df39707ac574a",
            "signature_algorithm": "sha256RSA"
          },
          "extensions": {
            "1.3.6.1.4.1.11129.2.4.2": "048201670165007500ee4bbdb775ce60bae142691fabe19e66a30f7e5fb072d8",
            "CA": true,
            "authority_key_identifier": {
              "keyid": "2c69ff80c98790ae34e1b4e74c93859940e9a7b2"
            },
            "ca_information_access": {
              "CA Issuers": "http://crt.sectigo.com/SectigoRSAExtendedValidationSecureServerCA.crt",
              "OCSP": "http://ocsp.sectigo.com"
            },
            "certificate_policies": [
              "1.3.6.1.4.1.6449.1.2.1.5.1",
              "2.23.140.1.1"
            ],
            "crl_distribution_points": [
              "http://crl.sectigo.com/SectigoRSAExtendedValidationSecureServerCA.crl"
            ],
            "extended_key_usage": [
              "serverAuth",
              "clientAuth"
            ],
            "key_usage": [
              "ff"
            ],
            "subject_alternative_name": [
              "sectigo.com",
              "comodoca.com",
              "enterprisessl.com",
              "hackerguardian.com",
              "instantssl.com",
              "optimumssl.com",
              "positivessl.com",
              "ssl.comodoca.com",
              "www.comodoca.com",
              "www.enterprisessl.com",
              "www.hackerguardian.com",
              "www.instantssl.com",
              "www.optimumssl.com",
              "www.positivessl.com",
              "www.sectigo.com"
            ],
            "subject_key_identifier": "0ab1dee9864beaf398bf6341c1f6b3073fe396a1",
            "tags": []
          },
          "issuer": {
            "C": "GB",
            "CN": "Sectigo RSA Extended Validation Secure Server CA",
            "L": "Salford",
            "O": "Sectigo Limited",
            "ST": "Greater Manchester"
          },
          "public_key": {
            "algorithm": "RSA",
            "rsa": {
              "exponent": "010001",
              "key_size": 2048,
              "modulus": "00b26cfcecd97c407ad8e934503c08828bb74ccf40273f770227332b62f13130f207db6f0876c980ad6af13d51091a907fcabe13899dd70bb1a0693c0e631cb5ddc67920f31cee1dbc751ec26832826b7e3c7ecaebf82d26d0bb37357e06aa9ecc98f59cc074a11d71ded04e4777bb2cff919f27b9b228d6ca8aad4afaf3eb15c96aeece43cd3f088d39c9221ae216352e29a1d014ba1911babb3fa34068ba3391212ae52fd2479439525339f0b5ea1095dea9be500001b068ea87ec52ce51a54b8d46291c25a491b62fac959fcc82a0d1dcd02783040caa1c5469f3202d9ec4827a5be2751fde7843fd46ae406e84e09e8413b935d1fa3cb24fb19d8f9dc31a51"
            }
          },
          "serial_number": "261b645f45a6e62ff82c0cb0494bef34",
          "signature_algorithm": "sha256RSA",
          "size": 2213,
          "subject": {
            "C": "GB",
            "CN": "sectigo.com",
            "Country": "GB",
            "L": "Salford",
            "O": "Sectigo Limited",
            "OU": "Operations",
            "ST": "Manchester",
            "businessCategory": "Private Organization",
            "postalCode": "M5 3EQ",
            "serialNumber": "04058690",
            "streetAddress": "3rd Floor Building 26"
          },
          "tags": [],
          "thumbprint": "5161d6ddcce13ab64ca77a26e560b2ec86c7a514",
          "thumbprint_sha256": "feb64851436d33561075dec03176f6f2100bfa227083785858047340fb936ad8",
          "validity": {
            "not_after": "2021-07-02 23:59:59",
            "not_before": "2019-07-03 00:00:00"
          },
          "version": "V3"
        },
        "last_https_certificate_date": 1601816721,
        "last_modification_date": 1602152993,
        "last_update_date": 1573280970,
        "popularity_ranks": {
          "Alexa": {
            "rank": 164127,
            "timestamp": 1601998563
          },
          "Cisco Umbrella": {
            "rank": 325,
            "timestamp": 1602084961
          },
          "Majestic": {
            "rank": 123454,
            "timestamp": 1602084964
          },
          "Quantcast": {
            "rank": 251695,
            "timestamp": 1585841767
          },
          "Statvoo": {
            "rank": 92213,
            "timestamp": 1602084964
          }
        },
        "registrar": "CSC CORPORATE DOMAINS, INC.",
        "reputation": -41,
        "tags": [],
        "total_votes": {
          "harmless": 0,
          "malicious": 1
        },
        "whois": "Admin City: Clifton\nAdmin Country: US\nAdmin Email: 46323fe0b45d1456s@comodogroup.com\nAdmin Organization: Comodo Security Solutions, Inc.\nAdmin Postal Code: 07013\nAdmin State/Province: NJ\nCreation Date: 2002-11-13T10:25:27Z\nCreation Date: 2002-11-13T15:25:27Z\nDNSSEC: unsigned\nDomain Name: COMODOCA.COM\nDomain Name: comodoca.com\nDomain Status: clientTransferProhibited http://www.icann.org/epp#clientTransferProhibited\nDomain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited\nName Server: NS1.AS48447.NET\nName Server: NS2.AS48447.NET\nName Server: NS3.AS48447.NET\nName Server: ns1.as48447.net\nName Server: ns2.as48447.net\nName Server: ns3.as48447.net\nRegistrant City: 09f0cc05ebf86495\nRegistrant Country: US\nRegistrant Email: 46323fe0b45d1456s@comodogroup.com\nRegistrant Fax Ext: 3432650ec337c945\nRegistrant Fax: 8b0d9f69cc6ce83a\nRegistrant Name: 9c6c3696f64fa5f8\nRegistrant Organization: a2ee100ebbb3e483\nRegistrant Phone Ext: 3432650ec337c945\nRegistrant Phone: 9e63e183b87545a3\nRegistrant Postal Code: 6c285eafb0c1bbd6\nRegistrant State/Province: 9a233af5b6f71214\nRegistrant Street: a43ae810ee80594c\nRegistrar Abuse Contact Email: domainabuse@cscglobal.com\nRegistrar Abuse Contact Phone: +1.8887802723\nRegistrar Abuse Contact Phone: 8887802723\nRegistrar IANA ID: 299\nRegistrar Registration Expiration Date: 2020-11-13T15:25:27Z\nRegistrar URL: http://www.cscglobal.com/global/web/csc/digital-brand-services.html\nRegistrar URL: www.cscprotectsbrands.com\nRegistrar WHOIS Server: whois.corporatedomains.com\nRegistrar: CSC CORPORATE DOMAINS, INC.\nRegistrar: CSC Corporate Domains, Inc.\nRegistry Domain ID: 92169053_DOMAIN_COM-VRSN\nRegistry Expiry Date: 2020-11-13T15:25:27Z\nSponsoring Registrar IANA ID: 299\nTech City: Clifton\nTech Country: US\nTech Email: 46323fe0b45d1456s@comodogroup.com\nTech Organization: Comodo Security Solutions, Inc.\nTech Postal Code: 07013\nTech State/Province: NJ\nUpdated Date: 2019-11-09T01:29:30Z\nUpdated Date: 2019-11-09T06:29:30Z",
        "whois_date": 1600871554
      },
      "context_attributes": {
        "flag": "0",
        "tag": "issue",
        "timestamp": 1564620459,
        "ttl": "299"
      },
      "id": "comodoca.com",
      "links": {
        "self": "http://www.virustotal.com/api/v3/domains/comodoca.com"
      },
      "type": "domain"
    }
  ],
  "links": {
    "next": "http://www.virustotal.com/api/v3/domains/freedns.afraid.org/caa_records?cursor=eyJsaW1pdCI6IDEsICJvZmZzZXQiOiAxfQ%3D%3D%0A&limit=1",
    "self": "http://www.virustotal.com/api/v3/domains/freedns.afraid.org/caa_records?limit=1"
  },
  "meta": {
    "count": 2,
    "cursor": "eyJsaW1pdCI6IDEsICJvZmZzZXQiOiAxfQ==\n"
  }
}
```

---

← [🔀 urls](domain-urls.md) · [up](../README.md) · [🔀 cname_records](cname_records.md) →

*Archived from <https://gtidocs.virustotal.com/reference/caa_records>.*
