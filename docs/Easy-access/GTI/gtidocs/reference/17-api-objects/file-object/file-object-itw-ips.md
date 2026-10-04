---
title: "🔀 itw_ips"
source: https://gtidocs.virustotal.com/reference/file-object-itw-ips
slug: file-object-itw-ips
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:42:08.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › 🔀 itw_ips

---

# 🔀-itw_ips

In the wild IP addresses from where the file has been downloaded.

The *itw\_ips* relationship returns a list of ***in the wild IP addresses from which the file has been downloaded.***. We have seen this file being downloaded from these IP addresses. This relationship is only available for Premium API users.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/files/files-relationships.md). The response contains a list of [IP address](../ip-object.md) objects.

```json /files/{file_hash}/itw_ips
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
      "attributes": {
        "as_owner": "Strato AG",
        "asn": 6724,
        "continent": "EU",
        "country": "DE",
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
          "AutoShun": {
            "category": "harmless",
            "engine_name": "AutoShun",
            "method": "blacklist",
            "result": "clean"
          },
        },
        "last_analysis_stats": {
          "harmless": 5,
          "malicious": 0,
          "suspicious": 0,
          "timeout": 0,
          "undetected": 0
        },
        "last_https_certificate": {
          "cert_signature": {
            "signature": "97ef5af5e6e898ba4ec4b04644954ed60ba16b82e6f9c56967b90b5abc9a559bc3a912af382a1073c4793d75749035597b341efec1073c17bd8b5e03714781c6e9f11b1ce39ecc74afcb8319b9f6f1d9f6c484400bd58374fc0addf7d05f743cdba94a21ebee3d4ea074282a7662eec26171092a69fd60158cd72dd647146de7eb8ae2b5db6257588acc98429eb40f6b393fcbad71139ba11671370d41cbb5f6ca6a18506fccf26d05c3c555377d03946d9e01cdefedbd55c66f34276113885a77babb64ccea9fe16bfac6f2be823bce6d698aed09c3cc02c2c39127d6418c21dbacd723d8f5fa465ce72a8778eee58bf5603a8f42d4afc4c10b0470cef4b244",
            "signature_algorithm": "sha256RSA"
          },
          "extensions": {
            "1.3.6.1.4.1.11129.2.4.2": "0481f300f1007700e2694bae26e8e94009e8861bb63b83d43ee7fe7488fba48f",
            "CA": true,
            "authority_key_identifier": {
              "keyid": "a84a6a63047dddbae6d139b7a64565eff3a8eca1"
            },
            "ca_information_access": {
              "CA Issuers": "http://cert.int-x3.letsencrypt.org/",
              "OCSP": "http://ocsp.int-x3.letsencrypt.org"
            },
            "certificate_policies": [
              "2.23.140.1.2.1",
              "1.3.6.1.4.1.44947.1.1.1"
            ],
            "extended_key_usage": [
              "serverAuth",
              "clientAuth"
            ],
            "key_usage": [
              "ff"
            ],
            "subject_alternative_name": [
              "www.ufos-hosting.de"
            ],
            "subject_key_identifier": "f522cd9c9a4ccdf5d1ec3f925013bf1185e0bc0c"
          },
          "issuer": {
            "C": "US",
            "CN": "Let's Encrypt Authority X3",
            "O": "Let's Encrypt"
          },
          "public_key": {
            "algorithm": "RSA",
            "rsa": {
              "exponent": "010001",
              "key_size": 2048,
              "modulus": "00d1722efe2a2605072f27013b4f9371f1926464dc1c4285f38138a523dc09f0b9ae8578aa70934141bf14893921a2b754a5747a7c71ef9a29501f839a2fe3d052b1434a2fbd0d3149eb1bbe4eef14583791ea7cde3bee2babc5f7114a0fe1ab0c5c5f07701330056b510e020154cca0385a93955684d4d99b74904a44e1ad93f035ebe02bd6e9721285855cbe8f6ce4aaf83ade044b6bc8bd8424ce41f21cf72a1d4ce42ae539fb202efcc791ef810fa49e1c791d4edf4fb83f468cc78b76b5f70333280681f034b80613438f1b0a387e3bdb0dd324e63905d96d1dc810498d5d157d12fc87d4dee9b2abc264b5b6bd7b1e00b838735270e614e15c2c72babb99"
            }
          },
          "serial_number": "36feb381e87e4ed9b5ee53c76bdaccfabc0",
          "signature_algorithm": "sha256RSA",
          "size": 1379,
          "subject": {
            "CN": "www.ufos-hosting.de"
          },
          "thumbprint": "b796e1d3210edcf97290e147d1245cfc9a78132c",
          "thumbprint_sha256": "988858e7387a90af438c9d1edad64fa01e0e85666ebf88ae458b1ceb553c5760",
          "validity": {
            "not_after": "2019-10-10 14:36:27",
            "not_before": "2019-07-12 14:36:27"
          },
          "version": "V3"
        },
        "last_https_certificate_date": 1566463571,
        "last_modification_date": 1591890478,
        "network": "81.169.128.0/17",
        "regional_internet_registry": "RIPE NCC",
        "reputation": 0,
        "tags": [],
        "total_votes": {
          "harmless": 0,
          "malicious": 0
        },
        "whois": "NetRange: 31.0.0.0 - 31.255.255.255\nCIDR: 31.0.0.0/8\nNetName: 31-RIPE\nNetHandle: NET-31-0-0-0-1\nParent: ()\nNetType: Allocated to RIPE NCC\nOriginAS: \nOrganization: RIPE Network Coordination Centre (RIPE)\nRegDate: \nUpdated: 2009-03-25\nComment: These addresses have been further assigned to users in\nComment: the RIPE NCC region. Contact information can be found in\nComment: the RIPE database at http://www.ripe.net/whois\nRef: https://rdap.arin.net/registry/ip/31.0.0.0\nResourceLink: https://apps.db.ripe.net/search/query.html\nResourceLink: whois.ripe.net\nOrgName: RIPE Network Coordination Centre\nOrgId: RIPE\nAddress: P.O. Box 10096\nCity: Amsterdam\nStateProv: \nPostalCode: 1001EB\nCountry: NL\nRegDate: \nUpdated: 2013-07-29\nRef: https://rdap.arin.net/registry/entity/RIPE\nReferralServer: whois://whois.ripe.net\nResourceLink: https://apps.db.ripe.net/search/query.html\nOrgTechHandle: RNO29-ARIN\nOrgTechName: RIPE NCC Operations\nOrgTechPhone: +31 20 535 4444 \nOrgTechEmail: hostmaster@ripe.net\nOrgTechRef: https://rdap.arin.net/registry/entity/RNO29-ARIN\nOrgAbuseHandle: ABUSE3850-ARIN\nOrgAbuseName: Abuse Contact\nOrgAbusePhone: +31205354444 \nOrgAbuseEmail: abuse@ripe.net\nOrgAbuseRef: https://rdap.arin.net/registry/entity/ABUSE3850-ARIN\ninetnum: 31.139.365.0 - 31.139.365.255\nnetname: STRATO-RZG-DED\norg: ORG-SRA1-RIPE\ndescr: Strato Rechenzentrum, Berlin\ncountry: DE\nadmin-c: SRDS-RIPE\ntech-c: SRDS-RIPE\nremarks: ************************************************************\nremarks: * Please send abuse complaints to abuse-server@strato.de *\nremarks: * or fax +49-30-88615-755 ONLY. *\nremarks: * Abuse reports to other e-mail addresses will be ignored. *\nremarks: ************************************************************\nstatus: ASSIGNED PA\nmnt-by: STRATO-RZG-MNT\ncreated: 2004-02-03T18:37:52Z\nlast-modified: 2013-07-06T09:34:25Z\nsource: RIPE\norganisation: ORG-SRA1-RIPE\norg-name: Strato AG\norg-type: LIR\naddress: Pascalstrasse 10\naddress: 10587\naddress: Berlin\naddress: GERMANY\nphone: +4930398020\nfax-no: +493039802222\nadmin-c: CM265-RIPE\nabuse-c: SRAC-RIPE\nmnt-ref: RIPE-NCC-HM-MNT\nmnt-ref: STRATO-RZG-MNT\nmnt-by: RIPE-NCC-HM-MNT\nmnt-by: STRATO-RZG-MNT\ncreated: 2004-04-17T11:12:39Z\nlast-modified: 2019-02-06T12:46:35Z\nsource: RIPE # Filtered\nrole: RIPE contact Dedicated Server\naddress: STRATO AG\naddress: Pascalstr. 10\naddress: D-10587 Berlin\naddress: Germany\nphone: +49 30 39802-0\norg: ORG-SRA1-RIPE\nabuse-mailbox: abuse-server@strato.de\nadmin-c: XX1-RIPE\ntech-c: XX1-RIPE\nnic-hdl: SRDS-RIPE\nremarks: ************************************************************\nremarks: * Please send abuse complaints to abuse-server@strato.de *\nremarks: * or fax +49-30-88615-755 ONLY. *\nremarks: * Abuse reports to other e-mail addresses will be ignored. *\nremarks: * *\nremarks: * For peering requests or operational issues please look *\nremarks: * at the information in the AS6724 RIPE database object. *\nremarks: ************************************************************\nmnt-by: STRATO-RZG-MNT\ncreated: 2010-01-15T08:35:31Z\nlast-modified: 2019-02-06T12:47:52Z\nsource: RIPE # Filtered\nroute: 81.169.165.0/24\ndescr: STRATO AG\ndescr: prefix only advertised in case of DDoS\norigin: AS6724\nmnt-by: STRATO-RZG-MNT\ncreated: 2014-02-18T16:19:05Z\nlast-modified: 2014-02-18T16:19:05Z\nsource: RIPE\n",
        "whois_date": 1565760528
      },
      "id": "31.139.365.245",
      "links": {
        "self": "https://www.virustotal.com/api/v3/ip_addresses/31.139.365.245"
      },
      "type": "ip_address"
    }
  ],
  "links": {
    "next": "http://www.virustotal.com/api/v3/files/abfa4d04ecfb8cd9e22e2301bfe902c30caea6071ce6a9742eb1f1ce1494696c/itw_ips?cursor=eyJsaW1pdCI6IDEsICJvZmZzZXQiOiAxfQ%3D%3D%0A&limit=1",
    "self": "http://www.virustotal.com/api/v3/files/abfa4d04ecfb8cd9e22e2301bfe902c30caea6071ce6a9742eb1f1ce1494696c/itw_ips?limit=1"
  },
  "meta": {
    "count": 26,
    "cursor": "eyJsaW1pdCI6IDEsICJvZmZzZXQiOiAxfQ==\n"
  }
}
```

---

← [html_info](file-object-html-info.md) · [up](../README.md) · [🔀 overlay_children](file-object-overlay-children.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-itw-ips>.*
