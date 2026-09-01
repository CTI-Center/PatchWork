---
title: "IoC Collections"
source: https://gtidocs.virustotal.com/docs/ioc-collections
slug: ioc-collections
section: guides
group: "Global Landscape"
updatedAt: 2026-02-27T12:29:26.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [Global Landscape](README.md) › IoC Collections

---

# ioc-collections

A collection is a live report which contains a title, a group of IoCs (file hashes, URLs, domains and IP addresses) and an optional description. Collections are open to our Google Threat Intelligence Community (registered users) and they will be enhanced with Google Threat Intelligence (Google TI) analysis metadata providing the latest information we have for the IoCs, along with some aggregated tags. 

# ioc-collection-creation

## create-an-ioc-collection

You can create a collection through the home view by clicking on the "Smart Search" button as shown below:

![Link to create a collection](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/collections_createlink_20240409.png)

You need to add a name (1), a list of IoCs (2) (file hashes, URLs, domains and IP addresses) and then click on Create collection (3).\
You can also write a summary of what is the collection about in "Collection description" and setup visibility settings in "Visibility" section.

![Collection Details](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/collections_details_20241127.png)

If you are in the [IoC collections tab](https://www.virustotal.com/gui/threat-landscape/ioc-collections) you can click on "Create IoC Collection" button, and you will be presented with the same options mentioned.

![Create Collection from collection tab](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/collections_createnew_20241127.png)

Other places from where you can create IoC collections in the same way are:

* From the **Global Landscape** module, on the **IoC Collections** tab you will find the **Create IoC Collection** button
* From the user **Profile**, on the **COLLECTIONS** tab you will find the **Create IoC Collection** button

## create-an-ioc-collection-from-a-list-of-iocs

You can create a collection directly with a list of IOCs from a result page, click on "Tools" and "Add to Collection" and "Add to a new collection"

![Collection creation from IOCs](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/gticollections_addtocollection_20241008.png)

![New Collection creation from IOCs ](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/gticollections_addtocollection_new_20241008.png)

# ioc-collection-report

After your collection is created, you'll see a report that looks like this.

![Collection Report](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/collections_report_20241127.png)

We've numbered the elements in the screenshot above for easy reference. They are:

1. Follow the collection for get notifications on new IoCs added.
2. You can share the collection permanent link or post it to Twitter.
3. The collection provides exporting capabilities in STIX, JSON and CSV formats.
4. Open the IOCs in a Graph.
5. You can add more IOCs.
6. Delete the collection.
7. See commonalities between all the IoCs of the collection.
8. See telemetry of all the IoCs of the collection.
9. You can search for IOCs of an specific type to filter the results.
10. You can sort the IOCs by several attributes.
11. Edit IOCs of an specific type: you can add more IOCs or delete selected ones.
12. You can export IOCs of an specific type in STIX, JSON and CSV formats. You can also copy to clipboard. For files you can Download a selection of them.
13. Different Tools for the selected IoCs depending on the IOC type: Send to Diff, Open in Graph, Calculate commonalities or add to Another collection.

## add-more-iocs-directly-from-a-result-page

When you get a list of IOCs, as a result page, you can select some or all of these IOCs and add them to an already existant collection.

* Check the IOCs you want to add
* Click on Tools
* Click on Add to collection
* Select the collection you want these IOCs to be added to.

![Add IOCs to collections](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/collections_addtocollection_20241128.png)

![Add IOCs to collection selected](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/collections_addtocollection_list_20241128.png)

# own-ioc-collection-dashboard

Users can see their created collections in their profile page, as they currently do for graphs and comments.\
![Collections Dashboard](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/collections_dashboard_20240409.png)

# ioc-collections-visibility

You can set the visibility of your collections so they can be stablished as:

* Public
* Private - only you see the collection
* Private - with expanded visibility
  * Internally accessible - only you and the members of your group see the collection
  * Externally accessible - shared with external groups or other selected members

Note only IoC collection owners can change the visibility.

## setting-ioc-collections-visibility

### on-creation

You can select the visibility when creating an IoC collection using this dropdown in the bottom of the creation dialog:

![Collections X Integration](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/collections_visibility_creation_20240409.png)

### from-ioc-collection-report

You can modify the visibility of an IoC collection owned by you, by clicking on the Share & Visibility icon of your collection:

![Collections share button](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/collections_own_collection_share_20241127.png)

As you can see, you can control the users / groups you establish as editors / viewers, also set the private / public status of the collection, so this gives the collections owner full control on visibility.

![Collections Custom Visibility](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/collections_custom_visibility_20241127.png)

#### collaborator-types

Collaborators can be groups or users playing one of the following roles:

* Viewer: Can see the collection, but cannot modify
* Editor: Can see the collection, also add / delete IoCs and description.

Collaborators cannot delete collections, neither modify the visibility. Only the owner can perform those actions.

## public-ioc-collections

All **public** collections are available in Google TI under the Associations section, also the Global Landscape section. This way our users benefit from other analysis investigations.

![Collections Visibility on reports](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/collections_visibility_20241128.png)

### x-integration

Security community is very active using X to promote their investigations. Public IoC collections can be shared on X using the share link in the collections report header:

![Collections X Integration](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/collections_share_collection_20241128.png)

The IoC collection report shows the following card on X.

![Collections X Integration Card](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/collections_twitter_20231108.png)

## private-ioc-collections

**Private** IoC collections can be found in Google TI on the [Global Landscape section](https://www.virustotal.com/gui/threat-landscape/ioc-collections) or listed on the "Associations" tab of IoCs reports, and they can be identified through the "Private" tag.

A private IoC collection will usually be accessible to its owner or users who belong to the same Google TI group, as configured at creation time.\
However, private collections can be shared with external groups or specific members while maintaining their private status.

Typically, they are used for work-in-progress collections, then these collections may be shared with the desired scope. Check the [Collections Visibility](#ioc-collections-visibility) section for more details on how to create a private collection.

> ⚠️
>
> Unlike with public collections, IoCs added to a private collection will not automatically generate a report if they are not already part of our existing database.
> To provide the IoC report, the IoC must be scanned then made searchable and its report available to all Google TI users. So users must scan those IoCs separately to prevent potential leaks.

# on-quota-exceeded

***

Public users will have a quota of 20 Collections per month, if you reach the limit you would find the following message.

![Collections Quota exceeded message](https://storage.googleapis.com/gtidocresources/guides/threat-landscape/images/collections_quotaexceeded_20231108.png)

# api-usage

***

As usual we have also most of the functionality available using our API v3. You can check the API documentation in our [API Reference](https://gtidocs.readme.io/reference/threat-actors-malware-tools-campaigns-ioc-collections) page.

---

← [Campaigns](campaigns.md) · [up](README.md) · [TTP Analysis](ttp-analysis.md) →

*Archived from <https://gtidocs.virustotal.com/docs/ioc-collections>.*
