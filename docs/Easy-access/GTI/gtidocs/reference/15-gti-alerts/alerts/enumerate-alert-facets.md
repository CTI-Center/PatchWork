---
title: "Enumerate Facets"
source: https://gtidocs.virustotal.com/reference/enumerate-alert-facets
slug: enumerate-alert-facets
section: reference
group: "GTI Alerts"
updatedAt: 2026-03-06T12:09:47.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [GTI Alerts](../README.md) › [Alerts](../alerts.md) › Enumerate Facets

---

# enumerate-facets

EnumerateAlertFacets returns the facets and the number of alerts that meet
the filter criteria and have that value for each facet.

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
      "EnumerateAlertFacetsResponse": {
        "description": "Response message for EnumerateAlertFacets.",
        "type": "object",
        "properties": {
          "facets": {
            "description": "List of facets and the counts.",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Facet"
            }
          }
        }
      },
      "Facet": {
        "description": "Facet represents a sub element of a resource for filtering.\nThe results from this method are used to populate the filterable facets in\nthe UI.",
        "type": "object",
        "properties": {
          "facet": {
            "description": "Name of the facet. This is also the string that needs to be used in the\nfiltering expression.",
            "type": "string"
          },
          "facetCounts": {
            "description": "List of counts for the facet (if categorical).",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/FacetCount"
            }
          },
          "facetType": {
            "description": "The type of the facet. Options include \"string\", \"int\", \"float\", \"bool\",\n\"enum\", \"timestamp\", \"user\" and are useful to show the right sort of\nUI controls when building a AIP-160 style filtering string.",
            "type": "string"
          },
          "minValue": {
            "description": "Min value of the facet stringified based on type. This is only populated\nfor facets that have a clear ordering, for types like enum it will be\nleft empty.\nTimestamps will be formatted using RFC3339.",
            "type": "string"
          },
          "maxValue": {
            "description": "Max value of the facet stringified based on type. Will be populated and\nformatted the same as min_value.",
            "type": "string"
          },
          "totalCount": {
            "description": "Total number of records that contain this facet with ANY value.",
            "type": "string",
            "format": "int64"
          }
        }
      },
      "FacetCount": {
        "description": "FacetCount represents a count of records with each facet value.",
        "type": "object",
        "properties": {
          "value": {
            "description": "Value of the facet stringified.\nTimestamps will be formatted using RFC3339.",
            "type": "string"
          },
          "count": {
            "description": "Count of records with the value.",
            "type": "integer",
            "format": "int32"
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
    "/v1beta/projects/{project}/alerts:enumerateFacets": {
      "get": {
        "tags": [
          "threatintelligence"
        ],
        "operationId": "EnumerateAlertFacets",
        "description": "EnumerateAlertFacets returns the facets and the number of alerts that meet\nthe filter criteria and have that value for each facet.",
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
            "name": "filter",
            "description": "Optional. Filter on what alerts will be enumerated.",
            "in": "query",
            "schema": {
              "type": "string"
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
        "responses": {
          "default": {
            "description": "Successful operation",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/EnumerateAlertFacetsResponse"
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

← [List Alerts](list-alerts.md) · [up](../README.md) · [Triage Alerts](triage-alerts.md) →

*Archived from <https://gtidocs.virustotal.com/reference/enumerate-alert-facets>.*
