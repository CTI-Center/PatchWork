---
title: "Configure SAML with Okta"
source: https://gtidocs.virustotal.com/docs/saml-okta
slug: saml-okta
section: guides
group: "Group Management"
updatedAt: 2026-03-11T13:30:47.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [Group Management](README.md) › Configure SAML with Okta

---

# configure-saml-with-okta

# set-up

You can configure Google Threat Intelligence to use SAML with Okta. These are the recommended steps for this set-up:

## 1.-okta-admin-panel

In the Okta Admin Panel, go to the Applications tab:

![Okta Administration Panel](https://storage.googleapis.com/gtidocresources/guides/group-management/images/okta_adminpanel_20231026.png)

## 2.-applications-tab

In the Applications tab, click on “Create App Integration”

![Okta Create APP](https://storage.googleapis.com/gtidocresources/guides/group-management/images/okta_createapp_20231026.png)

## 3.-select-“saml-2.0”

![Okta Create APP choose SAML](https://storage.googleapis.com/gtidocresources/guides/group-management/images/okta_createappsaml_20231026.png)

## 4.-provide-an-app-name-and-a-logo

![Okta General Settings](https://storage.googleapis.com/gtidocresources/guides/group-management/images/okta_generalsettings_20231026.png)

## 5.-fill-in-the-fields

Fill the following fields with the following information:\
\_**Single sign on URL:**\
<https://virustotalcloud.firebaseapp.com/__/auth/handler>

***Audience URI:** You can use any string you want as “Audience URI” as long as it's exactly the same in Google Threat Intelligence and in Okta. Alternatively, you can also introduce the Single sign on URL mentioned above\&#xA;***Name ID:** “EmailAddress”

\_ **Application username:** “Email”

* Leave all other fields with their default values:

![Okta SSO URL](https://storage.googleapis.com/gtidocresources/guides/group-management/images/okta_ssourl_20231026.png)

## 6.-configuration-is-finished.-view-setup-instructions

Once your configuration is finished, this is how your configuration should look. Click on the “View Setup Instructions” button:

![Okta Setup Instructions](https://storage.googleapis.com/gtidocresources/guides/group-management/images/okta_setupinstructions_20231026.png)

## 7.-overview

You should see something like this:

![Okta ](https://storage.googleapis.com/gtidocresources/guides/group-management/images/okta_details_20231026.png)

## 8.-copy-data-in-google-threat-intelligence

Copy those values in your Google Threat Intelligence’s group configuration available at <https://www.virustotal.com/gui/group/GROUP_NAME/settings> and click on Save SSO data:

![Okta Google Threat Intelligence group settings](https://storage.googleapis.com/gtidocresources/guides/group-management/images/okta_vtgroupsettings_20240606.png)

## 9.-copy-the-google-threat-intelligence-sign-in-url

Copy the URL at the “Google Threat Intelligence sign-in URL” section and use it to configure a bookmark app that will launch the sign-in process.

![Okta Copy URL](https://storage.googleapis.com/gtidocresources/guides/group-management/images/okta_copyurl_20240606.png)

![Okta Add Bookmark](https://storage.googleapis.com/gtidocresources/guides/group-management/images/okta_addbookmark_20231026.png)

## 10.-bookmark-app

Your users must use the bookmark app to login into Google Threat Intelligence. Make sure the SAML app is hidden for them.

![Okta Hide Icon](https://storage.googleapis.com/gtidocresources/guides/group-management/images/okta_hideicon_20231026.png)

# troubleshooting

This section aims to provide steps to solve the most common issues when setting up a SAML configuration.

* *Unable to Process request due to missing initial state. This may happen if browser sessionStorage is inaccessible or accidentally cleared*: Check the reply URL is configured correctly on your IdP configuration.

* *Pop up blocked*: The signin dialog opens in a popup, so you need to explicitly allow virustotal.com to open popups.

* *Response\<Issuer> mismatch*: the field "identity provider issuer" must be an URL to your SAML provider.

* *Error: app\_not\_configured\_for\_user*: Specifically when configuring SAML using Google Workspace. This error occurs when attempting to log into signin.blackbaud.com using a BBID enabled Google account while another Google account is already signed in in the browser

* *User is not assigned to this application.*: Contact your group administrators so they can add you to the user list on Okta.

If you still need assistance, [contact our support team](https://www.virustotal.com/gui/contact-us/technical-support) attaching the SAML XML configuration.

---

← [Single Sign On Authentication](sso-authentication.md) · [up](README.md) · [Configure SAML with Ping](saml-ping.md) →

*Archived from <https://gtidocs.virustotal.com/docs/saml-okta>.*
