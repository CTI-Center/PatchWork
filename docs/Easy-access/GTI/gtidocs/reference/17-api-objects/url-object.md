---
title: "URLs"
source: https://gtidocs.virustotal.com/reference/url-object
slug: url-object
section: reference
group: "API OBJECTS"
updatedAt: 2026-08-26T14:46:16.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › URLs

---

# urls

Information about URLs.

A *URL object* represents an individual URL tracked by Google TI, with every attribute aggregated across all the analyses performed for it. Unlike the per-visit [URL Analysis](url-analysis-object.md) object, which captures the state observed during a single browser session, the URL object exposes the *last-seen* aggregate values plus a set of historical fields (`first_submission_date`, `times_submitted`, `first_seen_itw_date`, etc.).

URL objects are retrievable through `GET /urls/{id}`, where the ID is the SHA-256 of the canonical URL (or, equivalently, the URL Base64-encoded with `=` padding stripped, as explained [here](../03-ioc-investigation/urls.md)).

Different URL calls may return different URL-related objects that we list here.

## object-attributes

* `categories`: <*dictionary*> last-seen category assignments per partner. The key is the partner that categorised the URL; the value is that partner's verdict (e.g. `"Forcepoint ThreatSeeker": "uncategorized"`).
* `favicon` : <*dictionary*> favicon fingerprints. Only returned to premium API and Google TI partners.
  * `dhash`: <*string*> difference hash.
  * `raw_md5`: <*string*> favicon's MD5 hash.
* `first_seen_itw_date`: <*integer*> Unix epoch UTC time (seconds) the URL was first seen in the wild. Returned to Google TI customers.
* `last_seen_itw_date`: <*integer*> Unix epoch UTC time (seconds) the URL was last seen in the wild. Returned to Google TI customers.
* `first_submission_date`: <*integer*> Unix epoch UTC time (seconds) the URL was first submitted to Google TI.
* `gti_assessment*`: <*dictionary*> Google Threat Intelligence assessment. To receive this attribute the request must set the `x-tool` header to identify the calling tool or service. It contains the following fields:
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
* `has_content`: <*boolean*> whether we store response body content for the URL. Premium API only.
* `html_meta`: <*dictionary*> contents of every `<meta>` tag captured from the last analysis. Keys are tag names, values are the list of `content` values for that tag.
* `identified_brands`: <*dictionary*> brands identified on the page by visual / OCR / heuristic detectors. Keys are detector names, values are detector-specific payloads. Returned to GTI customers.
* `main_brand`: <*string*> primary identity, entity, or organization that owns and operates the website or is impersonated in phishing.
* `last_analysis_date`: <*integer*> Unix epoch UTC time (seconds) of the last analysis performed for the URL.
* `last_analysis_results`: <*dictionary*> result from URL scanners. dict with scanner name as key and a dict with notes/result from that scanner as value.
  * `category`: <*string*> normalized result. can be:
    * "harmless" (site is not malicious),
    * "undetected" (scanner has no opinion about this site),
    * "suspicious" (scanner thinks the site is suspicious),
    * "malicious" (scanner thinks the site is malicious).
  * `engine_name`: <*string*> complete name of the URL scanning service.
  * `method`: <*string*> type of service given by that URL scanning service (i.e. "blacklist").
  * `result`: <*string*> raw value returned by the URL scanner ("clean", "malicious", "suspicious", "phishing"). It may vary from scanner to scanner, hence the need for the "category" field for normalisation.
* `last_analysis_stats`: <*dictionary*> summary of `last_analysis_results`.
  * `harmless`: <*integer*> number of reports saying that the URL is harmless.
  * `malicious`: <*integer*> number of reports saying that the URL is malicious.
  * `suspicious`: <*integer*> number of reports saying that the URL is suspicious.
  * `timeout`: <*integer*> number of timeouts when checking this URL.
  * `undetected`: <*integer*> number of reports saying that the URL is undetected.
* `last_final_url`: <*string*> URL the most recent visit landed on after following all redirects.
* `last_http_response_code`: <*integer*> HTTP status code of the response served at `last_final_url` during the last visit.
* `last_http_response_content_length`: <*integer*> size in bytes of the body of the last response.
* `last_http_response_content_sha256`: <*string*> last URL response body's SHA256 hash.
* `last_http_response_cookies`: <*dictionary*> cookies set during the last visit, in the `name -> raw-cookie-string` shape.
* `last_http_response_cookies_extended`: <*list of dictionaries*> cookies set during the last visit, with full per-cookie metadata:
  * `value`: <*string*> the data payload stored inside the cookie associated with the name.
  * `expires`: <*integer*> the expiration Unix epoch UTC time (seconds) of the cookie, dictating how long the browser should keep it before deletion. -1 means that the cookie has no explicit expiration date set.
  * `priority`: \<string>a Chrome-specific extension used to define the eviction priority of the cookie if the cookie store reaches its size limit `COOKIE_PRIORITY_LOW`, `COOKIE_PRIORITY_MEDIUM`, or `COOKIE_PRIORITY_HIGH`).
  * `name`: <*string*> the unique identifier for the cookie. It acts as the key in the key-value pair, allowing the server or client-side scripts to look up and retrieve this specific piece of data.
  * `size`: <*integer*> the total size of the cookie in bytes, typically calculated as the length of the name string plus the length of the value string.
  * `secure`: <*boolean*> indicating if the cookie should only be transmitted over secure (HTTPS) connections, protecting it from being intercepted by man-in-the-middle attacks over unencrypted HTTP.
  * `session`: <*boolean*> flag indicating if the cookie is a session cookie. If `true`, the cookie is deleted when the client's session ends (e.g., when the browser is closed), ignoring the `expires` attribute.
  * `http_only`: <*boolean*> when `true`, prevents client-side scripts (like JavaScript's document.cookie) from accessing the cookie.
  * `domain`: <*string*> specifies which hosts are allowed to receive the cookie.
* `last_http_response_headers`: <*dictionary*> headers and values of last HTTP response.
* `last_modification_date`: <*integer*> Unix epoch UTC time (seconds) the URL object was last modified.
* `last_submission_date`: <*integer*> Unix epoch UTC time (seconds) the URL was last submitted for analysis.
* `outgoing_links`: <*list of strings*> URLs seen in the rendered DOM that point to a different domain than this URL.
* `proxy_country`: <*string*> ISO country code of the egress proxy used for the last visit.
* `redirection_chain`: <*list of strings*> ordered list of URLs traversed during the last visit.
* `reputation`: <*integer*> value of votes from VT community.
* `tags`: <*list of strings*> tags attached to the URL (e.g. `trackers`, `password-input`).
* `targeted_brand`: <*dictionary*> brands the page appears to impersonate, as reported by phishing engines. Keys are engine names, values are the brand strings each engine assigned.
* `threat_names`: <*list of strings*> malware-family / threat-actor / campaign names associated with the URL.
* `threat_severity`: <*dictionary*> net threat severity computed for the URL (severity level + contributing signals). Premium API and GTI customers only.
* `threat_verdict`: <*string*> Google Threat Intelligence verdict about how malicious the URL may be (e.g. `VERDICT_BENIGN`, `VERDICT_MALICIOUS`). GTI customers only.
* `times_submitted`: <*integer*> number of times that URL has been analyzed.
* `title`: <*string*> webpage title.
* `tld`: <*string*> top-level / root domain of the URL (e.g. `example.com` for `https://www.example.com/path`).
* `total_votes`: *\<dictionary*> the number of positive ("harmless") and negative ("malicious") votes received from VT community.
  * `harmless`: <*integer*> number of positive votes.
  * `malicious`: <*integer*> number of negative votes.
* `trackers`: <*dictionary*> third-party trackers ever detected on the page, grouped by tracker family. Each family maps to a list of entries with:
  * `id`: <*string*> tracker ID, when available.
  * `timestamp`: <*integer*> Unix epoch UTC time (seconds) the tracker was last ingested.
  * `url`: <*string*> tracker script URL.
* `url`: <*string*> original URL to scan (canonical form).
* `console_messages`: <*list of strings*> browser console messages captured during the last visit.
* `crowdsourced_ai_results`: <*list of dictionaries*> results contributed by crowdsourced AI analyzers for the URL. Not returned when AI features are disabled for the account.
* `javascript_variables`: <*list*> JavaScript variables observed in the page during the last visit.
* `user_agent`: <*string*> User-Agent string the browser used for the last visit. Currently restricted to internal preview.
* `web_category`: <*string*> normalised category of the page (e.g. `news`, `phishing`, `streaming`, `business`). Currently restricted to internal preview.
* `web_technologies`: <*list of dictionaries*> web technologies / frameworks detected on the page (CMS, JS libraries, analytics, ad networks…), each with `name` and `version`.

> ⚠️ gti\_assessment attribute
>
> To get the **gti\_assessment** attribute in the JSON response, ensure that the **x-tool** header is added to the request headers. This header should be used to identify your tool or service with a custom name.

## relationships

In addition to the previously described attributes, URL objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../01-api-introduction/api-responses/introduction-relationships.md) section. The available relationships are described bellow.

| Relationship                   | Description                                                                                                                                                                           | Accessibility                                        | Return object type                                                                                                                                                                                                                                                                                                    |
| :----------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| analyses                       | Analyses for the URL.                                                                                                                                                                 | Google TI users only.                                | List of [Analyses](analyses-object.md).                                                                                                                                                                                                                                                                              |
| associations                   | URL's associated objects (reports, campaigns, IoC collections, malware families, software toolkits, vulnerabilities, threat-actors), without filtering by the associated object type. | Everyone.                                            | List of [reports](report-object.md), [campaigns](campaign-object.md), [IoC collections](ioc-collection-object.md), [malware families](malware-family-object.md), [software toolkits](software-toolkit-object.md), [vulnerabilities](vulnerability-object.md), [threat-actors](threat-actor-object.md) objects. |
| campaigns                      | Campaigns associated to the URL.                                                                                                                                                      | Google TI Enterprise and Enterprise Plus users only. | List of collections of type [Campaign](campaign-object.md).                                                                                                                                                                                                                                                          |
| collections                    | IoC Collections associated to the URL.                                                                                                                                                | Everyone.                                            | List of collections of type [IoC Collection](ioc-collection-object.md).                                                                                                                                                                                                                                              |
| comments                       | Community posted comments about the URL.                                                                                                                                              | Everyone.                                            | List of [Comments](comment-object.md).                                                                                                                                                                                                                                                                               |
| communicating\_files           | Files that communicate with a given URL when they're executed.                                                                                                                        | Google TI users only.                                | List of [Files](file-object.md).                                                                                                                                                                                                                                                                                     |
| contacted\_domains             | Domains from which the URL loads some kind of resource.                                                                                                                               | Google TI users only.                                | List of [Domains](domains-object.md).                                                                                                                                                                                                                                                                                |
| contacted\_ips                 | IPs from which the URL loads some kind of resource.                                                                                                                                   | Google TI users only.                                | List of [IP addresses](ip-object.md).                                                                                                                                                                                                                                                                                |
| downloaded\_files              | Files downloaded from the URL.                                                                                                                                                        | Google TI users only.                                | List of [Files](file-object.md).                                                                                                                                                                                                                                                                                     |
| embedded\_js\_files            | JS files embedded in a URL.                                                                                                                                                           | Google TI users only.                                | List of [Files](file-object.md).                                                                                                                                                                                                                                                                                     |
| graphs                         | Graphs including the URL.                                                                                                                                                             | Everyone.                                            | List of [Graphs](graph-object.md).                                                                                                                                                                                                                                                                                   |
| http\_response\_contents       | TTP response contents from the URL.                                                                                                                                                   | Google TI users only.                                | List of [Files](file-object.md).                                                                                                                                                                                                                                                                                     |
| last\_serving\_ip\_address     | Last IP address that served the URL.                                                                                                                                                  | Everyone.                                            | A single [IP address](ip-object.md).                                                                                                                                                                                                                                                                                 |
| malware\_families              | Malware families associated to the URL.                                                                                                                                               | Google TI Enterprise and Enterprise Plus users only. | A list of collections of type [malware family](malware-family-object.md).                                                                                                                                                                                                                                            |
| memory\_pattern\_parents       | Files having a domain as string on memory during sandbox execution.                                                                                                                   | Google TI users only.                                | List of [Files](file-object.md).                                                                                                                                                                                                                                                                                     |
| network\_location              | Domain or IP for the URL.                                                                                                                                                             | Everyone.                                            | A single [IP address](ip-object.md) or [Domain](domains-object.md).                                                                                                                                                                                                                                                 |
| outgoing\_links\_urls          | URL objects for the outgoing links seen in the URL's rendered DOM (the URL counterparts of the `outgoing_links` attribute).                                                           | Google TI users only.                                | A list of [URLs](url-object.md).                                                                                                                                                                                                                                                                                     |
| parent\_resource\_urls         | Returns the URLs where this URL has been loaded as resource.                                                                                                                          | Google TI users only.                                | A list of [URLs](url-object.md).                                                                                                                                                                                                                                                                                     |
| redirecting\_urls              | URLs that redirected to the given URL.                                                                                                                                                | Google TI users only.                                | A list of [URLs](url-object.md).                                                                                                                                                                                                                                                                                     |
| redirects\_to                  | URLs that this url redirects to.                                                                                                                                                      | Google TI users only.                                | A list of [URLs](url-object.md).                                                                                                                                                                                                                                                                                     |
| referrer\_files                | Files containing the URL.                                                                                                                                                             | Google TI users only.                                | A list of [Files](file-object.md).                                                                                                                                                                                                                                                                                   |
| referrer\_urls                 | URLs referring the URL.                                                                                                                                                               | Google TI users only.                                | A list of [URLs](url-object.md).                                                                                                                                                                                                                                                                                     |
| related\_collections           | Returns the Collections of the parent Domains or IPs of this URL.                                                                                                                     | Google TI Enterprise and Enterprise Plus users only. | List of [IoC Collections](ioc-collection-object.md).                                                                                                                                                                                                                                                                 |
| related\_comments              | Community posted comments in the URL's related objects.                                                                                                                               | Everyone.                                            | A list of [Comments](comment-object.md).                                                                                                                                                                                                                                                                             |
| related\_reports               | Reports that are directly and indirectly related to the URL.                                                                                                                          | Google TI Enterprise and Enterprise Plus users only. | List of collections of type [Reports](report-object.md).                                                                                                                                                                                                                                                             |
| related\_threat\_actors        | URL's related threat actors.                                                                                                                                                          | Google TI Enterprise and Enterprise Plus users only. | List of [Threat Actors](threat-actor-object.md).                                                                                                                                                                                                                                                                     |
| reports                        | Reports directly associated to the URL.                                                                                                                                               | Google TI Enterprise and Enterprise Plus users only. | A list of [Reports](report-object.md).                                                                                                                                                                                                                                                                               |
| software\_toolkits             | Software and Toolkits associated to the URL.                                                                                                                                          | Google TI Enterprise and Enterprise Plus users only. | A list of [Software and Toolkits](software-toolkit-object.md).                                                                                                                                                                                                                                                       |
| submissions                    | URL's submissions.                                                                                                                                                                    | Google TI users only.                                | A list of [Submissions](submission-object.md).                                                                                                                                                                                                                                                                       |
| urls\_related\_by\_tracker\_id | URLs that share the same tracker ID.                                                                                                                                                  | Google TI users only.                                | A list of [URLs](url-object.md).                                                                                                                                                                                                                                                                                     |
| user\_votes                    | URL's votes made by current signed-in user.                                                                                                                                           | Everyone.                                            | A list of [Votes](vote-object.md).                                                                                                                                                                                                                                                                                   |
| votes                          | Votes for the URL.                                                                                                                                                                    | Everyone.                                            | A list of [Votes](vote-object.md).                                                                                                                                                                                                                                                                                   |
| vulnerabilities                | Vulnerabilities associated to the URL.                                                                                                                                                | Google TI Enterprise and Enterprise Plus users only. | A list of [Vulnerabilities](vulnerability-object.md).                                                                                                                                                                                                                                                                |

<br />

## identifiers

A URL's object ID is the SHA-256 of its canonical form. The same ID can equivalently be derived from the URL itself by Base64-encoding it (URL-safe alphabet, padding stripped); both forms are accepted as path parameters.

## example

```json URL object
{
  "data": {
    "id": "<sha256>",
    "type": "url",
    "attributes": {
      "url": "https://example.com/",
      "tld": "example.com",
      "last_final_url": "https://www.example.com/landing",
      "title": "Example Domain",
      "redirection_chain": [
        "https://example.com/"
      ],
      "last_http_response_code": 200,
      "last_http_response_content_length": 14580,
      "last_http_response_content_sha256": "<sha256>",
      "last_http_response_headers": {
        "content-type": "text/html; charset=UTF-8",
        "server": "nginx"
      },
      "last_http_response_cookies": {
        "sessionid": "<value>"
      },
      "html_meta": {
        "viewport": ["width=device-width, initial-scale=1"]
      },
      "favicon": {
        "dhash": "<dhash>",
        "raw_md5": "<md5>"
      },
      "categories": {
        "Forcepoint ThreatSeeker": "business and economy"
      },
      "trackers": {
        "google-analytics": [
          {"id": "G-XXXXXXX", "timestamp": 1716115200, "url": "https://www.googletagmanager.com/gtag/js"}
        ]
      },
      "outgoing_links": [
        "https://www.iana.org/domains/example"
      ],
      "targeted_brand": {
        "<engine_name>": "<brand name>"
      },
      "identified_brands": {
          "GTI": ["<brand name>"]
      },
      "main_brand": "google",
      "tags": ["tag1", "tag2"],
      "threat_names": [],
      "first_submission_date": 1380000000,
      "first_seen_itw_date": 1700000000,
      "last_submission_date": 1716115200,
      "last_analysis_date": 1716115200,
      "last_modification_date": 1716115200,
      "times_submitted": 421,
      "last_analysis_results": {
        "<engine_name>": {
          "category": "harmless",
          "engine_name": "<engine_name>",
          "method": "blacklist",
          "result": "clean"
        }
      },
      "last_analysis_stats": {
        "harmless": 71,
        "malicious": 2,
        "suspicious": 0,
        "timeout": 0,
        "undetected": 21
      },
      "reputation": 12,
      "total_votes": {
        "harmless": 9,
        "malicious": 3
      },
      "has_content": true,
      "gti_assessment": {
        "threat_score": {
          "value": 1
        },
        "severity": {
          "value": "SEVERITY_NONE"
        },
        "verdict": {
          "value": "VERDICT_UNDETECTED"
        },
        "contributing_factors": {
          "malicious_sandbox_verdict": false,
          "mandiant_confidence_score": 50,
          "gti_confidence_score": 34,
          "safebrowsing_verdict": "harmless"
        },
        "description": "This indicator did not match our detection criteria and there is currently no evidence of malicious activity.",
        "gti_description_cards": {
          "BULK_SIGNALS": [
            {
              "influence": "medium",
              "title": "Google Safe Browsing: undetected",
              "sub_title": "",
              "related_links": [],
              "collection_type": null
            }
          ]
        }
      },
    }
  }
}
```

<br />

---

← [Threat Profile](threat-profile-object.md) · [up](README.md) · [🔀 analyses](url-object/url-analyses.md) →

*Archived from <https://gtidocs.virustotal.com/reference/url-object>.*
