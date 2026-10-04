---
title: "Campaign"
source: https://gtidocs.virustotal.com/reference/campaign-object
slug: campaign-object
section: reference
group: "API OBJECTS"
updatedAt: 2026-03-31T09:10:02.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Campaign

---

# campaign

Information about campaigns

> 🚧 Special privileges required
>
> Campaigns are only available to users with the Google Threat Intelligence (Google TI) Enterprise or Enterprise Plus licenses.

Campaigns objects are cyberattacks performed by one or more threat actors against a specific target or group of targets.

## object-attributes

A campaign object contains the following attributes:

* `aggregations`: <*dictionary*> dictionary of commonalities between the different IoCs associated with the campaign, grouped by IoC type (files, URLs, domains, IP addresses).
  * `domains`: <*dictionary*> technical commonalities among all domains tied to the campaign.
  * `files`: <*dictionary*> technical commonalities among all files tied to the campaign.
  * `ip_addresses`: <*dictionary*> technical commonalities among all IP addresses tied to the campaign.
  * `urls`: <*dictionary*> technical commonalities among all URLs tied to the campaign.
* `alt_names`: <*list of strings*> list of alternative names / aliases by which the campaign is known.
* `alt_names_details`: <*list of dictionaries*> dictionary of alternative names / aliases by which the campaign could be known, including additional information such as the confidence of the attribution or information and the first and last attribution dates for this particular attribute.
  * `confidence`: <*string*> confidence on the information or the attribution of the alternative name to the campaign.
  * `description`: <*string*> additional information related to the alternative name.
  * `first_seen`: <*integer*> the first time that alternative name was attributed to the campaign (UTC timestamp).
  * `last_seen`: <*integer*> the last time that alternative name was attributed to the campaign (UTC timestamp).
  * `value`: <*string*> alternative name / alias.
* `capabilities`: <*list of dictionaries*> list of capabilities associated with the campaign.
  * `confidence`: <*string*> the confidence of the campaign's associated capability.
  * `description`: <*string*> description of the capability.
  * `first_seen`: <*integer*> the first time when the capability was associated with the campaign (UTC timestamp).
  * `last_seen`: <*integer*> the first time when the capability was associated with the campaign (UTC timestamp).
  * `value`: <*string*> capability associated with the campaign.
* `collection_type`: <*string*> identifies the type of the object. For campaigns the value of this attribute is `campaign`.
* `counters`: <*dictionary*> dictionary of counters of related objects.
  * `attack_techniques`: <*integer*> number of MITRE ATT\&CK techniques associated with the campaign.
  * `domains`: <*integer*> number of domains related to the campaign.
  * `files`: <*integer*> number of files related to the campaign.
  * `iocs`: <*integer*> number of IoCs (files + URLs + domains + IP addresses) related to the campaign.
  * `ip_addresses`: <*integer*> number of IP addresses related to the campaign.
  * `subscribers`: <*integer*> number of users subscribed to the campaign.
  * `urls`: <*integer*> number of URLs related to the campaign.
* `creation_date`: <*integer*> campaign object creation date (UTC timestamp).
* `description`: <*string*> description / context about the campaign.
* `detection_names`: <*list of dictionaries*> list of detection names and extra context.
  * `confidence`: <*string*> the confidence of the detection.
  * `description`: <*string*> descriptive information related to the detection.
  * `first_seen`: <*integer*> the first time when the detection was associated with the campaign (UTC timestamp).
  * `last_seen`: <*integer*> the last time when the detection was associated with the campaign (UTC timestamp).
  * `value`: <*string*> the detection name.
* `first_seen_details`: <*list of dictionaries*> dictionaries with additional information related to the campaign's first activity, differentiating between confirmed and unconfirmed activity.
  * `confidence`: <*string*> confidence on the information or the attribution of the first activity seen related to the campaign.
  * `description`: <*string*> description / additional information about the first activity seen related to the campaign.
  * `first_seen`: <*integer*> the first time this first activity date has been attributed to the campaign (UTC timestamp).
  * `last_seen`: <*integer*> the last time this first activity date has been attributed to the campaign (UTC timestamp).
  * `value`: <*string*> date when the first observation about that campaign was made ("YYYY-MM-DDTHH:mm:ssZ" format).
* `last_modification_date`: <*integer*> last time when the campaign's information was updated (UTC timestamp).
* `last_seen_details`: \<list of dictionaries> dictionaries with additional information related to the campaign's last activity, differentiating between confirmed and unconfirmed activity.
  * `confidence`: <*string*> confidence on the information or the attribution of the last activity seen related to the campaign.
  * `description`: <*string*> description / additional information about the last activity seen related to the campaign.
  * `first_seen`: <*integer*> the first time this last activity date has been attributed to the campaign (UTC timestamp).
  * `last_seen`: <*integer*> the last time this last activity date has been attributed to the campaign (UTC timestamp).
  * `value`: <*string*> date when the last observation about that campaign was made ("YYYY-MM-DDTHH:mm:ssZ" format).
* `link`: <*string*> URL to extra resources.
* `malware_roles`: <*list of dictionaries*> the list of malware roles used by the threat campaign.
  * `confidence`: <*string*> the confidence of the associated malware role.
  * `description`: <*string*> descriptive information related to the associated malware role.
  * `first_seen`: <*integer*> the first time when the malware role was associated with the campaign (UTC timestamp).
  * `last_seen`: <*integer*> the last time when the malware role was associated with the campaign (UTC timestamp).
  * `value`: <*string*> the malware role name.
* `motivations`: <*list of dictionaries*> motivations of the threat actor behind the campaign such as espionage, financial gain, etc.
  * `confidence`: <*string*> confidence on the associated motivation.
  * `description`: <*string*> description / additional information about the associated motivation.
  * `first_seen`: <*integer*> the first time this motivation was associated with the campaign (UTC timestamp).
  * `last_seen`: <*integer*> the last time this motivation was associated with the campaign (UTC timestamp).
  * `value`: <*string*> motivation name.
* `name`: <*string*> campaign's name.
* `operating_systems`: <*list of dictionaries*> operating systems targeted by the threat campaign. Possible values: Android, BSD, FreeBSD, Linux, Mac, Unix, VMkernel, Windows, iOS.
  * `confidence`: <*string*> the confidence that the operating system is affected by the threat campaign.
  * `description`: <*string*> descriptive information related to the targeted operating system.
  * `first_seen`: <*integer*> the first time when the operating system was targeted by the campaign (UTC timestamp).
  * `last_seen`: <*integer*> the last time when the operating system was targeted by the campaign (UTC timestamp).
  * `value`: <*string*> operating system name.
* `origin`: <*string*> identifies the source of the information. **Google Threat Intelligence** for curated objects from our Google TI experts.
* `private`: <*boolean*> whether the campaign object is private or not.
* `recent_activity_relative_change`: <*float*> ratio of change between the last two "recent activity" periods. Note: "recent activity" refers to a period of 14 days.
* `recent_activity_summary`: <*list of integers*> time series representing the activity of the indicators of compromise related to the campaign. (2 weeks)
* `status`: <*string*> ndicates if the object has attributes pending to be computed again (e.g. top\_icon\_md5 after making changes). The possible values are `PENDING_RECOMPUTE` and `COMPUTED`.
* `sponsor_region`: <*string*> the main country or region suspected to sponsor the threat campaign.
* `source_region`: <*string*> the main country or region from which the campaign is known to originate.
* `source_regions_hierarchy`: <*list of dictionaries*> country or region from which the campaign is known to originate.
  * `confidence`: <*string*> confidence on the information or the source region of the malicious campaign.
  * `country`: <*string*> country from which the malicious campaign is known to originate.
  * `country_iso2`: <*string*> source country in ISO 3166 Alpha2 - code format.
  * `description`: <*string*> description / additional information about the country or region targeted by the campaign.
  * `first_seen`: <*integer*> the first time this source region was attributed to the campaign (UTC timestamp).
  * `last_seen`:<*integer*> the last time this source region was attributed to the campaign (UTC timestamp).
  * `region`: <*string*> region from which the malicious campaign is known to originate.
  * `source`: <*string*> information's supplier.
  * `sub_region`: <*string*> subregion from which the malicious campaign is known to originate.
* `summary_stats`: <*list of dictionaries*> stats associated with the campaign.
  * `first_submission_date`: <*dictionaries*> the minimun (`min`), maximun (`max`) and average (`avg`) values of the first\_submission\_date of all the IoCs associated to the campaign.
  * `last_submission_date`: <*dictionaries*> the minimun (`min`), maximun (`max`) and average (`avg`) values of the last\_submission\_date of all the IoCs associated to the campaign.
  * `files_detections`: <*dictionaries*> the minimun (`min`), maximun (`max`) and average (`avg`) values of the files\_detections of all the IoCs associated to the campaign.
  * `urls_detections`: <*dictionaries*> the minimun (`min`), maximun (`max`) and average (`avg`) values of the urls\_detections of all the IoCs associated to the campaign.
* `tags`: <*list of string*> tags associated with the campaign.
* `targeted_industries_tree`: <*list of dictionaries*> list of industries and industry groups known to be targeted by the campaign.
  * `confidence`: <*string*> confidence on the information or the industry targeted by the campaign.
  * `description`: <*string*> description / additional information related to the industry targeted by the campaign.
  * `first_seen`: <*integer*> the first time this targeted industry was associated with the campaign (UTC timestamp).
  * `industry`: <*string*> sub-industry targeted by the campaign.
  * `industry_group`: <*string*> industry group targeted by the campaign.
  * `last_seen`: <*integer*> the last time this targeted industry was associated with the campaign (UTC timestamp).
  * `source`: <*string*> information's supplier.
* `targeted_regions_hierarchy`: <*list of dictionaries*> list of regions and countries known to be targeted by the campaign.
  * `confidence`: <*string*> confidence on the information related to the region targeted by the malicious campaign.
  * `country`: <*string*> country targeted by the malicious campaign.
  * `country_iso2`: <*string*> targeted country in ISO 3166 Alpha2 - code format.
  * `description`: <*string*> description / additional information about the region targeted by the malicious campaign.
  * `first_seen`: <*integer*> the first time this targeted region was associated with the campaign (UTC timestamp).
  * `last_seen`:<*integer*> : the last time this targeted region was associated with the campaign (UTC timestamp).
  * `region`: <*string*> region targeted by the malicious campaign.
  * `sub_region`: <*string*> sub-region targeted by the malicious campaign.
  * `source`: <*string*> information's supplier.
* `tlp`: <*string*> it indicates the sensitivity of the information and defines the boundaries for how and with whom the data can be shared. Available values are: `RED`, `AMBER`, `GREEN`, `CLEAR` .
* `top_icon_md5`: <*list of strings*> list of the 3 most frequent icons among the campaign's associated IoCs (file's icons, URLs and domain's favicons). Favicons are represented by their MD5 hash.

## relationships

In addition to the previously described attributes, campaign objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../01-api-introduction/api-responses/introduction-relationships.md) section.

The following table shows a summary of available relationships.

| Relationship         | Return object type                                                                                                                                                                                                                                                                                                                                                                                         |    |
| :------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :- |
| associations         | List of all objects ([Reports](report-object.md), [Campaigns](campaign-object.md), [IoC collections](ioc-collection-object.md), [Malware families](malware-family-object.md), [Software and Toolkits](software-toolkit-object.md), [Vulnerabilities](vulnerability-object.md), [Threat Actors](threat-actor-object.md)) associated with the current campaign, without filtering by the object type. |    |
| attack\_techniques   | List of MITRE ATT\&CK [techniques](object-attack-techniques.md).                                                                                                                                                                                                                                                                                                                                          |    |
| campaigns            | List of associated collections of type [Campaign](campaign-object.md) objects.                                                                                                                                                                                                                                                                                                                            |    |
| collections          | List of associated collections of type [IoC collection](ioc-collection-object.md) objects.                                                                                                                                                                                                                                                                                                                |    |
| comments             | List of [Comments](comment-object.md).                                                                                                                                                                                                                                                                                                                                                                    |    |
| domains              | List of [Domains](domains-object.md) associated with the campaign.                                                                                                                                                                                                                                                                                                                                        |    |
| editors              | List of [users](user-object.md), [groups](group-object.md) and data connectors that can edit this threat actor *(only available to the owner or editor of the entity).*                                                                                                                                                                                                                                  |    |
| files                | List of [Files](file-object.md) associated with the campaign.                                                                                                                                                                                                                                                                                                                                             |    |
| hunting\_rulesets    | List of curated [YARA rulesets](yara-rulesets-object.md) assigned by the entity owner.                                                                                                                                                                                                                                                                                                                    |    |
| ip\_addresses        | List of [IP addresses](ip-object.md) associated with the campaign.                                                                                                                                                                                                                                                                                                                                        |    |
| malware\_families    | List of associated collections of type [Malware family](malware-family-object.md) objects.                                                                                                                                                                                                                                                                                                                |    |
| owner                | [User](user-object.md) who created the object.                                                                                                                                                                                                                                                                                                                                                            |    |
| related\_collections | List of collection object of type ([Reports](report-object.md), [Campaigns](campaign-object.md), [IoC collections](ioc-collection-object.md), [Malware families](malware-family-object.md), [Software and Toolkits](software-toolkit-object.md), [Vulnerabilities](vulnerability-object.md), [Threat Actors](threat-actor-object.md)) containing IoCs associated with this entity.                  |    |
| reports              | List of associated collections of type [Report](report-object.md) objects.                                                                                                                                                                                                                                                                                                                                |    |
| software\_toolkits   | List of associated collections of type [Software or Toolkit](software-toolkit-object.md) objects.                                                                                                                                                                                                                                                                                                         |    |
| threat\_actors       | List of other collections of type [threat actors](threat-actor-object.md) associated to the current campaign.                                                                                                                                                                                                                                                                                             |    |
| urls                 | List of [URLs](url-object.md) associated with the campaign.                                                                                                                                                                                                                                                                                                                                               |    |
| viewers              | List of [users](user-object.md), [groups](group-object.md) and data connectors that can view the entity *(only available to the owner or editor of the entity).*                                                                                                                                                                                                                                         |    |
| vulnerabilities      | List of associated collections of type [Vulnerability](vulnerability-object.md) objects.                                                                                                                                                                                                                                                                                                                  |    |
| yara\_rulesets       | List of crowdsourced [YARA rulesets](yara-rulesets-object.md) matching at least one file associated with this campaign.                                                                                                                                                                                                                                                                                   |    |

---

← [🔀 threat_actors](object-attack-techniques/attack-techniques-threat_actors.md) · [up](README.md) · [Comments](comment-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/campaign-object>.*
