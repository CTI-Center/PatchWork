---
title: "Getting Started with ASM"
source: https://gtidocs.virustotal.com/docs/get-started-asm
slug: get-started-asm
section: guides
group: "ASM"
updatedAt: 2025-09-25T01:57:06.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [ASM](README.md) › Getting Started with ASM

---

# getting-started-with-asm

## introduction

The Attack Surface Management (ASM) tool is a vital cybersecurity solution that empowers organizations to assess their external digital assets from an adversarial perspective. By simulating an attacker's viewpoint, ASM enables you to identify vulnerabilities, misconfigurations, and their potential impact on your organization.

ASM continuously evaluates your internet-accessible digital assets, adapting to the dynamic nature of IT infrastructure. This proactive approach ensures you stay informed about emerging threats and potential attack vectors. This guide will walk you through the initial setup of ASM, providing a foundational understanding of its functionality and how you can quickly gain insights into your attack surface exposure.

## brief-overview:-how-asm-works

You begin using ASM by providing it a starting point, known as a [seed](understanding-attack-surface-management-seeds.md). This could be a domain name relevant to your organization. In our example we will use *mandiant.com*. With this seed, ASM is able to automatically generate an inventory of related entities sharing *mandiant.com*’s infrastructure.

This information is added to a [collection](create-a-collection.md), which is used to create and manage a scan workflow. Once a collection runs, it creates [entity](entities-guide.md) entries for all discovered digital assets to include each port hosting a service. An Entity refers to any external asset associated with an organization, such as a domain name, email address, or URL. Each discovered entity that is found serves as a pivot point for further data gathering.

ASM creates a list of all technologies fingerprinted on discovered Entities. ​Once the assets are collected and discovered, ASM continuously monitors the assets, detecting [issues](issues-guide.md) where they exist for each entity.\
Issues can arise from multiple sources:

* Known CVEs (Common Vulnerabilities and Exposures
* Misconfigurations
* Data or Port/Protocol exposures and leaks
* World readable AWS S3 Buckets, GCP storage buckets, Azure Blobs, etc.
* Custom findings and configurable scans

Issues are [prioritized and scored on a criticality scale](issues-guide/issues-severity-definitions.md), allowing for efficient risk assessment.\
ASM generally utilizes the same open-source tools that penetration testers, red teams, and adversaries use. If you want to know more about how the ASM Tool differs from vulnerability management tools, and how we conduct active versus passive scanning, review this [article](issues-guide/how-issues-work.md).

To ensure optimal functionality, it's wise to allowlist ASM's originating IP addresses within your security features that might sinkhole any scanning activities.

## seeds-and-sources

Seeds are entities that ASM uses to start a data collection. ASM takes each Seed as a starting point and recursively analyzes all other entities that are related or touched upon by that Seed, adding each entity that is encountered to the Collection.\
The efficacy of ASM relies on thoughtful seed selection. It's best to start with:

* Netblocks
* Domains
* DNS records
* Nameservers

Once these seeds are entered, we recommend integrating ASM with any of your cloud resources like AWS, Azure, GCP, GitHub repos, and others of interest. ​This can be done via an Inbound Integration which is covered below.

Some out of scope entities may include old DNS records identified with recursive DNS lookup, or even IPs related to 3rd parties that you may not want to look into.

![Out of scope option in ASM](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_out_of_scope.png)

We highly recommend checking out our [Collections Tips and Tricks](create-a-collection/collections-tips-and-tricks.md) page once you are starting to build your first collection with your seeds.

## integrations-for-enhanced-capabilities

ASM readily integrates with popular cloud environments and other platforms for streamlined operations. These integrations broaden asset discovery, automate processes, and enable the population of SIEM or ticketing systems with issue data.

* [Inbound Integrations](inbound-integrations.md) are API Integrations that feed ASM with relevant information from certain Cloud products which automates and expands the discovery of Cloud entities
* Alternatively, [Outbound Integrations](outbound-integrations.md) are API Integrations which enable ASM to populate SIEMs or ticketing systems with issue and entity data for further handling.

## cross-team-collaboration

A successful ASM strategy harnesses the expertise of multiple security teams:

* Application Security: Automate application discovery and inventory underlying technologies.
* Vulnerability Management: Amplify the scope of existing tools to give full external attack surface visibility.
* Security Operations: Gain deeper insight into domains and DNS records. Uncover compromised machines and missing email protections.
* Red Teams/Intelligence: Assess the efficacy of security controls using data on typosquats and compromised assets.
* Governance, Risk, Compliance (GRC): Create inventories that reveal shared services, subsidiaries, and unsanctioned assets for more robust risk assessments.

ASM offers [role-based access controls](create-a-collection/assign-roles-within-a-collection.md), making it possible for multiple teams to benefit from using the tool while restricting data access based on need-to-know. ​

## additional-considerations

Attack Surface Management offers a user-friendly interface, powerful insights, and customizable reporting to help reduce risks posed by your external attack surface. To maximize value and adoption, consider the following:

* Update asset inventories as your infrastructure evolves.
* Invest in continuous vulnerability scanning for early detection.
* Utilize threat intelligence integrations for enriched threat context.
* Implement risk-based prioritization to address the most critical issues first.
* Collaborate closely with IT and DevOps teams to expedite remediation.

Should you have any additional questions, don't forget to utilize our [Google Cloud Community ASM page](https://www.googlecloudcommunity.com/gc/Attack-Surface-Management/bd-p/mandiant-attack-surface-mgmt); or reach out to our [support team](https://www.virustotal.com/gui/contact-us).

---

← [Vulnerability report details](../10-vulnerability-intelligence/vulnerability-report.md) · [up](README.md) · [Dashboard](dashboard.md) →

*Archived from <https://gtidocs.virustotal.com/docs/get-started-asm>.*
