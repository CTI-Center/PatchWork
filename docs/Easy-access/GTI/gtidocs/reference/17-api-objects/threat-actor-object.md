---
title: "Threat Actor"
source: https://gtidocs.virustotal.com/reference/threat-actor-object
slug: threat-actor-object
section: reference
group: "API OBJECTS"
updatedAt: 2026-03-31T09:18:22.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Threat Actor

---

# threat-actor

Information about threat actors

> 🚧 Special privileges required
>
> Threat Actors are only available to users with the Google Threat Intelligence (Google TI) Enterprise or Enterprise Plus licenses.

Threat actors are known persons or groups responsible for security incidents.

## object-attributes

A threat actor object contains the following attributes:

* `aggregations`: <*dictionary*> dictionary of commonalities between the different IoCs associated with the threat actor, grouped by IoC type (files, URLs, domains, IP addresses).
  * `domains`: <*dictionary*> technical commonalities among all domains tied to a threat actor.
  * `files`: <*dictionary*> technical commonalities among all files tied to a threat actor.
  * `ip_addresses`: <*dictionary*> technical commonalities among all IP addresses tied to a threat actor.
  * `urls`: <*dictionary*> technical commonalities among all URLs tied to a threat actor.
* `alt_names`: <*list of strings*> list of alternative names / aliases by which the threat actor is known.
* `alt_names_details`: <*list of dictionaries*> dictionary of alternative names / aliases by which the threat actor is known, including additional data such as the confidence of the information.
  * `confidence`: <*string*> confidence on the information or the attribution of the alternative name to the threat actor.
  * `description`: <*string*> additional information related to the alternative name.
  * `first_seen`: <*integer*> the first time that alternative name was attributed to the threat actor (UTC timestamp).
  * `last_seen`: <*integer*> the last time that alternative name was attributed to the threat actor (UTC timestamp).
  * `value`: <*string*> alternative name / alias.
* `capabilities`: <*list of dictionaries*> list of capabilities associated with the threat actor.
  * `confidence`: <*string*> the confidence of the threat actor's associated capability.
  * `description`: <*string*> description of the capability.
  * `first_seen`: <*integer*> the first time when the capability was associated with the threat actor (UTC timestamp).
  * `last_seen`: <*integer*> the first time when the capability was associated with the threat actor (UTC timestamp).
  * `value`: <*string*> capability associated with the threat actor.
* `collection_type`: <*string*> identifies the type of the object. For threat actors the value of this attribute is `threat_actor`.
* `counters`: <*dictionary*> dictionary of counters of related objects.
  * `domains`: <*integer*> number of domains related to the threat actor.
  * `files`: <*integer*> number of files related to the threat actor.
  * `iocs`: <*integer*> number of IoCs (files + URLs + domains + IP addresses) related to the threat actor.
  * `ip_addresses`: <*integer*> number of IP addresses related to the threat actor.
  * `subscribers`: <*integer*> number of users subscribed to the threat actor.
  * `urls`: <*integer*> number of URLs related to the threat actor.
* `creation_date`: <*integer*> threat actor object creation date (UTC timestamp).
* `description`: <*string*> description / context about the threat actor.
* `detection_names`: <*list of dictionaries*> list of detection names and extra context.
  * `confidence`: <*string*> the confidence of the detection.
  * `description`: <*string*> descriptive information related to the detection.
  * `first_seen`: <*integer*> the first time when the detection was associated with the threat actor (UTC timestamp).
  * `last_seen`: <*integer*> the last time when the detection was associated with the threat actor (UTC timestamp).
  * `value`: <*string*> the detection name.
* `first_seen_details`: <*list of dictionaries*> dictionaries with additional information related to the threat actor's first activity, differentiating between confirmed and suspected activity.
  * `confidence`: <*string*> confidence on the information or the attribution of the first activity seen related to the threat actor.
  * `description`: <*string*> description / additional information about the first activity seen of the threat actor.
  * `first_seen`: <*integer*> the first time this first activity date has been attributed to the threat actor (UTC timestamp).
  * `last_seen`: <*integer*> the last time this first activity date has been attributed to the threat actor (UTC timestamp).
  * `value`: <*string*> date when the first observation about that threat actor was made ("YYYY-MM-DDTHH:mm:ssZ" format).
* `last_modification_date`: <*integer*> last time when the threat actor's information was updated (UTC timestamp).
* `last_seen_details`: \<list of dictionaries> dictionaries with additional information related to the threat actor's last activity, differentiating between confirmed and unconfirmed activity.
  * `confidence`: <*string*> confidence on the information or the attribution of the last activity seen related to the threat actor.
  * `description`: <*string*> description / additional information about the last activity seen of the threat actor.
  * `first_seen`: <*integer*> the first time this last activity date has been attributed to the threat actor (UTC timestamp).
  * `last_seen`: <*integer*> the last time this last activity date has been attributed to the threat actor (UTC timestamp).
  * `value`: <*string*> date when the last observation about that threat actor was made ("YYYY-MM-DDTHH:mm:ssZ" format).
* `link`: <*string*> URL to extra resources.
* `merged_actors`: <*list of dictionaries*> list of actors confirmed to be part of a larger group (current threat actor) to which they were merged.
  * `confidence`: <*string*> confidence on the information or the attribution of the merged threat actor to the current threat actor.
  * `description`: <*string*> description / additional information about the merged actor (e.g. reference to its report - actor ID).
  * `first_seen`: <*integer*> the first time this merged threat actor was attributed to the current threat actor (UTC timestamp).
  * `last_seen`: <*integer*> the last time this merged threat actor was attributed to the current threat actor (UTC timestamp).
  * `value`: <*string*> name of the merged threat actor.
* `malware_roles`: <*list of dictionaries*> the list of malware roles used by the threat actor.
  * `confidence`: <*string*> the confidence of the associated malware role.
  * `description`: <*string*> descriptive information related to the associated malware role.
  * `first_seen`: <*integer*> the first time when the malware role was associated with the threat actor(UTC timestamp).
  * `last_seen`: <*integer*> the last time when the malware role was associated with the threat actor (UTC timestamp).
  * `value`: <*string*> the malware role name.
* `motivations`: <*list of dictionaries*> motivations of the threat actor such as espionage, financial gain, etc.
  * `confidence`: <*string*> confidence on the associated motivation.
  * `description`: <*string*> description / additional information about the associated motivation.
  * `first_seen`: <*integer*> the first time this motivation was attributed to the current threat actor (UTC timestamp).
  * `last_seen`: <*integer*> the last time this motivation was attributed to the current threat actor (UTC timestamp).
  * `value`: <*string*> motivation name.
* `name`: <*string*> threat actor's name.
* `operating_systems`: <*list of dictionaries*> operating systems targeted by the threat actor. Possible values: Android, BSD, FreeBSD, Linux, Mac, Unix, VMkernel, Windows, iOS.
  * `confidence`: <*string*> the confidence that the operating system is affected by the threat actor.
  * `description`: <*string*> descriptive information related to the targeted operating system.
  * `first_seen`: <*integer*> the first time when the operating system was targeted by the threat actor (UTC timestamp).
  * `last_seen`: <*integer*> the last time when the operating system was targeted by the threat actor (UTC timestamp).
  * `value`: <*string*> operating system name.
* `origin`: <*string*> identifies the source of the information. **Partner** for curated objects from trusted partners and security researchers and **Google Threat Intelligence** for curated objects from our Google TI experts.
* `private`: <*boolean*> whether the threat actor object is private or not.
* `recent_activity_relative_change`: <*float*> ratio of change between the last two "recent activity" periods. Note: "recent activity" refers to a period of 14 days.
* `recent_activity_summary`: <*list of integers*> time series representing the activity of the indicators of compromise related to the threat actor. (2 weeks)
* `sponsor_region`: <*string*> the main country or region suspected to sponsor the threat actor.
* `source_region`: <*string*> the main country or region where this threat actor is known to be based.
* `source_regions_hierarchy`: <*list of dictionaries*> country or region from which the threat actor of interest is known to originate.
  * `confidence`: <*string*> confidence on the information or the threat actor's source region association.
  * `country`: <*string*> country from which the threat actor of interest is known to originate.
  * `country_iso2`: <*string*> source country in ISO 3166 Alpha2 - code format.
  * `description`: <*string*> description / additional information about the threat actor's motivation.
  * `first_seen`: <*integer*> the first time this source region was attributed to the current threat actor (UTC timestamp).
  * `last_seen`:<*integer*> the last time this source region was attributed to the current threat actor (UTC timestamp).
  * `region`: <*string*> region from which the threat actor of interest is known to originate.
  * `source`: <*string*> information's supplier.
  * `sub_region`: <*string*> subregion from which the threat actor of interest is known to originate.
* `status`: <*string*> indicates if the object has attributes pending to be computed again (e.g. top\_icon\_md5 after making changes). The possible values are `PENDING_RECOMPUTE` and `COMPUTED`.
* `summary_stats`: <*list of dictionaries*> stats associated with the threat actor.
  * `first_submission_date`: <*dictionaries*> the minimun (`min`), maximun (`max`) and average (`avg`) values of the first\_submission\_date of all the IoCs associated to the threat actor.
  * `last_submission_date`: <*dictionaries*> the minimun (`min`), maximun (`max`) and average (`avg`) values of the last\_submission\_date of all the IoCs associated to the threat actor.
  * `files_detections`: <*dictionaries*> the minimun (`min`), maximun (`max`) and average (`avg`) values of the files\_detections of all the IoCs associated to the threat actor.
  * `urls_detections`: <*dictionaries*> the minimun (`min`), maximun (`max`) and average (`avg`) values of the urls\_detections of all the IoCs associated to the threat actor.
* `tags`: <*list of strings*> tags associated with the threat actor.
* `targeted_industries`: <*list of strings*> list of industries known to be targeted by the threat actor.
* `targeted_industries_tree`: <*list of dictionaries*> list of industries and industry groups known to be targeted by the threat actor.
  * `confidence`: <*string*> confidence on the information or the threat actor's targeted industry association.
  * `description`: <*string*> description / additional information related to the threat actor's targeted industry.
  * `first_seen`: <*integer*> the first time this targeted industry was associated with the current threat actor (UTC timestamp).
  * `industry`: <*string*> threat actor's targeted sub-industry.
  * `industry_group`: <*string*> threat actor's targeted industry group.
  * `last_seen`: <*integer*> the last time this targeted industry was associated with the current threat actor (UTC timestamp).
  * `source`: <*string*> information's supplier.
* `targeted_regions`: <*list of strings*> list of regions and countries known to be targeted by the threat actor.
* `targeted_regions_hierarchy`: <*list of dictionaries*> list of regions and countries known to be targeted by the threat actor.
  * `confidence`: <*string*> confidence on the information or the threat actor's targeted region association.
  * `country`: <*string*> threat actor's targeted country.
  * `country_iso2`: <*string*> targeted country in ISO 3166 Alpha2 - code format.
  * `description`: <*string*> description / additional information related to the threat actor's targeted region.
  * `first_seen`: <*integer*> the first time this targeted region was associated with the current threat actor (UTC timestamp).
  * `last_seen`:<*integer*> the last time this targeted region was associated with the current threat actor (UTC timestamp).
  * `region`: <*string*> threat actor's targeted region.
  * `source`: <*string*> information's supplier.
  * `sub_region`: <*string*> threat actor's targeted sub-region.
* `tlp`: <*string*> it indicates the sensitivity of the information and defines the boundaries for how and with whom the data can be shared. Available values are: `RED`, `AMBER`, `GREEN`, `CLEAR` .
* `top_icon_md5`: <*list of strings*> list of the 3 most frequent icons among the threat actor IoCs (file's icons, URLs and domain's favicons). Favicons are represented by their MD5 hash.

## relationships

In addition to the previously described attributes, threat actor objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../01-api-introduction/api-responses/introduction-relationships.md) section.

The following table shows a summary of available relationships.

| Relationship              | Return object type                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| associations              | List of all objects ([Reports](report-object.md), [Campaigns](campaign-object.md), [IoC collections](ioc-collection-object.md), [Malware families](malware-family-object.md), [Software and Toolkits](software-toolkit-object.md), [Vulnerabilities](vulnerability-object.md), [Threat Actors](threat-actor-object.md)) associated with the current threat actor, without filtering by the object type. |
| attack\_techniques        | List of MITRE ATT\&CK [techniques](object-attack-techniques.md).                                                                                                                                                                                                                                                                                                                                              |
| campaigns                 | List of associated collections of type [Campaign](campaign-object.md) objects.                                                                                                                                                                                                                                                                                                                                |
| collections               | List of associated collections of type [IoC collection](ioc-collection-object.md) objects.                                                                                                                                                                                                                                                                                                                    |
| comments                  | List of [Comments](comment-object.md).                                                                                                                                                                                                                                                                                                                                                                        |
| domains                   | List of [Domains](domains-object.md) associated with the threat actor.                                                                                                                                                                                                                                                                                                                                        |
| editors                   | List of [users](user-object.md), [groups](group-object.md) and data connectors that can edit this threat actor *(only available to the owner or editor of the entity).*                                                                                                                                                                                                                                      |
| files                     | List of [Files](file-object.md) associated with the threat actor.                                                                                                                                                                                                                                                                                                                                             |
| hunting\_rulesets         | List of curated [YARA rulesets](yara-rulesets-object.md) assigned by the entity owner.                                                                                                                                                                                                                                                                                                                        |
| ip\_addresses             | List of [IP addresses](ip-object.md) associated with the threat actor.                                                                                                                                                                                                                                                                                                                                        |
| malware\_families         | List of associated collections of type [Malware family](malware-family-object.md) objects.                                                                                                                                                                                                                                                                                                                    |
| owner                     | [User](user-object.md) who created the object.                                                                                                                                                                                                                                                                                                                                                                |
| related\_collections      | List of collection objects of type ([Reports](report-object.md), [Campaigns](campaign-object.md), [IoC collections](ioc-collection-object.md), [Malware families](malware-family-object.md), [Software and Toolkits](software-toolkit-object.md), [Vulnerabilities](vulnerability-object.md), [Threat Actors](threat-actor-object.md)) containing IoCs associated with this entity.                     |
| reports                   | List of associated collections of type [Report](report-object.md) objects.                                                                                                                                                                                                                                                                                                                                    |
| software\_toolkits        | List of associated collections of type [Software or Toolkit](software-toolkit-object.md) objects.                                                                                                                                                                                                                                                                                                             |
| suspected\_threat\_actors | List of collections of type [threat actors](threat-actor-object.md) that are suspected, not yet confirmed, to be part of the same group.                                                                                                                                                                                                                                                                      |
| threat\_actors            | List of other collections of type [threat actors](threat-actor-object.md) associated with the current threat actor.                                                                                                                                                                                                                                                                                           |
| urls                      | List of [URLs](url-object.md) associated with the threat actor.                                                                                                                                                                                                                                                                                                                                               |
| viewers                   | List of [users](user-object.md), [groups](group-object.md) and data connectors that can view the entity *(only available to the owner or editor of the entity).*                                                                                                                                                                                                                                             |
| vulnerabilities           | List of associated collections of type [Vulnerability](vulnerability-object.md) objects.                                                                                                                                                                                                                                                                                                                      |
| yara\_rulesets            | List of crowdsourced [YARA rulesets](yara-rulesets-object.md) matching at least one file associated with this threat actor.                                                                                                                                                                                                                                                                                   |

---

← [Submissions](submission-object.md) · [up](README.md) · [Threat Profile](threat-profile-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/threat-actor-object>.*
