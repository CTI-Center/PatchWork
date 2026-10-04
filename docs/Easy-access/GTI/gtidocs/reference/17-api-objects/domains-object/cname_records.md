---
title: "🔀 cname_records"
source: https://gtidocs.virustotal.com/reference/cname_records
slug: cname_records
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T02:09:40.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Domains](../domains-object.md) › 🔀 cname_records

---

# 🔀-cname_records

Records CNAME for the domain.

The *cname\_records* relationship returns a list of all domain's CNAME records. This relationship is only available for premium API users.

The relationship contains the following context attributes:

* `timestamp`: <*integer*> date when the relationship was created as UTC timestamp.
* `ttl`: <*integer*> time to live.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/domains-resolutions/domains-relationships.md). The response contains a list of [Domains](../domains-object.md) objects.

```json /domains/{domain}/cname_records
{
  "data": [
    {
      "attributes": <DOMAIN_ATTRIBUTES>,
      "context_attributes": {
        "timestamp": <integer>,
        "ttl": <integer>
      },...
    },
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
          "BitDefender": "parked",
          "Forcepoint ThreatSeeker": "search engines and portals"
        },
        "creation_date": 1063044441,
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
          "malicious": 1,
          "suspicious": 0,
          "timeout": 0,
          "undetected": 10
        },
        "last_dns_records": [
          {
            "ttl": 299,
            "type": "A",
            "value": "74.125.34.46"
          }
        ],
        "last_dns_records_date": 1602132707,
        "last_https_certificate": {
          "cert_signature": {
            "signature": "97f9a8c1ee4c83bfd3748a772f185eb557bd056cff899802965f20f2ccfa3891456cbf49d4e693e6fc496dd3dbd0672173f19e8907e061a6de4a61ef17b0dc6ec22c3b731cf9ac9c881d336a02d336370394dc1c547e66dfb13b44d244181a48222c7513157a1fa889a266244ecf94f117d4b3ce6f556e8fb955c863ef915341a4f10940dba3db7a67d9d73ce75876d267beb89283d6abe51bab98810539042b1de958e334c21a8e7cf648cc76b2d87803e8ecdb2d1a1f0951a7ebf33b56413563702af676411f97f09a05def905bd5f591bc93cec55ac155143ae6d35b66fb6cad1d9d09171e5c5f695e998b870a02dc971044bb5aa7c9f5707a6e625d9232e",
            "signature_algorithm": "sha256RSA"
          },
          "extensions": {
            "1.3.6.1.4.1.11129.2.4.2": "0482016c016a00760046a555eb75fa912030b5a28969f4f37d112c4174befd49",
            "CA": true,
            "authority_key_identifier": {
              "keyid": "53ca1759fc6bc003212f1aaee4aaa81c8256da75"
            },
            "ca_information_access": {
              "CA Issuers": "http://cacerts.rapidssl.com/RapidSSLRSACA2018.crt",
              "OCSP": "http://status.rapidssl.com"
            },
            "certificate_policies": [
              "2.16.840.1.114412.1.2",
              "2.23.140.1.2.1"
            ],
            "crl_distribution_points": [
              "http://cdp.rapidssl.com/RapidSSLRSACA2018.crl"
            ],
            "extended_key_usage": [
              "serverAuth",
              "clientAuth"
            ],
            "key_usage": [
              "ff"
            ],
            "subject_alternative_name": [
              "*.virustotal.com",
              "virustotal.com"
            ],
            "subject_key_identifier": "0a6842ac68bb0dbd947a9feeeba8e175b9c795a4",
            "tags": []
          },
          "issuer": {
            "C": "US",
            "CN": "RapidSSL RSA CA 2018",
            "O": "DigiCert Inc",
            "OU": "www.digicert.com"
          },
          "public_key": {
            "algorithm": "RSA",
            "rsa": {
              "exponent": "010001",
              "key_size": 2048,
              "modulus": "00e47d0e51d056c514638839c7d42e94c3d91ce47d2d5a5b37a1c6011867f160fcaf73a2248b3f2e9e2a9d4664e916284770af01cf2b88ae30486e156b4e0483da19c26346749b714f9be6748ee39a276b7654cb5cd690d19d67255fa705585b9a8a6ba169e26219fdf45458d3b0681d151fd56ccca1a8568cfd1f5922c9a5065572b929ef79aca7ffab44be30226b24e8d860b33dc6e4697fd9249d5b5f7df3789580ae16a0a38f89967968afdda20055e3ca9b2ddf26d591a3624baa4cecfb5b546d707afc618c8a332be7e8de66d09cc55e8cd73d0704bfcc5467209318208ad7f4c1c7fe3fbfed1183d8a02eafdcbbd8b9ba2efaa6f9d5d0e625fb11301189"
            }
          },
          "serial_number": "8a5adf368babebb5ee838c919e56042",
          "signature_algorithm": "sha256RSA",
          "size": 1597,
          "subject": {
            "CN": "*.virustotal.com"
          },
          "tags": [],
          "thumbprint": "6e38b6ce7e2bbe35e085e02eb5af4e24f476bfa8",
          "thumbprint_sha256": "34496f6678be2e3b2ee08741a8a001bf73cac7fa31c98df7cfef746bc9542299",
          "validity": {
            "not_after": "2022-02-02 12:00:00",
            "not_before": "2020-01-22 00:00:00"
          },
          "version": "V3"
        },
        "last_https_certificate_date": 1602132707,
        "last_modification_date": 1602152547,
        "last_update_date": 1596792817,
        "popularity_ranks": {
          "Cisco Umbrella": {
            "rank": 229716,
            "timestamp": 1602084970
          }
        },
        "registrar": "MarkMonitor Inc.",
        "reputation": -7,
        "tags": [],
        "total_votes": {
          "harmless": 2,
          "malicious": 1
        },
        "whois": "Admin Country: US\nAdmin Organization: Google LLC\nAdmin State/Province: CA\nCreation Date: 2003-09-08T00:00:00-0700\nCreation Date: 2003-09-08T18:07:21Z\nDNSSEC: unsigned\nDomain Name: GOOGLEHOSTED.COM\nDomain Name: googlehosted.com\nDomain Status: clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)\nDomain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited\nDomain Status: clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)\nDomain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited\nDomain Status: clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)\nDomain Status: clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited\nName Server: NS1.GOOGLE.COM\nName Server: NS2.GOOGLE.COM\nName Server: NS3.GOOGLE.COM\nName Server: NS4.GOOGLE.COM\nName Server: ns1.google.com\nName Server: ns2.google.com\nName Server: ns3.google.com\nName Server: ns4.google.com\nRegistrant Country: US\nRegistrant Email: fb0a32e703cc1013s@\nRegistrant Organization: 3307059bbb3149c4\nRegistrant State/Province: b1952dfc047df18a\nRegistrar Abuse Contact Email: abusecomplaints@markmonitor.com\nRegistrar Abuse Contact Phone: +1.2083895740\nRegistrar Abuse Contact Phone: +1.2083895770\nRegistrar IANA ID: 292\nRegistrar Registration Expiration Date: 2021-09-08T00:00:00-0700\nRegistrar URL: http://www.markmonitor.com\nRegistrar WHOIS Server: whois.markmonitor.com\nRegistrar: MarkMonitor Inc.\nRegistrar: MarkMonitor, Inc.\nRegistry Domain ID: 103257732_DOMAIN_COM-VRSN\nRegistry Expiry Date: 2021-09-08T18:07:21Z\nTech Country: US\nTech Organization: Google LLC\nTech State/Province: CA\nUpdated Date: 2020-08-07T02:33:37-0700\nUpdated Date: 2020-08-07T09:33:37Z"
      },
      "context_attributes": {
        "timestamp": 1586428658,
        "ttl": "3599"
      },
      "id": "ghs-svc-https-c46.ghs-ssl.googlehosted.com",
      "links": {
        "self": "http://www.virustotal.com/api/v3/domains/ghs-svc-https-c46.ghs-ssl.googlehosted.com"
      },
      "type": "domain"
    }
  ],
  "links": {
    "self": "http://www.virustotal.com/api/v3/domains/avs-control.virustotal.com/cname_records?limit=1"
  },
  "meta": {
    "count": 1
  }
}
```

---

← [🔀 caa_records](caa_records.md) · [up](../README.md) · [🔀 mx_records](mx_records.md) →

*Archived from <https://gtidocs.virustotal.com/reference/cname_records>.*
