---
title: "Mark as Duplicate"
source: https://gtidocs.virustotal.com/reference/markalertasduplicate
slug: markalertasduplicate
section: reference
group: "GTI Alerts"
updatedAt: 2026-03-06T12:09:47.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../../README.md) › [API Reference](../../../README.md) › [GTI Alerts](../../README.md) › [Alerts](../../alerts.md) › [Triage Alerts](../triage-alerts.md) › Mark as Duplicate

---

# mark-as-duplicate

Marks an alert as a duplicate of another alert. - DUPLICATE.

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
      "Alert": {
        "description": "Stateful object representing a group of Findings. Key feature to an Alert\nis that it expresses the user's intent towards the findings of that group,\neven those that haven't occurred yet.",
        "type": "object",
        "properties": {
          "name": {
            "description": "Identifier. Server generated name for the alert.\nformat is projects/{project}/alerts/{alert}",
            "x-google-identifier": true,
            "type": "string"
          },
          "findings": {
            "description": "Output only. Findings that are covered by this alert.",
            "readOnly": true,
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "state": {
            "description": "Output only. State of the alert.",
            "readOnly": true,
            "type": "string",
            "x-google-enum-descriptions": [
              "Default value, should never be set.",
              "alert is new.",
              "alert was read by a human.",
              "alert has been triaged.",
              "alert has been escalated.",
              "alert has been resolved.",
              "alert is a duplicate of another alert.",
              "alert is a false positive and should be ignored.",
              "alert is not actionable.",
              "alert is benign.",
              "alert is tracked externally."
            ],
            "enum": [
              "STATE_UNSPECIFIED",
              "NEW",
              "READ",
              "TRIAGED",
              "ESCALATED",
              "RESOLVED",
              "DUPLICATE",
              "FALSE_POSITIVE",
              "NOT_ACTIONABLE",
              "BENIGN",
              "TRACKED_EXTERNALLY"
            ]
          },
          "audit": {
            "description": "Output only. Audit information for the alert.",
            "readOnly": true,
            "allOf": [
              {
                "$ref": "#/components/schemas/Audit"
              }
            ]
          },
          "displayName": {
            "description": "Output only. A short title for the alert.",
            "readOnly": true,
            "type": "string"
          },
          "detail": {
            "description": "Output only. Details object for the alert, not all alerts will have a details object.",
            "readOnly": true,
            "allOf": [
              {
                "$ref": "#/components/schemas/AlertDetail"
              }
            ]
          },
          "duplicateOf": {
            "description": "Output only. alert name of the alert this alert is a duplicate of.\nFormat: projects/{project}/alerts/{alert}",
            "readOnly": true,
            "type": "string"
          },
          "duplicatedBy": {
            "description": "Output only. alert names of the alerts that are duplicates of this alert.\nFormat: projects/{project}/alerts/{alert}",
            "readOnly": true,
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "etag": {
            "description": "Optional. If included when updating an alert, this should be set to the current etag\nof the alert. If the etags do not match, the update will be rejected and\nan ABORTED error will be returned.",
            "type": "string"
          },
          "externalId": {
            "description": "Output only. External ID for the alert. This is used internally to provide protection\nagainst out of order updates.",
            "readOnly": true,
            "type": "string"
          },
          "aiSummary": {
            "description": "Optional. AI summary of the alert.",
            "type": "string"
          },
          "relevanceAnalysis": {
            "description": "Output only. High-Precision Relevance Analysis verdict for the alert.",
            "readOnly": true,
            "allOf": [
              {
                "$ref": "#/components/schemas/RelevanceAnalysis"
              }
            ]
          },
          "severityAnalysis": {
            "description": "Output only. High-Precision Severity Analysis for the alert.",
            "readOnly": true,
            "allOf": [
              {
                "$ref": "#/components/schemas/SeverityAnalysis"
              }
            ]
          },
          "priorityAnalysis": {
            "description": "Output only. High-Precision Priority Analysis for the alert.",
            "readOnly": true,
            "allOf": [
              {
                "$ref": "#/components/schemas/PriorityAnalysis"
              }
            ]
          },
          "findingCount": {
            "description": "Output only. The number of findings associated with this alert.",
            "readOnly": true,
            "type": "string",
            "format": "int64"
          },
          "configurations": {
            "description": "Output only. The resource names of the Configurations bound to this alert.\nFormat: projects/{project}/configurations/{configuration}",
            "readOnly": true,
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        }
      },
      "AlertDetail": {
        "description": "Container for different types of alert details.",
        "type": "object",
        "properties": {
          "initialAccessBroker": {
            "description": "Initial Access Broker alert detail type.",
            "allOf": [
              {
                "$ref": "#/components/schemas/InitialAccessBrokerAlertDetail"
              }
            ]
          },
          "dataLeak": {
            "description": "Data Leak alert detail type.",
            "allOf": [
              {
                "$ref": "#/components/schemas/DataLeakAlertDetail"
              }
            ]
          },
          "insiderThreat": {
            "description": "Insider Threat alert detail type.",
            "allOf": [
              {
                "$ref": "#/components/schemas/InsiderThreatAlertDetail"
              }
            ]
          },
          "targetTechnology": {
            "description": "Technology Watchlist alert detail type.",
            "allOf": [
              {
                "$ref": "#/components/schemas/TargetTechnologyAlertDetail"
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
      "InitialAccessBrokerAlertDetail": {
        "description": "Captures the specific details of InitialAccessBroker (IAB) alert.",
        "type": "object",
        "properties": {
          "severity": {
            "description": "Required. The severity of the Initial Access Broker (IAB) alert.",
            "type": "string",
            "enum": [
              "LOW",
              "MEDIUM",
              "HIGH",
              "CRITICAL"
            ]
          },
          "discoveryDocumentIds": {
            "description": "Required. Array of ids to accommodate multiple discovery documents",
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "severity",
          "discoveryDocumentIds"
        ]
      },
      "DataLeakAlertDetail": {
        "description": "Captures the specific details of Data Leak alert.",
        "type": "object",
        "properties": {
          "severity": {
            "description": "Required. The severity of the Data Leak alert.",
            "type": "string",
            "enum": [
              "LOW",
              "MEDIUM",
              "HIGH",
              "CRITICAL"
            ]
          },
          "discoveryDocumentIds": {
            "description": "Required. Array of ids to accommodate multiple discovery documents",
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "severity",
          "discoveryDocumentIds"
        ]
      },
      "InsiderThreatAlertDetail": {
        "description": "Captures the specific details of InsiderThreat alert.",
        "type": "object",
        "properties": {
          "severity": {
            "description": "Required. The severity of the Insider Threat alert.",
            "type": "string",
            "enum": [
              "LOW",
              "MEDIUM",
              "HIGH",
              "CRITICAL"
            ]
          },
          "discoveryDocumentIds": {
            "description": "Required. Array of ids to accommodate multiple discovery documents",
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "severity",
          "discoveryDocumentIds"
        ]
      },
      "TargetTechnologyAlertDetail": {
        "description": "Contains details for a technology watchlist alert.",
        "type": "object",
        "properties": {
          "vulnerabilityMatch": {
            "description": "Optional. The vulnerability match details.",
            "allOf": [
              {
                "$ref": "#/components/schemas/VulnerabilityMatch"
              }
            ]
          }
        }
      },
      "PriorityAnalysis": {
        "description": "Structured priority analysis for a threat.",
        "type": "object",
        "properties": {
          "priorityLevel": {
            "description": "The level of Priority.",
            "allOf": [
              {
                "$ref": "#/components/schemas/PriorityLevel"
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
            "description": "Human-readable explanation from the model, detailing why a particular\nresult is considered to have a certain priority.",
            "type": "string"
          }
        }
      },
      "MarkAlertAsDuplicateRequest": {
        "description": "Request message for MarkAlertAsDuplicate.",
        "type": "object",
        "properties": {
          "duplicateOf": {
            "description": "Optional. Name of the alert to mark as a duplicate of.\nFormat: projects/{project}/alerts/{alert}",
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
      },
      "PriorityLevel": {
        "type": "string",
        "x-google-enum-descriptions": [
          "Default value, should never be set.",
          "Low Priority.",
          "Medium Priority.",
          "High Priority.",
          "Critical Priority."
        ],
        "enum": [
          "PRIORITY_LEVEL_UNSPECIFIED",
          "PRIORITY_LEVEL_LOW",
          "PRIORITY_LEVEL_MEDIUM",
          "PRIORITY_LEVEL_HIGH",
          "PRIORITY_LEVEL_CRITICAL"
        ]
      },
      "ExploitationState": {
        "type": "string",
        "x-google-enum-descriptions": [
          "Unspecified exploitation state.",
          "No known exploitation.",
          "Exploitation has been reported.",
          "Exploitation is suspected.",
          "Exploitation is confirmed.",
          "Widespread exploitation."
        ],
        "enum": [
          "EXPLOITATION_STATE_UNSPECIFIED",
          "EXPLOITATION_STATE_NO_KNOWN",
          "EXPLOITATION_STATE_REPORTED",
          "EXPLOITATION_STATE_SUSPECTED",
          "EXPLOITATION_STATE_CONFIRMED",
          "EXPLOITATION_STATE_WIDESPREAD"
        ]
      },
      "Priority": {
        "type": "string",
        "x-google-enum-descriptions": [
          "Unspecified priority.",
          "Priority level 0.",
          "Priority level 1.",
          "Priority level 2.",
          "Priority level 3.",
          "Priority level 4."
        ],
        "enum": [
          "PRIORITY_UNSPECIFIED",
          "P0",
          "P1",
          "P2",
          "P3",
          "P4"
        ]
      },
      "RiskRating": {
        "type": "string",
        "x-google-enum-descriptions": [
          "Unspecified risk rating. This is the default value when the risk rating is not set.",
          "Low risk rating.",
          "Medium risk rating.",
          "High risk rating.",
          "Critical risk rating.",
          "The vulnerability has been assessed, but a specific risk rating could not be determined or assigned."
        ],
        "enum": [
          "RISK_RATING_UNSPECIFIED",
          "LOW",
          "MEDIUM",
          "HIGH",
          "CRITICAL",
          "UNRATED"
        ]
      },
      "VulnerabilityMatch": {
        "description": "Contains details about a vulnerability match.",
        "type": "object",
        "properties": {
          "cveId": {
            "description": "Required. The CVE ID of the vulnerability. Ex: \"CVE-2025-9876\". See https://www.cve.org/ for more information.",
            "type": "string"
          },
          "collectionId": {
            "description": "Required. The collection ID of the vulnerability. Ex: \"vulnerability--cve-2025-9876\".",
            "type": "string"
          },
          "description": {
            "description": "Required. A description of the vulnerability.",
            "type": "string"
          },
          "technologies": {
            "description": "Required. All technologies affected by the vulnerability. Ex: \"Apache Struts\".",
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "cvss3Score": {
            "description": "Required. The CVSS score of the vulnerability. Evaluates to CVSS v3 when available with a fallback to v2 and v4. Example: 6.4.",
            "type": "number",
            "format": "float"
          },
          "riskRating": {
            "description": "Required. The risk rating of the vulnerability.",
            "allOf": [
              {
                "$ref": "#/components/schemas/RiskRating"
              }
            ]
          },
          "exploitationState": {
            "description": "Required. The exploitation state of the vulnerability.",
            "allOf": [
              {
                "$ref": "#/components/schemas/ExploitationState"
              }
            ]
          },
          "associations": {
            "description": "Optional. Associated threat actors, malware, etc. This is embedded as a snapshot because the details of the association at the time of the vulnerability match are important for context and reporting.",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/VulnerabilityMatchAssociation"
            }
          },
          "epssScore": {
            "description": "Optional. The EPSS score, representing the probability of exploitation. Example: 0.87.",
            "type": "number",
            "format": "float"
          },
          "publicExploits": {
            "description": "Optional. List of public exploits.",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/VulnerabilityMatchPublicExploit"
            }
          },
          "productFixes": {
            "description": "Optional. List of product fixes for the vulnerability.",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/VulnerabilityMatchProductFix"
            }
          },
          "exploitationConsequences": {
            "description": "Optional. List of exploitation consequences for the vulnerability.",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/VulnerabilityMatchExploitationConsequence"
            }
          },
          "exploitationVectors": {
            "description": "Optional. List of exploitation vectors for the vulnerability.",
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/VulnerabilityMatchExploitationVector"
            }
          },
          "disclosureTime": {
            "description": "Optional. The disclosure time of the vulnerability.",
            "type": "string",
            "format": "date-time"
          },
          "priority": {
            "description": "Optional. The priority level of the vulnerability data. Ex: \"P1\".",
            "allOf": [
              {
                "$ref": "#/components/schemas/Priority"
              }
            ]
          },
          "matchedTechnologies": {
            "description": "Optional. The specific technologies from the configured watchlist that triggered the match. Ex: \"Apache Struts\".",
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "publiclyAvailableExploit": {
            "description": "Output only. Whether a publicly available exploit exists.",
            "readOnly": true,
            "type": "boolean"
          }
        },
        "required": [
          "cveId",
          "collectionId",
          "description",
          "technologies",
          "cvss3Score",
          "riskRating",
          "exploitationState"
        ]
      },
      "VulnerabilityMatchAssociation": {
        "description": "Represents an association with a vulnerability.",
        "type": "object",
        "properties": {
          "id": {
            "description": "Required. The ID of the association.",
            "type": "string"
          },
          "type": {
            "description": "Required. The type of the association.",
            "allOf": [
              {
                "$ref": "#/components/schemas/VulnerabilityMatchThreatIntelObjectType"
              }
            ]
          }
        },
        "required": [
          "id",
          "type"
        ]
      },
      "VulnerabilityMatchThreatIntelObjectType": {
        "description": "The type of threat intel object.",
        "type": "string",
        "x-google-enum-descriptions": [
          "Unspecified object type.",
          "Threat actor object type.",
          "Malware object type.",
          "Report object type.",
          "Campaign object type.",
          "IoC Collection object type.",
          "Software and toolkits object type.",
          "Vulnerability object type."
        ],
        "enum": [
          "THREAT_INTEL_OBJECT_TYPE_UNSPECIFIED",
          "THREAT_INTEL_OBJECT_TYPE_THREAT_ACTOR",
          "THREAT_INTEL_OBJECT_TYPE_MALWARE",
          "THREAT_INTEL_OBJECT_TYPE_REPORT",
          "THREAT_INTEL_OBJECT_TYPE_CAMPAIGN",
          "THREAT_INTEL_OBJECT_TYPE_IOC_COLLECTION",
          "THREAT_INTEL_OBJECT_TYPE_SOFTWARE_AND_TOOLKITS",
          "THREAT_INTEL_OBJECT_TYPE_VULNERABILITY"
        ]
      },
      "VulnerabilityMatchPublicExploit": {
        "description": "Contains details about a public exploit.",
        "type": "object",
        "properties": {
          "exploitName": {
            "description": "Required. The name of the exploit. Ex: \"Magentounauth.php.txt\".",
            "type": "string"
          },
          "uri": {
            "description": "Optional. The URI of the exploit.",
            "type": "string"
          },
          "exploitReliability": {
            "description": "Optional. The reliability of the exploit. Ex: \"Unreviewed\".",
            "allOf": [
              {
                "$ref": "#/components/schemas/VulnerabilityMatchExploitReliability"
              }
            ]
          },
          "exploitGrade": {
            "description": "Optional. The grade of the exploit. Ex: \"non-weaponized\".",
            "allOf": [
              {
                "$ref": "#/components/schemas/VulnerabilityMatchExploitGrade"
              }
            ]
          },
          "sizeBytes": {
            "description": "Optional. The size of the exploit.",
            "type": "string",
            "format": "int64"
          },
          "releaseTime": {
            "description": "Optional. The release time of the exploit.",
            "type": "string",
            "format": "date-time"
          }
        },
        "required": [
          "exploitName"
        ]
      },
      "VulnerabilityMatchExploitReliability": {
        "description": "Represents exploit reliability.",
        "type": "string",
        "x-google-enum-descriptions": [
          "Unspecified exploit reliability.",
          "Confirmed exploit reliability.",
          "Uncorroborated exploit reliability.",
          "Unconfirmed exploit reliability."
        ],
        "enum": [
          "EXPLOIT_RELIABILITY_UNSPECIFIED",
          "UNREVIEWED",
          "REVIEWED",
          "TESTED"
        ]
      },
      "VulnerabilityMatchExploitGrade": {
        "description": "Represents exploit grade.",
        "type": "string",
        "x-google-enum-descriptions": [
          "Unspecified exploit grade.",
          "Unevaluated exploit grade.",
          "Proof-of-concept exploit grade.",
          "Non-weaponized exploit grade.",
          "Weaponized exploit grade.",
          "Scanner exploit grade.",
          "Fake exploit grade."
        ],
        "enum": [
          "EXPLOIT_GRADE_UNSPECIFIED",
          "UNEVALUATED",
          "PROOF_OF_CONCEPT",
          "NON_WEAPONIZED",
          "WEAPONIZED",
          "SCANNER",
          "FAKE"
        ]
      },
      "VulnerabilityMatchProductFix": {
        "description": "Contains details about a product fix.",
        "type": "object",
        "properties": {
          "displayName": {
            "description": "Required. The name of the fix. Ex: \"Magento\".",
            "type": "string"
          },
          "uri": {
            "description": "Optional. The URI of the fix.",
            "type": "string"
          },
          "sourceId": {
            "description": "Required. The source ID of the fix. Ex: \"APPSEC-1420\".",
            "type": "string"
          },
          "publishTime": {
            "description": "Optional. The published time of the fix.",
            "type": "string",
            "format": "date-time"
          }
        },
        "required": [
          "displayName",
          "sourceId"
        ]
      },
      "VulnerabilityMatchExploitationConsequence": {
        "description": "Represents the consequence of exploitation.",
        "type": "string",
        "x-google-enum-descriptions": [
          "Unspecified exploitation consequence.",
          "Code execution consequence.",
          "Command execution consequence.",
          "Data loss consequence.",
          "Data manipulation consequence.",
          "Denial-of-Service consequence.",
          "Information disclosure consequence.",
          "Unauthorized access consequence.",
          "Privilege escalation consequence.",
          "Sandbox escape consequence.",
          "Security bypass consequence.",
          "Container escape consequence.",
          "Spoofing consequence."
        ],
        "enum": [
          "EXPLOITATION_CONSEQUENCE_UNSPECIFIED",
          "CODE_EXECUTION",
          "COMMAND_EXECUTION",
          "DATA_LOSS",
          "DATA_MANIPULATION",
          "DENIAL_OF_SERVICE",
          "INFORMATION_DISCLOSURE",
          "UNAUTHORIZED_ACCESS",
          "PRIVILEGE_ESCALATION",
          "SANDBOX_ESCAPE",
          "SECURITY_BYPASS",
          "CONTAINER_ESCAPE",
          "SPOOFING"
        ]
      },
      "VulnerabilityMatchExploitationVector": {
        "description": "Represents the vector of exploitation.",
        "type": "string",
        "x-google-enum-descriptions": [
          "Unspecified exploitation vector.",
          "Administrative interface vector.",
          "Bluetooth access vector.",
          "Browser vector.",
          "Compromised communication channel vector.",
          "Email vector.",
          "Exposed web application vector.",
          "Local network access vector.",
          "Malicious application vector.",
          "Malicious file vector.",
          "Malicious server vector.",
          "Open port vector.",
          "Physical access vector.",
          "Short range radio vector.",
          "Unspecified local vector.",
          "Unspecified remote vector.",
          "VPN access vector.",
          "WiFi access vector."
        ],
        "enum": [
          "EXPLOITATION_VECTOR_UNSPECIFIED",
          "ADMINISTRATIVE_INTERFACE",
          "BLUETOOTH_ACCESS",
          "BROWSER",
          "COMPROMISED_COMMUNICATION_CHANNEL",
          "EMAIL",
          "EXPOSED_WEB_APPLICATION",
          "LOCAL_NETWORK_ACCESS",
          "MALICIOUS_APPLICATION",
          "MALICIOUS_FILE",
          "MALICIOUS_SERVER",
          "OPEN_PORT",
          "PHYSICAL_ACCESS",
          "SHORT_RANGE_RADIO",
          "UNSPECIFIED_LOCAL_VECTOR",
          "UNSPECIFIED_REMOTE_VECTOR",
          "VPN_ACCESS",
          "WIFI_ACCESS"
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
    "/v1beta/projects/{project}/alerts/{alert}:duplicate": {
      "post": {
        "tags": [
          "threatintelligence"
        ],
        "operationId": "MarkAlertAsDuplicate",
        "description": "Marks an alert as a duplicate of another alert. - DUPLICATE.",
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
          "description": "The request body.",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/MarkAlertAsDuplicateRequest"
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
                  "$ref": "#/components/schemas/Alert"
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

← [Mark as Benign](markalertasbenign.md) · [up](../../README.md) · [Mark as Escalated](markalertasescalated.md) →

*Archived from <https://gtidocs.virustotal.com/reference/markalertasduplicate>.*
