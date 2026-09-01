---
title: "ASM Google Cloud Integration"
source: https://gtidocs.virustotal.com/docs/asm-google-cloud-integration
slug: asm-google-cloud-integration
section: guides
group: "ASM"
updatedAt: 2025-09-26T09:48:33.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [ASM](../README.md) › [Inbound Integrations](../inbound-integrations.md) › ASM Google Cloud Integration

---

# asm-google-cloud-integration

> 🚧 Special privileges required
>
> This feature is only available to ASM administrators.

> ℹ️
>
> See how credentials for integrations are stored [here](asm-credential-security-details.md)

This document outlines the Google Cloud integration process with Attack Surface Management (ASM). Using this integration, you gain visibility of your Google Cloud assets and extended ecosystem for faster identification of new or unmanaged assets and remediation of vulnerabilities, misconfigurations, and exposures.

> 💡
>
> ### For customers with IT infrastructure across multiple clouds, Google Threat Intelligence recommends using the inbound integrations with AWS, Azure, and Google Cloud for a consolidated view of cloud and internet-facing assets.

The ASM Google Cloud integration leverages Google Cloud's service account impersonation. By creating a service account and delegating your account access, you'll be able to assume control of the service account and fetch the respective resources. This prevents both parties from being required to retain their credentials.

> ℹ️
>
> * ASM implements a form of [confused-deputy](https://en.wikipedia.org/wiki/Confused_deputy_problem) mitigation, which works by preventing the creation of the integration if an integration associated with the same service account already exists.\* If your Google Cloud organization is configured with an organization policy that restricts identities by domain, such as `iam.allowedPolicyMemberDomains`, you need to allow ASM’s Google Workspace Customer ID in the policy. This Customer ID is *C0439tmya.* For instructions on how to allow a specific Customer ID, see [Setting the organization policy](https://cloud.google.com/resource-manager/docs/organization-policy/restricting-domains#setting_the_organization_policy).

See [Google Cloud Related Entities in ASM](#google-cloud-related-entities-in-asm) to learn more about the Entities created in ASM using this integration.

## create-a-service-account

Follow either Method A or Method B to create a Google Cloud service account.

* **Method A:** [Create a Service Account through Google Cloud Console](#method-a-create-a-service-account-through-google-cloud-console)
* **Method B:** [Create a Service Account through gcloud CLI](#method-b-create-a-service-account-through-gcloud-cli)

Once a service account has been created, proceed to the instructions to [Create Google Cloud Integration within ASM](#create-google-cloud-integration-within-asm).

### method-a:-create-a-service-account-through-google-cloud-console

Execute the following steps in the Google Cloud's web console:

1. Once successfully authenticated with Google Cloud console through a user who has the appropriate permissions to create a service account and a role, browse to <https://console.cloud.google.com/iam-admin/roles>. Ensure the current project is the one you would like for the integration to access. If you are not in the correct project, navigate to the desired project.

   ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_select_project_20240612.png)

2. Create a Role using the following process:

   1. Click **+Create role** .

      ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_create_role_20240612.png)

   2. In the **Create Role** interface, fill in the following fields and click **+Add permissions** .

      * **Title**: Friendly title for the role, for example, *ASM GCP Integration Role*
      * **Description**: Short description describing what the role does
      * **ID**: ID for the role, for example, *asm\_gcp\_integration-role*
      * **Role launch stage**: General Availability

      ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_permissions_20240612.png)

   3. In the **Add permissions** sub-menu, add the following permissions:

      * `cloudasset.assets.listResource`
      * `dns.managedZones.list`
      * `dns.resourceRecordSets.list`
      * `apigateway.apiconfigs.get`
      * `resourcemanager.projects.get`

        > ℹ️
        >
        > * The easiest way to do this is to copy the permission name, for example, `cloudasset.assets.listResource` and paste it into the **Enter property name or value** section and then click enter. When the role appears, click the checkbox next to it. Repeat this process for each permission.\* After clicking the checkbox, clear the filter before searching for the next permission, or else the new permission won't show up.

      ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_permissions_add1_20240612.png)

   4. After all the permissions have been added, click **Add**.

      ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_permissions_add2_20240612.png)

   5. Confirm the **Create Role** interface shows that all five permissions have been assigned and click **Create**.

      ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_create_role_with_permissions_20240612.png)

3. Create a service account using the following process:

   1. From the **IAM & Admin** menu, click the **Service Accounts** tab.

      ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_create_service_account1_20240612.png)
   2. Click **+ Create service account**.

      ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_create_service_account2_20240612.png)
   3. In the **Create service account** interface, fill in the following fields for the **Service account details** section and click **Create and continue**.

      * **Service account name**: Friendly name for the service account.
      * **Service account ID**: This is automatically populated based on the first field.
      * **Service account description**: Quick note providing a description of what this service account does.

      ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_create_and_continue_20240612.png)
   4. For the **Grant this service account access to project** section, click **Select a role** and, in the filter, type the name of the role created earlier in this section, for example, *ASM GCP Integration Role*.

      ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_manage_roles_20240612.png)
   5. Select the role and click **Continue**.

      ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_manage_roles_continue_20240612.png)
   6. Under the **Grant users access to this service account** section, for the **Service account users role** field, enter the Mandiant Google Cloud service account email and click **Done**.

      > 🛑
      >
      > The Mandiant Google Cloud service account email is `gcp-inbound-integration@asm-mcp-prod-01-f8ec.iam.gserviceaccount.com`.

      ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_done_20240612.png)
   7. Once the Service Account is created, navigate to the **Service accounts** page (you are automatically redirected after clicking **Done** in the previous step), and click the email link belonging to the service account you just created.

      ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_email_20240612.png)

      > ℹ️
      >
      > Make a note of the email belonging to your service account (not the `gcp-inbound-integration@` service account) as you'll need it in the next section, [Create Google Cloud Integration within ASM](#create-google-cloud-integration-within-asm).
   8. Click the **Permissions** tab in the navigation bar. A list of Principals appears.

      ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_permissions1_20240612.png)
   9. Ensure that the **View by principals** tab is selected and that the Mandiant Google Cloud service account email is listed.

      ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_view_by_principals_20240612.png)
   10. Click the pencil icon associated with this Principal.

   ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_edit_icon_20240612.png)

   11. Under the **Assign roles** section, click **+ Add another role** and choose **Service Account Token Creator** from the drop-down menu. Click **Save**.

   ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_assign_roles_20240612.png)

4. Lastly, enable the APIs for the following services by clicking each of the respective service hyperlinks and clicking **Enable**.

   * [Cloud Asset API](https://console.cloud.google.com/marketplace/product/google/cloudasset.googleapis.com): This allows the integration to fetch resources through Cloud Asset inventory.
   * [Cloud Resource Manager API](https://console.cloud.google.com/marketplace/product/google/cloudresourcemanager.googleapis.com): This allows the integration to fetch the list of projects.
   * [Cloud DNS API](https://console.cloud.google.com/marketplace/product/google/dns.googleapis.com): This allows you to translate domain name requests into IP addresses. 
   * [API Gateway API](https://console.cloud.google.com/marketplace/product/google/apigateway.googleapis.com): This allows the integration to secure and manage REST APIs.

     ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_asset_api_20240612.png)

### method-b:-create-a-service-account-through-gcloud-cli

1. Make sure you are authenticated with Google Cloud through the gcloud CLI by running:

   ```
   gcloud auth list
   ```

   The following output should be returned:

   ```
   Credentialed Accounts
   ACTIVE  ACCOUNT
   *       user.account@org.tld

   To set the active account, run:
       $ gcloud config set account 'ACCOUNT'
   ```
2. Set the project for which you would like the integration to fetch resources by running:

   ```
   gcloud config set project <var>PROJECT_ID</var>
   ```

   > ℹ️
   >
   > `PROJECT_ID` is a variable. Be sure to use the Project ID and not the Project name.

   Successful output looks like the following:

   ```
   Updated property [core/project].
   ```

   If you see the following output, it means that the project cannot be found. This is most likely because the Project Name instead of the Project ID was used.

   ```
   WARNING: You do not appear to have access to project <var>[REQUESTED-PROJECT-HERE]</var> or it does not exist.
   Are you sure you wish to set property [core/project] to REQUESTED<var>-PROJECT-HERE</var>?

   Do you want to continue (Y/n)?
   ```

   If you would like to see all the projects in your organization and their respective Project IDs, run the following command:

   ```
   gcloud projects list
   ```
3. Create a custom role within Google Cloud that follows the principle of least privileges.

   Save the contents of the following YAML configuration:

   ```
   title: masm-integration-role
   description: integration role for the mandiant asm gcp integration
   stage: GA
   includedPermissions:
   - cloudasset.assets.listResource
   - dns.managedZones.list
   - dns.resourceRecordSets.list
   - resourcemanager.projects.get
   - apigateway.apiconfigs.get
   ```

   Using the gcloud CLI, run the following command:

   ```
   gcloud iam roles create masm_integration_role --project <var>PROJECT_ID</var> --file=role.yaml
   ```

   > ℹ️
   >
   > `PROJECT_ID` is a variable. Be sure to use the Project ID and not the Project name.
4. Create a service account.

   Using the gcloud CLI, run the following command:

   ```
   gcloud iam service-accounts create masm-integration-svc-account --description="Service Account for MASM GCP Integration" --display-name="MASM GCP Integration Service Account"
   ```

   > ℹ️
   >
   > `masm-integration-svc-account` is the name of the service account created. You can use any value for this option, however, ensure to swap it in the next set of instructions.

   If successful, the following output should be returned:

   ```
   Created service account [masm-integration-svc-account].
   ```
5. Bind the role created in [Step 3](asm-google-cloud-integration.md#method-b:-create-a-service-account-through-gcloud-cli) to the service account created in the previous step.

   Using the gcloud CLI, run the following command:

   ```
   gcloud projects add-iam-policy-binding <var>PROJECT_ID</var> --member="serviceAccount:masm-integration-svc-account@<var>PROJECT_ID</var>.iam.gserviceaccount.com" --role="projects/<var>PROJECT_ID</var>/roles/masm_integration_role"
   ```

   > ℹ️
   >
   > `PROJECT_ID` is a variable. Be sure to use the Project ID and not the Project name. There are three locations where this needs to be replaced.

   If successful, the following output should be returned:

   ```
   Updated IAM policy for project [<var>PROJECT_ID</var>].
   bindings:
   - members:
     - serviceAccount:masm-integration-svc-account@<var>PROJECT_ID</var>.iam.gserviceaccount.com
     role: projects/<var>PROJECT_ID</var>/roles/masm_integration
   ...
   ```
6. Allow ASM to impersonate your service account.

   Using the gcloud CLI, run the following command:

   ```
   gcloud iam service-accounts add-iam-policy-binding masm-integration-svc-account@<var>PROJECT_ID</var>.iam.gserviceaccount.com --member="serviceAccount:gcp-inbound-integration@asm-mcp-prod-01-f8ec.iam.gserviceaccount.com" --role="roles/iam.serviceAccountTokenCreator"
   ```

   > ℹ️
   >
   > `gcp-inbound-integration@asm-mcp-prod-01-f8ec.iam.gserviceaccount.com` is the email of the service account belonging to ASM.

   If successful, the following output should be returned:

   ```
   Updated IAM policy for serviceAccount [masm-integration-svc-account@<var>PROJECT_ID</var>.iam.gserviceaccount.com].
   bindings:
   - members:
     - serviceAccount:gcp-inbound-integration@asm-mcp-prod-01-f8ec.iam.gserviceaccount.com
     role: roles/iam.serviceAccountTokenCreator
   ...
   ```
7. Enable the `Cloud Asset API`, `Cloud Resource Manager API`, `Cloud DNS API`, and `API Gateway API` services. Using the gcloud CLI, run the following commands:

   ```
   gcloud services enable cloudresourcemanager.googleapis.com
   gcloud services enable cloudasset.googleapis.com 
   gcloud services enable dns.googleapis.com
   gcloud services enable apigateway.googleapis.com
   ```

   If successful, each command should return output similar to:

   ```
   Operation "operations/acat.p2-11111111111-88a9d5b4-c262-40fa-aeee-be6029ebfef3" finished successfully.
   ```

   If no response is returned, it is most likely because the service was already enabled.

## create-google-cloud-integration-within-asm

The following steps take place within ASM's Platform. It's assumed that a Google Cloud service account was created as documented in the [Create a Service Account](#create-a-service-account) section:

1. From the **Projects and Settings** menu in ASM, select the appropriate Project then click **Account Settings**.

   ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_account_settings_20240504.png)

2. Click **Integrations**.

3. From **Inbound Integrations**, click **Add New** for Google Cloud.

   ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_add_20240606.png)

4. In the **Email** field, input the email of the Google Cloud service account, and click **Connect**.

   After successful integration, you should see an "Integration created" message:

   ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_integration_verified_20240612.png)

   > ℹ️
   >
   > If you see an error message, instead of an "Integration created" success message, the issue could be in how the Google Cloud service account was created. The most common reason would be to forget to grant the Google Cloud service account the [Service Account Token Creator](#method-a-create-a-service-account-through-google-cloud-console) role.

5. Connect the integration to the appropriate Collectio&#x6E;**.**

   1. Click **Collections** and click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/threatprofile_engine_icon_20240509.svg) **Collection Settings** for the Collection that you want to connect the integration to.

      ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_collections_20240604.png)
   2. Select the **Integrations** tab.

      ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_configurations_20240604.png)
   3. Select **Connect Integration** and **Link** the integration.

      ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_setup_20240605.png)

      The integration is immediately added to the Collection.

      > 💡
>
> ### Click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_delete_icon.svg) to remove the integration from this Collection. ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_delete_20240604.png)
   4. Click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/threatprofile_close_icon_20240509.svg) to close the **Connect Integration** pane. Click **Scan** **Collection** to update your Collection with the current settings and integrations. Otherwise, your newly configured integration is incorporated at your regularly scheduled scan interval.

      ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_gcp_scan_20240604.png)

## google-cloud-related-entities-in-asm

The Entities created from the Google Cloud inbound integration are as follows:

| Entity Name | Google Cloud Asset Name | Relevant Raw JSON Fields | Dependencies |
| --- | --- | --- | --- |
| GcpApiGateway | API Gateway | <ul><br><li><br><code>name</code>: The hostname of the <span class="ko-glossary-term" data-toggle="popover" data-content="Application Programming Interface" data-original-title="" title="">API</span> Gateway. For example,<br><var>gateway-1337-66i59fug.uc.gateway.dev</var>.<br></li><br><li><code>project</code></li><br><li><code>gateway_name</code>: Friendly name of the API Gateway.</li><br><li><code>location</code></li><br><li><code>created_time</code></li><br><li><code>api_config</code></li><br><li><code>scoped</code></li><br><li><code>cloud_hosted</code></li><br></ul> | Only API Gateways which are in the ACTIVE state are created as Entities. |
| GcpAppEngineApplication | App Engine Application | <ul><br><li><br><code>name</code>: apps/<br><var>project_name</var><br></li><br><li><code>project</code></li><br><li><code>application_hostname</code></li><br><li><code>services</code>: List of services running under the App Engine.</li><br><li><code>scoped</code></li><br><li><code>cloud_hosted</code></li><br></ul> | There can only be one App Engine Application per project. |
| GcpCloudFunction | Cloud Function | <ul><br><li><code>name</code></li><br><li><code>project</code></li><br><li><code>http_invocation_url</code></li><br><li><code>additional_info</code>: Information from the resource JSON.</li><br><li><code>runtime</code></li><br><li><code>scoped</code></li><br><li><code>cloud_hosted</code></li><br></ul> | Only Cloud Functions which are triggered using HTTP are created as Entities as they are deemed to be public facing. Functions configured with other triggers, such as "write to bucket," are ignored. |
| GcpCloudSQLInstance | Cloud SQL Instance | <ul><br><li><code>name</code></li><br><li><code>project</code></li><br><li><code>ip_addresses</code></li><br><li><code>database_version</code></li><br><li><code>region</code></li><br><li><code>cloud_hosted</code></li><br><li><code>scoped</code></li><br></ul> | Only Cloud SQL Instances with public IP addresses and in the RUNNABLE state are created as Entities. |
| GcpComputeEngineInstance | Compute Engine | <ul><br><li><br><code>name</code>:<br><var>project</var>/<br><var>name</var><br></li><br><li><code>project</code></li><br><li><code>zone</code></li><br><li><code>public_ip_addresses</code></li><br><li><code>cloud_hosted</code></li><br><li><code>scoped</code></li><br></ul> | Only Compute Engine Instances with public IP addresses and in the RUNNING state are created as Entities. |
| GcpStorageBucket | Storage Bucket | <ul><br><li><code>name</code></li><br><li><code>bucket_url</code></li><br><li><code>project</code></li><br><li><code>location</code></li><br><li><code>anonymous_access_forbidden</code></li><br><li><code>scoped</code></li><br><li><code>cloud_hosted</code></li><br></ul> | If <code>anonymous_access_forbidden</code> is <code>false</code>, a World Readable Google Cloud Storage Bucket Issue is created during the enrichment process. |

---

← [ASM GoDaddy Integration](asm-godaddy-integration.md) · [up](../README.md) · [Scale Google Cloud Integration](scale-google-cloud-integration.md) →

*Archived from <https://gtidocs.virustotal.com/docs/asm-google-cloud-integration>.*
