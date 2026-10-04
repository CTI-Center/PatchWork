---
title: "Campaigns"
source: https://gtidocs.virustotal.com/docs/campaigns
slug: campaigns
section: guides
group: "Global Landscape"
updatedAt: 2026-02-27T12:13:53.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [Global Landscape](README.md) › Campaigns

---

# campaigns

Security teams may struggle with understanding their threat landscape and determining what activity to focus on, especially when faced with a myriad of emerging threats. To better assist these teams, the Threat Campaign feature in Google Threat Intelligence gives security professionals visibility into active campaigns affecting their industries, regions, and peers.

This feature provides a campaign-centric view and lets you easily pivot across all accompanying intelligence. Campaigns help you better prioritize mitigation and response actions in preparation for the next attack with a high degree of confidence. Data is updated daily as analysts get new campaign details, so you get access to Google Threat Intelligence’s knowledge in near real-time.

![The Explore Campaigns dashboard.](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/campaigns_dash_20241125.png)

## campaign-creation

Google TI analyzes emerging threat data directly from client engagements and from open source or other collections methods when assessing a campaign's viability for a Threat Campaign profile. Considerations for campaign creation include the following:

* Who is the threat actor, what are their motivations, and how impactful are their operations on targeted organizations? For example, an espionage actor targeting Ministries of Foreign Affairs or a fast-paced extortion operator does not equate to automated drive-by adware or infostealer campaigns.
* What level of insight into the campaign do we have? Can we confirm that multiple organizations have been targeted? Do we have a sufficient amount of shareable, actionable data that we can disseminate to our clients?
* Is the targeting broad enough that the targeted organizations could not be discerned based on the data we have available to share?

  We take sensitivities of this data very seriously and make every effort to restrict the unintended release of sensitive, client-attributable data into the Threat Campaign profile.

## campaign-list

All active campaigns appear in full in the Campaign List. You can search or filter on the results and open a specific campaign to access its more granular details. Campaigns are automatically updated as analysts tag events.\
You can use various filters to pare down the list:

* Creation Date
* Last Modification Date
* Origin
* Source Region
* Targeted Region
* Targeted Industry
* Associated Malware
* Associated Tools

## campaign-card

Each campaign is shown as a card in the list with relevant information.

![A modal displays a sample Campaign Summary.](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/campaigns_card_20241125.png)

1. Campaign title
2. Update date: Date when the campaign card was last updated with any new associated report, malware family, targeted region, etc.
3. Owner: Creator of the campaign card.
4. Campaign ID
5. Last activity: Date when the last observation about that campaign was made by Google Threat Intelligence analysts.
6. Description: Short summary of the Campaign
7. Targeted Industries
8. Targeted Regions
9. Associated Actors
10. Associated Malware
11. IoCs: number of IoCs related to this Campaign
12. Telemetry graph on IoC activity

Each Campaign card has a checkbox to the left to select it, when selected you have two options that are enabled in the top right corner:

#### follow-campaigns

In the **Campaigns** tab, click **Follow** for any Campaign to monitor changes to the selected Campaigns over time, such as new activity, associations or IoCs.\
![Follow  campaign buttons](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/campaigns_follow_20241125.png)

To add a Campaign to a Threat Profile, open the card details and use the Follow button inside, it will give you the option to choose which profile to add it to.

![Malware Follow and Add to Threat profile](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/campaigns_follow2_20241125.png)

#### run-ttp-analysis

You are redirected to [TTP Analysis](ttp-analysis.md) tab where a MITRE ATT\&ACK matrix is filled with the TTPs of the campaign/s selected so you can explore it in detail.

Actions available for TTPs:

* Hovering over the ID of a Technique or Tactic provides a brief description of it and a link to open details in MITRE site.
* Clicking on the name of a Technique or Tactic will redirect you to a Intelligene search filtering for that specific Technique (example: [attack\_technique:T1129](https://www.virustotal.com/gui/search/attack_technique%253AT1129?type=files))
* Clicking on the matches tag on the bottom right corner of a Technique will redirect you to the list of the current Campaign's IOCs that match this Technique

## campaign-details

Click on the name of any Campaign card for a view its details, navigate its tabs for specific data:

* **Summary**: This tab displays the same comprehensive summary of the Campaign as seen in the quick view. It also includes an Overview block with information such as Targeted Regions and Industries and  dates on campaigns's activity. The following blocks have a dashboard with a timeline with Campaign most relevant activity, and summarized information on Associated Actors, Malware, Tools & Vulnerabilities, Associations timeline, Telemetry Graph and Activity board.

![Campaign summary tab](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/campaigns_summary_20241125.png)

* **Associations**: This tab provides a list of the various associations with this Campaign. It includes associated Malware, Toolkits, Threat Actors and Vulnerabilities. Various filter options let you customize your view.

![Campaign associations tab](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/campaigns_associations_20241125.png)

* **IOCs**: This tab includes a table with all known Indicators attributed to this Campaign, such as specific IP addresses, urls, domains, and hashes.\
  ![Campaign IoCs tab](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/campaigns_ioc_20241125.png)

* **Rules**: This tab shows detection rules for this Campaigns IoCs, there are Yara, Sigma and IDS rules, and they can be crowdsourced or curated. These rules can be downloaded for use in threat hunt efforts or other workflows involving third-party security tools outside the Google Threat Intelligence platform.

![Rules tab](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/campaigns_rules_20241125.png)

* **TTPs**: This tab shows the Tactics, Techniques, and Procedures (TTPs) observed to be associated with this Campaign. This tab contains 2 sub tabs:
  1. **Threat Actor Actions**: shows the events observed by Google Threat Intelligence analysts in a timeline and as a detailed list.
  2. **MITRE ATT\&CK**: shows the MITRE matrix with all TTPs associated, they can be downloaded by clicking Download TTPs from the Actions drop-down.

![TTPs tab.](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/campaigns_ttps_20241125.png)

* **Community**: This tab features a dedicated space for community discussion, it is a section that contains comments posted by the community making observations on the Campaign.

---

← [Malware & Tools](malware-tools.md) · [up](README.md) · [IoC Collections](ioc-collections.md) →

*Archived from <https://gtidocs.virustotal.com/docs/campaigns>.*
