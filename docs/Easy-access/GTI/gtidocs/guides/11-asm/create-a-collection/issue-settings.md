---
title: "Issue Settings"
source: https://gtidocs.virustotal.com/docs/issue-settings
slug: issue-settings
section: guides
group: "ASM"
updatedAt: 2025-09-25T01:58:44.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [ASM](../README.md) › [Create a Collection](../create-a-collection.md) › Issue Settings

---

# issue-settings

In Attack Surface Management (ASM), you decide what Issues you see for each Collection that you create. There are a variety of settings that you can establish and modify to curate the Issues exposed to you for each of your Collections. 

Access the [Collections Settings](customize-collections.md) for an existing Collection to customize any of the following **Issue Settings**:

* [Inferred CVEs](#inferred-cves)
* [Technologies](#technology-policy)
* [Ports](#port-policy-beta)
* [Issue Types](#issue-types)

> ℹ️
>
> You can modify **Issue Settings** before a Collection is scanned for the first time. To do so, when you [create a Collection](../create-a-collection.md), click **Create Collection**, rather than **Create & Run Collection**, to be directed to the **Issue Settings** for the new Collection.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/collection_issue_settings_20240517.png)

## inferred-cves

You can employ Inferred CVE data to create Issues.

> ℹ️
>
> * Updates to these settings require a Collection refresh. For an immediate refresh, click **Scan Collection**.\* If you choose to turn off this setting, no additional Issues are automatically created from Inferred CVEs. Issues remain that have already been created from Inferred CVEs.

## technology-policy

You can select technologies to be translated into Issues. When the technology you define is identified in a scan, an Issue is created with the severity that you have selected. 

To establish a Technology Policy:

1. Navigate to the [Collections Settings](customize-collections.md) for one of your existing Collections.
2. Click **Set Policy** on the **Technology Policy** tile.
3. Select a **Technology Vendor**.
4. Select a **Product** or a **Technology Label**.
5. Choose a [severity](../issues-guide/issues-severity-definitions.md) for Issues created as a result of this new policy.
6. Click **Create Issue**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/collection_issue_tech_policy_20240517.png)

## port-policy-(beta)

You can add ports to create Issues. When the port you define is discovered in a scan, an Issue is created with the severity that you have selected. 

To establish a Port Policy:

1. Navigate to the [Collections Settings](customize-collections.md) for one of your existing Collections.
2. Click **Set Policy** on the **Port** **Policy** tile.
3. Enter a **TCP Port**. 
4. Choose a [severity](../issues-guide/issues-severity-definitions.md) for Issues created as a result of this new policy.
5. Click **Create Issue**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/collection_issue_port_policy_20240517.png)

## issue-types

You can disable Issue Types so that they are not shown for a Collection. Toggle off any Issue Types you do not want to see. You can also adjust the [severity](../issues-guide/issues-severity-definitions.md) for each Issue Type to suit your needs.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/collection_issue_types_20240517.png)

To help you easily identify specific Issue Types, you can filter or search. The Issue Types filter options include **All Issue Types**, **Recent Issue Types**, **Technology Policies**, and **Port Policies**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/collection_issue_filter_20240517.png)

> ℹ️
>
> * Updates to these settings require a Collection refresh. For an immediate refresh, click **Scan Collection**.\* Active checks are not run for disabled Issues.

---

← [Third Party Monitoring Workflow](third-party-monitoring-workflow.md) · [up](../README.md) · [Assign Roles Within a Collection](assign-roles-within-a-collection.md) →

*Archived from <https://gtidocs.virustotal.com/docs/issue-settings>.*
