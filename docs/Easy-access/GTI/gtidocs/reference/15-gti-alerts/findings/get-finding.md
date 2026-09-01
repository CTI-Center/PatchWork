---
title: "Get finding"
source: https://gtidocs.virustotal.com/reference/get-finding
slug: get-finding
section: reference
group: "GTI Alerts"
updatedAt: 2026-03-06T12:09:47.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [GTI Alerts](../README.md) › [Findings](../findings.md) › Get finding

---

# get-finding

Get a finding by name.

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
      "Finding": {
        "description": "A ‘stateless’ and a point in time event that a check produced a result\nof interest.",
        "type": "object",
        "properties": {
          "name": {
            "description": "Identifier. Server generated name for the finding (leave clear during creation).\nFormat: projects/{project}/findings/{finding}",
            "x-google-identifier": true,
            "type": "string"
          },
          "provider": {
            "description": "Required. Logical source of this finding (name of the sub-engine).",
            "type": "string"
          },
          "displayName": {
            "description": "Required. A short descriptive title for the finding <= 250 chars.\nEX: \"Actor 'baddy' offering $1000 for credentials of 'goodguy'\".",
            "type": "string"
          },
          "detail": {
            "description": "Required. Holder of the domain specific details of the finding.",
            "allOf": [
              {
                "$ref": "#/components/schemas/FindingDetail"
              }
            ]
          },
          "severity": {
            "description": "Optional. Deprecated: Use the `severity_analysis` field instead.\nBase severity score from the finding source.",
            "deprecated": true,
            "type": "number",
            "format": "float"
          },
          "reoccurrenceTimes": {
            "description": "Output only. When identical finding (same labels and same details) has re-occurred.",
            "readOnly": true,
            "type": "array",
            "items": {
              "type": "string",
              "format": "date-time"
            }
          },
          "relevanceAnalysis": {
            "description": "Output only. High-Precision Relevance Analysis verdict for the finding.",
            "readOnly": true,
            "allOf": [
              {
                "$ref": "#/components/schemas/RelevanceAnalysis"
              }
            ]
          },
          "severityAnalysis": {
            "description": "Output only. High-Precision Severity Analysis verdict for the finding.",
            "readOnly": true,
            "allOf": [
              {
                "$ref": "#/components/schemas/SeverityAnalysis"
              }
            ]
          },
          "aiSummary": {
            "description": "Optional. AI summary of the alert.",
            "type": "string"
          },
          "audit": {
            "description": "Output only. Audit data about the finding.",
            "readOnly": true,
            "allOf": [
              {
                "$ref": "#/components/schemas/Audit"
              }
            ]
          },
          "alert": {
            "description": "Optional. Name of the alert that this finding is bound to.",
            "type": "string"
          },
          "configurations": {
            "description": "Optional. Configuration names that are bound to this finding.",
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "provider",
          "displayName",
          "detail"
        ]
      },
      "FindingDetail": {
        "description": "Wrapper class that contains the union struct for all the various findings\ndetail specific classes.",
        "type": "object",
        "properties": {
          "initialAccessBroker": {
            "description": "Initial Access Broker finding detail type.",
            "allOf": [
              {
                "$ref": "#/components/schemas/InitialAccessBrokerFindingDetail"
              }
            ]
          },
          "dataLeak": {
            "description": "Data Leak finding detail type.",
            "allOf": [
              {
                "$ref": "#/components/schemas/DataLeakFindingDetail"
              }
            ]
          },
          "insiderThreat": {
            "description": "Insider Threat finding detail type.",
            "allOf": [
              {
                "$ref": "#/components/schemas/InsiderThreatFindingDetail"
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
      "InitialAccessBrokerFindingDetail": {
        "description": "A detail object for an Initial Access Broker (IAB) finding.",
        "type": "object",
        "properties": {
          "matchScore": {
            "description": "Required. Reference to the match score of the IAB finding. This is a float value\nbetween 0 and 1 calculated by the matching engine based on the similarity\nof the document and the user provided configurations.",
            "type": "number",
            "format": "float"
          },
          "severity": {
            "description": "Required. The severity of the IAB finding. This indicates the potential\nimpact of the threat.",
            "type": "string",
            "x-google-enum-descriptions": [
              "",
              "",
              "",
              "",
              ""
            ],
            "enum": [
              "SEVERITY_UNSPECIFIED",
              "LOW",
              "MEDIUM",
              "HIGH",
              "CRITICAL"
            ]
          },
          "documentId": {
            "description": "Required. The unique identifier of the document that triggered the IAB finding.\nThis ID can be used to retrieve the content of the document for further\nanalysis.",
            "type": "string"
          }
        },
        "required": [
          "matchScore",
          "severity",
          "documentId"
        ]
      },
      "DataLeakFindingDetail": {
        "description": "A detail object for a Data Leak finding.",
        "type": "object",
        "properties": {
          "matchScore": {
            "description": "Required. Reference to the match score of the Data Leak finding. This is a float\nvalue greater than 0 and less than or equal to 1 calculated by the matching\nengine based on the similarity of the document and the user provided\nconfigurations.",
            "type": "number",
            "format": "float"
          },
          "severity": {
            "description": "Required. The severity of the Data Leak finding. This indicates the potential\nimpact of the threat.",
            "type": "string",
            "x-google-enum-descriptions": [
              "Default value, should never be set.",
              "Low severity.",
              "Medium severity.",
              "High severity.",
              "Critical severity."
            ],
            "enum": [
              "SEVERITY_UNSPECIFIED",
              "LOW",
              "MEDIUM",
              "HIGH",
              "CRITICAL"
            ]
          },
          "documentId": {
            "description": "Required. The unique identifier of the document that triggered the Data Leak finding.\nThis ID can be used to retrieve the content of the document for further\nanalysis.",
            "type": "string"
          }
        },
        "required": [
          "matchScore",
          "severity",
          "documentId"
        ]
      },
      "InsiderThreatFindingDetail": {
        "description": "A detail object for a InsiderThreat finding.",
        "type": "object",
        "properties": {
          "matchScore": {
            "description": "Required. Reference to the match score of the InsiderThreat finding. This is a float\nvalue greater than 0 and less than or equal to 1 calculated by the matching\nengine based on the similarity of the document and the user provided\nconfigurations.",
            "type": "number",
            "format": "float"
          },
          "severity": {
            "description": "Required. The severity of the InsiderThreat finding. This indicates the potential\nimpact of the threat.",
            "type": "string",
            "x-google-enum-descriptions": [
              "Default value, should never be set.",
              "Low severity.",
              "Medium severity.",
              "High severity.",
              "Critical severity."
            ],
            "enum": [
              "SEVERITY_UNSPECIFIED",
              "LOW",
              "MEDIUM",
              "HIGH",
              "CRITICAL"
            ]
          },
          "documentId": {
            "description": "Required. The unique identifier of the document that triggered the InsiderThreat\nfinding. This ID can be used to retrieve the content of the document for\nfurther analysis.",
            "type": "string"
          }
        },
        "required": [
          "matchScore",
          "severity",
          "documentId"
        ]
      },
      "RelevanceAnalysis": {
        "description": "Structured relevance analysis for a threat.",
        "type": "object",
        "properties": {
          "relevant": {
            "description": "Indicates whether the threat is considered relevant.",
            "type": "boolean"
          },
          "confidence": {
            "description": "The level of confidence in the given verdict.",
            "allOf": [
              {
                "$ref": "#/components/schemas/ConfidenceLevel"
              }
            ]
          },
          "reasoning": {
            "description": "Human-readable explanation from the matcher, detailing why a particular\nresult is considered relevant or not relevant.",
            "type": "string"
          },
          "evidence": {
            "description": "Evidence supporting the verdict, including matched and unmatched items.",
            "allOf": [
              {
                "$ref": "#/components/schemas/Evidence"
              }
            ]
          },
          "relevanceLevel": {
            "description": "The level of relevance.",
            "allOf": [
              {
                "$ref": "#/components/schemas/RelevanceLevel"
              }
            ]
          }
        }
      },
      "Evidence": {
        "description": "Details the evidence used to determine the relevance verdict.",
        "type": "object",
        "properties": {
          "commonThemes": {
            "description": "A list of semantic themes or concepts found to be common, related, or\naligned between the sources, supporting the verdict.",
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "distinctThemes": {
            "description": "A list of semantic themes or descriptions unique to one source or\nsemantically distant.",
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        }
      },
      "SeverityAnalysis": {
        "description": "Structured severity analysis for a threat.",
        "type": "object",
        "properties": {
          "severityLevel": {
            "description": "The level of severity.",
            "allOf": [
              {
                "$ref": "#/components/schemas/SeverityLevel"
              }
            ]
          },
          "confidence": {
            "description": "The level of confidence in the given verdict.",
            "allOf": [
              {
                "$ref": "#/components/schemas/ConfidenceLevel"
              }
            ]
          },
          "reasoning": {
            "description": "Human-readable explanation from the model, detailing why a particular\nresult is considered to have a certain severity.",
            "type": "string"
          }
        }
      },
      "ConfidenceLevel": {
        "type": "string",
        "x-google-enum-descriptions": [
          "Default value. Confidence level is not specified.",
          "Low confidence in the verdict.",
          "Medium confidence in the verdict.",
          "High confidence in the verdict."
        ],
        "enum": [
          "CONFIDENCE_LEVEL_UNSPECIFIED",
          "CONFIDENCE_LEVEL_LOW",
          "CONFIDENCE_LEVEL_MEDIUM",
          "CONFIDENCE_LEVEL_HIGH"
        ]
      },
      "RelevanceLevel": {
        "type": "string",
        "x-google-enum-descriptions": [
          "Default value, should never be set.",
          "Low Relevance.",
          "Medium Relevance.",
          "High Relevance."
        ],
        "enum": [
          "RELEVANCE_LEVEL_UNSPECIFIED",
          "RELEVANCE_LEVEL_LOW",
          "RELEVANCE_LEVEL_MEDIUM",
          "RELEVANCE_LEVEL_HIGH"
        ]
      },
      "SeverityLevel": {
        "type": "string",
        "x-google-enum-descriptions": [
          "Default value, should never be set.",
          "Low Severity.",
          "Medium Severity.",
          "High Severity."
        ],
        "enum": [
          "SEVERITY_LEVEL_UNSPECIFIED",
          "SEVERITY_LEVEL_LOW",
          "SEVERITY_LEVEL_MEDIUM",
          "SEVERITY_LEVEL_HIGH"
        ]
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
    "/v1beta/projects/{project}/findings/{finding}": {
      "get": {
        "tags": [
          "threatintelligence"
        ],
        "operationId": "GetFinding",
        "description": "Get a finding by name.",
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
            "name": "finding",
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
                  "$ref": "#/components/schemas/Finding"
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

← [Overview](findings-overview.md) · [up](../README.md) · [List Findings](list-findings.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-finding>.*
