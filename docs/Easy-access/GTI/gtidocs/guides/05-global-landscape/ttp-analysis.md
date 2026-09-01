---
title: "TTP Analysis"
source: https://gtidocs.virustotal.com/docs/ttp-analysis
slug: ttp-analysis
section: guides
group: "Global Landscape"
updatedAt: 2026-02-27T12:30:08.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [Global Landscape](README.md) › TTP Analysis

---

# ttp-analysis

Google Threat Intelligence allows you to explore Threat Actors and Malware on the basis of the [MITRE ATT\&CK<sup>®</sup> Framework](https://attack.mitre.org/). Analyzing Threat Actors and Malware this way helps you explore threats in terms of adversary Tactics, Techniques, and Procedures (TTPs) based on real-world observations.

In the MITRE ATT\&CK Framework:

* [Tactics](https://attack.mitre.org/tactics/enterprise/) represent the route or path of a MITRE ATT\&CK technique or sub-technique, which is the tactical goal (*why*) of an adversary.
* [Techniques and sub-techniques](https://attack.mitre.org/techniques/enterprise/) represent *how* an adversary achieves a tactical goal by performing an action.

Google Threat Intelligence is periodically updated to support the latest versions of MITRE ATT\&CK.

After reading this article, you will be able to:

* [Discover how to analyze Threat Actors and their associated TTPs](#analyze-threat-actors-using-the-explore-mitre-attck-dashboard) by focusing on use cases for tightening your security controls throughout the attack lifecycle. 
* [Learn how to explore specific Malware families](#analyze-malware-using-the-explore-mitre-attck-dashboard), using the role of Backdoor as an example filter.

## analyze-threat-actors-using-the-explore-mitre-att\&ck-dashboard

For example, say you want to explore the TTPs associated with five Actors targeting the automotive industry:

* UNC4393
* UNC2465
* UNC5806
* APT43
* UNC1069

### to-filter-and-analyze-threat-actors

![The Actors Selection](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/ttp_analysis_actor_selection_20241128.png)

1. Select **Global Landscape > TTP Analysis** to go to the Explore MITRE ATT\&CK dashboard

2. Choose **Threat Actor** from the Object Types (you might need to click View all if is not showing). This displays all Actors currently tracked by Google Threat Intelligence.

3. Select **Automotive** from the list of **Targeted Industries** filters to narrow your search.

4. From the resulting **Threat Actor List** we are going to select the first five for the example.

5. Click **Analysis** or **Next** to populate the MITRE ATT\&CK heat map with TTPs specific to the **Selected Actors**.

If more than one Actor is selected and analyzed as per the MITRE ATT\&CK framework, the heat map shows the number of selected Actors associated with each technique or sub-technique to aid in prioritizing mitigation efforts.If there are multiple sub-techniques associated with a technique, an expander arrow can be clicked to reveal them.

Hovering over a technique or sub-technique in the MITRE ATT\&CK matrix will:

* Display a brief description of the technique. This helps you understand what the technique entails and how it's used by attackers.
* Visually highlight relevant Threat Actors. Threat Actors who utilize the selected technique will remain in their original color, while those who do not will be grayed out.

![TTP heatmap description](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/ttp_analysis_heatmap_description_20241129.png)

You can select and de-select **Actors** on the heat map page itself to easily compare Actor TTPs within the heat map view.

## download-the-mitre-att\&ck-heat-map

![Download TTPs](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/ttp_analisis_mitre_download_20241129.png)

You can download the MITRE ATT\&CK (multi-actor) heat map as a CSV or JSON file for further analysis by clicking **Download TTPs** and choosing between **Export to CSV** and **Export to JSON**.\
This allows you to filter and sort heat map data to aid in prioritizing mitigation efforts. For example, you can filter on specific techniques or sub-techniques for a given MITRE Category Name (or, tactic), and then sort Actor(s) Usage Count to focus on the most commonly used techniques.

The following fields are included in the exported CSV file:

* Tactic ID
* Tactic Name
* Technique ID
* Technique Name
* Sub-Technique IDs
* Sub-Technique Names
* Number of associated objects
* Actors IDs
* Actors Names
* Malware IDs
* Malware Names
* Campaigns IDs
* Campaigns Names
* Tools IDs
* Tools Names
* IoC Collections IDs
* IoC Collections Names

## analyze-malware-using-the-explore-mitre-att\&ck-dashboard

The workflow for exploring Malware is similar to exploring Actors, but with different filtering options. For example, suppose a recent report noted an increased use of backdoor Malware in your industry. A vulnerability scan of Malware in your environment included the following Malware families, so you want to explore them further to understand your associated risk:

* QAKBOT
* 3FEXE
* BEACON
* EXPLOSIVE
* CARWASH

To filter and analyze malware

1. Select **Global Landscape > TTP Analysis** to go to the Explore MITRE ATT\&CK dashboard
2. Write **Backdoor** in the search bar that says "Begin your search here".
3. Choose **Malware** from the Object Types filter.
4. Select the five Malware families noted in your vulnerability scan.\
   ![You may select more than one Malware and your selection will appear as Selected Malware.](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/ttp_analysis_malware_selection_20241205.png)
5.  Click **Run TTP analysis** to populate the MITRE ATT\&CK heat map with TTPs specific to the selected Malware.\
   ![If more than one Malware is selected and analyzed as per the MITRE ATT\&CK framework, you get a heat map showing the number of selected Malware associated with each technique or sub-technique to aid in prioritizing mitigation efforts. If there are sub-techniques associated with a technique, a drop-down arrow will expand the heat map cell to reveal them.](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/ttp_analysis_malware_heat_map_20241211.png)

You can de-select **Malware** on the heat map page itself to easily compare **Malware** TTPs within the heat map view.

If more than one Malware is selected and analyzed in the MITRE ATT\&CK framework, a heat map displays the number of selected Malware associated with each technique or sub-technique. You can download the heat map as a CSV or JSON for further analysis to aid in prioritizing mitigation efforts against the selected Malware families, check [Download the MITRE ATT\&CK heat map](#download-the-mitre-att\&ck-heat-map) for more details.

---

← [IoC Collections](ioc-collections.md) · [up](README.md) · [New dark web research](dark-web-guide.md) →

*Archived from <https://gtidocs.virustotal.com/docs/ttp-analysis>.*
