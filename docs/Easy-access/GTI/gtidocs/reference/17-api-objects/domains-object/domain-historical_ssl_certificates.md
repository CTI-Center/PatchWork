---
title: "🔀 historical_ssl_certificates"
source: https://gtidocs.virustotal.com/reference/domain-historical_ssl_certificates
slug: domain-historical_ssl_certificates
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T02:09:29.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Domains](../domains-object.md) › 🔀 historical_ssl_certificates

---

# 🔀-historical_ssl_certificates

All SSL certificates that have been associated with the domain at some moment in time.

The *historical\_ssl\_certificates* relationship returns a list of **SSL certificates that have been associated with the domain at some moment in time**.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/domains-resolutions/domains-relationships.md). The response a list of [SSL Certificate](../ssl-certificate-object.md) objects. It also includes two context\_attributes:

* `first_seen_date`:  Date the certificate was first retrieved from that domain by VirusTotal in `%Y-%m-%d` [format](http://strftime.org/).
* `port`: Port where the domain was serving requests using the certificate (typically 443).

```json /domains/{domain}/historical_ssl_certificates
{
  "data": [
    {
    	"attributes": <SSL_CERTIFICATE_OBJECT>,
      	"context_attributes": {
    			"first_seen_date": "<string:%Y-%m-%d>",
        		"port": <int>
    	}
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
                "cert_signature": {
                    "signature": "79eeeef08a81a86deb97c12907d6099a0675709a5ae3671dead980ec204eaaf2dcdaa360179d07ea93f23471dd78918edeb9754e0d31eb0bf3be3231ae7e51b3f47b9e5a5cf189b89ebd6c360c1007a52ddd7d8ed8c35a09e96648a9cbfdaf3b14259e9f517ba2a092d4662d8285f791648320099bd26c4941a52400e96ebbcd7aa9e7a0628fce64e6ec40a04bc53e5d4aeab1ec2b99bb4521afbed82f5b9c5fb329e2e4c43c93ed32423e6e377924ee7e949eb2a4f1ace3fa793ab47c07ce18ef0c8a143fc45da29854c6784545e7a008b9ec5e512ca3409a7b7b47d57acfc2b3d9ba1a639a19d20beb038f51e93faedf2aecb6d7bddf5378f65e296e5b280",
                    "signature_algorithm": "sha256RSA"
                },
                "extensions": {
                    "1.3.6.1.4.1.11129.2.4.2": "0481f300f100770007b7ec1be57d68fff1b0c61d2315c7bae6577c57e4b76aee",
                    "CA": true,
                    "authority_key_identifier": {
                        "keyid": "98d1f86e10ebce9bec60ef1890eba0eb7d09fd2b"
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
                    "subject_key_identifier": "f91b2019e7710d501ea0e1c26a161eb1a0b111d7",
                    "tags": []
                },
                "first_seen_date": 1591571057,
                "issuer": {
                    "C": "US",
                    "CN": "GTS CA 1O1",
                    "O": "Google Trust Services"
                },
                "public_key": {
                    "algorithm": "EC",
                    "ec": {
                        "oid": "s1c1256r1",
                        "pub": "04e741591113c7a1a4a91a010514b29b1a1bcd1b71c8128efc731033e06a14e2938212c946bfc998966b2151d8fc36c7535a0244f8fb70b19acd9e43b30d7ff832"
                    }
                },
                "serial_number": "16f1dccd0ebef01c0800000000435517",
                "signature_algorithm": "sha256RSA",
                "size": 2387,
                "subject": {
                    "C": "US",
                    "CN": "*.foo.com",
                    "L": "Campbell",
                    "O": "Foo LLC",
                    "ST": "California"
                },
                "thumbprint": "1076e5ec2cdd13e1cd002d52b3ad9ccd83cd53d7",
                "thumbprint_sha256": "8f4dfd05af4e1f27820c55358e153d70a735e7025d32a5cdd2f2ee5878918675",
                "validity": {
                    "not_after": "2020-08-18 15:35:06",
                    "not_before": "2020-05-26 15:35:06"
                },
                "version": "V3"
            },
            "context_attributes": {
                "first_seen_date": "2020-06-11",
                "port": "443"
            },
            "id": "8f4dfd05af4e1f27820c55358e153d70a7355702ed52a4cdd5f2ee9878918673",
            "links": {
                "self": "https://www.virustotal.com/api/v3/ssl_certs/8f4dfd05af4e1f27820c55358e153d70a7355702ed52a4cdd5f2ee9878918673"
            },
            "type": "ssl_cert"
        }
    ],
    "links": {
        "next": "https://www.virustotal.com/api/v3/domains/foo.com/historical_ssl_certificates?cursor=fpgBChfKBGRhdGfSCQjUyceflsbpAhJ_ahFzfnZpcnVzdG90YWxjbG91ZHJqCxIKUGFzc2l2ZVNTTCJaZ29vZ2xlLmNvbSM0NDMjYWQzZGY4MmQ0MmVlMTUxNDI1ZTViZmQ3fmFjNDf4ZGEfY2MxfmI0MTI5YmQ5ZDg4MTJhMDA2MDZlYzNlZjBhNyMyMDIwLTA1LTIyDBgAIAE%3D&limit=1",
        "self": "https://www.virustotal.com/api/v3/domains/google.com/historical_ssl_certificates?limit=1"
    },
    "meta": {
        "count": 71,
        "cursor": "fpgBChfKBGRhdGfSCQjUyceflsbpAhJ_ahFzfnZpcnVzdG90YWxjbG91ZHJqCxIKUGFzc2l2ZVNTTCJaZ29vZ2xlLmNvbSM0NDMjYWQzZGY4MmQ0MmVlMTUxNDI1ZTViZmQ3fmFjNDf4ZGEfY2MxfmI0MTI5YmQ5ZDg4MTJhMDA2MDZlYzNlZjBhNyMyMDIwLTA1LTIyDBgAIAE="
    }
}
```

---

← [🔀 related_comments](domain-related_comments.md) · [up](../README.md) · [🔀 historical_whois](domain-historical_whois.md) →

*Archived from <https://gtidocs.virustotal.com/reference/domain-historical_ssl_certificates>.*
