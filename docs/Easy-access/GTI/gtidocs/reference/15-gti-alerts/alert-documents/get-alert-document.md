---
title: "Get Document"
source: https://gtidocs.virustotal.com/reference/get-alert-document
slug: get-alert-document
section: reference
group: "GTI Alerts"
updatedAt: 2026-03-06T12:09:47.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [GTI Alerts](../README.md) › [Alert Documents](../alert-documents.md) › Get Document

---

# get-document

Gets a specific document associated with an alert.

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
      "AlertDocument": {
        "description": "A document that is associated with an alert.",
        "type": "object",
        "properties": {
          "name": {
            "description": "Identifier. Server generated name for the alert document.\nformat is projects/{project}/alerts/{alert}/documents/{document}",
            "x-google-identifier": true,
            "type": "string"
          },
          "content": {
            "description": "Output only. The content of the document.",
            "readOnly": true,
            "type": "string"
          },
          "author": {
            "description": "Output only. The author of the document.",
            "readOnly": true,
            "type": "string"
          },
          "createTime": {
            "description": "Output only. The time the document was created.",
            "readOnly": true,
            "type": "string",
            "format": "date-time"
          },
          "languageCode": {
            "description": "Output only. The language code of the document.",
            "readOnly": true,
            "type": "string"
          },
          "title": {
            "description": "Output only. The title of the document, if available.",
            "readOnly": true,
            "type": "string"
          },
          "aiSummary": {
            "description": "Output only. AI summary of the finding.",
            "readOnly": true,
            "type": "string"
          },
          "translation": {
            "description": "Output only. The translation of the document, if available.",
            "readOnly": true,
            "allOf": [
              {
                "$ref": "#/components/schemas/AlertDocumentTranslation"
              }
            ]
          },
          "source": {
            "description": "Output only. Source of the intel item, e.g. DarkMarket.",
            "readOnly": true,
            "type": "string"
          },
          "sourceUri": {
            "description": "Output only. URI of the intel item from the source.",
            "readOnly": true,
            "type": "string"
          },
          "ingestTime": {
            "description": "Output only. Time when GTI received the intel.",
            "readOnly": true,
            "type": "string",
            "format": "date-time"
          },
          "collectionTime": {
            "description": "Output only. Time when the origin source collected the intel.",
            "readOnly": true,
            "type": "string",
            "format": "date-time"
          },
          "sourceUpdateTime": {
            "description": "Output only. Time when the intel was last updated by the source.",
            "readOnly": true,
            "type": "string",
            "format": "date-time"
          }
        }
      },
      "AlertDocumentTranslation": {
        "description": "The translation of an alert document.",
        "type": "object",
        "properties": {
          "translatedTitle": {
            "description": "Output only. The translated title of the document.",
            "readOnly": true,
            "type": "string"
          },
          "translatedContent": {
            "description": "Output only. The translated content of the document.",
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
    "/v1beta/projects/{project}/alerts/{alert}/documents/{document}": {
      "get": {
        "tags": [
          "threatintelligence"
        ],
        "operationId": "GetAlertDocument",
        "description": "Gets a specific document associated with an alert.",
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
            "name": "alert",
            "description": "Resource ID segment making up resource `name`. It identifies the resource within its parent collection as described in https://google.aip.dev/122.",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "document",
            "description": "Resource ID segment making up resource `name`. It identifies the resource within its parent collection as described in https://google.aip.dev/122.",
            "in": "path",
            "required": true,
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
                  "$ref": "#/components/schemas/AlertDocument"
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

← [Overview](alert-documents-overview.md) · [up](../README.md) · [Configurations](../configurations.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-alert-document>.*
