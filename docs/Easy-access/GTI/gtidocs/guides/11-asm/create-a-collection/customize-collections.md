---
title: "Customize Collections"
source: https://gtidocs.virustotal.com/docs/customize-collections
slug: customize-collections
section: guides
group: "ASM"
updatedAt: 2025-09-25T00:27:46.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [ASM](../README.md) › [Create a Collection](../create-a-collection.md) › Customize Collections

---

# customize-collections

In Attack Surface Management (ASM), Collections are created within Projects and are lists of assets that are actively being monitored. Collections define the starting point of external asset discovery. Entities, known as Seeds, are populated into a Collection to uncover additional Entities that are exposed. The data identified as related to the Seeds is represented in the [Entities](../entities-guide.md) section of ASM.

> Collection configuration is available for paid Attack Surface Management (ASM) customers.
>
> If you would like to upgrade to a more feature-rich account, send a message using our contact form, <https://www.virustotal.com/gui/contact-us>.

For information on establishing Collections, see [Create a Collection](../create-a-collection.md).

## explore-collections

To view all the Collections in your current Project, from the **Collections** menu in ASM, select **Settings**. You see a list of all the Collections in this Project. 

![A list of two Collections in a specific Project with details about each Collection](https://storage.googleapis.com/gtidocresources/guides/asm/images/customize_collections_asm_collections_20250320.png)

Each Collection listing contains:

* The title of the Collection
* The [Workflow](../create-a-collection.md#scan-workflow-templates) associated with the Collection
* The [Entities](../entities-guide.md) and [Issues](../issues-guide.md) associated with the Collection
* The date of the last scan
* The [scan rate](collection-scan-rate.md)
* An on-demand **Scan** option

  > ℹ️
  >
  > Collection scans run for a maximum of 72 hours.
* Access to [**Settings**](customize-collections.md) specific to this Collection

## customize-a-collection

To explore a Collection in depth or modify its current settings, click **Settings** for the Collection.

Each collection contains four sections:

* [Configurations](#configurations)
* [Notifications](#notifications)
* [History](#history)
* [Groups & Members](#groups--members)

### configurations

Collections can be configured to focus on areas relevant to your organization. With custom configuration, you can define specific tasks, workflows, and scope. Multinational organizations with numerous subsidiaries and companies with operational technologies (OT) benefit from this functionality.

> ℹ️
>
> You must be the Collection owner to modify **Configurations**.

To establish Collection-specific configurations, navigate to a collection. **Configurations** is the default view.

![Configurations options for a Collection.](https://storage.googleapis.com/gtidocresources/guides/asm/images/customize_collections_asm_collections_details_20240514.png)

**Configurations** are divided into six groups:

* [Issue Settings](issue-settings.md): Control the Issues that are shown to you.

  > ℹ️
  >
  > * All updates require a collection refresh when first enabled. For immediate refresh, click **Scan** **Collection**.\* Disabled Issues are still monitored but do not show up in your alerts or surface as Issues within the platform.
* **Scan Settings**: Active Filter, Scoping and custom input types, including Cookies, Ports, and Headers.

  ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/customize_collections_asm_collections_scan_options_20240514.png)

  * **Configurable Active Filter**: Define the timeline for when Entities, Technologies, and Issues are considered Active versus Inactive.
  * **Enable Broad Scoping**: By default, broad scoping is disabled.

    Broad scoping is useful for penetration testers who want to expand the scope of their collection to find more Entities to test. However, this may result in false positives. When broad scoping is enabled, ASM changes its default behavior and scopes DNS Entities where scoping logic indicates potential ownership.
  * **Cookies** (string, name=value format): Enter one or more cookies to make a HTTP request. Individual cookies are concatenated and sent as one combined string.

    For example: `x-cdn=akamai; SimpleSAMLSessionID=12312;`
  * **Ports**: Limited to 100 TCP ports. You can add/delete multiple ports based on your requirements.
  * **Headers**: Limited to 100 Headers. Headers are case sensitive.

    > ℹ️
    >
    > * Scanning time increases as more Cookies, Ports, or Headers are added.\* If you add an entry that exists, you receive a "Validation failed" error.
* **Seed Entities**: See [Understanding Attack Surface Management Seeds](../understanding-attack-surface-management-seeds.md) to learn more about Seeds in ASM. Seeds can be uploaded from a CSV file.
* **Seed Keywords**: These are `UniqueKeyword` Seed Types.
* **Integrations**

  > ℹ️
  >
  > You must be the Collection owner to view and modify **Integrations**.

  You can connect an available integration by clicking **Connect Integration** and selecting **Link** associated with that integration. See [Integrations](../inbound-integrations/asm-azure-integration.md) for more details on how to add a new integration to a Collection.
* **Out of Scope**: Choose an Entity to set out of scope.

  > ℹ️
  >
  > By default, these changes are effective at the next Collection scan. For immediate refresh, click **Scan** **Collection**.

### notifications

> ℹ️
>
> You must be the Collection owner to view and modify **Notifications**.

You can enable email notifications as well as webhooks. Both Slack and Microsoft Teams webhooks are supported. For more information, see [Notifications](../notifications.md).

![Notifications options for a Collection including email and webhook options.](https://storage.googleapis.com/gtidocresources/guides/asm/images/customize_collections_asm_collections_notifications_20240514.png)

### history

You can view scan history information including:

* **Engine**
* **Status**
* **#Entities**: Number of Entities discovered.
* **Created By**: Who initiated the scan.
* **Started At**: When the scan started.
* **Finished At**: When the scan finished. 
* **Duration**

  ![Scan History for a Collection showing a table of relevant data.](https://storage.googleapis.com/gtidocresources/guides/asm/images/customize_collections_asm_collections_history_20240514.png)

> ℹ️
>
> Freemium organizations and organizations with trial entitlements may be linked to Read Only Collections that have historic data from the ASM catalogue. This can cause First seen dates for Issues to be well before a collection was established.

> 💡
>
> ### Read Only Collections can be archived to prevent historic Issues from appearing in current scans.

### groups-&-members

> ℹ️
>
> You must be the Collection owner to view and modify **Groups & Members**.

See [Assign Roles Within a Collection](assign-roles-within-a-collection.md) for more information about how to add an individual member or a group to a Collection.

## archive-a-collection

1. In ASM, from the **Collections** menu, select **Settings**.
2. Click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/threatprofile_more_icon_20240509.svg) associated with the Collection that you want to archive and select **Archive**.

## delete-a-collection

> ℹ️
>
> A Collection must be archived before it can be deleted.

1. In ASM, from the **Collections** menu, select **Settings**.
2. Click the **Archived** tab.
3. Click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/threatprofile_more_icon_20240509.svg) associated with the Collection that you want to delete and select **Delete**.

---

← [Collections Tips and Tricks](collections-tips-and-tricks.md) · [up](../README.md) · [Third Party Monitoring Workflow](third-party-monitoring-workflow.md) →

*Archived from <https://gtidocs.virustotal.com/docs/customize-collections>.*
