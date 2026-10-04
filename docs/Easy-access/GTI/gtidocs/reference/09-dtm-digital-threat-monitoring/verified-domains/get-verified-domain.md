---
title: "Get a verified domain by ID"
source: https://gtidocs.virustotal.com/reference/get-verified-domain
slug: get-verified-domain
section: reference
group: "DTM (DIGITAL THREAT MONITORING)"
updatedAt: 2025-09-25T02:07:00.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [DTM (DIGITAL THREAT MONITORING)](../README.md) › [Verified Domains](../verified-domains.md) › Get a verified domain by ID

---

# get-a-verified-domain-by-id

Get a verified domain by its ID.

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
      },
      "VerifiedDomain": {
        "description": "A verified domain proves ownership of domain and is used for authenticating login credential visibility for Compromised Credential alerts.",
        "properties": {
          "challenge": {
            "description": "The DNS TXT record challenge code that's used to verified domain ownership.",
            "readOnly": true,
            "type": "string"
          },
          "created_at": {
            "description": "The time the verified domain was created.",
            "format": "date-time",
            "readOnly": true,
            "type": "string"
          },
          "created_by": {
            "description": "The user name that created the verified domain.",
            "readOnly": true,
            "type": "string"
          },
          "created_by_user_id": {
            "description": "The user ID that created the verified domain.",
            "readOnly": true,
            "type": "string"
          },
          "domain": {
            "description": "The domain name. Must not be a free email provider domain.",
            "readOnly": false,
            "type": "string"
          },
          "id": {
            "description": "The ID of the verified domain.",
            "example": "c4fbb52bqsiatib6i4gg",
            "readOnly": true,
            "type": "string"
          },
          "primary_domain": {
            "description": "The primary domain extracted from the domain name. e.g. the parent domain.",
            "readOnly": true,
            "type": "string"
          },
          "status": {
            "description": "The status of the verified domain with respect to its proven ownership.",
            "enum": [
              "unverified",
              "verified",
              "pending",
              "error"
            ],
            "readOnly": true,
            "type": "string"
          },
          "updated_at": {
            "description": "The time the verified domain was last updated.",
            "format": "date-time",
            "readOnly": true,
            "type": "string"
          },
          "updated_by": {
            "description": "The user name that last updated the verified domain.",
            "readOnly": true,
            "type": "string"
          },
          "updated_by_user_id": {
            "description": "The user ID that last updated the verified domain.",
            "readOnly": true,
            "type": "string"
          },
          "verification_checked_at": {
            "description": "The last time the DNS TXT record was checked for verification.",
            "format": "date-time",
            "readOnly": true,
            "type": "string"
          },
          "verification_message": {
            "description": "A explaination pretaining to the last time the TXT record was checked for the verification code.",
            "readOnly": true,
            "type": "string"
          },
          "verification_type": {
            "description": "The type of verification used for the domain.",
            "enum": [
              "txt_record",
              "manual"
            ],
            "readOnly": true,
            "type": "string"
          }
        },
        "title": "Verifeid Domain",
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
    "/settings/domains/{id}": {
      "get": {
        "description": "",
        "operationId": "get-verified-domain",
        "parameters": [
          {
            "description": "The domain ID.",
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
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/VerifiedDomain"
                }
              }
            },
            "description": "OK"
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
        "summary": "Get a verified domain by ID",
        "tags": [
          "Verified Domains"
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
      "name": "Verified Domains"
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

← [Delete an existing verified domain.](delete-domain-id.md) · [up](../README.md) · [Perform a synchronous verification check for the domain's TXT record code.](reverify-domain-id.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-verified-domain>.*
