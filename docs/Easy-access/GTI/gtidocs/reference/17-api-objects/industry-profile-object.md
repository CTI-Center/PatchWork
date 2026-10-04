---
title: "Industry Profile"
source: https://gtidocs.virustotal.com/reference/industry-profile-object
slug: industry-profile-object
section: reference
group: "API OBJECTS"
updatedAt: 2026-02-20T09:43:24.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Industry Profile

---

# industry-profile

> 🚧 Special privileges required
>
> Industry Profiles are only available to users with the Google Threat Intelligence (Google TI) Enterprise or Enterprise Plus licenses.

Industry Profiles objects provide consolidated, targeted intelligence tailored to your specific sector.

## object-attributes

An Industry Profiles object contains the following attributes:

* `collection_type`: <*string*> identifies the type of the object. For Industry Profile the value of this attribute is `industry-profile`.
* `creation_date`: <*integer*> profile object creation date (UTC timestamp).
* `last_modification_date`: <*integer*> UTC timestamp of the last time the profile was updated (refreshed quarterly).
* `name`: <*string*> profile's name which includes the targeted industry name.
* `analyst_observed_activity`: <*string*> AI-synthesized intelligence based on curated data and proprietary findings from the Global Threat Intelligence Group (GTIG) regarding the target industry.
* `osint_summary`: <*string*> AI-synthesized summaries of high-relevance Open Source Intelligence (OSINT) regarding the target industry.
* `threat_activity_drivers`: <*string*> AI-summarized insights into geopolitical, technological, or economic factors among others, that are currently shaping and motivating threat activity against the target industry.
* `origin`: <*string*> identifies the entity responsible for creating the object (**Google Threat Intelligence**).
* `source_regions_hierarchy`: <*list of dictionaries*> list of countries where threat activity against the target industry originated.
  * `confidence`: <*string*> level of confidence in the identified source region targeting the profile industry.
  * `country`: <*string*> country where the threat activity targeting the profile industry originated.
  * `region`: <*string*> region where the threat activity targeting the profile industry originated.
  * `sub_region`: <*string*> sub-region where the threat activity targeting the profile industry originated.
  * `country_iso2`: <*string*> two-letter ISO 3166-1 alpha-2 code of the country where the threat activity targeting the profile industry originated.
  * `description`: <*string*> description / additional information related to the threat activity.
  * `first_seen`: <*integer*> UTC timestamp of the first recorded threat activity originating from the source country against the target industry.
  * `last_seen`:<*integer*> UTC timestamp of the last recorded threat activity originating from the source country against the target industry.
  * `source`: <*string*> information's supplier.
* `targeted_regions`: <*list of strings*> a list containing the two-letter ISO 3166-1 alpha-2 code of the countries and the name of the region targeted by the threat activity.
* `targeted_industries`: <*list of strings*> a single-entry list containing the name of the industry targeted by the threat activity.
* `profile_stats`: <*dictionary of dictionaries*> statistical data used to populate charts representing the current threat landscape for the target industry.
  * `source_region_heatmap`: <*dictionary*> dictionary containing a `data` list that maps ISO 3166-1 alpha-2 country codes to the total number of recorded campaigns originating from each.
  * `top_targeted_geographies`: <*dictionaries*> dictionary containing a `data` list showing the distribution of targeted countries, expressed as a percentage of the total targeted set.
  * `top_source_regions`: <*dictionaries*> dictionary containing a `data` list of records representing the top countries of origin for recent threat activity, along with the specific actors and motivations identified for those attacks. Each record consists of four specific data points:
    * The source region of the threat activity
    * The timestamp of the threat activity
    * The threat actor performing the activity
    * Motivation behind the threat activity
  * `top_espionage_malware`: <*dictionaries*> dictionary containing a `data` list mapping malware family names to their observation frequency within espionage campaigns targeting the profile industry.
  * `top_threat_actors_on_campaigns`: <*dictionaries*> dictionary containing a `data` list mapping threat actors to their observation frequency within campaigns targeting the profile industry.
  * `top_threat_actors_motivations`: <*dictionaries*> dictionary containing a `data` list that provides the frequency of identified threat actor motivations across all campaigns targeting the profile industry.
  * `top_vulnerabilities`: <*dictionaries*> dictionary containing a `data` list that maps specific vulnerabilities to the frequency of their exploitation in campaigns targeting the profile country.
  * `cyber_threat_score`: <*dictionaries*> dictionary containing a `data` object that provides a risk assessment across three threat categories: **STATE** (state-sponsored), **IO/HACK** (hacktivism), and **FIN** (financial). It includes Frequency and Magnitude metrics for each type within the target industry.

<br />

---

← [Hunting Rulesets](hunting-ruleset-object.md) · [up](README.md) · [IoC Collection](ioc-collection-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/industry-profile-object>.*
