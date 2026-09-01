---
title: "How to delete an ASM project"
source: https://gtidocs.virustotal.com/docs/delete-asm-project
slug: delete-asm-project
section: guides
group: "ASM"
updatedAt: 2025-09-25T02:47:33.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [ASM](README.md) › How to delete an ASM project

---

# how-to-delete-an-asm-project

You can delete an existing Attack Surface Management (ASM) project using the [Attack Surface Management (ASM) API](https://gtidocs.readme.io/reference/delete_projects-uuid) if you are the owner of this project. If you need assistance with this process, contact [Support](https://www.virustotal.com/gui/contact-us/technical-support).

> ℹ️ Collection configuration
>
> * Only project owners have permission to delete an ASM project.
> * The base URL is expected to be **<https://www.virustotal.com/api/v3/asm/>**, unless otherwise specified.

1. Run the following curl command to get the project `uuid`.

```
    curl --request GET \
     --url https://www.virustotal.com/api/v3/asm/projects \
     --header 'accept: application/json' \
     --header 'x-apikey: {x-apikey}'
```

2. Using this `uuid`, run the following command to delete the project.

```
    curl --request DELETE \
     --url https://www.virustotal.com/api/v3/asm/projects/{uuid} \
     --header 'accept: application/json' \
     --header 'x-apikey: {x-apikey}'
```

---

← [Mandiant Advantage for Splunk](outbound-integrations/mandiant-advantage-for-splunk.md) · [up](README.md) · [ASM API Limits and Quotas](asm-limits-quotas.md) →

*Archived from <https://gtidocs.virustotal.com/docs/delete-asm-project>.*
