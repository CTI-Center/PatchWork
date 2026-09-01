---
title: "ASM Akamai Integration"
source: https://gtidocs.virustotal.com/docs/asm-akamai-integration
slug: asm-akamai-integration
section: guides
group: "ASM"
updatedAt: 2025-09-25T00:28:57.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [ASM](../README.md) › [Inbound Integrations](../inbound-integrations.md) › ASM Akamai Integration

---

# asm-akamai-integration

> 🚧 Special privileges required
>
> This feature is only available to ASM administrators.

> ℹ️
>
> See how credentials for integrations are stored [here](asm-credential-security-details.md)

Attack Surface Management (ASM)'s Akamai integration gives you more visibility by pulling both DNS records and CDN hostnames from Akamai directly into the ASM platform as a [Seed](../understanding-attack-surface-management-seeds.md).

Adding this integration requires two steps: 

1. [Create API Key in the Akamai API Clients utility](#create-api-key-in-akamai)
2. [Provide Akamai API Credentials for ASM integration](##provide-akamai-api-credentials-for-asm-integration)

## create-api-key-in-akamai

1. Once authenticated with Akamai, go to <https://control.akamai.com/apps/identity-management/#/tabs/users/list>.
2. From the **Identity and Access Management** menu, select the **Users and API Clients** tab (1) and click **Create API client** (2).

![Red boxes highlight the Users and API Client tab and Create API client button.](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_create_api_20240603.png)

3. In the **Select API client type** section, select the **Service account** tab (1)  and click **Set API client options** (2).

![Red boxes highlight the set api client button.](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_service_account_20240603.png)

4. On the **Details** page, fill in the required fields and click **Select APIs**.

![Red boxes highlight the select APIs.](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_select_api_20240603.png)

5. Select and configure APIs.

   1. Search for the APIs you wish to pull downstream:

   * **DNS - Zone Record Management** (DNS records)

   > ℹ️
   >
   > The **DNS - Zone Record Management API** is required for this integration.

   * **Property Manager (PAPI)**  (CDN hostnames)

   2. For each applicable API, set the **Access level** to **READ-ONLY**.

   3. Click **Submit**.

   > ℹ️
   >
   > As an example, a DNS record is shown here, but this process is similar for a CDN hostname, also known as Property Manager (PAPI).\
   > ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_api_seleccion_20240503.png)

6. Back on the **Details** page, click **Select groups** and set the **Role** to **Viewer** for any groups that will be sending data to the ASM API. Click **Submit.**

![Red boxes highlight the select groups button.](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_select_group_20240603.png)

![Red boxes highlight the select APIs.](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_group_selection_20240603.png)

7. After reviewing your entries on the **Details** page, select the acknowledgement checkbox (1) and click **Create API client** (2).

![Red boxes highlight the select APIs.](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_create_api_client_20240603.png)

> ℹ️
>
> Only a DNS record API is shown in the preceding example. Depending on your setup, a Property Manager (PAPI) API may also be listed:\
> ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_property_manager_20240603.png)

8. Click **Create credential** and then download or copy the credential information. This is required to complete the Akamai API integration in ASM.

![Red boxes highlight the select APIs.](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_api_service_account_20240603.png)

![Red boxes highlight the select APIs.](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_credentials_20240603.png)

## provide-akamai-api-credentials-for-asm-integration

1. From the **Projects and Settings** menu in ASM, select the appropriate Project then click **Account Settings**.

![Red boxes highlight the Users and API Client tab and Create API client button.](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_account_settings_20240504.png)

2. Click **Integrations**.

![Red boxes highlight the Users and API Client tab and Create API client button.](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_integrations_20240604.png)

3. From **Inbound Integrations**, click **Add New** for Akamai.

![Red boxes highlight the Users and API Client tab and Create API client button.](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_add_20240604.png)

4. Paste the **Client Secret**, **Host**, **Access Token**, and **Client Token** values from the preceding section into the appropriate fields and click **Connect**.

![Red boxes highlight the Users and API Client tab and Create API client button.](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_credentials_20240604.png)

5. Connect the integration to the appropriate Collectio&#x6E;**.**

   1. Click **Collections** and click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/threatprofile_engine_icon_20240509.svg) **Collection Settings** for the Collection that you want to connect the integration to.

![Red boxes highlight the Users and API Client tab and Create API client button.](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_collections_20240604.png)

2. Select the **Integrations** tab.

![Red boxes highlight the Users and API Client tab and Create API client button.](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_configurations_20240604.png)

3. Select **Connect Integration** and **Set-up** the integration.

![Red boxes highlight the Users and API Client tab and Create API client button.](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_setup_20240604.png)

The integration is immediately added to the Collection.

> 💡
>
> ### Click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_delete_icon.svg) to remove the integration from this Collection. ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_delete_20240604.png)

4. Click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/threatprofile_close_icon_20240509.svg) to close the **Connect Integration** pane. Click **Scan** **Collection** to update your Collection with the current settings and integrations. Otherwise, your newly configured integration is incorporated at your regularly scheduled scan interval.

![Red boxes highlight the Users and API Client tab and Create API client button.](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_scan_20240604.png)

---

← [Inbound Integrations](../inbound-integrations.md) · [up](../README.md) · [ASM Credential Security Details](asm-credential-security-details.md) →

*Archived from <https://gtidocs.virustotal.com/docs/asm-akamai-integration>.*
