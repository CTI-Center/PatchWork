---
title: "🔀 memory_pattern_ips"
source: https://gtidocs.virustotal.com/reference/file-object-memory-pattern-ips
slug: file-object-memory-pattern-ips
section: reference
group: "API OBJECTS"
updatedAt: 2026-06-22T14:05:01.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › 🔀 memory_pattern_ips

---

# 🔀-memory_pattern_ips

IPs extracted from the memory pattern of the file.

The *memory\_pattern\_ips* relationship returns the list of ***all IPs includded in the memory pattern of a given file***. This relationship is only available for Premium API users.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/files/files-relationships.md). The response contains a list of [IP address](../ip-object.md) objects.

```json /files/{file_hash}/memory_pattern_ips
{
  "data": [
    <IP_ADDRESS_OBJECT>,
    <IP_ADDRESS_OBJECT>,
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
      "id": "1.1.1.1",
      "type": "ip_address",
      "links": {
        "self": "https://www.virustotal.com/api/v3/ip_addresses/1.1.1.1"
      },
      "attributes": {
        "last_analysis_stats": {
          "malicious": 1,
          "suspicious": 1,
          "undetected": 30,
          "harmless": 62,
          "timeout": 0
        },
        "tags": [
          "suspicious-udp"
        ],
        "whois": "NetRange: 1.0.0.0 - 1.255.255.255\nCIDR: 1.0.0.0/8\nNetName: APNIC-1\nNetHandle: NET-1-0-0-0-1\nParent: ()\nNetType: Allocated to APNIC\nOriginAS: \nOrganization: Asia Pacific Network Information Centre (APNIC)\nRegDate: \nUpdated: 2010-07-30\nComment: This IP address range is not registered in the ARIN database.\nComment: For details, refer to the APNIC Whois Database via\nComment: WHOIS.APNIC.NET or http://wq.apnic.net/apnic-bin/whois.pl\nComment: ** IMPORTANT NOTE: APNIC is the Regional Internet Registry\nComment: for the Asia Pacific region. APNIC does not operate networks\nComment: using this IP address range and is not able to investigate\nComment: spam or abuse reports relating to these addresses. For more\nComment: help, refer to http://www.apnic.net/apnic-info/whois_search2/abuse-and-spamming\nRef: https://rdap.arin.net/registry/ip/1.0.0.0\nResourceLink: http://wq.apnic.net/whois-search/static/search.html\nResourceLink: whois.apnic.net\nOrgName: Asia Pacific Network Information Centre\nOrgId: APNIC\nAddress: PO Box 3646\nCity: South Brisbane\nStateProv: QLD\nPostalCode: 4101\nCountry: AU\nRegDate: \nUpdated: 2012-01-24\nRef: https://rdap.arin.net/registry/entity/APNIC\nReferralServer: whois://whois.apnic.net\nResourceLink: http://wq.apnic.net/whois-search/static/search.html\nOrgAbuseHandle: AWC12-ARIN\nOrgAbuseName: APNIC Whois Contact\nOrgAbusePhone: +61 7 3858 3188 \nOrgAbuseEmail: search-apnic-not-arin@apnic.net\nOrgAbuseRef: https://rdap.arin.net/registry/entity/AWC12-ARIN\nOrgTechHandle: AWC12-ARIN\nOrgTechName: APNIC Whois Contact\nOrgTechPhone: +61 7 3858 3188 \nOrgTechEmail: search-apnic-not-arin@apnic.net\nOrgTechRef: https://rdap.arin.net/registry/entity/AWC12-ARIN\ninetnum: 1.1.1.0 - 1.1.1.255\nnetname: APNIC-LABS\ndescr: APNIC and Cloudflare DNS Resolver project\ndescr: Routed globally by AS13335/Cloudflare\ndescr: Research prefix for APNIC Labs\ncountry: AU\norg: ORG-ARAD1-AP\nadmin-c: AIC3-AP\ntech-c: AIC3-AP\nabuse-c: AA1412-AP\nstatus: ASSIGNED PORTABLE\nremarks: ---------------\nremarks: All Cloudflare abuse reporting can be done via\nremarks: resolver-abuse@cloudflare.com\nremarks: ---------------\nmnt-by: APNIC-HM\nmnt-routes: MAINT-APNICRANDNET\nmnt-irt: IRT-APNICRANDNET-AU\nlast-modified: 2023-04-26T22:57:58Z\nmnt-lower: MAINT-APNICRANDNET\nsource: APNIC\nirt: IRT-APNICRANDNET-AU\naddress: PO Box 3646\naddress: South Brisbane, QLD 4101\naddress: Australia\ne-mail: helpdesk@apnic.net\nabuse-mailbox: helpdesk@apnic.net\nadmin-c: AR302-AP\ntech-c: AR302-AP\nauth: # Filtered\nremarks: helpdesk@apnic.net was validated on 2021-02-09\nmnt-by: MAINT-AU-APNIC-GM85-AP\nlast-modified: 2021-03-09T01:10:21Z\nsource: APNIC\norganisation: ORG-ARAD1-AP\norg-name: APNIC Research and Development\norg-type: LIR\ncountry: AU\naddress: 6 Cordelia St\nphone: +61-7-38583100\nfax-no: +61-7-38583199\ne-mail: helpdesk@apnic.net\nmnt-ref: APNIC-HM\nmnt-by: APNIC-HM\nlast-modified: 2023-09-05T02:15:19Z\nsource: APNIC\nrole: ABUSE APNICRANDNETAU\naddress: PO Box 3646\naddress: South Brisbane, QLD 4101\naddress: Australia\ncountry: ZZ\nphone: +000000000\ne-mail: helpdesk@apnic.net\nadmin-c: AR302-AP\ntech-c: AR302-AP\nnic-hdl: AA1412-AP\nremarks: Generated from irt object IRT-APNICRANDNET-AU\nabuse-mailbox: helpdesk@apnic.net\nmnt-by: APNIC-ABUSE\nlast-modified: 2021-03-09T01:10:22Z\nsource: APNIC\nrole: APNICRANDNET Infrastructure Contact\naddress: 6 Cordelia St\n South Brisbane\n QLD 4101\ncountry: AU\nphone: +61 7 3858 3100\ne-mail: research@apnic.net\nadmin-c: AIC3-AP\ntech-c: AIC3-AP\nnic-hdl: AIC3-AP\nmnt-by: MAINT-APNICRANDNET\nlast-modified: 2024-07-18T04:37:37Z\nsource: APNIC\nroute: 1.1.1.0/24\norigin: AS13335\ndescr: APNIC Research and Development\n 6 Cordelia St\nmnt-by: MAINT-APNICRANDNET\nlast-modified: 2023-04-26T02:42:44Z\nsource: APNIC\n",
        "reputation": 112,
        "last_analysis_date": 1732188282,
        "total_votes": {
          "harmless": 108,
          "malicious": 24
        },
        "last_seen_itw_date": 1732117912,
        "network": "1.1.1.0/24",
        "asn": 13335,
        "threat_severity": {
          "version": "I3",
          "threat_severity_level": "SEVERITY_NONE",
          "threat_severity_data": {
            "num_detections": 1,
            "has_bad_communicating_files_high": true,
            "has_bad_communicating_files_medium": true,
            "belongs_to_bad_collection": true,
            "belongs_to_threat_actor": true
          },
          "last_analysis_date": "1732148658",
          "level_description": "Severity NONE because it has less than 2 detections."
        },
        "last_https_certificate_date": 1732188599,
        "last_https_certificate": {
          "cert_signature": {
            "signature_algorithm": "sha256RSA",
            "signature": "38bcfb5c158113acdfae2488e5eb09995de597f02a99d47a398d2bde4724194d656a6991f831f1424ee409fe8b6cff839c2d3ced89540c2e85330a845601cdd77af85495cccab37e386b28b4de3e061ff16b4ac75937c250833b0a9b7e5b26dd8220791b60ca3099d12f28da9c94b197ecff0757dcda234f176ce9b65eb1c51e36283783d7720b3e17e1242ad6f3d1a64e3a9913d948ffbfe20a865e04db80d8bc4235463e0d7fe4b5df5ad04b25f1929a4a063fb2a57578be98595c13263744cfa44f7dc4f04e71af720ce047cdc9b359b768dffdc8600e32f6adcddf861adcfb336b417d782d1d7b8f2bf051a4b59e56b3f6362ff917d3e224ea8218835d90"
          },
          "extensions": {
            "authority_key_identifier": {
              "keyid": "748580c066c7df37decfbd2937aa031dbeedcd17"
            },
            "subject_key_identifier": "e2c43be3f11e7967ee51bdeeaacff578147937a0",
            "subject_alternative_name": [
              "cloudflare-dns.com",
              "*.cloudflare-dns.com",
              "one.one.one.one",
              "1.0.0.1",
              "1.1.1.1",
              "162.159.36.1",
              "162.159.46.1",
              "2606:4700:4700::1001",
              "2606:4700:4700::1111",
              "2606:4700:4700::64",
              "2606:4700:4700::6400"
            ],
            "certificate_policies": [
              "2.23.140.1.2.2"
            ],
            "key_usage": [
              "digitalSignature",
              "keyAgreement"
            ],
            "extended_key_usage": [
              "serverAuth",
              "clientAuth"
            ],
            "crl_distribution_points": [
              "http://crl3.digicert.com/DigiCertGlobalG2TLSRSASHA2562020CA1-1.crl",
              "http://crl4.digicert.com/DigiCertGlobalG2TLSRSASHA2562020CA1-1.crl"
            ],
            "ca_information_access": {
              "OCSP": "http://ocsp.digicert.com",
              "CA Issuers": "http://cacerts.digicert.com/DigiCertGlobalG2TLSRSASHA2562020CA1-1.crt"
            },
            "CA": false,
            "1.3.6.1.4.1.11129.2.4.2": "0482016901670075004e75a3275c9a10c3385b6cd4df3f52eb1df0e08e1b8d69"
          },
          "validity": {
            "not_after": "2025-01-21 23:59:59",
            "not_before": "2024-07-30 00:00:00"
          },
          "size": 1703,
          "version": "V3",
          "public_key": {
            "algorithm": "EC",
            "ec": {
              "oid": "secp256r1",
              "pub": "3059301306072a8648ce3d020106082a8648ce3d030107034200044caa4cb260c25e823e6335d3ac004f706dc72b2fcd56ab766aac04edfd8dd7d3ff2e1536c07a9e7ecf297940854c80fe2436906c5c869523615d2862816048f0"
            }
          },
          "thumbprint_sha256": "eb7235019f3012b7a8147d56f792963048be997b4f44ffe9377073eade8a86a5",
          "thumbprint": "20071a1616b91b226729c4ee1d71fcdbff22cefd",
          "serial_number": "fc14a6aba8f3e34358f564fb17c522",
          "issuer": {
            "C": "US",
            "O": "DigiCert Inc",
            "CN": "DigiCert Global G2 TLS RSA SHA256 2020 CA1"
          },
          "subject": {
            "C": "US",
            "ST": "California",
            "L": "San Francisco",
            "O": "Cloudflare, Inc.",
            "CN": "cloudflare-dns.com"
          }
        },
        "first_seen_itw_date": 1577959590,
        "jarm": "27d27d27d00027d00042d43d00041df04c41293ba84f6efe3a613b22f983e6",
        "last_modification_date": 1732189484,
        "whois_date": 1730983946,
        "as_owner": "CLOUDFLARENET",
        "mandiant_ic_score": 0,
        "threat_verdict": "VERDICT_UNDETECTED",
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
            "category": "undetected",
            "result": "unrated"
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
            "category": "suspicious",
            "result": "suspicious"
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
          },
          "SOCRadar": {
            "method": "blacklist",
            "engine_name": "SOCRadar",
            "category": "harmless",
            "result": "clean"
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
            "category": "malicious",
            "result": "malicious"
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
            "category": "undetected",
            "result": "unrated"
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
            "mehod": "blacklist",
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
            "category": "undetected",
            "result": "unrated"
          },
          "ZeroFox": {
            "method": "blacklist",
            "engine_name": "ZeroFox",
            "category": "undetected",
            "result": "unrated"
          }
        },
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
    "count": 5,
    "cursor": "eyJsaW1pdCI6IDEsICJvZmZzZXQiOiAxfQ=="
  },
  "links": {
    "self": "https://www.virustotal.com/api/v3/files/0f40fa13ff13ac967c3582d2b386a32638306821aed9d914a0f31629d3617fa5/memory_pattern_ips?limit=1",
    "next": "https://www.virustotal.com/api/v3/files/0f40fa13ff13ac967c3582d2b386a32638306821aed9d914a0f31629d3617fa5/memory_pattern_ips?limit=1&cursor=eyJsaW1pdCI6IDEsICJvZmZzZXQiOiAxfQ%3D%3D"
  }
}
```

---

← [🔀 memory_pattern_domains](file-object-memory-pattern-domains.md) · [up](../README.md) · [🔀 memory_pattern_urls](file-object-memory-pattern-urls.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-memory-pattern-ips>.*
