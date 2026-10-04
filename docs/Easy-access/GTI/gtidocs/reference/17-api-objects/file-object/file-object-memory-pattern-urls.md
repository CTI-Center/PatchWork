---
title: "🔀 memory_pattern_urls"
source: https://gtidocs.virustotal.com/reference/file-object-memory-pattern-urls
slug: file-object-memory-pattern-urls
section: reference
group: "API OBJECTS"
updatedAt: 2026-06-22T14:05:01.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Files](../file-object.md) › 🔀 memory_pattern_urls

---

# 🔀-memory_pattern_urls

URLs extracted from the memory pattern of the file.

The *memory\_pattern\_urls* relationship returns the list of ***all URLs includded in the memory pattern of a given file***. This relationship is only available for Premium API users.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/files/files-relationships.md). The response contains a list of [URL](../url-object.md) objects.

```json /files/{file_hash}/memory_pattern_urls
{
  "data": [
    <URL_OBJECT>,
    <URL_OBJECT>,
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
      "id": "006289eb4515a94c57c9a053106029964618fb18e283a7ff5ced28d5b304048e",
      "type": "url",
      "links": {
        "self": "https://www.virustotal.com/api/v3/urls/006289eb4515a94c57c9a053106029964618fb18e283a7ff5ced28d5b304048e"
      },
      "attributes": {
        "last_http_response_headers": {
          "Server": "nginx/1.18.0 (Ubuntu)",
          "Date": "Wed, 25 Sep 2024 10:55:13 GMT",
          "Content-Type": "text/html",
          "Transfer-Encoding": "chunked",
          "Connection": "keep-alive"
        },
        "categories": {
          "alphaMountain.ai": "Malicious, Phishing (alphaMountain.ai)",
          "Sophos": "spyware and malware",
          "Webroot": "Phishing and Other Frauds",
          "Forcepoint ThreatSeeker": "malicious web sites"
        },
        "last_analysis_stats": {
          "malicious": 12,
          "suspicious": 1,
          "undetected": 26,
          "harmless": 57,
          "timeout": 0
        },
        "url": "http://185.215.113.43/Zu7JuNko/index.phpW",
        "last_http_response_content_sha256": "340c8464c2007ce3f80682e15dfafa4180b641d53c14201b929906b7b0284d87",
        "first_submission_date": 1727261411,
        "last_submission_date": 1727261411,
        "last_analysis_date": 1727261411,
        "reputation": 0,
        "total_votes": {
          "harmless": 0,
          "malicious": 0
        },
        "title": "404 Not Found",
        "webrisk": {
          "scores": [
            {
              "confidenceLevel": "SAFE",
              "threatType": "UNWANTED_SOFTWARE"
            },
            {
              "confidenceLevel": "LOW",
              "threatType": "SOCIAL_ENGINEERING"
            },
            {
              "confidenceLevel": "SAFE",
              "threatType": "MALWARE"
            }
          ]
        },
        "threat_names": [
          "Mal/HTMLGen-A"
        ],
        "threat_severity": {
          "version": "U3",
          "threat_severity_level": "SEVERITY_NONE",
          "threat_severity_data": {
            "num_detections": 12
          },
          "last_analysis_date": "1727261731",
          "level_description": "Severity NONE because it has less than 2 detections."
        },
        "tags": [
          "ip"
        ],
        "last_modification_date": 1727261732,
        "threat_verdict": "VERDICT_UNDETECTED",
        "last_http_response_code": 404,
        "private": false,
        "last_final_url": "http://185.215.113.43/Zu7JuNko/index.phpW",
        "redirection_chain": [
          "http://185.215.113.43/Zu7JuNko/index.phpW"
        ],
        "has_content": false,
        "last_analysis_results": {
          "Artists Against 419": {
            "method": "blacklist",
            "engine_name": "Artists Against 419",
            "category": "harmless",
            "result": "clean"
          },
          "Acronis": {
            "method": "blacklist",
            "engine_name": "Acronis",
            "category": "harmless",
            "result": "clean"
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
          "Lionic": {
            "method": "blacklist",
            "engine_name": "Lionic",
            "category": "harmless",
            "result": "clean"
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
            "category": "malicious",
            "result": "phishing"
          },
          "AlphaSOC": {
            "method": "blacklist",
            "engine_name": "AlphaSOC",
            "category": "malicious",
            "result": "malware"
          },
          "Antiy-AVL": {
            "method": "blacklist",
            "engine_name": "Antiy-AVL",
            "category": "malicious",
            "result": "malicious"
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
          "Axur": {
            "method": "blacklist",
            "engine_name": "Axur",
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
            "category": "malicious",
            "result": "malware"
          },
          "Bkav": {
            "method": "blacklist",
            "engine_name": "Bkav",
            "category": "undetected",
            "result": "unrated"
          },
          "BlockList": {
            "method": "blacklist",
            "engine_name": "BlockList",
            "category": "harmless",
            "result": "clean"
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
          "Snort IP sample list": {
            "method": "blacklist",
            "engine_name": "Snort IP sample list",
            "category": "harmless",
            "result": "clean"
          },
          "Cluster25": {
            "method": "blacklist",
            "engine_name": "Cluster25",
            "category": "undetected",
            "result": "unrated"
          },
          "CMC Threat Intelligence": {
            "method": "blacklist",
            "engine_name": "CMC Threat Intelligence",
            "category": "harmless",
            "result": "clean"
          },
          "Xcitium Verdict Cloud": {
            "method": "blacklist",
            "engine_name": "Xcitium Verdict Cloud",
            "category": "undetected",
            "result": "unrated"
          },
          "CRDF": {
            "method": "blacklist",
            "engine_name": "CRDF",
            "category": "malicious",
            "result": "malicious"
          },
          "CSIS Security Group": {
            "method": "blacklist",
            "engine_name": "CSIS Security Group",
            "category": "undetected",
            "result": "unrated"
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
            "category": "malicious",
            "result": "malicious"
          },
          "desenmascara.me": {
            "method": "blacklist",
            "engine_name": "desenmascara.me",
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
          "Emsisoft": {
            "method": "blacklist",
            "engine_name": "Emsisoft",
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
            "category": "suspicious",
            "result": "suspicious"
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
          "Feodo Tracker": {
            "method": "blacklist",
            "engine_name": "Feodo Tracker",
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
            "category": "malicious",
            "result": "malware"
          },
          "Google Safebrowsing": {
            "method": "blacklist",
            "engine_name": "Google Safebrowsing",
            "category": "harmless",
            "result": "clean"
          },
          "GCP Abuse Intelligence": {
            "method": "blacklist",
            "engine_name": "GCP Abuse Intelligence",
            "category": "undetected",
            "result": "unrated"
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
            "category": "malicious",
            "result": "malware"
          },
          "Lumu": {
            "method": "blacklist",
            "engine_name": "Lumu",
            "category": "undetected",
            "result": "unrated"
          },
          "Malwared": {
            "method": "blacklist",
            "engine_name": "Malwared",
            "category": "harmless",
            "result": "clean"
          },
          "MalwareURL": {
            "method": "blacklist",
            "engine_name": "MalwareURL",
            "category": "undetected",
            "result": "unrated"
          },
          "MalwarePatrol": {
            "method": "blacklist",
            "engine_name": "MalwarePatrol",
            "category": "harmless",
            "result": "clean"
          },
          "malwares.com URL checker": {
            "method": "blacklist",
            "engine_name": "malwares.com URL checker",
            "category": "harmless",
            "result": "clean"
          },
          "Netcraft": {
            "method": "blacklist",
            "engine_name": "Netcraft",
            "category": "malicious",
            "result": "malicious"
          },
          "OpenPhish": {
            "method": "blacklist",
            "engine_name": "OpenPhish",
            "category": "harmless",
            "result": "clean"
          },
          "0xSI_f33d": {
            "method": "blacklist",
            "engine_name": "0xSI_f33d",
            "category": "undetected",
            "result": "unrated"
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
          "Rising": {
            "method": "blacklist",
            "engine_name": "Rising",
            "category": "harmless",
            "result": "clean"
          },
          "SafeToOpen": {
            "method": "blacklist",
            "engine_name": "SafeToOpen",
            "category": "undetected",
            "result": "unrated"
          },
          "Sangfor": {
            "method": "blacklist",
            "engine_name": "Sangfor",
            "category": "harmless",
            "result": "clean"
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
          "SOCRadar": {
            "method": "blacklist",
            "engine_name": "SOCRadar",
            "category": "undetected",
            "result": "unrated"
          },
          "Sophos": {
            "method": "blacklist",
            "engine_name": "Sophos",
            "category": "malicious",
            "result": "malware"
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
          "securolytics": {
            "method": "blacklist",
            "engine_name": "securolytics",
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
          "Underworld": {
            "method": "blacklist",
            "engine_name": "Underworld",
            "category": "undetected",
            "result": "unrated"
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
          "ViriBack": {
            "method": "blacklist",
            "engine_name": "ViriBack",
            "category": "harmless",
            "result": "clean"
          },
          "VX Vault": {
            "method": "blacklist",
            "engine_name": "VX Vault",
            "category": "harmless",
            "result": "clean"
          },
          "Webroot": {
            "method": "blacklist",
            "engine_name": "Webroot",
            "category": "malicious",
            "result": "malicious"
          },
          "Forcepoint ThreatSeeker": {
            "method": "blacklist",
            "engine_name": "Forcepoint ThreatSeeker",
            "category": "malicious",
            "result": "malicious"
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
          "ZeroFox": {
            "method": "blacklist",
            "engine_name": "ZeroFox",
            "category": "undetected",
            "result": "unrated"
          }
        },
        "times_submitted": 1,
        "last_http_response_content_length": 162,
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
      },
      "context_attributes": {
        "url": "http://185.215.113.43/Zu7JuNko/index.phpW"
      }
    }
  ],
  "meta": {
    "count": 77,
    "cursor": "eyJsaW1pdCI6IDEsICJvZmZzZXQiOiAxfQ=="
  },
  "links": {
    "self": "https://www.virustotal.com/api/v3/files/0f40fa13ff13ac967c3582d2b386a32638306821aed9d914a0f31629d3617fa5/memory_pattern_urls?limit=1",
    "next": "https://www.virustotal.com/api/v3/files/0f40fa13ff13ac967c3582d2b386a32638306821aed9d914a0f31629d3617fa5/memory_pattern_urls?limit=1&cursor=eyJsaW1pdCI6IDEsICJvZmZzZXQiOiAxfQ%3D%3D"
  }
}
```

---

← [🔀 memory_pattern_ips](file-object-memory-pattern-ips.md) · [up](../README.md) · [🔀 screenshots](file-object-screenshots.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-object-memory-pattern-urls>.*
