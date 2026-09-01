---
title: "Migrate from VirusTotal"
source: https://gtidocs.virustotal.com/docs/migrate-from-virustotal
slug: migrate-from-virustotal
section: guides
group: "Integrations"
updatedAt: 2026-02-26T16:13:11.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [Integrations](README.md) › Migrate from VirusTotal

---

# migrate-from-virustotal

How to move from VirusTotal integrations to the Google Threat Intelligence ones.

This migration guide assumes that you are already familiar with using VirusTotal integrations. If you're not, please refer to the table below to access the relevant documentation for each Google Threat Intelligence integration.

Equivalent integrations:

| VirusTotal                                                                                                                                                                                                                                      | Google Threat Intelligence                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [VT4Splunk](https://splunkbase.splunk.com/app/6654)                                                                                                                                                                                             | [Google Threat Intelligence for Splunk](https://splunkbase.splunk.com/app/7351)                                                                          |
| [Cortex XSOAR VirusTotal (API v3)](https://xsoar.pan.dev/docs/reference/integrations/virus-total-api-v3)                                                                                                                                        | [Cortex XSOAR Google Threat Intelligence](https://xsoar.pan.dev/docs/reference/integrations/google-threat-intelligence)                                  |
| [Cortex XSOAR VirusTotal Livehunt Feed](https://xsoar.pan.dev/docs/reference/integrations/virus-total-livehunt-feed) and [Cortex XSOAR VirusTotal Retrohunt Feed](https://xsoar.pan.dev/docs/reference/integrations/virus-total-retrohunt-feed) | [Cortex XSOAR Google Threat Intelligence IoC Stream Feed](https://xsoar.pan.dev/docs/reference/integrations/google-threat-intelligence-io-c-stream-feed) |
| [MISP VirusTotal](https://misp.github.io/misp-modules/expansion/#virustotal)                                                                                                                                                                    | [MISP Google Threat Intelligence](https://misp.github.io/misp-modules/expansion/#google_threat_intelligence)                                             |

<br />

### google-threat-intelligence-for-splunk

This add-on has been designed to mimic the behavior of VT4Splunk as closely as possible to facilitate migration from it. Below are described *the most significative differences* from the VirusTotal integration.

Check out the complete Splunk integration guide [here](gti4splunk-guide.md).

#### commands

The main enrichment command is called **gti** (former vt4splunk) and it can be used in the same way as in the VT integration. [Refer to the add-on documentation to learn more](https://splunkbase.splunk.com/app/7351).

The commands *vtdeleteiocs*, *vtadversaryupdate*, *vtmitreupdate* are now called **gtideleteiocs**, **gtiadversaryupdate**, **gtimitreupdate**.

#### dashboards

1 - Threat Intelligence

You can retrieve the GTI assessment (threat score, verdict, and severity) for each IoC. Additionally, you can drill down by the GTI verdict by clicking on the new pie chart.

![Integrations Pie Chart](https://storage.googleapis.com/gtidocresources/guides/integrations/images/integrations_piechart_20241031.png)

2 - Adversary Intelligence

You can select the origin of the collections, in VT4SPlunk the collections showed in this dashboard are solely provided by the community. In this add-on you receive additional **curated** collections from Partners and Google Threat Intelligence teams as Mandiant.

![Integrations Select Origin](https://storage.googleapis.com/gtidocresources/guides/integrations/images/integrations_selectorigin_20241031.png)

### google-threat-intelligence-for-cortex-xsoar

This pack has been designed to mimic the behavior of the VirusTotal (API v3) integration as closely as possible, making migration from it seamless. All commands available in the VirusTotal integration are included here with a new prefix, but their functionality remains unchanged:

* gti-comments-add
* gti-file-scan-upload-url
* gti-comments-delete
* gti-comments-get
* gti-comments-get-by-id
* gti-search
* gti-file-sandbox-report
* gti-passive-dns-data
* gti-analysis-get
* gti-file-sigma-analysis
* gti-privatescanning-file
* gti-privatescanning-file-scan
* gti-privatescanning-analysis-get
* gti-url-scan-and-analysis-get
* gti-file-scan-and-analysis-get
* gti-private-file-scan-and-analysis-get

In addition, we've included a new command, **gti-assessment-get**, which retrieves the GTI assessment (threat score, verdict, and severity) for a given entity. This information is also included in the responses of the **file**, **url**, **ip**, and **domain** commands provided by the integration.

We've also added commands to retrieve curated information for a given entity:

* gti-curated-malware-families-get
* gti-curated-campaigns-get
* gti-curated-threat-actors-get

<br />

### google-threat-intelligence-ioc-stream-feed-for-cortex-xsoar

This new package provides the functionality of our IoC Stream, which includes the former VirusTotal Livehunt Feed and VirusTotal Retrohunt Feed. It allows you to obtain IoCs from our IoC Stream. This integration incorporates two new arguments: a limit, to constrain the number of IoCs, and a filter, to refine your search. The latter allows you to achieve the functionality of the old Livehunt and Retrohunt, filtering by hunting\_ruleset and retrohunt\_job, respectively. To use this integration, you only need to use the following command:

* gti-iocstream-get-indicators

### google-threat-intelligence-for-misp

This expansion module complements the VirusTotal one rather than replacing it. It allows you to enrich IoCs found in MISP event attributes (similar to the VirusTotal module) with Google TI assessments (threat score, verdict, and severity). If you still require VirusTotal engine verdicts, please use both modules together.

---

← [Digital Threat Monitoring User Roles](../12-dtm/dtm-user-roles.md) · [up](README.md) · [List of Google TI Integrations](technology-integrations-list.md) →

*Archived from <https://gtidocs.virustotal.com/docs/migrate-from-virustotal>.*
