---
title: "Sessions"
source: https://gtidocs.virustotal.com/reference/sessions
slug: sessions
section: reference
group: "agentic"
updatedAt: 2026-08-05T11:47:31.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [agentic](README.md) › Sessions

---

# sessions

Overview of Google Threat Intelligence agentic chat sessions and authentication.

> ❗️
>
> ### Public preview
>
> **Agentic sessions is currently in Public Preview.** Quotas are temporarily waived during the preview phase. They will be enforced upon official launch, and we’ll notify you in advance before any changes take effect.
>
> We’d love your feedback! Share your thoughts, bug reports, or feature requests via this [form](https://forms.gle/Wx3Cr5ZZFP4cmJTs7).

Agentic sessions represent a conversation with the Google Threat Intelligence agent. Each session keeps the ordered list of events exchanged with the agent and any artifacts attached to it.

These endpoints run synchronously: when you post a message the response is returned only after the agent finishes processing it. Responses follow the JSON:API convention, with the session exposed under the `agentic_session` type.

All requests must be authenticated with your API key sent in the `x-apikey` header.

---

← [Cancel a Flow Execution](flow-executions/cancel-flow-execution.md) · [up](README.md) · [List sessions](sessions/list-sessions.md) →

*Archived from <https://gtidocs.virustotal.com/reference/sessions>.*
