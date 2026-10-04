---
title: "ASM GoDaddy Integration"
source: https://gtidocs.virustotal.com/docs/asm-godaddy-integration
slug: asm-godaddy-integration
section: guides
group: "ASM"
updatedAt: 2025-09-25T00:29:06.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [ASM](../README.md) › [Inbound Integrations](../inbound-integrations.md) › ASM GoDaddy Integration

---

# asm-godaddy-integration

> 🚧 Special privileges required
>
> This feature is only available to ASM administrators.

> ℹ️
>
> See how credentials for integrations are stored [here](asm-credential-security-details.md)

Our GoDaddy integration gives customers more visibility by pulling DNS data from GoDaddy directly into the platform as a Seed.

Adding this integration requires two steps: 

1. [Create API Key in GoDaddy](#create-api-key-in-godaddy)
2. [Provide GoDaddy Credentials for ASM](#provide-godaddy-credentials-for-asm)

## create-api-key-in-godaddy

1. Once authenticated with GoDaddy, access <https://developer.godaddy.com/keys> and select **Create New API Key**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_daddy_create_new_api_key_20240612.png)

2. Populate the fields and select **Next**.
   * **Name (Optional):** We suggest a name that you'll remember easily
   * **Environment**: Production

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_daddy_api_production_20240612.png)

3. Copy API **Key** and **Secret** to be used when [providing credentials to ASM](#provide-godaddy-credentials-for-asm).

> 🛑
>
> For security reasons, these credentials will only be shown once. Please copy and store in a secure location.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_daddy_api_secret_20240612.png)

## provide-godaddy-credentials-for-asm

1. From the ASM **Projects and Settings** menu, select the appropriate Project then click **Account Settings**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_daddy_account_settings_20240504.png)

2. Click **Integrations**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_daddy_integrations_20240606.png)

3. Under **Inbound Integrations**, click **Add New** for GoDaddy:

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_daddy_add_20240606.png)

4. Paste the **Key** and **Secret** values from above into the appropriate fields.
5. Click **Connect**.
6. Connect the integration to the appropriate Collectio&#x6E;**.**

   1. Click **Collections** and click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/threatprofile_engine_icon_20240509.svg) **Collection Settings** for the Collection that you want to connect the integration to.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_daddy_collections_20240604.png)

ii. Select the **Integrations** tab.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_daddy_configurations_20240604.png)

iii. Select **Connect Integration** and **Link** the integration.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_daddy_setup_20240605.png)

The integration is immediately added to the Collection.

> 💡
>
> ### Click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_delete_icon.svg) to remove the integration from this Collection. ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_daddy_delete_20240604.png)

iv. Click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/threatprofile_close_icon_20240509.svg) to close the **Connect Integration** pane. Click **Scan** **Collection** to update your Collection with the current settings and integrations. Otherwise, your newly configured integration is incorporated at your regularly scheduled scan interval.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_daddy_scan_20240604.png)

---

← [ASM GitHub Integration](asm-github-integration.md) · [up](../README.md) · [ASM Google Cloud Integration](asm-google-cloud-integration.md) →

*Archived from <https://gtidocs.virustotal.com/docs/asm-godaddy-integration>.*
