---
title: "Configure SAML with Ping"
source: https://gtidocs.virustotal.com/docs/saml-ping
slug: saml-ping
section: guides
group: "Group Management"
updatedAt: 2025-09-25T02:35:16.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [Guides](../README.md) › [Group Management](README.md) › Configure SAML with Ping

---

# configure-saml-with-ping

# set-up

## 1.-create-app

In the Ping Identity dashboard, go to applications and create a new application by clicking on the "+" icon in the upper part of the application.

![PingIdentity dashboard](https://storage.googleapis.com/gtidocresources/guides/group-management/images/saml_ping_1_20240723.png)

## 2.-configure-app

Fill the necessary data, select "SAML" as application type and finally click on "Configure":

![Create SAML app](https://storage.googleapis.com/gtidocresources/guides/group-management/images/saml_ping_2_20240723.png)

## 3.-acs-url-and-audience

Fill the ACS URL (which is `https://virustotalcloud.firebaseapp.com/__/auth/handler`) and the entity ID (which will be used as **audience in the Google Threat Intelligence config**). The entity ID must be unique so make sure not to use a generic string such as "test" or "example". After that click on "Save".

![ACS URL and audience](https://storage.googleapis.com/gtidocresources/guides/group-management/images/saml_ping_3_20240723.png)

## 4.-retrieve-app-data

Enable the app and retrieve the necessary data required on the Google Threat Intelligence configuration: the certificate, issuer ID and SSO URL:

![Certificate, issuer ID and SSO URL](https://storage.googleapis.com/gtidocresources/guides/group-management/images/saml_ping_4_20240723.png)

## 5.-google-threat-intelligence-configuration

Fill this data in the Google TI configuration:

![VT configuration](https://storage.googleapis.com/gtidocresources/guides/group-management/images/saml_ping_5_20240723.png)

## 6.-attribute-mappings

Edit the attribute mappings to use email instead of user ID. To do so, go back to the PingIdentity dashboard and click on the "Attribute mappings" tab. Click on the "edit" button highlighted in the following screenshot:

![Correct attribute mappings](https://storage.googleapis.com/gtidocresources/guides/group-management/images/saml_ping_6_20240723.png)

## 7.-login-url

Share the login URL with your users to login in Google TI.

---

← [Configure SAML with Okta](saml-okta.md) · [up](README.md) · [Configure SAML with Entra ID](saml-entraid.md) →

*Archived from <https://gtidocs.virustotal.com/docs/saml-ping>.*
