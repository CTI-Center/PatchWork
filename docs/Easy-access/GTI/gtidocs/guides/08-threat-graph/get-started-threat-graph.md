---
title: "Get started with Threat Graph"
source: https://gtidocs.virustotal.com/docs/get-started-threat-graph
slug: get-started-threat-graph
section: guides
group: "Threat Graph"
updatedAt: 2025-09-25T01:56:31.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [Threat Graph](README.md) › Get started with Threat Graph

---

# get-started-with-threat-graph

Google Threat Intelligence Graph is a visualization tool built on top of Google Threat Intelligence data set. It understands the relationship between files, URLs, domains, IP addresses and other items encountered in an ongoing investigation. With it, you can pivot intelligently over any of the malware artifacts in your graph and synthesize your findings into a threat map that you can share with your colleagues.

[Google Threat Intelligence Graph Overview](threat-graph-overview.md)\
[Google Threat Intelligence Graph search and start new investigation](threat-graph-search.md)\
[Google Threat Intelligence Graph management](threat-graph-management.md)\
[Google Threat Intelligence Graph nodes](threat-graph-nodes.md)\
[Google Threat Intelligence Graph Commonalities and Hunting](threat-graph-commonalities.md)\
[Quick access to relevant graphs to you](#quick-access-to-relevant-graphs-to-you)\
[Toolbar](#toolbar)\
[Google Threat Intelligence Graph API](#google-threat-intelligence-graph-api)

## getting-started:-key-steps

1. **Understanding Nodes and Relationships**\
   The Google Threat Intelligence backend maps over 30 types of relationships between files, URLs, domains, and more. Explore this network in an interactive graph, following the links between [nodes](threat-graph-nodes.md) and arcs to discover new infrastructure and artifacts used by your adversaries
2. **How to Search and Start a New Graph Investigation**
   1. [**Search For Threat Graphs**](threat-graph-search.md): Using the search functionality, you can search for other graphs that have been published publicly by the security community, or search for ones published by your team. You are also able to search for files or hashes to see Threat Graphs for those entities.
   2. You can start a new graph from the [Graph tab](https://www.virustotal.com/gui/graphs), clicking on the New graph button, or from a file report clicking on **More > Explore in Threat Graph**
3. **Find Commonalities and Start Hunting in Your Threat Graphs**\
   [Commonalities and Hunting](threat-graph-commonalities.md): Accelerate your investigations with Google Threat Intelligence Commonalities feature. By identifying common patterns within your selected nodes or relationships, you'll gain critical insights into the tactics, techniques, and procedures (TTPs) of your adversaries.

## quick-access-to-relevant-graphs-to-you

This overview page shows different list of graphs:

* **Your graphs:** It includes your saved graphs and those graphs where you are editor or viewer

![VTGraph yours graphs list](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphdocumentation_yourgraphs_20240405.png)

* **All graphs:** It includes the public graphs
* **My group graphs:** It includes the graphs from my group

![VTGraph latest graphs list](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphdocumentation_allgraphs_20240405.png)

## toolbar

For any of the list of graphs you are able to

![VTGraph sort criteria](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphdocumentation_sortcriteria_20231113.png):  Sort by different criteria

![VTGraph graphs list view](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphdocumentation_listview_20231113.png)/![VTGraph yours graphs list](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphdocumentation_gridview_20231113.png) : Switch between list and grid views

## google-threat-intelligence-graph-api

As most of our other products, Google Threat Intelligence Graph is getting a restful API. The documentation can be found [here](https://gtidocs.readme.io/reference/graphs) and a Python library to reduce the learning curve; it is available in our [Github repository](https://github.com/VirusTotal/vt-graph-api).

---

← [Threat Intelligence Report Types](../07-report-analysis/report-types.md) · [up](README.md) · [Commonalities and Hunting](threat-graph-commonalities.md) →

*Archived from <https://gtidocs.virustotal.com/docs/get-started-threat-graph>.*
