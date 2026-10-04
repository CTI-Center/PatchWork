---
title: "Software and Toolkit"
source: https://gtidocs.virustotal.com/reference/software-toolkit-object
slug: software-toolkit-object
section: reference
group: "API OBJECTS"
updatedAt: 2026-03-31T09:22:46.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Software and Toolkit

---

# software-and-toolkit

Information about software and toolkits

> 🚧 Special privileges required
>
> Software and Toolkits are only available to users with the Google Threat Intelligence (Google TI) Enterprise or Enterprise Plus licenses.

Software and toolkits are digital tools used by threat actors in their threat campaigns.

## object-attributes

A software and toolkits object contains the following attributes:

* `aggregations`: <*dictionary*> dictionary of commonalities between the different IoCs associated with the software or toolkit, grouped by IoC type (files, URLs, domains, IP addresses).
  * `domains`: <*dictionary*> technical commonalities among all domains tied to the software or toolkit.
  * `files`: <*dictionary*> technical commonalities among all files tied to the software or toolkit.
  * `ip_addresses`: <*dictionary*> technical commonalities among all IP addresses tied to the software or toolkit.
  * `urls`: <*dictionary*> technical commonalities among all URLs tied to the software or toolkit.
* `alt_names`: <*list of strings*> list of alternative names / aliases by which the software or toolkit is known.
* `alt_names_details`: <*list of dictionaries*> dictionary of alternative names / aliases by which the software or toolkit could be known, including additional information such as the confidence of the attribution or information and the first and last attribution dates for this particular attribute.
  * `confidence`: <*string*> confidence on the information or the attribution of the alternative name to the software or toolkit.
  * `description`: <*string*> additional information related to the alternative name.
  * `first_seen`: <*integer*> the first time that alternative name was attributed to the software or toolkit (UTC timestamp).
  * `last_seen`: <*integer*> the last time that alternative name was attributed to the software or toolkit (UTC timestamp).
  * `value`: <*string*> alternative name / alias.
* `capabilities`: <*list of dictionaries*> list of capabilities associated with the software or toolkit.
  * `confidence`: <*string*> the confidence of the software or toolkit's associated capability.
  * `description`: <*string*> description of the capability.
  * `first_seen`: <*integer*> the first time when the capability was associated with the software or toolkit (UTC timestamp).
  * `last_seen`: <*integer*> the first time when the capability was associated with the software or toolkit (UTC timestamp).
  * `value`: <*string*> capability associated with the software or toolkit.
* `collection_type`: <*string*> identifies the type of the object. For software and toolkits the value of this attribute is `software_toolkits`.
* `counters`: <*dictionary*> dictionary of counters of related objects.
  * `attack_techniques`: <*integer*> number of MITRE ATT\&CK techniques associated with the software or toolkits.
  * `domains`: <*integer*> number of domains related to the software or toolkits.
  * `files`: <*integer*> number of files related to the software or toolkits.
  * `iocs`: <*integer*> number of IoCs (files + URLs + domains + IP addresses) related to the software or toolkits.
  * `ip_addresses`: <*integer*> number of IP addresses related to the software or toolkits.
  * `subscribers`: <*integer*> number of users subscribed to the software or toolkits.
  * `urls`: <*integer*> number of URLs related to the software or toolkits.
* `creation_date`: <*integer*> software or toolkit object creation date (UTC timestamp).
* `description`: <*string*> description / context about the software or toolkit.
* `detection_names`: <*list of dictionaries*> list of external detection names associated to software or toolkits with additional context.
  * `description`: <*string*> descriptive information related to the detection name.
  * `confidence`: <*string*> the confidence of the detection name associated to the software or toolkit.
  * `first_seen`: <*integer*> the first time when the detection name was associated to the software or toolkit (UTC timestamp).
  * `last_seen`: <*integer*> the last time when the detection name was associated to the software or toolkit (UTC timestamp).
  * `value`: <*string*> the detection name.
* `first_seen_details`: <*list of dictionaries*> dictionaries with additional information related to the software or toolkit's first activity, differentiating between confirmed and unconfirmed activity.
  * `confidence`: <*string*> confidence on the information or the attribution of the first activity seen related to the software or toolkit.
  * `description`: <*string*> description / additional information about the first activity seen related to the software or toolkit.
  * `first_seen`: <*integer*> the first time this first activity date has been attributed to the software or toolkit (UTC timestamp).
  * `last_seen`: <*integer*> the last time this first activity date has been attributed to the software or toolkit (UTC timestamp).
  * `value`: <*string*> date when the first observation about that software or toolkit was made ("YYYY-MM-DDTHH:mm:ssZ" format).
* `last_modification_date`: <*integer*> last time when the software or toolkit's information was updated (UTC timestamp).
* `last_seen_details`: \<list of dictionaries> dictionaries with additional information related to the software or toolkit's last activity, differentiating between confirmed and unconfirmed activity.
  * `confidence`: <*string*> confidence on the information or the attribution of the last activity seen related to the software or toolkit.
  * `description`: <*string*> description / additional information about the last activity seen related to the software or toolkit.
  * `first_seen`: <*integer*> the first time this last activity date has been attributed to the software or toolkit (UTC timestamp).
  * `last_seen`: <*integer*> the last time this last activity date has been attributed to the software or toolkit (UTC timestamp).
  * `value`: <*string*> date when the last observation about that software or toolkit was made ("YYYY-MM-DDTHH:mm:ssZ" format).
* `link`: <*string*> URL to extra resources.
* `malware_roles`: <*list of dictionaries*> the list of malware roles associated with the software or toolkit.
  * `value`: <*string*> the malware role name associated with the software or toolkit.
  * `first_seen`: <*integer*> the first time when the malware role was associated with the software or toolkit (UTC timestamp).
  * `last_seen`: <*integer*> the last time when the malware role was associated with the software or toolkit (UTC timestamp).
  * `confidence`: <*string*> the confidence of the software or toolkit's associated malware role.
  * `description`: <*string*> descriptive information related to the software or toolkit's associated malware role.
* `motivations`: <*list of dictionaries*> motivations of the threat actor using the software or toolkit such as espionage, financial gain, etc.
  * `confidence`: <*string*> confidence on the associated motivation.
  * `description`: <*string*> description / additional information about the associated motivation.
  * `first_seen`: <*integer*> the first time this motivation was associated with the software or toolkit (UTC timestamp).
  * `last_seen`: <*integer*> the last time this motivation was associated with the software or toolkit (UTC timestamp).
  * `value`: <*string*> motivation name.
* `name`: <*string*> software or toolkit's name.
* `operating_systems`: <*list of dictionaries*> operating systems affected by the software or toolkit. Possible values: Android, BSD, FreeBSD, Linux, Mac, Unix, VMkernel, Windows, iOS.
  * `value`: <*string*> affected operating system.
  * `first_seen`: <*integer*> the first time when the operating system was associated to the software or toolkit (UTC timestamp).
  * `last_seen`: <*integer*> the last time when the operating system was associated to the software or toolkit (UTC timestamp).
  * `confidence`: <*string*> the confidence that the operating system is affected by the software or toolkit.
  * `description`: <*string*> descriptive information related to the software or toolkit's targeted operating system.
* `origin`: <*string*> identifies the source of the information. **Partner** for curated objects from trusted partners and security researchers and **Google Threat Intelligence** for curated objects from our Google TI experts.
* `private`: <*boolean*> whether the software or toolkit object is private or not.
* `recent_activity_relative_change`: <*float*> ratio of change between the last two "recent activity" periods. Note: "recent activity" refers to a period of 14 days.
* `recent_activity_summary`: <*list of integers*> time series representing the activity of the indicators of compromise related to the software or toolkit. (2 weeks)
* `sponsor_region`: <*string*> the main country or region suspected to sponsor the threat that uses the software or toolkit.
* `source_region`: <*string*> the main country or region from which the threat that uses the software or toolkit is known to originate.
* `source_regions_hierarchy`: <*list of dictionaries*> country or region from which the software or toolkit is known to originate.
  * `confidence`: <*string*> confidence on the information related to the source region of the software or toolkit.
  * `country`: <*string*> country from which software or toolkit is known to originate.
  * `country_iso2`: <*string*> source country in ISO 3166 Alpha2 - code format.
  * `description`: <*string*> description / additional information about the source region of the software or toolkit.
  * `first_seen`: <*integer*> the first time this source region was attributed to the software or toolkit (UTC timestamp).
  * `last_seen`:<*integer*> the last time this source region was attributed to the software or toolkit (UTC timestamp).
  * `region`: <*string*> region from which the software or toolkit is known to originate.
  * `source`: <*string*> information's supplier.
  * `sub_region`: <*string*> subregion from which the software or toolkit is known to originate.
* `status`: <*string*> indicates if the object has attributes pending to be computed again (e.g. top\_icon\_md5 after making changes). The possible values are `PENDING_RECOMPUTE` and `COMPUTED`.
* `summary_stats`: <*list of dictionaries*> stats associated with the software and toolkit.
  * `first_submission_date`: <*dictionaries*> the minimun (`min`), maximun (`max`) and average (`avg`) values of the first\_submission\_date of all the IoCs associated to the software and toolkit.
  * `last_submission_date`: <*dictionaries*> the minimun (`min`), maximun (`max`) and average (`avg`) values of the last\_submission\_date of all the IoCs associated to the software and toolkit.
  * `files_detections`: <*dictionaries*> the minimun (`min`), maximun (`max`) and average (`avg`) values of the files\_detections of all the IoCs associated to the software and toolkit.
  * `urls_detections`: <*dictionaries*> the minimun (`min`), maximun (`max`) and average (`avg`) values of the urls\_detections of all the IoCs associated to the software and toolkit.
* `tags`: <*list of string*> tags associated with the software and toolkit.
* `targeted_industries`: <*list of strings*> list of industries known to be targeted by the software or toolkit.
* `targeted_industries_tree`: <*list of dictionaries*> list of industries and industry groups known to be targeted by the software or toolkit.
  * `confidence`: <*string*> confidence on the information or the industry targeted by the software or toolkit.
  * `description`: <*string*> description / additional information related to the industry targeted by the software or toolkit.
  * `first_seen`: <*integer*> the first time this targeted industry was associated with the software or toolki (UTC timestamp).
  * `industry`: <*string*> sub-industry targeted by the software or toolkit.
  * `industry_group`: <*string*> industry group targeted by the software or toolkit.
  * `last_seen`: <*integer*> the last time this targeted industry was associated with the software or toolki (UTC timestamp).
  * `source`: <*string*> information's supplier.
* `targeted_regions`: <*list of strings*> list of regions and countries known to be targeted by the software or toolkit.
* `targeted_regions_hierarchy`: <*list of dictionaries*> list of regions and countries known to be targeted by the software or toolkit.
  * `confidence`: <*string*> confidence on the information or the software or toolkit's targeted region association.
  * `country`: <*string*> software or toolkit's targeted country.
  * `country_iso2`: <*string*> targeted country in ISO 3166 Alpha2 - code format.
  * `description`: <*string*> description / additional information related to the software or toolkit's targeted region.
  * `first_seen`: <*integer*> the first time this targeted region was associated with the current software or toolkit (UTC timestamp).
  * `last_seen`:<*integer*> the last time this targeted region was associated with the current software or toolkit (UTC timestamp).
  * `region`: <*string*> software or toolkit's targeted region.
  * `source`: <*string*> information's supplier.
  * `sub_region`: <*string*> software or toolkit's targeted sub-region.
* `tlp`: <*string*> it indicates the sensitivity of the information and defines the boundaries for how and with whom the data can be shared. Available values are: `RED`, `AMBER`, `GREEN`, `CLEAR` .
* `top_icon_md5`: <*list of strings*> list of the 3 most frequent icons among the software or toolkit's associated IoCs (file's icons, URLs and domain's favicons). Favicons are represented by their MD5 hash.

## relationships

In addition to the previously described attributes, software and toolkits objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../01-api-introduction/api-responses/introduction-relationships.md) section.

The following table shows a summary of available relationships.

| Relationship         | Return object type                                                                                                                                                                                                                                                                                                                                                                                               |    |
| :------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :- |
| associations         | List of all objects ([Reports](report-object.md), [Campaigns](campaign-object.md), [IoC collections](ioc-collection-object.md), [Malware families](malware-family-object.md), [Software and Toolkits](software-toolkit-object.md), [Vulnerabilities](vulnerability-object.md), [Threat Actors](threat-actor-object.md)) associated with the current malware family, without filtering by the object type. |    |
| attack\_techniques   | List of MITRE ATT\&CK [techniques](object-attack-techniques.md).                                                                                                                                                                                                                                                                                                                                                |    |
| campaigns            | List of associated collections of type [Campaign](campaign-object.md) objects.                                                                                                                                                                                                                                                                                                                                  |    |
| collections          | List of associated collections of type [IoC collection](ioc-collection-object.md) objects.                                                                                                                                                                                                                                                                                                                      |    |
| comments             | List of [Comments](comment-object.md).                                                                                                                                                                                                                                                                                                                                                                          |    |
| domains              | List of [Domains](domains-object.md) associated with the software or toolkit.                                                                                                                                                                                                                                                                                                                                   |    |
| editors              | List of [users](user-object.md), [groups](group-object.md) and data connectors that can edit this threat actor *(only available to the owner or editor of the entity).*                                                                                                                                                                                                                                        |    |
| files                | List of [Files](file-object.md) associated with the software or tolkit.                                                                                                                                                                                                                                                                                                                                         |    |
| hunting\_rulesets    | List of curated [YARA rulesets](yara-rulesets-object.md) assigned by the entity owner.                                                                                                                                                                                                                                                                                                                          |    |
| ip\_addresses        | List of [IP addresses](ip-object.md) associated with the software or toolkit.                                                                                                                                                                                                                                                                                                                                   |    |
| malware\_families    | List of associated collections of type [Malware family](malware-family-object.md) objects.                                                                                                                                                                                                                                                                                                                      |    |
| owner                | [User](user-object.md) who created the object.                                                                                                                                                                                                                                                                                                                                                                  |    |
| related\_collections | List of collection objects of type ([Reports](report-object.md), [Campaigns](campaign-object.md), [IoC collections](ioc-collection-object.md), [Malware families](malware-family-object.md), [Software and Toolkits](software-toolkit-object.md), [Vulnerabilities](vulnerability-object.md), [Threat Actors](threat-actor-object.md)) containing IoCs associated with this entity.                       |    |
| reports              | List of associated collections of type [Report](report-object.md) objects.                                                                                                                                                                                                                                                                                                                                      |    |
| software\_toolkits   | List of associated collections of type [Software or Toolkit](software-toolkit-object.md) objects.                                                                                                                                                                                                                                                                                                               |    |
| threat\_actors       | List of other collections of type [threat actors](threat-actor-object.md) associated to the current software or toolkit.                                                                                                                                                                                                                                                                                        |    |
| urls                 | List of [URLs](url-object.md) associated with the software or toolkit.                                                                                                                                                                                                                                                                                                                                          |    |
| viewers              | List of [users](user-object.md), [groups](group-object.md) and data connectors that can view the entity *(only available to the owner or editor of the entity).*                                                                                                                                                                                                                                               |    |
| vulnerabilities      | List of associated collections of type [Vulnerability](vulnerability-object.md) objects.                                                                                                                                                                                                                                                                                                                        |    |
| yara\_rulesets       | List of crowdsourced [YARA rulesets](yara-rulesets-object.md) matching at least one file associated with this software or toolkit.                                                                                                                                                                                                                                                                              |    |

---

← [Sigma Rules](sigma-rule-object.md) · [up](README.md) · [SSL Certificate](ssl-certificate-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/software-toolkit-object>.*
