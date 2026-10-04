---
title: "Get Started"
source: https://gtidocs.virustotal.com/reference/ti-get-started
slug: ti-get-started
section: reference
group: "GTI Alerts"
updatedAt: 2026-08-31T10:09:50.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [GTI Alerts](README.md) › Get Started

---

# get-started

> 🚧 Beta
>
> Google Threat Intelligence Alerts API is provided as a beta feature and is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://cloud.google.com/terms/service-terms), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages).

This guide provides a practical introduction to the Google Threat Intelligence Alerts API. You will learn how to authenticate and perform basic operations against Alerts, Findings, and Configurations using standard HTTP requests. For detailed API documentation, see the [Threat Intelligence API](alerts/alerts-overview.md).

## prerequisites

Before you begin, ensure you have the following:

1. **GTI Alerts Role**: Your user account must have the **GTI Alerts** role (`Admin` or `Member`) assigned within the Google Threat Intelligence portal (under your group/organization user settings).
2. **Google Cloud Project ID**: Your organization's Google Cloud Project ID, assigned by the Google Threat Intelligence team upon onboarding. You can retrieve this ID directly from the URL when accessing the GTI Alerts portal (e.g., `https://proactive.virustotal.com/alerts?...&project=projects%2F**your-project-id**`), or request it from your group administrator or account team.
3. **GTI API Key**: A GTI API key, which you can find in the GTI UI under [Profile > API Key](https://www.virustotal.com/gui/my-apikey).

> 📘
>
> **Web UI Visibility & Troubleshooting:**
>
> * **Missing GTI Alerts in UI menu**: If you cannot see the GTI Alerts / ATD section in the portal navigation bar, verify with your group administrator that **AI features are enabled** in your group preferences, as ATD is categorized as an AI-powered capability.
> * **Troubleshooting 403 Errors:** If you encounter a `403 PERMISSION_DENIED` error when calling the API, ensure your GTI administrator has assigned you the **GTI Alerts** role in the GTI portal.

### authentication

The API requires OAuth 2.0 authentication. You can exchange your GTI API key for an access token using the following endpoint:

```sh
curl https://idp.prod.identity.proactive.virustotal.com/realms/master/exchange/api-key \
  -H "Content-Type: application/json" \
  -d '{"api_key": "YOUR_API_KEY"}'
```

The response will contain the access token and its expiration time (usually 4 hours).

```json
{
  "access_token": "YOUR_ACCESS_TOKEN",
  "issued_token_type": "urn:ietf:params:oauth:token-type:access_token",
  "token_type": "Bearer",
  "expires_in": 14398
}
```

## working-with-alerts

[Alerts](alerts.md) are the primary actionable units in the system. They represent consolidated groups of findings that require your attention.

### list-alerts

Retrieve all alerts for your project. Note by default, the alerts returned are unordered.

```sh
curl -H "x-goog-user-project: YOUR_ORG_PROJECT_ID" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     "https://threatintelligence.googleapis.com/v1beta/projects/YOUR_ORG_PROJECT_ID/alerts"
```

### list-alerts-with-filtering-and-orderby

Retrieve a filtered list of alerts for your project and order the results.

The following example only filters for the `data_leak` [alert detail](alerts/alerts-overview.md#alertdetail) type with a `HIGH` [severity](alerts/alerts-overview.md#dataleakalertdetail), and orders the results by create time with latest alerts first. For more filtering and ordering options with examples, see the [List Alerts API reference](alerts/list-alerts.md).

```sh
curl -G \
     -H "x-goog-user-project: YOUR_ORG_PROJECT_ID" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     --data-urlencode 'filter=((detail.data_leak.severity="HIGH"))' \
     --data-urlencode 'orderBy=audit.create_time desc' \
     "https://threatintelligence.googleapis.com/v1beta/projects/YOUR_ORG_PROJECT_ID/alerts"
```

### get-an-alert

Retrieve full details for a specific alert using its resource ID. This includes the generated summary, severity scores, and status. You can get the resource ID from the `name` field in the response from the [List Alerts](#list-alerts) call.

```sh
# Replace ALERT_ID with the specific ID. 
curl -H "x-goog-user-project: YOUR_ORG_PROJECT_ID" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     "https://threatintelligence.googleapis.com/v1beta/projects/YOUR_ORG_PROJECT_ID/alerts/ALERT_ID"
```

## working-with-configurations

[Configurations](configurations.md) hold your Customer Profile and Threat Scenarios, which define what the system matches for.

### list-configurations

See all configurations associated with your project.

```sh
curl -H "x-goog-user-project: YOUR_ORG_PROJECT_ID" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     "https://threatintelligence.googleapis.com/v1beta/projects/YOUR_ORG_PROJECT_ID/configurations"
```

### get-a-configuration

View the details of a specific configuration, such as your defined profiles and threat scenarios.

```sh
# Replace CONFIG_ID with the specific ID. You can get the ID from the name field in the response from the [List Configurations](#list-configurations) call.
curl -H "x-goog-user-project: YOUR_ORG_PROJECT_ID" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     "https://threatintelligence.googleapis.com/v1beta/projects/YOUR_ORG_PROJECT_ID/configurations/CONFIG_ID"
```

### upserting-configurations

#### customer-profile

A CustomerProfile configuration is created by default when an organization is onboarded. Additional CustomerProfile configurations cannot be added, but the initial configuration can be updated. The example below shows how to add a new product, YouTube, to an existing CustomerProfile that currently only includes Google Cloud. You can replace each of the fields in the example below with your own values from the [List Configurations](#list-configurations) call above.

```shell
# Replace CONFIG_ID with the specific ID.
curl -X POST -H "x-goog-user-project: YOUR_ORG_PROJECT_ID" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "projects/YOUR_ORG_PROJECT_ID/configurations/CONFIG_ID",
       "provider": "GTI Alerts",
       "state": "ENABLED",
       "detail": {
         "customerProfile": {
           "org": "Google",
           "products": [
             {
               "product": "Cloud",
               "brand": "Google Cloud"
             },
             {
               "product": "Video Platform",
               "brand": "YouTube"
             }
           ]
         }
       }
     }' \
     "https://threatintelligence.googleapis.com/v1beta/projects/YOUR_ORG_PROJECT_ID/configurations:upsert"
```

#### threat-scenario-configurations

The example below shows how to create a new [TechnologyWatchList](configurations/configurations-overview.md#technologywatchlistconfig) threat scenario configuration.

```shell
# Replace CONFIG_ID with the specific ID.
curl -X POST -H "x-goog-user-project: YOUR_ORG_PROJECT_ID" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "projects/YOUR_ORG_PROJECT_ID/configurations/CONFIG_ID",
       "provider": "GTI Alerts",
       "state": "ENABLED",
       "detail": {
         "technologyWatchlist": {
           "technologies": [
             "Cloud"
           ],
           "alertThreshold": {
            "priorityMinimum": "P1",
            "cvssScoreMinimum": 7.0,
            "epssScoreMinimum": 0.8,
            "exploitationStates": [
               "EXPLOITATION_STATE_CONFIRMED"
             ],
            "riskRatingMinimum": "MEDIUM"
           }
         }
       }
     }' \
     "https://threatintelligence.googleapis.com/v1beta/projects/YOUR_ORG_PROJECT_ID/configurations:upsert"
```

## working-with-findings

[Findings](findings.md) are the raw pieces of evidence (e.g., a specific forum post or leaked credential) that are aggregated into Alerts.

### list-findings

Retrieve all findings for your project.

```sh
curl -H "x-goog-user-project: YOUR_ORG_PROJECT_ID" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     "https://threatintelligence.googleapis.com/v1beta/projects/YOUR_ORG_PROJECT_ID/findings"
```

### get-a-finding

Get the complete technical details of a specific finding. You can get the ID from the `name` field in the response from the [List Findings](#list-findings) call.

```sh
# Replace FINDING_ID with the specific ID.
curl -H "x-goog-user-project: YOUR_ORG_PROJECT_ID" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     "https://threatintelligence.googleapis.com/v1beta/projects/YOUR_ORG_PROJECT_ID/findings/FINDING_ID"
```

<br />

---

← [Key Concepts](ti-key-concepts.md) · [up](README.md) · [Authentication](ti-get-started/ti-authentication.md) →

*Archived from <https://gtidocs.virustotal.com/reference/ti-get-started>.*
