---
title: "List audit records for a given alert"
source: https://gtidocs.virustotal.com/reference/get-alert-audit
slug: get-alert-audit
section: reference
group: "DTM (DIGITAL THREAT MONITORING)"
updatedAt: 2025-09-25T02:06:49.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [DTM (DIGITAL THREAT MONITORING)](../README.md) › [Alert Audit](../alert-audit.md) › List audit records for a given alert

---

# list-audit-records-for-a-given-alert

Get alert audit records for a given alert. This API uses the next link header to provide the URI of the next page of results. When fetching subsequent pages, only use the link header URI.

# openapi-definition

```json
{
  "components": {
    "schemas": {
      "AlertAuditRecord": {
        "description": "Metadata regarding an operation performed on an alert.",
        "properties": {
          "alert_id": {
            "description": "The ID of the alert that was operated on.",
            "readOnly": true,
            "type": "string"
          },
          "history_created_at": {
            "description": "The time the operation was performed.",
            "format": "date-time",
            "readOnly": true,
            "type": "string"
          },
          "id": {
            "description": "The ID of the audit record.",
            "readOnly": true,
            "type": "string"
          },
          "monitor_id": {
            "description": "The ID of the monitor that created the alert.",
            "readOnly": true,
            "type": "string"
          },
          "operation": {
            "description": "The operation performed on the alert.",
            "enum": [
              "read",
              "update",
              "rollback",
              "delete",
              "update_analysis",
              "delete_analysis",
              "create_attachment",
              "delete_attachment",
              "add_tags",
              "remove_tags",
              "download"
            ],
            "readOnly": true,
            "type": "string"
          },
          "previous_status": {
            "description": "The status of the alert prior to the operation.",
            "readOnly": true,
            "type": "string"
          },
          "to_status": {
            "description": "The status of the alert after the operation.",
            "readOnly": true,
            "type": "string"
          },
          "user_email": {
            "description": "The username that performed the operation.",
            "readOnly": true,
            "type": "string"
          },
          "user_id": {
            "description": "The ID of the user that performed the operation.",
            "readOnly": true,
            "type": "string"
          }
        },
        "title": "Alert Audit Record",
        "type": "object"
      },
      "AlertAuditRecords": {
        "description": "List of alert audit records.",
        "properties": {
          "history": {
            "description": "The list of alert audit records.",
            "items": {
              "$ref": "#/components/schemas/AlertAuditRecord"
            },
            "type": "array"
          }
        },
        "title": "Alert Audit Records",
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
    "/alerts/{id}/audit": {
      "get": {
        "description": "",
        "operationId": "get-alert-audit",
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
            "description": "The ID for the alert to get the audit records for.",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "example": "c4huif0mhcmiku5g7jsg",
              "type": "string"
            }
          },
          {
            "description": "The alert operation field name to sort the response by.",
            "in": "query",
            "name": "sort",
            "schema": {
              "default": "alert_id",
              "enum": [
                "alert_id",
                "history_created_at",
                "operation"
              ],
              "type": "string"
            }
          },
          {
            "description": "The order used to sort the response alerts field by.",
            "in": "query",
            "name": "order",
            "schema": {
              "default": "desc",
              "enum": [
                "asc",
                "desc"
              ],
              "example": "asc",
              "type": "string"
            }
          },
          {
            "description": "The number of alerts to return in each page. Max value of 100.",
            "in": "query",
            "name": "size",
            "schema": {
              "default": 10,
              "example": 20,
              "type": "integer",
              "maximum": 100,
              "minimum": 0
            }
          },
          {
            "description": "When listing by date range, since defines the starting date in RFC3339 format",
            "in": "query",
            "name": "since",
            "schema": {
              "format": "date-time",
              "type": "string"
            }
          },
          {
            "description": "When listing by date range, until defines the ending date in RFC3339 format",
            "in": "query",
            "name": "until",
            "schema": {
              "format": "date-time",
              "type": "string"
            }
          },
          {
            "description": "Only used when fetching subsequent pages during pagination and will contain a unique page ID. No other query parameters can be used with page",
            "in": "query",
            "name": "page",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Filter by operation. This parameter can be specified multiple times.",
            "in": "query",
            "name": "operation",
            "schema": {
              "enum": [
                "read",
                "update",
                "rollback",
                "delete",
                "update_analysis",
                "delete_analysis",
                "create_attachment",
                "delete_attachment",
                "add_tags",
                "remove_tags",
                "download"
              ],
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "examples": {
                  "list-alerts": {
                    "value": {
                      "history": [
                        {
                          "alert_id": "cmuh3gc77f5qjuh393s0",
                          "history_created_at": "2024-02-02T16:01:14.868Z",
                          "id": "cmuh3im6ilcc4m24o070",
                          "monitor_id": "cmkjgpondpooldkse410",
                          "operation": "read",
                          "previous_status": "read",
                          "tenant_id": "5541ab0d-f16a-4354-b025-1239048935",
                          "to_status": "read",
                          "user_email": "John Doe",
                          "user_id": "1239048935-6ca8-103c-9ee0-4bc16e027a2d"
                        },
                        {
                          "alert_id": "cmuh3gc77f5qjuh393s0",
                          "history_created_at": "2024-02-02T16:01:11.74Z",
                          "id": "cmuh3hu6ilcc4m24o060",
                          "monitor_id": "cmkjgpondpooldkse410",
                          "operation": "update",
                          "previous_status": "new",
                          "tenant_id": "5541ab0d-f16a-4354-b025-1239048935",
                          "to_status": "read",
                          "user_email": "Jane Smith",
                          "user_id": "1239048935-6ca8-103c-9ee0-4bc16e027a2d"
                        }
                      ]
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/AlertAuditRecords"
                }
              }
            },
            "description": "OK",
            "headers": {
              "Content-Type": {
                "description": "The content type of the response body.",
                "schema": {
                  "default": "application/json",
                  "example": "application/json",
                  "type": "string"
                }
              },
              "Link": {
                "description": "If another page of results is available for pagination, the Link header will contain the URI used to fetch the next page.",
                "schema": {
                  "example": "<https://api.intelligence.mandiant.com/v4/dtm/alerts/cmuh3gc77f5qjuh393s0/audit?page=c52e5bc1hrv40t8d0gvg>; rel=\"next\"",
                  "type": "string"
                }
              }
            }
          },
          "400": {
            "content": {
              "application/json": {
                "examples": {
                  "bad-request": {
                    "value": {
                      "message": "Bad Request"
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Response-message"
                }
              }
            },
            "description": "Bad Request"
          },
          "401": {
            "content": {
              "application/json": {
                "examples": {
                  "unauthorized": {
                    "value": {
                      "message": "Unauthorized"
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Response-message"
                }
              }
            },
            "description": "Unauthorized"
          },
          "500": {
            "content": {
              "application/json": {
                "examples": {
                  "internal-error": {
                    "value": {
                      "message": "Internal Error"
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Response-message"
                }
              }
            },
            "description": "Internal Server Error"
          }
        },
        "summary": "List audit records for a given alert",
        "tags": [
          "Alert Audit"
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
      "name": "Alert Audit"
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

← [Alert Audit](../alert-audit.md) · [up](../README.md) · [List alert audit records](get-all-alert-audit.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-alert-audit>.*
