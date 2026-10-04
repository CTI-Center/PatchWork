---
title: "Partial update an existing monitor"
source: https://gtidocs.virustotal.com/reference/patch-monitor-id
slug: patch-monitor-id
section: reference
group: "DTM (DIGITAL THREAT MONITORING)"
updatedAt: 2025-09-25T02:06:52.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [DTM (DIGITAL THREAT MONITORING)](../README.md) › [Monitors](../monitors.md) › Partial update an existing monitor

---

# partial-update-an-existing-monitor

Partial update an existing monitor with the fields in the request body. This request only updates the specified fields in the request body; the remaining fields of the existing monitor are unchanged.

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
      "Monitor": {
        "description": "A monitor defines 1 or more conditions and an optional doc query string to use for matching documents of interest. Matching a document results in the creation of an alert.",
        "properties": {
          "created_at": {
            "description": "The timestamp the monitor was created.",
            "example": "\"2021-08-19T19:48:36Z\"",
            "format": "date-time",
            "readOnly": true,
            "type": "string"
          },
          "created_by_user_email": {
            "description": "The user's name that created the monitor.",
            "readOnly": true,
            "type": "string"
          },
          "created_by_user_id": {
            "description": "The ID of the user that created the monitor.",
            "readOnly": true,
            "type": "string"
          },
          "description": {
            "description": "The description of the monitor.",
            "type": "string"
          },
          "doc_condition": {
            "$ref": "#/components/schemas/Condition"
          },
          "email_notify_enabled": {
            "description": "If email notifications are enabled for this monitor.",
            "type": "boolean"
          },
          "email_notify_immediate": {
            "description": "If immediate email delivery is enabled for this monitor.",
            "type": "boolean"
          },
          "enabled": {
            "description": "If the monitor is enabled or not.",
            "type": "boolean"
          },
          "id": {
            "description": "The ID of the monitor.",
            "example": "c4fbb52bqsiatib6i4gg",
            "readOnly": true,
            "type": "string"
          },
          "last_updated_by_user_id": {
            "description": "The ID of the user that last updated the monitor.",
            "readOnly": true,
            "type": "string"
          },
          "last_updated_user_email": {
            "description": "The user's name that last updated the monitor.",
            "readOnly": true,
            "type": "string"
          },
          "name": {
            "description": "The name of the monitor.",
            "type": "string"
          },
          "password_policy": {
            "$ref": "#/components/schemas/PasswordPolicy"
          },
          "template_id": {
            "description": "If a monitor was created from a template, then this field is populated with the template's ID. It cannot be changed after creation.",
            "readOnly": true,
            "type": "string"
          },
          "updated_at": {
            "description": "The timestamp the monitor was last updated.",
            "example": "\"2021-08-19T19:48:36Z\"",
            "format": "date-time",
            "readOnly": true,
            "type": "string"
          },
          "version": {
            "description": "The version number for the monitor. A monitor's version is incremented each time the monitor is updated.",
            "readOnly": true,
            "type": "integer"
          }
        },
        "required": [
          "doc_condition"
        ],
        "title": "Monitor",
        "type": "object"
      },
      "PasswordPolicy": {
        "description": "Criteria defining a password policy.",
        "properties": {
          "length_max": {
            "description": "The maxium length of the password in order to meet the policy.",
            "readOnly": false,
            "type": "integer"
          },
          "length_min": {
            "description": "The minimum length of the password in order to meet the policy.",
            "readOnly": false,
            "type": "integer"
          },
          "lowercase_char_count": {
            "description": "The minimum numer of lowercase characters a password is expected to have in order to meet the policy.",
            "readOnly": false,
            "type": "integer"
          },
          "lowercase_char_required": {
            "description": "If true, then the password is expected to have lowercase characters in order to meet the policy.",
            "readOnly": false,
            "type": "boolean"
          },
          "numbers_count": {
            "description": "The minimum numer of numerical characters a password is expected to have in order to meet the policy.",
            "readOnly": false,
            "type": "integer"
          },
          "numbers_required": {
            "description": "If true, then the password is expected to have numerical characters in order to meet the policy.",
            "readOnly": false,
            "type": "boolean"
          },
          "special_char_count": {
            "description": "The minimum numer of special case characters a password is expected to have in order to meet the policy.",
            "readOnly": false,
            "type": "integer"
          },
          "special_char_required": {
            "description": "If true, then the password is expected to have special case characters in order to meet the policy.",
            "readOnly": false,
            "type": "boolean"
          },
          "uppercase_char_count": {
            "description": "The minimum numer of uppercase characters a password is expected to have in order to meet the policy.",
            "readOnly": false,
            "type": "integer"
          },
          "uppercase_char_required": {
            "description": "If true, then the password is expected to have uppercase characters in order to meet the policy.",
            "readOnly": false,
            "type": "boolean"
          }
        },
        "title": "Password Policy",
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
    "/monitors/{id}": {
      "patch": {
        "description": "",
        "operationId": "patch-monitor-id",
        "parameters": [
          {
            "description": "The monitor ID.",
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
            "description": "The accept type supported in the response.",
            "in": "header",
            "name": "Accept",
            "required": true,
            "schema": {
              "default": "application/json",
              "example": "application/json",
              "type": "string"
            }
          },
          {
            "description": "The content type of the request body.",
            "in": "header",
            "name": "Content-Type",
            "required": true,
            "schema": {
              "default": "application/json",
              "example": "application/json",
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "examples": {
                "patch-monitor": {
                  "value": {
                    "description": "My updated description"
                  }
                }
              },
              "schema": {
                "$ref": "#/components/schemas/Monitor"
              }
            }
          },
          "description": "The monitor fields to update."
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Monitor"
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
          "404": {
            "content": {
              "application/json": {
                "examples": {
                  "not-found": {
                    "value": {
                      "message": "Not Found"
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
        "summary": "Partial update an existing monitor",
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

← [Get a monitor by its ID](get-monitor-id.md) · [up](../README.md) · [Update an existing monitor](put-monitor-id.md) →

*Archived from <https://gtidocs.virustotal.com/reference/patch-monitor-id>.*
