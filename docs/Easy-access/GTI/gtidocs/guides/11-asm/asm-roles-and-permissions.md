---
title: "ASM Roles and Permissions"
source: https://gtidocs.virustotal.com/docs/asm-roles-and-permissions
slug: asm-roles-and-permissions
section: guides
group: "ASM"
updatedAt: 2025-09-25T01:59:24.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [ASM](README.md) › ASM Roles and Permissions

---

# asm-roles-and-permissions

There are two levels of roles in Attack Surface Management (ASM): Project Roles and Collection Roles. Each role is associated with different permissions and is assigned in a different manner. 

## project-roles

Two project-level roles are available in ASM: Owner and Member. 

To confirm whether you are an Owner or a Member of a Project, select the Project from the ASM **Projects and Settings** menu. Your role is displayed with the Project name in the menu.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_roles_permission_project_role_20240829.png)

For information on how to assign these roles, see [Manage Project Membership](guides/manage-project-membership.md).

### project-owner

The creator of a Project is the initial Project Owner. Project Owners are able to:

* assign additional Project Owners to the Project
* invite Members to the Project or Collections contained within
* archive the Project
* add integrations to the Project
* rename the Project or Collections contained within

### project-member

When a Member is invited to a Project, they do not see any Collections in the Project until they have been explicitly assigned a role within a Collection. For more information see the following section about Collection Roles.

## collection-roles

Project Members must be assigned a collection-level role to be able to view a Collection in MA-ASM. Three roles are available:

* **Viewer**: Able to view Collection output, but not able to make any changes, even to Seeds
* **Analyst**: Able to change the settings of a given Entity or Issue, but not collection-level settings
* **Admin**: Able to change the Collection settings, add Seeds, and configure Issues, but cannot invite others

> ℹ️
>
> Project Owners are Admins on all Collections within the Project.

![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_roles_permission_roles_20240829.png)

For information on how to assign these roles, see [Assign Roles Within a Collection](create-a-collection/assign-roles-within-a-collection.md).

---

← [Notifications](notifications.md) · [up](README.md) · [Assessment Capabilities](assessment-capabilities.md) →

*Archived from <https://gtidocs.virustotal.com/docs/asm-roles-and-permissions>.*
