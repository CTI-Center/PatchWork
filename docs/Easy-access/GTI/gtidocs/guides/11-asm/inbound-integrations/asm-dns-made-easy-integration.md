---
title: "ASM DNS Made Easy Integration"
source: https://gtidocs.virustotal.com/docs/asm-dns-made-easy-integration
slug: asm-dns-made-easy-integration
section: guides
group: "ASM"
updatedAt: 2025-09-25T00:29:04.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [ASM](../README.md) › [Inbound Integrations](../inbound-integrations.md) › ASM DNS Made Easy Integration

---

# asm-dns-made-easy-integration

> 🚧 Special privileges required
>
> This feature is only available to ASM administrators.

> ℹ️
>
> See how credentials for integrations are stored [here](asm-credential-security-details.md)

Attack Surface Management (ASM)'s DNS Made Easy integration gives customers more visibility by pulling DNS records from DNS Made Easy directly into the ASM platform as a [Seed](../understanding-attack-surface-management-seeds.md).

Adding this integration requires two steps: 

1. [Locate DNS Made Easy keys](#locate-dns-made-easy-keys)
2. [Provide DNS Made Easy credentials to ASM](#provide-dns-made-easy-credentials-to-asm)

## locate-dns-made-easy-keys

Log into your DNS Made Easy account and access the **Config - Account Information** page. Save the **DNS Made Easy API Key** and **DNS Made Easy Secret Key** values for use in the next section.

> ℹ️
>
> For more for information about authentication, see the [DNS Made Easy API](https://api-docs.dnsmadeeasy.com/#5b98221f-37e9-4845-a349-5e959241b4a5).

## provide-dns-made-easy-credentials-to-asm

1. From the **Projects and Settings** menu in ASM, select the appropriate Project then click **Account Settings**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_dns_account_settings_20240504.png)

2. Click **Integrations**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_dns_integrations_20240606.png)

3. From **Inbound Integrations**, select **Add New** for DNS Made Easy.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_dns_add_20240606.png)

4. Modify your **DNS Made Easy API Endpoint**, if necessary. Enter your **DNS Made Easy API Key** and **DNS Made Easy Secret Key** values from the previous section into the appropriate fields and click **Connect**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_dns_credentials_20240606.png)

5. Connect the integration to the appropriate Collectio&#x6E;**.**

   1. Click **Collections** and click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/threatprofile_engine_icon_20240509.svg) **Collection Settings** for the Collection that you want to connect the integration to.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_dns_collections_20240604.png)

ii. Select the **Integrations** tab.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_dns_configurations_20240604.png)

iii. Select **Connect Integration** and **Link** the integration.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_dns_setup_20240605.png)

The integration is immediately added to the Collection.

> 💡
>
> ### Click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_delete_icon.svg) to remove the integration from this Collection. ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_azure_delete_20240604.png)

iv. Click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/threatprofile_close_icon_20240509.svg) to close the **Connect Integration** pane. Click **Scan** **Collection** to update your Collection with the current settings and integrations. Otherwise, your newly configured integration is incorporated at your regularly scheduled scan interval.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_dns_scan_20240604.png)

---

← [ASM Cloudflare Integration](asm-cloudflare-integration.md) · [up](../README.md) · [ASM GitHub Integration](asm-github-integration.md) →

*Archived from <https://gtidocs.virustotal.com/docs/asm-dns-made-easy-integration>.*
