---
title: "Network hunting"
source: https://gtidocs.virustotal.com/docs/nethunt
slug: nethunt
section: guides
group: "IOC Investigation"
updatedAt: 2025-09-29T08:14:01.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [IOC Investigation](../README.md) › [Livehunt](../livehunt-guide.md) › Network hunting

---

# network-hunting

# hunting-network-assets

In addition to hunting all scanned files in Google Threat Intelligence, you can also hunt for all scanned URLs, domains and IP addresses. For this now you need to choose between File, URL, Domain or IP when you create a new Livehunt ruleset.

![Hunting types](https://storage.googleapis.com/gtidocresources/guides/ioc-investigation/livehunt-guide/images/nethunt_image_20240901.png)

The "vt" module is now expanded with a ".net" attribute that contains all metadata extracted from the URL, its Domain and the IP address where it's hosted. It also has complementary attributes to easily reference specific IoCs characteristics without having to deal with data's internal representation. Instead of that, [self-descriptive](hunting-reference.md#http-methods) enums are provided.

The tables below summarize all "vt" module attributes.
The first table is focused on the **main attributes**:

* The first column shows the **entity type** that the YARA rule match against
* The second column shows the **main attribute** used in the rule
* The third column shows other **secondary attributes** belonging to different entity types and **complementary attributes** that can be **combined in the same YARA rule**
* The last column provides a brief **description** of the **main attribute**

| Type of IoC/entity | "vt" module attribute                | Other fields combination                                                   | Description                                                                       |
| ------------------ | ------------------------------------ | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| URL                | [vt.net.url](#url-metadata)          | vt.net.domain <br/> vt.net.ip <br/> vt.FileType (complementary attributes) | URL characteristics and other IoCs relationships                                  |
| Domain             | [vt.net.domain](#domain-metadata)    | vt.net.ip <br/> vt.FileType (complementary attributes)                     | Domain characteristics and other IoCs relationships                               |
| IP Address         | [vt.net.ip](#ip-metadata)            | vt.FileType (complementary attributes)                                     | IP addresses characteristics and other IoCs relationships                         |
| Files \*static     | [vt.metadata](hunting-metadata.md)  | vt.FileType and vt.behaviour + rest of complementary attributes            | File metadata                                                                     |
| Files \*dynamic    | [vt.behaviour](hunting-behavior.md) | vt.metadata + vt.FileType and the rest of complementary attributes         | File characteristics extracted via sandbox execution and other IoCs relationships |

The second table shows the **complementary attributes**, basically enums that can be used in combination with the previous attributes to deploy a functional rule.

| Type of IoC/entity | "vt" module attribute                                           | Description                                                                                 |
| ------------------ | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Files \*static     | [vt.FileType](hunting-reference.md#file-types)                 | Enum of available file types                                                                |
| Files \*dynamic    | [vt.BehaviourTrait](hunting-reference.md#behaviour-traits)     | Enum of behavior traits that can be found on a file behavior report after sandbox execution |
| Files \*dynamic    | [vt.BehaviourVerdict](hunting-reference.md#behaviour-verdicts) | Enum of sandbox verdicts based on file behavior after sandbox execution                     |
| Files \*dynamic    | [vt.Http](hunting-reference.md#http-methods)                   | Enum of HTTP methods                                                                        |
| Files \*dynamic    | [vt.Net](hunting-reference.md#network-protocols)               | Enum of network protocols                                                                   |

⚠️ Please note that `vt.net` and `vt.Net` are different attributes. The first one represents network entities while the second one provides an abstraction layer of the internal representation of the network protocols.

Let's walk through some examples:

Get all detected URLs under a specific domain first select "Create a new rule" and choose to match URL, these will produce URL notifications.

```yara
import "vt"

rule detectedPythonPackages {
meta:
  description = "URLs with detections matching files.pythonhosted.org domain"
  author = "google_ti"
  target_entity = "url"
condition:
  vt.net.url.analysis_stats.malicious > 1 and
  vt.net.domain.raw == "files.pythonhosted.org"
}
```

Notice how is possible to combine `vt.net.url` and `vt.net.domain`, it works in a top down fashion:

* URL matching rules will allow `vt.net.url`, `vt.net.domain` and `vt.net.ip` fields
* Domain matching rules will allow `vt.net.domain` and `vt.net.ip` fields
* IP matching rules will allow only `vt.net.ip` fields

In a similar way we can create another URL rule to monitor new URLs from the [LilithBot campaign](https://www.zscaler.com/blogs/security-research/analysis-lilithbot-malware-and-eternity-threat-group):

```yara
import "vt"

rule LilithBot {
meta:
  description = "URLs matching LilithBot C2C"
  author = "google_ti"
  target_entity = "url"
condition:
  vt.net.url.raw matches /\/gate\/.{60}\/registerBot/ or
  vt.net.url.raw matches /\/gate\/.{60}\/getFile\?name=admin_settings_plugin\.json/ or
  vt.net.url.raw matches /\/gate\/.{60}\/uploadFile\?name/
}
```

The vt.net module contains the following metadata:

## url-metadata

| Field                                           | Type            | Description                                                                                                                                                                                          | Example                                                                                                                                                           |
| ----------------------------------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| vt.net.url.raw                                  | string          | The URL in canonical form.                                                                                                                                                                           | vt.net.url.raw matches /.\*\\.php/                                                                                                                                |
| vt.net.url.path                                 | string          | Path part of the current URL.                                                                                                                                                                        | vt.net.url.path icontains "private/reviewsGallery/get-image-gallery-assets"                                                                                       |
| vt.net.url.query                                | string          | Raw URL query string                                                                                                                                                                                 | vt.net.url.query contains "dir="                                                                                                                                  |
| vt.net.url.hostname                             | string          | Hostname part of the current URL.                                                                                                                                                                    | vt.net.url.hostname iendswith "google.com"                                                                                                                        |
| vt.net.url.new\_url                             | bool            | Whether the URL is observed for the first time or not.                                                                                                                                               |                                                                                                                                                                   |
| vt.net.url.first\_submission\_date              | int             | UNIX UTC timestamp for the URL's first submission date.                                                                                                                                              | vt.net.url.first\_submission\_date < 1672531200                                                                                                                   |
| vt.net.url.params                               | dict            | Parsed URL GET params                                                                                                                                                                                | for any k, v in vt.net.url.params: ( k == "user" )                                                                                                                |
| vt.net.url.port                                 | int             | The port in which the URL is accessed                                                                                                                                                                | vt.net.url.port > 8080 and vt.net.url.port < 8090                                                                                                                 |
| vt.net.url.trackers                             | array of struct | All trackers found in the URL                                                                                                                                                                        | for any tracker in vt.net.url.trackers: ( tracker.name == "Google Tag Manager" and tracker.id == "G-Y8J4SNTNFY" )                                                 |
| vt.net.url.trackers\[x].name                    | string          | Tracker name                                                                                                                                                                                         |                                                                                                                                                                   |
| vt.net.url.trackers\[x].id                      | string          | Tracker assigned unique ID                                                                                                                                                                           |                                                                                                                                                                   |
| vt.net.url.trackers\[x].url                     | string          | URL the tracker is loaded from                                                                                                                                                                       | for any tracker in vt.net.url.trackers: ( tracker.url contains "google-analytics.com/analytics.js" )                                                              |
| vt.net.url.response\_headers                    | dict            | Headers returned when making a request to the URL                                                                                                                                                    | vt.net.url.response\_headers\["Server"] == "nginx"                                                                                                                |
| vt.net.url.number\_of\_response\_headers        | int             | Amount of response headers                                                                                                                                                                           | vt.net.url.number\_of\_response\_headers == 10                                                                                                                    |
| vt.net.url.response\_code                       | int             | HTTP status code seen when making a request to the URL                                                                                                                                               | vt.net.url.response\_code == 429                                                                                                                                  |
| vt.net.url.cookies                              | dict            | Request cookies                                                                                                                                                                                      | for any k, v in vt.net.url.cookies: ( k == "APPSESSID" ) and vt.net.url.cookies\["APPSESSID"] contains "xxx"                                                      |
| vt.net.url.favicon.raw\_md5                     | string          | MD5 hash of the URL's favicon. To find a property raw md5 search VT for its URL and check details. [Retrieving raw\_md5](#how-do-i-obtain-a-domain-favicon-hashes).                                  | vt.net.url.favicon.raw\_md5 == "6cf6865d5e5cb8f65fe9c0ff93a7904d"                                                                                                 |
| vt.net.url.favicon.dhash                        | string          | The URL's favicon dhash. To find a property dhash search VT for its URL and check details. [Retrieving dhash](#how-do-i-obtain-a-domain-favicon-hashes).                                             | vt.net.url.favicon.dhash == "924dccd4d46933cc"                                                                                                                    |
| vt.net.url.outgoing\_links                      | array of string | Links included in the URL's response pointing to URLs from other domains.                                                                                                                            | for any link in vt.net.url.outgoing\_links: ( link matches /.\*www\\.bankofamerica\\.com.\*/ )                                                                    |
| vt.net.url.redirects                            | array of string | List of redirecting URLs visited until reaching the final one.                                                                                                                                       | for any r in vt.net.url.redirects: ( not r contains vt.net.domain.domain )                                                                                        |
| vt.net.url.html\_title                          | string          | Text found under the URL's returned HTML \<title> tag                                                                                                                                                |                                                                                                                                                                   |
| vt.net.url.html\_meta\_tags                     | dict            | Values found under the `meta` tags in the returned HTML                                                                                                                                              | for any meta\_tags in vt.net.url.html\_meta\_tags: ( meta\_tags.key == "og:title" and for any value in meta\_tags.values: ( value == "Amazon - Start a Career" )) |
| vt.net.url.tags                                 | array of string | Tags defining interesting features of the URL                                                                                                                                                        | for any tag in vt.net.url.tags: ( tag == "opendir" or tag == "ip" )                                                                                               |
| vt.net.url.analysis\_stats                      | struct          | [Analysis Stats Struct info](#analysis-stats-struct)                                                                                                                                                 | vt.net.url.analysis\_stats.malicious > 1                                                                                                                          |
| vt.net.url.categories                           | dict            | Content categories of its domain by engine                                                                                                                                                           | for any engine, value in vt.net.url.categories: (value == "known infection source")                                                                               |
| vt.net.url.signatures                           | dict            | Signature returned by the engine.                                                                                                                                                                    | for any engine, value in vt.net.url.signatures: ( engine == "Kaspersky" and value icontains "pua" )                                                               |
| vt.net.url.downloaded\_file                     | struct          | Metadata from the latest file downloaded from the URL.                                                                                                                                               |                                                                                                                                                                   |
| vt.net.url.downloaded\_file.new\_for\_vt        | bool            | Indicates that the file has not been previously seen in VT.                                                                                                                                          |                                                                                                                                                                   |
| vt.net.url.downloaded\_file.new\_for\_url       | bool            | Indicates that the file has not been previously seen being downloaded from that particular URL.                                                                                                      |                                                                                                                                                                   |
| vt.net.url.downloaded\_file.new\_for\_domain    | bool            | Indicates that the file has not been previously seen being downloaded from the URL's domain.                                                                                                         |                                                                                                                                                                   |
| vt.net.url.downloaded\_file.new\_for\_ip        | bool            | Indicates that the file has not been previously seen being downloaded from the IP the URL resolves to.                                                                                               |                                                                                                                                                                   |
| vt.net.url.downloaded\_file.sha256              | string          | Latest downloaded file SHA256.                                                                                                                                                                       |                                                                                                                                                                   |
| vt.net.url.downloaded\_file.file\_type          | int             | Latest downloaded file's type (one of the types listed in the file types table).                                                                                                                     |                                                                                                                                                                   |
| vt.net.url.downloaded\_file.analysis\_stats     | struct          | Latest downloaded file analysis stats. [Analysis Stats Struct info](#analysis-stats-struct)                                                                                                          |                                                                                                                                                                   |
| vt.net.url.downloaded\_file.signatures          | dict            | Signature returned by the engine.                                                                                                                                                                    |                                                                                                                                                                   |
| vt.net.url.communicating\_file                  | struct          | Metadata from the latest file that has made communications (behaviour) with this URL.                                                                                                                |                                                                                                                                                                   |
| vt.net.url.communicating\_file.new\_for\_vt     | bool            | File has not been previously seen in VT.                                                                                                                                                             |                                                                                                                                                                   |
| vt.net.url.communicating\_file.new\_for\_url    | bool            |                                                                                                                                                                                                      |                                                                                                                                                                   |
| vt.net.url.communicating\_file.new\_for\_domain | bool            |                                                                                                                                                                                                      |                                                                                                                                                                   |
| vt.net.url.communicating\_file.new\_for\_ip     | bool            |                                                                                                                                                                                                      |                                                                                                                                                                   |
| vt.net.url.communicating\_file.sha256           | string          | Latest file (sha256) making communications with this URL.                                                                                                                                            |                                                                                                                                                                   |
| vt.net.url.communicating\_file.file\_type       | int             | Latest file type making communications with this URL (one of the types listed in the file types table).                                                                                              |                                                                                                                                                                   |
| vt.net.url.communicating\_file.analysis\_stats  | struct          | [Analysis Stats Struct info](#analysis-stats-struct)                                                                                                                                                 |                                                                                                                                                                   |
| vt.net.url.submitter.city                       | string          | City from where the resource was submitted, referred to the last submission. All lowercases.                                                                                                         |                                                                                                                                                                   |
| vt.net.url.submitter.country                    | string          | Country from where the resource was submitted, referred to the last submission. This is a two-letter [ISO 3166](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code, in uppercase.        |                                                                                                                                                                   |
| vt.net.url.gti\_assessment.severity.value       | string          | Severity of the URL provided by Google Threat Intelligence. One of the values defined on the [Google TI assessment severity types](hunting-reference.md#google-ti-assessment-severity-types) table. | vt.net.url.gti\_assessment.severity.value == vt.GtiSeverity.SEVERITY\_MEDIUM                                                                                      |
| vt.net.url.gti\_assessment.threat\_score.value  | integer         | Threat score of the URL provided by Google Threat Intelligence. This is a value between 1 and 100.                                                                                                   | vt.net.url.gti\_assessment.threat\_score.value > 20                                                                                                               |
| vt.net.url.gti\_assessment.verdict.value        | string          | Verdict of the file provided by [Google Threat Intelligence](hunting-reference.md#google-ti-assessment-verdicts). One of the values defined on the Google TI assessment verdicts table.             | vt.net.url.gti\_assessment.verdict.value == vt.GtiVerdict.VERDICT\_MALICIOUS                                                                                      |

## ip-metadata

| Field                                                   | Type   | Description                                                                                                                                                                                         | Example                                                                                            |
| ------------------------------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| vt.net.ip.raw                                           |        | The URL in canonical form.                                                                                                                                                                          |                                                                                                    |
| vt.net.ip.new\_ip                                       |        |                                                                                                                                                                                                     |                                                                                                    |
| vt.net.ip.whois                                         | dict   | Whois record in key, value format.                                                                                                                                                                  | vt.net.ip.whois\["Admin Country"] == "ES"                                                          |
| vt.net.ip.whois\_raw                                    | string | Whole IP whois as a string for pattern matching.                                                                                                                                                    |                                                                                                    |
| vt.net.ip.new\_whois                                    | bool   | IP has an updated whois.                                                                                                                                                                            |                                                                                                    |
| vt.net.ip.reverse\_lookup                               | string | Domain observed resolving to this IP address for first time. [Creating a feed of domain IP resolutions](#how-do-i-obtain-a-feed-of-ip-resolutions-for-a-certain-domain).                            | vt.net.ip.reverse\_lookup equals "yourdomain.com"                                                  |
| vt.net.ip.jarm                                          | string | TLS fingerprint                                                                                                                                                                                     |                                                                                                    |
| vt.net.ip.https\_certificate.thumbprint                 |        |                                                                                                                                                                                                     |                                                                                                    |
| vt.net.ip.https\_certificate.subject                    | struct | [Certificate Subject info](#https-certificate-subject-struct)                                                                                                                                       |                                                                                                    |
| vt.net.ip.https\_certificate.validity.not\_after        | int    | Timestamp after which the certificate is no longer valid, in seconds since the Unix epoch                                                                                                           | vt.net.ip.https\_certificate.validity.not\_after < 1672531200  // 2023-01-01                       |
| vt.net.ip.https\_certificate.validity.not\_before       | int    | Timestamp at which the certificate becomes valid, in seconds since the Unix epoch                                                                                                                   | vt.net.ip.https\_certificate.validity.not\_before < 946684800  // 2000-01-01                       |
| vt.net.ip.https\_certificate.subject\_alternative\_name | string |                                                                                                                                                                                                     |                                                                                                    |
| vt.net.ip.https\_certificate.signature                  | string |                                                                                                                                                                                                     |                                                                                                    |
| vt.net.ip.https\_certificate.serial\_number             | string |                                                                                                                                                                                                     |                                                                                                    |
| vt.net.ip.https\_certificate.issuer                     | struct | [Certificate Subject info](#https-certificate-subject-struct)                                                                                                                                       |                                                                                                    |
| vt.net.ip.analysis\_stats                               | struct | [Analysis Stats Struct info](#analysis-stats-struct)                                                                                                                                                |                                                                                                    |
| vt.net.ip.signatures                                    | dict   | Signature returned by the engine.                                                                                                                                                                   | for any engine, value in vt.net.ip.signatures: ( engine == "Kaspersky" and value icontains "pua" ) |
| vt.net.ip.downloaded\_file                              | struct | Metadata from the latest file downloaded from the IP.                                                                                                                                               |                                                                                                    |
| vt.net.ip.downloaded\_file.new\_for\_vt                 | bool   | Seen for the first time being downloaded in Google TI.                                                                                                                                              |                                                                                                    |
| vt.net.ip.downloaded\_file.new\_for\_ip                 | bool   | Seen for the first time being downloaded from this IP. Notice that it may already be known in Google TI.                                                                                            |                                                                                                    |
| vt.net.ip.downloaded\_file.sha256                       | string | Latest downloaded file SHA256.                                                                                                                                                                      |                                                                                                    |
| vt.net.ip.downloaded\_file.file\_type                   | int    | Latest downloaded file's type (one of the types listed in the file types table).                                                                                                                    |                                                                                                    |
| vt.net.ip.downloaded\_file.analysis\_stats              | struct | [Analysis Stats Struct info](#analysis-stats-struct)                                                                                                                                                |                                                                                                    |
| vt.net.ip.downloaded\_file.signatures                   | dict   | Signature returned by the engine.                                                                                                                                                                   |                                                                                                    |
| vt.net.ip.communicating\_file                           | struct | Metadata from the latest file that has made communications (behavior) with this IP.                                                                                                                 |                                                                                                    |
| vt.net.ip.communicating\_file.new\_for\_ip              | bool   | A communicating file is seen for the first time connected to this IP. Notice that it may already be known in Google TI.                                                                             |                                                                                                    |
| vt.net.ip.communicating\_file.new\_for\_vt              | bool   |                                                                                                                                                                                                     |                                                                                                    |
| vt.net.ip.communicating\_file.sha256                    | string | Latest file sha256 that made communications with this IP.                                                                                                                                           |                                                                                                    |
| vt.net.ip.communicating\_file.file\_type                | int    | Latest file type (one of the types listed in the file types table) that made communications with this IP.                                                                                           |                                                                                                    |
| vt.net.ip.communicating\_file.analysis\_stats           | struct | [Analysis Stats Struct info](#analysis-stats-struct)                                                                                                                                                |                                                                                                    |
| vt.net.ip.communicating\_file.signatures                | dict   | Signature returned by the engine.                                                                                                                                                                   |                                                                                                    |
| vt.net.ip.ip\_as\_owner                                 | string | IP AS (Autonomous System) owner                                                                                                                                                                     |                                                                                                    |
| vt.net.ip.ip\_asn                                       | int    | Autonomous System Number                                                                                                                                                                            |                                                                                                    |
| vt.net.ip.ip\_country                                   | string | IP Country                                                                                                                                                                                          |                                                                                                    |
| vt.net.ip.ip\_as\_int                                   | int    | IP dotless decimal number notation                                                                                                                                                                  | vt.net.ip.ip\_as\_int == 3941835776                                                                |
| vt.net.ip.gti\_assessment.severity.value                | string | Severity of the IP provided by Google Threat Intelligence. One of the values defined on the [Google TI assessment severity types](hunting-reference.md#google-ti-assessment-severity-types) table. | vt.net.ip.gti\_assessment.severity.value == vt.GtiSeverity.SEVERITY\_MEDIUM                        |
| vt.net.ip.gti\_assessment.threat\_score.value           | int    | Threat score of the IP provided by Google Threat Intelligence. This is a value between 1 and 100.                                                                                                   | vt.net.ip.gti\_assessment.threat\_score.value > 20                                                 |
| vt.net.ip.gti\_assessment.verdict.value                 | string | Verdict of the IP provided by [Google Threat Intelligence](hunting-reference.md#google-ti-assessment-verdicts). One of the values defined on the Google TI assessment verdicts table.              | vt.net.ip.gti\_assessment.verdict.value == vt.GtiVerdict.VERDICT\_MALICIOUS                        |

## domain-metadata

| Field                                                       | Type             | Description                                                                                                                                                                                             | Example                                                                                                |
| ----------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| vt.net.domain.raw                                           | string           | Domain as a string                                                                                                                                                                                      | vt.net.domain.raw matches /virustotal/                                                                 |
| vt.net.domain.root                                          | string           | Root part of the domain, ie: sub2.sub.root.tld -> root.tld                                                                                                                                              | vt.net.domain.root == "example.com"                                                                    |
| vt.net.domain.new\_domain                                   | bool             | Domain is first seen in Google TI, not necessarily still exists.                                                                                                                                        |                                                                                                        |
| vt.net.domain.first\_resolution                             | bool             | Domain resolves to an IP for first time                                                                                                                                                                 |                                                                                                        |
| vt.net.domain.new\_resolution                               | bool             | Domain resolves to a different IP                                                                                                                                                                       |                                                                                                        |
| vt.net.domain.whois                                         | dict             | Whois record in key, value format.                                                                                                                                                                      | vt.net.domain.whois\["Admin Country"] == "ES"                                                          |
| vt.net.domain.whois\_raw                                    | string           | Whole Domain whois as a string for pattern matching.                                                                                                                                                    |                                                                                                        |
| vt.net.domain.first\_whois                                  | bool             | Domain has whois for first time                                                                                                                                                                         |                                                                                                        |
| vt.net.domain.new\_whois                                    | bool             | Domain has an updated whois                                                                                                                                                                             |                                                                                                        |
| vt.net.domain.https\_certificate.thumbprint                 | string           | Hash of the certificate                                                                                                                                                                                 | vt.net.domain.https\_certificate.thumbprint == "5d079c6fad2ac214bbdbfcead1584475c3ff41a1"              |
| vt.net.domain.https\_certificate.subject                    | struct           | [Certificate Subject info](#https-certificate-subject-struct)                                                                                                                                           |                                                                                                        |
| vt.net.domain.https\_certificate.validity.not\_after        | int              | Timestamp after which the certificate is no longer valid, in seconds since the Unix epoch                                                                                                               | vt.net.domain.https\_certificate.validity.not\_after < 1672531200  // 2023-01-01                       |
| vt.net.domain.https\_certificate.validity.not\_before       | int              | Timestamp at which the certificate becomes valid, in seconds since the Unix epoch                                                                                                                       | vt.net.domain.https\_certificate.validity.not\_before < 946684800  // 2000-01-01                       |
| vt.net.domain.https\_certificate.subject\_alternative\_name | array of strings | Additional certified hostnames                                                                                                                                                                          | for any name in vt.net.domain.https\_certificate.subject\_alternative\_name: name matches /virustotal/ |
| vt.net.domain.https\_certificate.signature                  | string           | Certificate signature                                                                                                                                                                                   | vt.net.domain.https\_certificate.signature matches /757abd2f/                                          |
| vt.net.domain.https\_certificate.serial\_number             | string           | Unique identifier of the certificate, generated by the issuer                                                                                                                                           | vt.net.domain.https\_certificate.serial\_number = "0bd240b87061dc31bda675382053bef9"                   |
| vt.net.domain.https\_certificate.issuer                     | struct           | [Certificate Subject info](#https-certificate-subject-struct)                                                                                                                                           |                                                                                                        |
| vt.net.domain.jarm                                          | string           | TLS fingerprint                                                                                                                                                                                         | vt.net.domain.jarm = "29d3fd00029d29d21c42d43d00041d188e8965256b2536432a9bd447ae607f"                  |
| vt.net.domain.dns\_records\[].value                         | string           | DNS record resolution.                                                                                                                                                                                  | for any record in vt.net.domain.dns\_records: (record.value contains "sslserver")                      |
| vt.net.domain.dns\_records\[].type                          | string           | Record type                                                                                                                                                                                             | for any record in vt.net.domain.dns\_records: (record.type == "SOA")                                   |
| vt.net.domain.dns\_records\[].dns\_class                    | string           | Class (IN, CH or HS)                                                                                                                                                                                    | for any record in vt.net.domain.dns\_records: (record.dns\_class == "CH")                              |
| vt.net.domain.dns\_records\[].ttl                           | int              | TTL (in seconds)                                                                                                                                                                                        | for any record in vt.net.domain.dns\_records: (record.ttl < 2)                                         |
| vt.net.domain.dns\_records\[].mname                         | string           | Primary name server                                                                                                                                                                                     | for any record in vt.net.domain.dns\_records: (record.mname matches /nameserver/)                      |
| vt.net.domain.dns\_records\[].rname                         | string           | E-mail address of the administrator                                                                                                                                                                     | for any record in vt.net.domain.dns\_records: (record.rname matches /cloud.\*host/)                    |
| vt.net.domain.dns\_records\[].priority                      | int              | Priority                                                                                                                                                                                                | for any record in vt.net.domain.dns\_records: (record.priority = 1)                                    |
| vt.net.domain.dns\_records\[].serial                        | int              | Serial number                                                                                                                                                                                           | for any record in vt.net.domain.dns\_records: (record.serial matches /^9999/)                          |
| vt.net.domain.dns\_records\[].retry                         | int              | Number of seconds after which secondary name servers should retry to request the serial number from the master if the master does not respond                                                           | for any record in vt.net.domain.dns\_records: (record.retry < 100)                                     |
| vt.net.domain.dns\_records\[].refresh                       | int              | Seconds after which secondary name servers should query the master for the SOA record, to detect zone changes                                                                                           | for any record in vt.net.domain.dns\_records: (record.refresh < 5000)                                  |
| vt.net.domain.dns\_records\[].expire                        | int              | Seconds after which secondary name servers should stop answering request for this zone if the master does not respond                                                                                   | for any record in vt.net.domain.dns\_records: (record.expire < 500000)                                 |
| vt.net.domain.dns\_records\[].minimum                       | int              | In seconds. Used in calculating the TTL for purposes of negative caching                                                                                                                                | for any record in vt.net.domain.dns\_records: (record.minimum == 3000)                                 |
| vt.net.domain.favicon.raw\_md5                              | string           | MD5 hash of the URL's favicon. To find a property raw md5 search Google TI for its URL and check details. [Retrieving raw\_md5](#how-do-i-obtain-a-domain-favicon-hashes).                              | vt.net.domain.favicon.raw\_md5 == "6cf6865d5e5cb8f65fe9c0ff93a7904d"                                   |
| vt.net.domain.favicon.dhash                                 | string           | The URL's favicon dhash. To find a property dhash search Google TI for its URL and check details [Retrieving dhash](#how-do-i-obtain-a-domain-favicon-hashes).                                          | vt.net.domain.favicon.dhash == "924dccd4d46933cc"                                                      |
| vt.net.domain.tags                                          | array of strings |                                                                                                                                                                                                         | for any tag in vt.net.domain.tags: name == "dga"                                                       |
| vt.net.domain.analysis\_stats                               | struct           | [Analysis Stats Struct info](#analysis-stats-struct)                                                                                                                                                    |                                                                                                        |
| vt.net.domain.categories                                    | dict             | Content categories by engine                                                                                                                                                                            | for any engine, value in vt.net.domain.categories: (value == "malware command and control")            |
| vt.net.domain.popularity\_ranks\[].position                 | int              | Position of the domain in a specific popularity rank. Low numbers (closer to 1) indicate that the domain is more popular.                                                                               | for any r in vt.net.domain.popularity\_ranks: (r.position < 10)                                        |
| vt.net.domain.popularity\_ranks\[].ingestion\_time          | int              | UNIX UTC timestamp at which the position in the rank was ingested.                                                                                                                                      | for any r in vt.net.domain.popularity\_ranks: (r.ingestion\_time > 1672531200) // 2023-01-01           |
| vt.net.domain.popularity\_ranks\[].rank                     | string           | Name of the popularity rank.                                                                                                                                                                            | for any r in vt.net.domain.popularity\_ranks: (r.rank == "Example")                                    |
| vt.net.domain.number\_of\_popularity\_ranks                 | int              | Number of popularity ranks entries for the domain.                                                                                                                                                      | vt.net.domain.number\_of\_popularity\_ranks == 5                                                       |
| vt.net.domain.root\_popularity\_ranks\[].position           | int              | Position of the root domain in a specific popularity rank. Low numbers (closer to 1) indicate that the domain is more popular.                                                                          | for any r in vt.net.domain.root\_popularity\_ranks: (r.position < 10)                                  |
| vt.net.domain.root\_popularity\_ranks\[].ingestion\_time    | int              | UNIX UTC timestamp at which the position in the rank was ingested.                                                                                                                                      | for any r in vt.net.domain.root\_popularity\_ranks: (r.ingestion\_time > 1672531200) // 2023-01-01     |
| vt.net.domain.root\_popularity\_ranks\[].rank               | string           | Name of the popularity rank.                                                                                                                                                                            | for any r in vt.net.domain.root\_popularity\_ranks: (r.rank == "Example")                              |
| vt.net.domain.number\_of\_root\_popularity\_ranks           | int              | Number of popularity ranks entries for the root domain.                                                                                                                                                 | vt.net.domain.number\_of\_root\_popularity\_ranks == 5                                                 |
| vt.net.domain.signatures                                    | dict             | Dictionary where keys are antivirus names and values are malware signatures (in lowercase).                                                                                                             | vt.net.domain.signatures\["Avira"] == "phishing"                                                       |
| vt.net.url.downloaded\_file                                 | struct           | Metadata from the latest file downloaded from the domain.                                                                                                                                               |                                                                                                        |
| vt.net.domain.downloaded\_file.new\_for\_vt                 | bool             | Seen for the first time being downloaded in Google TI.                                                                                                                                                  |                                                                                                        |
| vt.net.domain.downloaded\_file.new\_for\_domain             | bool             | Seen for the first time being downloaded from this domain. Notice that it may already be known in Google TI.                                                                                            |                                                                                                        |
| vt.net.domain.downloaded\_file.sha256                       | string           | Latest downloaded file SHA256.                                                                                                                                                                          |                                                                                                        |
| vt.net.domain.downloaded\_file.file\_type                   | int              | Latest downloaded file's type (one of the types listed in the file types table).                                                                                                                        |                                                                                                        |
| vt.net.domain.downloaded\_file.analysis\_stats              | struct           | [Analysis Stats Struct info](#analysis-stats-struct)                                                                                                                                                    |                                                                                                        |
| vt.net.domain.downloaded\_file.signatures                   | dict             | Dictionary where keys are antivirus names and values are malware signatures (in lowercase).                                                                                                             |                                                                                                        |
| vt.net.domain.communicating\_file                           | struct           | Metadata from the latest file that has made communications (behaviour) with this domain.                                                                                                                |                                                                                                        |
| vt.net.domain.communicating\_file.new\_for\_domain          | bool             |                                                                                                                                                                                                         |                                                                                                        |
| vt.net.domain.communicating\_file.new\_for\_vt              | bool             |                                                                                                                                                                                                         |                                                                                                        |
| vt.net.domain.communicating\_file.sha256                    | string           | Latest file sha256 that made communications with this domain.                                                                                                                                           |                                                                                                        |
| vt.net.domain.communicating\_file.file\_type                | int              | Latest file's type (one of the types listed in the file types table) that made communications with this domain.                                                                                         |                                                                                                        |
| vt.net.domain.communicating\_file.analysis\_stats           | struct           | [Analysis Stats Struct info](#analysis-stats-struct)                                                                                                                                                    |                                                                                                        |
| vt.net.domain.communicating\_file.signatures                | dict             | Dictionary where keys are antivirus names and values are malware signatures (in lowercase).                                                                                                             |                                                                                                        |
| vt.net.domain.gti\_assessment.severity.value                | string           | Severity of the domain provided by Google Threat Intelligence. One of the values defined on the [Google TI assessment severity types](hunting-reference.md#google-ti-assessment-severity-types) table. | vt.net.domain.gti\_assessment.severity.value == vt.GtiSeverity.SEVERITY\_MEDIUM                        |
| vt.net.domain.gti\_assessment.threat\_score.value           | int              | Threat score of the domain provided by Google Threat Intelligence. This is a value between 1 and 100.                                                                                                   | vt.net.domain.gti\_assessment.threat\_score.value > 20                                                 |
| vt.net.domain.gti\_assessment.verdict.value                 | string           | Verdict of the domain provided by [Google Threat Intelligence](hunting-reference.md#google-ti-assessment-verdicts). One of the values defined on the Google TI assessment verdicts table.              | vt.net.domain.gti\_assessment.verdict.value == vt.GtiVerdict.VERDICT\_MALICIOUS                        |

## file-itw-field

| Field                   | Type   | Description                                                                                                                                                                                                        | Example |
| ----------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| vt.metadata.itw         | struct | Latest ITW relation observed for the file. When Google TI opens a URL that downloads a file this struct will be filled with the information of the corresponding URL/Domain/IP and it will notify you accordingly. |         |
| vt.metadata.itw\.url    | struct | Refers to [URL information](#url-metadata) for the latest itw relation                                                                                                                                             |         |
| vt.metadata.itw\.domain | struct | Refers to [Domain information](#domain-metadata) for the latest itw relation                                                                                                                                       |         |
| vt.metadata.itw\.ip     | struct | Refers to [IP information](#ip-metadata) for the latest itw relation                                                                                                                                               |         |

## analysis-stats-struct

| Field                              | Type | Description                                                   | Example                                           |
| ---------------------------------- | ---- | ------------------------------------------------------------- | ------------------------------------------------- |
| analysis\_stats.malicious          | int  | Amount of engine returning malicious in the analysis.         | vt.net.domain.analysis\_stats.malicious > 5       |
| analysis\_stats.suspicious         | int  | Amount of engine returning suspicious in the analysis.        | vt.net.url.analysis\_stats.suspicious > 10        |
| analysis\_stats.undetected         | int  | Amount of engine returning undetected in the analysis.        | vt.net.ip.analysis\_stats.undetected > 20         |
| analysis\_stats.harmless           | int  | Amount of engine returning harmless in the analysis.          | vt.metadata.analysis\_stats.harmless > 25         |
| analysis\_stats.timeout            | int  | Amount of engine returning timeout in the analysis.           | vt.net.domain.analysis\_stats.timeout > 1         |
| analysis\_stats.confirmed\_timeout | int  | Amount of engine returning confirmed timeout in the analysis. | vt.net.url.analysis\_stats.confirmed\_timeout > 1 |
| analysis\_stats.failure            | int  | Amount of engine that failed during the analysis process.     | vt.net.ip.analysis\_stats.failure > 1             |
| analysis\_stats.type\_unsupported  | int  | Amount of engine that do not support the file/IoC type.       | vt.metadata.analysis\_stats.type\_unsupported > 1 |

## https-certificate-subject-struct

| Field                                           | Type   | Description                                                                                          | Example                                                                                |
| ----------------------------------------------- | ------ | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| https\_certificate.subject.common\_name         | string | Common name, also known as the Fully Qualified Domain Name (FQDN), of the subject that is certified. | vt.net.ip.https\_certificate.subject.common\_name matches /virustotal/                 |
| https\_certificate.subject.country              | string | Two-letter country code that identifies the country of the subject that is certified.                | vt.net.domain.https\_certificate.subject.country == "US"                               |
| https\_certificate.subject.organization         | string | The organization to which the certificate has been issued.                                           | vt.net.ip.https\_certificate.subject.organization matches /VirusTotal/                 |
| https\_certificate.subject.organizational\_unit | string | Additional information about the certified organization.                                             | vt.net.domain.https\_certificate.subject.organizational\_unit matches /Domain Control/ |
| https\_certificate.subject.locality             | string | The city where the certified organization is located.                                                | vt.net.ip.https\_certificate.subject.locality == "Madrid"                              |
| https\_certificate.subject.state                | string | The state where the certified organization is located.                                               | vt.net.domain.https\_certificate.subject.state == "Washington"                         |

## network-range

In order to match complex IP range you can use the `in_range` method associated to IP addresses. These are some examples:

```yara
import "vt"
rule ip_in_range {
  condition:
    vt.net.ip.in_range("142.250.184.164/20")
}
rule ip_in_range {
  condition:
    vt.metadata.itw.ip.in_range("192.168.1.0/24")
}
```

This method also works with IPv6 addresses:

```yara
import "vt"
rule ip_in_range {
  condition:
    vt.net.ip.in_range("2001:db8::1/32")
}
rule ip_in_range {
  condition:
    vt.metadata.itw.ip.in_range("2001:db8::1/32")
}
```

## typosquatting

The `vt` module provides a `permutation_of` method to detect malicious domains attempting to impersonate legitimate ones using typosquatting techniques. This feature helps identify domains designed to deceive users by mimicking trusted domain names.

### basic-usage

To detect typosquatted domains, use the permutation\_of method as shown in the example below:

```yara
import "vt"
rule fake_virustotal {
  condition:
    vt.net.domain.permutation_of("www.virustotal.com")
}
```

In this example, any scanned domain that attempts to pass as `www.virustotal.com` using common typosquatting techniques will be detected. The `vt.net.domain.permutation_of` method returns true if the examined domain is a permutation of the specified domain.

### detected-typosquatting-techniques

The `permutation_of` method detects various types of domain permutations, including:

#### 1.-typo-squatting

* Character omission: `www.vrustotal.com`

* Character repetition: `www.viirustotal.com`

* Character replacement (keyboard proximity): `www.viorustotal.com`, `www.vurustotal.com`

* Character swapping: `www.virustoatl.com`

#### 2.-homoglyph-attacks

Replaces characters with visually similar ones:

* `www.vırustotal.com` ("i" was replaced with "ı")
* `ⱳⱳⱳ.virustotal.com` ("w" were replaced with "ⱳ" )
* `www.viruṡtotal.com` ("s" was replaced with "ṡ")

#### 3.-hyphenation

Inserts hyphens between domain name characters:

* `www.virus-total.com`

#### 4.-subdomain

Inserts additional dots (.) in the domain name:

* `w.ww.virustotal.com`
* `www.vi.rustotal.com`

#### 5.-bitsquatting

Bitsquatting is a type of cybersquatting attack where attackers register domain names that are one bit-flip
away from a legitimate domain name. This exploits memory errors, transmission errors, or hardware faults that
can cause a single bit in a domain name to change, leading users to the attacker's domain instead of the
intended one.

For more information, refer to:

* [Why bitsquatting attacks are here to stay](https://sec.okta.com/articles/2020/11/why-bitsquatting-attacks-are-here-stay/)
* [Understanding bitsquatting attacks](https://www.the-parallax.com/bitsquatting-cyberattack/)

### fine-tunning-your-detection

By default, `permutation_of` detects all types of typosquatting attacks. However, you can customize detection by specifying specific techniques using flags. For example:

```yara
import "vt"
rule fake_virustotal {
  condition:
    vt.net.domain.permutation_of("www.virustotal.com", vt.Net.Domain.Permutation.TYPO)
}
```

Or to combine multiple techniques:

```yara
import "vt"
rule fake_virustotal {
  condition:
    vt.net.domain.permutation_of("www.virustotal.com", vt.Domain.Permutation.TYPO | vt.Domain.Permutation.HOMOGLYPH)
}
```

The following flags can be used to refine detection and can be combined using the bitwise OR (|) operator:

* `vt.Domain.Permutation.TYPO`
* `vt.Domain.Permutation.HOMOGLYPH`
* `vt.Domain.Permutation.HYPHENATION`
* `vt.Domain.Permutation.SUBDOMAIN`
* `vt.Domain.Permutation.BITSQUATTING`

Using these options, you can precisely target the types of typosquatting threats relevant to your security needs.

## filetypes-automatically-analysed

There is only some filetypes that are automatically submitted for a file analysis after URL is received:

<div id="types" style={{ maxWidth: 'none' }}>

|               |                   |                   |                   |      |      |
|:-------------:|:-----------------:|:-----------------:|:-----------------:|:----:|:----:|
|     GZIP      |   .Z compressed   |        PDF        |   Certificates    | 7ZIP | BZIP |
|    ISO9660    | Chrome extensions |        DMG        | Microsoft Cabinet | EXE  | ZIP  |
|      RAR      |      WinZip       | Android dex files | Apple Disk Image  | ELF  | DMG  |
| Java bytecode |       Macho       |       DOCs        |                   |      |      |

</div>

These filetypes applies to `vt.net.url.downloaded_file.` attributes, in case you want to scan other filetypes you should write a content rule ("strings") and once the match is done the hash will be visible in Google TI and you will have the possibility to submit it for a file analysis.

## faq

### how-do-i-match-certain-content-or-sized-response:

In Nethunt the content of the response is treated as a file (HTTP headers, etc are not included), you can use that content/file to make matches like in traditional matching yaras. Some examples:

* Matching some strings:

```yara
import "vt"

rule html_content {
meta:
  description = "URLs matching certain strings in content"
  author = "google_ti"
  target_entity = "url"
strings:
  $mystring: "some&html"
condition:
  $mystring and $mystring at 400
}
```

* Matching empty response:

```yara
import "vt"

rule empty_content {
meta:
  description = "URLs matching empty content"
  author = "google_ti"
  target_entity = "url"
condition:
  filesize == 0
}
```

### how-do-i-match-urls-in-certain-asn-number/ip-range,-etc:

You are able to mix different net modules in a single rule and match over a single net type, for example:

* Notify new URLs whos domain resolve its IP address of a certain ASN in a certain IP range

```yara
import "vt"

rule urls_in_asn {
meta:
  description = "New URLs whos domain resolve to certain ASN"
  author = "google_ti"
  target_entity = "url"
condition:
  vt.net.url.new_url and
  vt.net.ip.ip_asn == 74838
}
```

* Notify new URLs whos domain resolve in a certain IP range ([IP range helper](#network-range-helper)):

```yara
import "vt"

rule urls_in_iprange {
meta:
  description = "New URLs whos domain resolve to my IP range"
  author = "google_ti"
  target_entity = "url"
condition:
  vt.net.url.new_url and
  vt.net.ip.ip_as_int >= 3941835776 and vt.net.ip.ip_as_int < 3941836800 // 234.243.166.33/22
}
```

### how-do-i-obtain-a-domain-favicon-hashes:

You need to search for the domain URL in Google TI, go to <<https://www.virustotal.com/gui/search>>, and write your domain url, ie: <<http://google.com>> , then go to details tab and at the end you will find a "Favicon" header, there you can see both dhash and raw mad5 hashes.

```yara
import "vt"

rule urls_with_dhash {
meta:
  description = "Domains with similar favicons"
  author = "google_ti"
  target_entity = "domain"
condition:
  vt.net.url.favicon.dhash == "f0cc929ab296cc71" or
  vt.net.url.favicon.raw_md5 == "30e26a059b7b858731e172c431d55bb4"
}
```

### how-do-i-obtain-domains-with-self-signed-certificates:

You can use the "self-signed" tag for that, to be notified you could use for example:

```yara
import "vt"

rule selfsigned_certificate_domains {
meta:
  description = "Domains with self signed certificates"
  author = "google_ti"
  target_entity = "domain"
condition:
  for any tag in vt.net.domain.tags: (
    tag == "self-signed"
  )
}
```

### how-do-i-obtain-a-feed-of-ip-resolutions-for-a-certain-domain:

It's currently not possible to combine domain matching attributes in IP rules, to overcome this limitation exists the `vt.net.ip.reverse_lookup` attribute, it can be used like this:

```yara
import "vt"

rule ip_resolutions_for_domain {
meta:
  description = "IP resolutions for a certain domain"
  author = "google_ti"
  target_entity = "ip_address"
condition:
  vt.net.ip.reverse_lookup == "somedomain.com"
}
```

---

← [File hunting](hunting-metadata.md) · [up](../README.md) · [Behavior hunting](hunting-behavior.md) →

*Archived from <https://gtidocs.virustotal.com/docs/nethunt>.*
