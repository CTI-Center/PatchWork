---
title: "ASM Azure Integration"
source: https://gtidocs.virustotal.com/docs/asm-azure-integration
slug: asm-azure-integration
section: guides
group: "ASM"
updatedAt: 2025-09-25T00:29:02.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [ASM](../README.md) › [Inbound Integrations](../inbound-integrations.md) › ASM Azure Integration

---

# asm-azure-integration

> 🚧 Special privileges required
>
> This feature is only available to ASM administrators.

> ℹ️
>
> See how credentials for integrations are stored [here](asm-credential-security-details.md)

> ℹ️
>
> This integration is not currently supported for Azure Government users.

With Azure, Attack Surface Management (ASM) retrieves public virtual machine (VM) instances, public DNS zones, and Blob Storage resources. For Blobs, ASM checks to see if they are publicly accessible and creates relevant issues. This gives a more through view of your inventory.

> ℹ️
>
> Only one Azure integration is allowed per Project in ASM.

Adding this integration requires three steps:

1. [Give ASM access to Azure](#give-asm-access-to-azure)

> ℹ️
>
> For this step, you are required to authenticate using an Azure account that has privileges to add an application to the Azure account. This should be one of the following account types:
>
> * Global Administrator
> * Privileged Role Administrator
> * Cloud Application Administrator
> * Application Administrator

2. [Add role assignment for ASM in Azure](#add-role-assignment-for-asm-in-azure)
3. [Connect the integration to the appropriate Collection](#connect-the-integration-to-the-appropriate-collection)

## give-asm-access-to-azure

1. From the **Projects and Settings** menu in ASM, select the appropriate Project then click **Account Settings**.
2. Click **Integrations**.
3. Next to Azure, click **Add New**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_azure_integrations_20240605.png)

4. Click **Connect**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_azure_connect_20240605.png)

The system redirects you to the Microsoft sign-in page.

5. Authenticate using an account that has privileges to add an application to the Azure account.\
   6\. When authentication is complete, you see a Microsoft screen requesting permission for **Mandiant ASM** to access your Azure instance.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_azure_permissions_20240605.png)

7. Click **Accept** and the system redirects you back to ASM.

## add-role-assignment-for-asm-in-azure

Role assignment can be performed for specific resource groups, or all resource groups in a subscription. This includes any future resource groups that may be added to a subscription. For role assignment, sign in to the Azure Portal and perform the following actions:

> ℹ️
>
> The following screenshots depict the role assignment workflow for resource groups but the process is the same for subscriptions.

1. Browse to [Resource groups](https://portal.azure.com/#blade/HubsExtension/BrowseResourceGroups) (or [Subscriptions](https://portal.azure.com/#blade/Microsoft_Azure_Billing/SubscriptionsBlade)) within Microsoft Azure.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_azure_resource_groups_20240605.png)

2. For each resource group (or subscription) that you would like to allow ASM to pull data in from, perform the following actions:
   1. Click the respective resource group (or subscription). 
   2. Click **Access control (IAM)**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_azure_iam_20240605.png)

3. Within the **Access Control (IAM)** menu, click **Add** and select **Add role assignment**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_azure_iam_role_20240605.png)

4. Select **Role** and choose the **Reader** role for view-only access. Click **Next**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_azure_reader_20240605.png)

5. On the **Members** screen, choose the following options:
   1. **Assign access to**: **User, group, or service principal**
   2. Click **+** **Select members**. When the **Select members** menu opens, search for and select **Mandiant ASM**.
   3. Click **Select.**

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_azure_members_20240605.png)

6. Click **Review + assign**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_azure_review_20240605.png)

7. Ensure that all the information in the **Review + assign** section is correct and click **Review + assign.**

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_azure_role_assignment_20240605.png)

## connect-the-integration-to-the-appropriate-collection

Connect the integration to the appropriate Collectio&#x6E;**.**

1. Click **Collections** and click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/threatprofile_engine_icon_20240509.svg) **Collection Settings** for the Collection that you want to connect the integration to.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_azure_collections_20240604.png)

2. Select the **Integrations** tab.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_azure_configurations_20240604.png)

3. Select **Connect Integration** and **Link** the integration.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_azure_setup_20240605.png)

The integration is immediately added to the Collection.

> 💡
>
> ### Click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_delete_icon.svg)  to remove the integration from this Collection. ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_azure_delete_20240604.png)

4. Click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/threatprofile_close_icon_20240509.svg) to close the **Connect Integration** pane. Click **Scan** **Collection** to update your Collection with the current settings and integrations. Otherwise, your newly configured integration is incorporated at your regularly scheduled scan interval.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_azure_scan_20240604.png)

Repeat the same steps for each resource group or subscription you would like ASM to access.

---

← [Scale AWS Integration Across AWS Organizations](scale-aws-integration-across-aws-organizations.md) · [up](../README.md) · [ASM Cloudflare Integration](asm-cloudflare-integration.md) →

*Archived from <https://gtidocs.virustotal.com/docs/asm-azure-integration>.*
