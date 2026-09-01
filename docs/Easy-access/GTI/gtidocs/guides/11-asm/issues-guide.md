---
title: "Issues"
source: https://gtidocs.virustotal.com/docs/issues-guide
slug: issues-guide
section: guides
group: "ASM"
updatedAt: 2025-09-25T01:57:08.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [ASM](README.md) › Issues

---

# issues

Issues are respective to the entity type, and different entity types warrant their own issue checks. The most common issue checks are for URI entities. Issue checks are selected based on the technology and version (as captured) that is fingerprinted on the Entity. So for example, a WordPress check will only run against an Entity that is fingerprinted with WordPress. This helps Attack Surface Management (ASM) to be more efficient and economical with resources, speeding up the scan and data gathering process. 

[ASM Issues en](https://www.youtube.com/watch?v=nCracshEk_Q)

## recent-issues-list

The **Issues** page of ASM shows you a list of the most recent Issues that were identified in the selected Collections. Each Issue listing contains:

* A short description of what was found
* The Collection containing the Issue
* Its [Severity](issues-guide/issues-severity-definitions.md), [Status](#issue-status), and [Confidence Level](#confidence-level)
* Any tags associated with it
* The first and last times it was seen

![Reviewing Issues](https://storage.googleapis.com/gtidocresources/guides/asm/images/issues_home_20240411.png)

### confidence-level

ASM uses a [Confidence level](issues-guide/issues-severity-definitions.md) of **Confirmed** or **Potential** to describe the degree of certainty that the Entity is actually vulnerable with the detected Issue. 

* **Confirmed**: ASM interacted directly with the target Entity to confirm that it was vulnerable with the associated Issue.
* **Potential**: Some form of inference was used to identify the Entity as being potentially vulnerable with the associated Issue.

Confidence level is driven by the type of check (active or passive) used to query the Entity in the Issues list:

* **Active Checks**: Most checks are active, which means ASM sends a benign check directly to the target Entity to verify that it is indeed vulnerable. These payloads are strategically crafted to avoid any business disruptions to customer systems. Benign checks ensure that the integrity and availability of your systems are not compromised.
* **Passive Checks**: In scenarios where a public exploit cannot be verified without more aggressive methods, we passively determine that the system is potentially vulnerable based on the technology version.

For more information on checks, see [How Issues Work](issues-guide/how-issues-work.md).

### active-and-inactive-filter

On the **Issues** page, you will see filter options including **Active Issues** and **Inactive Issues**:

![Active Inactive Issues](https://storage.googleapis.com/gtidocresources/guides/asm/images/issues_active_inactive_20240417.png)

* **Active Issues**: Issues that have been seen in the most recent scan.
* **Inactive Issues**:  Issues that were seen in a previous scan and were not seen in the most recent scan.

## reviewing-issue-details

Clicking on an Issue allows you to send Issue details to an email address, review or add Notes, and drill down into additional components of the Issue:

* **Description**: Provides a short **Description** of the Issue and recommended **Remediation** steps, if available.
* **References**: Includes links to additional resources with greater details related to the detected vulnerability.
* **Proof**: Details the specific attributes of the query that triggered the successful detection of the vulnerability.
* **Raw (JSON)**: The raw JSON structure of the query itself.

![Issues Details](https://storage.googleapis.com/gtidocresources/guides/asm/images/issues_details_20240411.png)

## issue-status

A variety of Status options are provided for tracking Issues. The following statuses are available:

| Status |
| --- |
| <ul><li>Open</li><ul><li>Triaged</li><li>In Progress</li></ul></ul> |
| <ul><li>Closed</li><ul><li>Mitigated</li><li>Resolved</li><li>Duplicate</li><li>Out of Scope</li><li>Not a Security Issue (Benign)</li><li>Risk Accepted</li><li>False Positive</li><li>Unable to Reproduce</li><li>Tracked Externally</li></ul></ul> |

* Only Issues with an Open status are included in Dashboard widgets, unless otherwise specified.
* By default, when accessing the [Issues page](https://asm.advantage.mandiant.com/issues), the search parameters are set to only show Issues with an Open status.

![Issues Search Bar](https://storage.googleapis.com/gtidocresources/guides/asm/images/issues_search_bar_20240411.png)

## issues-library

A library of **Issue Definitions** is available from your **[Projects and Settings > Library > Issue Definitions page](https://asm.advantage.mandiant.com/explorer/issues)** in ASM. This comprehensive list shows the issue types we currently index, along with their **Severity** and **Confidence** ratings.

![Library Issues](https://storage.googleapis.com/gtidocresources/guides/asm/images/issues_library_20240417.png)

---

← [Dashboard](dashboard.md) · [up](README.md) · [Create Issues from Inferred CVEs](issues-guide/issues-creation.md) →

*Archived from <https://gtidocs.virustotal.com/docs/issues-guide>.*
