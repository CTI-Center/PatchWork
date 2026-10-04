---
title: "Entities"
source: https://gtidocs.virustotal.com/docs/entities-guide
slug: entities-guide
section: guides
group: "ASM"
updatedAt: 2025-09-25T00:26:49.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [ASM](README.md) › Entities

---

# entities

An Entity is an external asset belonging to an organization such as a domain name, email address, or URL. Every Entity that is found serves as a pivot point for additional data gathering.

For a list of available Entities in ASM, see [Entity types](#entity-types).

## recent-entities-list

The [**Entities** page](https://asm.advantage.mandiant.com/entities) of ASM shows you a list of the most recent Entities that were inspected in the selected Collections. Each Entity listing contains:

* Its status, type, and country
* The name of the Entity
* The Collection containing the Entity
* The number and [severity](issues-guide/issues-severity-definitions.md) of associated Issues
* Any tags associated with it
* The first and last times it was seen
* Associated [technologies](technologies-guide.md)

  If there isn't a vendor-specific logo associated with a technology, a generic icon is displayed.

![Attack Surface Management Entities page](https://storage.googleapis.com/gtidocresources/guides/asm/images/entities_home_20240418.png)

### active-and-inactive-filter

On the **Entities** page, you will see filter options based on the following definitions:

![A screenshot of the Active Entities filter](https://storage.googleapis.com/gtidocresources/guides/asm/images/entities_active_inactive_filter_20240418.png)

* **Active Entities**:  Entities that have been seen in the most recent scan.
* **Inactive Entities**: Entities that were seen in a previous scan and were not seen in the most recent scan.

## entity-overview

From the [**Entities** page](https://asm.advantage.mandiant.com/entities), open an Entity to explore it in depth. If applicable to the Entity type, you can [set the Entity Out Of Scope](entities-guide/how-to-set-entities-out-of-scope.md). You can review or add notes. Associated Issues are listed. Additional context surrounding the Entity may include:

* **Details**: Information about the Entity.
* [**Scan History**](entities-guide/scan-history.md): Changes that have occurred to the Entity over time.
* **Raw (JSON)**: The raw JSON structure of the query itself.
* [**Discovery Context**](discovery-context-visualizer.md): A visual representation of the discovery path and context identified during the discovery and attribution process of the Entity.
* **Checks**: Checks that have been run on the Entity. Links to the [Library definitions](https://asm.advantage.mandiant.com/library/tasks) are provided.
* [**Technologies**](technologies-guide.md): Technologies associated with the Entity. Links to the [Library definitions](https://asm.advantage.mandiant.com/library/technologies) are provided.
* [Inferred CVE](inferred-vulnerabilities.md): Inferred vulnerabilities (CVEs) that were found in the Entity.
* [Potential Typosquats](tld-list.md): Domains that have been identified as potential typosquats but may be legitimate websites.

![Entity Overview page for a specific Entity. Details tab is showing.](https://storage.googleapis.com/gtidocresources/guides/asm/images/entities_details_20240418.png)

## entity-types

The following table provides a list of Entities available in ASM, categorized by type:

| Entity Type | Entity Name | Entity Description |
| --- | --- | --- |
| Applications | API Endpoint (<code>ApiEndpoint</code>) | A HTTP based API endpoint |
| Application Endpoint (<code>AppEndpoint</code>) | A HTTP / HTTPS application endpoint |  |
| Certificate (<code>SslCertificate</code>) | A Digital Certificate |  |
| GcpApiGateway | Google Cloud Platform API Gateway |  |
| GcpAppEngineApplication | Google Cloud App Engine Application |  |
| GcpCloudFunction | Google Cloud Platform Cloud Function that is public facing and triggered via HTTP |  |
| Network Service (<code>NetworkService</code>) | A TCP or UDP Network Service |  |
| URL (<code>Uri</code>) | A HTTP / HTTPS application endpoint |  |
| Code | Github Account (<code>GithubAccount</code>) | A FQDN of a Github Account |
| Github Repository (<code>GithubRepository</code>) | A FQDN of a Github Repository |  |
| Domains &amp; Networking | Autonomous System (<code>AutonomousSystem</code>) | Unique Autonomous System ID, advertised globally to publish network routes |
| DNS Record (<code>DnsRecord</code>) | DNS Subdomain, any type of DNS record that is not an authoritative domain |  |
| Domain | An Authoritative Domain |  |
| Nameserver | An FQDN or an IP Address that points to a Nameserver |  |
| Network (<code>NetBlock</code>) | A Block of IPs, in CIDR format |  |
| Hosts &amp; Compute | AWS EC2 (<code>AwsEC2Instance</code>) | An AWS EC2 Compute Instance |
| Azure Virtual Machine (<code>AzureVirtualMachine</code>) | An Azure Virtual Machine |  |
| GcpComputeEngineInstance | Google Cloud Compute Engine Instance |  |
| IP Address (<code>IpAddress</code>) | An IPv4 or IPv6 Address |  |
| Storage | AWS RDS (<code>AwsRdsDbInstance</code>) | An AWS RDS Database Instance |
| AWS S3 (<code>AwsS3Bucket</code>) | An S3 Bucket |  |
| AzureStorageAccount | An Azure Storage Account |  |
| GcpCloudSQLInstance | Google Cloud Platform Cloud SQL Instance |  |
| GcpStorageBucket | Google Cloud Platform Storage Bucket |  |
| System | <p>Unique Keyword (<code>UniqueKeyword</code>)</p> | A globally unique keyword that can be reliably searched |
| Users &amp; Access | API Token (<code>UniqueToken</code>) | An api key or analytics id |
| Email Address (<code>EmailAddress</code>) | An Email Address |  |

---

← [How Issues Work](issues-guide/how-issues-work.md) · [up](README.md) · [How to Set Entities Out of Scope](entities-guide/how-to-set-entities-out-of-scope.md) →

*Archived from <https://gtidocs.virustotal.com/docs/entities-guide>.*
