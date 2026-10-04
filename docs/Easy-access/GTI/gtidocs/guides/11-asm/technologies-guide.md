---
title: "Technologies"
source: https://gtidocs.virustotal.com/docs/technologies-guide
slug: technologies-guide
section: guides
group: "ASM"
updatedAt: 2025-09-25T01:58:07.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [ASM](README.md) › Technologies

---

# technologies

With our robust fingerprinting engine, we focus on popular technologies commonly found across enterprise systems. When a new vulnerability comes out, we add it to our fingerprinting engine if the technology is not already in there.

## technologies-list

The **Technologies** page of Attack Surface Management (ASM) shows you a list of the technologies used in your organization. This list gives you insight into and oversight of the tools used in your organization so that you can easily identify whether you are running a particular technology that may have a risky vulnerability. Click on a listed technology to see the list of Entities where this technology was located.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/technologies_home_20240418.png)

For each technology encountered, the following items are identified:

* **Technology**: The name of the vendor, technology, and version if available. The vendor is the company that owns the technology. For example, Microsoft (a vendor) owns Microsoft Exchange (a technology product). In some instances, the vendor and technology have the same name, such as Cloudflare. Every technology has a unique logo. Logos are displayed on the cards, table, and detail view.

  If there isn't a vendor-specific logo associated with a technology, the default logo is displayed.
* **CPE Type**: The [Common Platform Enumeration (CPE)](https://nvd.nist.gov/products/cpe) name identifying whether this technology is a service or an application. A **service** is software that is managed *for* its users, an **application** is software that is managed *by* its users. For example, Cloudflare is a service, whereas WordPress is an application. AWS is a service that can run applications.
* **Collection**: The name of the Collection where this technology was identified.
* **Labels**: A short identifier for an attribute of the technology.
* **First Seen** date
* **Last Seen** date

### active-and-inactive-filter

On the **Technologies** page, you see filter options based on the following definitions:

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/technologies_filter_20240418.png)

* **Active Technologies**: Technologies that have been seen in the most recent scan.
* **Inactive Technologies**: Technologies that were seen in a previous scan and were not seen in the most recent scan.

## technology-library

A list of the over 3,000 technologies that ASM currently fingerprints is available in the [Technology Definitions](https://asm.advantage.mandiant.com/library/technologies) section of the ASM Library.

### access-technology-definitions-in-the-asm-library

1. From the ASM **Projects and Settings** menu, select **Library**.
2. Select **Technology Definitions**. 
3. Optional: To filter the list, select a **Label** or **Vendor**. Alternatively, you can **Search for technologies**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/technologies_library_20240418.png)

If a specific version is not listed for a technology, all versions are included in detection. 

The number of **Fingerprints** represents how many methods are available to detect a specific technology. For instance, there are four distinct detection methods for identifying the **3dcart** product. As a technology progresses and implementations vary, more identifiers are developed to encompass both older and newer versions of the software.

---

← [Scan History](entities-guide/scan-history.md) · [up](README.md) · [Insights](insights.md) →

*Archived from <https://gtidocs.virustotal.com/docs/technologies-guide>.*
