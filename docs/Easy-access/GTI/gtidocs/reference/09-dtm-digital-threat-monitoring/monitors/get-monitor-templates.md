---
title: "List monitor templates for top DTM use cases"
source: https://gtidocs.virustotal.com/reference/get-monitor-templates
slug: get-monitor-templates
section: reference
group: "DTM (DIGITAL THREAT MONITORING)"
updatedAt: 2025-09-25T02:06:55.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [DTM (DIGITAL THREAT MONITORING)](../README.md) › [Monitors](../monitors.md) › List monitor templates for top DTM use cases

---

# list-monitor-templates-for-top-dtm-use-cases

Lists all monitor templates for top DTM use cases. Templates are intended to be the starting place for montior creation based on a specific use case.

# openapi-definition

```json
{
  "components": {
    "schemas": {
      "Condition": {
        "description": "A Condition forms the basis for querying topics and labels in monitors. It can be used to form complex conditions using all/any as well as specifying specific values to match for documents. See the user guide for more details.",
        "properties": {
          "match": {
            "description": "The match values, or sub Conditions.",
            "items": {
              "$ref": "#/components/schemas/Condition"
            },
            "type": "array"
          },
          "operator": {
            "description": "The operator to use for this Condition.",
            "enum": [
              "must_equal",
              "must_not_equal",
              "must_start_with",
              "must_not_start_with",
              "must_end_with",
              "must_not_end_with",
              "must_contain",
              "must_not_contain",
              "any",
              "all"
            ],
            "type": "string"
          },
          "topic": {
            "description": "The topic to apply this Condition to.",
            "enum": [
              "doc_type",
              "source",
              "match_conditions",
              "credential_domain",
              "typosquatted_domain",
              "keyword",
              "lucene",
              "group_bin",
              "group_brand",
              "group_crypto",
              "group_hash",
              "group_identity",
              "group_keys",
              "group_location",
              "group_network",
              "group_paths",
              "group_social",
              "group_threats",
              "label_industry",
              "label_language",
              "label_threat",
              "label_type",
              "bin",
              "bin_foreign",
              "bin_partial",
              "organization",
              "product",
              "name",
              "brand",
              "product_batch_name",
              "atom_address",
              "bch_address",
              "btc_address",
              "dash_address",
              "doge_address",
              "ltc_address",
              "xlm_address",
              "xmr_address",
              "zec_address",
              "sha1_hash",
              "sha256_hash",
              "md5_hash",
              "client_identifier",
              "email_address",
              "identity_name",
              "twitter_handle",
              "telegram_user_name",
              "phone_number",
              "access_token",
              "crypto_key_private",
              "crypto_key_public",
              "password_plaintext",
              "predict_password_plaintext",
              "location_name",
              "city",
              "country",
              "ipv4_address",
              "ipv6_address",
              "domain",
              "mac_address",
              "url",
              "filename",
              "path",
              "registry_key",
              "hashtag",
              "icq_uin",
              "jid",
              "cve",
              "threat_name",
              "threat_group_name",
              "service_name",
              "cwe"
            ],
            "type": "string"
          }
        },
        "required": [
          "operator",
          "topic",
          "match"
        ],
        "title": "Condition",
        "type": "object"
      },
      "MonitorTemplate": {
        "description": "Monitor templates provide suggested monitor conditions based on top DTM use cases.",
        "properties": {
          "description": {
            "description": "The description of the monitor.",
            "type": "string"
          },
          "doc_condition": {
            "$ref": "#/components/schemas/Condition"
          },
          "id": {
            "description": "The ID of the monitor.",
            "example": "c4fbb52bqsiatib6i4gg",
            "readOnly": true,
            "type": "string"
          },
          "name": {
            "description": "The name of the monitor.",
            "type": "string"
          }
        },
        "required": [
          "doc_condition"
        ],
        "title": "Monitor Template",
        "type": "object"
      },
      "MonitorTemplates": {
        "description": "A list of monitor templates for top DTM use cases.",
        "properties": {
          "templates": {
            "description": "The list of monitor templates.",
            "items": {
              "$ref": "#/components/schemas/MonitorTemplate"
            },
            "type": "array"
          }
        },
        "title": "Monitor Templates",
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
    "/monitors/templates": {
      "get": {
        "description": "",
        "operationId": "get-monitor-templates",
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
            "description": "The type of content accepted.",
            "in": "header",
            "name": "Accept",
            "schema": {
              "default": "application/json",
              "example": "application/json",
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/MonitorTemplates"
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
        "summary": "List monitor templates for top DTM use cases",
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

← [Estimate how many alerts will be created for the backfill of a newly created monitor](post-monitor-backfill-estimate.md) · [up](../README.md) · [Email Settings](../email-settings.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-monitor-templates>.*
