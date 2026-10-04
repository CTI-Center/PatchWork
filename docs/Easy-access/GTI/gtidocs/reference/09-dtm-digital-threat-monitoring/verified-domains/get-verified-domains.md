---
title: "List verified domains for the current organization"
source: https://gtidocs.virustotal.com/reference/get-verified-domains
slug: get-verified-domains
section: reference
group: "DTM (DIGITAL THREAT MONITORING)"
updatedAt: 2025-09-25T02:06:59.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [DTM (DIGITAL THREAT MONITORING)](../README.md) › [Verified Domains](../verified-domains.md) › List verified domains for the current organization

---

# list-verified-domains-for-the-current-organization

Lists all verified domains. Pagination is supported and the URI to next page of results is provided in the response link header. If fetching subsequent pages, only use the next link header provided in the previous page of results.

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
    "/settings/domains": {
      "get": {
        "description": "",
        "operationId": "get-verified-domains",
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
            "description": "The field to sort the response objects by.",
            "in": "query",
            "name": "sort",
            "schema": {
              "default": "created_at",
              "enum": [
                "id",
                "domain",
                "status",
                "created_at",
                "updated_at"
              ],
              "example": "updated_at",
              "type": "string"
            }
          },
          {
            "description": "The order used to sort the response objects.",
            "in": "query",
            "name": "order",
            "schema": {
              "default": "desc",
              "enum": [
                "desc",
                "asc"
              ],
              "example": "asc",
              "type": "string"
            }
          },
          {
            "description": "The number of objects to return in each page.",
            "in": "query",
            "name": "size",
            "schema": {
              "default": 10,
              "example": 20,
              "type": "integer"
            }
          },
          {
            "description": "The type of content accepted.",
            "in": "header",
            "name": "Accept",
            "schema": {
              "default": "application/json",
              "example": "application/json",
              "type": "string"
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
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/VerifiedDomains"
                }
              }
            },
            "description": "OK",
            "headers": {
              "Link": {
                "description": "If another page of results is available for pagination, the Link header will contain the URI used to fetch the next page.",
                "schema": {
                  "example": "<https://api.intelligence.mandiant.com/v4/dtm/settings/domains?page=c52e5bc1hrv40t8d0gvg>; rel=\"next\"",
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
        "summary": "List verified domains for the current organization",
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

← [Verified Domains](../verified-domains.md) · [up](../README.md) · [Add a new verified domain](post-domain.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-verified-domains>.*
