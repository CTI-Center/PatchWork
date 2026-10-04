---
title: "ASM AWS Integration"
source: https://gtidocs.virustotal.com/docs/asm-aws-integration
slug: asm-aws-integration
section: guides
group: "ASM"
updatedAt: 2025-09-25T00:28:59.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [ASM](../README.md) › [Inbound Integrations](../inbound-integrations.md) › ASM AWS Integration

---

# asm-aws-integration

> 🚧 Special privileges required
>
> This feature is only available to ASM administrators.

> ℹ️
>
> See how credentials for integrations are stored [here](asm-credential-security-details.md)

> ℹ️
>
> This integration is not currently supported for AWS GovCloud (US) users.

To provide a more thorough view of your inventory, Attack Surface Management (ASM) can integrate with Amazon Web Services (AWS) to retrieve the following:

* Public EC2 instances 
* S3 buckets

  > ℹ️
  >
  > ASM confirms whether S3 buckets are publicly accessible and creates relevant Issues.
* Route 53 zones
* Amazon Relational Database Service (RDS DB) instances

  > ℹ️
  >
  > ASM uses Mandiant Security Integrations-as-a-Service (MSI) to collect RDS DB data.

Adding the AWS integration requires three steps: 

1. [Create the policy in AWS](#create-the-policy-in-aws)
2. [Create an access method for ASM](#authenticate-using-cross-account-access)
3. [Provide AWS credentials to ASM](#provide-aws-credentials-to-asm)

## create-the-policy-in-aws

You first need to create the policy in AWS for ASM to use.

1. Authenticate to AWS and browse to **Identity and Access Management (IAM)** in the AWS console.
2. Go to **Access Management > Policies**. Alternatively, access <https://us-east-1.console.aws.amazon.com/iam/home#/policies>.
3. Click **Create policy**.

> ℹ️
>
> You must have permissions to create roles and policies within AWS.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_aws_policies_20240605.png)

4. Select **JSON**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_aws_permissions_20240605.png)

5. Copy and paste the following JSON snippet into the text field and click **Next**.

   ```
   {
      <span>"Version"</span>:<span>"2012-10-17"</span>,
      <span>"Statement"</span>:[
         {
            <span>"Effect"</span>:<span>"Allow"</span>,
            <span>"Action"</span>:[
               <span>"route53:ListHostedZones"</span>,
               <span>"route53:ListResourceRecordSets"</span>
            ],
            <span>"Resource"</span>:<span>"*"</span>
         },
         {
            <span>"Effect"</span>:<span>"Allow"</span>,
            <span>"Action"</span>:<span>"s3:ListAllMyBuckets"</span>,
            <span>"Resource"</span>:<span>"*"</span>
         },
         {
            <span>"Effect"</span>:<span>"Allow"</span>,
            <span>"Action"</span>:<span>"ec2:DescribeInstances"</span>,
            <span>"Resource"</span>:<span>"*"</span>
         }, 
         {
            <span>"Effect"</span>:<span>"Allow"</span>,  
            <span>"Action"</span>:<span>"rds:DescribeDBInstances"</span>,  
            <span>"Resource"</span>:<span>"*"</span>  
         }
      ]
   }
   ```

6. On the **Review and create** page, populate the following **Policy details** fields:

   * **Policy name**: Name for the policy. 

   > ℹ️
   >
   > Make a note of the name that you use as it is needed in the next section.

   * **Description -*optional***: Description of the policy.

7. Review the **Permissions defined in this policy** section and click **Create policy**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_aws_review_create_20240605.png)

## authenticate-using-cross-account-access

Once the AWS Policy is created, you must provide a method for ASM to authenticate with your AWS Accounts. ASM uses the cross-account access from the preceding section to automatically generate temporary, short-lived tokens whenever it needs to integrate with your AWS account. This access method eliminates the need for any additional access keys.

1. In the AWS console, browse to **Identity and Access Management (IAM)**. 
2. Go to **Access Management > Roles**. Alternatively, access [<https://us-east-1.console.aws.amazon.com/iam/home#/roles>](https://us-east-1.console.aws.amazon.com/iam/home#/roles).
3. Click **Create role**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_aws_roles_20240605.png)

4. On the **Select trusted entity** page:

   1. Select the **AWS Account** tile. 
   2. Select the **Another AWS account** radio button.
   3. In the **Account ID** field, enter `220283773642`.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_aws_trusted_entity_20240605.png)

5. Under **Options**, select the checkbox requiring use of an external ID. Copy the **External ID** from ASM and paste it here.

> ℹ️
>
> Requiring an external ID is an AWS best practice when a third party (ASM, in this case) assumes the role.\
> There is one external ID per ASM project.\
> To access the **AWS External ID** from ASM:
>
> * From the **Projects and Settings** menu in ASM, select the appropriate Project then click **Account Settings**.
> * Click **Integrations**.
> * Click **Add New** for **AWS (Roles)**.
> * Click **Copy Key**.
>
> ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_aws_external_id_20240605.png)

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_aws_options_20240605.png)

6. Click **Next**.
7. On the **Add permissions** page, search for the name of the policy that you created in the preceding section. Once the search populates, select the checkbox associated with the policy.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_aws_add_permissions_20240605.png)

8. Click **Next**. 
9. On the **Name, review and create** page:\
   a. In the **Role name** field, enter a meaningful name.\
   b. Confirm that the **Step 1: Select trusted** **entities** section shows `"AWS": "220283773642"` and `"sts:ExternalID": "AWS External ID"`.\
   c. Click **Create role**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_aws_review_create_20240605.png)

10. Select the newly created role and make a note of the **Role ARN** to be used when [providing AWS Credentials to ASM](#provide-aws-credentials-to-asm).

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_aws_role_arn_20240605.png)

## provide-aws-credentials-to-asm

Now that you have AWS ready to accept connection requests from ASM, it's time to add the appropriate AWS credentials into your Project.

1. From the **Projects and Settings** menu in ASM, select the appropriate Project then click **Account Settings**.
2. Click **Integrations**.
3. Click **Add New** for the appropriate connection method:

   * Recommended: **AWS (Roles)**
   * **AWS (Keys)**

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_aws_integrations_20240603.png)

4. Depending on what you select in the preceding step:
   * Enter the Role ARN value from your AWS account into the appropriate field.
   * Enter the AWS **Access Key ID** and AWS **Secret Access Key** into the appropriate fields.
5. Click **Connect**.
6. Connect the integration to the appropriate Collectio&#x6E;**.**

   1. Click **Collections** and click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/threatprofile_engine_icon_20240509.svg)  **Collection Settings** for the Collection that you want to connect the integration to.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_aws_collections_20240604.png)

2. Select the **Integrations** tab.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_aws_configurations_20240604.png)

3. Select **Connect Integration** and **Link** the integration.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_aws_setup_20240605.png)

The integration is immediately added to the Collection.

> 💡
>
> ### Click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_akamai_delete_icon.svg) to remove the integration from this Collection. ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_aws_delete_20240604.png)

4. Click ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/threatprofile_close_icon_20240509.svg) to close the **Connect Integration** pane. Click **Scan** **Collection** to update your Collection with the current settings and integrations. Otherwise, your newly configured integration is incorporated at your regularly scheduled scan interval.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_aws_scan_20240604.png)

---

← [ASM Credential Security Details](asm-credential-security-details.md) · [up](../README.md) · [Scale AWS Integration Across AWS Organizations](scale-aws-integration-across-aws-organizations.md) →

*Archived from <https://gtidocs.virustotal.com/docs/asm-aws-integration>.*
