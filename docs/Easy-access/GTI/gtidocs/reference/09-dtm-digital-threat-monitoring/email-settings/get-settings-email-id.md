---
title: "Fetch an email setting"
source: https://gtidocs.virustotal.com/reference/get-settings-email-id
slug: get-settings-email-id
section: reference
group: "DTM (DIGITAL THREAT MONITORING)"
updatedAt: 2025-09-25T02:06:57.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [DTM (DIGITAL THREAT MONITORING)](../README.md) › [Email Settings](../email-settings.md) › Fetch an email setting

---

# fetch-an-email-setting

Get email settings by ID.

# openapi-definition

```json
{
  "components": {
    "schemas": {
      "EmailRecipient": {
        "description": "An email recipient.",
        "properties": {
          "email_address": {
            "description": "The email address of the recipient.",
            "format": "email",
            "type": "string"
          },
          "status": {
            "description": "The status of the email address verification.",
            "enum": [
              "invalid",
              "pending",
              "verified",
              "expired"
            ],
            "readOnly": true,
            "type": "string"
          },
          "verification_sent_at": {
            "description": "The timestamp an email verification was sent at for this email address.",
            "format": "date-time",
            "readOnly": true,
            "type": "string"
          }
        },
        "required": [
          "email_address"
        ],
        "title": "Email Recipient",
        "type": "object"
      },
      "EmailSetting": {
        "description": "Email notification settings.",
        "properties": {
          "created_at": {
            "description": "The timestamp this email setting was created.",
            "format": "date-time",
            "readOnly": true,
            "type": "string"
          },
          "delivery_times": {
            "description": "The delivery times specified for scheduled emails.",
            "items": {
              "enum": [
                "00:00",
                "00:30",
                "01:00",
                "01:30",
                "02:00",
                "02:30",
                "03:00",
                "03:30",
                "04:00",
                "04:30",
                "05:00",
                "05:30",
                "06:00",
                "06:30",
                "07:00",
                "07:30",
                "08:00",
                "08:30",
                "09:00",
                "09:30",
                "10:00",
                "10:30",
                "11:00",
                "11:30",
                "12:00",
                "12:30",
                "13:00",
                "13:30",
                "14:00",
                "14:30",
                "15:00",
                "15:30",
                "16:00",
                "16:30",
                "17:00",
                "17:30",
                "18:00",
                "18:30",
                "19:00",
                "19:30",
                "20:00",
                "20:30",
                "21:00",
                "21:30",
                "22:00",
                "22:30",
                "23:00",
                "23:30"
              ],
              "type": "string"
            },
            "type": "array"
          },
          "frequency": {
            "description": "The frequency at which scheduled emails are delivered.",
            "items": {
              "enum": [
                "sunday",
                "monday",
                "tuesday",
                "wednesday",
                "thursday",
                "friday",
                "saturday"
              ],
              "type": "string"
            },
            "type": "array"
          },
          "id": {
            "description": "The ID of the email settings.",
            "readOnly": true,
            "type": "string"
          },
          "recipients": {
            "description": "The recipients to receive emails.",
            "items": {
              "$ref": "#/components/schemas/EmailRecipient"
            },
            "type": "array"
          },
          "timezone_location": {
            "description": "The timezone location to use for scheduled emails.",
            "type": "string"
          },
          "updated_at": {
            "description": "The timestamp this email setting was last updated.",
            "format": "date-time",
            "readOnly": true,
            "type": "string"
          }
        },
        "title": "Email Setting",
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
    "/settings/email/{id}": {
      "get": {
        "description": "",
        "operationId": "get-settings-email-id",
        "parameters": [
          {
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
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
            "description": "Accept type",
            "in": "header",
            "name": "Accept",
            "required": true,
            "schema": {
              "enum": [
                "application/json"
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
                  "get-email-setting": {
                    "value": {
                      "created_at": "2022-01-20T17:29:20.205Z",
                      "delivery_times": [
                        "00:00",
                        "00:30",
                        "01:00",
                        "01:30",
                        "02:00",
                        "02:30",
                        "03:00",
                        "03:30",
                        "04:00",
                        "04:30",
                        "05:00",
                        "05:30",
                        "06:00",
                        "06:30",
                        "07:00",
                        "07:30",
                        "08:00",
                        "08:30",
                        "09:00",
                        "09:30",
                        "10:00",
                        "10:30",
                        "11:00",
                        "11:30",
                        "12:00",
                        "12:30",
                        "13:00",
                        "13:30",
                        "14:00",
                        "14:30",
                        "15:00",
                        "15:30",
                        "16:00",
                        "16:30",
                        "17:00",
                        "17:30",
                        "18:00",
                        "18:30",
                        "19:00",
                        "19:30",
                        "20:00",
                        "20:30",
                        "21:00",
                        "21:30",
                        "22:00",
                        "22:30",
                        "23:00",
                        "23:30"
                      ],
                      "frequency": [
                        "sunday",
                        "monday",
                        "tuesday",
                        "wednesday",
                        "thursday",
                        "friday",
                        "saturday"
                      ],
                      "id": "c7kpns36fv7ll65ekbog",
                      "recipients": [
                        {
                          "email_address": "username1@yourdomain.com",
                          "status": "verified",
                          "verification_sent_at": "2022-01-20T17:29:20.205Z"
                        },
                        {
                          "email_address": "username2@yourdomain.com",
                          "status": "invalid",
                          "verification_sent_at": "2022-01-20T17:29:20.205Z"
                        }
                      ],
                      "timezone_location": "America/Denver",
                      "updated_at": "2022-01-20T17:30:00.013Z"
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/EmailSetting"
                }
              }
            },
            "description": "OK",
            "headers": {
              "Content-Type": {
                "description": "Response content type",
                "schema": {
                  "enum": [
                    "application/json"
                  ],
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
            "description": "Unauthorized"
          },
          "404": {
            "content": {
              "application/json": {
                "examples": {
                  "not-found": {
                    "value": {
                      "message": "not found"
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Response-message"
                }
              }
            },
            "description": "Not Found"
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
            "description": "Internal Server Error"
          }
        },
        "summary": "Fetch an email setting",
        "tags": [
          "Email Settings"
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
      "name": "Email Settings"
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

← [Delete email settings](delete-settings-email-id.md) · [up](../README.md) · [Update email settings](patch-settings-email-id.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-settings-email-id>.*
