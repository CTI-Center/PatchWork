---
title: "IP addresses"
source: https://gtidocs.virustotal.com/reference/ip-object
slug: ip-object
section: reference
group: "API OBJECTS"
updatedAt: 2026-08-26T14:46:16.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › IP addresses

---

# ip-addresses

IPv4 addresses are other of the network locations that Google Threat Intelligence stores information about. A description of the fields stored within these objects follows.

IP addresses are, as domains, network locations related to File and URLs objects in many ways. That is why it is possible to retrieve them by its relationship with other objects, by other means when searching in Enterprise services, or just by searching an already existing IP.

## object-attributes

A IP address object contains the following attributes:

* `as_owner`: <*string*> owner of the Autonomous System to which the IP belongs.
* `asn`: <*integer*> autonomous System Number to which the IP belongs.
* `continent`: <*string*> continent where the IP is placed (ISO-3166 continent code).
* `country`: <*string*> country where the IP is placed (ISO-3166 country code).
* `gti_assessment*`: <*dictionary*> containing the following fields:
  * `verdict`: <*dictionary*>. The `value` property can have any of these values:
    * `VERDICT_BENIGN`: the entity is considered harmless.
    * `VERDICT_UNDETECTED`: no immediate evidence of malicious intent.
    * `VERDICT_SUSPICIOUS`: possible malicious activity detected, requires further investigation.
    * `VERDICT_MALICIOUS`: high confidence that the entity poses a threat.
    * `VERDICT_UNKNOWN`: we were not able to generate a verdict for this entity.
  * `severity`: <*dictionary*>. The `value` property can have any of these values:
    * `SEVERITY_NONE`: this is the level assigned to entities with non-malicious verdict.
    * `SEVERITY_LOW`: the threat likely has a minor impact but should still be monitored
    * `SEVERITY_MEDIUM`: indicates a potential threat that warrants attention.
    * `SEVERITY_HIGH`: immediate action is recommended; the threat could have a critical impact
    * `SEVERITY_UNKNOWN`: not enough data to assess a severity.
  * `description`: <*string*> a human readable description of the factors contributing to the verdict and severity classification.
  * `threat_score`: <*int*> the Google Threat Intelligence score is a function of the Verdict and Severity, and leverages additional internal factors to generate the score. Valid values go from 0 to 100.
  * `contributing_factors`: <*dictionary*> the signals that contributed to the verdict and severity classification.
    * `mandiant_analyst_benign`: <*bool*> the indicator was determined as benign by a Google Threat Intelligence analyst and likely poses no threat.
    * `mandiant_analyst_malicious`: <*bool*> it was determined as malicious by a Google Threat Intelligence analyst.
    * `google_malware_analysis`: <*bool*> it was detected by Google Threat Intelligence's malware analysis.
    * `google_botnet_emulation`: <*bool*> it was detected by Google Threat Intelligence's botnet analysis.
    * `google_mobile_malware_analysis`: <*bool*> it was detected by Google Threat Intelligence's mobile malware analysis.
    * `google_malware_similarity`: <*bool*> it was detected by Google Threat Intelligence's malware analysis.
    * `google_malware_analysis_auto`: <*bool*> it was detected by Google Threat Intelligence's malware analysis.
    * `mandiant_association_report`: <*bool*> it is associated with a Google Threat Intelligence Intelligence Report.
    * `mandiant_association_actor`: <*bool*> it is associated with a tracked Google Threat Intelligence threat actor.
    * `mandiant_association_malware`: <*bool*> it is associated with a tracked Google Threat Intelligence malware family.
    * `mandiant_domain_hijack`: <*bool*> the domain was recently determined as malicious by a Google Threat Intelligence analyst.
    * `mandiant_osint`: <*bool*> it is considered widespread.
    * `safebrowsing_verdict`: <*bool*> Google Safebrowsing verdict.
    * `gavs_detections`: <*int*> number of detections by Google’s spam and threat filtering engines.
    * `gavs_categories`: <*list of strings*> known threat categories.
    * `normalised_categories`: <*list of strings*> known threat categories.
    * `legitimate_software`: <*bool*> the indicator is benign. It is associated with a well-known and trusted software distributor and likely poses no threat.
    * `matched_malicious_yara`: <*bool*> matches YARA rules.
    * `malicious_sandbox_verdict`: <*bool*> it was detected by sandbox analysis, indicating suspicious behavior.
    * `associated_reference`: <*bool*> it appears in public sources.
    * `associated_malware_configuration`: <*bool*> contains known malware configurations.
    * `associated_actor`: <*bool*> it is associated with a community threat actor.
    * `high_severity_related_files`: <*bool*> related files are marked as malicious (high severity).
    * `medium_severity_related_files`: <*bool*> related files are marked as malicious (medium severity).
    * `low_severity_related_files`: <*bool*> related files are marked as malicious (low severity).
    * `pervasive_indicator`: <*bool*> related files have been seen in OSINT sources.
    * `gti_confidence_score`: <*int*> the Google Threat Intelligence confidence score of the indicator. This score uses a probabilistic model to weight different signals. It expresses the confidence we have in an indicator being malicious (values closer to 100) or benign (values closer to 0). It's an additional signal used to determine the `gti_assessment.verdict` field.
      * Values Above 95 are considered malicious and analysts should prioritize investigation.
      * Values above 80 are considered malicious.
      * Values between 60 and 80 are considered suspicious.
      * Values between 20-60 mean we don't have signals to say the file is malicious or benign. This is equivalent to the verdict undetected.
      * Values below 20 mean the IoC can be considered benign or noisy.
    * `mandiant_confidence_score`: <*int*> this is a similar probabilistic score, like the gti\_confidence\_score above, but is only available in a subset of IoCs. It's in the process of being **deprecated** in favor of `gti_confidence_score`.
  * `gti_description_cards`: <*dictionary*> containing lists of explainability cards grouped by category. The keys represent the card category (e.g., `HIGHEST_IMPACT_FACTOR`, `TECHNICAL_EVIDENCE`, `MITIGATING_FACTORS`, etc.). Each card contains:
    * `influence`: <*string*> Impact on the final verdict ("high", "medium", "low", "benign").
    * `title`: <*string*> Formatted descriptive title for the card.
    * `sub_title`: <*string*> Detailed technical explanation (if available).
    * `collection_type`: <*string*> Associated entity type (e.g., "threat-actor", "malware-family").
    * `related_links`: <*list of dictionaries*> Dynamic links related to the card, each containing:
      * `title`: <*string*> Link display text.
      * `url`: <*dictionary*> Link target object containing:
        * `object_type`: <*string*> Type of the target object.
        * `id`: <*string*> ID of the target object.
* `jarm`: <*string*> IP address' [JARM hash](https://engineering.salesforce.com/easily-identify-malicious-servers-on-the-internet-with-jarm-e095edac525a).
* `last_analysis_date`: <*integer*> UTC timestamp representing last time the IP was scanned.
* `last_analysis_results`: <*dictionary*> result from URL scanners. dict with scanner name as key and a dict with notes/result from that scanner as value.
  * `category`: <*string*> normalized result. can be:
    * "harmless" (site is not malicious),
    * "undetected" (scanner has no opinion about this site),
    * "suspicious" (scanner thinks the site is suspicious),
    * "malicious" (scanner thinks the site is malicious).
  * `engine_name`: <*string*> complete name of the URL scanning service.
  * `method`: <*string*> type of service given by that URL scanning service (i.e. "blacklist").
  * `result`: <*string*> raw value returned by the URL scanner ("clean", "malicious", "suspicious", "phishing"). It may vary from scanner to scanner, hence the need for the "category" field for normalisation.
* `last_analysis_stats`: <*dictionary*> number of different results from this scans.
  * `harmless`: <*integer*> number of reports saying that is harmless.
  * `malicious`: <*integer*> number of reports saying that is malicious.
  * `suspicious`: <*integer*> number of reports saying that is suspicious.
  * `timeout`: <*integer*> number of timeouts when checking this URL.
  * `undetected`: <*integer*> number of reports saying that is undetected.
* `last_https_certificate`: <*[SSL Certificate](ssl-certificate-object.md)* > SSL Certificate object certificate information for that IP.
* `last_https_certificate_date`: <*integer*> date when the certificate shown in `last_https_certificate` was retrieved by Google TI. UTC timestamp.
* `last_modification_date`: <*integer*> date when any of the IP's information was last updated. UTC timestamp.
* `network`: <*string*> IPv4 network range to which the IP belongs.
* `regional_internet_registry`: <*string*> RIR (one of the current RIRs: AFRINIC, ARIN, APNIC, LACNIC or RIPE NCC).
* `reputation`: <*integer*> IP's score calculated from the votes of the Google TI's community.
* `tags`: <*list of strings*> identificative attributes.
* `total_votes`: <*dictionary*> unweighted number of total votes from the community, divided in "harmless" and "malicious".
  * `harmless`: <*integer*> number of positive votes.
  * `malicious`: <*integer*> number of negative votes.
* `whois`: <*string*> whois information as returned from the pertinent whois server.
* `whois_date`: <*integer*> date of the last update of the whois record in Google TI. UTC timestamp.

> ⚠️ gti\_assessment attribute
>
> To get the **gti\_assessment** attribute in the JSON response, ensure that the **x-tool** header is added to the request headers. This header should be used to identify your tool or service with a custom name.

> 📘 About reputation
>
> The reputation for a given domain is determined by Google TI's Community (registered users). Users sometimes vote on domains, these users in turn have a reputation themselves: the *community score* condenses the votes performed on a given item weighted by the reputation of the users that casted these votes. Negative (red) scores indicate maliciousness, whereas positive (green) scores reflect harmlessness. The higher the absolute number, the more that you may trust a given score.

```json "ip_address" object
{
  "data": {
    "attributes": {
      "as_owner": "<string>",
      "asn": <int>,
      "continent": "<string>",
      "country": "<string>",
      "gti_assessment": {
           "verdict": {
               "value": "<string>"
           },
           "severity": {
               "value": "<string>"
           },
           "threat_score": {
               "value": "<int>"
           },
           "contributing_factors": {
                "mandiant_analyst_benign": "<bool>",
                "mandiant_analyst_malicious": "<bool>",
                "mandiant_malware_analysis_1": "<bool>",
                "mandiant_malware_analysis_2": "<bool>",
                "mandiant_malware_analysis_3": "<bool>",
                "mandiant_botnet_emulation": "<bool>",
                "mandiant_mobile_malware_analysis": "<bool>",
                "mandiant_malware_similarity": "<bool>",
                "mandiant_malware_analysis_auto": "<bool>",
                "mandiant_association_report": "<bool>",
                "mandiant_association_actor": "<bool>",
                "mandiant_association_malware": "<bool>",
                "mandiant_confidence_score": "<int>",
                "gti_confidence_score": "<int>",
                "mandiant_domain_hijack": "<bool>",
                "mandiant_osint": "<bool>",
                "safebrowsing_verdict": "<bool>",
                "gavs_detections": "<int>",
                "gavs_categories": "<list of strings>",
                "normalised_categories": "<list of strings>",
                "legitimate_software": "<bool>",
                "matched_malicious_yara": "<bool>",
                "malicious_sandbox_verdict": "<bool>",
                "associated_reference": "<bool>",
                "associated_malware_configuration": "<bool>",
                "associated_actor": "<bool>",
                "high_severity_related_files": "<bool>",
                "medium_severity_related_files": "<bool>",
                "low_severity_related_files": "<bool>",
                "pervasive_indicator": "<bool>"
           },
           "gti_description_cards": {
                "<string:category_name>": [
                    {
                        "influence": "<string>",
                        "title": "<string>",
                        "sub_title": "<string>",
                        "collection_type": "<string>",
                        "related_links": [
                            {
                                "title": "<string>",
                                "url": {
                                    "object_type": "<string>",
                                    "id": "<string>"
                                }
                            }
                        ]
                    }
                ]
           },
           "description": "<string>"
      },
      "jarm": "<string>",
      "last_analysis_date": <int:timestamp>,
      "last_analysis_results": {
        "<engine name:string>": {
          "category": "<string>",
          "engine_name": "<string>",
          "method": "<string>",
          "result": "<string>"
        }
      },
      "last_analysis_stats": {
        "harmless": <int>,
        "malicious": <int>,
        "suspicious": <int>,
        "timeout": <int>,
        "undetected": <int>
      },
      "last_modification_date": <int:timestamp>,
      "network": "<ipv4_range>",
      "regional_internet_registry": "<string>",
      "reputation": <int>,
      "total_votes": {
        "harmless": <int>,
        "malicious": <int>
      },
      "tags": ["<string>"],
      "whois": "<string>",
      "whois_date": <int:timestamp>
    },
    "id": "<ipv4>",
    "links": {
      "self": "https://www.virustotal.com/api/v3/ip_addresses/<ipv4>"
    },
    "type": "ip_address"
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "as_owner": "Strato AG",
            "asn": 6724,
            "continent": "EU",
            "country": "DE",
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
                     "mandiant_confidence_score": 80,
                     "gti_confidence_score": 90
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
            },
            "jarm": "27d40d40d29d40d1dc42d43d00041d4689ee210389f4f6b4b5b1b93f92252d",
            "last_analysis_date": 1671691600,
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
}
```

## relationships

In addition to the previously described attributes, IP address objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../01-api-introduction/api-responses/introduction-relationships.md) section. The available relationships are described in the following table:

| Relationship                  | Description                                                                                                                                                                          | Accessibility                                        | Return object type                                                                                                                                                                                                                                                                                                   |
| :---------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| associations                  | IP's associated objects (reports, campaigns, IoC collections, malware families, software toolkits, vulnerabilities, threat-actors), without filtering by the associated object type. | Everyone.                                            | List of [reports](report-object.md), [campaigns](campaign-object.md), [IoC collections](ioc-collection-object.md), [malware families](malware-family-object.md), [software toolkits](software-toolkit-object.md), [vulnerabilities](vulnerability-object.md), [threat-actors](threat-actor-object.md) objecs. |
| campaigns                     | Campaigns associated to the IP address.                                                                                                                                              | Google TI Enterprise and Enterprise Plus users only. | List of collections of type [Campaign](campaign-object.md).                                                                                                                                                                                                                                                         |
| collections                   | IoC Collections associated to the IP address.                                                                                                                                        | Everyone.                                            | List of collections of type [IoC Collection](ioc-collection-object.md).                                                                                                                                                                                                                                             |
| comments                      | Comments for the IP address.                                                                                                                                                         | Everyone.                                            | List of [Comments](comment-object.md).                                                                                                                                                                                                                                                                              |
| communicating\_files          | Files that communicate with the IP address.                                                                                                                                          | Everyone.                                            | List of [Files](file-object.md).                                                                                                                                                                                                                                                                                    |
| downloaded\_files             | Files downloaded from the IP address.                                                                                                                                                | Google TI users only.                                | List of [Files](file-object.md).                                                                                                                                                                                                                                                                                    |
| graphs                        | Graphs including the IP address.                                                                                                                                                     | Everyone.                                            | List of [Graphs](graph-object.md).                                                                                                                                                                                                                                                                                  |
| historical\_ssl\_certificates | SSL certificates associated with the IP.                                                                                                                                             | Everyone.                                            | List of [SSL Certificate](ssl-certificate-object.md).                                                                                                                                                                                                                                                               |
| historical\_whois             | WHOIS information for the IP address.                                                                                                                                                | Everyone.                                            | List of [Whois](whois-object.md).                                                                                                                                                                                                                                                                                   |
| malware\_families             | Malware families associated to the IP address.                                                                                                                                       | Google TI Enterprise and Enterprise Plus users only. | A list of collections of type [malware family](malware-family-object.md).                                                                                                                                                                                                                                           |
| memory\_pattern\_parents      | Files having an IP as string on memory during sandbox execution.                                                                                                                     | Google TI users only.                                | A list of [Files](file-object.md).                                                                                                                                                                                                                                                                                  |
| referrer\_files               | Files containing the IP address.                                                                                                                                                     | Everyone.                                            | List of [Files](file-object.md).                                                                                                                                                                                                                                                                                    |
| related\_comments             | Community posted comments in the IP's related objects.                                                                                                                               | Everyone.                                            | List of [Comments](comment-object.md).                                                                                                                                                                                                                                                                              |
| related\_reports              | Reports that are directly and indirectly related to the IP.                                                                                                                          | Google TI Enterprise and Enterprise Plus users only. | List of [Reports](report-object.md).                                                                                                                                                                                                                                                                                |
| related\_threat\_actors       | Threat actors related to the IP address.                                                                                                                                             | Google TI Enterprise and Enterprise Plus users only. | List of collections of type [Threat Actor](threat-actor-object.md).                                                                                                                                                                                                                                                 |
| reports                       | Reports directly associated to the IP.                                                                                                                                               | Google TI Enterprise and Enterprise Plus users only. | A list of collections of type [Report](report-object.md).                                                                                                                                                                                                                                                           |
| resolutions                   | IP address' resolutions                                                                                                                                                              | Everyone.                                            | List of [Resolutions](resolution-object.md).                                                                                                                                                                                                                                                                        |
| software\_toolkits            | Software and Toolkits associated to the IP address.                                                                                                                                  | Google TI Enterprise and Enterprise Plus users only. | A list of collections of type [Software and Toolkits](software-toolkit-object.md).                                                                                                                                                                                                                                  |
| urls                          | URLs related to the IP address.                                                                                                                                                      | Google TI users only.                                | List of [URLs](url-object.md).                                                                                                                                                                                                                                                                                      |
| user\_votes                   | IP's votes made by current signed-in user.                                                                                                                                           | Everyone.                                            | List of [Votes](vote-object.md).                                                                                                                                                                                                                                                                                    |
| votes                         | IP's votes.                                                                                                                                                                          | Everyone.                                            | List of [Votes](vote-object.md).                                                                                                                                                                                                                                                                                    |
| vulnerabilities               | Vulnerabilities associated to the IP address.                                                                                                                                        | Google TI Enterprise and Enterprise Plus users only. | A list of collections of type [Vulnerability](vulnerability-object.md).                                                                                                                                                                                                                                             |

These relationships are detailed in the subsections below.

---

← [IoC-Stream Notifications](ioc-stream-notifications-object.md) · [up](README.md) · [🔀 comments](ip-object/ip-object-comments.md) →

*Archived from <https://gtidocs.virustotal.com/reference/ip-object>.*
