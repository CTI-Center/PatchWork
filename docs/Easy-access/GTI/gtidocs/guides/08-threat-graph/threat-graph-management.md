---
title: "Management"
source: https://gtidocs.virustotal.com/docs/threat-graph-management
slug: threat-graph-management
section: guides
group: "Threat Graph"
updatedAt: 2025-09-26T13:57:24.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [Threat Graph](README.md) › Management

---

# management

It is essential that when you are working in an investigation you are able to stop today and resume your investigation tomorrow. At the same time, you might want to share the graph with you colleagues so they can add their insights to the graph and, finally, publish it once you have finished working on it, if you decide to. All of these cases are covered by Google Threat Intelligence Graph.

In summary, you can:

* Edit graphs.
* Share graphs with other users or groups.
* Set graphs private.
* Embed your graphs in any webpage.

## create

***

You can save the progress you made on your graph doing click on the “Save graph” button or clicking the "File-->Save" menu item.

![Google Threat Intelligence Graph save icon](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphmanagement_saveicon_20240405.png)

Note: all saved graphs are made PRIVATE by default. This means that nobody could see your investigation unless you give them access or making the graph public. If you would like to set you graphs PUBLIC, see the section below.

## collaborate

***

The sharing panel gives you the opportunity to include other users as viewers or editors of the graph.

Click the shared/embedded button to open the shared modal.

![Google Threat Intelligence Graph share button](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphmanagement_sharebutton_20240405.png)

Viewers will get read-only access to the graph. In the case of editors, they will be able to modify and save the graph, add more collaborators or set the graph public/private. Although, only graph owners can delete graphs.

| Role | Read | Expand/Delete nodes | Add collaborators | Delete graph |
| --- | --- | --- | --- | --- |
| <strong>Owner</strong> | Yes | Yes | Yes | Yes |
| <strong>Editor</strong> | Yes | Yes | Yes | No |
| <strong>Viewer</strong> | Yes | No | No | No |

To add a user or group as editor or viewer you just need to type the user identifier in the collaborators input, select from the dropdown if the user is editor or viewer and finally click on the add button to save the changes.

![Google Threat Intelligence Graph add user button](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphmanagement_adduserbutton_20240405.png)

## private-graphs

***

As part of the premium package, you can set graphs private to collaborators, so only viewers or editors can find and access the graph.

The visibility of the graph can be changed at anytime by the graph owner.

![Google Threat Intelligence Graph visibility button](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphmanagement_visibilitybutton_20240504.png)

To make a graph public or private you just need to click on the button of the same name in the sharing panel.

## embed

***

Once an investigation has been finished, often you want to share the result of the investigation with other researchers or publish it on your website.

Google Threat Intelligence Graph allows you to embed public graphs in web pages thanks to our graph viewer that loads a lighter and read-only version of the graph.

Same way other resources are embedded on the internet nowadays, Google Threat Intelligence Graph is embedded using iframes. To add the graph in your website you just need to copy the html snippet from the embed graph panel as described below and paste it in your webpage.

![Google Threat Intelligence Graph embed html](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphmanagement_embedhtml_20240405.png)

## main-menu

***

You have a main menu that allows you to interact with the graph and with the different nodes within the graph.

* **File**: Management of the graph
* **Edit**: Interactions with all the nodes of the graph
* **View**: Management of the visible information of the nodes within the graph
* **Selection**: Interactions with the selected nodes of the graph
* **Visualization**: Different visualizations

![Google Threat Intelligence Graph main menu](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphmanagement_mainmenu_20240405.png)

## graph-toolbar

***

Type 3 characters or more in the input box to perform a search within the nodes of the current graph.

![Google Threat Intelligence Graph input box](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphmanagement_inputbox_20240405.png)

Use the icons in the toolbar to:

![](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphmanagement_addnodeicon_20231113.png): Add a new node to the graph

![](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphmanagement_undoicon_20231113.png): Undo the latest nodes added or removed to the graph

![](https://storage.googleapis.com/gtidocresources/guides/threat-graph/images/graphmanagement_redoicon_20231113.png): Redo the latest nodes added or removed to the graph

---

← [Nodes](threat-graph-nodes.md) · [up](README.md) · [Private Scanning](../09-private-scanning/private-scanning.md) →

*Archived from <https://gtidocs.virustotal.com/docs/threat-graph-management>.*
