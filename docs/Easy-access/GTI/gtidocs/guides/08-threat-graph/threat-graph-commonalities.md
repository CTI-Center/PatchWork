---
title: "Commonalities and Hunting"
source: https://gtidocs.virustotal.com/docs/threat-graph-commonalities
slug: threat-graph-commonalities
section: guides
group: "Threat Graph"
updatedAt: 2025-09-25T01:56:32.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [Threat Graph](README.md) › Commonalities and Hunting

---

# commonalities-and-hunting

# find-commonalities

***

Find common patterns is very important to achieve a successful investigation. Google Threat Intelligence Graph gives you the opportunity to find common patterns in a selection of nodes or even the nodes within a relationship.

There is a toolbar in the right side of the graph. That toolbar shows you in real time the status of the commonalities depending on the node selection.

* If there are more than one node selected, it shows the commonalities for the selected nodes
* If there are one or zero nodes selected, it shows the commonalities for all the nodes in the graph.

![VTGraph commonalities icon](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphcommonalities_icon_20240405.png)

You can also get the commonalities for all the children of a relationship node:

* Select a relationship node, and click "Calculate commonalities" in the left drawer panel

![VTGraph commonalities left panel link](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphcommonalities_leftpanellink_20240504.png)

# analyze-commonalities

***

Once you calculate the commonalities manually or once you click the commonality icon in the toolbar in the right side, the commonalities drawer will show up. This drawer allows you to interact with the graph and its commonalities.

Select a list of commonalities and click the button "Search and add to the graph" to perform a VTI search and aggregate the nodes to the graph.

![VTGraph commonalities add to graph](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphcommonalities_addtograph_20240405.png)

### commonality-contextual-menu

All the commonalities have a contextual menu with actions to execute.

* **Show node list:** Open the list nodes that matches this commonality.
* **Add a relationship node:** Create a commonality relationship node to connect all the nodes that matches this commonality.
* **Launch VT search & add to graph:** For the selected commonality, perform a search in VTI and add the result to the graph.
* **Create Yara Rule using this attribute:** Open a new YARA rule with this attribute

![VTGraph commonalities contextual menu](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphcommonalities_contextualmenu_20240405.png)

# hunting-and-retrohunt

***

New virus total graph allows you to integrate your hunting and retrohunt jobs with graph. Open it using the icon in the toolbar placed in the right side of the graph:

![VTGraph commonalities hunting icon](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphcommonalities_huntingicon_20240405.png)

### hunting

In this drawer you have your list of rulesets. You can interact with them:

* Load results on graph: Load the next twenty matches of this ruleset in the graph as nodes
* Open results on hunting
* Launch retrohunt: Open this ruleset in a new window to create a retrohunt job
* Delete rule

![VTGraph commonalities hunting options](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphcommonalities_huntingoptions_20240417.png)

### retrohunt

In this drawer you have the list of retrohunt jobs. The different status of the jobs are

* Starting
* Running
* Aborted
* Aborting
* Finished

The different actions to take with the jobs are:

* Load results on graph: Load the next twenty matches of the job in the graph as nodes
* Open results on hunting
* Download: Download the list of matches
* Delete retrohunt

![VTGraph commonalities retrohunt options](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphcommonalities_retrohuntoptions_20240417.png)

---

← [Get started with Threat Graph](get-started-threat-graph.md) · [up](README.md) · [Search and start new investigation](threat-graph-search.md) →

*Archived from <https://gtidocs.virustotal.com/docs/threat-graph-commonalities>.*
