---
title: "Collections Tips and Tricks"
source: https://gtidocs.virustotal.com/docs/collections-tips-and-tricks
slug: collections-tips-and-tricks
section: guides
group: "ASM"
updatedAt: 2025-09-25T01:58:41.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [ASM](../README.md) › [Create a Collection](../create-a-collection.md) › Collections Tips and Tricks

---

# collections-tips-and-tricks

Collections within Attack Surface Management (ASM) define the scope, type of data, and discovery task workflows perform.

Access control can be configured at the Collection, Project, and Organization level in ASM. If you have requirements around controlling access, make sure to take this into consideration when building out your Collection plan.

Collections, when set up strategically, can serve as a way to segment based on business unit, team, subsidiary, and so on.

> ℹ️
>
> We suggest that you familiarize yourself with these two documents before establishing Collections:
>
> * [Creating & Seeding Collections](../create-a-collection.md)
> * [Understanding Attack Surface Management Seeds](../understanding-attack-surface-management-seeds.md)

Here are some best practices to help you get the most out of ASM Collections.

## a-sample-build-out

* Organization: **Acme Corporation**
  * Project: **Acme Widgets**
    * Collection: **Acme Widgets - External Surface**
    * Collection: **Acme Widgets - Cloud Surface - AWS Accounts**
    * Collection: **Acme Widgets - Cloud Surface - GCP Accounts**
    * Collection: **Acme Widgets - Cloud Surface - Github Account**
  * Project: **Acme Offices**
    * Collection: **Acme Offices - External Surface**

## general-guidelines

* Only one organization per Collection
* Add Seeds for specific asset types or unique parts of your organization: IPs, top-level domains, netblocks
* 50 Collections or less per Project for maximum performance

> ℹ️ Business Unit and Subsidiary Considerations
>
> It’s key to configure Collections in a way that makes this easy going forward. Think of Collections as a way to configure groupings of assets and findings together.

## building-your-first-collection

The key to setting a Collection up for success is accounting for the time and resources available for managing the attack surface. We recommend slowly and strategically building Collections within the module to ensure that your security team can manage the flow of data.

### seed-and-scope-selection

ASM uses Seeds to define the scope of asset discovery.

The following are the recommended Seed types to use when building your first Collection:

| **Seed Type**            | **Quantity per Collection** |
| ------------------------ | --------------------------- |
| Netblocks (IPv4 or IPv6) | 500 IP Addresses per        |
| Primary Domains          | 1-5                         |
| IP Addresses             | 500                         |

> ℹ️
>
> Avoid using RFC 1918 addresses.

Using one or more of these recommended Seeds will produce a baseline view of external assets and security issues. Then you can have your security team assess the external asset, Entity, and inventory, and prioritize critical and high severity Issues.

### using-integrations

[Inbound integrations](../inbound-integrations.md) reduce manual tasks to upload Seeds to Collections. As you onboard, start with a single integration to make data management easier on your security team. 

### account-permissions

Where applicable, identify the cloud or DNS administrators before configuring the integration. 

Creating an individual Collection per integration to make data management easier on your security team. 

> ℹ️
>
> Account Permissions\
> Where applicable, identify the cloud or DNS administrators before configuring the integration.

<br />

> 💡
>
> ### Creating an individual Collection per integration will enable cleaner data segmentation later on.

The following inbound integrations are available for integration with ASM:

* [Akamai](../inbound-integrations/asm-akamai-integration.md): Retrieve DNS zones
* [AWS](../inbound-integrations/asm-aws-integration.md): Retrieve EC2 instances, S3 buckets, route 53 zones, and RDS
* [Azure](../inbound-integrations/asm-azure-integration.md): Retrieve virtual machine instances, storage accounts (blobs), and public DNS zones
* [Cloudflare](../inbound-integrations/asm-cloudflare-integration.md): Retrieve DNS zones
* [GitHub](../inbound-integrations/asm-github-integration.md): Retrieve Organization and Account information
* [GoDaddy](../inbound-integrations/asm-godaddy-integration.md): Retrieve DNS zones
* [Google Cloud](../inbound-integrations/asm-google-cloud-integration.md): Retrieve APIs via API Gateway, applications, cloud functions, cloud SQL instances, compute, storage, and DNS

> ℹ️
>
> Once integrations have been established in ASM, they must be linked to a relevant Collection.

---

← [Create a Collection](../create-a-collection.md) · [up](../README.md) · [Customize Collections](customize-collections.md) →

*Archived from <https://gtidocs.virustotal.com/docs/collections-tips-and-tricks>.*
