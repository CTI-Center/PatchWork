---
title: "Files"
source: https://gtidocs.virustotal.com/reference/file-object
slug: file-object
section: reference
group: "API OBJECTS"
updatedAt: 2026-08-26T14:46:16.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Files

---

# files

Information about files

Files are one of the most important type of objects in the Google Threat Intelligence API. We have a huge dataset of more than 2 billion files that have been analysed by Google Threat Intelligence over the years. A file object can be obtained either by [uploading a new file](../03-ioc-investigation/files/files-scan.md) to Google Threat Intelligence, by [searching for an already existing file hash](../03-ioc-investigation/files/file-info.md) or by other meanings when searching in [Google Threat Intelligence services](../03-ioc-investigation/search-metadata.md).

A file object ID is its SHA256 hash.

## object-attributes

In a File object you are going to find some relevant basic attributes about the file and its relationship with Google Threat Intellogence:

* `capabilities_tags`: <*list of strings*> list of representative tags related to the file's capabilities. Only available for Premium API users.
* `creation_date`: <*integer*> extracted when possible from the file's metadata. Indicates when it was built or compiled. It can also be faked by malware creators. UTC timestamp.
* `downloadable`: <*boolean*>  true if the file can be downloaded, false otherwise. Only available for Premium API users.
* `first_submission_date`: <*integer*> date when the file was first seen in Google TI. UTC timestamp.
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
    * `mandiant_association_malware`: <*bool*> it is associated with a tracked Google Threat Intelligence malware family
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
* `last_analysis_date`: <*integer*> most recent scan date. UTC timestamp.
* `last_analysis_results`: <*dictionary*> latest scan results. For more information about its format, check the [Analysis](analyses-object.md) object `results` attribute.
* `last_analysis_stats`: <*dictionary*> a summary of the latest scan results. For more information about its format, check the [Analysis](analyses-object.md) object `stats` attribute.
* `last_modification_date`: <*integer*> date when the object itself was last modified. UTC timestamp.
* `last_submission_date`: <*integer*> most recent date the file was posted to Google TI. UTC timestamp.
* `main_icon`: <*dictionary*> icon's relevant hashes, the dictionary contains two keys:
  * `raw_md5`: <*string*> icon's MD5 hash.
  * `dhash`: <*string*> icon's difference hash. It can be used to search for files with similar icons using the [/intelligence/search](../03-ioc-investigation/search-metadata/intelligence-search.md) endpoint.
* `md5`: <*string*> file's MD5 hash.
* `meaningful_name`: <*string*> the most interesting name out of all file's names.
* `names`: <*list of strings*> all file names associated with the file.
* `reputation`: <*integer*> file's score calculated from all votes posted by the Google TI community.
* `sandbox_verdicts`: <*dictionary*> A summary of all sandbox verdicts:
  * `category`: <*string*> normalized verdict category. It can be one of `suspicious`, `malicious`, `harmless` or `undetected`.
  * `confidence`: <*integer*> verdict confidence from 0 to 100.
  * `malware_classification`: <*list of strings*> raw sandbox verdicts.
  * `malware_names`: <*list of strings*> malware family names.
  * `sandbox_name`: <*string*> sandbox that provided the verdict.
* `sha1`: <*string*> file's SHA1 hash.
* `sha256`: <*string*> file's SHA256 hash.
* `sigma_analysis_summary`: <*dictionary*> dictionary containing the number of matched sigma rules group by its severity, same as `sigma_analysis_stats` but split by ruleset. Dictionary key is the ruleset name and value is the stats for that specific ruleset.
* `size`: <*integer*> file size in bytes.
* `tags`: <*list of strings*> list of representative attributes.
* `times_submitted`: <*integer*> number of times the file has been posted to Google TI.
* `tlsh`: <*string*> file's TLSH hash.
* `permhash`: <*string*> file's Permhash.
* `total_votes`: <*dictionary*> unweighted number of total votes from the community, divided in "harmless" and "malicious":
  * `harmless`: <*integer*> number of positive votes.
  * `malicious`: <*integer*> number of negative votes.
* `type_description`: <*string*> describes the file type.
* `type_extension`: <*string*> specifies file extension.
* `type_tag`: <*string*> tag representing the file type. Can be used to filter by file type in [Google TI intelligence searches](https://gtidocs.readme.io/docs/file-search-modifiers).
* `type_tags`: <*list of strings*> broader tags related to the specific file type, for instance, for a DLL this list would include - executable, windows, win32, pe, pedll. Can be used to filter in [Google TI intelligence searches](https://www.virustotal.com/gui/search/type%253Adocument/files), all *typetags get added to the\_type* search modifier.
* `unique_sources`: <*integer*> indicates from how many different sources the file has been posted from.
* `vhash`: <*string*> in-house similarity clustering algorithm value, based on a simple structural feature hash allows you to find similar files.
* `crowdsourced_ai_results` : <*dictionary*> A summary of all crowdsourced ai results:
  * `analysis` : <*string*> Natural language summary of code snippets.
  * `source`: <*string*> result source.
  * `id`: <*string*> id of the crowdsourced\_ai result.
* `threat_severity`: <*dictionary*>.
  * `last_analysis_date`: <*int*> timestamp when the threat severity was calculated.
  * `threat_severity_level`:
    * `SEVERITY_NONE`: this is the level assigned to entities with non-malicious verdict.
    * `SEVERITY_LOW`: the threat likely has a minor impact but should still be monitored
    * `SEVERITY_MEDIUM`: indicates a potential threat that warrants attention.
    * `SEVERITY_HIGH`: immediate action is recommended; the threat could have a critical impact
    * `SEVERITY_UNKNOWN`: not enough data to assess a severity.
  * `level_description`: \<string> a human readable description of the signals that contributed to determine the severity level.
  * `version`: <*int*>
  * `threat_severity_data`: <*dictionary*>
    * `popular_threat_category`: <*string*> Popular\_threat\_category when the severity score was calculated.
    * `type_tag`: <*string*> File type when the severity score was calculated.
    * `has_similar_files_with_detections`: <*bool*> Files similar to this by vhash have detections.
    * `is_matched_by_crowdsourced_yara_with_detections`: <*bool*> At least 1 yara rule matching this file matches other files with detections.
    * `has_vulnerabilities`: <*bool*>  The file is affected by CVE vulnerabilities.
    * `can_be_detonated`: <*bool*> The file has been characterized in sandboxes (behaviour).
    * `has_legit_tag`: <*bool*> The file has the 'legit' tag
    * `num_gav_detections`: <*int*> The number of Google antivirus detections
    * `has_execution_parents_with_detections`: <*bool*> Parent files have detections
    * `has_dropped_files_with_detections`: <*bool*> Dropped files have detections.
    * `has_contacted_ips_with_detections`: <*bool*> Has contacted IPs, domains and URLs with detections.
    * `has_contacted_domains_with_detections`: <*bool*>
    * `has_contacted_urls_with_detections`: <*bool*>
    * `has_embedded_ips_with_detections`: <*bool*> Has embedded IPs with detections.
    * `has_embedded_domains_with_detections`: <*bool*> Has embedded domains with detections.
    * `has_embedded_urls_with_detections`: <*bool*> Has embedded URLs with detections.
    * `has_malware_configs`: <*bool*>
    * `has_references`: <*bool*>
    * `belongs_to_threat_actor`: <*bool*>
    * `belongs_to_bad_collection`: <*bool*>
    * `num_av_detections`: <*int*> Number of regular AV detections if available.
    * `has_bad_sandbox_verdicts`: <*bool*>: The file has been identified as malicious in dynamic analysis.

> ⚠️ gti\_assessment attribute
>
> To get the **gti\_assessment** attribute in the JSON response, ensure that the **x-tool** header is added to the request headers. This header should be used to identify your tool or service with a custom name.

Additionally Google Threat Intelligence together with each Antivirus scan runs a set of tool that allows us to collect more information about the file. All this tool information is included in the "attributes" key, together with the rest of fields previously described. These tools and the data they extract, are documented in the subsections below.

```json "file" object
{
    "data": {
        "attributes": {
          	"capabilities_tags": [
              	"<strings>",....
            ],
            "creation_date": <int:timestamp>,
            "crowdsourced_ids_results": [
                {
                    "alert_context": [
                        {
                            "dest_ip": "<string>",
                            "dest_port": <int>,
                            "hostname": "<string>",
                            "protocol": "<string>",
                            "src_ip": "<string>",
                            "src_port": <int>,
                            "url": "<string>"
                        }
                    ],
                    "alert_severity": "<string>",
                    "rule_category": "<string>",
                    "rule_id": "<string>",
                    "rule_msg": "<string>",
                    "rule_source": "<string>"
                }
            ],
            "crowdsourced_ids_stats": {
                "info": <int>,
                "high": <int>,
                "low": <int>,
                "medium": <int>
            },
            "crowdsourced_yara_results": [
                {
                    "description": "<string>",
                    "match_in_subfile": <boolean>,
                    "rule_name": "<string>",
                    "ruleset_id": "<string>",
                    "ruleset_name": "<string>",
                    "source": "<string>"
                }
            ],
            "downloadable": <bool>,
            "first_submission_date": <int:timestamp>,
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
            "last_analysis_date": <int:timestamp>,
            "last_analysis_results": {
                "<string:engine_name>": {
                    "category": "<string>",
                    "engine_name": "<string>",
                    "engine_update": "<string>",
                    "engine_version": "<string>",
                    "method": "<string>",
                    "result": "<string>"
                }
            },
            "last_analysis_stats": {
                "confirmed-timeout": <int>,
                "failure": <int>,
                "harmless": <int>,
                "malicious": <int>,
                "suspicious": <int>,
                "timeout": <int>,
                "type-unsupported": <int>,
                "undetected": <int>
            },
            "last_modification_date": <int:timestamp>,
            "last_submission_date": <int:timestamp>,
            "md5": "<string>",
            "meaningful_name": "<string>",
            "names": [
                "<strings>",...
            ],
            "permhash": <str>,
            "reputation": <int>,
            "sandbox_verdicts": {
                "<string:sandbox_name>": {
                    "category": "<string>",
                    "confidence": <int>,
                    "malware_classification": [
                        "<string>"
                    ],
                    "malware_names": [
                        "<string>"
                    ],
                    "sandbox_name": "<string>"
                }
            },
            "sha1": "<string>",
            "sha256": "<string>",
            "sigma_analysis_results": [{
              "rule_title": "<string>",
              "rule_source": "<string>",
              "match_context": [{
                "values": {
                  "<string>": "<string>"}}],
              "rule_level": "<string>",
              "rule_description": "<string>",
              "rule_author": "<string>",
              "rule_id": "<string>"
            }],
            "sigma_analysis_stats": {
                "critical": <int>,
                "high": <int>,
                "low": <int>,
                "medium": <int>
            },
            "sigma_analysis_summary": {
                "<string:ruleset_name>": {
                    "critical": <int>,
                    "high": <int>,
                    "low": <int>,
                    "medium": <int>
                }
            },
            "size": <int>,
            "tags": [
                "<strings>",...
            ],
            "tlsh": <str>,
            "times_submitted": <int>,
            "total_votes": {
                "harmless": <int>,
                "malicious": <int>
            },
            "type_description": "<string>",
            "type_extension": "<string>",
            "type_tag": "<string>",
            "unique_sources": <int>,
            "vhash": "<string>"
        },
        "id": "<SHA256>",
        "links": {
            "self": "https://www.virustotal.com/ui/files/<SHA256>"
        },
        "type": "file"
    }
}
```
```json Example
{
    "data": {
        "attributes": {
          	"capabilities_tags": [
                "str_win32_internet_api",
                "cred_ff",
                "win_mutex",
                "keylogger",
                "str_win32_winsock2_library",
                "sniff_audio",
                "network_dropper",
                "ldpreload",
                "win_files_operation",
                "str_win32_wininet_library",
                "inject_thread"
            ],
            "creation_date": 1589251011,
            "crowdsourced_ids_results": [
              {
                "alert_context": [
                  {
                    "proto": "TCP",
                    "src_ip": "152.126.25.42",
                    "src_port": 80
                  }
                ],
                "alert_severity": "high",
                "rule_category": "Potential Corporate Privacy Violation",
                "rule_id": "32481",
                "rule_msg": "POLICY-OTHER Remote non-JavaScript file found in script tag src attribute",
                "rule_source": "snort"
               }
            ],
            "crowdsourced_ids_stats": {
                "high": 1,
                "info": 0,
                "low": 0,
                "medium": 0
             },
            "crowdsourced_yara_results": [
                {
                    "description": "Detects a very evil attack",
                    "match_in_subfile": true,
                    "rule_name": "evil_a_b",
                    "ruleset_id": "000abc43",
                    "ruleset_name": "evilness",
                    "source": "https://example.com/evil/ruleset"
                }
            ],
            "downloadable": true,
            "first_submission_date": 1592134853,
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
            "last_analysis_date": 1592141610,
            "last_analysis_results": {
                "ALYac": {
                    "category": "malicious",
                    "engine_name": "ALYac",
                    "engine_update": "20200614",
                    "engine_version": "1.1.1.5",
                    "method": "blacklist",
                    "result": "Trojan.GenericKDZ.67102"
                },
                "APEX": {
                    "category": "malicious",
                    "engine_name": "APEX",
                    "engine_update": "20200613",
                    "engine_version": "6.36",
                    "method": "blacklist",
                    "result": "Malicious"
                },
                "AVG": {
                    "category": "malicious",
                    "engine_name": "AVG",
                    "engine_update": "20200614",
                    "engine_version": "18.4.3895.0",
                    "method": "blacklist",
                    "result": "Win32:PWSX-gen [Trj]"
                },
                "Acronis": {
                    "category": "undetected",
                    "engine_name": "Acronis",
                    "engine_update": "20200603",
                    "engine_version": "1.1.1.76",
                    "method": "blacklist",
                    "result": null
                }
            },
            "last_analysis_stats": {
                "confirmed-timeout": 0,
                "failure": 0,
                "harmless": 0,
                "malicious": 3,
                "suspicious": 0,
                "timeout": 0,
                "type-unsupported": 0,
                "undetected": 2
            },
            "last_modification_date": 1592141790,
            "last_submission_date": 1592141610,
            "md5": "5a430646b4d3c04f0b43b444ad48443f",
            "meaningful_name": "o4oz44Z4E444.exe",
            "names": [
                "myfile.exe",
                "o4oz44Z4E444.exe"
            ],
            "reputation": 0,
            "sandbox_verdicts": {
                "VirusTotal Jujubox": {
                    "category": "malicious",
                    "confidence": 70,
                    "malware_classification": [
                        "MALWARE",
                        "TROJAN"
                    ],
                    "malware_names": [
                        "XMRigMiner"
                    ],
                    "sandbox_name": "VirusTotal Jujubox"
                },
            },
            "sha1": "54fdf53af86f90bf446f0a5fe26f6e4fd5f4c9fd",
            "sha256": "3f6fa13af90cf967f0b5f5d07f413f9d1f39d2fa366f09ff760fcd3fd8bf6fbf",
			"sigma_analysis_summary": {
				"Sigma Integrated Rule Set (GitHub)": {
					"high": 0,
					"medium": 0,
					"critical": 0,
					"low": 1
				},
				"SOC Prime Threat Detection Marketplace": {
					"high": 1,
					"medium": 0,
					"critical": 0,
					"low": 0
				}
			},
			"sigma_analysis_stats": {
				"high": 1,
				"medium": 0,
				"critical": 0,
				"low": 1
			},
			"sigma_analysis_results": [
				{
					"rule_title": "File deletion via CMD (via cmdline)",
					"rule_source": "SOC Prime Threat Detection Marketplace",
					"match_context": [
						{
							"values": {
								"TerminalSessionId": "0",
								"ProcessGuid": "C784477D-ED34-629E-4105-000000003000",
								"ProcessId": "4164",
								"Product": "Microsoft® Windows® Operating System",
								"Description": "Windows Command Processor",
								"Company": "Microsoft Corporation",
								"ParentProcessGuid": "C784477D-ED16-629E-2305-000000003000",
								"User": "NT AUTHORITY\\SYSTEM",
								"Hashes": "MD5=4E2ACF4F8A396486AB4268C94A6A245F,SHA256=9A7C58BD98D70631AA1473F7B57B426DB367D72429A5455B433A05EE251F3236,IMPHASH=8542FB14699D84D7E8DA92F66145C7FE",
								"OriginalFileName": "Cmd.Exe",
								"ParentImage": "C:\\Program Files\\rempl\\sedlauncher.exe",
								"FileVersion": "10.0.17134.1 (WinBuild.160101.0800)",
								"ParentProcessId": "5204",
								"CurrentDirectory": "C:\\Windows\\system32\\",
								"CommandLine": "C:\\Windows\\System32\\cmd.exe /c C:\\Windows\\System32\\ipconfig.exe /flushdns >C:\\Windows\\TEMP\\ipconfig.out 2>&1",
								"EventID": "1",
								"LogonGuid": "C784477D-EC60-629E-E703-000000000000",
								"LogonId": "999",
								"Image": "C:\\Windows\\System32\\cmd.exe",
								"IntegrityLevel": "System",
								"ParentCommandLine": "\"C:\\Program Files\\rempl\\sedlauncher.exe\"",
								"UtcTime": "2022-06-07 06:16:20.702",
								"RuleName": "-"
							}
						},
						{
							"values": {
								"TerminalSessionId": "0",
								"ProcessGuid": "C784477D-ED34-629E-4405-000000003000",
								"ProcessId": "1368",
								"Product": "Microsoft® Windows® Operating System",
								"Description": "Windows Command Processor",
								"Company": "Microsoft Corporation",
								"ParentProcessGuid": "C784477D-ED16-629E-2305-000000003000",
								"User": "NT AUTHORITY\\SYSTEM",
								"Hashes": "MD5=4E2ACF4F8A396486AB4268C94A6A245F,SHA256=9A7C58BD98D70631AA1473F7B57B426DB367D72429A5455B433A05EE251F3236,IMPHASH=8542FB14699D84D7E8DA92F66145C7FE",
								"OriginalFileName": "Cmd.Exe",
								"ParentImage": "C:\\Program Files\\rempl\\sedlauncher.exe",
								"FileVersion": "10.0.17134.1 (WinBuild.160101.0800)",
								"ParentProcessId": "5204",
								"CurrentDirectory": "C:\\Windows\\system32\\",
								"CommandLine": "C:\\Windows\\System32\\cmd.exe /c C:\\Windows\\System32\\netsh.exe interface ip delete arpcache >C:\\Windows\\TEMP\\ipconfig.out 2>&1",
								"EventID": "1",
								"LogonGuid": "C784477D-EC60-629E-E703-000000000000",
								"LogonId": "999",
								"Image": "C:\\Windows\\System32\\cmd.exe",
								"IntegrityLevel": "System",
								"ParentCommandLine": "\"C:\\Program Files\\rempl\\sedlauncher.exe\"",
								"UtcTime": "2022-06-07 06:16:20.741",
								"RuleName": "-"
							}
						}
					],
					"rule_level": "high",
					"rule_description": "Detects \"cmd\" utilization to self-delete files in some critical Windows destinations.",
					"rule_author": "Ariel Millahuel",
					"rule_id": "f9333cf120369debd56e4e238fffa10bdb2a1497c11e08a082befd02f9f3bdf2"
				},
				{
					"rule_title": "Failed Code Integrity Checks",
					"rule_source": "Sigma Integrated Rule Set (GitHub)",
					"match_context": [
						{
							"values": {
								"EventID": "5038",
								"param1": "\\Device\\HarddiskVolume4\\Program Files (x86)\\sandbox\\driver\\sandbox-driver.sys"
							}
						}
					],
					"rule_level": "low",
					"rule_description": "Code integrity failures may indicate tampered executables.",
					"rule_author": "Thomas Patzke",
					"rule_id": "134564d292d785dff102940b8a1ee06dba2d462c5fb852124b3771a49d7885f1"
				}
			],
            "size": 374272,
            "tags": [
                "peexe",
                "runtime-modules",
                "assembly",
                "direct-cpu-clock-access",
                "detect-debug-environment"
            ],
            "times_submitted": 3,
            "total_votes": {
                "harmless": 0,
                "malicious": 0
            },
            "type_description": "Win32 EXE",
            "type_tag": "exe",
            "type_tag": "peexe",
            "unique_sources": 3,
            "vhash": "2350f6f515f29f93f147f0f0"
        },
        "id": "3f6fa13af90cf967f0b5f5d07f413f9d1f39d2fa366f09ff760fcd3fd8bf6fbf",
        "links": {
            "self": "https://www.virustotal.com/ui/files/3f6fa13af90cf967f0b5f5d07f413f9d1f39d2fa366f09ff760fcd3fd8bf6fbf"
        },
        "type": "file"
    }
}
```

## relationships

In addition to the previously described attributes (and the ones described in the following subsections), File objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../01-api-introduction/api-responses/introduction-relationships.md) section.

The following table shows a summary of available relationships for file objects.

| Relationship                | Description                                                                                                                                                                            | Accessibility                                        | Return object type                                                                                                                                                                                                                                                                                                     |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| analyses                    | Analyses for the file                                                                                                                                                                  | Google TI users only.                                | A list of [Analyses](analyses-object.md)                                                                                                                                                                                                                                                                              |
| associations                | File's associated objects (reports, campaigns, IoC collections, malware families, software toolkits, vulnerabilities, threat-actors), without filtering by the associated object type. | Everyone.                                            | A list of [reports](report-object.md), [campaigns](campaign-object.md), [IoC collections](ioc-collection-object.md), [malware families](malware-family-object.md), [software toolkits](software-toolkit-object.md), [vulnerabilities](vulnerability-object.md), [threat-actors](threat-actor-object.md) objecs. |
| behaviours                  | Behaviour reports for the file. See [File behaviour](file-behaviour-summary-object.md).                                                                                               | Everyone.                                            | A list of [File behaviour](file-behaviour-summary-object.md).                                                                                                                                                                                                                                                         |
| attack\_techniques          | Returns the Attack Techniques of the File.                                                                                                                                             | Google TI Enterprise and Enterprise Plus users only. | List of [Attack Techniques](object-attack-techniques.md).                                                                                                                                                                                                                                                             |
| bundled\_files              | Files bundled within the file.                                                                                                                                                         | Everyone.                                            | A list of [Files](file-object.md).                                                                                                                                                                                                                                                                                    |
| campaigns                   | Campaigns associated to the file.                                                                                                                                                      | Google TI Enterprise and Enterprise Plus users only. | A list of collections of type [Campaign](campaign-object.md).                                                                                                                                                                                                                                                         |
| carbonblack\_children       | Files derived from the file according to Carbon Black.                                                                                                                                 | Google TI users only.                                | A list of [Files](file-object.md).                                                                                                                                                                                                                                                                                    |
| carbonblack\_parents        | Files from where the file was derived according to Carbon Black.                                                                                                                       | Google TI users only.                                | A list of [Files](file-object.md).                                                                                                                                                                                                                                                                                    |
| collections                 | IoC Collections associated to the file.                                                                                                                                                | Everyone.                                            | A list of collections of type [IoC Collection](ioc-collection-object.md).                                                                                                                                                                                                                                             |
| comments                    | Comments for the file.                                                                                                                                                                 | Everyone.                                            | A list of [Comments](comment-object.md).                                                                                                                                                                                                                                                                              |
| compressed\_parents         | Compressed files that contain the file.                                                                                                                                                | Google TI users only.                                | A list of [Files](file-object.md).                                                                                                                                                                                                                                                                                    |
| contacted\_domains          | Domains contacted by the file.                                                                                                                                                         | Everyone.                                            | A list of [Domains](domains-object.md).                                                                                                                                                                                                                                                                               |
| contacted\_ips              | IP addresses contacted by the file.                                                                                                                                                    | Everyone.                                            | A list of [IP addresses](ip-object.md).                                                                                                                                                                                                                                                                               |
| contacted\_urls             | URLs contacted by the file.                                                                                                                                                            | Everyone.                                            | A list of [URLs](url-object.md).                                                                                                                                                                                                                                                                                      |
| dropped\_files              | Files dropped by the file during its execution.                                                                                                                                        | Everyone.                                            | A list of [Files](file-object.md).                                                                                                                                                                                                                                                                                    |
| email\_attachments          | Files attached to the email.                                                                                                                                                           | Google TI users only.                                | A list of [Files](file-object.md).                                                                                                                                                                                                                                                                                    |
| email\_parents              | Email files that contained the file.                                                                                                                                                   | Google TI users only.                                | A list of [Files](file-object.md).                                                                                                                                                                                                                                                                                    |
| embedded\_domains           | Domain names embedded in the file.                                                                                                                                                     | Google TI users only.                                | A list of [Domains](domains-object.md).                                                                                                                                                                                                                                                                               |
| embedded\_ips               | IP addresses embedded in the file.                                                                                                                                                     | Google TI users only.                                | A list of [IP addresses](ip-object.md).                                                                                                                                                                                                                                                                               |
| embedded\_urls              | URLs embedded in the file.                                                                                                                                                             | Google TI users only.                                | A list of [URLs](url-object.md).                                                                                                                                                                                                                                                                                      |
| execution\_parents          | Files that executed the file.                                                                                                                                                          | Everyone.                                            | A list of [Files](file-object.md).                                                                                                                                                                                                                                                                                    |
| graphs                      | Graphs that include the file.                                                                                                                                                          | Everyone.                                            | A list of [Graphs](graph-object.md).                                                                                                                                                                                                                                                                                  |
| itw\_domains                | In the wild domain names from where the file has been downloaded.                                                                                                                      | Google TI users only.                                | A list of [Domains](domains-object.md).                                                                                                                                                                                                                                                                               |
| itw\_ips                    | In the wild IP addresses from where the file has been downloaded.                                                                                                                      | Google TI users only.                                | A list of [IP addresses](ip-object.md).                                                                                                                                                                                                                                                                               |
| itw\_urls                   | In the wild URLs from where the file has been downloaded.                                                                                                                              | Google TI users only.                                | A list of [URLs](url-object.md).                                                                                                                                                                                                                                                                                      |
| malware\_families           | Malware families associated to the file.                                                                                                                                               | Google TI Enterprise and Enterprise Plus users only. | A list of collections of type [malware family](malware-family-object.md).                                                                                                                                                                                                                                             |
| memory\_pattern\_domains    | Domain string patterns found in memory during sandbox execution.                                                                                                                       | Google TI users only.                                | List of [Domains](domains-object.md).                                                                                                                                                                                                                                                                                 |
| memory\_pattern\_ips        | IP address string patterns found in memory during sandbox execution.                                                                                                                   | Google TI users only.                                | List of [IP Addresses](ip-object.md).                                                                                                                                                                                                                                                                                 |
| memory\_pattern\_urls       | URL string patterns found in memory during sandbox execution.                                                                                                                          | Google TI users only.                                | List of [URLs](url-object.md).                                                                                                                                                                                                                                                                                        |
| overlay\_children           | Files contained by the file as an overlay.                                                                                                                                             | Google TI users only.                                | List of [Files](file-object.md).                                                                                                                                                                                                                                                                                      |
| overlay\_parents            | File that contain the file as an overlay.                                                                                                                                              | Google TI users only.                                | A list of [Files](file-object.md).                                                                                                                                                                                                                                                                                    |
| payloads\_extracted         | Files extracted by the payload file.                                                                                                                                                   | Google TI users only.                                | A list of [Files](file-object.md).                                                                                                                                                                                                                                                                                    |
| payload\_parents            | Files that have payloads of this file.                                                                                                                                                 | Google TI users only.                                | A list of [Files](file-object.md).                                                                                                                                                                                                                                                                                    |
| pcap\_children              | Files contained within the PCAP file.                                                                                                                                                  | Google TI users only.                                | A list of [Files](file-object.md).                                                                                                                                                                                                                                                                                    |
| pcap\_parents               | PCAP files that contain the file.                                                                                                                                                      | Google TI users only.                                | A list of [Files](file-object.md).                                                                                                                                                                                                                                                                                    |
| pe\_resource\_children      | Files contained by a PE file as a resource.                                                                                                                                            | Everyone.                                            | A list of [Files](file-object.md).                                                                                                                                                                                                                                                                                    |
| pe\_resource\_parents       | PE files containing the file as a resource.                                                                                                                                            | Everyone.                                            | A list of [Files](file-object.md).                                                                                                                                                                                                                                                                                    |
| related\_attack\_techniques | Returns the Attack Techniques of the Collections containing this File.                                                                                                                 | Google TI Enterprise and Enterprise Plus users only. | List of [Attack Techniques](object-attack-techniques.md).                                                                                                                                                                                                                                                             |
| related\_reports            | Reports that are directly and indirectly related to the file.                                                                                                                          | Google TI Enterprise and Enterprise Plus users only. | List of [Reports](report-object.md).                                                                                                                                                                                                                                                                                  |
| related\_threat\_actors     | File's related threat actors.                                                                                                                                                          | Google TI Enterprise and Enterprise Plus users only. | List of collections of type [Threat Actor](threat-actor-object.md).                                                                                                                                                                                                                                                   |
| reports                     | Reports directly associated to the file.                                                                                                                                               | Google TI Enterprise and Enterprise Plus users only. | A list of collections of type [Report](report-object.md).                                                                                                                                                                                                                                                             |
| screenshots                 | Screenshots related to the sandbox execution of the file.                                                                                                                              | Google TI users only.                                | A list of [Screenshots](screenshots-object.md).                                                                                                                                                                                                                                                                       |
| similar\_files              | Files that are similar to the file.                                                                                                                                                    | Google TI users only.                                | A list of [Files](file-object.md).                                                                                                                                                                                                                                                                                    |
| software\_toolkits          | Software and Toolkits associated to the file.                                                                                                                                          | Google TI Enterprise and Enterprise Plus users only. | A list of collections of type [Software and Toolkits](software-toolkit-object.md).                                                                                                                                                                                                                                    |
| submissions                 | Submissions for the file.                                                                                                                                                              | Google TI users only.                                | A list of [Submissions](submission-object.md).                                                                                                                                                                                                                                                                        |
| urls\_for\_embedded\_js     | URLs where this (JS) file is embedded.                                                                                                                                                 | Google TI users only.                                | List of [URLs](url-object.md).                                                                                                                                                                                                                                                                                        |
| user\_votes                 | File's votes made by current signed-in user.                                                                                                                                           | Everyone.                                            | A list of [Votes](vote-object.md).                                                                                                                                                                                                                                                                                    |
| votes                       | Votes for the file.                                                                                                                                                                    | Everyone.                                            | A list of [Votes](vote-object.md).                                                                                                                                                                                                                                                                                    |
| vulnerabilities             | Vulnerabilities associated to the file.                                                                                                                                                | Google TI Enterprise and Enterprise Plus users only. | A list of collections of type [Vulnerability](vulnerability-object.md).                                                                                                                                                                                                                                               |

**(1)** This endpoint requires you to have access to the Enterprise or Enterprise Plus module, which only comes with our top packages

---

← [🔀 related_threat_actors](domains-object/domains-object-related_threat_actors.md) · [up](README.md) · [exiftool](file-object/file-object-exiftool.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object>.*
