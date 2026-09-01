---
title: "Update the analysis text on an alert"
source: https://gtidocs.virustotal.com/reference/put-alert-analysis
slug: put-alert-analysis
section: reference
group: "DTM (DIGITAL THREAT MONITORING)"
updatedAt: 2025-09-25T02:06:47.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [DTM (DIGITAL THREAT MONITORING)](../README.md) › [Alert Analysis](../alert-analysis.md) › Update the analysis text on an alert

---

# update-the-analysis-text-on-an-alert

Update the analysis text on an alert object. The empty string will clear out existing analysis. Markdown format can be used.

# openapi-definition

```json
{
  "components": {
    "schemas": {
      "AlertAnalysisOp": {
        "description": "The analysis text for an alert. This can be in markdown format.",
        "properties": {
          "analysis": {
            "description": "The analysis text that can be in markdown format.",
            "readOnly": false,
            "type": "string"
          }
        },
        "title": "Alert Analysis Operation",
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
    "/alerts/{id}/analysis": {
      "put": {
        "description": "",
        "operationId": "put-alert-analysis",
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
            "description": "The ID of the alert to update the analysis on.",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "example": "c4huif0mhcmiku5g7jsg",
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/AlertAnalysisOp"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK"
          },
          "400": {
            "content": {
              "application/json": {
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
        "summary": "Update the analysis text on an alert",
        "tags": [
          "Alert Analysis"
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
      "name": "Alert Analysis"
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

← [Alert Analysis](../alert-analysis.md) · [up](../README.md) · [List the file attachments for the alert](get-alert-analysis-attachments.md) →

*Archived from <https://gtidocs.virustotal.com/reference/put-alert-analysis>.*
