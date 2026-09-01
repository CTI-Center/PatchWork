---
title: "ASM Cortex XSOAR Integration"
source: https://gtidocs.virustotal.com/docs/asm-cortex-xsoar-integration
slug: asm-cortex-xsoar-integration
section: guides
group: "ASM"
updatedAt: 2025-09-25T02:01:13.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [ASM](../README.md) › [Outbound Integrations](../outbound-integrations.md) › ASM Cortex XSOAR Integration

---

# asm-cortex-xsoar-integration

> 🚧 Special privileges required
>
> This feature is only available to ASM administrators.

Cortex XSOAR from Palo Alto Networks is a security orchestration, automation, and response (SOAR) platform that unifies case management, automation, real-time collaboration, and threat intel management to serve security teams across the incident lifecycle.

This Cortex XSOAR integration lets you import Attack Surface Management (ASM) Issues into XSOAR as Incidents. The process for configuring this integration is outlined in the following sections.

## generate-api-credentials-in-the-asm-platform

1. In ASM, navigate to **Projects and Settings >** **Account Settings**.
2. Click **API Keys** to bring up a list of any keys that exist.
3. Click **Generate New Key** and make a note of the **Access Key** and **Secret Key** that are shown. These keys are used when configuring access to a Collection in XSOAR.

> 🛑
>
> This is the ONLY time that you have access to this information. If these keys are lost, you must remove this set and generate a new pair.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_xsoar_apikey_20240613.png)

4. Click **I understand & saved the key**.

## add-the-asm-integration-to-your-cortex-xsoar-configuration

1. Access the [Cortex XSOAR Marketplace](https://cortex.marketplace.pan.dev/marketplace/) and search for the Attack Surface Management integration. 
2. Download and install the Surface Management integration pack.
3. Within your Cortex XSOAR instance, navigate to **Settings** > **Integrations**.
4. Search for the Attack Surface Management integration, and click **Add Instance** to configure a new instance of the integration.
5. Enter **Name**, select **Fetches incidents**, and enter `http://www.virustotal.com/` as **Your server** **URL**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_xsoar_instance_settings_1_20240613.png)

6. Enter **Access Key** and **Secret Key** from the Cortex XSOAR integration settings in the ASM platform described in the preceding section.
7. Define **Maximum Issues to Fetch** and **Minimum Severity**. See the [Numeric Severity](../issues-guide/issues-severity-definitions.md#numeric-severity) for more information.
8. Adjust additional settings to suit your environment and requirements then click **Save & exit**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_xsoar_fetch_and_severity_1_20240613.png)

## included-commands-for-xsoar

Two commands have been included with this integration to assist you with obtaining the Project IDs and Collection IDs for the configuration.

1. `!attacksurfacemanagement-get-projects` shows a list of all the Projects associated with your API key and their corresponding IDs.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/xsoar_get_projects_2024061.png)

2. `!attacksurfacemanagement-get-collections` shows a list of all the collections within the Project configured in the instance configuration.

> 💡
>
> ### If a `project_id` is provided, it overrides the Project ID in the integration configuration.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_xsoar_get_collections_20240613.png)

---

← [ASM Google SecOps SOAR Integration  Docs](asm-soar-integration.md) · [up](../README.md) · [ASM Jira Integration](asm-jira-integration.md) →

*Archived from <https://gtidocs.virustotal.com/docs/asm-cortex-xsoar-integration>.*
