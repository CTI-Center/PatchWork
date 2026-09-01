---
title: "Insights"
source: https://gtidocs.virustotal.com/docs/insights
slug: insights
section: guides
group: "ASM"
updatedAt: 2025-09-25T01:58:08.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [ASM](README.md) › Insights

---

# insights

# insights-overview-|-docs

> ## Excerpt
>
> Insights is a Attack Surface Management (ASM) reporting feature. The data reflected in this dashboard is related to the Collections that are selected. You can select specific Collections to modify the data presented to suit your needs. The names of the selected Collections are listed along with the number of associated Entities, Issues, and Technologies. Various widgets related to these Entities, Issues, and Technologies are also provided.

***

[Insights](https://asm.advantage.mandiant.com/insights) is a Attack Surface Management (ASM) reporting feature. The data reflected in this dashboard is related to the Collections that are selected. You can select specific Collections to modify the data presented to suit your needs. The names of the selected Collections are listed along with the number of associated [Entities](entities-guide.md), [Issues](issues-guide.md), and [Technologies](technologies-guide.md). Various widgets related to these Entities, Issues, and Technologies are also provided. 

The data is refreshed upon the completion of each Collection scan. The last scan date is listed with the Collection name.

![Insights Dashboard in ASM.](https://storage.googleapis.com/gtidocresources/guides/asm/images/insights_overview_20240418.png)

## widgets

Widgets include more detailed information about data from the selected Collections. Depending on the widget, you can click or hold the pointer over the data for more information. The following is an outline of the provided widgets:

### **hosts-by-country-widget**

Explore the the distribution of hosts across the globe.

![Hosts by Country widget.](https://storage.googleapis.com/gtidocresources/guides/asm/images/insights_host_country_20240418.png)

### **issue-widgets**

![Five widgets displaying different sets of data related to Issues.](https://storage.googleapis.com/gtidocresources/guides/asm/images/insights_issues_20240418.png)

* **Top 10 issue types by prevalence across critical or high**: View the top ten most common Issue types of Issues that have a [severity](issues-guide/issues-severity-definitions.md) of critical or high.
* **Top 10 most severe issues**: View the top ten most severe Issues. Critical is the highest Issue severity.
* **Issues by Severity**: View Issues by severity over time and understand their criticality.
* **Issues by Status**: View the breakdown of Issue [status](issues-guide.md#issue-status) to understand how many Issues are being addressed by your security team at any moment.
* **Issues by** [**Confidence**](issues-guide.md#confidence-level): Compare how many Issues ASM has determined to be confirmed versus potentially vulnerable.

### entity-widgets

![Four widgets displaying different sets of data related to Entities.](https://storage.googleapis.com/gtidocresources/guides/asm/images/insights_entities_20240418.png)

* **Entity types by prevalence**: View the most common Entity types.
* **Entities with the most inferred CVEs**: View the Entities with the most associated [inferred CVEs](entities-guide.md). 
* **Entities with the most issues**: View the Entities with the most associated Issues, excluding Issues of informational severity.
* **Entities by Type**: View the number of Entities of each type over time.

### technology-widgets

![A horizontal bar graph showing the top prevalent technology labels.](https://storage.googleapis.com/gtidocresources/guides/asm/images/insights_technologies_20240418.png)

* **Top prevalent technology labels**: View the most common Technologies identified in the selected Collections.

## export-an-insights-pdf

You can create a PDF containing all the information visible on the Insights dashboard.

1. From the **Collections** menu, select the Collections you want to include in your dataset.![Insights dashboard with the Collection menu expanded and three of eight collections selected.](https://storage.googleapis.com/gtidocresources/guides/asm/images/insights_collections_20240418.png)
2. Click **Generate PDF** to export.

---

← [Technologies](technologies-guide.md) · [up](README.md) · [Understanding Attack Surface Management Seeds](understanding-attack-surface-management-seeds.md) →

*Archived from <https://gtidocs.virustotal.com/docs/insights>.*
