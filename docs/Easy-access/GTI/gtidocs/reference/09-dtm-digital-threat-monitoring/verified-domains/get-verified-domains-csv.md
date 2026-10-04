---
title: "Download all verified domains with their TXT verification code in CSV format"
source: https://gtidocs.virustotal.com/reference/get-verified-domains-csv
slug: get-verified-domains-csv
section: reference
group: "DTM (DIGITAL THREAT MONITORING)"
updatedAt: 2025-09-25T02:07:01.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [DTM (DIGITAL THREAT MONITORING)](../README.md) › [Verified Domains](../verified-domains.md) › Download all verified domains with their TXT verification code in CSV format

---

# download-all-verified-domains-with-their-txt-verification-code-in-csv-format

Lists all verified domains in CSV format suitable for getting an inventory of the domain TXT record codes to verify.

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
      "VerifiedDomains": {
        "description": "A list of verified domains.",
        "properties": {
          "domains": {
            "description": "The list of verified domains.",
            "items": {
              "$ref": "#/components/schemas/VerifiedDomain"
            },
            "type": "array"
          }
        },
        "required": [
          "domains"
        ],
        "title": "Verified Domains",
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
    "/settings/domains/txt_record": {
      "get": {
        "description": "",
        "operationId": "get-verified-domains-csv",
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
            "description": "Only text/csv is supported.",
            "in": "header",
            "name": "Accept",
            "schema": {
              "default": "text/csv",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "text/csv": {
                "schema": {
                  "$ref": "#/components/schemas/VerifiedDomains"
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
        "summary": "Download all verified domains with their TXT verification code in CSV format",
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

← [Add new verified domains](post-domain-bulk.md) · [up](../README.md) · [DTM Docs](../dtm-docs.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-verified-domains-csv>.*
