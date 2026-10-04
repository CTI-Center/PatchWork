---
title: "List monitors"
source: https://gtidocs.virustotal.com/reference/get-monitors
slug: get-monitors
section: reference
group: "DTM (DIGITAL THREAT MONITORING)"
updatedAt: 2025-09-25T02:06:51.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [DTM (DIGITAL THREAT MONITORING)](../README.md) › [Monitors](../monitors.md) › List monitors

---

# list-monitors

Lists all monitors belonging to the current organization. Pagination is supported and the URI to next page of results is provided in the response link header. If fetching subsequent pages, only use the next link header provided in the previous page of results.

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
      "Monitors": {
        "description": "A list of monitor.",
        "properties": {
          "monitors": {
            "description": "The list of monitors.",
            "items": {
              "$ref": "#/components/schemas/Monitor"
            },
            "type": "array"
          }
        },
        "title": "Monitors",
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
    "/monitors": {
      "get": {
        "description": "",
        "operationId": "get-monitors",
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
            "description": "The monitor field name to sort the response monitors by.",
            "in": "query",
            "name": "sort",
            "schema": {
              "default": "created_at",
              "enum": [
                "id",
                "name",
                "description",
                "created_at",
                "updated_at"
              ],
              "example": "updated_at",
              "type": "string"
            }
          },
          {
            "description": "The order used to sort the response monitors.",
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
            "description": "The number of monitors to return in each page.",
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
            "description": "When listing monitors by date range, since defines the starting date in RFC3339 format",
            "in": "query",
            "name": "since",
            "schema": {
              "format": "date-time",
              "type": "string"
            }
          },
          {
            "description": "When listing monitors by date range, until defines the ending date in RFC3339 format",
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
                  "$ref": "#/components/schemas/Monitors"
                }
              }
            },
            "description": "OK",
            "headers": {
              "Link": {
                "description": "If another page of results is available for pagination, the Link header will contain the URI used to fetch the next page.",
                "schema": {
                  "example": "<https://api.intelligence.mandiant.com/v4/dtm/monitors?page=c52e5bc1hrv40t8d0gvg>; rel=\"next\"",
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
        "summary": "List monitors",
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

← [Monitors](../monitors.md) · [up](../README.md) · [Create a new monitor](post-monitor.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-monitors>.*
