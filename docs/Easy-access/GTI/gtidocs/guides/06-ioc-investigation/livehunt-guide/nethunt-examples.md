---
title: "Network hunting examples"
source: https://gtidocs.virustotal.com/docs/nethunt-examples
slug: nethunt-examples
section: guides
group: "IOC Investigation"
updatedAt: 2025-09-25T02:41:06.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [IOC Investigation](../README.md) › [Livehunt](../livehunt-guide.md) › Network hunting examples

---

# network-hunting-examples

## uncover-new-artifacts-and-infrastructure-related-to-a-known-campaign

#### new-files-downloaded-from-urls-with-a-pattern

Matches: FILE

```cplusplus
import "vt"

rule NewFileDownloadedFromUrlMatchingExpression {
meta:
  description = "New Files downloaded from URLs with a pattern"
  author = "google_ti"
  target_entity = "file"
condition:
  vt.metadata.new_file and
  vt.metadata.itw.url.raw matches /example[.]com\/foo\/.*/
}
```

⚠️ Finetuned alternatives to regexps matching:

* `vt.metadata.itw.url.raw icontains "example.com/foo"`
* `vt.metadata.itw.domain.root == "example.com" and vt.metadata.itw.url.path istartswith "/foo"` (for every domain or subdomain of example.com including itself)
* `vt.metadata.itw.domain.raw iendswith ".example.com" and vt.metadata.itw.url.path istartswith "/foo"` (for only example.com subdomains)

#### new-pe-files-downloaded-from-urls-with-a-pattern

Matches: FILE

```cplusplus
import "vt"

rule NewExesDownloadedFromSomeURLPattern {
meta:
  description = "New PE files downloaded from URLs with a pattern"
  author = "google_ti"
  target_entity = "file"
condition:
  vt.metadata.new_file and
  vt.metadata.itw.url.raw matches /example.com\/foo\/.*/ and
  vt.metadata.file_type == vt.FileType.PE_EXE
}
```

#### urls-matching-a-pattern-that-downloads-a-pe-file-for-first-time

Matches: URL

```cplusplus
import "vt"

rule UrlsMatchingExpressionDownloadingNewFiles {
meta:
  description = "URLs matching a pattern that downloads a PE file for first time"
  author = "google_ti"
  target_entity = "url"
condition:
  vt.net.url.downloaded_file.new_for_url and
  vt.net.url.raw matches /example[.]com\/foo\/.*/ and
  vt.net.url.downloaded_file.file_type == vt.FileType.PE_EXE
}
```

⚠️ Notice that `vt.net.url.downloaded_file.new_for_url` matches once the file haven't been previously downloaded from that particular URL, it may already be  known in Google Threat Intelligence.

#### new-urls-serving-certain-hash

Matches: URL

```cplusplus
import "vt"

rule NewURLsServingThisFile {
meta:
  description = "New URLs serving certain hash"
  author = "google_ti"
  target_entity = "url"
condition:
  vt.net.url.new_url and
  vt.net.url.downloaded_file.sha256 == "<sha256>"
}
```

#### new-url-with-a-pattern-serving-a-new-file

Matches: URL

```cplusplus
import "vt"

rule NewURLsServingANewFile {
meta:
  description = "New URL with a pattern serving a new file"
  author = "google_ti"
  target_entity = "url"
condition:
  vt.net.url.new_url and
  vt.net.url.downloaded_file.new_for_vt and  // For VT
  vt.net.url.raw icontains "example.com/foo/"
}
```

#### urls-matching-a-string-in-its-content-and-served-for-first-time

Matches: URL

⚠️ The content will be new for that particular URL, alternatively you can use `vt.net.url.downloaded_file.new_for_vt` to check if it's first time seen in the whole Google TI collection.

```cplusplus
import "vt"

rule URLsMatchingContent {
meta:
  description = "URLs matching a string in its content and served for first time"
  author = "google_ti"
  target_entity = "url"
strings:
  $cmdlet_str = "CmdletBinding" nocase
condition:
  vt.net.url.downloaded_file.new_for_url and
  $cmdlet_str
}
```

#### new-urls-matching-certain-strings-in-its-content

Matches: URL

```cplusplus
import "vt"

rule NewURLsServingFileContentMatchingConditions {
meta:
  description = "New URLs matching certain strings in its content"
  author = "google_ti"
  target_entity = "url"
strings:
  $foo = "foo"
  $bar = "bar"
condition:
  vt.net.url.new_url and
  all of them
}
```

#### new-domains-having-communicating-files-detected

Matches: DOMAIN

⚠️ `vt.net.domain.communicating_file.*` refers to a File behavioural analysis that reported this Domain (or URL domain) as part of its indicators.

```cplusplus
import "vt"

rule NewCommunicatingDomainForDetectedFiles {
meta:
  description = "New Domains having communicating files detected"
  author = "google_ti"
  target_entity = "domain"
condition:
  vt.net.domain.new_domain and
  // communicating_file.* refers to a File behavioural analysis that reported this Domain (or URL domain).
  vt.net.domain.communicating_file.analysis_stats.malicious > 2
}
```

#### new-domains-having-a-specific-communicating-file

Matches: DOMAIN

⚠️ `vt.net.domain.communicating_file.*` refers to a File behavioural analysis that reported this Domain (or URL domain) as part of its indicators.

```cplusplus
import "vt"

rule NewCommunicatingDomainForSpecificFile {
meta:
  description = "New Domains having a specific communicating file"
  author = "google_ti"
  target_entity = "domain"
condition:
  vt.net.domain.new_domain and
  // communicating_file.* refers to a File behavioural analysis that reported this Domain (or URL domain).
  vt.net.domain.communicating_file.sha256 == "<sha256>"
}
```

#### new-domains-reported-for-a-subsequent-file-behaviour-analyses

Matches: DOMAIN

```cplusplus
import "vt"

rule EveryCommunicatingDomainForSpecificFile {
meta:
  description = "New Domains reported for a subsequent File behaviour analyses"
  author = "google_ti"
  target_entity = "domain"
condition:
  vt.net.domain.communicating_file.sha256 == "<sha256>"
}
```

⚠️ Fixing `communicating_file` to a certain hash means that once Google TI receives a new behavioural report over that file you will be notified.

#### new-domains-observed-in-behaviour-analyses-of-files-with-detections

Matches: DOMAIN

```cplusplus
import "vt"

rule CommunicatingDomainForDetectedFiles {
meta:
  description = "New Domains observed in behaviour analyses of files with detections"
  author = "google_ti"
  target_entity = "domain"
condition:
  vt.net.domain.new_domain and
  vt.net.domain.communicating_file.analysis_stats.malicious >= 2
}
```

#### domains-observed-from-detected-samples-behaviours

Matches: DOMAIN

```cplusplus
import "vt"

rule DomainsContactedByADetectedFile {
meta:
  description = "Domains observed from detected samples behaviours"
  author = "google_ti"
  target_entity = "domain"
condition:
  vt.net.domain.communicating_file.analysis_stats.malicious >= 2
}
```

#### ip-addresses-observed-from-detected-samples-behaviours

Matches: IP

```cplusplus
import "vt"

rule IpsContactedByADetectedFile {
meta:
  description = "IP addresses observed from detected samples behaviours"
  author = "google_ti"
  target_entity = "ip_address"
condition:
  vt.net.ip.communicating_file.analysis_stats.malicious >= 2
}
```

#### new-urls-under-a-specific-domain

Matches: URL

```cplusplus
import "vt"

rule newURLsUnderDomain {
meta:
  description = "New URLs under a specific domain"
  author = "google_ti"
  target_entity = "url"
condition:
  vt.net.url.new_url
  and vt.net.domain.raw == "example.com"
}
```

#### new-urls-in-subdomains

Matches: URL

```cplusplus
import "vt"

rule newURLsInSubDomains {
meta:
  description = "New URLs in subdomains"
  author = "google_ti"
  target_entity = "url"
condition:
  vt.net.url.new_url
  and vt.net.domain.raw endswith ".example.com"
}
```

#### root-domain-appearing-in-a-sample-behavior-for-first-time

Matches: DOMAIN

```cplusplus
import "vt"

rule newDomainRelationshipForIOC {
meta:
  description = "Root domain appearing in a sample behavior for first time"
  author = "google_ti"
  target_entity = "domain"
condition:
  vt.net.domain.root == "example.com" and
  vt.net.domain.communicating_file.new_for_domain
}
```

#### ip-addresses-range-appearing-in-a-sample-behavior-for-first-time

Matches: IP

```cplusplus
import "vt"

rule newIPRelationshipForIOC {
meta:
  description = "IP addresses range appearing in a sample behavior for first time"
  author = "google_ti"
  target_entity = "ip_address"
condition:
  vt.net.ip.communicating_file.new_for_ip and
  vt.net.ip.ip_as_int >= 3941835776 and vt.net.ip.ip_as_int < 3941836800 // 234.243.166.33/22
}
```

***

## unearth-malicious-infrastructure-being-used-by-certain-malware-toolkits

#### urls-with-pattern-and-a-set-of-query-params

Matches: URL\
⚠️ URL matching can be fine-tuned, for example: `vt.net.domain.root == "example.com" and vt.net.url.path istartswith "/foo"`

```cplusplus
import "vt"

rule paramsOverURL {
meta:
  description = "URLs with pattern and a set of query params"
  author = "google_ti"
  target_entity = "url"
condition:
  vt.net.url.raw matches /example[.]com/ and
  for any key, value in vt.net.url.params: (
    key == "foo" and
    value icontains "bar"
  )
}
```

#### url-subdomains-matching-certain-get-params

Matches: URL

```cplusplus
import "vt"

rule paramsOverSubDomain {
meta:
  description = "URL subdomains matching certain GET params"
  author = "google_ti"
  target_entity = "url"
condition:
  vt.net.domain.root == "example.com" and
  // vt.net.domain.raw != "example.com" and  // enable to skip naked domain matches
  for any key, value in vt.net.url.params: (
    key == "foo" and
    value icontains"bar"
  )
}
```

#### new-files-serverd-from-a-domain-matching-certain-jarm

Matches: FILE

```cplusplus
import "vt"

rule NewDownloadedFilesJarmMatching {
meta:
  description = "New Files serverd from a domain matching certain JARM"
  author = "google_ti"
  target_entity = "file"
condition:
  vt.metadata.new_file and
  vt.metadata.itw.domain.jarm == "00112233445566778899AABBCCDDEEFF"
}
```

#### new-domains-with-a-specific-jarm

Matches: DOMAIN

```cplusplus
import "vt"

rule NewDomainJarmMatching {
meta:
  description = "New domains with a specific JARM"
  author = "google_ti"
  target_entity = "domain"
condition:
  vt.net.domain.new_domain and
  vt.net.domain.jarm == "00112233445566778899AABBCCDDEEFF"
}
```

#### ip-addresses-with-ssl/tls-serving-with-a-specific-jarm

Matches: IP

```cplusplus
import "vt"

rule IPJarmMatching {
meta:
  description = "IP addresses with SSL/TLS serving with a specific JARM"
  author = "google_ti"
  target_entity = "ip_address"
condition:
  vt.net.ip.jarm == "00112233445566778899AABBCCDDEEFF"
}
```

#### new-urls-with-certain-ssl-certificate-subject

Matches: URL

```cplusplus
import "vt"

rule sslCertificateAttributeMatching {
meta:
  description = "New URLs with certain SSL certificate subject"
  author = "google_ti"
  target_entity = "url"
condition:
  vt.net.url.new_url and
  vt.net.domain.https_certificate.subject.common_name == "*.example.com"
}
```

#### urls-with-a-certain-set-and-amount-of-http-headers

Matches: URL

```cplusplus
import "vt"

rule missingAndContainedHTTPHeaders {
meta:
  description = "URLs with a certain set and amount of HTTP headers"
  author = "google_ti"
  target_entity = "url"
condition:
  vt.net.url.number_of_response_headers == 4 and
  for all name, value in vt.net.url.response_headers : (
    name != "Content-Encoding"
  ) and
  for any name, value in vt.net.url.response_headers : (
    name == "Foo" and value == "Bar"
  )
}
```

#### urls-with-a-certain-cookie-name

Matches: URL

```cplusplus
import "vt"

rule cookieWithName {
meta:
  description = "URLs with a certain cookie name"
  author = "google_ti"
  target_entity = "url"
condition:
  for any name, value in vt.net.url.cookies : (
    name == "SuspiciousCookie"
  )
}
```

#### new-urls-serving-content-strings-and-urlscanner-detections

Matches: URL

```cplusplus
import "vt"

rule MatchHTTPResponseContentAndAnalysis {
meta:
  description = "New URLs serving content strings and URLscanner detections"
  author = "google_ti"
  target_entity = "url"
strings:
  $html = "<HTML "
  $bar = "bar"
condition:
  vt.net.url.new_url
  and vt.net.url.analysis_stats.malicious > 1
  and $html at 0 and $bar
}
```

#### new-urls-with-urlscanner-detections-matching-potentially-malicious-html/js-strings

Matches: URL

```cplusplus
import "vt"

rule MatchEmbeddedJavascriptContent {
meta:
  description = "New URLs with URLscanner detections matching potentially malicious HTML/JS strings"
  author = "google_ti"
  target_entity = "url"
strings:
  $html = "<HTML " nocase
  $js_script = "script" nocase
  $js_unescape = "unescape" nocase
  $js_parseint = "parseint" nocase
  $js_fromcharcode = "fromcharcode" nocase
condition:
  vt.net.url.new_url and
  vt.net.url.analysis_stats.malicious > 1 and
  $html at 0 and $js_script and
  ($js_unescape or $js_parseint or $js_fromcharcode)
}
```

#### urls-serving-strings-seen-in-google-ti-for-first-time

Matches: URL

```cplusplus
import "vt"

rule MatchHTTPResponseContentFirstSeen {
meta:
  description = "URLs serving strings seen in Google TI for first time"
  author = "google_ti"
  target_entity = "url"
strings:
  $securestring_str = "ConvertFrom-SecureString" nocase
condition:
  vt.net.url.downloaded_file.new_for_vt and
  $securestring_str
}
```

#### urls-serving-potential-powershell-content

Matches: URL

⚠️ Useful for filetypes that are not automatically submmited to Google TI ([list](nethunt.md#filetypes-automatically-analysed)).

```cplusplus
import "vt"

rule MatchPowerShellContent {
meta:
  description = "URLs serving potential PowerShell content"
  author = "google_ti"
  target_entity = "url"
strings:
  $mz_header = { 4d 5a 90 }
  $cmdlet_str = "CmdletBinding" nocase
  $securestring_str = "ConvertFrom-SecureString" nocase

condition:
  not ($mz_header at 0) and
  ($cmdlet_str or $securestring_str)
}
```

#### urls-serving-new-potential-powershell-content

Matches: URL

⚠️ Useful for filetypes that are not automatically submmited to Google TI ([list](nethunt.md#filetypes-automatically-analysed)).

```cplusplus
import "vt"

rule MatchNewServedPowerShellContent {
meta:
  description = "URLs serving new potential PowerShell content"
  author = "google_ti"
  target_entity = "url"
strings:
  $mz_header = { 4d 5a 90 }
  $cmdlet_str = "CmdletBinding" nocase
  $securestring_str = "ConvertFrom-SecureString" nocase

condition:
  vt.net.url.downloaded_file.new_for_url and
  not ($mz_header at 0) and
  ($cmdlet_str or $securestring_str)
}
```

#### domains-with-certain-dns-records

Matches: DOMAIN

```cplusplus
import "vt"

rule dnsRecord {
meta:
  description = "Domains with certain DNS records"
  author = "google_ti"
  target_entity = "domain"
condition:
  for any record in vt.net.domain.dns_records : (
    record.type == "TXT" and
    record.value istartswith "v=spf1 include:"
  )
}
```

***

## track-specific-threat-actors-and-their-newly-created-infrastructure

#### urls-with-a-certain-set-of-html-meta-tags

Matches: URL

```cplusplus
import "vt"

rule htmlMetaTags {
meta:
  description = "URLs with a certain set of HTML meta tags"
  author = "google_ti"
  target_entity = "url"
condition:
  for any entry in vt.net.url.html_meta_tags : (
    entry.key == "generator" and
    for any value in entry.values : (
      value startswith "Foo"
    ) and
    for any value in entry.values : (
      value startswith "Bar"
    )
  )
}
```

#### urls-with-a-combination-of-tracker-and-tracker-id

Matches: URL

```cplusplus
import "vt"

rule newURLsUsingSpecificTracker {
meta:
  description = "URLs with a combination of tracker and tracker id"
  author = "google_ti"
  target_entity = "url"
condition:
  for any tracker in vt.net.url.trackers : (
    tracker.name == "Google Analytics" and
    tracker.id == "Foo"
  )
}
```

#### domains-matching-whois-key/values

Matches: DOMAIN

⚠️ This will notify new and updated Whois records.

```cplusplus
import "vt"

rule WhoisProperties {
meta:
  description = "Domains matching Whois key/values"
  author = "google_ti"
  target_entity = "domain"
condition:
  for any key, value in vt.net.domain.whois : (
    key == "Foo" and
    value == "Bar"
  )
}
```

#### domains-serving-https-with-certain-a-certificate-thumbprint

Matches: DOMAIN

⚠️ To match other HTTPS certificate fields check [cert struct](nethunt.md#https-certificate-subject-struct).

```cplusplus
import "vt"

rule httpsCertificate {
  meta:
  description = "Domains serving HTTPS with certain a certificate thumbprint"
  author = "google_ti"
  target_entity = "domain"
vt.net.domain.https_certificate.thumbprint == "AABBCCDD"
}
```

***

## identify-supply-chain-risk,-mainly-phishing,-against-my-identity-provider-or-specific-companies

#### urls-containing-certain-html-title-and-serving-a-favicon-dhash

Matches: URL

⚠️ To obtain a dhash check: [obtaining a domain favicon dhash](nethunt.md#how-do-i-obtain-a-domain-favicon-hashes).

```cplusplus
import "vt"

rule URLsWithMyFavIcon {
meta:
  description = "URLs containing certain HTML title and serving a favicon dhash"
  author = "google_ti"
  target_entity = "url"
condition:
  (vt.net.url.html_title contains "Example Bank" or
   vt.net.url.favicon.dhash == "5a923260c3c8708f") and

  not vt.net.url.raw istartswith "https://www.example-bank.com/"
}
```

#### urls-matching-string-in-its-url-excluding-the-canonical-url

Matches: URL

```cplusplus
import "vt"

rule URLHostingPhishing {
meta:
  description = "URLs matching string in its URL excluding the canonical URL"
  author = "google_ti"
  target_entity = "url"
condition:
  vt.net.url.raw contains "example-bank" and
  vt.net.domain.root != "example-bank.com"
}
```

⚠️ Notice how `vt.net.domain.root` condition excludes the root domain and all its possible subdomains.

***

## attack-surface/infrastructure-management

#### files-with-positives-downloaded-from-a-certain-ip-range

Matches: FILE

⚠️ To convert an IP range to Integer match you can check: [generating IP integer range](nethunt.md#how-do-i-match-urls-in-certain-asn-numberip-range-etc).

```cplusplus
import "vt"

rule maliciousFilesFromMyIPRange {
meta:
  description = "Files with positives downloaded from a certain IP range"
  author = "google_ti"
  target_entity = "file"
condition:
  vt.metadata.analysis_stats.malicious > 1 and
  vt.metadata.itw.ip.ip_as_int >= 3941835776 and vt.metadata.itw.ip.ip_as_int < 3941836800 // 234.243.166.33/22
}
```

#### files-with-positives-downloaded-from-a-certain-urls

Matches: FILE

```cplusplus
import "vt"

rule maliciousFilesFromMyURLs {
meta:
  description = "Files with positives downloaded from a certain URLs"
  author = "google_ti"
  target_entity = "file"
condition:
  vt.metadata.analysis_stats.malicious > 1 and
  vt.metadata.itw.url.raw matches /mydomain[.]com/
}
```

#### ip-addresses-marked-as-malicious-in-an-ip-range

Matches: IP

⚠️ To convert an IP range to Integer match you can check: [generating IP integer range](nethunt.md#how-do-i-match-urls-in-certain-asn-numberip-range-etc).

```cplusplus
import "vt"

rule IPMarkedAsMaliciousFromMyIPRange {
meta:
  description = "IP addresses marked as malicious in an IP range"
  author = "google_ti"
  target_entity = "ip_address"
condition:
  vt.net.ip.analysis_stats.malicious > 1 and
  vt.net.ip.ip_as_int >= 3941835776 and vt.net.ip.ip_as_int < 3941836800 // 234.243.166.33/22
}
```

#### ip-addresses-serving-malicious-files

Matches: IP

Useful to monitor your own infrastructure.

```cplusplus
import "vt"

rule IPServesMaliciousFile {
meta:
  description = "IP addresses serving malicious files"
  author = "google_ti"
  target_entity = "ip_address"
condition:
  vt.net.ip.raw matches /ˆ11\.22\.33\./ and
  vt.net.ip.downloaded_file.analysis_stats.malicious > 2
}
```

#### domain-serving-malicious-files

Matches: DOMAIN

Useful to monitor your own infrastructure.

```cplusplus
import "vt"

rule DomainServesMaliciousFile {
meta:
  description = "Domain serving malicious files"
  author = "google_ti"
  target_entity = "domain"
condition:
  vt.net.domain.raw iendswith "drive.google.com" and
  vt.net.domain.downloaded_file.analysis_stats.malicious > 2
}
```

***

## false-positives-related-to-your-internet-exposed-assets

#### files-with-positives-downloaded-from-a-certain-domain

Matches: DOMAIN

```cplusplus
import "vt"

rule falsePositivesFromMyDomain {
meta:
  description = "Files with positives downloaded from a certain Domain"
  author = "google_ti"
  target_entity = "domain"
condition:
  vt.net.domain.raw == "example.com" and
  vt.net.domain.analysis_stats.malicious > 0
}
```

---

← [Behavior hunting](hunting-behavior.md) · [up](../README.md) · [Reference](hunting-reference.md) →

*Archived from <https://gtidocs.virustotal.com/docs/nethunt-examples>.*
