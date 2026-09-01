---
title: "IoC Collection"
source: https://gtidocs.virustotal.com/reference/ioc-collection-object
slug: ioc-collection-object
section: reference
group: "API OBJECTS"
updatedAt: 2026-05-19T11:29:21.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › IoC Collection

---

# ioc-collection

Information about IoC collections

IoC collections are sets of IoCs (files, URLs, IPs and domains) related to threat campaigns or malware families provided by the community, users, researchers, investigators and our Google TI experts.

## object-attributes

A IoC collection object contains the following attributes:

* `aggregations`: <*dictionary*> dictionary of commonalities between the different IoCs associated with the IoC collection, grouped by IoC type (files, URLs, domains, IP addresses).
  * `domains`: <*dictionary*> technical commonalities among all domains tied to the collection.
  * `files`: <*dictionary*> technical commonalities among all files tied to the collection.
  * `ip_addresses`: <*dictionary*> technical commonalities among all IP addresses tied to the collection.
  * `urls`: <*dictionary*> technical commonalities among all URLs tied to the collection.
* `alt_names`: <*list of strings*> list of alternative names / aliases for the IoC collection.
* `capabilities`: <*list of dictionaries*> list of capabilities associated with the IoC collection.
  * `confidence`: <*string*> the confidence of the IoC collection's associated capability.
  * `description`: <*string*> description of the capability.
  * `first_seen`: <*integer*> the first time when the capability was associated with the IoC collection (UTC timestamp).
  * `last_seen`: <*integer*> the first time when the capability was associated with the IoC collection (UTC timestamp).
  * `value`: <*string*> capability associated with the IoC collection.
* `collection_type`: <*string*> identifies the type of the object. For IoC collections the value of this attribute is `collection`.
* `counters`: <*dictionary*> dictionary of counters of related objects.
  * `attack_techniques`: <*integer*> number of MITRE ATT\&CK techniques associated with the collection.
  * `domains`: <*integer*> number of domains related to the collection.
  * `files`: <*integer*> number of files related to the collection.
  * `iocs`: <*integer*> number of IoCs (files + URLs + domains + IP addresses) related to the collection.
  * `ip_addresses`: <*integer*> number of IP addresses related to the collection.
  * `subscribers`: <*integer*> number of users subscribed to the collection.
  * `urls`: <*integer*> number of URLs related to the collection.
* `creation_date`: <*integer*> collection object creation date (UTC timestamp).
* `description`: <*string*> description / context about the collection.
* `detection_names`: <*list of dictionaries*> list of detection names and extra context.
  * `confidence`: <*string*> the confidence of the detection.
  * `description`: <*string*> descriptive information related to the detection.
  * `first_seen`: <*integer*> the first time when the detection was associated with the IoC collection (UTC timestamp).
  * `last_seen`: <*integer*> the last time when the detection was associated with the IoC collection (UTC timestamp).
  * `value`: <*string*> the detection name.
* `first_seen_details`: <*list of dictionaries*> dictionaries with additional information related to the first activity among the IoCs of the collection, differentiating between confirmed and suspected activity.
  * `confidence`: <*string*> confidence on the information of the first activity seen among the IoCs associated with the collection.
  * `description`: <*string*> description / additional information about the first activity seen among the IoCs associated with the collection.
  * `first_seen`: <*integer*> the first time this first activity date has been attributed to the collection (UTC timestamp).
  * `last_seen`: <*integer*> the last time this first activity date has been attributed to the collection (UTC timestamp).
  * `value`: <*string*> date when the first observation about that collection was made ("YYYY-MM-DDTHH:mm:ssZ" format).
* `last_modification_date`: <*integer*> last time when the collection's information was updated (UTC timestamp).
* `last_seen_details`: \<list of dictionaries> dictionaries with additional information related to the last activity among the IoCs of the collection, differentiating between confirmed and unconfirmed activity.
  * `confidence`: <*string*> confidence on the information or the last activity seen among the IoCs associated with the collection.
  * `description`: <*string*> description / additional information about the last activity seen among the IoCs associated with the collection.
  * `first_seen`: <*integer*> the first time this last activity date has been attributed to the collection (UTC timestamp).
  * `last_seen`: <*integer*> the last time this last activity date has been attributed to the collection (UTC timestamp).
  * `value`: <*string*> date when the last observation about that collection was made ("YYYY-MM-DDTHH:mm:ssZ" format).
* `link`: <*string*> URL to extra resources.
* `malware_roles`: <*list of dictionaries*> the list of malware roles associated with the threat represented by the IoC collection.
  * `confidence`: <*string*> the confidence of the associated malware role.
  * `description`: <*string*> descriptive information related to the associated malware role.
  * `first_seen`: <*integer*> the first time when the malware role was associated with the IoC collection (UTC timestamp).
  * `last_seen`: <*integer*> the last time when the malware role was associated with the IoC collection (UTC timestamp).
  * `value`: <*string*> the malware role name.
* `motivations`: <*list of dictionaries*> motivations of the threat represented by the IoC collection such as espionage, financial gain, etc.
  * `confidence`: <*string*> confidence on the associated motivation.
  * `description`: <*string*> description / additional information about the associated motivation.
  * `first_seen`: <*integer*> the first time this motivation was associated with the IoC collection (UTC timestamp).
  * `last_seen`: <*integer*> the last time this motivation was associated with the IoC collection (UTC timestamp).
  * `value`: <*string*> motivation name.
* `name`: <*string*> IoC collection's name.
* `operating_systems`: <*list of dictionaries*> operating systems targeted by the threat represented by the IoC collection. Possible values: Android, BSD, FreeBSD, Linux, Mac, Unix, VMkernel, Windows, iOS.
  * `confidence`: <*string*> the confidence that the operating system is affected by the represented threat.
  * `description`: <*string*> descriptive information related to the targeted operating system.
  * `first_seen`: <*integer*> the first time when the operating system was targeted by the represented threat (UTC timestamp).
  * `last_seen`: <*integer*> the last time when the operating system was targeted by the represented threat (UTC timestamp).
  * `value`: <*string*> operating system name.
* `origin`: <*string*> identifies the source of the information. **Partner** for curated objects from trusted partners and security researchers, **Google Threat Intelligence** for curated objects from our Google TI experts and **Crowdsourced** for OSINT objects from the community.
* `private`: <*boolean*> whether the collection object is private or not.
* `recent_activity_relative_change`: <*float*> ratio of change between the last two "recent activity" periods. Note: "recent activity" refers to a period of 14 days.
* `recent_activity_summary`: <*list of integers*> time series representing the activity of the IoCs that belong to the collection. (2 weeks)
* `sponsor_region`: <*string*> the main country or region suspected to sponsor the threat represented by the IoC collection.
* `source_region`: <*string*> the main country or region from which the malicious activity represented by the IoC collection is known to originate.
* `source_regions_hierarchy`: <*list of dictionaries*> country or region from which the malicious activity is known to originate.
  * `confidence`: <*string*> confidence on the information related to the source region of the malicious activity.
  * `country`: <*string*> country from which malicious activity is known to originate.
  * `country_iso2`: <*string*> source country in ISO 3166 Alpha2 - code format.
  * `description`: <*string*> description / additional information about the source region of the malicious activity.
  * `first_seen`: <*integer*> the first time this source region was attributed to the collection (UTC timestamp).
  * `last_seen`:<*integer*> the last time this source region was attributed to the collection (UTC timestamp).
  * `region`: <*string*> region from which the malicious activity is known to originate.
  * `source`: <*string*> information's supplier.
  * `sub_region`: <*string*> subregion from which the malicious activity is known to originate.
* `status`: <*string*> indicates if the object has attributes pending to be computed again (e.g. top\_icon\_md5 after making changes). The possible values are `PENDING_RECOMPUTE` and `COMPUTED`.
* `summary_stats`: <*list of dictionaries*> stats associated with the collection.
  * `first_submission_date`: <*dictionaries*> the minimun (`min`), maximun (`max`) and average (`avg`) values of the first\_submission\_date of all the IoCs included on the collection.
  * `last_submission_date`: <*dictionaries*> the minimun (`min`), maximun (`max`) and average (`avg`) values of the last\_submission\_date of all the IoCs included on the collection.
  * `files_detections`: <*dictionaries*> the minimun (`min`), maximun (`max`) and average (`avg`) values of the files\_detections of all the IoCs included on the collection.
  * `urls_detections`: <*dictionaries*> the minimun (`min`), maximun (`max`) and average (`avg`) values of the urls\_detections of all the IoCs included on the collection.
* `tags`: <*list of string*> tags associated with the collection.
* `targeted_industries`: <*list of strings*> list of industries known to be targeted by the threat represented by the IoC collection.
* `targeted_industries_tree`: <*list of dictionaries*> list of industries and industry groups known to be targeted by the collection's associated campaign or malicious activity.
  * `confidence`: <*string*> confidence on the information related to the industry targeted by the malicious activity.
  * `description`: <*string*> description / additional information about the industry targeted by the malicious activity.
  * `first_seen`: <*integer*> the first time this targeted industry was associated with the collection (UTC timestamp).
  * `last_seen`: <*integer*> the last time this targeted industry was associated with the collection (UTC timestamp).
  * `industry`: <*string*> sub-industry targeted by the malicious activity.
  * `industry_group`: <*string*> industry group targeted by the malicious activity.
  * `source`: <*string*> information's supplier.
* `targeted_regions`: <*list of strings*> list of regions and countries known to be targeted by the threat represented by the IoC collection.
* `targeted_regions_hierarchy`: <*list of dictionaries*> list of regions and countries known to be targeted by collection's associated campaign or malicious activity.
  * `confidence`: <*string*> confidence on the information related to the region targeted by the malicious activity.
  * `country`: <*string*> country targeted by the malicious activity.
  * `country_iso2`: <*string*> targeted country in ISO 3166 Alpha2 - code format.
  * `description`: <*string*> description / additional information about the region targeted by the malicious activity.
  * `first_seen`: <*integer*> the first time this targeted region was associated with the collection (UTC timestamp).
  * `last_seen`:<*integer*> : the last time this targeted region was associated with the collection (UTC timestamp).
  * `region`: <*string*> region targeted by the malicious activity.
  * `sub_region`: <*string*> sub-region targeted by the malicious activity.
  * `source`: <*string*> information's supplier.
* `tlp`: <*string*> it indicates the sensitivity of the information and defines the boundaries for how and with whom the data can be shared. Available values are: `RED`, `AMBER`, `GREEN`, `CLEAR` .
* `top_icon_md5`: <*list of strings*> list of the 3 most frequent icons among the collection's associated IoCs (file's icons, URLs and domain's favicons). Favicons are represented by their MD5 hash.

## relationships

In addition to the previously described attributes, IoC collection objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../01-api-introduction/api-responses/introduction-relationships.md) section.

The following table shows a summary of available relationships.

| Relationship         | Return object type                                                                                                                                                                                                                                                                                                                                                                 | Allowed Methods |
| :------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------- |
| associations         | List of all objects ([Campaigns](campaign-object.md), [IoC collections](ioc-collection-object.md), [Malware families](malware-family-object.md), [Software and Toolkits](software-toolkit-object.md), [Vulnerabilities](vulnerability-object.md), [Threat Actors](threat-actor-object.md)) associated with the current IoC collection, without filtering by the object type. | GET             |
| attack\_techniques   | List of MITRE ATT\&CK [techniques](object-attack-techniques.md).                                                                                                                                                                                                                                                                                                                  | GET             |
| campaigns            | List of associated collections of type [Campaign](campaign-object.md) objects.                                                                                                                                                                                                                                                                                                    | GET             |
| collections          | List of associated collections of type [IoC collection](ioc-collection-object.md) objects.                                                                                                                                                                                                                                                                                        | GET             |
| comments             | List of [Comments](comment-object.md).                                                                                                                                                                                                                                                                                                                                            | GET             |
| domains              | List of [Domains](domains-object.md) associated with the IoC collection.                                                                                                                                                                                                                                                                                                          | GET             |
| editors              | List of [users](user-object.md), [groups](group-object.md) and data connectors that can edit this threat actor *(only available to the owner or editor of the entity).*                                                                                                                                                                                                          | GET , POST      |
| files                | List of [Files](file-object.md) associated with the IoC collection.                                                                                                                                                                                                                                                                                                               | GET             |
| hunting\_rulesets    | List of curated [YARA rulesets](yara-rulesets-object.md) assigned by the entity owner.                                                                                                                                                                                                                                                                                            | GET             |
| ip\_addresses        | List of [IP addresses](ip-object.md) associated with the IoC collection.                                                                                                                                                                                                                                                                                                          | GET             |
| malware\_families    | List of associated collections of type [Malware family](malware-family-object.md) objects.                                                                                                                                                                                                                                                                                        | GET             |
| owner                | [User](user-object.md) who created the object.                                                                                                                                                                                                                                                                                                                                    | GET             |
| related\_collections | List of objects ([Campaigns](campaign-object.md), [IoC collections](ioc-collection-object.md), [Malware families](malware-family-object.md), [Software and Toolkits](software-toolkit-object.md), [Vulnerabilities](vulnerability-object.md), [Threat Actors](threat-actor-object.md)) containing IoCs associated with this entity.                                          | GET             |
| reports              | List of associated collections of type [Report](report-object.md) objects.                                                                                                                                                                                                                                                                                                        | GET             |
| software\_toolkits   | List of associated collections of type [Software or Toolkit](software-toolkit-object.md) objects.                                                                                                                                                                                                                                                                                 | GET             |
| threat\_actors       | List of other collections of type [threat actors](threat-actor-object.md) associated to the current IoC collection.                                                                                                                                                                                                                                                               | GET             |
| urls                 | List of [URLs](url-object.md) associated with the IoC collection.                                                                                                                                                                                                                                                                                                                 | GET             |
| viewers              | List of [users](user-object.md), [groups](group-object.md) and data connectors that can view the entity *(only available to the owner or editor of the entity).*                                                                                                                                                                                                                 | GET , POST      |
| vulnerabilities      | List of associated collections of type [Vulnerability](vulnerability-object.md) objects.                                                                                                                                                                                                                                                                                          | GET             |
| yara\_rulesets       | List of crowdsourced [YARA rulesets](yara-rulesets-object.md) matching at least one file associated with this IoC collection.                                                                                                                                                                                                                                                     | GET             |

---

← [Industry Profile](industry-profile-object.md) · [up](README.md) · [IoC-Stream Notifications](ioc-stream-notifications-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/ioc-collection-object>.*
