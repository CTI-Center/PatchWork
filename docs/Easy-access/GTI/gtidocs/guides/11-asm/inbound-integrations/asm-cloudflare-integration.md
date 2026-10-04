---
title: "ASM Cloudflare Integration"
source: https://gtidocs.virustotal.com/docs/asm-cloudflare-integration
slug: asm-cloudflare-integration
section: guides
group: "ASM"
updatedAt: 2025-09-25T00:29:03.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [ASM](../README.md) › [Inbound Integrations](../inbound-integrations.md) › ASM Cloudflare Integration

---

# asm-cloudflare-integration

> 🚧 Special privileges required
>
> This feature is only available to ASM administrators.

> ℹ️
>
> See how credentials for integrations are stored [here](asm-credential-security-details.md)

The Attack Surface Management (ASM) Cloudflare integration is designed to pull all DNS Records from zones for which the Cloudflare API Token was authorized. The records pulled downstream are then created as Entities based on their respective type. For example, A/AAAA records will be created as IPAddress Entities and the associated name and label will be turned into DnsRecord Entities.

This increases the quality of [Seeds](../understanding-attack-surface-management-seeds.md) in cases where the Cloudflare account is managing a substantial amount of records.

Adding this integration requires two steps: 

1. [Create Cloudflare API Token](#create-cloudflare-api-token)
2. [Provide Cloudflare API credentials for ASM integration](#provide-cloudflare-credentials-for-asm-integration)

## create-cloudflare-api-token

1. Once authenticated on `https://cloudflare.com`, browse to <https://dash.cloudflare.com/profile/api-tokens> and click **Create Token**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_cloudfare_create_custom_token_20240606.png)

2. Within the **API Tokens** interface, click **Get Started** next to **Create Custom Token**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_cloudfare_get_started_20240606.png)

3. Within the **Create Custom Token** interface, populate the fields as defined here and click **Continue to summary**:

   1. **Token name**: A friendly name that's easily remembered such as  *ASM Cloudflare Integration*
   2. **Permissions**:

      1. Zone - Zone - Read
      2. Zone - DNS - Read
   3. **Zone Resources**: Include - All zones

      > ℹ️
      >
      > Cloudflare provides the flexibility to allow the API Token to access all zones, a specific zone, or exclude specific zones. Typically most organizations would select **All Zones**, however adjust this option to fit your organization’s requirements.
   4. **Client IP Address Filtering**: Leave blank
   5. **TTL**: Leave blank

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_cloudfare_continue_to_summary_20240606.png)

4. Review and click **Create Token**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_cloudfare_create_token_finish_20240606.png)

5. Copy this token to be used when [providing credentials to ASM](#provide-cloudflare-credentials-for-asm-integration).

   > ❗️
   >
   > For security reasons, these credentials will only be shown once. Please copy and store in a secure location.

   ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_cloudfare_copy_token_20240606.png)

## provide-cloudflare-credentials-for-asm-integration

Add your Cloudflare API Token into the integration page and then on the Collection, choose which Collection you would like to pull the entities into.

1. From the **Projects and Settings** menu in ASM, select the appropriate Project then click **Account Settings**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_cloudflare_account_settings_20240504.png)

2. Click **Integrations**.
3. Under **Inbound Integrations**, click **Add New** for Cloudflare.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_cloudflare_add_20240606.png)

4. Paste the token value from the [Create Cloudflare API Token](#create-cloudflare-api-token) process outlined above into the **Cloudflare API** **Token** field and click **Connect**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_cloudflare_connect_20240606.png)

5. Connect the integration to the appropriate Collectio&#x6E;**.**

   1. Click **Collections** and click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/threatprofile_engine_icon_20240509.svg) **Collection Settings** for the Collection that you want to connect the integration to.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_cloudflare_collections_20240604.png)

2. Select the **Integrations** tab.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_cloudflare_configurations_20240604.png)

3. Select **Connect Integration** and **Link** the integration.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_cloudflare_setup_20240605.png)

The integration is immediately added to the Collection.

> 💡
>
> ### Click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_delete_icon.svg) to remove the integration from this Collection. ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_cloudflare_delete_20240604.png)

4. Click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/threatprofile_close_icon_20240509.svg) to close the **Connect Integration** pane. Click **Scan** **Collection** to update your Collection with the current settings and integrations. Otherwise, your newly configured integration is incorporated at your regularly scheduled scan interval.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_cloudflare_scan_20240604.png)

---

← [ASM Azure Integration](asm-azure-integration.md) · [up](../README.md) · [ASM DNS Made Easy Integration](asm-dns-made-easy-integration.md) →

*Archived from <https://gtidocs.virustotal.com/docs/asm-cloudflare-integration>.*
