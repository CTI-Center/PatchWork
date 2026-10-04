---
title: "Flows"
source: https://gtidocs.virustotal.com/reference/flows
slug: flows
section: reference
group: "agentic"
updatedAt: 2026-08-05T11:46:07.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [agentic](README.md) › Flows

---

# flows

API endpoints for managing and executing Agentic Flows.

> ❗️
>
> ### Public preview
>
> **This feature is currently in Public Preview.** Active Flows are limited based on your package tier.
>
> We’d love your feedback! Share your thoughts, bug reports, or feature requests via this [form](https://forms.gle/Wx3Cr5ZZFP4cmJTs7).

> 🚧
>
> ### Special privileges required
>
> Flows are only available to users with the Google Threat Intelligence (Google TI) Enterprise, Enterprise Plus, or Integration Advanced licenses, and require AI features to be enabled in your group settings.

A **Flow** is a user-defined automation graph made of *nodes* (steps) and *connections* (edges) that Google Threat Intelligence runs on a trigger. A typical Flow, for example, starts with a **Schedule Time** node, runs a **Run Prompt** node against the Agentic platform, and optionally ends with a **Send Email** node.

These endpoints let you create, read, update, delete, and manually run Flows. Flows are a Google Threat Intelligence capability and consume API quota.

---

← [Search Findings](../15-gti-alerts/findings/search-findings.md) · [up](README.md) · [List Flows](flows/list-flows.md) →

*Archived from <https://gtidocs.virustotal.com/reference/flows>.*
