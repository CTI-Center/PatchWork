---
title: "Asynchronously backfill alerts for the monitor"
source: https://gtidocs.virustotal.com/reference/post-monitor-backfill
slug: post-monitor-backfill
section: reference
group: "DTM (DIGITAL THREAT MONITORING)"
updatedAt: 2025-09-25T02:06:54.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [DTM (DIGITAL THREAT MONITORING)](../README.md) › [Monitors](../monitors.md) › Asynchronously backfill alerts for the monitor

---

# asynchronously-backfill-alerts-for-the-monitor

Begin a new alert backfill for the current monitor using the time range specified. This API is only supported for monitors created from the Compromised Credential monitor template and will create at most 10,000 alerts.

# openapi-definition

```json
{
  "components": {
    "schemas": {
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
    "/monitors/{id}/backfill": {
      "post": {
        "description": "",
        "operationId": "post-monitor-backfill",
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
            "description": "application/json",
            "in": "header",
            "name": "Content-Type",
            "required": true,
            "schema": {
              "example": "application/json",
              "type": "string"
            }
          },
          {
            "description": "The ID of the monitor to begin a backfill for.",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "example": "c4huif0mhcmiku5g7jsg",
              "type": "string"
            }
          },
          {
            "description": "Backfill alerts starting from this date in RFC3339 format",
            "in": "query",
            "name": "since",
            "schema": {
              "format": "date-time",
              "type": "string"
            }
          },
          {
            "description": "Backfill alerts ending at this date in RFC3339 format",
            "in": "query",
            "name": "until",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "202": {
            "description": "Accepted"
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
                      "message": "Internal Server Error"
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
        "summary": "Asynchronously backfill alerts for the monitor",
        "tags": [
          "Monitors"
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
      "name": "Monitors"
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

← [Asynchronously backfill alerts for new domains](patch-monitor-backfill.md) · [up](../README.md) · [Estimate how many alerts will be created for the backfill of an updated monitor](patch-monitor-backfill-estimate.md) →

*Archived from <https://gtidocs.virustotal.com/reference/post-monitor-backfill>.*
