---
title: "Notifications"
source: https://gtidocs.virustotal.com/docs/notifications
slug: notifications
section: guides
group: "ASM"
updatedAt: 2025-09-25T01:59:23.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [ASM](README.md) › Notifications

---

# notifications

Attack Surface Management (ASM) offers email and chat-based alerting to ensure you can easily monitor changes in your Collections and quickly investigate new assets and exposures.

[ASM - Notifications](https://www.youtube-nocookie.com/embed/VXwQ3LGQ2PE?si=dFWvTBiSgAl9gS7B)

## member-specific-email-alerts

To enable email alerts on a Project for yourself:

1. From the ASM **Projects and Settings** menu, select a Project and click **Account Settings**.
2. Click **Notifications**.
3. Click the **Daily Digest Emails** toggle to the on position.![Notifications tab of Account Settings showing the toggle for Daily Digest Emails.](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_notifications_account_settings_20240521.png)

* **Daily Digest Emails** include updates for all changed Collections within the selected Project.
* If you want to send alerts to a shared inbox or workflow, see the **Collection-specific alerts** section of this document.

## collection-specific-alerts

In some scenarios, it's helpful to send email alerts to multiple emails or to integrate alerts into a team workflow. For these situations, Project Owners can do the following:

1. Enable email notifications to one or more email addresses on a specific Collection:

   1. From the **Collections** menu, select **Settings**.
   2. Click **Settings** for the Collection that you want to enable email notifications for, then open the **Notifications** tab.
   3. Enter all the email addresses that should receive notifications. 

      Enter a space, comma, or the return key after each entry to confirm the email address.
   4. Once all emails have been entered, click **Test** to verify that notification emails can be sent out correctly. ![Notifications tab in Collection Settings where email notifications can be enabled.](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_notifications_collections_20240521.png)
2. Configure [Slack](https://slack.com/help/articles/115005265063-Incoming-webhooks-for-Slack) and [Microsoft Teams](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/what-are-webhooks-and-connectors) webhooks to send alerts directly into a specific channel in those apps.
   1. From the **Collections** menu, select **Settings**.
   2. Click **Settings** for the Collection that you want to enable email notifications for, then open the **Notifications** tab.
   3. Enter a webhook and click **Test** to verify that the webhook is configured correctly. ![](https://storage.googleapis.com/gtidocresources/guides/asm/images/asm_notifications_slack_20240521.png)

---

← [Exporting Search Results](exporting-search-results.md) · [up](README.md) · [ASM Roles and Permissions](asm-roles-and-permissions.md) →

*Archived from <https://gtidocs.virustotal.com/docs/notifications>.*
