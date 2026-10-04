---
title: "Synchronously bulk update alerts"
source: https://gtidocs.virustotal.com/reference/post-alerts-bulk
slug: post-alerts-bulk
section: reference
group: "DTM (DIGITAL THREAT MONITORING)"
updatedAt: 2025-09-25T01:37:03.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [DTM (DIGITAL THREAT MONITORING)](../README.md) › [DTM Alerts](../dtm-alerts.md) › Synchronously bulk update alerts

---

# synchronously-bulk-update-alerts

Bulk apply updates to alerts. The only updatable fields are those available via the PATCH alert API. Updates occur synchronously.

# openapi-definition

```json
{
  "components": {
    "schemas": {
      "AlertBulk": {
        "description": "Request body for bulk alert operations.",
        "properties": {
          "patch": {
            "items": {
              "$ref": "#/components/schemas/AlertBulkOp"
            },
            "maxItems": 1000,
            "type": "array"
          }
        },
        "required": [
          "patch"
        ],
        "title": "Bulk Alert Request",
        "type": "object"
      },
      "AlertBulkOp": {
        "description": "An alert bulk operation to apply in a bulk request.",
        "properties": {
          "id": {
            "description": "The ID of the alert.",
            "type": "string"
          },
          "status": {
            "description": "The status to set for the alert.",
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
          },
          "tags": {
            "description": "The tags to set for the alert and will replace any existing tags on the alert.",
            "items": {
              "type": "string"
            },
            "maxItems": 100,
            "type": "array"
          }
        },
        "required": [
          "id"
        ],
        "title": "Bulk Alert Operation",
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
    "/alerts/bulk": {
      "post": {
        "description": "",
        "operationId": "post-alerts-bulk",
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
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "examples": {
                "alert-bulk-update-request": {
                  "value": {
                    "patch": [
                      {
                        "id": "c6pl4eo1148jji4ad7l0",
                        "status": "read"
                      },
                      {
                        "id": "c6pl4eo1148jji4ad7lg",
                        "status": "read"
                      },
                      {
                        "id": "c6pl4eo1148jji4ad7m0",
                        "status": "read",
                        "tags": [
                          "my-tag",
                          "another-tag"
                        ]
                      }
                    ]
                  }
                }
              },
              "schema": {
                "$ref": "#/components/schemas/AlertBulk"
              }
            }
          },
          "description": "A bulk request body includes the http method (only patch supported) with an array of bulk operations to apply. Each bulk operation is an object containing the id of the alert to apply the operation to and any properties/values to update as part of the bulk request."
        },
        "responses": {
          "200": {
            "description": "OK"
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
        "summary": "Synchronously bulk update alerts",
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

← [List child alerts for a given aggregated alert bucket](get-agg-child-alerts.md) · [up](../README.md) · [Asynchronously bulk update alerts using query params to target the alerts](post-alerts-bulk-apply.md) →

*Archived from <https://gtidocs.virustotal.com/reference/post-alerts-bulk>.*
