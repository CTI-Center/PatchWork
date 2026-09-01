---
title: "Asynchronously bulk update alerts using query params to target the alerts"
source: https://gtidocs.virustotal.com/reference/post-alerts-bulk-apply
slug: post-alerts-bulk-apply
section: reference
group: "DTM (DIGITAL THREAT MONITORING)"
updatedAt: 2025-09-25T01:37:04.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [DTM (DIGITAL THREAT MONITORING)](../README.md) › [DTM Alerts](../dtm-alerts.md) › Asynchronously bulk update alerts using query params to target the alerts

---

# asynchronously-bulk-update-alerts-using-query-params-to-target-the-alerts

Asynchronously update alerts using query params to taget which alerts will be updated.

# openapi-definition

```json
{
  "components": {
    "schemas": {
      "AlertBulkApplyOp": {
        "description": "The changes to apply to alerts meeting the query criteria.",
        "properties": {
          "add_tags": {
            "description": "Tags to add on any alerts updated. Duplicate tags will not be created on any alert.",
            "items": {
              "type": "string"
            },
            "type": "array"
          },
          "exlcude_ids": {
            "description": "If provided, an array of alert IDs that should be explictly skipped during the update operation.",
            "items": {
              "type": "string"
            },
            "type": "array"
          },
          "remove_tags": {
            "description": "Tags to remove on any alerts updated.",
            "items": {
              "type": "string"
            },
            "type": "array"
          },
          "status": {
            "description": "The status to apply to the alerts.",
            "enum": [
              "new",
              "read",
              "escalated",
              "in_progress",
              "closed",
              "no_action_required",
              "duplicate",
              "not_relevant",
              "tracked_external"
            ],
            "type": "string"
          }
        },
        "title": "Bulk Alert Apply Operation",
        "type": "object"
      },
      "Response-message": {
        "description": "Error response message.",
        "properties": {
          "message": {
            "description": "The response message.",
            "type": "string"
          }
        },
        "title": "Error Response",
        "type": "object"
      }
    }
  },
  "info": {
    "contact": {},
    "description": "The Digital Threat Monitoring (DTM) API provides programatic access to Mandiant's DTM capabilities.",
    "title": "DTM (DIGITAL THREAT MONITORING)",
    "version": "1.0"
  },
  "openapi": "3.1.0",
  "paths": {
    "/alerts/bulk/apply": {
      "post": {
        "description": "",
        "operationId": "post-alerts-bulk-apply",
        "parameters": [
          {
            "description": "Your API key",
            "in": "header",
            "name": "x-apikey",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "The content type of the body.",
            "in": "header",
            "name": "Content-Type",
            "required": true,
            "schema": {
              "enum": [
                "application/json"
              ],
              "type": "string"
            }
          },
          {
            "description": "If true, then alert buckets are updated where applicable.",
            "in": "query",
            "name": "buckets",
            "schema": {
              "default": false,
              "type": "boolean"
            }
          },
          {
            "description": "Only return alerts for the given monitor ID. This parameter can be specified multiple times to filter on more than one monitor ID.",
            "in": "query",
            "name": "monitor_id",
            "schema": {
              "example": "c4fcpm2bqsiatib6i4h0",
              "type": "string"
            }
          },
          {
            "description": "If true, then only alerts that have analysis are returned. An alert has anlysis if it has either analysis text or analysis file attachments.",
            "in": "query",
            "name": "has_analysis",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "description": "When listing alerts by date range, since defines the starting date in RFC3339 format",
            "in": "query",
            "name": "since",
            "schema": {
              "format": "date-time",
              "type": "string"
            }
          },
          {
            "description": "When listing alerts by date range, until defines the ending date in RFC3339 format",
            "in": "query",
            "name": "until",
            "schema": {
              "format": "date-time",
              "type": "string"
            }
          },
          {
            "description": "Filter alerts by their status. This parameter can be specified multiple times.",
            "in": "query",
            "name": "status",
            "schema": {
              "enum": [
                "new",
                "read",
                "escalated",
                "in_progress",
                "closed",
                "no_action_required",
                "duplicate",
                "not_relevant",
                "tracked_external"
              ],
              "type": "string"
            }
          },
          {
            "description": "Filter alerts by alert type. This parameter can be specified multiple times.",
            "in": "query",
            "name": "alert_type",
            "schema": {
              "enum": [
                "Compromised Credentials",
                "Domain Discovery",
                "Forum Post",
                "Message",
                "Paste",
                "Shop Listing",
                "Tweet",
                "Web Content"
              ],
              "type": "string"
            }
          },
          {
            "description": "Search alert and triggering doc contents based on a simple Lucene query string including 1 or more text values separated by AND or OR.",
            "in": "query",
            "name": "search",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "If specified, then only alerts that have the given match value are returned. This parameter can be repeated multiple times.",
            "in": "query",
            "name": "match_value",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Filter alerts by tag(s). This parameter can be used more than once to filter on multiple tags.",
            "in": "query",
            "name": "tags",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "When using the search parameter, its value can be base64 encoded in which case search_encoding indicates the value encoding type.",
            "in": "query",
            "name": "search_encoding",
            "schema": {
              "enum": [
                "base64"
              ],
              "type": "string"
            }
          },
          {
            "description": "Return alerts that have the given severity. This parameter can be repeated multiple times.",
            "in": "query",
            "name": "severity",
            "schema": {
              "enum": [
                "high",
                "medium",
                "low"
              ],
              "type": "string"
            }
          },
          {
            "description": "Filter alerts with mscores greater than or equal to the given value.",
            "in": "query",
            "name": "mscore_gte",
            "schema": {
              "maximum": 100,
              "minimum": 0,
              "type": "integer"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "examples": {
                "alert-bulk-apply-update-request": {
                  "value": {
                    "add_tags": [
                      "add_tag_1",
                      "add_tag_2"
                    ],
                    "exlcude_ids": [
                      "alert_id_to_skip"
                    ],
                    "remove_tags": [
                      "remove_tag_1",
                      "remove_tag_2"
                    ],
                    "status": "read"
                  }
                }
              },
              "schema": {
                "$ref": "#/components/schemas/AlertBulkApplyOp"
              }
            }
          },
          "description": "Asynchronously update alerts based on query parameters."
        },
        "responses": {
          "202": {
            "description": "Accepted and will be processed in the background."
          },
          "400": {
            "content": {
              "application/json": {
                "examples": {
                  "bad-request": {
                    "value": {
                      "message": "on or more IDs are invalid"
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Response-message"
                }
              }
            },
            "description": "Bad Request",
            "headers": {
              "Content-Type": {
                "description": "Response body content type",
                "schema": {
                  "type": "string"
                }
              }
            }
          },
          "401": {
            "content": {
              "application/json": {
                "examples": {
                  "unauthorized": {
                    "value": {
                      "message": "unauthorized"
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Response-message"
                }
              }
            },
            "description": "Unauthorized",
            "headers": {
              "Content-Type": {
                "description": "Response body content type",
                "schema": {
                  "type": "string"
                }
              }
            }
          },
          "403": {
            "content": {
              "application/json": {
                "examples": {
                  "forbidden": {
                    "value": {
                      "message": "forbidden"
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Response-message"
                }
              }
            },
            "description": "Forbidden",
            "headers": {
              "Content-Type": {
                "description": "Response body content type",
                "schema": {
                  "type": "string"
                }
              }
            }
          },
          "500": {
            "content": {
              "application/json": {
                "examples": {
                  "internal-server-error": {
                    "value": {
                      "message": "internal server error"
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Response-message"
                }
              }
            },
            "description": "Internal Server Error",
            "headers": {
              "Content-Type": {
                "description": "Response body content type",
                "schema": {
                  "type": "string"
                }
              }
            }
          }
        },
        "summary": "Asynchronously bulk update alerts using query params to target the alerts",
        "tags": [
          "DTM Alerts"
        ]
      }
    }
  },
  "security": [
    {}
  ],
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3/dtm"
    }
  ],
  "tags": [
    {
      "name": "DTM Alerts"
    }
  ],
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": false,
    "samples-enabled": true
  }
}
```

---

← [Synchronously bulk update alerts](post-alerts-bulk.md) · [up](../README.md) · [Alert Analysis](../alert-analysis.md) →

*Archived from <https://gtidocs.virustotal.com/reference/post-alerts-bulk-apply>.*
