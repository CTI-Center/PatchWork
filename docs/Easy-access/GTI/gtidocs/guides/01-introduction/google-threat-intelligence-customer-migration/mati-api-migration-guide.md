---
title: "Google Threat Intelligence - API Migration guide for Mandiant Advantage former users"
source: https://gtidocs.virustotal.com/docs/mati-api-migration-guide
slug: mati-api-migration-guide
section: guides
group: "Introduction"
updatedAt: 2025-11-28T16:03:22.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [Introduction](../README.md) › [Google Threat Intelligence Customer Migration](../google-threat-intelligence-customer-migration.md) › Google Threat Intelligence - API Migration guide for Mandiant Advantage former users

---

# google-threat-intelligence---api-migration-guide-for-mandiant-advantage-former-users

This guide serves as a follow-up to the **[Google Threat Intelligence Migration Guide for former Mandiant users](mati-migration-guide.md)**. It's designed to help users transition from the Mandiant Advantage API to the Google Threat Intelligence (Google TI) API. Please consider this an additional resource alongside the [official API documentation](https://gtidocs.readme.io/reference/).

Building on that foundation, developers can leverage the comprehensive suite of Google TI [API v3](https://gtidocs.readme.io/reference/) endpoints for building custom integrations. These powerful endpoints provide access to an extensive range of tools, features, and functionalities that mirror those available in the web interface, all accessible under a single, globally used server URL: `www.virustotal.com/api/v3/`.

In the following sections, we'll cover key aspects of migrating to Google Threat Intelligence. We'll specifically address:

* **API authentication methods**
* **API URL and paths mapping** to the Google TI API:
  * Mandiant's **Digital Threat Management (DTM)**
  * Mandiant's **Attack Surface Management (ASM)**
  * Mandiant's **Threat Intelligence API**

Finally we'll take a deep dive into the Threat Intelligence module itself. This section will highlight several key differences and new concepts, and introduce Google TI tools the reader might not be familiar with yet.

> 🚧 Skipping introductory content
>
> If you'd like to skip the introductory content, you can jump straight to the **Threat Intelligence API Endpoints Mapping** section **[here](#threat-intelligence-api-endpoints-mapping)**!

# api-authentication

Unlike Mandiant, which typically offers both Bearer Token Authentication and Basic Authentication, Google TI primarily uses **API keys** for authentication. Any endpoints that support additional authentication methods will explicitly indicate it in their specific documentation.

Each Google TI user has its own unique API key, but service accounts were specifically designed for automation tasks. They are not tied to individual users, do not require an email address for creation, and provide API authentication solely via API keys accessible only to group administrators, and only administrators can create them.

## api-key

**Users** can access their individual API key [on the platform](https://www.virustotal.com/gui/home/) by navigating to the **API key** option in either the **left navigation menu bar** or the **top-right User menu**:

<div class="row">
  <div class="column" style={{ width: "44%" }} align="left">
    ![](https://storage.googleapis.com/gtidocresources/guides/introduction/images/api_key_2_20240715.png) API key option" />
  </div>

  <div class="column" style={{ width: "2%" }} align="center" />

  <div class="column" style={{ width: "44%" }} align="right">
    ![](https://storage.googleapis.com/gtidocresources/guides/introduction/images/api_key_1_20240715.png) API key option" />
  </div>

</div>

Administrators can access service accounts' API keys [on the platform](https://www.virustotal.com/gui/home/) by navigating to the **top-right User menu**, selecting **My Group** option, and then heading to the **USERS** tab. Within the **Service accounts** section, they'll find dedicated buttons to view and copy each service account's API key.

 My Group option -> USERS tab -> Service accounts section" border={false} caption="User menu -> My Group option -> USERS tab -> Service accounts section" src="https://storage.googleapis.com/gtidocresources/guides/group-management/images/gti_1.3.3_service_account_api_key_20240606.png" width="900px" />

# api-url-&-paths-segments-mapping

When migrating to Google TI, in addition to the authentication method, the other most critical change is the update to API server URLs and their corresponding paths. While much of the core functionality from Mandiant's modules remains, specifically for ASM and DTM, the access points have been consolidated and streamlined under the Google TI umbrella.

The table below provides a clear mapping of the base URLs and initial path segments from Mandiant's core modules (ASM, DTM, and the Threat Intelligence module) to their equivalents within the new Google TI API.

| Service                  | Mandiant Advantage Base URL + path       | Google TI Base URL + path        |
| ------------------------ | ---------------------------------------- | -------------------------------- |
| (\*) Threat Intelligence | `api.intelligence.mandiant.com/v4/`      | `www.virustotal.com/api/v3/`     |
| DTM                      | `api.intelligence.mandiant.com/v4/dtm/`  | `www.virustotal.com/api/v3/dtm/` |
| ASM                      | `asm-api.advantage.mandiant.com/api/v1/` | `www.virustotal.com/api/v3/asm/` |

(\*) The next section of this document details the equivalent Threat Intelligence endpoints and highlights other differences and concepts to take into account when migrating.

# digital-threat-monitoring-(dtm)-\&attack-surface-management-(asm)

When transitioning from Mandiant to Google TI, the core functionality and structure of the Digital Threat Management (DTM) and Attack Surface Management (ASM) APIs largely remain the same. The primary difference lies in their server URLs and the initial segments of their paths as shown in the previous table. Please refer to the Google TI documentation for:

* **[Digital Threat Monitoring (DTM)](https://gtidocs.readme.io/reference/dtm-pagination)**
* **[Attack Surface Management (ASM)](https://gtidocs.readme.io/reference/get_projects)**

# threat-intelligence-api

Before we dive into the Threat Intelligence endpoints, it's helpful to first understand some key Google TI concepts and differences between Mandiant Threat Intelligence API and Google TI API specifically.

## google-ti-api-objects

It's important to note that while Google TI provides all information found in Mandiant API objects (and more), the JSON response objects have different structures. The following list shows the most popular objects and links to their respective documentation, where their JSON structure is defined:

* **Indicators of Compromise**
  * [File](https://gtidocs.readme.io/reference/file-object)
    * Additionally, files can present a Sandbox analysis report represented by the [File Behaviour object](https://gtidocs.readme.io/reference/file-behaviour-summary-object).
  * [URL](https://gtidocs.readme.io/reference/url-object)
  * [Domain](https://gtidocs.readme.io/reference/domains-object)
  * [IP address](https://gtidocs.readme.io/reference/ip-object)

* **Threat Intelligence objects**: note that these objects include the `origin` attribute which identifies the source of the data for their attributes. **Google Threat Intelligence** `origin` refers to objects whose information was checked and validated by the Mandiant analysts, **Partner** `origin` refers to the objects coming from our trusted external partners and **Crowdsourced** `origin` refers to objects created by the rest of the community.
  * [Threat Actor](https://gtidocs.readme.io/reference/threat-actor-object)
  * The Mandiant Malware object equivalent in Google TI is conceptually split into two objects: [Malware Family](https://gtidocs.readme.io/reference/malware-family-object) and [Software and Toolkit](https://gtidocs.readme.io/reference/software-toolkit-object)
  * [Campaign](https://gtidocs.readme.io/reference/campaign-object)
  * [**IoC collections**](https://gtidocs.readme.io/reference/ioc-collection-object): although not present in Mandiant, it plays a crucial role in Google TI through its ability to aggregate, enrich, and distribute indicators of compromise from the community in real time.
  * [Report](https://gtidocs.readme.io/reference/report-object)
  * [Vulnerability](https://gtidocs.readme.io/reference/vulnerability-object)

While these are some of the frequently encountered objects, Google TI offers a more extensive range of object types. For a comprehensive definition of all available objects and their structures, please refer to the [API Objects documentation](https://gtidocs.readme.io/reference/analyses-object).

## google-ti-relationships-endpoints

[Most objects](#google-ti-api-objects) in the documentation include a **Relationships** section. Values in this section can be used, along with the specific object `id`, to retrieve additional related or associated objects as documented [here](https://gtidocs.readme.io/reference/introduction-relationships):

* `/api/v3/{collection name}/{object id}?relationships={relationship}` - returns one relationship objects' descriptors, which include only the most relevant attributes of the related objects such as their `type`, `id` and `links` to retrieve the complete objects.
* `/api/v3/{collection name}/{object id}?relationships={relationship1},{relationship2}` - returns several relationships objects' descriptors , which include only the most relevant attributes of the related objects such as their `type`, `id` and `links` to retrieve the complete objects.
* `/api/v3/{collection name}/{object id}/{relationship}` - returns one relationship complete objects, not only their descriptors.

`{collection name}` can be one of the following: `files`, `urls`, `domains`, `ip_addresses`, `domains`, `ip_addresses` or `collections` for all ***Threat Intelligence objects*** such as Threat Actors, Campaigns, Reports, Vulnerabilities, etc.

## additional-observations

* **Pagination**: Mandiant does pagination through the `next` field of the JSON response, while Google TI does it via `links` -> `next` field.

| Mandiant Advantage Threat Intelligence | Google TI |
| --- | --- |
| ```json<br>{<br>"next": "next URL value"<br>}<br>``` | ```json<br>{<br>"links": {<br>"self": "current URL",<br>"next": "next URL value"<br>}<br>}<br>``` |

* **Indicators of Compromise**: here are the differences in how indicator types are named in their respective JSON responses

| Mandiant Advantage Threat Intelligence | Google TI |
| --- | --- |
| "type": "ipv4" | "type": "ip\_address" |
| "type": "md5" | "type": "file" |
| "type": "fqdn" | "type": "domain" |
| "type": "url" | "type": "url" |

* **Set of objects**: while Mandiant's API separates different object types into distinct JSON response fields (`threat-actors`, `campaigns`, `malware`, `vulnerability`, `objects` for reports, and `indicators`), Google TI is consistent and simplifies this by grouping all objects under a single `data` field. The specific object type is then identified by the `type` attribute for indicators or the `collection_type` attribute for other ***Threat Intelligence*** objects.

| Mandiant Advantage Threat Intelligence | Google TI |
| --- | --- |
| ```json<br>{<br>"threat-actors": [...]<br>}<br>``` | ```json<br>{<br>…<br>"data": [<br>{<br>"type": "collection",<br>"collection_type":"threat_actor"<br>}<br>]<br>}<br>``` |

* **HTTP POST method**: In Google TI the **POST** method is reserved to send data to the platform, such as creating new IoC Collections, building Threat Graphs, adding community comments to objects cards and more. All requests for retrieving information from our databases require the **GET** method.
* **Object identifiers**: in Google TI, Threat Intelligence objects (including Actors, Malware, Tools, Campaigns, IoC Collections, Vulnerabilities, and Reports) and IoCs are consistently identified in API JSON responses by the `id` attribute. Same `id` values are displayed on the browser URL when opening any object card or IoC report.

| IoC | ID value |
| --- | --- |
| File | (`*`) Sha256 hash |
| URL | Check here <a href="urls#url-identifiers">URL `id` representation</a> |
| Domain | Domain name |
| IP address | IP address |

(\*) While SHA256 is the primary identifier for files, MD5 and SHA1 hashes can also be used for unique identification. Please note that files integrated from Mandiant without provided binary content can only be searched using their MD5 hash, not SHA256.

* **[Google TI score](../../06-ioc-investigation/google-threat-intelligence-indicator-score.md)**: endpoints that can provide the Google TI assessment of an object require the `x-tool` header to do so. This header must specify the tool or service that will be consuming our data. Without this header, the Google TI score will not be returned.

```json
headers = {
   "accept": "application/json",
   "x-apikey": "your API key",
   "X-tool":"SIEM custom integration"
}
```

---

← [Google Threat Intelligence - Migration guide for Mandiant Advantage former users](mati-migration-guide.md) · [up](../README.md) · [Contributors](../contributors.md) →

*Archived from <https://gtidocs.virustotal.com/docs/mati-api-migration-guide>.*
