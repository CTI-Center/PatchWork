---
title: "Upload attachments to an alert's analysis"
source: https://gtidocs.virustotal.com/reference/post-alert-analysis-attachment
slug: post-alert-analysis-attachment
section: reference
group: "DTM (DIGITAL THREAT MONITORING)"
updatedAt: 2025-09-25T02:06:48.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [DTM (DIGITAL THREAT MONITORING)](../README.md) › [Alert Analysis](../alert-analysis.md) › Upload attachments to an alert's analysis

---

# upload-attachments-to-an-alert's-analysis

Upload one or more files to the alert's analysis. The following file type extensions are supported; doc, docx, xls, xlsx, pdf, png, zip, csv, txt

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
    "/alerts/{id}/attachments": {
      "post": {
        "description": "",
        "operationId": "post-alert-analysis-attachment",
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
            "description": "Multipart form data is used to upload one or more files to an alert analysis.",
            "in": "header",
            "name": "Content-Type",
            "required": true,
            "schema": {
              "enum": [
                "multipart/form-data"
              ],
              "type": "string"
            }
          },
          {
            "description": "The ID of the alert to add the attachment to.",
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
        "summary": "Upload attachments to an alert's analysis",
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

← [List the file attachments for the alert](get-alert-analysis-attachments.md) · [up](../README.md) · [Delete a file attachment from an alert](delete-alert-attachment.md) →

*Archived from <https://gtidocs.virustotal.com/reference/post-alert-analysis-attachment>.*
