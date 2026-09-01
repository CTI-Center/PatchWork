---
title: "Domains"
source: https://gtidocs.virustotal.com/reference/domains-object
slug: domains-object
section: reference
group: "API OBJECTS"
updatedAt: 2026-08-26T14:46:16.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Domains

---

# domains

Along with URLs, Google Threat Intelligence stores information related network locations, as domains and IP addresses. Within this section we will go through the information provided by Domain objects.

Domain objects represent information about a domain or [FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name), and can be retrieved by searching an already existing domain, by its relationship with other objects or by other meanings when searching in Enterprise services.

## object-attributes

A Domain object contains the following attributes:

* `categories`: <*dictionary*> mapping that relates categorisation services with the category it assigns the domain to. These services are, among others: Alexa, BitDefender, TrendMicro, Websense ThreatSeeker, etc.
* `creation_date`: <*integer*> creation date extracted from the Domain's whois (UTC timestamp).
* `favicon`: <*dictionary*> dictionary including difference hash and md5 hash of the domain's favicon. Only available for premium users.
  * `dhash`: <*string*> difference hash
  * `raw_md5`: <*string*> favicon's MD5 hash.
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
    * `google_malware_analysis`: <*bool*> it was detected by Google Threat Intelligence's malware analysis.
    * `google_botnet_emulation`: <*bool*> it was detected by Google Threat Intelligence's botnet analysis.
    * `google_mobile_malware_analysis`: <*bool*> it was detected by Google Threat Intelligence's mobile malware analysis.
    * `google_malware_similarity`: <*bool*> it was detected by Google Threat Intelligence's malware analysis.
    * `google_malware_analysis_auto`: <*bool*> it was detected by Google Threat Intelligence's malware analysis.
    * `mandiant_association_report`: <*bool*> it is associated with a Google Threat Intelligence Intelligence Report.
    * `mandiant_association_actor`: <*bool*> it is associated with a tracked Google Threat Intelligence threat actor.
    * `mandiant_association_malware`: <*bool*> it is associated with a tracked Google Threat Intelligence malware family
    * `mandiant_domain_hijack`: <*bool*> the domain was recently determined as malicious by a Google Threat Intelligence analyst.
    * `mandiant_osint`: <*bool*> it is considered widespread.
    * `safebrowsing_verdict'`: <*bool*> Google Safebrowsing verdict.
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
* `jarm`: <*string*> domain's [JARM hash](https://engineering.salesforce.com/easily-identify-malicious-servers-on-the-internet-with-jarm-e095edac525a).
* `last_analysis_date`: <*integer*> UTC timestamp representing last time the domain was scanned.
* `last_analysis_results`: <*dictionary*> result from URL scanners. dict with scanner name as key and a dict with notes/result from that scanner as value.
  * `category`: <*string*> normalised result. can be:
    * "harmless" (site is not malicious),
    * "undetected" (scanner has no opinion about this site),
    * "suspicious" (scanner thinks the site is suspicious),
    * "malicious" (scanner thinks the site is malicious).
  * `engine_name`: <*string*> complete name of the URL scanning service.
  * `engine_version`: <*string*> engine version value, in case it reports that data.
  * `method`: <*string*> type of service given by that URL scanning service (i.e. "blacklist").
  * `result`: <*string*> raw value returned by the URL scanner ("clean", "malicious", "suspicious", "phishing"). It may vary from scanner to scanner, hence the need for the "category" field for normalisation.
* `last_analysis_stats`: <*dictionary*> number of different results from this scans.
  * `harmless`: <*integer*> number of reports saying that is harmless.
  * `malicious`: <*integer*> number of reports saying that is malicious.
  * `suspicious`: <*integer*> number of reports saying that is suspicious.
  * `timeout`:  <*integer*> number of timeouts when checking this URL.
  * `undetected`: <*integer*> number of reports saying that is undetected.
* `last_dns_records`: <*list of dictionaries*>  domain's DNS records on its last scan. Every entry is a *dictionary* containing the following fields:
  * `expire`: <*integer*>
  * `flag`: <*integer*>
  * `minimum`: <*integer*>
  * `priority`: <*integer*>
  * `refresh`: <*integer*>
  * `rname`: <*string*>
  * `retry`: <*integer*>
  * `serial`: <*integer*>
  * `tag`: <*string*>
  * `ttl`: <*integer*>
  * `type`: <*string*>
  * `value`: <*string*>
* `last_dns_records_date`: <*integer*> date when the dns records list was retrieved by Google TI (UTC timestamp).
* `last_https_certificate`: <*[SSL Certificate](ssl-certificate-object.md)*> SSL Certificate object retrieved last time the domain was analysed.
* `last_https_certificate_date`: <*integer*> date when the certificate was retrieved by Google TI (UTC timestamp).
* `last_modification_date`: <*integer*> date when any of domain's information was last updated.
* `last_update_date`: <*integer*> updated date extracted from whois (UTC timestamp).
* `popularity_ranks`: <*dictionary*> domain's position in popularity ranks such as Alexa, Quantcast, Statvoo, etc. Every dictionary contains the following subfields:
  * `rank`: <*integer*> rank position.
  * `timestamp`: <*integer*> UTC timestamp when the rank was ingested.
* `registrar`: <*string*> company that registered the domain.
* `reputation`: <*integer*> domain's score calculated from the votes of the Google TI's community.
* `tags`: <*list of strings*> list of representative attributes.
* `total_votes`: <*dictionary*> unweighted number of total votes from the community, divided in "harmless" and "malicious":
  * `harmless`: <*integer*> number of positive votes.
  * `malicious`: <*integer*> number of negative votes.
* `whois`: <*string*> whois information as returned from the pertinent whois server.
* `whois_date`: <*integer*> date of the last update of the whois record in Google TI.

> ⚠️ gti\_assessment attribute
>
> To get the **gti\_assessment** attribute in the JSON response, ensure that the **x-tool** header is added to the request headers. This header should be used to identify your tool or service with a custom name.

> 📘 About reputation
>
> The reputation for a given domain is determined by Google TI's Community (registered users). Users sometimes vote on domains, these users in turn have a reputation themselves: the *community score* condenses the votes performed on a given item weighted by the reputation of the users that casted these votes. Negative (red) scores indicate maliciousness, whereas positive (green) scores reflect harmlessness. The higher the absolute number, the more that you may trust a given score.

```json "domain" object
{
  "data": {
    "attributes": {
      "categories": {
        "<SERVICE>": "<string>"
      },
      "creation_date": <int:timestamp>,
      "favicon": {
        "dhash": "<string>",
        "raw_md5": "<string>"
      },
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
      "last_dns_records": [
        {
          "expire": <int>,
          "flag": <int>,
          "minimum": <int>,
          "priority": <int>,
          "refresh": <int>,
          "rname": "<string>",
          "retry": <int>,
          "serial": <int>,
          "tag": "<string>",
          "ttl": <int>,
          "type": "<string>",
          "value": "<string>"
        }
      ],
      "last_dns_records_date": <int:timestamp>,
      "last_https_certificate": <SSL Certificate object>,
      "last_https_certificate_date": <int:timestamp>,
      "last_modification_date": <int:timestamp>,
      "last_update_date": <int:timestamp>,
      "popularity_ranks": {
      	"<string:rank name>": {
          	"rank": <int>,
            "timestamp": <int:timestamp>
        }
      },
      "registrar": "<string>",
      "reputation": <int>,
      "tags": ["<string>"],
      "total_votes": {
        "harmless": <int>,
        "malicious": <int>
      },
      "whois": "<string>",
      "whois_date": <int:timestamp>
    },
    "id": "<DOMAIN>",
    "links": {
      "self": "https://www.virustotal.com/api/v3/domains/<DOMAIN>"
    },
    "type": "domain"
  }
}
```
```json Example
{
    "data": {
        "attributes": {
            "categories": {
            	"Dr.Web": "known infection source",
            	"Forcepoint ThreatSeeker": "bot networks. parked domain"
            },
            "creation_date": 1106675546,
            "favicon": {
                "dhash": "71f0cc989386ba80",
                "raw_md5": "01625852ea10d9fa44p676b1g2ff1df3"
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
                    "expire": 1814400,
                    "minimum": 600,
                    "refresh": 3600,
                    "retry": 300,
                    "rname": "hostmaster.foo-inc.com",
                    "serial": 2020061203,
                    "ttl": 1799,
                    "type": "SOA",
                    "value": "ns1.foo.com"
                },
              	{
                    "ttl": 1162,
                    "type": "A",
                    "value": "91.117.116.8"
                },
                {
                    "ttl": 299,
                    "type": "AAAA",
                    "value": "2430:2fb0:f0b1:ca3b::6f"
                },
              	{
                    "priority": 1,
                    "ttl": 1545,
                    "type": "MX",
                    "value": "mta6.am0.foodns.net"
                },
                {
                    "flag": 0,
                    "tag": "issue",
                    "ttl": 1799,
                    "type": "CAA",
                    "value": "globalsign.com"
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
            "tags": [
                "dga"
            ],
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
}
```

## relationships

In addition to the previously described attributes, Domain objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../01-api-introduction/api-responses/introduction-relationships.md) section. The available relationships are shown in the following table:

| Relationship                  | Description                                                                                                                                                                              | Accessibility                                        | Return object type                                                                                                                                                                                                                                                                                                   |
| :---------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| associations                  | Domain's associated objects (reports, campaigns, IoC collections, malware families, software toolkits, vulnerabilities, threat-actors), without filtering by the associated object type. | Everyone.                                            | List of [reports](report-object.md), [campaigns](campaign-object.md), [IoC collections](ioc-collection-object.md), [malware families](malware-family-object.md), [software toolkits](software-toolkit-object.md), [vulnerabilities](vulnerability-object.md), [threat-actors](threat-actor-object.md) objecs. |
| caa\_records                  | Records CAA for the domain.                                                                                                                                                              | Google TI users only.                                | List of [Domains](domains-object.md).                                                                                                                                                                                                                                                                               |
| campaigns                     | Campaigns associated to the domain.                                                                                                                                                      | Google TI Enterprise or Enterprise Plus users only.  | List of collections of type [Campaign](campaign-object.md).                                                                                                                                                                                                                                                         |
| cname\_records                | Records CNAME for the domain.                                                                                                                                                            | Google TI users only.                                | List of [Domains](domains-object.md).                                                                                                                                                                                                                                                                               |
| collections                   | IoC Collections associated to the domain.                                                                                                                                                | Everyone.                                            | List of collections of type [IoC Collections](ioc-collection-object.md).                                                                                                                                                                                                                                            |
| comments                      | Community posted comments about the domain.                                                                                                                                              | Everyone.                                            | List of [Comments](comment-object.md).                                                                                                                                                                                                                                                                              |
| communicating\_files          | Files that communicate with the domain.                                                                                                                                                  | Everyone.                                            | List of [Files](file-object.md).                                                                                                                                                                                                                                                                                    |
| downloaded\_files             | Files downloaded from that domain.                                                                                                                                                       | Google TI users only.                                | List of [Files](file-object.md).                                                                                                                                                                                                                                                                                    |
| graphs                        | Graphs including the domain.                                                                                                                                                             | Everyone.                                            | List of [Graphs](graph-object.md).                                                                                                                                                                                                                                                                                  |
| historical\_ssl\_certificates | SSL certificates associated with the domain.                                                                                                                                             | Everyone.                                            | List of [SSL Certificate](ssl-certificate-object.md).                                                                                                                                                                                                                                                               |
| historical\_whois             | WHOIS information for the domain.                                                                                                                                                        | Everyone.                                            | List of [Whois](whois-object.md).                                                                                                                                                                                                                                                                                   |
| immediate\_parent             | Domain's immediate parent.                                                                                                                                                               | Everyone.                                            | A single [Domain](domains-object.md).                                                                                                                                                                                                                                                                               |
| malware\_families             | Malware families associated to the domain.                                                                                                                                               | Google TI Enterprise or Enterprise Plus users only.  | List of collections of type [malware families](malware-family-object.md).                                                                                                                                                                                                                                           |
| memory\_pattern\_parents      | Files having a domain as string on memory during sandbox execution.                                                                                                                      | Google TI users only.                                | List of [Files](file-object.md).                                                                                                                                                                                                                                                                                    |
| mx\_records                   | Records MX for the domain.                                                                                                                                                               | Google TI users only.                                | List of [Domains](domains-object.md).                                                                                                                                                                                                                                                                               |
| ns\_records                   | Records NS for the domain.                                                                                                                                                               | Google TI users only.                                | List of [Domains](domains-object.md).                                                                                                                                                                                                                                                                               |
| parent                        | Domain's top parent.                                                                                                                                                                     | Everyone.                                            | A single [Domain](domains-object.md).                                                                                                                                                                                                                                                                               |
| referrer\_files               | Files containing the domain.                                                                                                                                                             | Everyone.                                            | A list of [Files](file-object.md).                                                                                                                                                                                                                                                                                  |
| related\_comments             | Community posted comments in the domain's related objects.                                                                                                                               | Everyone.                                            | A list of [Comments](comment-object.md).                                                                                                                                                                                                                                                                            |
| related\_reports              | Reports that are directly and indirectly related to the domain.                                                                                                                          | Google TI Enterprise and Enterprise Plus users only. | List of [Reports](report-object.md).                                                                                                                                                                                                                                                                                |
| related\_threat\_actors       | Threat actors related to the domain.                                                                                                                                                     | Google TI Enterprise users only.                     | A list of collections of type [Threat Actors](threat-actor-object.md).                                                                                                                                                                                                                                              |
| reports                       | Reports directly associated to the domain.                                                                                                                                               | Google TI Enterprise and Enterprise Plus users only. | A list of collections of type [Reports](report-object.md).                                                                                                                                                                                                                                                          |
| resolutions                   | DNS resolutions for the domain.                                                                                                                                                          | Everyone.                                            | A list of [Resolutions](resolution-object.md).                                                                                                                                                                                                                                                                      |
| siblings                      | Domain's sibling domains.                                                                                                                                                                | Everyone.                                            | A list of [Domains](domains-object.md).                                                                                                                                                                                                                                                                             |
| soa\_records                  | Records SOA for the domain.                                                                                                                                                              | Google TI users only.                                | List of [Domains](domains-object.md).                                                                                                                                                                                                                                                                               |
| software\_toolkits            | Software and Toolkits associated to the domain.                                                                                                                                          | Google TI Enterprise and Enterprise Plus users only. | A list of collections of type [Software and Toolkits](software-toolkit-object.md).                                                                                                                                                                                                                                  |
| subdomains                    | Domain's subdomains.                                                                                                                                                                     | Everyone.                                            | A list of [Domains](domains-object.md).                                                                                                                                                                                                                                                                             |
| urls                          | URLs having this domain.                                                                                                                                                                 | Google TI users only.                                | List of [URLs](url-object.md).                                                                                                                                                                                                                                                                                      |
| user\_votes                   | Current user's votes.                                                                                                                                                                    | Everyone.                                            | List of [Votes](vote-object.md)                                                                                                                                                                                                                                                                                     |
| votes                         | Domain's votes.                                                                                                                                                                          | Everyone.                                            | List of [Votes](vote-object.md)                                                                                                                                                                                                                                                                                     |
| vulnerabilities               | Vulnerabilities associated to the domain.                                                                                                                                                | Google TI Enterprise and Enterprise Plus users only. | A list of collections of type [Vulnerabilities](vulnerability-object.md).                                                                                                                                                                                                                                           |

These relationships are detailed in the subsections below.

---

← [Dark Web User Profile](dark-web-objects/dark-web-user-profile-object.md) · [up](README.md) · [🔀 communicating_files](domains-object/domain-communicating_files.md) →

*Archived from <https://gtidocs.virustotal.com/reference/domains-object>.*
