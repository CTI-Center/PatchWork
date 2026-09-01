---
title: "🔀 memory_pattern_domains"
source: https://gtidocs.virustotal.com/reference/file-object-memory-pattern-domains
slug: file-object-memory-pattern-domains
section: reference
group: "API OBJECTS"
updatedAt: 2026-06-22T14:05:01.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › 🔀 memory_pattern_domains

---

# 🔀-memory_pattern_domains

Domains extracted from the memory pattern of the file.

The *memory\_pattern\_domains* relationship returns the list of ***all domains includded in the memory pattern of a given file***. This relationship is only available for Premium API users.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/files/files-relationships.md). The response contains a list of [Domain](../domains-object.md) objects.

```json /files/{file_hash}/memory_pattern_domains
{
  "data": [
    <DOMAIN_OBJECT>,
    <DOMAIN_OBJECT>
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
      "id": "ac.ecosia.org",
      "type": "domain",
      "links": {
        "self": "https://www.virustotal.com/api/v3/domains/ac.ecosia.org"
      },
      "attributes": {
        "total_votes": {
          "harmless": 0,
          "malicious": 0
        },
        "popularity_ranks": {
          "Cisco Umbrella": {
            "rank": 47714,
            "timestamp": 1732112351
          }
        },
        "first_seen_itw_date": 1639178102,
        "jarm": "29d29d00029d29d00029d29d29d29d00efabaa2e194cf5d86dd52d92433bab",
        "registrar": "Amazon Registrar, Inc.",
        "last_analysis_results": {
          "Acronis": {
            "method": "blacklist",
            "engine_name": "Acronis",
            "category": "harmless",
            "result": "clean"
          },
          "0xSI_f33d": {
            "method": "blacklist",
            "engine_name": "0xSI_f33d",
            "category": "undetected",
            "result": "unrated"
          },
          "Abusix": {
            "method": "blacklist",
            "engine_name": "Abusix",
            "category": "harmless",
            "result": "clean"
          },
          "ADMINUSLabs": {
            "method": "blacklist",
            "engine_name": "ADMINUSLabs",
            "category": "harmless",
            "result": "clean"
          },
          "Axur": {
            "method": "blacklist",
            "engine_name": "Axur",
            "category": "undetected",
            "result": "unrated"
          },
          "Criminal IP": {
            "method": "blacklist",
            "engine_name": "Criminal IP",
            "category": "harmless",
            "result": "clean"
          },
          "AILabs (MONITORAPP)": {
            "method": "blacklist",
            "engine_name": "AILabs (MONITORAPP)",
            "category": "harmless",
            "result": "clean"
          },
          "AlienVault": {
            "method": "blacklist",
            "engine_name": "AlienVault",
            "category": "harmless",
            "result": "clean"
          },
          "alphaMountain.ai": {
            "method": "blacklist",
            "engine_name": "alphaMountain.ai",
            "category": "harmless",
            "result": "clean"
          },
          "AlphaSOC": {
            "method": "blacklist",
            "engine_name": "AlphaSOC",
            "category": "undetected",
            "result": "unrated"
          },
          "Antiy-AVL": {
            "method": "blacklist",
            "engine_name": "Antiy-AVL",
            "category": "harmless",
            "result": "clean"
          },
          "ArcSight Threat Intelligence": {
            "method": "blacklist",
            "engine_name": "ArcSight Threat Intelligence",
            "category": "undetected",
            "result": "unrated"
          },
          "AutoShun": {
            "method": "blacklist",
            "engine_name": "AutoShun",
            "category": "undetected",
            "result": "unrated"
          },
          "benkow.cc": {
            "method": "blacklist",
            "engine_name": "benkow.cc",
            "category": "harmless",
            "result": "clean"
          },
          "Bfore.Ai PreCrime": {
            "method": "blacklist",
            "engine_name": "Bfore.Ai PreCrime",
            "category": "undetected",
            "result": "unrated"
          },
          "BitDefender": {
            "method": "blacklist",
            "engine_name": "BitDefender",
            "category": "harmless",
            "result": "clean"
          },
          "Bkav": {
            "method": "blacklist",
            "engine_name": "Bkav",
            "category": "undetected",
            "result": "unrated"
          },
          "Blueliv": {
            "method": "blacklist",
            "engine_name": "Blueliv",
            "category": "harmless",
            "result": "clean"
          },
          "Certego": {
            "method": "blacklist",
            "engine_name": "Certego",
            "category": "harmless",
            "result": "clean"
          },
          "Chong Lua Dao": {
            "method": "blacklist",
            "engine_name": "Chong Lua Dao",
            "category": "harmless",
            "result": "clean"
          },
          "CINS Army": {
            "method": "blacklist",
            "engine_name": "CINS Army",
            "category": "harmless",
            "result": "clean"
          },
          "Cluster25": {
            "method": "blacklist",
            "engine_name": "Cluster25",
            "category": "undetected",
            "result": "unrated"
          },
          "CRDF": {
            "method": "blacklist",
            "engine_name": "CRDF",
            "category": "harmless",
            "result": "clean"
          },
          "CSIS Security Group": {
            "method": "blacklist",
            "engine_name": "CSIS Security Group",
            "category": "undetected",
            "result": "unrated"
          },
          "Snort IP sample list": {
            "method": "blacklist",
            "engine_name": "Snort IP sample list",
            "category": "harmless",
            "result": "clean"
          },
          "CMC Threat Intelligence": {
            "method": "blacklist",
            "engine_name": "CMC Threat Intelligence",
            "category": "harmless",
            "result": "clean"
          },
          "Cyan": {
            "method": "blacklist",
            "engine_name": "Cyan",
            "category": "undetected",
            "result": "unrated"
          },
          "Cyble": {
            "method": "blacklist",
            "engine_name": "Cyble",
            "category": "harmless",
            "result": "clean"
          },
          "CyRadar": {
            "method": "blacklist",
            "engine_name": "CyRadar",
            "category": "harmless",
            "result": "clean"
          },
          "DNS8": {
            "method": "blacklist",
            "engine_name": "DNS8",
            "category": "harmless",
            "result": "clean"
          },
          "Dr.Web": {
            "method": "blacklist",
            "engine_name": "Dr.Web",
            "category": "harmless",
            "result": "clean"
          },
          "Ermes": {
            "method": "blacklist",
            "engine_name": "Ermes",
            "category": "undetected",
            "result": "unrated"
          },
          "ESET": {
            "method": "blacklist",
            "engine_name": "ESET",
            "category": "harmless",
            "result": "clean"
          },
          "ESTsecurity": {
            "method": "blacklist",
            "engine_name": "ESTsecurity",
            "category": "harmless",
            "result": "clean"
          },
          "EmergingThreats": {
            "method": "blacklist",
            "engine_name": "EmergingThreats",
            "category": "harmless",
            "result": "clean"
          },
          "Emsisoft": {
            "method": "blacklist",
            "engine_name": "Emsisoft",
            "category": "harmless",
            "result": "clean"
          },
          "Forcepoint ThreatSeeker": {
            "method": "blacklist",
            "engine_name": "Forcepoint ThreatSeeker",
            "category": "harmless",
            "result": "clean"
          },
          "Fortinet": {
            "method": "blacklist",
            "engine_name": "Fortinet",
            "category": "harmless",
            "result": "clean"
          },
          "G-Data": {
            "method": "blacklist",
            "engine_name": "G-Data",
            "category": "harmless",
            "result": "clean"
          },
          "GCP Abuse Intelligence": {
            "method": "blacklist",
            "engine_name": "GCP Abuse Intelligence",
            "category": "undetected",
            "result": "unrated"
          },
          "Google Safebrowsing": {
            "method": "blacklist",
            "engine_name": "Google Safebrowsing",
            "category": "harmless",
            "result": "clean"
          },
          "GreenSnow": {
            "method": "blacklist",
            "engine_name": "GreenSnow",
            "category": "harmless",
            "result": "clean"
          },
          "Gridinsoft": {
            "method": "blacklist",
            "engine_name": "Gridinsoft",
            "category": "undetected",
            "result": "unrated"
          },
          "Heimdal Security": {
            "method": "blacklist",
            "engine_name": "Heimdal Security",
            "category": "harmless",
            "result": "clean"
          },
          "Hunt.io Intelligence": {
            "method": "blacklist",
            "engine_name": "Hunt.io Intelligence",
            "category": "undetected",
            "result": "unrated"
          },
          "IPsum": {
            "method": "blacklist",
            "engine_name": "IPsum",
            "category": "harmless",
            "result": "clean"
          },
          "Juniper Networks": {
            "method": "blacklist",
            "engine_name": "Juniper Networks",
            "category": "harmless",
            "result": "clean"
          },
          "Kaspersky": {
            "method": "blacklist",
            "engine_name": "Kaspersky",
            "category": "harmless",
            "result": "clean"
          },
          "Lionic": {
            "method": "blacklist",
            "engine_name": "Lionic",
            "category": "harmless",
            "result": "clean"
          },
          "Lumu": {
            "method": "blacklist",
            "engine_name": "Lumu",
            "category": "undetected",
            "result": "unrated"
          },
          "MalwarePatrol": {
            "method": "blacklist",
            "engine_name": "MalwarePatrol",
            "category": "harmless",
            "result": "clean"
          },
          "MalwareURL": {
            "method": "blacklist",
            "engine_name": "MalwareURL",
            "category": "undetected",
            "result": "unrated"
          },
          "Malwared": {
            "method": "blacklist",
            "engine_name": "Malwared",
            "category": "harmless",
            "result": "clean"
          },
          "Mimecast": {
            "method": "blacklist",
            "engine_name": "Mimecast",
            "category": "undetected",
            "result": "unrated"
          },
          "Netcraft": {
            "method": "blacklist",
            "engine_name": "Netcraft",
            "category": "undetected",
            "result": "unrated"
          },
          "OpenPhish": {
            "method": "blacklist",
            "engine_name": "OpenPhish",
            "category": "harmless",
            "result": "clean"
          },
          "Phishing Database": {
            "method": "blacklist",
            "engine_name": "Phishing Database",
            "category": "harmless",
            "result": "clean"
          },
          "PhishFort": {
            "method": "blacklist",
            "engine_name": "PhishFort",
            "category": "undetected",
            "result": "unrated"
          },
          "PhishLabs": {
            "method": "blacklist",
            "engine_name": "PhishLabs",
            "category": "undetected",
            "result": "unrated"
          },
          "Phishtank": {
            "method": "blacklist",
            "engine_name": "Phishtank",
            "category": "harmless",
            "result": "clean"
          },
          "PREBYTES": {
            "method": "blacklist",
            "engine_name": "PREBYTES",
            "category": "harmless",
            "result": "clean"
          },
          "PrecisionSec": {
            "method": "blacklist",
            "engine_name": "PrecisionSec",
            "category": "undetected",
            "result": "unrated"
          },
          "Quick Heal": {
            "method": "blacklist",
            "engine_name": "Quick Heal",
            "category": "harmless",
            "result": "clean"
          },
          "Quttera": {
            "method": "blacklist",
            "engine_name": "Quttera",
            "category": "harmless",
            "result": "clean"
          },
          "SafeToOpen": {
            "method": "blacklist",
            "engine_name": "SafeToOpen",
            "category": "undetected",
            "result": "unrated"
          },
          "Sansec eComscan": {
            "method": "blacklist",
            "engine_name": "Sansec eComscan",
            "category": "undetected",
            "result": "unrated"
          },
          "Scantitan": {
            "method": "blacklist",
            "engine_name": "Scantitan",
            "category": "harmless",
            "result": "clean"
          },
          "SCUMWARE.org": {
            "method": "blacklist",
            "engine_name": "SCUMWARE.org",
            "category": "harmless",
            "result": "clean"
          },
          "Seclookup": {
            "method": "blacklist",
            "engine_name": "Seclookup",
            "category": "harmless",
            "result": "clean"
          },
          "SecureBrain": {
            "method": "blacklist",
            "engine_name": "SecureBrain",
            "category": "undetected",
            "result": "unrated"
          }
          "SOCRadar": {
            "method": "blacklist",
            "engine_name": "SOCRadar",
            "category": "undetected",
            "result": "unrated"
          },
          "Sophos": {
            "method": "blacklist",
            "engine_name": "Sophos",
            "category": "harmless",
            "result": "clean"
          },
          "Spam404": {
            "method": "blacklist",
            "engine_name": "Spam404",
            "category": "harmless",
            "result": "clean"
          },
          "StopForumSpam": {
            "method": "blacklist",
            "engine_name": "StopForumSpam",
            "category": "harmless",
            "result": "clean"
          },
          "Sucuri SiteCheck": {
            "method": "blacklist",
            "engine_name": "Sucuri SiteCheck",
            "category": "harmless",
            "result": "clean"
          },
          "ThreatHive": {
            "method": "blacklist",
            "engine_name": "ThreatHive",
            "category": "harmless",
            "result": "clean"
          },
          "LevelBlue": {
            "method": "blacklist",
            "engine_name": "LevelBlue",
            "category": "harmless",
            "result": "clean"
          },
          "URLhaus": {
            "method": "blacklist",
            "engine_name": "URLhaus",
            "category": "harmless",
            "result": "clean"
          },
          "URLQuery": {
            "method": "blacklist",
            "engine_name": "URLQuery",
            "category": "harmless",
            "result": "clean"
          },
          "Viettel Threat Intelligence": {
            "method": "blacklist",
            "engine_name": "Viettel Threat Intelligence",
            "category": "harmless",
            "result": "clean"
          },
          "VIPRE": {
            "method": "blacklist",
            "engine_name": "VIPRE",
            "category": "undetected",
            "result": "unrated"
          },
          "VX Vault": {
            "method": "blacklist",
            "engine_name": "VX Vault",
            "category": "harmless",
            "result": "clean"
          },
          "ViriBack": {
            "method": "blacklist",
            "engine_name": "ViriBack",
            "category": "harmless",
            "result": "clean"
          },
          "Webroot": {
            "method": "blacklist",
            "engine_name": "Webroot",
            "category": "harmless",
            "result": "clean"
          },
          "Yandex Safebrowsing": {
            "method": "blacklist",
            "engine_name": "Yandex Safebrowsing",
            "category": "harmless",
            "result": "clean"
          },
          "ZeroCERT": {
            "method": "blacklist",
            "engine_name": "ZeroCERT",
            "category": "harmless",
            "result": "clean"
          },
          "desenmascara.me": {
            "method": "blacklist",
            "engine_name": "desenmascara.me",
            "category": "harmless",
            "result": "clean"
          },
          "malwares.com URL checker": {
            "method": "blacklist",
            "engine_name": "malwares.com URL checker",
            "category": "harmless",
            "result": "clean"
          },
          "securolytics": {
            "method": "blacklist",
            "engine_name": "securolytics",
            "category": "harmless",
            "result": "clean"
          },
          "Xcitium Verdict Cloud": {
            "method": "blacklist",
            "engine_name": "Xcitium Verdict Cloud",
            "category": "harmless",
            "result": "clean"
          },
          "ZeroFox": {
            "method": "blacklist",
            "engine_name": "ZeroFox",
            "category": "undetected",
            "result": "unrated"
          }
        },
        "creation_date": 1254665324,
        "mandiant_ic_score": 10,
        "categories": {},
        "tags": [],
        "reputation": 0,
        "threat_severity": {
          "version": "D3",
          "threat_severity_level": "SEVERITY_NONE",
          "threat_severity_data": {
            "domain_rank": "49460"
          },
          "last_analysis_date": "1732061914",
          "level_description": "Severity NONE because it has no detections."
        },
        "last_analysis_date": 1732185090,
        "last_dns_records_date": 1732185397,
        "last_seen_itw_date": 1639178102,
        "tld": "org",
        "last_update_date": 1725488385,
        "last_modification_date": 1732190106,
        "last_https_certificate_date": 1732185397,
        "last_analysis_stats": {
          "malicious": 0,
          "suspicious": 0,
          "undetected": 29,
          "harmless": 65,
          "timeout": 0
        },
        "threat_verdict": "VERDICT_UNDETECTED",
        "last_dns_records": [
          {
            "type": "A",
            "ttl": 60,
            "value": "3.97.61.133"
          },
          {
            "type": "A",
            "ttl": 60,
            "value": "3.96.249.0"
          },
          {
            "type": "A",
            "ttl": 60,
            "value": "3.96.93.7"
          },
          {
            "type": "CNAME",
            "ttl": 60,
            "value": "ca-central-1.prod.ecosia.org"
          },
          {
            "type": "CNAME",
            "ttl": 60,
            "value": "prod.ecosia.org"
          },
          {
            "type": "CNAME",
            "ttl": 60,
            "value": "k8s-eks-fcc82f6e13-1142972146.ca-central-1.elb.amazonaws.com"
          }
        ],
        "last_https_certificate": {
          "cert_signature": {
            "signature_algorithm": "sha256RSA",
            "signature": "6eb8a2b9d820ddc7c09eaff2cbf78596daab0c6af6ab457a53dc0610b7e590202435e9155205024cd754d52aaab053494b7deea58e823f41bacff09218042fc9ea8ae165100be57b7712ebfeab171d3fc27d870f807eb80c44df842dfa82cf11e5ddf545e5b776d236f4edb59e7c70e44b13077c4983d1f437b3d6411235178779abb5f063686924db00ffcd53b11e60c56057dee6d736029dd378e06dbb88bf39ea628d075707ad425f4dd701bbcf1c3bb0dcfee32ed52f01b6fed7c4dd4636ed50e85157dfcc39ac2b55d9481b906d75080273700a0784ebbf2be6db2a23d53e09d6c3d65245d7d642713b4c406f960c4e723b58be900c63e4584fbc92e52b"
          },
          "extensions": {
            "authority_key_identifier": {
              "keyid": "55d9185fd21ccc01e158b4beabd9554201d72e02"
            },
            "subject_key_identifier": "ff29197e8493592b8fac7696eb1142e897f41dee",
            "subject_alternative_name": [
              "ecosia.org",
              "*.ecosia.org",
              "*.ca-central-1.prod.ecosia.org"
            ],
            "certificate_policies": [
              "2.23.140.1.2.1"
            ],
            "key_usage": [
              "digitalSignature",
              "keyEncipherment"
            ],
            "extended_key_usage": [
              "serverAuth",
              "clientAuth"
            ],
            "crl_distribution_points": [
              "http://crl.r2m03.amazontrust.com/r2m03.crl"
            ],
            "ca_information_access": {
              "OCSP": "http://ocsp.r2m03.amazontrust.com",
              "CA Issuers": "http://crt.r2m03.amazontrust.com/r2m03.cer"
            },
            "CA": false,
            "1.3.6.1.4.1.11129.2.4.2": "0482016b0169007600dddcca3495d7e11605e79532fac79ff83d1c50dfdb003a"
          },
          "validity": {
            "not_after": "2025-09-15 23:59:59",
            "not_before": "2024-08-18 00:00:00"
          },
          "size": 1523,
          "version": "V3",
          "public_key": {
            "algorithm": "RSA",
            "rsa": {
              "modulus": "a264335523b3e593e76e52ccfcfd95bf5121c47cb2bcc41a330405ff5d3d4d2ec8783a26aed3b4db55649a7d602784d0c8167952eb67cc8beca75904ea104488a6391b2f6cc37576ecc84ce550ddf54ccf562815b809b96a417700df1778921887e63fee27f3188a1bc87cc731a5ee9352884c89062e7d4bb163c3863638b3e7b49759eead96edda4be41047b9037884d0ef3c38d245cb041367c8f1168c0f54038ac5f3e05e91b5ba463b47f78207c145d8cb91505aad05e5603cffaa22591b4eefe1ab662222b1a68e4d10f4bfd994c7388790d3e3b423b24512001faaae517e939cf8213d974711f0a93b94f932f0e9459b6e7af20d8e3e0ccab8e0d75b9d",
              "exponent": "10001",
              "key_size": 2048
            }
          },
          "thumbprint_sha256": "6f407f92306f216ea10f8a2da908b6b2f170cc8ee1ca610dc48b3cc6473197fb",
          "thumbprint": "3577581e84254e36a3b235299d0dc2e2423b93c6",
          "serial_number": "984da3e4ffeed29016f3e14fb9dfea9",
          "issuer": {
            "C": "US",
            "O": "Amazon",
            "CN": "Amazon RSA 2048 M03"
          },
          "subject": {
            "CN": "ecosia.org"
          }
        },
        "whois": "Admin City: REDACTED FOR PRIVACY\nAdmin Country: REDACTED FOR PRIVACY\nAdmin Organization: REDACTED FOR PRIVACY\nAdmin Postal Code: REDACTED FOR PRIVACY\nAdmin State/Province: REDACTED FOR PRIVACY\nCreation Date: 2009-10-04T14:08:44Z\nDNSSEC: unsigned\nDomain Name: ecosia.org\nDomain Status: clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited\nDomain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited\nDomain Status: clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited\nName Server: NS-1130.AWSDNS-13.ORG\nName Server: NS-1717.AWSDNS-22.CO.UK\nName Server: NS-327.AWSDNS-40.COM\nName Server: NS-815.AWSDNS-37.NET\nName Server: ns-1130.awsdns-13.org\nName Server: ns-1717.awsdns-22.co.uk\nName Server: ns-327.awsdns-40.com\nName Server: ns-815.awsdns-37.net\nRegistrant City: 1f8f4166599d23ee\nRegistrant City: e8faa050f23df84b\nRegistrant Country: GB\nRegistrant Email: 0bfbe1eb6b3ce2f0s@identity-protect.org\nRegistrant Email: f651612a2f356ad3s@\nRegistrant Fax Ext: 1f8f4166599d23ee\nRegistrant Fax Ext: 3432650ec337c945\nRegistrant Fax: 1f8f4166599d23ee\nRegistrant Fax: a4c349958db8f29d\nRegistrant Name: 1f8f4166599d23ee\nRegistrant Name: 907afca70403c309\nRegistrant Oranization: 038a292988566233\nRegistrant Phone Ext: 1f8f4166599d23ee\nRegistrant Phone Ext: 3432650ec337c945\nRegistrant Phone: 1f8f4166599d23ee\nRegistrant Phone: 33d4221f20a0d199\nRegistrant Postal Code: 0c47207fb5546dc6\nRegistrant Postal Code: 1f8f4166599d23ee\nRegistrant State/Province: 0449eb7840e3a030\nRegistrant Street: 1614d10740614cc5\nRegistrant Street: 1f8f4166599d23ee\nRegistrar Abuse Contact Email: trustandsafety@support.aws.com\nRegistrar Abuse Contact Phone: +1.2024422253\nRegistrar IANA ID: 468\nRegistrar Registration Expiration Date: 2025-10-04T14:08:44Z\nRegistrar URL: http://registrar.amazon.com\nRegistrar URL: https://registrar.amazon.com\nRegistrar WHOIS Server: whois.registrar.amazon\nRegistrar WHOIS Server: whois.registrar.amazon.com\nRegistrar: Amazon Registrar, Inc.\nRegistry Admin ID: REDACTED FOR PRIVACY\nRegistry Domain ID: 228cc2b122554b019e061043d98d698c-LROR\nRegistry Expiry Date: 2025-10-04T14:08:44Z\nRegistry Registrant ID: Not Available From Registry\nRegistry Registrant ID: REDACTED FOR PRIVACY\nRegistry Tech ID: Not Available From Registry\nRegistry Tech ID: REDACTED FOR PRIVACY\nTech City: Hayes\nTech City: REDACTED FOR PRIVACY\nTech Country: GB\nTech Country: REDACTED FOR PRIVACY\nTech Email: 0bfbe1eb6b3ce2f0s@identity-protect.org\nTech Organization: Identity Protection Service\nTech Organization: REDACTED FOR PRIVACY\nTech Postal Code: REDACTED FOR PRIVACY\nTech Postal Code: UB3 9TR\nTech State/Province: Middlesex\nTech State/Province: REDACTED FOR PRIVACY\nUpdated Date: 2024-08-30T22:18:54Z\nUpdated Date: 2024-09-04T22:19:45Z",
        "gti_assessment": {
          "verdict": {
            "value": "VERDICT_MALICIOUS"
          },
          "severity": {
            "value": "SEVERITY_HIGH"
          },
          "threat_score": {
            "value": 80
          },
          "contributing_factors": {
            "safebrowsing_verdict": "malicious",
            "mandiant_confidence_score": 80
          },
          "gti_description_cards": {
            "HIGHEST_IMPACT_FACTOR": [
              {
                "influence": "high",
                "title": "Attributed to Mandiant Threat Actor",
                "sub_title": "",
                "collection_type": "threat-actor",
                "related_links": [
                  {
                    "title": "APT1",
                    "url": {
                      "object_type": "collection",
                      "id": "apt1"
                    }
                  }
                ]
              }
            ],
            "TECHNICAL_EVIDENCE": [
              {
                "influence": "medium",
                "title": "Multi-Engine AV Detections: 24",
                "sub_title": "",
                "collection_type": "",
                "related_links": []
              }
            ]
          },
          "description": "This indicator is highly malicious based on Mandiant intelligence and community detections."
        }
      }
    }
  ],
  "meta": {
    "count": 29,
    "cursor": "eyJsaW1pdCI6IDEsICJvZmZzZXQiOiAxfQ=="
  },
  "links": {
    "self": "https://www.virustotal.com/api/v3/files/0f40fa13ff13ac967c3582d2b386a32638306821aed9d914a0f31629d3617fa5/memory_pattern_domains?limit=1",
    "next": "https://www.virustotal.com/api/v3/files/0f40fa13ff13ac967c3582d2b386a32638306821aed9d914a0f31629d3617fa5/memory_pattern_domains?limit=1&cursor=eyJsaW1pdCI6IDEsICJvZmZzZXQiOiAxfQ%3D%3D"
  }
}
```

---

← [🔀 graphs](file-object-graphs.md) · [up](../README.md) · [🔀 memory_pattern_ips](file-object-memory-pattern-ips.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-memory-pattern-domains>.*
