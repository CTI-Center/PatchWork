---
title: "ASM Jira Integration"
source: https://gtidocs.virustotal.com/docs/asm-jira-integration
slug: asm-jira-integration
section: guides
group: "ASM"
updatedAt: 2025-09-25T02:01:14.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [ASM](../README.md) › [Outbound Integrations](../outbound-integrations.md) › ASM Jira Integration

---

# asm-jira-integration

> 🚧 Special privileges required
>
> This feature is only available to ASM administrators.

> ℹ️
>
> This integration is only available for JIRA Cloud. JIRA Data Center (on-prem) is not supported.

JIRA has evolved into a powerful work management tool for all kinds of use cases, while using Attack Surface Management (ASM) you can use JIRA for the purpose of Issue tracking and management. After integrating, here, in ASM you can create JIRA tickets directly from Issues. No copy and paste is necessary; Issue details are pre-populated in the JIRA ticket.

## configure-jira-integration

1. From the **Projects and Settings** menu in ASM, select the appropriate Project then click **Account Settings**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_jira_account_settings_20240504.png)

2. Click the **Integrations** tab on the left.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_jira_integrations_20240606.png)

3. Scroll down to **Outbound Integrations** and click **Add New** next to **Jira**. 

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_jira_add_20240613.png)

4. On the **Connect your Jira Account** screen, enter your **Email**, **Host**, and **Jira API Key**.

   **NOTE:** For more information see [Manage API tokens for your Atlassian account](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/).

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_jira_credentials_20240613.png)

5. Press **Connect**.

## create-jira-ticket

1. Once integrated, navigate to the **Issues** page, select an issue and there on the issue details page you will find a **Create Jira Ticket** button right at the top.
2. Click the **Create Jira Ticket** button.
3. **Choose Project** in JIRA.
4.  **Send** the issue to JIRA.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_jira_integrations_20240613.png)

---

← [ASM Cortex XSOAR Integration](asm-cortex-xsoar-integration.md) · [up](../README.md) · [ASM ServiceNow Integration](asm-servicenow-integration.md) →

*Archived from <https://gtidocs.virustotal.com/docs/asm-jira-integration>.*
