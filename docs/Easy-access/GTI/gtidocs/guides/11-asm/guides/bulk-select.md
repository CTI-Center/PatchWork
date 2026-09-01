---
title: "Bulk Select"
source: https://gtidocs.virustotal.com/docs/bulk-select
slug: bulk-select
section: guides
group: "ASM"
updatedAt: 2025-09-25T01:59:31.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [ASM](../README.md) › [Guides](../guides.md) › Bulk Select

---

# bulk-select

Bulk Select in Attack Surface Management (ASM) lets you select multiple [Issues](../issues-guide.md) or [Entities](../entities-guide.md) and perform specific actions on your selection. The following bulk actions are available:

### issues

* Add Tags
* Set Status

### entities

* Add Tags
* Set Out Of Scope

> ℹ️
>
> You are unable to perform any of the actions listed here on Issues or Entities associated with Read Only Collections in ASM.

## select-multiple-issues-or-entities

> ℹ️
>
> Bulk Select is only available in table view, not card view.

1. From the [Issues dashboard](https://asm.advantage.mandiant.com/issues) or [Entities dashboard](https://asm.advantage.mandiant.com/entities) in ASM, select **Switch to Table View**. 
2. Hold the pointer over the Collection tile of an Issue or Entity you want to modify. This reveals a checkbox. Select the checkbox.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_bulk_select_select_20241008.png)

3. Select the checkbox associated with each additional Issue or Entity you want to modify.

> ℹ️
>
> Alternatively, select the checkbox in the header of the table to select the first 50 Issues or Entities listed.\
> ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_bulk_select_items_selected_20241008.png)

4. Click **Add Tag**, **Set Status**, or **Set Out of Scope** to perform that action on your selected set of Issues or Entities. Specific directions for completing each action are outlined in the following sections.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_bulk_select_tag_status_20241008.png)

A list of six Active Issues in Table View. Three of the Issues are selected for modification.

## add-tags

1. Once you click **Add Tag**, click **+New Tag** . 
2. Enter a word or phrase and click the check mark to save the tag. 
3. Optional: Use **+** to add additional tags. 
4. Click **Apply** to bulk tag all of the Issues or Entities you previously selected.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_bulk_select_add_tags_20241008.png)

> ℹ️
>
> If you want to modify tags after a bulk tagging, edits must be performed for each individual Issue or Entity.

## set-status

> ℹ️
>
> This bulk action only applies to Issues, not Entities.

Once you click **Set Status**, select a status and click **Submit** to apply this status to all of the Issues you previously selected. For more information about statuses, see [Issue Status](../issues-guide.md#issue-status).

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_bulk_select_set_status_20241008.png)

## set-out-of-scope

> ℹ️
>
> This bulk action only applies to Entities, not Issues.

When you select this action, subdomains and URLs related to the selected Entities are excluded from their respective Collections. For more information, see [How to Set Entities Out of Scope](../entities-guide/how-to-set-entities-out-of-scope.md).

Once you click **Set Out of Scope**, click **Submit**.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_bulk_select_out_of_scope_20241008.png)

> ℹ️
>
> * Independent domains are not affected.\* Changes take effect upon the next collection scan.

---

← [Search Summary](search-summary.md) · [up](../README.md) · [Analyzing SSL/TLS Issues](analyzing-ssltls-issues.md) →

*Archived from <https://gtidocs.virustotal.com/docs/bulk-select>.*
