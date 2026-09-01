---
title: "🔀 embedded_domains"
source: https://gtidocs.virustotal.com/reference/file-object-embedded-domains
slug: file-object-embedded-domains
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:41:39.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › 🔀 embedded_domains

---

# 🔀-embedded_domains

Domain names embedded in the file.

The *embedded\_domains* relationship returns the list of ***all domain names embedded in a given file***. This relationship is only available for Premium API users.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/files/files-relationships.md). The response contains a list of [Domain](../domains-object.md) objects.

```json /files/{file_hash}/embedded_domains
{
  "data": [
    <DOMAIN_OBJECT>,
    <DOMAIN_OBJECT>,
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
                "categories": {},
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
                    },
                    "Antiy-AVL": {
                        "category": "harmless",
                        "engine_name": "Antiy-AVL",
                        "method": "blacklist",
                        "result": "clean"
                    }
                },
                "last_analysis_stats": {
                    "harmless": 4,
                    "malicious": 0,
                    "suspicious": 0,
                    "timeout": 0,
                    "undetected": 0
                },
                "last_dns_records": [
                    {
                        "ttl": 299,
                        "type": "A",
                        "value": "1.2.3.102"
                    },
                    {
                        "ttl": 299,
                        "type": "A",
                        "value": "1.2.3.139"
                    }
                ],
                "last_dns_records_date": 1591971990,
                "last_https_certificate": {
                    "cert_signature": {
                        "signature": "79eeeef08a81a86d0b97c12907d4099a467574945a64671dead9805c204eaaf2dcdaa360179d07ea93f23471dd789188d6b9754e0431eb0bf3be3231ae7051b3f47b9e5a5cf189b89ebd6c360c1007a52ddd7d8ed8c35a09596648a9cbfdaf3b1445949f517ba4a092d4662d8285f791648320099bd26c4941a52400e96ebbcd7aa9e7a0628fce64e6ec40a04bc533e5d4aeab1ec2b99bb4521afbed82f5b9c5fb329e2e4c43c93ed32423e61377924e77e949342a4f1acd3fa793ab47c07ce18ef0c8a143fc45da29854c6784545e7a008b90c5e512ca3449a7b7b44d47acfc2b3d9ba1a639a19d20beb038f51e93faedf2aecb6d7bddf5378f65c29695b280",
                        "signature_algorithm": "sha256RSA"
                    },
                    "extensions": {
                        "1.3.6.1.4.1.11129.2.4.2": "0481f300f100770007b75c1be47d48fff1b4c61d4315c4ba46574c4794b76aee",
                        "CA": true,
                        "authority_key_identifier": {
                            "keyid": "98d1f86e10ebcf9bec609f18901ba0eb7d09fd2b"
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
                            "*.foo.com",
                            "*.bar.com"
                        ],
                        "subject_key_identifier": "f90b2039e77e0d5ecea0eec26ae61ee8a0e1e1d7",
                        "tags": []
                    },
                    "issuer": {
                        "C": "US",
                        "CN": "FOO CA 1O1",
                        "O": "Foo Trust Services"
                    },
                    "public_key": {
                        "algorithm": "EC",
                        "ec": {
                            "oid": "secp256r1",
                            "pub": "04e74159ce13c7e5a4a91e0a0514e29b1a0bce1b71c822eefc73e033e0ea54e29e8232ce46bfc998966e2151defc36c7e35a0244e8fb70be9acd9e43b30d7ff832"
                        }
                    },
                    "serial_number": "56fadcce0ebef0ec08e0e0e0e0e355e7",
                    "signature_algorithm": "sha256RSA",
                    "size": 2387,
                    "subject": {
                        "C": "US",
                        "CN": "*.foo.com",
                        "L": "Campbell",
                        "O": "Foo LLC",
                        "ST": "California"
                    },
                    "tags": [],
                    "thumbprint": "10e6e5ececed1ee1ce002e52bea49ec18ece5ee7",
                    "thumbprint_sha256": "8f4ded05ae4e1fe7820e5535ee153de0a735e70eed32e4cde2f2ee98e89e8673",
                    "validity": {
                        "not_after": "2020-08-18 15:35:06",
                        "not_before": "2020-05-26 15:35:06"
                    },
                    "version": "V3"
                },
                "last_https_certificate_date": 1591971990,
                "last_modification_date": 1591971990,
                "last_update_date": 1568043544,
                "popularity_ranks": {
                    "Cisco Umbrella": {
                        "rank": 1011,
                        "timestamp": 1591889762
                    }
                },
                "registrar": "MarkMonitor Inc.",
                "reputation": 0,
                "tags": [],
                "total_votes": {
                    "harmless": 0,
                    "malicious": 0
                },
                "whois": "Admin Country: US\nAdmin Organization: Foo LLC\nAdmin State/Province: CA\nCreation Date: 1997-09-15T00:00:00-0700\nCreation Date: 1997-09-15T04:00:00Z\nDNSSEC: unsigned\nDomain Name: FOO.COM\nDomain Name: foo.com\nDomain Status: clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)\nDomain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited\nDomain Status: clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)\nDomain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited\nDomain Status: clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)\nDomain Status: clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited\nDomain Status: serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)\nDomain Status: serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited\nDomain Status: serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)\nDomain Status: serverTransferProhibited https://icann.org/epp#serverTransferProhibited\nDomain Status: serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)\nDomain Status: serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited\nName Server: NS1.FOO.COM\nName Server: NS2.FOO.COM\nName Server: NS3.FOO.COM\nName Server: NS4.FOO.COM\nName Server: ns1.foo.com\nName Server: ns2.foo.com\nName Server: ns3.foo.com\nName Server: ns4.foo.com\nRegistrant Country: US\nRegistrant Email: c44484b4e50484b4s@\nRegistrant Organization: 3304049bb43444c4\nRegistrant State/Province: b1952d4c4474f18a\nRegistrar Abuse Contact Email: abusecomplaints@markmonitor.com\nRegistrar Abuse Contact Phone: +1.2083895740\nRegistrar Abuse Contact Phone: +1.2083895770\nRegistrar IANA ID: 292\nRegistrar Registration Expiration Date: 2028-09-13T00:00:00-0700\nRegistrar URL: http://www.markmonitor.com\nRegistrar WHOIS Server: whois.markmonitor.com\nRegistrar: MarkMonitor Inc.\nRegistrar: MarkMonitor, Inc.\nRegistry Domain ID: 2134544_DOMAIN_COM-VRSN\nRegistry Expiry Date: 2028-09-14T04:00:00Z\nTech Country: US\nTech Organization: Foo LLC\nTech State/Province: CA\nUpdated Date: 2019-09-09T08:39:04-0700\nUpdated Date: 2019-09-09T15:39:04Z"
            },
            "id": "bar.foo.com",
            "links": {
                "self": "https://www.virustotal.com/api/v3/domains/bar.foo.com"
            },
            "type": "domain"
        }
    ],
    "links": {
        "next": "https://www.virustotal.com/api/v3/files/abfa4d04ecfb8cd9e22e2301bfe902c30caea6071ce6a9742eb1f1ce1494696c/embedded_domains?cursor=STewei4%3D&limit=1",
        "self": "https://www.virustotal.com/api/v3/files/abfa4d04ecfb8cd9e22e2301bfe902c30caea6071ce6a9742eb1f1ce1494696c/embedded_domains?limit=1"
    },
    "meta": {
        "count": 99,
        "cursor": "STewei4="
    }
}
```

---

← [🔀 email_parents](file-object-email-parents.md) · [up](../README.md) · [🔀 embedded_ips](file-object-embedded-ips.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-embedded-domains>.*
