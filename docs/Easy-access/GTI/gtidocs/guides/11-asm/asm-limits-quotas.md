---
title: "ASM API Limits and Quotas"
source: https://gtidocs.virustotal.com/docs/asm-limits-quotas
slug: asm-limits-quotas
section: guides
group: "ASM"
updatedAt: 2026-08-18T15:13:05.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [ASM](README.md) › ASM API Limits and Quotas

---

# asm-api-limits-and-quotas

The Attack Surface Management (ASM) API has a number of limits in place to help ensure a secure and consistent experience for all users. 

> ℹ️
>
> If you need increases to any configurable limits, you can work with your Customer Success Manager.

## api-quotas

API quotas provide limitations that define the maximum number of resources a single organization can have.

| **Description**       | **Quota** | **Scope**        | **Configurable** |
| --------------------- | --------- | ---------------- | ---------------- |
| Number of collections | 100       | Per organization | Yes              |

> 📘 Collection Limit Calculation & Deletion
>
> The maximum collection limit is the sum of all **Active** and **Archived** Collections across all Projects in the Organization.
>
> To stay under the limit and add a new Active Collection, users can delete an Archived Collection through the UI or via [the API](https://gtidocs.readme.io/reference/delete_user-collections-uuid).

---

← [How to delete an ASM project](delete-asm-project.md) · [up](README.md) · [Get started with DTM](../12-dtm/get-started-dtm.md) →

*Archived from <https://gtidocs.virustotal.com/docs/asm-limits-quotas>.*
