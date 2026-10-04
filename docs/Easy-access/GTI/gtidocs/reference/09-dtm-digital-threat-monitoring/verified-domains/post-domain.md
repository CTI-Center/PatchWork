---
title: "Add a new verified domain"
source: https://gtidocs.virustotal.com/reference/post-domain
slug: post-domain
section: reference
group: "DTM (DIGITAL THREAT MONITORING)"
updatedAt: 2025-09-25T02:06:59.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [DTM (DIGITAL THREAT MONITORING)](../README.md) › [Verified Domains](../verified-domains.md) › Add a new verified domain

---

# add-a-new-verified-domain

Add a new verified domain.

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
      },
      "VerifiedDomainOp": {
        "description": "A verified domain proves ownership of domain and is used for authenticating login credential visibility for Compromised Credential alerts.",
        "properties": {
          "domain": {
            "description": "A verified domain to create.",
            "readOnly": false,
            "type": "string"
          }
        },
        "title": "Verified Domain Operation",
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
    "/settings/domains": {
      "post": {
        "description": "",
        "operationId": "post-domain",
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
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/VerifiedDomainOp"
              }
            }
          },
          "description": "The new verified domain to add."
        },
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
        "summary": "Add a new verified domain",
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

← [List verified domains for the current organization](get-verified-domains.md) · [up](../README.md) · [Delete an existing verified domain.](delete-domain-id.md) →

*Archived from <https://gtidocs.virustotal.com/reference/post-domain>.*
