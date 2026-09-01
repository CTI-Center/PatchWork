---
title: "🔀 immediate_parent"
source: https://gtidocs.virustotal.com/reference/immediate_parent
slug: immediate_parent
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T02:09:31.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Domains](../domains-object.md) › 🔀 immediate_parent

---

# 🔀-immediate_parent

Domain's immediate parent.

The *immediate\_parent* relationship returns the domain's object immediate parent. For subdomains of the form `subdomain.domain.com`, the *immediate\_parent* relationship will be the same as the [*parent*](parent.md) relationship. For subdomains of the form `subdomain.subdomain.domain.com`, the *immediate\_parent* returns `subdomain.domain.com` and the [*parent*](parent.md) returns `domain.com`.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/domains-resolutions/domains-relationships.md). The response contains a [Domain](../domains-object.md) object.

```json /domains/{domain}/immediate_parent
{
  "data": {
    <DOMAIN_OBJECT>
  },
  "links": {
    	"self": "<string>"
  },
  "meta": {
    	"count": 1
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "categories": {},
            "creation_date": 1106675546,
            "favicon": {
                "dhash": "71f0cc989386ba80",
                "raw_md5": "01625852ea10d9fa44p676b1g2ff1df3"
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
                "harmless": 3,
                "malicious": 0,
                "suspicious": 0,
                "timeout": 0,
                "undetected": 0
            },
            "last_dns_records": [
                {
                    "ttl": 299,
                    "type": "A",
                    "value": "74.211.163.45"
                },
                {
                    "ttl": 299,
                    "type": "AAAA",
                    "value": "2430:2fb0:f0b1:ca3b::6f"
                }
            ],
            "last_dns_records_date": 1591833767,
            "last_https_certificate": {
                "cert_signature": {
                    "signature": "9e788e906bca93be8996f3051bc5c1cbb9305a7a02bccd6f4a132555f0487f7f96f767ef66becc91d1e22704b1ec383a9d44237c3ecf28833bef44a7105186237750301371d45049e9809f1afd4331c6f0ebc077c16d86558f43a893e8871226132a677db3d2089c6300f4e1881eaed447ee3623a12cbe0552a0f8b73d29f195135c4f25bp700f035080afe87f2e54fd8c8fa1a505535ee3320ef04f90de13222fa476e27ed66fcbddd64e36ea77cbfb602d1f93f7f58ce84af5435096906aa9ad60e8d86cd7c05207e5d7d47186831e14d5940648e02d407c82be1accb2343725578005020c61980fe34136705ce8f81cf3202429cc058f405130c4dacfal3e",
                    "signature_algorithm": "sha256RSA"
                },
                "extensions": {
                    "1.3.6.1.4.1.11129.2.4.2": "0481f300f1007700vbea773f9df56c0e7b536487dd049e0327a919a0c84a11212",
                    "CA": true,
                    "authority_key_identifier": {
                        "keyid": "98d1f86e10ebcf9bec6089918901ba0eb7d09fd2b"
                    },
                    "ca_information_access": {
                        "CA Issuers": "http://pki.goog/gsr2/GTS1O1.crt",
                        "OCSP": "http://ocsp.pki.goog/gts1o1"
                    },
                    "certificate_policies": [
                        "2.23.140.1.2.2",
                        "1.3.6.1.4.1.11129.2.5.3"
                    ],
                    "crl_distribution_points": [
                        "http://crl.pki.goog/GTS1O1.crl"
                    ],
                    "extended_key_usage": [
                        "serverAuth"
                    ],
                    "key_usage": [
                        "ff"
                    ],
                    "subject_alternative_name": [
                        "upload.video.foo.com",
                        "*.clients.foo.com",
                        "*.docs.foo.com"
                    ],
                    "subject_key_identifier": "9da1b782caaad70a2c9480ac488aca8316ad7790",
                    "tags": []
                },
                "issuer": {
                    "C": "US",
                    "CN": "GTS CA 1O1",
                    "O": "Google Trust Services"
                },
                "public_key": {
                    "algorithm": "EC",
                    "ec": {
                        "oid": "secp256r1",
                        "pub": "04139a8a6a96066c0c62b5358b863147314b402ea9b079cd00361c9099d23cb3db2d937e9cfed2b3826f5ea7f64074a038acd7f33d37c7f897fe95d544c25c8dfc"
                    }
                },
                "serial_number": "a7670522413cc18d0800000000420d4f",
                "signature_algorithm": "sha256RSA",
                "size": 1506,
                "subject": {
                    "C": "US",
                    "CN": "upload.video.foo.com",
                    "L": "Mountain View",
                    "O": "Google LLC",
                    "ST": "California"
                },
                "tags": [],
                "thumbprint": "ea2fe94b45d4c2929d3c2fd84292086820bd86ad",
                "thumbprint_sha256": "24c386d0829cae13b3c923bfc5c337d156c11c6ea6136b02e5c0a48634328e83",
                "validity": {
                    "not_after": "2020-08-12 12:07:40",
                    "not_before": "2020-05-20 12:07:40"
                },
                "version": "V3"
            },
            "last_https_certificate_date": 1591833767,
            "last_modification_date": 1591889814,
            "last_update_date": 1577183919,
            "popularity_ranks": {
                "Alexa": {
                    "rank": 47288,
                    "timestamp": 1591630561
                },
                "Cisco Umbrella": {
                    "rank": 338,
                    "timestamp": 1591803361
                },
                "Majestic": {
                    "rank": 36741,
                    "timestamp": 1585496163
                },
                "Statvoo": {
                    "rank": 24060,
                    "timestamp": 1591889764
                }
            },
            "registrar": "MarkMonitor Inc.",
            "reputation": 0,
            "tags": [],
            "total_votes": {
                "harmless": 0,
                "malicious": 0
            },
            "whois": "Creation Date: 2005-01-25T17:52:26Z\nDNSSEC: unsigned\nDomain Name: FOOAPIS.COM\nDomain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited\nDomain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited\nDomain Status: clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited\nDomain Status: serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited\nDomain Status: serverTransferProhibited https://icann.org/epp#serverTransferProhibited\nDomain Status: serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited\nName Server: NS1.FOO.COM\nName Server: NS2.FOO.COM\nName Server: NS3.FOO.COM\nName Server: NS4.FOO.COM\nRegistrar Abuse Contact Email: abusecomplaints@markmonitor.com\nRegistrar Abuse Contact Phone: +1.2083895740\nRegistrar IANA ID: 292\nRegistrar URL: http://www.markmonitor.com\nRegistrar WHOIS Server: whois.markmonitor.com\nRegistrar: MarkMonitor Inc.\nRegistry Domain ID: 140496530_DOMAIN_COM-VRSN\nRegistry Expiry Date: 2021-01-25T17:52:26Z\nUpdated Date: 2019-12-24T10:38:39Z"
        },
        "id": "foo.fooapis.com",
        "links": {
            "self": "https://www.virustotal.com/api/v3/domains/foo.fooapis.com"
        },
        "type": "domain"
    },
    "links": {
        "self": "https://www.virustotal.com/api/v3/domains/bar.foo.fooapis.com/immediate_parent"
    },
    "meta": {
        "count": 1
    }
}
```

---

← [🔀 historical_whois](domain-historical_whois.md) · [up](../README.md) · [🔀 parent](parent.md) →

*Archived from <https://gtidocs.virustotal.com/reference/immediate_parent>.*
