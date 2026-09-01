---
title: "Understanding Attack Surface Management Seeds"
source: https://gtidocs.virustotal.com/docs/understanding-attack-surface-management-seeds
slug: understanding-attack-surface-management-seeds
section: guides
group: "ASM"
updatedAt: 2025-09-25T00:56:33.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [ASM](README.md) › Understanding Attack Surface Management Seeds

---

# understanding-attack-surface-management-seeds

## what-are-seeds?

Seeds are entities that Attack Surface Management (ASM) uses to start a data collection run. ASM takes each Seed as a starting point and recursively analyzes all other Entities that are related or touched upon by that Seed, adding each Entity that is encountered to the Collection.

When adding a Seed to a Collection, both the value and the type must be provided. ASM uses this pairing to determine how to analyze this Seed and enumerate Entities from it. For example, if we add the domain `mandiant.com` as a Seed, then we select `Domain` as the Seed type. If we want to refer to a website, we must provide the full URL of `http://www.mandiant.com` (including the prefix `http://`) and select the Seed type `Uri`.

## seed-examples

The following table lists the name, the description, and a sample value for each Seed type. All sample entries are in the format that you'd enter them, unless you see **or**, which means there are two samples provided. 

| Seed Type            | Description                                                                       | Sample Values                                          |
| -------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **ApiEndpoint**      | HTTP-based API endpoint                                                           | `https://app.acme.com/api`                             |
| **AutonomousSystem** | An autonomous system number (AsNumber)                                            | `AS1234`                                               |
| **AwsS3Bucket**      | AWS S3 bucket                                                                     | `publicfiles-acme`                                     |
| **DnsRecord**        | DNS record                                                                        | `est.acme.com`                                         |
| **Domain**           | Top-Level Domain (TLD)                                                            | `acme.com`                                             |
| **EmailAddress**     | Email address                                                                     | `no-reply@acme.com`                                    |
| **GithubAccount**    | Account in GitHub                                                                 | `https://github.com/acme`                              |
| **GithubRepository** | Repository in GitHub                                                              | `https://github.com/acme/acme-core`                    |
| **IpAddress**        | IP address, either IPv4 or IPv6                                                   | `1.1.1.1` or `3FFE:FFFF:7654:FEDA:1245:BA98:3210:4562` |
| **Nameserver**       | Domain Name Server (DNS), either fully-qualified domain name (FQDN) or IP address | `ns1.acme.com` or `2.2.2.2`                            |
| **NetBlock**         | A block of IP addresses (IPv4) in CIDR notation                                   | `1.1.1.1/24`                                           |
| **UniqueKeyword**    | Globally unique keyword that can be reliably searched for                         | `Acme`                                                 |
| **UniqueToken**      | API key or analytics ID                                                           | `UA-34505845`                                          |
| **Uri**              | Link to a website or a webpage                                                    | `https://acme.com`                                     |

## how-to-determine-the-best-seeds-when-starting-a-new-collection

Domains and netblocks are the best types of seeds to start with. This is because many child Entities can be discovered through enumeration. If resources and time allow, adding all known entities that belong to your organization is even better.

The more known entities that are provided to start, the better the scoping works. ASM assigns a confidence rating to each Entity that is found, and automatically determines whether it is "in scope" or "out of scope". By having more defined data points, in this case, Seeds that are in scope, the accuracy of the system goes up.

For more information about Seeds, see [Collections Tips and Tricks](create-a-collection/collections-tips-and-tricks.md).

---

← [Insights](insights.md) · [up](README.md) · [Create a Collection](create-a-collection.md) →

*Archived from <https://gtidocs.virustotal.com/docs/understanding-attack-surface-management-seeds>.*
