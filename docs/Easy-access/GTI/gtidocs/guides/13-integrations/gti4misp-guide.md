---
title: "MISP integration guide"
source: https://gtidocs.virustotal.com/docs/gti4misp-guide
slug: gti4misp-guide
section: guides
group: "Integrations"
updatedAt: 2025-09-25T17:21:05.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [Integrations](README.md) › MISP integration guide

---

# misp-integration-guide

This guide provides comprehensive, step-by-step instructions for integrating the Google Threat Intelligence (Google TI) data with your *Malware Information Sharing Platform* (MISP) instance.

This integration allows for the **automated enrichment of indicators of compromise within MISP**, leveraging the high-fidelity, contextualized threat data provided by Google Threat Intelligence.

By following this guide, you will enable your MISP instance to query Google TI for intelligence to enrich specific attributes (file hashes, domains, urls and IP addresses), and seamlessly import the results as structured MISP objects. This enhances the analytical value of your data and streamlines threat investigation workflows.

For any issues related to Google TI integration setup, please contact our support team [here](https://www.virustotal.com/gui/contact-us/technical-support).

**Table of contents**

* [1. Benefits](#1-benefits)
* [2. Prerequisites](#2-prerequisites)
* [3. Configuration](#3-configuration)
* [4. Using the Enrichment Module](#4-using-the-enrichment-module)
  * [4.1. Individual attribute enrichment](#41-individual-attribute-enrichment)
  * [4.2. Event-Level enrichment](#42-event-level-enrichment)
* [Annex I: Enriched data in MISP events](#annex-i-enriched-data-in-misp-events)

# 1.-benefits

Integrating Google TI with MISP automates your threat intelligence workflow, making it significantly faster and more powerful. Some examples are:

**Automated Enrichment and Accelerated Triage**: this integration will automatically enrich indicators (file hashes, domains, urls and IP addresses) with Google TI vast dataset. This provides immediate context like Google TI verdict and score, antivirus detection ratios and behavioral analysis, enabling your team to assess threats and make decisions in a fraction of the time.

**Expanded Investigations and Infrastructure Discovery**: empower your analysts to move beyond single data points. The integration allows them to **pivot** seamlessly from one indicator to related artifacts. This capability is crucial for **expanding investigations** to uncover an adversary's entire operational infrastructure.

**Creation of a Correlated Intelligence Graph**: use the newly discovered indicators to **create new relationships** directly within your MISP events. By mapping out how these indicators are interconnected, you can transform a flat list of IOCs into a structured, interconnected graph of an entire attack campaign, making your threat data significantly more valuable and actionable.

# 2.-prerequisites

Before proceeding, ensure the following requirements are met. Failure to meet these prerequisites is the most common source of operational issues.

* **`misp-modules`** service must be installed, configured, and running on your MISP server. If it is not yet installed in MISP, please refer to the official MISP Modules installation [documentation](https://github.com/MISP/misp-modules).
* **MISP Administrator Privileges**: you must have **administrator-level access** to your MISP instance to access *server settings* and *manage plugins*.
* **Google TI API Key**: a valid API key is required to authenticate with the Google TI service. It is strongly recommended to use a [service account](../02-group-management/admins-guide.md#1.3.-service-accounts-management) API key rather than a key tied to an individual user account. Service account keys are better suited for automated systems. Please, notice that the usage of this integration entails API [quota consumption](../02-group-management/quota-consumption.md).

# 3.-configuration

This section details how to enable and configure the Google TI enrichment module within your MISP environment. You can follow these steps:

* Log in to your MISP instance with an **administrator** account.
* Go to **Administration -> Server Settings & Maintenance**.
* Click on the **Plugin** Settings tab.
* Locate the Google Threat Intelligence Module. You can use the search bar at the top and enter **google\_threat\_intelligence**.

![](https://storage.googleapis.com/gtidocresources/guides/integrations/images/misp_server_settings_20250910.png)

* Enable the Module (*mandatory step*)
  * In the filtered results, locate the setting named **Plugin.Enrichment\_google\_threat\_intelligence\_enabled** and double-click on the value field and set it to **true**.
* Configure the API Key setting (*mandatory step*)
  * Locate the setting named **Plugin.Enrichment\_google\_threat\_intelligence\_apikey** and paste your Google TI [service account API key](../02-group-management/admins-guide.md#1.3.3.-getting-a-service-accounts-api-key).
* Configure Optional Parameters (*if required*)
  * The module offers additional settings for **proxy configuration** and **event limit**.

Once finished, please reboot the service to apply the changes correctly. You can use this command `sudo systemctl restart misp-modules.service` but it might differ slightly based on your operating system and initial MISP setup.

# 4.-using-the-enrichment-module

The Google TI integration can be used to enrich attributes within any MISP event. MISP events are like *encapsulations for contextually related information*, such as threat articles, malware analyses, or reports on cyberattacks. Here you have an example of a MISP event:

![](https://storage.googleapis.com/gtidocresources/guides/integrations/images/misp_event_20250910.png)

The information  within an Event is structured using two main components: [attributes](https://www.circl.lu/doc/misp/GLOSSARY.html#misp-attribute) and [objects](https://www.circl.lu/doc/misp/GLOSSARY.html#misp-objects).

An **Attribute** is a single, discrete piece of information or an Indicator of Compromise (IoC). It is the most basic building block for representing data in MISP.

**Examples of Attributes**

* IP Address: 198.52.101.10
* Domain Name: evil-phishing-site.com
* File Hash (SHA-256): e3b0c44298fc1c149afbf4c8996fb92427ae51e4649b934ca495991b7852b855
* URL: <https://evil-phishing-site.com/login.php>
* Email Address: <spammer@example.com>

An **Object** is a structured template that groups multiple related attributes together to describe a more complex concept or entity. Objects provide context by showing how individual attributes are connected.

**Examples of Objects**

* Email Object: An "email" object would group several attributes together, such as:
  * from address: <spammer@example.com>
  * subject: Urgent: Invoice F-D4538934
  * attachment-filename: invoice.pdf.exe
  * attachment-sha256: (the hash of the malicious file)
* File Object: A "file" object could contain attributes like:
  * filename: svchost.exe
  * md5: d41d8cd98f00b204e9800998ecf8427e
  * size-in-bytes: 15360
  * path: C:\Windows\Temp\\

In the next image you can see that each line of the Event contain an attribute.

![](https://storage.googleapis.com/gtidocresources/guides/integrations/images/misp_event_attributes_20250910.png)

You can enrich your data in two different ways explain below:

## 4.1-individual-attribute-enrichment

This is the most granular and direct method. It allows an analyst to select a specific attribute within an event and run the Google TI enrichment module **exclusively for that attribute**. Allowed attributes to be enriched are file hashes, domains, urls and IP addresses.

This method is useful when a detailed and focused analysis on a single element of interest is required. In order to automate the enrichment of individual attributes follow these steps:

* Navigate to a **MISP event** containing the attribute you wish to enrich.
* Select the **attribute** by ticking the checkbox next to them.
* With the attributes selected, click the **Enrich Attributes icon** (a star symbol) in the actions menu. Depending on your user role, this may appear as "**Run enrichment**" (for administrator role) or "**Propose enrichment**" (for user role).

![](https://storage.googleapis.com/gtidocresources/guides/integrations/images/attribute_enrichment_20250910.png)

* A new window will appear, listing all available and enabled enrichment modules. Select **google threat intelligence** from the list.

![](https://storage.googleapis.com/gtidocresources/guides/integrations/images/enrichment_plugin_20250910.png)

* The module will query the Google TI API and return its findings. A new view will appear, **proposing the creation of new MISP Objects and Attributes** based on the intelligence received. Some results for the previous attribute enrichment proposal are presented below:
  * **Detection resume**: Containing the Google TI verdict (e.g., malicious), impact (e.g., high), threat score (e.g., 100) and other security vendors detection ratios.

![](https://storage.googleapis.com/gtidocresources/guides/integrations/images/enrichment_detection_information_20250910.png)

* **Relationships**: Discovered links or dependencies between the original attribute and other observables.

![](https://storage.googleapis.com/gtidocresources/guides/integrations/images/enrichment_related_attribute_20250910.png)

* **Identifiers and hashes**: Such as MD5, SHA1, SHA256, ssdeep, imphash, etc.
* Carefully review the proposed additions. You can deselect any objects you do not wish to import. Finally, click **Submit** to finalize and apply changes for the enrichment.

![](https://storage.googleapis.com/gtidocresources/guides/integrations/images/enrichment_related_hash_20250910.png)

For a **full list of data returned per indicator type**, please check out the [Annex I](#annex-i-enriched-data-in-misp-events).

## 4.2.-event-level-enrichment

MISP offers the "**Enrich Event**" functionality. When this option is selected, the platform will attempt to enrich **all compatible attributes** within that event using the selected enrichment modules, including Google TI.

![](https://storage.googleapis.com/gtidocresources/guides/integrations/images/enrichment_event_level_20250910.png)

This means that if an event contains, for example, several IP addresses and file hashes, MISP will run queries to Google TI **for all of them in a single operation**, optimizing the workflow when analyzing a set of related indicators.

# annex-i:-enriched-data-in-misp-events

The next table shows the attributes and relationships that the integration adds to MISP events for each indicator type.

| Files                                                               | URLs                                                                | Domains                                                             | IP addresses                                                        |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| [Google TI verdict](../06-ioc-investigation/google-threat-intelligence-indicator-score.md) | [Google TI verdict](../06-ioc-investigation/google-threat-intelligence-indicator-score.md) | [Google TI verdict](../06-ioc-investigation/google-threat-intelligence-indicator-score.md) | [Google TI verdict](../06-ioc-investigation/google-threat-intelligence-indicator-score.md) |
| [Google TI score](../06-ioc-investigation/google-threat-intelligence-indicator-score.md)   | [Google TI score](../06-ioc-investigation/google-threat-intelligence-indicator-score.md)   | [Google TI score](../06-ioc-investigation/google-threat-intelligence-indicator-score.md)   | [Google TI score](../06-ioc-investigation/google-threat-intelligence-indicator-score.md)   |
| Google TI impact                                                    | Google TI impact                                                    | Google TI impact                                                    | Google TI impact                                                    |
| Detection ratio                                                     | Detection ratio                                                     | Detection ratio                                                     | Detection ratio                                                     |
| md5,sha1,sha256                                                     | Communicating files                                                 | Whois                                                               | ANS                                                                 |
| tlsh                                                                | Downloaded files                                                    | Communicating files                                                 | Network                                                             |
| vhash                                                               | Referred files                                                      | Downloaded files                                                    | Country Resolutions                                                 |
| ssdeep                                                              | Resolutions                                                         | Referred files                                                      | URLs                                                                |
| imphash                                                             | URLs                                                                | Subdomains Siblings Resolutions                                     |                                                                     |
| ITW URLs                                                            |                                                                     | URLs                                                                |                                                                     |

---

← [Google Threat Intelligence for MSFT Sentinel](gti4sentinel-guide.md) · [up](README.md) · [Splunk integration guide](gti4splunk-guide.md) →

*Archived from <https://gtidocs.virustotal.com/docs/gti4misp-guide>.*
