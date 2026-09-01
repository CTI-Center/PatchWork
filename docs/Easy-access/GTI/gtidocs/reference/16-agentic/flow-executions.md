---
title: "Flow Executions"
source: https://gtidocs.virustotal.com/reference/flow-executions
slug: flow-executions
section: reference
group: "agentic"
updatedAt: 2026-08-05T11:48:00.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [agentic](README.md) › Flow Executions

---

# flow-executions

API endpoints for monitoring and managing Agentic Flow Executions.

> ❗️
>
> ### Public preview
>
> **This feature is currently in Public Preview.** Active Flows are limited based on your package tier.
>
> We’d love your feedback! Share your thoughts, bug reports, or feature requests via this [form](https://forms.gle/Wx3Cr5ZZFP4cmJTs7).

> 🚧 Special privileges required
>
> Flow Executions are only available to users with the Google Threat Intelligence (Google TI) Enterprise, Enterprise Plus, or Integration Advanced licenses, and require AI features to be enabled in your group settings.

A **Flow Execution** is a single run of a [Flow](../17-api-objects/flow-object.md), created automatically on the Flow's trigger or manually via *Run a Flow now*. Each execution records its overall `status`, `duration_seconds`, the per-node `steps` with their typed output, and a `flow_snapshot` of the Flow definition as it was when the run started.

Executions are read-only through the API except for cancellation.

---

← [Unsubscribe from a Flow's email notifications](flows/unsubscribe-flow.md) · [up](README.md) · [List Flow Executions](flow-executions/list-flow-executions.md) →

*Archived from <https://gtidocs.virustotal.com/reference/flow-executions>.*
