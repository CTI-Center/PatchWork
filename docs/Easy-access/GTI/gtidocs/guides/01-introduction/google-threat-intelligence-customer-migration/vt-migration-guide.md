---
title: "Google Threat Intelligence - Migration guide for VirusTotal former users"
source: https://gtidocs.virustotal.com/docs/vt-migration-guide
slug: vt-migration-guide
section: guides
group: "Introduction"
updatedAt: 2026-06-29T10:32:41.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [Introduction](../README.md) › [Google Threat Intelligence Customer Migration](../google-threat-intelligence-customer-migration.md) › Google Threat Intelligence - Migration guide for VirusTotal former users

---

# google-threat-intelligence---migration-guide-for-virustotal-former-users

This guide is designed to help VirusTotal users seamlessly transition to and effectively utilize the new Google Threat Intelligence platform.

Former VirusTotal users can continue to use all of VirusTotal's familiar capabilities, now enhanced with Mandiant's curated threat intelligence and Google's unparalleled threat visibility. By combining Mandiant's frontline expertise and analyst insights, we're adding rich depth to VirusTotal's existing knowledge, helping users make smarter, more reliable decisions.

For former Mandiant Advantage users, we've developed a dedicated migration guide available [here](mati-migration-guide.md).

# get-started

You can find [here](https://gtidocs.readme.io/docs/google-threat-intelligence-provisioning-guide) the provisioning process with all details on each step and all information required for closing the contract. Our provisioning team will support you during the  entire process.

Retaining your existing **VirusTotal group Token** in your Google Threat Intelligence account is essential for a seamless transition and uninterrupted access to your data and configurations.

By doing so, all your configurations and settings from VirusTotal accounts will remain intact and accessible within Google Threat Intelligence, and users will be upgraded to Google TI with the same access level as regular users or "**Members**" and administrators or "**Admins**".

This will ensure service continuity and access to your previously created:

<div class="row">
  <div class="column" style={{ width: "50%" }}>
    <ul>
      <li><a href="https://www.virustotal.com/gui/hunting/rulesets?order=modification_date-" target="_blank">Livehunt rules</a></li>
      <li><a href="https://www.virustotal.com/gui/hunting/retrohunt" target="_blank">Retrohunt rules</a></li>
      <li><a href="https://www.virustotal.com/gui/user/{user_id}/subscriptions" target="_blank">Threat Actors subscriptions (`*`)</a></li>
      <li><a href="https://www.virustotal.com/gui/user/{user_id}/subscriptions" target="_blank">IoC Collections subscriptions (`*`)</a></li>
      <li><a href="https://www.virustotal.com/gui/ioc-notifications?order=date-" target="_blank">IoC Stream notifications</a></li>
      <li><a href="https://www.virustotal.com/gui/graphs?scope=user" target="_blank">Threat Graphs</a></li>
      <li><a href="https://www.virustotal.com/gui/diffs" target="_blank">Diffs</a></li>
    </ul>
  </div>

  <div class="column" style={{ width: "50%" }}>
    <ul>
      <li><a href="https://www.virustotal.com/gui/user/{user_id}/collections" target="_blank">IoC collections (`*`)</a></li>
      <li><a href="https://www.virustotal.com/gui/private-scanning/analyses?filter=item_type%25253Afile" target="_blank">Private files analyses</a></li>
      <li><a href="https://www.virustotal.com/gui/private-scanning/analyses?filter=item_type%25253Aurl" target="_blank">Private URLs analyses</a></li>
      <li><a href="https://www.virustotal.com/gui/user/{user_id}/comments" target="_blank">Comments (`*`)</a></li>
      <li><a href="https://www.virustotal.com/gui/group/{group_id}" target="_blank">Service accounts (`*`)</a></li>
      <li><a href="https://www.virustotal.com/gui/user/{user_id}/apikey" target="_blank">API keys (`*`)</a></li>
    </ul>
  </div>
</div>

(\*) Replace \{user\_id} and \{group\_id} (or %7Buser\_id%7D and %7Bgroup\_id%7D) in the links by your values.

# google-threat-intelligence-tools

Google Threat Intelligence integrates the power of VirusTotal's community-driven data with Mandiant Advantage Threat Intelligence's curated insights, all enhanced by Google's unparalleled visibility.

Depending on your Google Threat Intelligence subscription, you can access these resources through the new left [navigation menu](../google-threat-intelligence-navigation.md), where some of the tools and services are grouped by different topics for effortless exploration and navigation:

![](https://storage.googleapis.com/gtidocresources/guides/introduction/images/menu_tools_groups_20250620.png)

The table below enumerates the UI tools available within Google Threat Intelligence.This presentation highlights which capabilities will be familiar from your VirusTotal experience and which are new additions designed to expand your threat intelligence resources.

<div style={{ overflowX: 'auto', width: '100%' }}>
  
| Module | Tool | Status for VT Users | Description |
| --- | --- | --- | --- |
| <b>Threat Landscape</b> | <a href="../../05-global-landscape/manage-threat-profiles.md" target="_blank"><b>Manage Threat Profiles</b></a> | New Capability in Google TI | Personalized, dynamic lens that filters curated <b>Google Threat Intelligence</b>'s vast data to highlight threats most relevant to your organization, based on your own custom criteria. |
| <a href="../../05-global-landscape/threat-actors-card.md" target="_blank"><b>Threat Actors</b></a> | Familiar from VirusTotal | Highly contextualized Threat Actors cards providing curated details verified by <b>Google Threat Intelligence</b> analysts and our community <b>Partners</b>. |  |
| <a href="../../05-global-landscape/malware-tools.md" target="_blank"><b>Malware & Tools</b></a> | Familiar from VirusTotal | Rich, contextualized details on Malware families and Toolkits, powered by <b>Google Threat Intelligence</b> analysts and our community <b>Partners</b>. |  |
| <a href="../../05-global-landscape/campaigns.md" target="_blank"><b>Campaigns</b></a> | Familiar from VirusTotal | Curated intelligence on malware Campaigns continuously monitored by our <b>Google Threat Intelligence</b> analysts. |  |
| <a href="../../05-global-landscape/ioc-collections.md" target="_blank"><b>IoC Collections</b></a> | Familiar from VirusTotal | Live reports of indicators of compromise. Our <b>Google Threat Intelligence</b> analysts create them, as do our community <b>Partners</b> who track indicators in malicious campaigns. We also incorporate <b>Crowdsourced</b> threats observed by the wider community as Open Source Intelligence (OSINT). |  |
| <a href="../../05-global-landscape/ttp-analysis.md" target="_blank"><b>TTP Analysis</b></a> | New Capability in Google TI | Powerful tool for exploring and analyzing threat objects, vulnerabilities, and reports, from the perspective of aligning the malicious activity represented  by them against the MITRE ATT\&CK framework. |  |
| <b>IoC Investigation</b> | <a href="../../06-ioc-investigation/check-vt.md" target="_blank"><b>Check with VirusTotal</b> (\*)</a> | Familiar from VirusTotal | Evolving from VirusTotal Intelligence, this tool serves as a robust <b>IoC search engine</b> for querying based on specific criteria and for uploading files for analysis. Additionally, its advanced <b>semantic search</b> goes beyond just IoC lists, delivering a broader spectrum of threat intelligence including Threats, Reports, Vulnerabilities, Rules, Graphs, and valuable community Comments. |
| <a href="../../06-ioc-investigation/livehunt-guide.md" target="_blank"><b>Livehunt</b></a> | Familiar from VirusTotal | Constantly running <b>YARA rulesets jobs</b>, which analyze new IoCs submitted to the platform and generate notifications on IoCs that match the implemented conditions (search in the future). |  |
| <a href="../../06-ioc-investigation/retrohunt-guide.md" target="_blank"><b>Retrohunt</b></a> | Familiar from VirusTotal | <b>YARA rulesets</b> running against our extensive file database to pinpoint files that satisfy the rule's conditions (search in the past). |  |
| <a href="../../06-ioc-investigation/ioc-stream-guide.md" target="_blank"><b>IoC Stream</b></a> | Familiar from VirusTotal | The <b>centralized notifications hub</b> for Livehunt and Retrohunt matches, Threat Intelligence objects subscriptions and Managed Threat Profiles. |  |
| <a href="../../06-ioc-investigation/diff.md" target="_blank"><b>Diff</b></a> | Familiar from VirusTotal | The assistant for creating files-based Yara rules. |  |
|  | <a href="../../07-report-analysis/reports-and-analysis.md#2.-reports-cards" target="_blank"><b>Reports & Analysis</b></a> | Familiar from VirusTotal | Curated reports from <b>Google Threat Intelligence</b> analysts or community <b>Partners</b> as well as <b>Crowdsourced</b> reports from the rest of the community. |
| <a href="../../08-threat-graph/get-started-threat-graph.md" target="_blank"><b>Threat Graph</b></a> | Familiar from VirusTotal | Previously known as <b>VT Graph</b>, a tool for visually exploring relations between Indicators. |  |
| <a href="../../09-private-scanning/private-scanning.md" target="_blank"><b>Private Scanning</b></a> | Familiar from VirusTotal | VirusTotal Private Scanning for files and URLs that cannot be shared with the rest of the community. |  |
| <a href="../../10-vulnerability-intelligence/explore-vulnerabilities.md" target="_blank"><b>Vulnerability Intelligence</b></a> | New Capability in Google TI | A <b>curated database</b> providing actionable insights to prioritize and implement effective security fixes. |  |
| <a href="../../11-asm/get-started-asm.md" target="_blank"><b>Attack Surface Management</b></a> | New Capability in Google TI | <b>ASM</b> for assets and issues discovery. |  |
| <b>Digital Threat Monitoring</b> | <a href="../../12-dtm/get-started-dtm.md" target="_blank"><b>Digital Threat Monitoring</b></a> | New Capability in Google TI | <b>DTM</b> to ​​explore open-source and dark web data. |

</div>

> 🚧
>
> (*) Google Threat Intelligence introduces a new Indicator Score for IoCs (files, URLs, domains, IP addresses). This [**Google Threat Intelligence Indicator Score**](../../06-ioc-investigation/google-threat-intelligence-indicator-score.md) helps SecOps teams prioritize the most significant threats by evaluating various factors within the indicators' reports.

![](https://storage.googleapis.com/gtidocresources/guides/introduction/images/gti_score_20240711.png)

# integrations-and-automations-with-google-threat-intelligence-api

Already existing custom integrations or API automated processes won't be impacted.

New API endpoints have been introduced to cover all recently added features listed in the "[Google Threat Intelligence tools](#google-threat-intelligence-tools)" section. For detailed information, refer to the complete official [API v3 documentation](https://gtidocs.readme.io/reference/).

Moreover, the **`gti_assessment`** field is integrated into all IoCs' ([files](https://gtidocs.readme.io/reference/file-object), [URLs](https://gtidocs.readme.io/reference/url-object), [domains](https://gtidocs.readme.io/reference/domains-object), [IP addresses](https://gtidocs.readme.io/reference/ip-object)) reports. To leverage this new parameter in your automations, simply access it via the usual API endpoints:

* [Get a file report](https://gtidocs.readme.io/reference/file-info) - `/files/{id}`
* [Get a domain report](https://gtidocs.readme.io/reference/domain-info) - `/domains/{domain}`
* [Get a URL analysis report](https://gtidocs.readme.io/reference/url-info) - `/urls/{id}`
* [Get an IP address report](https://gtidocs.readme.io/reference/ip-info) - `/ip_addresses/{ip}`

> 🚧 gti\_assessment requires x-tool header
>
> To get the **gti\_assessment** attribute in the JSON response, ensure that the **x-tool header** is added to the request headers. This header should be used to identify your tool or service with a custom name.

Here's an example of retrieving the Google Threat Intelligence score (gti\_assessment) from a particular file:

```json
import os
from pprint import pprint
import requests

FILE_SHA256_HASH = '7203e2e674817c3cc2080d810a2e09323100163a1bd8f8d4ffbf5b9b1729b9c1'

def get_file_gti_score(file_hash):
 url = f'https://www.virustotal.com/api/v3/files/{file_hash}'
 headers = {
   'Accept': 'application/json',
   'x-apikey': os.environ['VT_APIKEY'],
   'x-tool': 'MyToolOrServiceName',
 }
 res = requests.get(url, headers=headers)
 res.raise_for_status()
 return res.json()['data']['attributes'].get('gti_assessment',None)

file_gti_score = get_file_gti_score(FILE_SHA256_HASH)
pprint(file_gti_score)
```

## new-api-only-tools

**Categorized Threat Lists**: Google TI includes API data streams that provide curated and categorized Indicators of Compromise (IoCs). While these feeds are pre-filtered by certain criteria and categories, they also include additional filters for an extra layer of user customization. For more details, refer to the API documentation section [here](https://gtidocs.readme.io/reference/get-latest-threat-list).

# out-of-the-box-third-party-integrations

Already existing out-of-the-box (OOTB) integrations won't be impacted.

While we are actively developing new integrations for Google Threat Intelligence, you can access the list of available ones not only from the [INTEGRATION](../../13-integrations/migrate-from-virustotal.md) dedicated section on our documentation portal but also from the [Technology Integration](https://www.virustotal.com/gui/technology-integrations) left navigation menu option, where you can easily identify the integrations that are "*compatible with Google Threat Intelligence*".

![](https://storage.googleapis.com/gtidocresources/guides/introduction/images/ootb_integrations_20250620.png)

> 🚧
>
> We strongly advise prioritizing the migration to Google Threat Intelligence integrations to ensure all your events benefit from Google Threat Intelligence's rich threat context. Check out our extended [**OOTB Migrate from VirusTotal**](../../13-integrations/migrate-from-virustotal.md) guide which will incorporate every new integration.

# official-documentation-portal

Explore our [documentation portal](https://gtidocs.readme.io/docs/) to discover everything you need to know about Google Threat Intelligence. You'll find in-depth information on features and services, plus helpful guides and walkthroughs to accelerate your learning journey.

To automate your workflows, we've compiled a comprehensive list of all [API v3](https://gtidocs.readme.io/reference/) endpoints, each with detailed descriptions to help you get started.

Stay informed on the latest platform updates in our [Release Notes](/changelog) and discover our new webinars and relevant blog posts announced through our **In-app** notification tool.

Continue to ask for platform technical support on our Google Threat Intelligence [contact portal](https://www.virustotal.com/gui/contact-us/), and if you need immediate assistance for an incident from here you can contact our Incident Response Team which will be happy to help you.

![](https://storage.googleapis.com/gtidocresources/guides/introduction/images/contact_form_20240711.png)

---

← [Google Threat Intelligence Customer Migration](../google-threat-intelligence-customer-migration.md) · [up](../README.md) · [Google Threat Intelligence - Migration guide for Mandiant Advantage former users](mati-migration-guide.md) →

*Archived from <https://gtidocs.virustotal.com/docs/vt-migration-guide>.*
