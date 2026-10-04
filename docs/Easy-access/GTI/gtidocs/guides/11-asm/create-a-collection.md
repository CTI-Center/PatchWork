---
title: "Create a Collection"
source: https://gtidocs.virustotal.com/docs/create-a-collection
slug: create-a-collection
section: guides
group: "ASM"
updatedAt: 2025-09-25T16:58:13.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [ASM](README.md) › Create a Collection

---

# create-a-collection

> ℹ️ Collection configuration
>
> It is available for paid Attack Surface Management customers.
>
> If you would like to upgrade to a more feature-rich account, send a message using our contact form, **<https://www.virustotal.com/gui/contact-us>**.

A Scan Workflow in Attack Surface Management (ASM) is a predefined set of tasks that are applied to a Collection. When you create a new Collection, you're required to select a Workflow. Various Scan Workflow templates are provided to guide you toward the setup that best suits your needs. Depending on the template you select, you're prompted to supply Seeds and integrations relevant to that selection. Once a Collection is created, the name of the Workflow associated with the Collection is available on the Collection Settings page.

> ℹ️ Note
>
> * Collections created before the availability of Workflows are linked to Legacy Workflows.
> * Once a Collection is created, the Workflow cannot be changed.

## scan-workflow-templates

The following predefined Scan Workflows are available to aid in Collection customization.

> ℹ️ Scan Workflows
>
> * Integrations for the **External Discovery & Assessment** Workflow only retrieve DNS zones from cloud or DNS providers.
> * Integrations for **Authenticated Cloud Discovery & Assessment** Workflow retrieve the full range of discoverable asset types from each respective cloud provider.
> * Each Workflow accepts specific integrations and Seed types. For more information, see the [Workflow Seeds table](#workflow-seeds).

* ### External Discovery & Assessment (Standard)

Identify shadow IT or unknown assets and vulnerabilities.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_external_discovery_assessment_20240426.png)

> ℹ️ Cloud integrations linked to this Workflow only pull in DNS records
>
> Also, when you link to cloud integrations using this Workflow, an extra Collection is created for every linked cloud integration using the **Authenticated Cloud Discovery & Assessment** Workflow. Supported cloud integrations include:
>
> * [AWS](inbound-integrations/asm-aws-integration.md)
> * [Azure](inbound-integrations/asm-azure-integration.md)
> * [Google Cloud](inbound-integrations/asm-google-cloud-integration.md)

* ### Authenticated Cloud Discovery & Assessment

  Identify vulnerabilities across your cloud providers.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_authenticated_cloud_discovery_assessment_20240426.png)

> ℹ️
>
> Cloud integrations linked to this Workflow pull in applicable cloud assets, such as Storage Buckets and Virtual Machine instances, in addition to DNS records.

* ### Code Repository Discovery & Assessment (Beta)

  Identify your company’s known accounts for secrets and discover unknown rogue repositories.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_code_repository_discovery_assessment_20240426.png)

> ℹ️
>
> This Workflow is used with GitHub. GitHub can be linked through [integration](inbound-integrations/asm-github-integration.md), or by Seed: `GithubAccount` or `GithubRepository`.

* ### Suspicious Domain Discovery (Beta)

  Identify unknown suspicious properties on the web including typosquats and punycode domains.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_suspicious_domain_discovery_20240426.png)

* ### Mobile App Discovery (Beta)

  Identify Android and iOS Apps tagged with your organization's brand keywords hosted in commonly used application marketplaces.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_mobile_app_discovery_20240426.png)

* ### Web Application Discovery (Beta)

  Identify web application endpoints derived from URLs. 

> ℹ️ Discovery methods
>
> They uses a recursive search feature for identifying additional assets. This recursive search works as follows:
>
> 1. Fetch the base URL and the scan responses for additional URLs. 
> 2. Log all returned URLs in the Entity details for the base URL.
> 3. Fetch and scan all returned URLs for additional URLs and log new URLs in the Entity details.
>    This recursive process continues until no additional new URLs are found, or until a predefined timeout duration is reached.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_web_application_discovery_202240426.png)

* ### Third Party Monitoring (Read Only)

  Monitor your supply chain. For more information, see [Third Party Monitoring Workflow](create-a-collection/third-party-monitoring-workflow.md).

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_third_party_monitoring_20240426.png)

Two additional Scan Workflows may be observed, but are not available for selection:

* **Legacy**: This Workflow applies to all Collections that existed before Scan Workflows were introduced to the collection creation process.
* **Freemium Discovery**: This Workflow applies to all Freemium Collections.

## create-a-collection-using-a-scan-workflow

1. In ASM, select **Settings** from the **Collections** menu.

2. Click **+ Create New Collection**.

   > ℹ️
>
> The **Third Party Monitoring** Workflow follows a different set of steps. For more information, see the "Create a Collection for Third Party Monitoring" section of [Third Party Monitoring Workflow](create-a-collection/third-party-monitoring-workflow.md).

3. Enter a title for your Collection and choose the [Scan Workflow](#scan-workflow-templates) that best suits your needs for this particular task.

   > ℹ️
>
> If you do not title a new Collection, a title is auto-generated.

4. Click **Next**.

   ![Collection Title and Scan Workflow configuration](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_create_collection_20240426.png)

5. **Add Seeds**, as necessary. Enter a [Seed](understanding-attack-surface-management-seeds.md) and select the **Seed Type** from the drop-down. You can add multiple Seeds using **+** **Add Another**.

   > ℹ️
>
> Accepted Seed types are specific to the Scan Workflow that you have selected. For more information, see the [Workflow Seeds table](#workflow-seeds).

   > 💡
>
> ### Seeds
>
> * Seeds can be uploaded from a CSV file. Download our [CSV Seed](https://d383cql5uq169w.cloudfront.net/app/image/pid/620d7e13ccb103e8557b25b0/id/62e7f30129f3d576b36b24e7/n/exports-seed-csv-example.csv) template or create your own CSV file with two columns. The first row must have `TYPE,NAME` and each subsequent row must have a comma-separated type-name pair. For example:
>
> ```
> TYPE,NAME
> Domain,intrigue.io
> Domain,mandiant.com
> ```
>
> * Capitalization matters when uploading a CSV file of Seeds.

6. **Connect Integration**, if appropriate.

   > 💡
>
> If integrations have already been added to the current project, they are available using **Link**. Otherwise, you can add an integration using **Set Up Another** or **Set Up**.

7. Click **Create Collection** to save without starting a scan right away or click **Create & Run Collection** to initiate the first scan for this new Collection.

   > ℹ️ Collection configurations
   >
   > * Collection scans run for a maximum of 72 hours.
   > * If you choose **Create Collection**, you're directed to the [Collection Settings](create-a-collection/customize-collections.md) for this Collection where you can configure Collection settings before the first scan. In specific, you may choose to disable specific Issue types before scanning begins.
   > * The **Create & Run Collection** option is not available for the **Third Party Monitoring** Workflow.

   ![New Collection Seed and Integration configuration](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_setup_collection_20240426.png)

## workflow-seeds

The following table outlines which integrations and Seeds are accepted by each Workflow.

| Seed ↓ Workflow →                  | External Discovery & Assessment (Standard) | Authenticated Cloud Discovery & Assessment | Code Repository Discovery & Assessment (Beta) | Suspicious Domain Discovery (Beta) | Mobile App Discovery (Beta) | Web Application Discovery (Beta) | Third Party Monitoring (Read Only) |
| ---------------------------------- | ------------------------------------------ | ------------------------------------------ | --------------------------------------------- | ---------------------------------- | --------------------------- | -------------------------------- | ---------------------------------- |
| Integrations available to be added | All Cloud and DNS Integrations             | All Cloud Integrations                     | GitHub Integration Only                       | None                               | None                        | None                             | None                               |
| `DnsRecord`                        | ✔                                          |                                            |                                               |                                    |                             |                                  |                                    |
| `Domain`                           | ✔                                          |                                            |                                               | ✔                                  |                             |                                  |                                    |
| `IpAddress`                        | ✔                                          |                                            |                                               |                                    |                             |                                  |                                    |
| `NetBlock`                         | ✔                                          |                                            |                                               |                                    |                             |                                  |                                    |
| `Uri`                              | ✔                                          |                                            |                                               |                                    |                             | ✔                                |                                    |
| `Nameserver`                       | ✔                                          |                                            |                                               |                                    |                             |                                  |                                    |
| `UniqueKeyword`                    | ✔                                          |                                            | ✔                                             |                                    | ✔                           |                                  |                                    |
| `GithubAccount`                    |                                            |                                            | ✔                                             |                                    |                             |                                  |                                    |
| `GithubRepository`                 |                                            | ✔                                          |                                               |                                    |                             |                                  |                                    |

> ℹ️
>
> The **Legacy** Workflow supports all [inbound integrations](inbound-integrations.md) and all the Seeds listed in this table as well as `ApiEndpoint`, `UniqueToken`, `AwsS3Bucket`, `EmailAddress`, and `AutonomousSystem`.

## modify-an-existing-collection

1. In ASM, navigate to your Collections by selecting **Settings** from the **Collections** menu.
2. Select **Settings** for the Collection that you want to modify.
3. Modify the Collection as necessary.

---

← [Understanding Attack Surface Management Seeds](understanding-attack-surface-management-seeds.md) · [up](README.md) · [Collections Tips and Tricks](create-a-collection/collections-tips-and-tricks.md) →

*Archived from <https://gtidocs.virustotal.com/docs/create-a-collection>.*
