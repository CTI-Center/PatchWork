---
title: "Configuring DTM Email Notifications"
source: https://gtidocs.virustotal.com/docs/configuring-dtm-email-notifications
slug: configuring-dtm-email-notifications
section: guides
group: "DTM"
updatedAt: 2025-09-25T02:48:29.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [DTM](README.md) › Configuring DTM Email Notifications

---

# configuring-dtm-email-notifications

Each organization can configure Email Alert Notifications for the Digital Threat Monitoring (DTM). These notifications can be sent out to multiple email addresses, with each member able to add & verify their email address. 

## configure-email-notifications

1. Click the **Alert List** tab.
2. Click **Email Alert Notification Settings** button. Note that this button is only visible to DTM admins.
3. Review & update the **Frequency**, **Delivery Time**, and **Timezone**.

   > 💡
>
> ### If this is already configured, we recommend you discuss any changes with others who are already receiving the email.

   > ℹ️
   >
   > All designated email addresses will receive notifications for all configured monitors. DTM does not currently support customizable notification options for specific monitors.
4. Enter your email address and press **Enter**.
5. Click **Save**.
6. Locate the verification email and click **Verify**. Once you've verified your email, you'll start receiving notifications for any Monitors that have Notifications enabled.\
   ![Sample verification email](https://storage.googleapis.com/gtidocresources/guides/dtm/images/dtm_verify_email_20240429.png)

## email-notifications-for-individual-monitors

1. Click the **Monitor List** tab.
2. Click **Edit** on the Monitor you want to receive email Notifications settings.
3. Configure the Email Alert Notifications:\
   ![Edit a Monitor modal shows configurable fields for Name and Description, a toggle to turn Email Alert Notifications on or off, and a checkbox to deliver email notifications immediately](https://storage.googleapis.com/gtidocresources/guides/dtm/images/dtm_email_notifications_20240429.png)
   1. Select **On** for **Email Alert Notifications**.
   2. If you want to receive email notifications immediately and not based on the overarching Email notification settings, select **enable Deliver email notifications immediately for this monitor.** 
4. Click **Save Changes**.

---

← [Research Tools](research-tools.md) · [up](README.md) · [Lucene Queries in DTM](lucene-queries-in-dtm.md) →

*Archived from <https://gtidocs.virustotal.com/docs/configuring-dtm-email-notifications>.*
