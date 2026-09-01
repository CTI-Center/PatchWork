---
title: "Upsert Configuration"
source: https://gtidocs.virustotal.com/reference/upsert-configuration
slug: upsert-configuration
section: reference
group: "GTI Alerts"
updatedAt: 2026-03-06T12:09:47.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [GTI Alerts](../README.md) › [Configurations](../configurations.md) › Upsert Configuration

---

# upsert-configuration

Creates or updates a configuration.

# openapi-definition

```json
{
  "externalDocs": {
    "description": "Find more info here.",
    "url": "https://docs.cloud.google.com/threatintelligence/"
  },
  "components": {
    "securitySchemes": {
      "google_oauth_implicit": {
        "type": "oauth2",
        "description": "Google Oauth 2.0 implicit authentication flow.",
        "flows": {
          "implicit": {
            "authorizationUrl": "https://accounts.google.com/o/oauth2/v2/auth",
            "scopes": {
              "https://www.googleapis.com/auth/cloud-platform": "See, edit, configure, and delete your Google Cloud data and see the email address for your Google Account."
            }
          }
        }
      },
      "google_oauth_code": {
        "type": "oauth2",
        "description": "Google Oauth 2.0 authorizationCode authentication flow.",
        "flows": {
          "authorizationCode": {
            "authorizationUrl": "https://accounts.google.com/o/oauth2/v2/auth",
            "tokenUrl": "https://oauth2.googleapis.com/token",
            "refreshUrl": "https://oauth2.googleapis.com/token",
            "scopes": {
              "https://www.googleapis.com/auth/cloud-platform": "See, edit, configure, and delete your Google Cloud data and see the email address for your Google Account."
            }
          }
        }
      },
      "bearer_auth": {
        "type": "http",
        "description": "Http bearer authentication.",
        "scheme": "bearer"
      }
    },
    "schemas": {
      "Configuration": {
        "description": "A configuration represents a behavior an engine should follow when producing\nnew findings.",
        "type": "object",
        "properties": {
          "name": {
            "description": "Identifier. Server generated name for the configuration.\nformat is projects/{project}/configurations/{configuration}",
            "x-google-identifier": true,
            "type": "string"
          },
          "displayName": {
            "description": "Output only. Human readable name for the configuration.",
            "readOnly": true,
            "type": "string"
          },
          "audit": {
            "description": "Output only. Audit information for the configuration.",
            "readOnly": true,
            "allOf": [
              {
                "$ref": "#/components/schemas/Audit"
              }
            ]
          },
          "provider": {
            "description": "Required. Name of the service that provides the configuration.",
            "type": "string"
          },
          "state": {
            "description": "Optional. State of the configuration.",
            "type": "string",
            "x-google-enum-descriptions": [
              "Configuration state is unspecified. This is not expected to occur.",
              "Configuration is enabled for the customer.",
              "Configuration is disabled for the customer.",
              "Configuration is deprecated, no new configs are allowed to be created."
            ],
            "enum": [
              "STATE_UNSPECIFIED",
              "ENABLED",
              "DISABLED",
              "DEPRECATED"
            ]
          },
          "detail": {
            "description": "Required. Domain specific details for the configuration.",
            "allOf": [
              {
                "$ref": "#/components/schemas/ConfigurationDetail"
              }
            ]
          },
          "version": {
            "description": "Optional. A user-manipulatable version.  Does not adhere to a specific format",
            "type": "string"
          },
          "description": {
            "description": "Optional. A description of the configuration.",
            "type": "string"
          }
        },
        "required": [
          "provider",
          "detail"
        ]
      },
      "Audit": {
        "description": "Tracks basic CRUD facts.",
        "type": "object",
        "properties": {
          "updateTime": {
            "description": "Output only. Time of creation or last update.",
            "readOnly": true,
            "type": "string",
            "format": "date-time"
          },
          "createTime": {
            "description": "Output only. Time of creation.",
            "readOnly": true,
            "type": "string",
            "format": "date-time"
          },
          "creator": {
            "description": "Output only. Agent that created or updated the record, could be a UserId or a JobId.",
            "readOnly": true,
            "type": "string"
          },
          "updater": {
            "description": "Output only. Agent that last updated the record, could be a UserId or a JobId.",
            "readOnly": true,
            "type": "string"
          }
        }
      },
      "ConfigurationDetail": {
        "description": "Wrapper class that contains the union struct for all the various\nconfiguration detail specific classes.",
        "type": "object",
        "properties": {
          "customerProfile": {
            "description": "Customer Profile detail config.",
            "allOf": [
              {
                "$ref": "#/components/schemas/CustomerProfileConfig"
              }
            ]
          },
          "detailType": {
            "description": "Output only. Name of the detail type. Will be set by the server during creation to the\nname of the field that is set in the detail union.",
            "readOnly": true,
            "type": "string"
          }
        }
      },
      "CustomerProfileConfig": {
        "description": "CustomerProfileConfig is the configuration for the customer profile.",
        "type": "object",
        "properties": {
          "org": {
            "description": "Required. The name of the organization.",
            "type": "string"
          },
          "orgSummary": {
            "description": "Optional. A summary of the organization.",
            "type": "string"
          },
          "industries": {
            "description": "Optional. The industries the organization is involved in.",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CustomerProfileIndustry"
            }
          },
          "parentCompanies": {
            "description": "Optional. The parent companies of the organization.",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CustomerProfileCompany"
            }
          },
          "products": {
            "description": "Optional. Product information for the organization.",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CustomerProfileProduct"
            }
          },
          "locations": {
            "description": "Optional. Locations the organization is present or conducts business in.",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CustomerProfileLocation"
            }
          },
          "executives": {
            "description": "Optional. Executives of the organization.",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CustomerProfilePerson"
            }
          },
          "webPresences": {
            "description": "Optional. Web presence of the organization.",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CustomerProfileWebPresence"
            }
          },
          "technologyPresence": {
            "description": "Optional. Technology presence of the organization.",
            "type": "string"
          },
          "securityConsiderations": {
            "description": "Optional. Security considerations for the organization.",
            "allOf": [
              {
                "$ref": "#/components/schemas/CustomerProfileSecurityConsiderations"
              }
            ]
          },
          "contactInfo": {
            "description": "Optional. Contact information for the organization.",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CustomerProfileContactInfo"
            }
          },
          "citations": {
            "description": "Optional. Citations for the organization profile.",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CustomerProfileCitation"
            }
          },
          "summary": {
            "description": "Optional. A summarized version of the customer profile.",
            "allOf": [
              {
                "$ref": "#/components/schemas/CustomerProfileSummary"
              }
            ]
          }
        },
        "required": [
          "org"
        ]
      },
      "CustomerProfileIndustry": {
        "description": "Industry information for the customer profile.",
        "type": "object",
        "properties": {
          "industry": {
            "description": "Required. The name of the industry.",
            "type": "string"
          },
          "citationIds": {
            "description": "Optional. The citation ids for the industry.",
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "industry"
        ]
      },
      "CustomerProfileCompany": {
        "description": "Company information for the customer profile.",
        "type": "object",
        "properties": {
          "company": {
            "description": "Required. The name of the company.",
            "type": "string"
          },
          "citationIds": {
            "description": "Optional. The citation ids for the company.",
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "company"
        ]
      },
      "CustomerProfileProduct": {
        "description": "Product information for the customer profile.",
        "type": "object",
        "properties": {
          "product": {
            "description": "Required. The name of the product.",
            "type": "string"
          },
          "brand": {
            "description": "Required. The brand of the product.",
            "type": "string"
          },
          "citationIds": {
            "description": "Optional. The citation ids for the product.",
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "product",
          "brand"
        ]
      },
      "CustomerProfileLocation": {
        "description": "Location information for the customer profile.",
        "type": "object",
        "properties": {
          "facilityType": {
            "description": "Optional. The type of location.",
            "type": "string"
          },
          "brand": {
            "description": "Required. The brand of the location.",
            "type": "string"
          },
          "address": {
            "description": "Required. The address of the location.",
            "type": "string"
          },
          "citationIds": {
            "description": "Optional. The citation ids for the location.",
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "brand",
          "address"
        ]
      },
      "CustomerProfilePerson": {
        "description": "Person information for the customer profile.",
        "type": "object",
        "properties": {
          "name": {
            "description": "Required. The name of the person.",
            "type": "string"
          },
          "title": {
            "description": "Optional. The title of the person.",
            "type": "string"
          },
          "citationIds": {
            "description": "Optional. The citation ids for the person.",
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "name"
        ]
      },
      "CustomerProfileWebPresence": {
        "description": "Web presence information for the customer profile.",
        "type": "object",
        "properties": {
          "domain": {
            "description": "Required. The domain name of the web presence.",
            "type": "string"
          },
          "citationIds": {
            "description": "Optional. The citation ids for the web presence.",
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "domain"
        ]
      },
      "CustomerProfileSecurityConsiderations": {
        "description": "Security considerations for the customer profile.",
        "type": "object",
        "properties": {
          "note": {
            "description": "Optional. A note about the security considerations.",
            "type": "string"
          },
          "considerations": {
            "description": "Optional. A series of considerations for the security of the organization,\nsuch as \"high risk of compromise\" or \"vulnerable to cyberbullying\".",
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        }
      },
      "CustomerProfileContactInfo": {
        "description": "Contact information for the customer profile.",
        "type": "object",
        "properties": {
          "email": {
            "description": "The email address of the contact.",
            "type": "string"
          },
          "phone": {
            "description": "The phone number of the contact.",
            "type": "string"
          },
          "address": {
            "description": "The address of the contact.",
            "type": "string"
          },
          "other": {
            "description": "The other contact information.",
            "type": "string"
          },
          "label": {
            "description": "Optional. The name of the contact.",
            "type": "string"
          },
          "citationIds": {
            "description": "Optional. The citation ids for the contact information.",
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        }
      },
      "CustomerProfileCitation": {
        "description": "Citation information for the customer profile.",
        "type": "object",
        "properties": {
          "citationId": {
            "description": "Required. The citation id for the citation.  Should be unique within the profile.",
            "type": "string"
          },
          "uri": {
            "description": "Optional. The url of the citation.",
            "type": "string"
          },
          "retrievalTime": {
            "description": "The time the citation was retrieved.",
            "type": "string",
            "format": "date-time"
          },
          "source": {
            "description": "Required. The source of the citation.",
            "type": "string"
          },
          "document": {
            "description": "Required. The name of the document the citation is from.",
            "type": "string"
          }
        },
        "required": [
          "citationId",
          "source",
          "document"
        ]
      },
      "CustomerProfileSummary": {
        "description": "A summarized version of the customer profile.\nGenerated by the backend.",
        "type": "object",
        "properties": {
          "title": {
            "description": "Optional. The official name of the customer.",
            "allOf": [
              {
                "$ref": "#/components/schemas/CustomerProfileCitedString"
              }
            ]
          },
          "entityType": {
            "description": "Optional. The entity type of the customer.",
            "allOf": [
              {
                "$ref": "#/components/schemas/CustomerProfileCitedString"
              }
            ]
          },
          "industry": {
            "description": "Optional. The industry the customer is in.",
            "allOf": [
              {
                "$ref": "#/components/schemas/CustomerProfileCitedString"
              }
            ]
          },
          "founded": {
            "description": "Optional. The date the customer was founded.",
            "allOf": [
              {
                "$ref": "#/components/schemas/CustomerProfileCitedString"
              }
            ]
          },
          "headquarters": {
            "description": "Optional. The headquarters of the customer.",
            "allOf": [
              {
                "$ref": "#/components/schemas/CustomerProfileCitedString"
              }
            ]
          },
          "areaServed": {
            "description": "Optional. The area the customer serves.",
            "allOf": [
              {
                "$ref": "#/components/schemas/CustomerProfileCitedString"
              }
            ]
          },
          "keyPeopleSummary": {
            "description": "Optional. A narrative summary of key people.",
            "allOf": [
              {
                "$ref": "#/components/schemas/CustomerProfileCitedString"
              }
            ]
          },
          "productsSummary": {
            "description": "Optional. A narrative summary of products.",
            "allOf": [
              {
                "$ref": "#/components/schemas/CustomerProfileCitedString"
              }
            ]
          },
          "servicesSummary": {
            "description": "Optional. A narrative summary of services.",
            "allOf": [
              {
                "$ref": "#/components/schemas/CustomerProfileCitedString"
              }
            ]
          },
          "brands": {
            "description": "Optional. A narrative summary of brands.",
            "allOf": [
              {
                "$ref": "#/components/schemas/CustomerProfileCitedString"
              }
            ]
          },
          "parentCompany": {
            "description": "Optional. The parent company of the customer.",
            "allOf": [
              {
                "$ref": "#/components/schemas/CustomerProfileCitedString"
              }
            ]
          },
          "primaryWebsite": {
            "description": "Optional. The primary website of the customer.",
            "allOf": [
              {
                "$ref": "#/components/schemas/CustomerProfileCitedString"
              }
            ]
          }
        }
      },
      "CustomerProfileCitedString": {
        "description": "A string with citation ids.",
        "type": "object",
        "properties": {
          "value": {
            "description": "Required. The value of the string.",
            "type": "string"
          },
          "citationIds": {
            "description": "Optional. The citation ids for the string.",
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "value"
        ]
      },
      "UpsertConfigurationResponse": {
        "description": "Response message for UpsertConfiguration.",
        "type": "object",
        "properties": {
          "configuration": {
            "description": "Output only. Created configuration ID with server assigned id.",
            "readOnly": true,
            "type": "string"
          }
        }
      }
    }
  },
  "info": {
    "title": "Threat Intelligence API",
    "description": "threatintelligence.googleapis.com API.",
    "version": "v1beta",
    "x-google-revision": "20260218"
  },
  "paths": {
    "/v1beta/projects/{project}/configurations:upsert": {
      "post": {
        "tags": [
          "threatintelligence"
        ],
        "operationId": "UpsertConfiguration",
        "description": "Creates or updates a configuration.",
        "security": [
          {
            "google_oauth_implicit": [
              "https://www.googleapis.com/auth/cloud-platform"
            ]
          },
          {
            "google_oauth_code": [
              "https://www.googleapis.com/auth/cloud-platform"
            ]
          },
          {
            "bearer_auth": []
          }
        ],
        "parameters": [
          {
            "name": "project",
            "description": "Resource ID segment making up resource `name`. It identifies the resource within its parent collection as described in https://google.aip.dev/122.",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "publishTime",
            "description": "Optional. Time that the configuration should be considered to have been published.\nThis is an advanced feature used when onboarding and bulk loading data from\nother systems. Do not set this field without consulting with the API team.",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "description": "Your organization's project ID",
            "in": "header",
            "name": "x-goog-user-project",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "Required. Configuration we are creating or updating.",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Configuration"
              }
            }
          }
        },
        "responses": {
          "default": {
            "description": "Successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/UpsertConfigurationResponse"
                }
              }
            }
          }
        }
      }
    }
  },
  "openapi": "3.0.3",
  "servers": [
    {
      "url": "https://threatintelligence.googleapis.com",
      "description": "Global Endpoint"
    },
    {
      "url": "https://threatintelligence.us-central1.rep.googleapis.com/",
      "description": "Regional Endpoint",
      "x-google-endpoint-location": "us-central1"
    },
    {
      "url": "https://threatintelligence.us-east5.rep.googleapis.com/",
      "description": "Regional Endpoint",
      "x-google-endpoint-location": "us-east5"
    },
    {
      "url": "https://threatintelligence.us-west2.rep.googleapis.com/",
      "description": "Regional Endpoint",
      "x-google-endpoint-location": "us-west2"
    },
    {
      "url": "https://threatintelligence.us.rep.googleapis.com/",
      "description": "Regional Endpoint",
      "x-google-endpoint-location": "us"
    }
  ]
}
```

---

← [List Configurations](list-configurations.md) · [up](../README.md) · [Configuration Revisions](../configuration-revisions.md) →

*Archived from <https://gtidocs.virustotal.com/reference/upsert-configuration>.*
