---
title: "Monitor Compromised Credentials"
source: https://gtidocs.virustotal.com/docs/monitor-compromised-credentials
slug: monitor-compromised-credentials
section: guides
group: "DTM"
updatedAt: 2025-09-25T00:30:39.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [DTM](../README.md) › [Monitors](../monitors-guide.md) › Monitor Compromised Credentials

---

# monitor-compromised-credentials

Digital Threat Monitoring (DTM) automatically alerts you if any accounts linked to designated domains have appeared in compromised credential data collected from the deep, dark web.

> ℹ️
>
> Compromised Credentials monitoring automatically includes any associated subdomains.

## create-a-compromised-credential-monitor

Use the following workflow to create a Compromised Credentials Monitor.

1. From DTM, select the **Monitors** tab.

2. Select the **Compromised Credentials** Monitor template. ![](https://storage.googleapis.com/gtidocresources/guides/dtm/monitors-guide/images/dtm_compromised_credentials_select_monitor_20240527.png)

   You are presented with a setup wizard to walk you through the monitor setup steps.

   ![create a compromised credentials monitor](https://storage.googleapis.com/gtidocresources/guides/dtm/monitors-guide/images/dtm_compromised_credentials_create_20240802.png)

3. Name the Monitor.
   1. Enter a name for the Monitor.
   2. Optional: Provide a description.
   3. Click **Next**.

4. Add your domains. 

   1. Enter domains to be monitored.

   2. Click **Next**.

   > ℹ️
   >
   > . Domains must be entered one per line.. You only need to add the most top-level domain; all sub-domains alerts are included.. You are required to prove that you own these domains in order to receive alerts containing unmasked login credential details.. Monitoring compromised credentials for free or public email domains is not supported.

5. Optional: Exclude specific subdomains if you want to reduce monitor noise and false positives.
   1. Enter domains to be excluded.
   2. Click **Next**.

6. Define Matching Logic. Select either or both of the following options:

   * **Match email domains in the login field**.
     * These are high-confidence employee credential matches.
     * When available, these matches deliver additional context around the breach including compromised machine’s IP, hostname and other metadata.
     * Only these matches for verified domains include clear text passwords.
     * When there are matches to both of the email domain and web service domain, the matches are shown.
   * **Match the web service domain**.
     * Match your domains to the web service the compromised credential logs into.
     * These matches expand coverage for when there are not email domains in the login field.
     * Clear text passwords are not provided for these credentials because it cannot be confirmed whether credentials with this match are employee credentials.

7. Optional: Configure password policy to know if passwords in compromised credentials alerts meet your organization’s password policy.
   1. Set a minimum and maximum password length.
   2. Configure Complexity Rules, such as at least one non-alphanumeric character or at least one uppercase character.
   3. Click **Next**.

8. Optional: Configure notification delivery.
   1. Select the checkbox to **Enable email alert notifications**.
   2. Select the checkbox to **Deliver email notifications from this monitor immediately**.
   3. Click **Next**.

9. Optional: Configure backfill alerts if you want to create historical alerts for the period you select.
   * Choose an option:
     * **No, do not backfill alerts**
     * **Yes, backfill alerts for the last**
       * Choose a time period from the drop-down. For example, **7 Days**.

10. Click **Create Monitor**.

11. Optional: Verify domain ownership with a TXT record.

> ℹ️
>
> Verifying ownership of a domain lets us enrich associated alerts with additional details such as PII that otherwise would not be displayed. This improved context typically results in more actionable alerts.\
> For more information on verifying domains with a TXT record, including step-by-step instructions, see [Verify your domain with a TXT record](https://support.google.com/a/answer/183895?hl=en).

i. Select **Click to Copy** to copy the verification code for the TXT record.

ii. Paste the verification code in to the DNS records for your domain. Once your domain registrar publishes your verification code, we'll know you're the owner of your domain.

> ℹ️
>
> This process may take up to three hours.

iii. Optional: If you know that your DNS records have been updated, click **Refresh** to initiate an ad hoc query to verify your domain.

iv. Optional: Click **Download Codes** to download all TXT record verification codes in a CSV file.

12. Click **Edit** to modify your domain list or **Done** to save the Monitor for the listed domains.

<br />

![Red boxes highlight the Click to Copy and Refresh icons, the Download Codes button, the Edit button, and the Done button.](https://storage.googleapis.com/gtidocresources/guides/dtm/monitors-guide/images/dtm_compromised_credentials_setup_20240802.png)

## view-or-edit-compromised-credentials-monitors

Once created, the new monitor will appear in Your Monitors. Use the following workflow to edit or delete Monitors from this list.

1.  From DTM, select the **Monitors** tab.
2. Select an existing monitor from the list of **Your Monitors**. A summary view of the monitor appears.

   * To delete, click **Delete Alerts or Monitor** and make a selection to delete the Alerts for this Monitor or the Monitor itself.

   > ❗️
   >
   > This process cannot be undone. Deleted Alerts and Monitors can be recreated but they can't be restored with historical data intact.

![Compromised credentials monitor details](https://storage.googleapis.com/gtidocresources/guides/dtm/monitors-guide/images/dtm_compromised_credentials_details_20240802.png)

* Alternatively, to edit any field associated with the Monitor, click\
  ![](https://storage.googleapis.com/gtidocresources/guides/dtm/monitors-guide/images/dtm_compromised_credentials_edit_icon_20240528.svg) **Edit** or the toggle associated with the field to make the necessary adjustments.

## explore-compromised-credentials-alerts

In DTM, the **Alerts** tab displays all Alerts generated from DTM Monitors.

> ℹ️
>
> See [Working with Alerts](../alerts-guide.md) for more information about DTM Alerts in general.

All Alerts associated with a single **Compromised Credentials** Monitor are automatically aggregated into a bucket Alert with a **Multiple Alerts** label. The label includes the number of related Alerts. 

Filtering the Alerts list affects how aggregated Alerts are displayed:

* If any child ticket in an aggregated bucket matches the filtering criteria, the bucket is displayed in the Alerts list.
* When using a **Date Range** filter in the **Alert List** view, the date range determines which child Alerts are displayed when you select the bucket.\
  ![Red boxes highlight the Alerts tab, the Date Range filter, the Multiple Alerts label, and the Compromised Credentials filter.](https://storage.googleapis.com/gtidocresources/guides/dtm/monitors-guide/images/dtm_compromised_credentials_alerts_20240802.png)

Click an aggregated bucket Alert to view a table containing all the associated Alerts. New Alerts are tagged with a yellow dot that becomes gray once the Alert has been opened. 

* Alert status can also be changed individually or in bulk. Select one or more Alerts and choose **New**, **Read**, or **Closed** from the **Mark Selected As** drop-down.\
  ![](https://storage.googleapis.com/gtidocresources/guides/dtm/monitors-guide/images/dtm_compromised_credentials_mark_selected_20240802.png)
* The Alerts table includes the following:

  * **Alerted**: Date and time the Alert was generated.

  * **Published**: Date and time at which the credentials were exposed.

  * **Status**: New, Read, or Closed.

  * **Service URL**: The specific source URL used for sign in, such as `myownpersonaldomain.com`.

  * **Account Login**: The username that was found in the compromised credentials data.

  * **Password**: The password that was found in the compromised credentials data.

  > ℹ️
  >
  > * Password hashes and clear text passwords are displayed if available for domains that have been verified.\* Passwords are only displayed if the Account Login contains the verified domain, or if the Service URL domain has been verified and the Account Login domain is empty.

  * **Pwd Policy Met?**: A password policy can be established when the monitor is created.

  * **Threat Name**: The associated threat, such as malware or threat actor, that was found in the compromised credentials data.

    > ℹ️
    >
    > Click the hyperlink for the threat to pivot directly to its profile in the Google Threat Intelligence platform.

  * **Source File**: If the domain has been verified, you can use this link to navigate to the Breach Data view. This view contains information about the threat, the compromised host, and credentials related to your domain.\
    ![Red boxes highlight each of the elements in the bulleted list.](https://storage.googleapis.com/gtidocresources/guides/dtm/monitors-guide/images/dtm_compromised_credentials_open_link_20240802.png)

  * ![](https://storage.googleapis.com/gtidocresources/guides/dtm/monitors-guide/images/dtm_compromised_credentials_link_icon_20240528.svg) **Link icon**: Copy the individual Alert URL to your clipboard.

  * ![](https://storage.googleapis.com/gtidocresources/guides/dtm/monitors-guide/images/dtm_compromised_credentials_open_in_icon_20240528.svg) **Open icon**: Open the individual Alert URL in DTM.

### download-credentials-and-view-history

DTM admins only: Click **Download Credentials** to export a CSV file that includes detailed information about each Alert such as:

* Date and time **Alerted**, **Collected**, **Published**
* **Service URL** 
* **Account Login**
* **Password**

  > ℹ️
  >
  > The Password field is only shown for verified domains.
* **Threat Name**
* **Alert URL**
* **Alert Status**

Click **View History** for an audit trail of the following activities with timestamps and the name of the user that performed the activity:

* Opened, reopened, or closed an Alert
* Created or deleted a Monitor
* Downloaded the CSV file of Alert credentials data

### assign-alert-status

Alert status can be changed individually or in bulk. Select one or more Alerts and click **Mark Selected As**. Select a status to apply to the selected Alerts.

![A red box highlights the Download Credentials and View History buttons.](https://storage.googleapis.com/gtidocresources/guides/dtm/monitors-guide/images/dtm_compromised_credentials_export_20240802.png)

### add-tags

Click **+ New Tag** to select tags from the **Popular Tags** list, or enter your own tag and press enter to save.

> ℹ️
>
> Tags apply to all Alerts in the table. Alerts cannot be tagged individually.

---

← [Monitor Matching Methodology](monitor-matching-methodology.md) · [up](../README.md) · [Research Tools](../research-tools.md) →

*Archived from <https://gtidocs.virustotal.com/docs/monitor-compromised-credentials>.*
