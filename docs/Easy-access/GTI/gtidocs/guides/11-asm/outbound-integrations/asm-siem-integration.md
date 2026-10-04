---
title: "ASM Google SecOps SIEM Integration"
source: https://gtidocs.virustotal.com/docs/asm-siem-integration
slug: asm-siem-integration
section: guides
group: "ASM"
updatedAt: 2025-09-25T02:01:11.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [ASM](../README.md) › [Outbound Integrations](../outbound-integrations.md) › ASM Google SecOps SIEM Integration

---

# asm-google-secops-siem-integration

> 🚧 Special privileges required
>
> This feature is only available to ASM administrators.

[Google Security Operations (SecOps) SIEM (Security Information and Event Management)](https://cloud.google.com/security-information-event-management) provides threat detection and investigation with integrated threat intelligence. This integration allows Google SecOps to ingest data from Attack Surface Management (ASM). Specifically: 

* [Entities](../entities-guide.md) discovered by ASM are ingested as entity objects.
* [Issues](../issues-guide.md) detected by ASM are ingested as events.

An ASM Issue represents a detected vulnerability or potential cyber security weakness in a customer’s infrastructure. Surfacing this information in Google SecOps SIEM provides greater visibility and awareness to the customer.

## configure-the-google-secops-siem-integration

> ℹ️
>
> This integration only runs when a Collection Scan finishes. For example, if this integration is added on Monday, but the next applicable Collection Scan is scheduled for Tuesday, the integration runs on Tuesday when the Scan finishes.

1. From the **Projects and Settings** menu in ASM, select the appropriate Project then click **Account Settings**.

> ℹ️
>
> This integration is applied to the selected Project and all Collections that Project contains.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_siem_account_settings_20240504.png)

2. Click the **Integrations** tab.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_siem_integrations_20240606.png)

3. Go to **Outbound Integrations** and click **Add New** next to **Google SecOps SIEM**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_siem_add_intergation_20240930.png)

4. In the **Google SecOps Credentials** section:

   1. Update your **Ingestion API Endpoint**, if necessary. This defaults to `malachiteingestion-pa.googleapis.com`. 

   2. Enter your **Google SecOps Customer ID**.

   3. **Upload** **Service Account Key**. This is a JSON file that has been provided to you by your Google SecOps representative.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_siem_integration_configuration_20240930.png)

4. > ℹ️
   >
   > Once the JSON file uploads successfully, you are notified.\
   > ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_siem_success_20240613.png)

5. Select an **Ingest Period** from the drop-down.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_siem_ingest_20240613.png)

6. Select the minimum **Issue Severity** for issues to be ingested into Google SecOps.

> ℹ️
>
> * For example, if you select **Info**, all Issue Severities are selected meaning that issues of any severity are ingested.\* If no **Issue Severity** is selected, only Critical Issues are ingested as this is the default.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_siem_severity_20240613.png)

7. Click **Add Integration** to create the integration.

   > ℹ️
   >
   > When the wrong credentials are entered, the integration fails to connect.\
   > ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_siem_unable_validate_20240613.png)

## find-asm-issues-using-udm-search

Once ASM Issues are ingested into Google SecOps, you can find them using the following UDM query in the Google SecOps UDM Search console: `metadata.product_name = "Mandiant Attack Surface Management"`

---

← [Outbound Integrations](../outbound-integrations.md) · [up](../README.md) · [ASM Google SecOps SOAR Integration  Docs](asm-soar-integration.md) →

*Archived from <https://gtidocs.virustotal.com/docs/asm-siem-integration>.*
