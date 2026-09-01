---
title: "Scale AWS Integration Across AWS Organizations"
source: https://gtidocs.virustotal.com/docs/scale-aws-integration-across-aws-organizations
slug: scale-aws-integration-across-aws-organizations
section: guides
group: "ASM"
updatedAt: 2025-09-25T00:29:00.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [ASM](../README.md) › [Inbound Integrations](../inbound-integrations.md) › Scale AWS Integration Across AWS Organizations

---

# scale-aws-integration-across-aws-organizations

> ℹ️
>
> See how credentials for integrations are stored [here](asm-credential-security-details.md)

> ℹ️
>
> The following information is not intended to apply to all variations of customer environments. There can be several factors that may prohibit you from achieving the intended results. As such, this document should be treated as general guidance. These instructions were written for an out-of-box AWS organization containing a single organization unit. If your organization differs, please adapt the instructions to fit your requirements.

There are two steps in this process:

1. [Create the Stack Set](#create-the-stack-set)
2. [Gather the Role ARNs](#gather-the-role-arns)

## create-the-stack-set

1. Sign in to the AWS Management Console as the root user.
2. Navigate to the **CloudFormation** service and select **StackSets**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_scale_aws_stackset_20240927.png)

3. Click **Create StackSet**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_scale_aws_create_stackset_20240927.png)

4. Under the **Specify template**, select **Upload a template file**, upload this [CloudFormation template file](https://dyzz9obi78pm5.cloudfront.net/app/image/id/66c8986f7d85fddd810af7c2/n/cloudformation-template-new.yaml), and click **Next**.

> ℹ️
>
> Ensure you are using the version of this template file that allows the `masm-access-policy` policy access to `ec2:DescribeInstances`, `route53:ListHostedZones`, `route53:ListResourceRecordSets`, `s3:ListAllMyBuckets`, and `rds:DescribeDBInstances`.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_scale_aws_template.png)

5. Populate the following fields and click **Next**.

   1. **StackSet name**: This should be a memorable value such as *Mandiant-ASM-Integration-StackSet*.
   2. **StackSet description**
   3. **External ID**

> 💡
>
> ### Requiring an External ID is an AWS best practice when a third party (ASM, in this case) assumes the role.

> ℹ️ External ID per ASM
>
> * There is one External ID per ASM project.
>
> * To access the **AWS External ID** from ASM:
>
> 1. From the **Projects and Settings** menu in ASM, select the appropriate Project then click Account Settings.
> 2. Click **Integrations**.
> 3. Click **Add New** for **AWS (Roles)**.
> 4. Click **Copy Key**.
>
>    ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_scale_aws_external_id_20240927.png)

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_scale_aws_stackset_details_20240927.png)

6. Under **Execution configuration**, select **Active**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_scale_aws_configure_20240927.png)

7. Define **Set deployment options** and click **Next**.
   1. **Deployment targets**:
      1. **Deploy to organization** (default): Deploys the stack to all accounts in the organization.
      2. **Deploy to organizational units (OUs)**: Deploys the stack to specific organizational units.
         > ℹ️
         >
         > StackSets don't create roles in AWS management by default. The user must use a combination of OUs and account ID filters in the "Deployment target" section to prevent the StackSet from running against the management account. Otherwise the operation will fail.
   2. **Specify regions**: As IAM is Global, you can select any single region of your choice.
      > ℹ️
      >
      > IAM roles have a global scope therefore you must should specify one region to run the StackSet in. Otherwise the operation will fail.
   3. **Deployment options**: The default options are shown here, but can be modified to suit the needs of your organization.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_scale_aws_deployment_20240927.png)

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_scalw_aws_deployment_options_20240927.png)

8. Review and click **Submit**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_scale_aws_review_20240927.png)

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_scale_aws_executio_configuration_20240927.png)

## gather-the-role-arns

The ASM [AWS Integration](asm-aws-integration.md) requires you to input the **Role ARN** associated with the **Mandiant-ASM-Access Role** belonging to each child account the StackSet was deployed to.

This list is easy to produce as the name of the role are the same across all accounts and AWS' Role ARNs follow a specific format.

Using the parent account in the AWS CLI, run the following command to obtain the Role ARNs associated with the AWS accounts belonging to your organization: 

```
aws cloudformation list-stack-instances --stack-set-name Mandiant-ASM-Integration-StackSet | jq -r '.Summaries[] | select(.StackInstanceStatus.DetailedStatus == "SUCCEEDED") | .Account | "arn:aws:iam::\(.):role/Mandiant-ASM-Access"'
```

> ℹ️
>
> * The `jq` utility parses the resulting JSON and forms the **Role ARN**.\* If the Role Name was changed from what is listed in the [CloudFormation template file](#create-the-stack-set), be sure to update the preceding command to include the correct Role Name.

Sample Result (where each line is an individual **Role ARN**):

```
arn:aws:iam::11111111111:role/Mandiant-ASM-Access
arn:aws:iam::22222222222:role/Mandiant-ASM-Access
arn:aws:iam::33333333333:role/Mandiant-ASM-Access
```

Create a new [AWS Integration](asm-aws-integration.md) for every **Role ARN** listed. If there are too many, it's highly suggested to script this process. The [API Docs](https://gtidocs.readme.io/reference/get_projects) can help provide more insight.

---

← [ASM AWS Integration](asm-aws-integration.md) · [up](../README.md) · [ASM Azure Integration](asm-azure-integration.md) →

*Archived from <https://gtidocs.virustotal.com/docs/scale-aws-integration-across-aws-organizations>.*
