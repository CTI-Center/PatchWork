---
title: "Overview"
source: https://gtidocs.virustotal.com/docs/threat-graph-overview
slug: threat-graph-overview
section: guides
group: "Threat Graph"
updatedAt: 2025-09-26T13:56:27.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [Threat Graph](README.md) › Overview

---

# overview

Google Threat Intelligence Graph is a visualization tool built on top of Google Threat Intelligence data set. It understands the relationship between files, URLs, domains, IP addresses and other items encountered in an ongoing investigation. With it, you can pivot intelligently over any of the malware artifacts in your graph and synthesize your findings into a threat map that you can share with your colleagues.

![](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphoverview_graph_20240404.png) 

# relationships-oriented

***

Google Threat Intelligence's backend generates rich relationships: URLs from which a file has been downloaded, whether a given file been seen contained in some other files, what are the parents of a given Portable Executable, domain to IP address mappings over time, etc. Explore all these 30+ inter-item links in a graph, with nodes and arcs that allow you to discover new infrastructure and artifacts leveraged by the subjects of your investigation.

![](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphoverview_relations_20240404.png) 

# create,-collaborate,-share

***

Work in the same investigation with your peers, save your investigation graphs and publish your findings either publicly or with your organization.

![](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphoverview_sharepublicly_20240404.png) ![](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphoverview_shareorganization_20240404.png) 

# find-patterns

***

Common patterns and commonalities are very interesting and, in a way, a critical piece in the investigation, this is why we have decided to calculate them on-demand for you. Just select a group of nodes in the graph and click on “Find commonalities” to see a list of common attributes in the selection.

![](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphoverview_patterns_20240404.png) 

# seamless-integration-with-vti-search-and-hunting

***

Expand a node using a VTI search query or download the selected nodes in the graph. Google Threat Intelligence Graph works along with their sibling VT tools.

![](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphoverview_vti_20240404.png) 

# threat-cards

***

Hover over any of the nodes in your graph and see a summary of the item with the most representative data in Google Threat Intelligence database. Click in the node to see the available expansions, the submission graph, the AV verdicts (for files and urls) and the community comments.

![](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphoverview_threatcards_20240404.png) 

# custom-nodes

***

Google Threat Intelligence dataset might not know a link between two entities as it might only happen in your environment. VT Graph allow you to manually add this links and furthermore, to add a new node to the graph even when VT doesn’t know about it. Our supported custom types are file, url, domain, IP address, actor, department, email and victim.

![Google Threat Intelligence Graph VTI custom nodes](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphoverview_customnodes_20240404.png)

---

← [Search and start new investigation](threat-graph-search.md) · [up](README.md) · [Nodes](threat-graph-nodes.md) →

*Archived from <https://gtidocs.virustotal.com/docs/threat-graph-overview>.*
