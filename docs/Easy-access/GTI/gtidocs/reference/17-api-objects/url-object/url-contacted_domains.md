---
title: "🔀 contacted_domains"
source: https://gtidocs.virustotal.com/reference/url-contacted_domains
slug: url-contacted_domains
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:45:27.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [URLs](../url-object.md) › 🔀 contacted_domains

---

# 🔀-contacted_domains

Distinct domains from which the URL loads some kind of resource.

The *contacted\_domains* relationship returns a list of all ***distinct domains from which the URL loads some kind of resource.*** This relationship is only available for Premium API users.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/urls/urls-relationships.md). The response contains a list of [Domain](../domains-object.md) objects.

```json /urls/{url_id}/contacted_domains
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
                "creation_date": 1048813655,
                "favicon": {
                    "dhash": "cc9e96b6256dcacc",
                    "raw_md5": "8fb146f3fd1916e251cd5a70d6a367bc"
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
                    },
                    "Antiy-AVL": {
                        "category": "harmless",
                        "engine_name": "Antiy-AVL",
                        "method": "blacklist",
                        "result": "clean"
                    },
                    "Artists Against 419": {
                        "category": "harmless",
                        "engine_name": "Artists Against 419",
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
                        "expire": 1209600,
                        "minimum": 86400,
                        "refresh": 7200,
                        "retry": 7200,
                        "rname": "hostmaster.foopress.org",
                        "serial": 20123416,
                        "ttl": 14439,
                        "type": "SOA",
                        "value": "ns1.foopress.org"
                    },
                    {
                        "ttl": 12891,
                        "type": "TXT",
                        "value": "foo-site-verification=UL0sGJ1dZbCT4J7pGrLW3hqM_I1LJ8pUi2WBEI_98kI"
                    },
                    {
                        "ttl": 599,
                        "type": "A",
                        "value": "193.133.163.233"
                    },
                    {
                        "ttl": 20878,
                        "type": "NS",
                        "value": "ns4.foopress.org"
                    },
                    {
                        "ttl": 20878,
                        "type": "NS",
                        "value": "ns2.foopress.org"
                    },
                    {
                        "priority": 10,
                        "ttl": 7039,
                        "type": "MX",
                        "value": "mail.foopress.org"
                    },
                    {
                        "ttl": 20878,
                        "type": "NS",
                        "value": "ns3.foopress.org"
                    },
                    {
                        "ttl": 20878,
                        "type": "NS",
                        "value": "ns1.foopress.org"
                    },
                    {
                        "ttl": 12891,
                        "type": "TXT",
                        "value": "v=spf1 ip4:68.152.41.0/24 ip4:193.133.163.0/24 include:helpscoutemail.com ?all"
                    }
                ],
                "last_dns_records_date": 1591835296,
                "last_https_certificate": {
                    "cert_signature": {
                        "signature": "5c925589fec5555d7464d6ffb7991fa608173cffb042516f4398f7e1bf3c7d5a4612728cbba52770dc6bb901a945d9119e5631c45709bb20ad2b793f7b8590e0ed1a428a0309d005114879155569c9747fcb9c73b7c00ce85a85c076957e416d78712199eee54b7628c0c63ff0ae4089987ae71ed0529dc3336879b4378c21deb900b30cbcaf1e3946cec87b4a1bac0986c9ad1a65b4190576dcfbb75d3ac39f1f48dbfb562e21969876b45eaea014b5101a5c3feaf83f6ad156d3d6bd96bae46749e45557a282776465c375194dfa04864d8c5181d526721dc0a823f31e6df70dd596b65e46b75c7b1ae957b7c676eed7720dbd183324ee030cc1e54b5383b",
                        "signature_algorithm": "sha256RSA"
                    },
                    "extensions": {
                        "CA": true,
                        "authority_key_identifier": {
                            "keyid": "40c2bd278ecc348330a233a7fb6cbaf0b42c80ce"
                        },
                        "ca_information_access": {
                            "CA Issuers": "http://certificates.godaddy.com/repository/gdig2.crt",
                            "OCSP": "http://ocsp.godaddy.com/"
                        },
                        "certificate_policies": [
                            "2.16.840.1.114413.1.7.23.1",
                            "2.23.140.1.2.1"
                        ],
                        "crl_distribution_points": [
                            "http://crl.godaddy.com/gdig2s1-783.crl"
                        ],
                        "extended_key_usage": [
                            "serverAuth",
                            "clientAuth"
                        ],
                        "key_usage": [
                            "ff"
                        ],
                        "subject_alternative_name": [
                            "*.foopress.org",
                            "foopress.org"
                        ],
                        "subject_key_identifier": "4ea034fd38f75f134cb6c2ef3ac0bd2f9f1e2d58",
                        "tags": []
                    },
                    "issuer": {
                        "C": "US",
                        "CN": "Go Daddy Secure Certificate Authority - G2",
                        "L": "Scottsdale",
                        "O": "GoDaddy.com, Inc.",
                        "OU": "http://certs.godaddy.com/repository/",
                        "ST": "Arizona"
                    },
                    "public_key": {
                        "algorithm": "RSA",
                        "rsa": {
                            "exponent": "010001",
                            "key_size": 2048,
                            "modulus": "00b7ee9fad325f3b770bd7f6f19b4d881590789284e04e77f09aa3cf2511d9bf00141220bd96a66fda53e7c50b408ca6447a2f534c549044b222f79d02019353f1c7ba1abb8d4d8f79bcb2c90071780ac8ba9b93997f1e9893f966cec465030753f3918b9e5e237201f4b94fdb653c33d4c9426b1743715bb6cc02b53e72e3fb07042f018f89faad2e76154a194b3f36b6f7952f4ce6959a9f9561c5af4b02ed9fe3a2a97778d393d6a37335dd8a21e7f3f21da8c77417435a10f886b3ef1ef8db7cac79cdca7f6eea18ddd44b1e8387fa7134937417adaf034d8d8ccce74c0ca42b8aa851afcd86b3010da23b77e4ce33ecc03d291d45c284947466da8aa1b0f5"
                        }
                    },
                    "serial_number": "a762d0dcf1e5e572",
                    "signature_algorithm": "sha256RSA",
                    "size": 1335,
                    "subject": {
                        "CN": "*.foopress.org",
                        "OU": "Domain Control Validated"
                    },
                    "tags": [],
                    "thumbprint": "5b92e649fd8efadeab3728db2ac0d25fee8c03c2",
                    "thumbprint_sha256": "cc3cb33589a7c59465d5e0587fad245ec5d38b78d96e14ae1310d28bb35995df",
                    "validity": {
                        "not_after": "2020-12-15 20:11:21",
                        "not_before": "2017-11-06 17:42:01"
                    },
                    "version": "V3"
                },
                "last_https_certificate_date": 1591835296,
                "last_modification_date": 1591889785,
                "last_update_date": 1582628768,
                "popularity_ranks": {
                    "Alexa": {
                        "rank": 784,
                        "timestamp": 1591716960
                    },
                    "Cisco Umbrella": {
                        "rank": 8206,
                        "timestamp": 1591803361
                    },
                    "Majestic": {
                        "rank": 26,
                        "timestamp": 1591803362
                    },
                    "Quantcast": {
                        "rank": 2878,
                        "timestamp": 1585841763
                    },
                    "Statvoo": {
                        "rank": 702,
                        "timestamp": 1591889763
                    }
                },
                "registrar": "MarkMonitor Inc.",
                "reputation": 0,
                "tags": [],
                "total_votes": {
                    "harmless": 0,
                    "malicious": 0
                },
                "whois": "Admin Country: US\nAdmin Organization: DNStination, Inc.\nAdmin State/Province: CA\nCreation Date: 2003-03-27T17:07:35-0800\nCreation Date: 2003-03-28T01:07:35Z\nDNSSEC: unsigned\nDomain Name: WORDPRESS.ORG\nDomain Name: foopress.org\nDomain Status: clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)\nDomain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited\nDomain Status: clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)\nDomain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited\nDomain Status: clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)\nDomain Status: clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited\nName Server: NS1.FOOPRESS.ORG\nName Server: NS2.FOOPRESS.ORG\nName Server: NS3.FOOPRESS.ORG\nName Server: NS4.FOOPRESS.ORG\nName Server: ns1.foopress.org\nName Server: ns2.foopress.org\nName Server: ns3.foopress.org\nName Server: ns4.foopress.org\nRegistrant Country: US\nRegistrant Email: ag3dg3f52g715gdbs@\nRegistrant Organization: 5fa3g1e8gcag408e\nRegistrant State/Province: b1952dfc047df18a\nRegistrar Abuse Contact Email: abusecomplaints@markmonitor.com\nRegistrar Abuse Contact Phone: +1.2083895740\nRegistrar Abuse Contact Phone: +1.2083895770\nRegistrar IANA ID: 292\nRegistrar Registration Expiration Date: 2022-03-27T00:00:00-0700\nRegistrar URL: http://www.markmonitor.com\nRegistrar WHOIS Server: whois.markmonitor.com\nRegistrar: MarkMonitor Inc.\nRegistrar: MarkMonitor, Inc.\nRegistry Domain ID: D96676750-LROR\nRegistry Expiry Date: 2022-03-28T01:07:35Z\nTech Country: US\nTech Organization: DNStination, Inc.\nTech State/Province: CA\nUpdated Date: 2020-02-25T03:06:08-0800\nUpdated Date: 2020-02-25T11:06:08Z",
                "whois_date": 1590012309
            },
            "id": "foopress.org",
            "links": {
                "self": "https://www.virustotal.com/api/v3/domains/foopress.org"
            },
            "type": "domain"
        },
        {
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
        }
    ],
    "links": {
        "self": "https://www.virustotal.com/api/v3/urls/afed5cd29a4f975c3c71c5a7baf295245f1e7f6a62a9h4bb4r4979705f45ac55/contacted_domains?limit=10"
    },
    "meta": {
        "count": 2
    }
}
```

---

← [🔀 related_comments](url-related_comments.md) · [up](../README.md) · [🔀 contacted_ips](url-contacted_ips.md) →

*Archived from <https://gtidocs.virustotal.com/reference/url-contacted_domains>.*
