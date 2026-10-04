---
title: "ASM ServiceNow Integration"
source: https://gtidocs.virustotal.com/docs/asm-servicenow-integration
slug: asm-servicenow-integration
section: guides
group: "ASM"
updatedAt: 2025-09-25T02:01:15.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [ASM](../README.md) › [Outbound Integrations](../outbound-integrations.md) › ASM ServiceNow Integration

---

# asm-servicenow-integration

> 🚧 Special privileges required
>
> This feature is only available to ASM administrators.

[ServiceNow](https://docs.servicenow.com/) is an automated cloud workflow solution. Using the Attack Surface Management (ASM) integration, you can create enterprise workflow applications to track ASM Issues. This way, you can synchronize issue management between ServiceNow and ASM; reflecting status changes and remediation progress in both products.

This integration provides interaction with ServiceNow Vulnerability Response only. The integration collects Issues from ASM and maps them to the ServiceNow data model. This lets you work with Issues detected in ASM and follow your workflow using the ServiceNow interface.

> ℹ️
>
> This integration is bidirectional. Updates made in ServiceNow are seen in ASM just as updates made to Issues in ASM are visible in ServiceNow.

## integration-configuration

Get and install the **Mandiant Advantage Attack Surface Management** Integration from the [ServiceNow Store](https://store.servicenow.com/). Then, follow these steps in ServiceNow:

1. Navigate to **Security Operations > Integrations > Integration Configurations**.

2. Click **Configure** for the **Mandiant Advantage Attack Surface Management** integratio&#x6E;**.**

3. Enter the integration parameters:

   * **API Base URL** defaults to `http://www.virustotal.com/api/v3/asm`.

   * ASM **Access Key** and **Secret Key** are available in [**API Keys**](https://asm.advantage.mandiant.com/account/settings/api-keys) section of ASM **Account Settings**.

   * (Optional) Select to **Include Potential Issues** if you'd like to include unconfirmed Issues.

   * Enter a value to define the **Minimum** [**Severity**](../issues-guide/issues-severity-definitions.md) of Issues to import:
     * 1 = Critical
     * 2 = High
     * 3 = Medium (suggested)
     * 4 = Low
     * 5 = Informational

   * Enter a numeric value for the **Initial** **Lookback Days** setting. The default is 90.

   > ℹ️
   >
   > This setting only applies to the first run of the scheduled import job. Subsequent runs are performed on an incremental basis as defined in the **Vulnerable Item Import** page of ServiceNow.

   * Enter a string value representing the **Project ID** that you want to access.

   > ℹ️
   >
   > To identify a `project_id`, run the following curl command:
   >
   > ```
   > curl --location --request GET 'https:\
   > ///api/v1/projects' \
   > --header 'INTRIGUE_ACCESS_KEY: {<span>{intrigue_access_key}</span>}' \
   > --header 'INTRIGUE_SECRET_KEY: {<span>{intrigue_secret_key}</span>}'
   > ```
   >
   > For more information, see [Attack Surface Management API](https://gtidocs.readme.io/reference/get_projects).

4. Click **Submit**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_servicenow_configuration_20240614.png)

5. Navigate to **Mandiant ASM > Projects and Collections** and select the Collections to be imported.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_servicenow_management_20240614.png)

> ℹ️
>
> Collections must all be from the same Project.

6. Ensure you are in the *CMDB CI Class Models* application. Search for `sys_choice.list` in the Search field. Add three new Choices as follows:

   1. **Table**: `Allocated IP Address [cmdb_ci_allocated_ip_address]`

      ```
        **Element**: `discovery_source`

        **Label**: `VR-MandiantASM`

        **Value**: `VR-MandiantASM`
      ```

      ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_servicenow_ip_20240614.png)

   2. **Table**: `Unique Certificate [cmdb_ci_certificate]`

      ```
        **Element**: `discovery_source`

        **Label**: `VR-MandiantASM`

        **Value**: `VR-MandiantASM`
      ```

      ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_servicenow_certificate_20240614.png)

   3. **Table**: `DNS Name [cmdb_ci_dns_name]`

      **Element**: `discovery_source`

      **Label**: `VR-MandiantASM`

      **Value**: `VR-MandiantASM`

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_servicenow_dns_20240614.png)

7. Navigate to **Mandiant ASM > Vulnerable Item Import** and define the schedule you want to use. The default is six hours.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_servicenow_import_20240614.png)

8. Click **Update**. Alternatively, click **Execute Now** if you want to run the job immediately. 

## vulnerable-items-in-servicenow

Once integrated, you can view **Vulnerable Items** in ServiceNow:

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_servicenow_vulnerable_items_list_20240614.png)

To display more details and perform actions on an item, select a Vulnerable Item from the list.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_servicenow_vulnerable_item_20240614.png)

## troubleshooting-tips

To view application logs:

* In ServiceNow, open a failed **Project and Collections** import.
* Open the **Notes** tab.
* Review the logs.

To force an import using the original **Lookback Days** setting:

* In ServiceNow, search for the `x_mandi_asm_mandiant_attack_surface_management_integration.list` page.
* To reset the job last run date and force an update, manually clear the **Download Issues Since** field.

The next time the job runs, the original **Lookback Days** setting is used as the start date.

## asm-servicenow-field-mapping

| ASM Field            | ServiceNow Table                                    | ServiceNow Field             |
| -------------------- | --------------------------------------------------- | ---------------------------- |
| confidence           | Vulnerable Item Detection                           | Confirmed                    |
| summary/status\_new  | Vulnerable Item Detection                           | Source status                |
| id                   | Vulnerable Item Detection                           | Vulnerable Item/external\_id |
| details/proof        | Vulnerable Item Detection                           | Proof                        |
| name                 | Vulnerable Item Detection                           | Solution/source\_id          |
| identifiers/name     | Vulnerable Item Detection                           | Vulnerability                |
| details/name         | Vulnerable Item Detection                           | Vulnerability                |
| summary/status       | Vulnerable Item Detection                           | Status                       |
| first\_seen          | Vulnerable Item Detection                           | First found                  |
| details/remediation  | Vulnerable Item Detection                           | Solution summary             |
| last\_seen           | Vulnerable Item Detection                           | Last found                   |
| display\_name        | Mandiant ASM Projects and Collections Configuration | Display Name                 |
| project\_name        | Mandiant ASM Projects and Collections Configuration | Project Name                 |
| collection\_id       | Mandiant ASM Projects and Collections Configuration | Collection ID                |
| collection\_name     | Mandiant ASM Projects and Collections Configuration | Collection Name              |
| project\_id          | Mandiant ASM Projects and Collections Configuration | Project ID                   |
| details/remediation  | National Vulnerability Database Entry               | Solution                     |
| details/category     | National Vulnerability Database Entry               | Classification               |
| identifiers/name     | National Vulnerability Database Entry               | ID                           |
| details/pretty\_name | National Vulnerability Database Entry               | Name                         |
| details/severity     | National Vulnerability Database Entry               | Source Severity              |
| details/description  | National Vulnerability Database Entry               | Threat                       |
| details/severity     | National Vulnerability Database Entry               | Normalized Severity          |
| details/added        | National Vulnerability Database Entry               | Date Published               |
| details/pretty\_name | National Vulnerability Database Entry               | Summary                      |
| details/description  | National Vulnerability Database Entry               | Summary                      |
| details/vendor       | Third Party Vulnerability Entry                     | Vendor                       |
| details/added        | Third Party Vulnerability Entry                     | Date Published               |
| details/pretty\_name | Third Party Vulnerability Entry                     | Summary                      |
| details/description  | Third Party Vulnerability Entry                     | Summary                      |
| name                 | Third Party Vulnerability Entry                     | Preferred Solution           |
| details/name         | Third Party Vulnerability Entry                     | ID                           |
| details/severity     | Third Party Vulnerability Entry                     | Source Severity              |
| details/remediation  | Third Party Vulnerability Entry                     | Solution                     |
| details/severity     | Third Party Vulnerability Entry                     | Normalized Severity          |
| details/category     | Third Party Vulnerability Entry                     | Category                     |
| details/description  | Third Party Vulnerability Entry                     | Threat                       |
| category             | Third Party Vulnerability Entry                     | Classification               |
| details/description  | Third Party Vulnerability Entry                     | Name                         |
| details/remediation  | Vulnerability Solution                              | Description                  |
| name                 | Vulnerability Solution                              | Source ID                    |
| description          | Vulnerable Item                                     | Description                  |
| id                   | Vulnerable Item                                     | External ID                  |
| status               | Vulnerable Item                                     | Status                       |
| summary/pretty\_name | Vulnerable Item                                     | Short Description            |
| identifiers/name     | Vulnerable Item                                     | Vulnerability                |
| details/name         | Vulnerable Item                                     | Vulnerability                |
| summary/status       | Vulnerable Item                                     | State                        |

---

← [ASM Jira Integration](asm-jira-integration.md) · [up](../README.md) · [ASM Splunk Integration](asm-splunk-integration.md) →

*Archived from <https://gtidocs.virustotal.com/docs/asm-servicenow-integration>.*
