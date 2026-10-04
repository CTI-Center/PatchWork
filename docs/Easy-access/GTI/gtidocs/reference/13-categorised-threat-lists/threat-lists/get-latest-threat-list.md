---
title: "Get the latest Threat List"
source: https://gtidocs.virustotal.com/reference/get-latest-threat-list
slug: get-latest-threat-list
section: reference
group: "Categorised Threat Lists"
updatedAt: 2026-07-23T08:31:40.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Categorised Threat Lists](../README.md) › [Threat Lists](../threat-lists.md) › Get the latest Threat List

---

# get-the-latest-threat-list

> 🚧 Special privileges required
>
> Specific Threat Lists are only available to users with the Google Threat Intelligence (Google TI) Enterprise Plus or  Enterprise and Enterprise Plus licenses.

This endpoint provides Indicators of Compromise (IoCs) such as files, URLs domains and IP addresses, categorized by our security engine partners and/or Google TI experts as follows:

| Category name                    | Threat List ID (`threat_list_id`)  | Entities supported                 | License required               | Description                                                                                                          |
| -------------------------------- | ---------------------------------- | ---------------------------------- | ------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| Ransomware                       | `ransomware`                       | files                              | All                            | IoCs categorized as Ransomware by our security engine partners or Google TI experts.                                 |
| Malicious Network Infrastructure | `malicious-network-infrastructure` | URLs, domains, IP addresses        | All                            | Network related IoCs which have been related with Malware Infrastructure by our Google TI experts.                   |
| Malware                          | `malware`                          | files, URLs, domains, IP addresses | Enterprise and Enterprise Plus | IoCs that have been identified and classified as malware by our Google TI specialists.                               |
| Threat Actor                     | `threat-actor`                     | files, URLs, domains, IP addresses | Enterprise and Enterprise Plus | IoCs that our Google TI experts have linked to specific Threat Actors.                                               |
| Daily Top Trending               | `trending`                         | files, URLs, domains, IP addresses | Enterprise and Enterprise Plus | Top Trending IoCs based on daily lookups and relevance.                                                              |
| Mobile                           | `mobile`                           | files                              | Enterprise Plus                | IOS and Android files that have been identified as malware by our security engine partners.                          |
| OS X                             | `osx`                              | files                              | Enterprise Plus                | OS X files that have been identified as malware by our security engine partners.                                     |
| Linux                            | `linux`                            | files                              | Enterprise Plus                | Linux files that have been identified as malware by our security engine partners.                                    |
| Internet of Things               | `iot`                              | files                              | Enterprise Plus                | IoT files that have been identified as malware by our security engine partners.                                      |
| Cryptominers                     | `cryptominer`                      | files, URLs, domains, IP addresses | Enterprise Plus                | IoCs which our security engine partners have classified as Miners.                                                   |
| Phishing                         | `phishing`                         | URLs, domains, IP addresses        | Enterprise Plus                | Network related IoCs which our security engine partners have classified as Phishing.                                 |
| First Stage Delivery Vectors     | `first-stage-delivery-vectors`     | files                              | Enterprise Plus                | Emails attachments and files served by URLs, that have been identified as malware by our security engine partners.   |
| Vulnerability Weaponization      | `vulnerability-weaponization`      | files, URLs, domains, IP addresses | Enterprise Plus                | IoCs which have been related with Vulnerabilities exploitation by our security engine partners or Google TI experts. |
| Infostealers                     | `infostealer`                      | files                              | Enterprise Plus                | Files that have been categorized as Infostealers  by our security engine partners or Google TI experts.              |

Threat Lists are hourly generated as IoCs packages, with 2 hours difference from the current time. This means that if the current time in UTC is T you can get T-2h Threat List but any more recent than that.\
This endpoint returns the last generated IoCs package.\
Alternatively, Threat Lists can be retrieved for up to 30 days using the [/threat\_lists/\{threat\_list\_id}/\{time}](get-hourly-threat-list.md) endpoint.

## filtering

> 🚧 URL-encode query string
>
> All query strings must be properly URL-encoded to ensure that special characters are handled correctly by the API. Failure to do so can lead to your request being parsed incorrectly.
>
> For example, to filter for gti\_score:50+, you must encode the colon (:) and plus (+) characters. The correct query parameter would be: `&query=gti_score%3A50%2B`

IoCs can be filtered by IoC type with the `type` parameter (`type=file`, `type=url`, `type=ip_address`, `type=domain`). Additionally, multiple types can be included in a single request. Ex: `type=file,url` or `type=domain,url,ip_address`.

Alternatively, the `query` parameter can combine (with or without the `and` boolean operator) the following search modifiers for extra filtering:

* `gti_score`: filter IoCs by the Google TI score. Ex: `query=gti_score:60+`, `query=gti_score:60-`, `query=gti_score:1`
* `positives`: filter IoCs by the number of AV detections. Ex: `query=positives:2+`, `query=positives:5-`, `query=positives:1`
* `has:malware_families`: retrieve only IoCs that have  at least one associated Malware Family. Ex: `query=has:malware_families and positives:10+ and gti_score:30+`
* `has:campaigns`: retrieve only IoCs that have  at least one associated Campaign. Ex: `query=has:campaigns positives:15+ gti_score:60+`
* `has:reports`: retrieve only IoCs that have at least one associated Report. Ex: `query=has:reports positives:2-  gti_score:2-`
* `has:threat_actors`: retrieve only IoCs that have at least one associated Threat Actor. It is not needed for retrieving Threat Actor Threat Lists. Ex: `query=has:threat_actors positives:2- gti_score:30+`

Note that only one modifier of each type can be used simultaneously.

* **Use this**: `gti_score:0+ positives:0+ and has:malware_families has:campaigns has:reports has:threat_actors`.
* **Avoid this**: `gti_score:30+ gti_score:50-`, or `positives:1+ positives:3-`.

## formats

Threat Lists can be exported in several formats by specifying it with the `format` parameter. These are the available formats:

* json (by default format).
* csv - Ex. `format=csv`
* stix - Ex. `format=stix`
* stix-sentinel - Ex. `format=stix-sentinel`
* misp - Ex. `format=misp`

## response

```json
{
    "iocs": <_list of dictionaries_> list of IoCs.
    [
        {
            "data": <_dictionary_> data of an IoC.
            {
                "type": "file",
                "id": \<_string_> sha256 hash identifier of the IoC. This identifier can be used to retrieve the complete IoC report.
                "attributes": \<_dictionaries_> attributes of the IoC.
                {
                    "gti_assessment": \<_dictionary_> shows the Google TI calculated Threat Assessment of the IoC, split by numerical threat score, associated severity and the global verdict.
                    {
                        "verdict": \<_dictionary_> determines the likelihood that the IoC is malicious. Possible verdicts include.
                        {
                            "value": \<_string_>
                            **VERDICT_BENIGN** means that the IoC is considered harmless
                            **VERDICT_UNDETECTED** means that there are no immediate evidence of malicious intent
                            **VERDICT_SUSPICIOUS** represents potentially malicious activity **VERDICT_MALICIOUS** represents high confidence that the IoC poses a threat
                            **VERDICT_UNKNOWN** means that we were not able to generate a verdict for this IoC.
                        },
                        "threat_score": \<_dictionary_> numerical value representing the harmfulness of the threat behind the IoC if any.
                        {
                            "value": \<_integer_> numerical value between 0 (harmless) and 100 (harmful).
                        },
                        "severity": \<_dictionary_> severity or impact of the threat behind the IoC if any.
                        {
                            "value": \<_string_>
                            **SEVERITY_NONE** means that the IoC hasnn't a malicious verdict
                            **SEVERITY_LOW** means that the IoC likely has a minor impact but should still be monitored
                            **SEVERITY_MEDIUM** indicates a potential threat that warrants attention
                            **SEVERITY_HIGH** requires immediate action because the threat behind the IoC could have a critical impact
                            **SEVERITY_UNKNOWN**: not enough data to assess a severity.
                        }
                    },
                    "creation_date": \<_integer_> extracted when possible from the file's metadata. Indicates when it was built or compiled. It can also be faked by malware creators. UTC timestamp.
                    "last_analysis_date": \<_integer_> timestamp of the last time the threat severity was calculated.
                    "last_analysis_stats":\ <_dictionary_> a summary of the latest scan results.
                    {
                        "malicious": \<_integer_> the number of AV engines detecting the IoC as malicious.
                        "suspicious": \<_integer_> the number of AV engines detecting the IoC as suspicious.
                        "harmless": \<_integer_> the number of AV engines detecting the IoC as harmless.
                        "undetected": \<_integer_> the number of AV engines returning undetected verdict.
                    },
                    "last_modification_date": \<_integer_> date when any of the file's information was last updated. UTC timestamp.
                    "last_submission_date": \<_integer_> most recent date the file was posted to Google TI. UTC timestamp.
                    "first_submission_date": \<_integer_> date when the file was first seen in Google TI. UTC timestamp.
                    "md5": \<_strings_> file's MD5 hash.
                    "meaningful_name": \<_strings_> the most interesting name out of all file's names.
                    "names": \<_list of strings_> list of names with which the file was submitted to Google TI.
                    "positives": \<_integer_> number of AV detections.
                    "tags": \<_list of strings_> list of tags associated with the IoC.
                    "times_submitted": \<_integer_> number of times the IoC was submitted to Google TI.
                    "type_tags": \<_list of strings_> list of type-related tags associated with the IoC.
                    "vhash": \<_strings_> in-house similarity clustering algorithm value, based on a simple structural feature hash, allows you to find similar files.
                },
                "relationships": \<_dictionary_> other objects with which the IoC is related - associations with other objects.
                {
                    "malware_families":
                    {
                        "data": <_list of dictionaries_> list of malware families associated with the IoC.
                        [
                            {
                                "id": \<_strings_> identifier of the associated malmare family. This identifier can be used to retrieve the complete malware family data.
                                "type": "collection",
                                "attributes": \<_dictionary_> attributes of the associated malware family.
                                {
                                    "name": \<_strings_> name of the malware family.
                                    "collection_type": "malware-family"
                                }
                            }
                        ]
                    },
                    "reports":
                    {
                        "data": <_list of dictionaries_> list of reports associated with the IoC.
                        [
                            {
                                "id": \<_strings_> identifier of the associated report. This identifier can be used to retrieve the complete report data.
                                "type": "collection",
                                "attributes": \<_dictionary_> attributes of the associated report.
                                {
                                    "name": \<_strings_> name of the report.
                                    "collection_type": "report"
                                }
                            }
                        ]
                    },
                    "threat_actors":
                    {
                        "data": <_list of dictionaries_> list of threat actors associated with the IoC.
                        [
                            {
                                "id": \<_strings_> identifier of the associated threat actor. This identifier can be used to retrieve the complete threat actor data.
                                "type": "collection",
                                "attributes": \<_dictionary_> attributes of the associated threat actor.
                                {
                                    "name": \<_strings_> name of the threat actor.
                                    "collection_type": "threat-actor"
                                }
                            }
                        ]
                    },
                    "campaigns":
                    {
                        "data": <_list of dictionaries_> list of campaigns associated with the IoC.
                        [
                            {
                                "id": \<_strings_> identifier of the associated campaign. This identifier can be used to retrieve the complete campaign data.
                                "type": "collection",
                                "attributes": \<_dictionary_> attributes of the associated campaign.
                                {
                                    "name": \<_strings_> name of the campaign.
                                    "collection_type": "campaign"
                                }
                            }
                        ]
                    }
                }
            }
        },
        {
            "data":
            {
                "type": "ip_address",
                "id": \<_string_> IP address. This identifier can be used to retrieve the complete IoC report.
                "attributes":
                {
                    "gti_assessment": \<_dictionary_> _(as above)_ shows the Google TI calculated Threat Assessment of the IoC, split by numerical threat score, associated severity and the global verdict.
                    "asn": \<_integer_> autonomous System Number to which the IP belongs.
                    "as_owner": \<_string_> owner of the Autonomous System to which the IP belongs.
                    "continent": \<_string_> continent where the IP is placed (ISO-3166 continent code).
                    "country": \<_string_> country where the IP is placed (ISO-3166 country code).
                    "last_analysis_stats": \<_dictionary_> _(as above)_ a summary of the latest scan results.
                    "last_modification_date": \<_integer_> date when any of the IP's information was last updated. UTC timestamp.
                    "jarm": \<_string_> IP address' JARM hash.
                    "network": \<_string_> IPv4 network range to which the IP belongs.
                    "positives": \<_integer_> number of AV detections.
                    "regional_internet_registry": \<_string_> RIR (one of the current RIRs: AFRINIC, ARIN, APNIC, LACNIC or RIPE NCC).
                    "tags": \<_list of strings_> list of tags associated with the IoC.
                },
                "relationships": \<_dictionary_> _(as above)_ other objects with which the IoC is related - associations with other objects.
            }
        },
        {
            "data":
            {
                "type": "url",
                "id": \<_string_> URL hash identifier. This identifier can be used to retrieve the complete IoC report.
                "attributes":
                {
                    "gti_assessment": \<_dictionary_> _(as above)_ shows the Google TI calculated Threat Assessment of the IoC, split by numerical threat score, associated severity and the global verdict.
                    "categories": \<_list of strings_> list of URL categories from security partners.
                    "first_submission_date": \<_integer_> date when the URL was first seen in Google TI. UTC timestamp.
                    "last_analysis_date": \<_integer_> timestamp of the last time the threat severity was calculated.
                    "last_analysis_stats": \<_dictionary_> _(as above)_ a summary of the latest scan results.
                    "last_final_url": \<_string_> if the original URL redirects, where does it end.
                    "last_http_response_code": \<_integer_> HTTP response code of the last response.
                    "last_modification_date": \<_integer_> date when any of the URL's information was last updated. UTC timestamp.
                    "last_submission_date": \<_integer_> most recent date the URL was posted to Google TI. UTC timestamp.
                    "outgoing_links": \<_list of strings_> list of links to different domains.
                    "positives": \<_integer_> number of AV detections.
                    "tags": \<_list of strings_> list of tags associated with the IoC.
                    "title": \<_string_> webpage title.
                    "times_submitted": \<_integer_> number of times the IoC was submitted to Google TI.
                    "tld": \<_string_> URL's top-level domain.
                    "url": \<_string_> original URL to be scanned.
                },
                "relationships": \<_dictionary_> _(as above)_ other objects with which the IoC is related - associations with other objects.
            }
        },
        {
            "data":
            {
                "type": "domain",
                "id": \<_string_> domain name. This identifier can be used to retrieve the complete IoC report.
                "attributes":
                {
                    "gti_assessment": \<_dictionary_> _(as above)_ shows the Google TI calculated Threat Assessment of the IoC, split by numerical threat score, associated severity and the global verdict.
                    "categories": \<_list of strings_> list of domain categories from security partners.
                    "creation_date": \<_integer_> creation date extracted from the Domain's whois (UTC timestamp).
                    "jarm": \<_string_> domain's JARM hash.
                    "last_analysis_stats": \<_dictionary_> _(as above)_ a summary of the latest scan results.
                    "last_modification_date": \<_integer_> date when any of the domain's information was last updated. UTC timestamp.
                    "positives": \<_integer_> number of AV detections.
                    "tags": \<_list of strings_> list of tags associated with the IoC.
                    "tld": \<_string_> domain's top-level domain.
                },
                "relationships": \<_dictionary_> _(as above)_ other objects with which the IoC is related - associations with other objects.
            }
        },
    ]
}
```

In **CSV** format, elements belonging to a list such as `threat_actors.ids`, `names`, `malware_families.names`, `threat_actors.names`, `type_tags`, `tags`, `malware_families.ids` are plit by `;`.

```csv-file
gti_severity,creation_date,positives,type,last_analysis_date,first_submission_date,gti_threat_score,threat_actors.ids,names,malware_families.names,meaningful_name,vhash,threat_actors.names,last_submission_date,type_tags,gti_verdict,md5,tags,id,last_modification_date,times_submitted,malware_families.ids
```

````csv-url
last_http_response_code,last_submission_date,malware_families.ids,url,threat_actors.ids,malware_families.names,times_submitted,tld,gti_verdict,type,last_analysis_date,gti_threat_score,first_submission_date,last_modification_date,id,threat_actors.names,positives,gti_severity,categories
```csv

```csv-domain
gti_verdict,creation_date,type,gti_threat_score,gti_severity,positives,tld,id,jarm,threat_actors.names,last_modification_date,reports.names,reports.ids,malware_families.ids,malware_families.names,threat_actors.ids
````

```csv-ip_address
continent,country,positives,threat_actors.names,malware_families.names,gti_verdict,network,last_modification_date,malware_families.ids,gti_threat_score,gti_severity,threat_actors.ids,regional_internet_registry,type,id
```

In **MISP** format we provide the list of IoCs identifiers without additional information.

```stix
{
  "type": "bundle",
  "id": "bundle--0b7af7f4-d710-5fa2-a7da-a1663508c42c",
  "objects": [
    [...]
  ]
}
```

```stix-sentinel
{
  "sourcesystem": "Google Threat Intelligence",
  "indicators": [
    [...]
  ]
}
```

## example-response

```json
{
    "iocs":
    [
        {
            "data":
            {
                "type": "file",
                "id": "92293befae5fa3cc80d1beab93993b254742072879b296f89e9039bdb7a4edf4",
                "attributes":
                {
                    "gti_assessment":
                    {
                        "verdict":
                        {
                            "value": "VERDICT_MALICIOUS"
                        },
                        "threat_score":
                        {
                            "value": 30
                        },
                        "severity":
                        {
                            "value": "SEVERITY_LOW"
                        }
                    },
                    "creation_date": 1675657023,
                    "last_analysis_date": 1739966526,
                    "last_analysis_stats":
                    {
                        "malicious": 62,
                        "undetected": 11,
                        "typeUnsupported": 4
                    },
                    "last_modification_date": 1739973772,
                    "last_submission_date": 1691346962,
                    "md5": "7e51245673d182bcf760ca81e3b848e6",
                    "meaningful_name": "sqhost.exe",
                    "names":
                    [
                        "92293befae5fa3cc80d1beab93993b254742072879b296f89e9039bdb7a4edf4exe.exe",
                        "7e51245673d182bcf760ca81e3b848e6.virus",
                        "sqhost.exe"
                    ],
                    "positives": 62,
                    "tags":
                    [
                        "upx",
                        "peexe",
                        "overlay",
                        "spreader"
                    ],
                    "times_submitted": 3,
                    "type_tags":
                    [
                        "win32",
                        "executable",
                        "windows",
                        "pe",
                        "peexe"
                    ],
                    "vhash": "02503e0f7d1013z13z47z101013z13z15z17z"
                },
                "relationships":
                {
                    "malware_families":
                    {
                        "data":
                        [
                            {
                                "id": "malpedia_win_prometei",
                                "type": "collection",
                                "attributes":
                                {
                                    "name": "prometei",
                                    "collection_type": "malware-family"
                                }
                            }
                        ]
                    }
                }
            }
        }
    ]
}
```

## examples

Get the latest First Stage Delivery Vectors Threat List.

```python
import requests

threat_list_id = "first-stage-delivery-vectors"

url = f'https://www.virustotal.com/api/v3/threat_lists/{threat_list_id}/latest'
headers = {"accept": "application/json","x-apikey": <api-key>}

response = requests.get(url, headers=headers)
print(response.text)
```

Get 5 files from the last Cryptominers Threat List which are associated with a malware family, have 5 or more AV detections and the Google TI Score equal to or greater than 2.

```python
import requests
import urllib

threat_list_id = "cryptominer"
limit = 5
ioc_type = "file"
query = 'has:malware_families positives:5+ gti_score:2+'

url = f'https://www.virustotal.com/api/v3/threat_lists/{threat_list_id}/latest?type={ioc_type}&limit={limit}&query={urllib.parse.quote(query)}'
headers = {"accept": "application/json","x-apikey": <api-key>}

response = requests.get(url, headers=headers)
print(response.text)
```

Get the entire list of last identified Malware files that have associated malware families, campaigns and threat actors, and export IoCs in CSV format.

```python
import requests
import urllib

threat_list_id = "malware"
ioc_type = "file"
format = "csv"
query = 'has:malware_families has:campaigns has:threat_actors'

url = f'https://www.virustotal.com/api/v3/threat_lists/{threat_list_id}/latest?type={ioc_type}&format={format}&query={urllib.parse.quote(query)}'
headers = {"accept": "application/json","x-apikey": <api-key>}

response = requests.get(url, headers=headers)
print(response.text)
```

From the Phishing Threat List, get latest URLs in STIX format.

```python
import requests

threat_list_id = "phishing"
ioc_type = "url"
format = "stix"

url = f'https://www.virustotal.com/api/v3/threat_lists/{threat_list_id}/latest?type={ioc_type}&format={format}'
headers = {"accept": "application/json","x-apikey": <api-key>}

response = requests.get(url, headers=headers)
print(response.text)
```

From the Malicious Network Infrastructure Threat List, get latest domains in MISP format.

```python
import requests

threat_list_id = "malicious-network-infrastructure"
ioc_type = "domain"
format = "misp"

url = f'https://www.virustotal.com/api/v3/threat_lists/{threat_list_id}/latest?type={ioc_type}&format={format}'
headers = {"accept": "application/json","x-apikey": <api-key>}

response = requests.get(url, headers=headers)
print(response.text)
```

From the Daily Top trending Threat List, get latest IP addresses in JSON format.

```python
import requests

threat_list_id = "trending"
ioc_type = "ip_address"

url = f'https://www.virustotal.com/api/v3/threat_lists/{threat_list_id}/latest?type={ioc_type}'
headers = {"accept": "application/json","x-apikey": <api-key>}

response = requests.get(url, headers=headers)
print(response.text)
```

From the Malware Threat List, get latest network related IoCs in STIX Sentinel format.

```python
import requests

threat_list_id = "malware"
ioc_type = "ip_address,url,domain"
format = "stix-sentinel"

url = f'https://www.virustotal.com/api/v3/threat_lists/{threat_list_id}/latest?type={ioc_type}&format={format}'
headers = {"accept": "application/json","x-apikey": <api-key>}

response = requests.get(url, headers=headers)
print(response.text)
```

# openapi-definition

```json
{
  "components": {
    "securitySchemes": {
      "sec0": {
        "in": "header",
        "name": "x-apikey",
        "type": "apiKey"
      },
      "sec1": {
        "type": "http",
        "scheme": "custom",
        "description": "Custom authentication token. The token must be provided in the query string via \"auth_token\" parameter if you don't use the apiKey method."
      }
    }
  },
  "info": {
    "title": "Categorised Threat Lists",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Threat Lists"
    }
  ],
  "paths": {
    "/threat_lists/{threat_list_id}/latest": {
      "get": {
        "tags": [
          "Threat Lists"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-latest-threat-list",
        "parameters": [
          {
            "description": "Threat List identifier. Ex: ransomware, malware, cryptominer, etc",
            "in": "path",
            "name": "threat_list_id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Maximum number of IoCs to retrieve (max 4000)",
            "in": "query",
            "name": "limit",
            "schema": {
              "default": "2000",
              "type": "integer",
              "maximum": 4000
            }
          },
          {
            "description": "Type of IoC to be retrieve (file, url, ip_address or domain)",
            "in": "query",
            "name": "type",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Export format (json (default), csv, stix, stix-sentinel or misp)",
            "in": "query",
            "name": "format",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Extra filtering query",
            "in": "query",
            "name": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Authorization token (one of Authorization token or API key is required, but not both)",
            "in": "query",
            "name": "auth_token",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Your API key (one of Authorization token or API key is required, but not both)",
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "properties": {},
                  "type": "object"
                }
              }
            },
            "description": "200"
          },
          "400": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "properties": {},
                  "type": "object"
                }
              }
            },
            "description": "400"
          }
        },
        "security": [],
        "summary": "Get the latest Threat List"
      }
    }
  },
  "security": [
    {
      "sec0": [],
      "sec1": []
    }
  ],
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3"
    }
  ],
  "x-readme": {
    "explorer-enabled": true,
    "headers": [],
    "proxy-enabled": false,
    "samples-enabled": true
  }
}
```

---

← [List provisioned Categorised Threat Lists](list-provisioned-threat-lists.md) · [up](../README.md) · [Get an hourly Threat List](get-hourly-threat-list.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-latest-threat-list>.*
