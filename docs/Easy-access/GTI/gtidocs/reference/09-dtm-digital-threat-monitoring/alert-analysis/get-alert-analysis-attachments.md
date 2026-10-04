---
title: "List the file attachments for the alert"
source: https://gtidocs.virustotal.com/reference/get-alert-analysis-attachments
slug: get-alert-analysis-attachments
section: reference
group: "DTM (DIGITAL THREAT MONITORING)"
updatedAt: 2025-09-25T02:06:47.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [DTM (DIGITAL THREAT MONITORING)](../README.md) › [Alert Analysis](../alert-analysis.md) › List the file attachments for the alert

---

# list-the-file-attachments-for-the-alert

List the file attachments for a given alert.

# openapi-definition

```json
{
  "components": {
    "schemas": {
      "FileAttachment": {
        "description": "Metadata describing a file attachment.",
        "properties": {
          "content_type": {
            "description": "The content type of the file attachment.",
            "readOnly": true,
            "type": "string"
          },
          "created_at": {
            "description": "The time the file attachment was created.",
            "format": "date-time",
            "readOnly": true,
            "type": "string"
          },
          "created_by_user_id": {
            "description": "The user ID that created the attachment.",
            "readOnly": true,
            "type": "string"
          },
          "filesize_bytes": {
            "description": "The size of the attachment measured in bytes.",
            "readOnly": true,
            "type": "integer"
          },
          "id": {
            "description": "The ID of the file attachment.",
            "readOnly": true,
            "type": "string"
          },
          "name": {
            "description": "The file name of the attachment.",
            "readOnly": true,
            "type": "string"
          }
        },
        "title": "File Attachment",
        "type": "object"
      },
      "FileAttachments": {
        "description": "List of file attachments.",
        "properties": {
          "attachments": {
            "description": "The list of file attachments.",
            "items": {
              "$ref": "#/components/schemas/FileAttachment"
            },
            "type": "array"
          }
        },
        "title": "File Attachments",
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
    "/alerts/{id}/attachments": {
      "get": {
        "description": "",
        "operationId": "get-alert-analysis-attachments",
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
            "description": "The content type.",
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
            "description": "The ID of the alert to list attachments for.",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "example": "c4huif0mhcmiku5g7jsg",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/FileAttachments"
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
              }
            }
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
        "summary": "List the file attachments for the alert",
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

← [Update the analysis text on an alert](put-alert-analysis.md) · [up](../README.md) · [Upload attachments to an alert's analysis](post-alert-analysis-attachment.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-alert-analysis-attachments>.*
