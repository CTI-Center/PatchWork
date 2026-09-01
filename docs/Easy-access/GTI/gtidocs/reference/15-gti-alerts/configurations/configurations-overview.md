---
title: "Overview"
source: https://gtidocs.virustotal.com/reference/configurations-overview
slug: configurations-overview
section: reference
group: "GTI Alerts"
updatedAt: 2026-06-18T07:32:59.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [GTI Alerts](../README.md) › [Configurations](../configurations.md) › Overview

---

# overview

## resource:-configuration

A configuration represents a behavior an engine should follow when producing new findings.

```json JSON representation
{
  "name": string,
  "displayName": string,
  "audit": {
    object (Audit)
  },
  "provider": string,
  "state": enum (State),
  "detail": {
    object (ConfigurationDetail)
  },
  "version": string,
  "description": string
}
```

<br />

| Fields        |                                                                                                                                          |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `name`        | `string`<br /><br />Identifier. Server generated name for the configuration. format is projects/{project}/configurations/{configuration} |
| `displayName` | `string`<br /><br />Output only. Human readable name for the configuration.                                                              |
| `audit`       | `object (`[Audit](../../17-api-objects/alerts-object/audit-object.md) `)`<br /><br />Output only. Audit information for the configuration.                                 |
| `provider`    | `string`<br /><br />Required. Name of the service that provides the configuration.                                                       |
| `state`       | `enum (`[State](#state)  `)`<br /><br />Optional. State of the configuration.                                                            |
| `detail`      | `object (`[ConfigurationDetail](#configurationdetail) `)`<br /><br />Required. Domain specific details for the configuration.            |
| `version`     | `string`<br /><br />Optional. A user-manipulatable version. Does not adhere to a specific format                                         |
| `description` | `string`<br /><br />Optional. A description of the configuration.                                                                        |

## state

State of the configuration.

| Enums               |                                                                        |
| ------------------- | ---------------------------------------------------------------------- |
| `STATE_UNSPECIFIED` | Configuration state is unspecified. This is not expected to occur.     |
| `ENABLED`           | Configuration is enabled for the customer.                             |
| `DISABLED`          | Configuration is disabled for the customer.                            |
| `DEPRECATED`        | Configuration is deprecated, no new configs are allowed to be created. |

## configurationdetail

Wrapper class that contains the union struct for all the various configuration detail specific classes.

```json JSON representation
{
  "detailType": string,

  // Union field detail can be only one of the following:
  "customerProfile": {
    object (CustomerProfileConfig)
  },
  "technologyWatchlist": {
    object (TechnologyWatchListConfig)
  }
  // End of list of possible types for union field detail.
}
```

<br />

| Fields                                                                                           |                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `detailType`                                                                                     | `string`<br /><br />Output only. Name of the detail type. Will be set by the server during creation to the name of the field that is set in the detail union. |
| Union field `detail`. Domain specific details object. `detail` can be only one of the following: |                                                                                                                                                               |
| `customerProfile`                                                                                | `object (`[CustomerProfileConfig](#customerprofileconfig) `)`<br /><br />Customer Profile detail config.                                                      |
| `technologyWatchlist`                                                                            | `object (`[TechnologyWatchListConfig](#technologywatchlistconfig) `)`<br /><br />Technology Watchlist detail config.                                          |

## customerprofileconfig

ustomerProfileConfig is the configuration for the customer profile. See [Get Started](https://gtidocs.readme.io/docs/get-started#customer-profile) for more details on creating and managing configurations.

```json JSON representation
{
  "org": string,
  "orgSummary": string,
  "industries": [
    {
      object (CustomerProfileIndustry)
    }
  ],
  "parentCompanies": [
    {
      object (CustomerProfileCompany)
    }
  ],
  "products": [
    {
      object (CustomerProfileProduct)
    }
  ],
  "locations": [
    {
      object (CustomerProfileLocation)
    }
  ],
  "executives": [
    {
      object (CustomerProfilePerson)
    }
  ],
  "webPresences": [
    {
      object (CustomerProfileWebPresence)
    }
  ],
  "technologyPresence": string,
  "securityConsiderations": {
    object (CustomerProfileSecurityConsiderations)
  },
  "contactInfo": [
    {
      object (CustomerProfileContactInfo)
    }
  ],
  "citations": [
    {
      object (CustomerProfileCitation)
    }
  ],
  "summary": {
    object (CustomerProfileSummary)
  }
}
```

<br />

| Fields                   |                                                                                                                                                                  |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `org`                    | `string`<br /><br />Required. The name of the organization.                                                                                                      |
| `orgSummary`             | `string`<br /><br />Optional. A summary of the organization.                                                                                                     |
| `industries[]`           | `object (`[CustomerProfileIndustry](#customerprofileindustry) `)`<br /><br />Optional. The industries the organization is involved in.                           |
| `parentCompanies[]`      | `object (`[CustomerProfileCompany](#customerprofilecompany) `)`<br /><br />Optional. The parent companies of the organization.                                   |
| `products[]`             | `object (`[CustomerProfileProduct](#customerprofileproduct) `)`<br /><br />Optional. Product information for the organization.                                   |
| `locations[]`            | `object (`[CustomerProfileLocation](#customerprofilelocation) `)`<br /><br />Optional. Locations the organization is present or conducts business in.            |
| `executives[]`           | `object (`[CustomerProfilePerson](#customerprofileperson) `)`<br /><br />Optional. Executives of the organization.                                               |
| `webPresences[]`         | `object (`[CustomerProfileWebPresence](#customerprofilewebpresence) `)`<br /><br />Optional. Web presence of the organization.                                   |
| `technologyPresence`     | `string`<br /><br />Optional. Technology presence of the organization.                                                                                           |
| `securityConsiderations` | `object (`[CustomerProfileSecurityConsiderations](#customerprofilesecurityconsiderations) `)`<br /><br />Optional. Security considerations for the organization. |
| `contactInfo[]`          | `object (`[CustomerProfileContactInfo](#customerprofilecontactinfo) `)`<br /><br />Optional. Contact information for the organization.                           |
| `citations[]`            | `object (`[CustomerProfileCitation](#customerprofilecitation) `)`<br /><br />Optional. Citations for the organization profile.                                   |
| `summary`                | `object (`[CustomerProfileSummary](#customerprofilesummary) `)`<br /><br />Optional. A summarized version of the customer profile.                               |

## customerprofileindustry

Industry information for the customer profile.

```json JSON representation
{
  "industry": string,
  "citationIds": [
    string
  ]
}
```

<br />

| Fields          |                                                                  |
| --------------- | ---------------------------------------------------------------- |
| `industry`      | `string`<br /><br />Required. The name of the industry.          |
| `citationIds[]` | `string`<br /><br />Optional. The citation ids for the industry. |

## customerprofilecompany

Company information for the customer profile.

```json JSON representation
{
  "company": string,
  "citationIds": [
    string
  ]
}
```

<br />

| Fields          |                                                                 |
| --------------- | --------------------------------------------------------------- |
| `company`       | `string`<br /><br />Required. The name of the company.          |
| `citationIds[]` | `string`<br /><br />Optional. The citation ids for the company. |

## customerprofileproduct

Product information for the customer profile.

```json JSON representation
{
  "product": string,
  "brand": string,
  "citationIds": [
    string
  ]
}
```

<br />

| Fields          |                                                                 |
| --------------- | --------------------------------------------------------------- |
| `product`       | `string`<br /><br />Required. The name of the product.          |
| `brand`         | `string`<br /><br />Required. The brand of the product.         |
| `citationIds[]` | `string`<br /><br />Optional. The citation ids for the product. |

## customerprofilelocation

Location information for the customer profile.

```json JSON representation
{
  "facilityType": string,
  "brand": string,
  "address": string,
  "citationIds": [
    string
  ]
}
```

<br />

| Fields          |                                                                  |
| --------------- | ---------------------------------------------------------------- |
| `facilityType`  | `string`<br /><br />Optional. The type of location.              |
| `brand`         | `string`<br /><br />Required. The brand of the location.         |
| `address`       | `string`<br /><br />Required. The address of the location.       |
| `citationIds[]` | `string`<br /><br />Optional. The citation ids for the location. |

## customerprofileperson

Person information for the customer profile.

```json JSON representation
{
  "name": string,
  "title": string,
  "citationIds": [
    string
  ]
}
```

| Fields          |                                                                |
| --------------- | -------------------------------------------------------------- |
| `name`          | `string`<br /><br />Required. The name of the person.          |
| `title`         | `string`<br /><br />Optional. The title of the person.         |
| `citationIds[]` | `string`<br /><br />Optional. The citation ids for the person. |

## customerprofilewebpresence

Web presence information for the customer profile.

```json JSON representation
{
  "domain": string,
  "citationIds": [
    string
  ]
}
```

<br />

| Fields          |                                                                      |
| --------------- | -------------------------------------------------------------------- |
| `domain`        | `string`<br /><br />Required. The domain name of the web presence.   |
| `citationIds[]` | `string`<br /><br />Optional. The citation ids for the web presence. |

## customerprofilesecurityconsiderations

Security considerations for the customer profile.

```json JSON representation
{
  "note": string,
  "considerations": [
    string
  ]
}
```

<br />

| Fields             |                                                                                                                                                                    |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `note`             | `string`<br /><br />Optional. A note about the security considerations.                                                                                            |
| `considerations[]` | `string`<br /><br />Optional. A series of considerations for the security of the organization, such as "high risk of compromise" or "vulnerable to cyberbullying". |

## customerprofilecontactinfo

Contact information for the customer profile.

```json JSON representation
{
  "label": string,
  "citationIds": [
    string
  ],

  // Union field contact_info can be only one of the following:
  "email": string,
  "phone": string,
  "address": string,
  "other": string
  // End of list of possible types for union field contact_info.
}
```

<br />

| Fields                                                                                                                         |                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| `label`                                                                                                                        | `string`<br /><br />Optional. The name of the contact.                      |
| `citationIds[]`                                                                                                                | `string`<br /><br />Optional. The citation ids for the contact information. |
| Union field `contact_info`. The contact information for the customer profile. `contact_info` can be only one of the following: |                                                                             |
| `email`                                                                                                                        | `string`<br /><br />The email address of the contact.                       |
| `phone`                                                                                                                        | `string`<br /><br />The phone number of the contact.                        |
| `address`                                                                                                                      | `string`<br /><br />The address of the contact.                             |
| `other`                                                                                                                        | `string`<br /><br />The other contact information.                          |

## customerprofilecitation

Citation information for the customer profile.

```json JSON representation
{
  "citationId": string,
  "uri": string,
  "retrievalTime": string,
  "source": string,
  "document": string
}
```

<br />

| Fields          |                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `citationId`    | `string`<br /><br />Required. The citation id for the citation. Should be unique within the profile.                                                                                                                                                                                                                                                                                                                         |
| `uri`           | `string`<br /><br />Optional. The url of the citation.                                                                                                                                                                                                                                                                                                                                                                       |
| `retrievalTime` | `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) ` format)`<br /><br />The time the citation was retrieved.<br /><br />Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |
| `source`        | `string`<br /><br />Required. The source of the citation.                                                                                                                                                                                                                                                                                                                                                                    |
| `document`      | `string`<br /><br />Required. The name of the document the citation is from.                                                                                                                                                                                                                                                                                                                                                 |

## customerprofilesummary

A summarized version of the customer profile. Generated by the backend.

```json JSON representation
{
  "title": {
    object (CustomerProfileCitedString)
  },
  "entityType": {
    object (CustomerProfileCitedString)
  },
  "industry": {
    object (CustomerProfileCitedString)
  },
  "founded": {
    object (CustomerProfileCitedString)
  },
  "headquarters": {
    object (CustomerProfileCitedString)
  },
  "areaServed": {
    object (CustomerProfileCitedString)
  },
  "keyPeopleSummary": {
    object (CustomerProfileCitedString)
  },
  "productsSummary": {
    object (CustomerProfileCitedString)
  },
  "servicesSummary": {
    object (CustomerProfileCitedString)
  },
  "brands": {
    object (CustomerProfileCitedString)
  },
  "parentCompany": {
    object (CustomerProfileCitedString)
  },
  "primaryWebsite": {
    object (CustomerProfileCitedString)
  }
}
```

<br />

| Fields             |                                                                                                                                   |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `title`            | `object (`[CustomerProfileCitedString](#customerprofilecitedstring) `)`<br /><br />Optional. The official name of the customer.   |
| `entityType`       | `object (`[CustomerProfileCitedString](#customerprofilecitedstring) `)`<br /><br />Optional. The entity type of the customer.     |
| `industry`         | `object (`[CustomerProfileCitedString](#customerprofilecitedstring) `)`<br /><br />Optional. The industry the customer is in.     |
| `founded`          | `object (`[CustomerProfileCitedString](#customerprofilecitedstring) `)`<br /><br />Optional. The date the customer was founded.   |
| `headquarters`     | `object (`[CustomerProfileCitedString](#customerprofilecitedstring) `)`<br /><br />Optional. The headquarters of the customer.    |
| `areaServed`       | `object (`[CustomerProfileCitedString](#customerprofilecitedstring) `)`<br /><br />Optional. The area the customer serves.        |
| `keyPeopleSummary` | `object (`[CustomerProfileCitedString](#customerprofilecitedstring) `)`<br /><br />Optional. A narrative summary of key people.   |
| `productsSummary`  | `object (`[CustomerProfileCitedString](#customerprofilecitedstring) `)`<br /><br />Optional. A narrative summary of products.     |
| `servicesSummary`  | `object (`[CustomerProfileCitedString](#customerprofilecitedstring) `)`<br /><br />Optional. A narrative summary of services.     |
| `brands`           | `object (`[CustomerProfileCitedString](#customerprofilecitedstring) `)`<br /><br />Optional. A narrative summary of brands.       |
| `parentCompany`    | `object (`[CustomerProfileCitedString](#customerprofilecitedstring) `)`<br /><br />Optional. The parent company of the customer.  |
| `primaryWebsite`   | `object (`[CustomerProfileCitedString](#customerprofilecitedstring) `)`<br /><br />Optional. The primary website of the customer. |

## customerprofilecitedstring

A string with citation ids.

```json JSON representation
{
  "value": string,
  "citationIds": [
    string
  ]
}
```

<br />

| Fields          |                                                                |
| --------------- | -------------------------------------------------------------- |
| `value`         | `string`<br /><br />Required. The value of the string.         |
| `citationIds[]` | `string`<br /><br />Optional. The citation ids for the string. |

## technologywatchlistconfig

TechnologyWatchListConfig is the configuration for the technology watchlist threat scenario. See [Get Started](/threat-intelligence/guides/get-started#threat-scenario-configurations) for more details on creating and managing threat scenario configurations.

```json
{
  "technologies": [
    string
  ],
  "alertThreshold": {
    object (TechnologyWatchListAlertThreshold)
  }
}
```

<br />

| Fields           |                                                                                                                                                                   |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `technologies[]` | `string`<br /><br />Optional. List of vendor, technology or cpe fingerprint. exam``le: `Microsoft office 360 Apache Server 3.5 cpe:2.3microsoft:outlook::::::::`` |
| `alertThreshold` | `object (`[TechnologyWatchListAlertThreshold](#technologywatchlistalertthreshold) `)`<br /><br />Optional. Alert thresholds to effectively reduce noise.          |

## technologywatchlistalertthreshold

TechnologyWatchListAlertThreshold contains the thresholds for alerting.

```json JSON representation
{
  "priorityMinimum": enum (Priority),
  "cvssScoreMinimum": number,
  "epssScoreMinimum": number,
  "exploitationStates": [
    enum (ExploitationState)
  ],
  "riskRatingMinimum": enum (RiskRating)
}
```

<br />

| Fields           |                                                                                                                                                                  |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `technologies[]` | `string`<br /><br />Optional. List of vendor, technology or cpe fingerprint. example: Microsoft office 360 Apache Server 3.5 cpe:2.3:a:microsoft:outlook:::::::: |
| `alertThreshold` | `object (`[TechnologyWatchListAlertThreshold](#technologywatchlistalertthreshold) `)`<br /><br />Optional. Alert thresholds to effectively reduce noise.         |

## technologywatchlistalertthreshold

TechnologyWatchListAlertThreshold contains the thresholds for alerting.

```json
json JSON representation
{
  "priorityMinimum": enum (Priority),
  "cvssScoreMinimum": number,
  "epssScoreMinimum": number,
  "exploitationStates": [
    enum (ExploitationState)
  ],
  "riskRatingMinimum": enum (RiskRating)
}
```

| Fields                 |                                                                                                                                                                             |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `priorityMinimum`      | `enum (Priority)`<br /><br />Optional. The minimum priority for the alert.                                                                                                  |
| `cvssScoreMinimum`     | `number`<br /><br />Optional. The minimum CVSS score for the alert. Evaluates to CVSS v3 when available with a fallback to v2 and v4. Ex: 7.0. Valid range is \[0.0, 10.0]. |
| `epssScoreMinimum`     | `number`<br /><br />Optional. The minimum epss score for the alert. Ex: 0.8. Valid range is \[0.0, 1.0].                                                                    |
| `exploitationStates[]` | `enum (ExploitationState)`<br /><br />Optional. The exploitation states of the alert.                                                                                       |
| `riskRatingMinimum`    | `enum (RiskRating)`<br /><br />Optional. The minimum risk rating for the alert.                                                                                             |

### methods

|                                    |                                                             |
| ---------------------------------- | ----------------------------------------------------------- |
| [get](get-configuration.md)       | Get a configuration by name.                                |
| [list](list-configurations.md)    | Get a list of configurations that meet the filter criteria. |
| [upsert](upsert-configuration.md) | Creates or updates a configuration.                         |

<br />

---

← [Configurations](../configurations.md) · [up](../README.md) · [Get Configuration](get-configuration.md) →

*Archived from <https://gtidocs.virustotal.com/reference/configurations-overview>.*
