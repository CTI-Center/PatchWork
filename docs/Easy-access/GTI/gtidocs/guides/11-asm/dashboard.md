---
title: "Dashboard"
source: https://gtidocs.virustotal.com/docs/dashboard
slug: dashboard
section: guides
group: "ASM"
updatedAt: 2025-09-25T00:55:01.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [ASM](README.md) › Dashboard

---

# dashboard

Attack Surface Management (ASM) helps companies understand their digital footprint and focus on the vulnerabilities that attackers are most likely to target. This is achieved in a couple of ways.

* **Asset discovery**: ASM helps organizations by discovering external assets within the IT infrastructure that the company is connected to. These assets are known as [Entities](entities-guide.md). 
  * Customers begin using ASM by choosing a [Scan Workflow](create-a-collection.md), or use case they want to solve for, and then adding a starting Entity, known as a Seed. For example, a domain name such as `mandiant.com` is considered a Seed. Using this Seed, ASM is able to generate an inventory of related Entities, including known assets and surprise, unmanaged assets. 
  * Customers may add other types of [Seeds](understanding-attack-surface-management-seeds.md) to help populate the discovery process. Seeds are enumerated to help ASM uncover additional assets that the organization might own. Seeds can include domain names, network services, URLs, nameservers, GitHub repositories and accounts, DNS records, certificates, and more.
* **Issue detection**: Once the assets are collected and discovered, ASM continuously monitors the assets, detecting [Issues](issues-guide/how-issues-work.md) where they exist for each Entity. Issues are generated when vulnerabilities, misconfigurations, exposures, or data leaks are identified. Issues can come from known Common Vulnerabilities and Exposures (CVEs) or can be based on custom rules. Issues give customers a high-level understanding of the risks that currently exist in their environment. Issues are rated on a five-point scoring system, with Issues labeled with a “1” as critical, and those labeled with a “5” as informational.

  * Types of Issues range from expired certificates, exposed development systems, and insecure cookies, to more severe problems like misconfigurations of automated build systems such as Jenkins, Microsoft Remote Desktop CVEs, and AWS S3 buckets accessible to unauthenticated users. A full list of Issues can be found on the **[Library > Issues page](https://asm.advantage.mandiant.com/library/issues)** in ASM.
  * Issues are then tackled by the organization's security team, and when resolved, become 'inactive' upon the next scan. Scans run either every day or every week, depending on the agreed upon configuration. 

    In cases where an Issue is resolved between the scans, the Issue still populates as 'active' until the next scan is completed.

ASM is used by pen-testers, red teams, security analysts, and anyone who needs to keep their attack surface secure. At the tactical level, ASM is commonly used to: 

* determine if there are any ports open to the internet
* uncover any vulnerable technologies in use
* monitor supply chain vendors and services
* assess API endpoints
* identify application endpoints that don't allow 2FA
* find unknown or unmanaged assets

[Attack Surface Management Demo](https://www.youtube.com/watch?v=5jPAlqFrI_s)

* Learn how ASM helps you automate external asset discovery and analysis to uncover vulnerabilities, misconfigurations and exposures.
* Provide an overview of Issues, Entities and Technologies. 
* Define the scope of the attack surface to help ASM find critical sources and exposures. 
* Learn how to leverage, search, sort, filter, and ask questions of the attack surface.

---

← [Getting Started with ASM](get-started-asm.md) · [up](README.md) · [Issues](issues-guide.md) →

*Archived from <https://gtidocs.virustotal.com/docs/dashboard>.*
