---
title: "Retrieve an indexed document by its type and ID"
source: https://gtidocs.virustotal.com/reference/get-docs-type-id
slug: get-docs-type-id
section: reference
group: "DTM (DIGITAL THREAT MONITORING)"
updatedAt: 2025-09-25T02:07:03.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [DTM (DIGITAL THREAT MONITORING)](../README.md) › [DTM Docs](../dtm-docs.md) › Retrieve an indexed document by its type and ID

---

# retrieve-an-indexed-document-by-its-type-and-id

A read-only endpoint that fetches an indexed document (optionally) along with its topics and labels.

# openapi-definition

```json
{
  "components": {
    "schemas": {
      "Doc": {
        "description": "A ingested/indexed raw document including thet topics and labels created from the doc by our Analytics processing.",
        "properties": {
          "doc": {
            "description": "The raw document.",
            "oneOf": [
              {
                "$ref": "#/components/schemas/message"
              },
              {
                "$ref": "#/components/schemas/paste"
              },
              {
                "$ref": "#/components/schemas/shop_listing"
              },
              {
                "$ref": "#/components/schemas/tweet"
              },
              {
                "$ref": "#/components/schemas/web_content_publish"
              },
              {
                "$ref": "#/components/schemas/forum_post"
              },
              {
                "$ref": "#/components/schemas/domain_discovery"
              }
            ]
          },
          "labels": {
            "description": "The labels identified in the raw document.",
            "items": {
              "$ref": "#/components/schemas/Label"
            },
            "readOnly": true,
            "type": "array"
          },
          "labels_url": {
            "description": "The URL to the labels for this document.",
            "format": "uri",
            "readOnly": true,
            "type": "string"
          },
          "topics": {
            "description": "The topics identified in the raw document.",
            "items": {
              "$ref": "#/components/schemas/Topic"
            },
            "readOnly": true,
            "type": "array"
          },
          "topics_url": {
            "description": "The URL to the topics for this document.",
            "format": "uri",
            "readOnly": true,
            "type": "string"
          }
        },
        "required": [
          "labels_url",
          "topics_url"
        ],
        "title": "Raw Source Document",
        "type": "object"
      },
      "Entity_location": {
        "description": "The location of a Topic (entity) identified within a (raw) document",
        "properties": {
          "element_path": {
            "description": "The JSON field path at which the entity was found in the raw document.",
            "example": "body",
            "readOnly": true,
            "type": "string"
          },
          "offsets": {
            "description": "The list of offsets where the entity was found in the element_path.",
            "items": {
              "example": "[72, 76]",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "readOnly": true,
            "type": "array"
          }
        },
        "required": [
          "element_path",
          "offsets"
        ],
        "title": "Entity Location",
        "type": "object"
      },
      "Label": {
        "description": "A Label identified within a (raw) document.",
        "properties": {
          "classifier": {
            "description": "The classifier that identified this label.",
            "example": "classifier-language",
            "readOnly": true,
            "type": "string"
          },
          "confidence": {
            "description": "The confidence estimate that the label was identified properly.",
            "example": 100,
            "readOnly": true,
            "type": "integer"
          },
          "element_path": {
            "description": "The JSON field path in the raw document where the label was identified.",
            "example": "body",
            "readOnly": true,
            "type": "string"
          },
          "id": {
            "description": "The ID of the label.",
            "example": "ad2fe138-92ea-4642-adc0-53db0e2d4d1b",
            "readOnly": true,
            "type": "string"
          },
          "label": {
            "description": "The label value.",
            "example": "en",
            "readOnly": true,
            "type": "string"
          },
          "version": {
            "description": "The version of the classifier that identified this label.",
            "example": "1-0-0",
            "type": "string"
          }
        },
        "required": [
          "id",
          "classifier",
          "version",
          "label",
          "confidence",
          "element_path"
        ],
        "title": "Label",
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
      },
      "Topic": {
        "description": "A topic identified within a (raw) document",
        "properties": {
          "confidence": {
            "description": "The estimated confidence that the value was properly idenitified.",
            "example": 100,
            "maximum": 100,
            "readOnly": true,
            "type": "integer"
          },
          "entity_locations": {
            "description": "The locations of the identified entities.",
            "items": {
              "$ref": "#/components/schemas/Entity_location"
            },
            "readOnly": true,
            "type": "array"
          },
          "extractor": {
            "description": "The name of the extractor that identified the topic value.",
            "example": "analysis-pipeline.preprocessor",
            "readOnly": true,
            "type": "string"
          },
          "id": {
            "description": "The ID of the identified topic.",
            "example": "c46bbad1-b542-4d66-9ddb-db84ed16b41f",
            "readOnly": true,
            "type": "string"
          },
          "type": {
            "description": "The type of the topic.",
            "example": "domain",
            "readOnly": true,
            "type": "string"
          },
          "value": {
            "description": "The value identified for the topic.",
            "example": "mydomain.com",
            "readOnly": true,
            "type": "string"
          },
          "version": {
            "description": "The version of the extractor.",
            "example": "1.0.0",
            "readOnly": true,
            "type": "string"
          }
        },
        "required": [
          "id",
          "value",
          "type",
          "extractor",
          "version",
          "confidence",
          "entity_locations"
        ],
        "title": "Topic",
        "type": "object"
      },
      "bin": {
        "title": "bin",
        "type": "string"
      },
      "brand": {
        "title": "brand",
        "type": "string"
      },
      "channel": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "channel_id": {
            "title": "channel_id",
            "type": "string"
          },
          "channel_info": {
            "$ref": "#/components/schemas/channel_info"
          },
          "invite_url": {
            "$ref": "#/components/schemas/url"
          },
          "messenger": {
            "$ref": "#/components/schemas/service"
          },
          "name": {
            "$ref": "#/components/schemas/name"
          }
        },
        "title": "channel",
        "type": "object"
      },
      "channel_info": {
        "properties": {
          "description": {
            "title": "description",
            "type": "string"
          }
        },
        "title": "channel_info",
        "type": "object"
      },
      "city": {
        "title": "city",
        "type": "string"
      },
      "contact": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "aim": {
            "title": "aim",
            "type": "string"
          },
          "email": {
            "$ref": "#/components/schemas/email_address"
          },
          "email_domain": {
            "$ref": "#/components/schemas/domain"
          },
          "email_redacted": {
            "title": "email_redacted",
            "type": "string"
          },
          "fax": {
            "$ref": "#/components/schemas/phone_number"
          },
          "geo_location": {
            "$ref": "#/components/schemas/geo_location"
          },
          "icq": {
            "$ref": "#/components/schemas/icq_uin"
          },
          "jid": {
            "$ref": "#/components/schemas/jid"
          },
          "msnm": {
            "title": "msnm",
            "type": "string"
          },
          "phone": {
            "$ref": "#/components/schemas/phone_number"
          },
          "twitter_handle": {
            "$ref": "#/components/schemas/twitter_handle"
          },
          "website": {
            "$ref": "#/components/schemas/url"
          }
        },
        "title": "contact",
        "type": "object"
      },
      "content_type": {
        "title": "content_type",
        "type": "string"
      },
      "continent_code": {
        "title": "continent_code",
        "type": "string"
      },
      "country": {
        "title": "country",
        "type": "string"
      },
      "country_code": {
        "title": "country_code",
        "type": "string"
      },
      "country_code_3": {
        "title": "country_code_3",
        "type": "string"
      },
      "cpu": {
        "properties": {
          "cores": {
            "format": "int32",
            "title": "cores",
            "type": "integer"
          },
          "product": {
            "$ref": "#/components/schemas/product"
          }
        },
        "title": "cpu",
        "type": "object"
      },
      "data_availability": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "admin_access_available": {
            "title": "admin_access_available",
            "type": "boolean"
          },
          "cvc_available": {
            "title": "cvc_available",
            "type": "boolean"
          },
          "dob_available": {
            "title": "dob_available",
            "type": "boolean"
          },
          "email_available": {
            "title": "email_available",
            "type": "boolean"
          },
          "geo_location_available": {
            "title": "geo_location_available",
            "type": "boolean"
          },
          "mmn_available": {
            "title": "mmn_available",
            "type": "boolean"
          },
          "name_available": {
            "title": "name_available",
            "type": "boolean"
          },
          "phone_available": {
            "title": "phone_available",
            "type": "boolean"
          },
          "pin_available": {
            "title": "pin_available",
            "type": "boolean"
          },
          "pvki_available": {
            "title": "pvki_available",
            "type": "boolean"
          },
          "pvv_available": {
            "title": "pvv_available",
            "type": "boolean"
          },
          "ssn_available": {
            "title": "ssn_available",
            "type": "boolean"
          },
          "track1_available": {
            "title": "track1_available",
            "type": "boolean"
          },
          "track2_available": {
            "title": "track2_available",
            "type": "boolean"
          },
          "vbv_available": {
            "title": "vbv_available",
            "type": "boolean"
          }
        },
        "title": "data_availability",
        "type": "object"
      },
      "dns_rr": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "priority": {
            "format": "int32",
            "title": "priority",
            "type": "integer"
          },
          "rdata_domain": {
            "$ref": "#/components/schemas/domain"
          },
          "rdata_ipv4": {
            "$ref": "#/components/schemas/ipv4_address"
          },
          "type": {
            "title": "type",
            "type": "string"
          }
        },
        "title": "dns_rr",
        "type": "object"
      },
      "domain": {
        "title": "domain",
        "type": "string"
      },
      "domain_discovery": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "domain": {
            "$ref": "#/components/schemas/domain"
          },
          "domain_whois": {
            "$ref": "#/components/schemas/domain_whois"
          },
          "ingested": {
            "format": "date-time",
            "title": "ingested",
            "type": "string"
          },
          "rr": {
            "items": {
              "$ref": "#/components/schemas/dns_rr"
            },
            "type": "array"
          },
          "similar_domains": {
            "items": {
              "$ref": "#/components/schemas/domain"
            },
            "type": "array"
          },
          "source": {
            "title": "source",
            "type": "string"
          },
          "timestamp": {
            "format": "date-time",
            "title": "timestamp",
            "type": "string"
          }
        },
        "title": "domain_discovery",
        "type": "object"
      },
      "domain_whois": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "created": {
            "format": "date-time",
            "title": "created",
            "type": "string"
          },
          "domain": {
            "$ref": "#/components/schemas/domain"
          },
          "expires": {
            "format": "date-time",
            "title": "expires",
            "type": "string"
          },
          "nameservers": {
            "items": {
              "$ref": "#/components/schemas/domain"
            },
            "type": "array"
          },
          "raw_text": {
            "title": "raw_text",
            "type": "string"
          },
          "registrant": {
            "$ref": "#/components/schemas/profile"
          },
          "registrar": {
            "$ref": "#/components/schemas/profile"
          },
          "source": {
            "title": "source",
            "type": "string"
          },
          "statuses": {
            "items": {
              "type": "string"
            },
            "type": "array"
          },
          "timestamp": {
            "format": "date-time",
            "title": "timestamp",
            "type": "string"
          },
          "updated": {
            "format": "date-time",
            "title": "updated",
            "type": "string"
          }
        },
        "title": "domain_whois",
        "type": "object"
      },
      "email_address": {
        "title": "email_address",
        "type": "string"
      },
      "file": {
        "properties": {
          "filename": {
            "$ref": "#/components/schemas/filename"
          }
        },
        "title": "file",
        "type": "object"
      },
      "filename": {
        "title": "filename",
        "type": "string"
      },
      "forum_post": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "author": {
            "$ref": "#/components/schemas/profile"
          },
          "board": {
            "$ref": "#/components/schemas/path"
          },
          "body": {
            "title": "body",
            "type": "string"
          },
          "forum": {
            "$ref": "#/components/schemas/service"
          },
          "in_reply_to": {
            "$ref": "#/components/schemas/message_id"
          },
          "ingested": {
            "format": "date-time",
            "title": "ingested",
            "type": "string"
          },
          "message_id": {
            "$ref": "#/components/schemas/message_id"
          },
          "original_id": {
            "title": "original_id",
            "type": "string"
          },
          "post_date": {
            "format": "date-time",
            "title": "post_date",
            "type": "string"
          },
          "source": {
            "title": "source",
            "type": "string"
          },
          "subject": {
            "title": "subject",
            "type": "string"
          },
          "timestamp": {
            "format": "date-time",
            "title": "timestamp",
            "type": "string"
          },
          "topic_id": {
            "title": "topic_id",
            "type": "string"
          }
        },
        "title": "forum_post",
        "type": "object"
      },
      "geo_location": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "bbox": {
            "$ref": "#/components/schemas/geo_shape"
          },
          "city": {
            "$ref": "#/components/schemas/city"
          },
          "continent_code": {
            "$ref": "#/components/schemas/continent_code"
          },
          "country": {
            "$ref": "#/components/schemas/country"
          },
          "country_code": {
            "$ref": "#/components/schemas/country_code"
          },
          "country_code_3": {
            "$ref": "#/components/schemas/country_code_3"
          },
          "location": {
            "$ref": "#/components/schemas/location_point"
          },
          "postal_code": {
            "$ref": "#/components/schemas/postal_code"
          },
          "region": {
            "$ref": "#/components/schemas/region"
          },
          "street_address": {
            "$ref": "#/components/schemas/street_address"
          }
        },
        "title": "geo_location",
        "type": "object"
      },
      "geo_shape": {
        "properties": {
          "coordinates": {
            "items": {
              "$ref": "#/components/schemas/location_point"
            },
            "type": "array"
          },
          "type": {
            "title": "type",
            "type": "string"
          }
        },
        "title": "geo_shape",
        "type": "object"
      },
      "hard_disk": {
        "properties": {
          "size": {
            "format": "int64",
            "title": "size",
            "type": "integer"
          }
        },
        "title": "hard_disk",
        "type": "object"
      },
      "hashes": {
        "properties": {
          "sha256": {
            "$ref": "#/components/schemas/sha256_hash"
          }
        },
        "title": "hashes",
        "type": "object"
      },
      "hashtag": {
        "title": "hashtag",
        "type": "string"
      },
      "host_access": {
        "properties": {
          "host_info": {
            "$ref": "#/components/schemas/host_info"
          },
          "service_account": {
            "$ref": "#/components/schemas/service_account"
          }
        },
        "title": "host_access",
        "type": "object"
      },
      "host_info": {
        "properties": {
          "av_installed": {
            "title": "av_installed",
            "type": "boolean"
          },
          "cpu": {
            "$ref": "#/components/schemas/cpu"
          },
          "files": {
            "items": {
              "$ref": "#/components/schemas/file"
            },
            "type": "array"
          },
          "geo_location": {
            "$ref": "#/components/schemas/geo_location"
          },
          "hard_disks": {
            "items": {
              "$ref": "#/components/schemas/hard_disk"
            },
            "type": "array"
          },
          "http_cookies": {
            "items": {
              "$ref": "#/components/schemas/http_cookie"
            },
            "type": "array"
          },
          "installed_memory": {
            "format": "int32",
            "title": "installed_memory",
            "type": "integer"
          },
          "installed_software": {
            "items": {
              "$ref": "#/components/schemas/product"
            },
            "type": "array"
          },
          "network_info": {
            "$ref": "#/components/schemas/network_info"
          },
          "number_user_accounts": {
            "format": "int32",
            "title": "number_user_accounts",
            "type": "integer"
          },
          "operating_system": {
            "$ref": "#/components/schemas/product"
          },
          "ransomware_installed": {
            "title": "ransomware_installed",
            "type": "boolean"
          },
          "service_accounts": {
            "items": {
              "$ref": "#/components/schemas/service_account"
            },
            "type": "array"
          },
          "sites_visited": {
            "items": {
              "$ref": "#/components/schemas/inet_location"
            },
            "type": "array"
          },
          "tags": {
            "items": {
              "$ref": "#/components/schemas/tag"
            },
            "type": "array"
          },
          "uptime": {
            "format": "int64",
            "title": "uptime",
            "type": "integer"
          },
          "virtualization": {
            "$ref": "#/components/schemas/product"
          }
        },
        "title": "host_info",
        "type": "object"
      },
      "http_cookie": {
        "properties": {
          "domain": {
            "$ref": "#/components/schemas/domain"
          }
        },
        "title": "http_cookie",
        "type": "object"
      },
      "icq_uin": {
        "title": "icq_uin",
        "type": "string"
      },
      "identity": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "dob": {
            "format": "date-time",
            "title": "dob",
            "type": "string"
          },
          "dob_format": {
            "title": "dob_format",
            "type": "string"
          },
          "first_name": {
            "$ref": "#/components/schemas/identity_name"
          },
          "last_name": {
            "$ref": "#/components/schemas/identity_name"
          },
          "mmn": {
            "title": "mmn",
            "type": "string"
          },
          "name": {
            "$ref": "#/components/schemas/identity_name"
          },
          "ssn": {
            "title": "ssn",
            "type": "string"
          }
        },
        "title": "identity",
        "type": "object"
      },
      "identity_name": {
        "title": "identity_name",
        "type": "string"
      },
      "inet_location": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "domain": {
            "$ref": "#/components/schemas/domain"
          },
          "ips_v4": {
            "items": {
              "$ref": "#/components/schemas/ipv4_address"
            },
            "type": "array"
          },
          "ips_v6": {
            "items": {
              "$ref": "#/components/schemas/ipv6_address"
            },
            "type": "array"
          },
          "path": {
            "$ref": "#/components/schemas/path"
          },
          "port": {
            "$ref": "#/components/schemas/inet_port"
          },
          "protocol": {
            "$ref": "#/components/schemas/network_protocol"
          },
          "url": {
            "$ref": "#/components/schemas/url"
          }
        },
        "title": "inet_location",
        "type": "object"
      },
      "inet_port": {
        "format": "int32",
        "title": "inet_port",
        "type": "integer"
      },
      "ipv4_address": {
        "format": "ip",
        "title": "ipv4_address",
        "type": "string"
      },
      "ipv6_address": {
        "format": "ip",
        "title": "ipv6_address",
        "type": "string"
      },
      "jid": {
        "title": "jid",
        "type": "string"
      },
      "language": {
        "title": "language",
        "type": "string"
      },
      "location_point": {
        "title": "location_point",
        "type": "string"
      },
      "message": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "body": {
            "title": "body",
            "type": "string"
          },
          "channel": {
            "$ref": "#/components/schemas/channel"
          },
          "edit_of": {
            "$ref": "#/components/schemas/message_id"
          },
          "in_reply_to": {
            "$ref": "#/components/schemas/message_id"
          },
          "ingested": {
            "format": "date-time",
            "title": "ingested",
            "type": "string"
          },
          "message_id": {
            "$ref": "#/components/schemas/message_id"
          },
          "messenger": {
            "$ref": "#/components/schemas/service"
          },
          "original_id": {
            "title": "original_id",
            "type": "string"
          },
          "parts": {
            "items": {
              "$ref": "#/components/schemas/mime_part"
            },
            "type": "array"
          },
          "sender": {
            "$ref": "#/components/schemas/profile"
          },
          "source": {
            "title": "source",
            "type": "string"
          },
          "timestamp": {
            "format": "date-time",
            "title": "timestamp",
            "type": "string"
          }
        },
        "title": "message",
        "type": "object"
      },
      "message_id": {
        "title": "message_id",
        "type": "string"
      },
      "mime_part": {
        "properties": {
          "body": {
            "title": "body",
            "type": "string"
          },
          "content_type": {
            "$ref": "#/components/schemas/content_type"
          },
          "filename": {
            "$ref": "#/components/schemas/filename"
          },
          "hashes": {
            "$ref": "#/components/schemas/hashes"
          }
        },
        "title": "mime_part",
        "type": "object"
      },
      "name": {
        "title": "name",
        "type": "string"
      },
      "nested_tweet": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "author": {
            "$ref": "#/components/schemas/profile"
          },
          "body": {
            "title": "body",
            "type": "string"
          },
          "display_text_range": {
            "items": {
              "format": "int32",
              "type": "integer"
            },
            "type": "array"
          },
          "geo_location": {
            "$ref": "#/components/schemas/geo_location"
          },
          "id_str": {
            "$ref": "#/components/schemas/message_id"
          },
          "in_reply_to": {
            "$ref": "#/components/schemas/message_id"
          },
          "is_quote": {
            "title": "is_quote",
            "type": "boolean"
          },
          "language": {
            "$ref": "#/components/schemas/language"
          },
          "place": {
            "$ref": "#/components/schemas/geo_location"
          },
          "possibly_sensitive": {
            "title": "possibly_sensitive",
            "type": "boolean"
          },
          "quote_count": {
            "format": "int32",
            "title": "quote_count",
            "type": "integer"
          },
          "quotes": {
            "$ref": "#/components/schemas/message_id"
          },
          "recipient": {
            "$ref": "#/components/schemas/profile"
          },
          "reply_count": {
            "format": "int32",
            "title": "reply_count",
            "type": "integer"
          },
          "retweet_count": {
            "format": "int32",
            "title": "retweet_count",
            "type": "integer"
          },
          "source": {
            "title": "source",
            "type": "string"
          },
          "timestamp": {
            "format": "date-time",
            "title": "timestamp",
            "type": "string"
          },
          "tweet_hashtags": {
            "items": {
              "$ref": "#/components/schemas/twitter_entity_hashtag"
            },
            "type": "array"
          },
          "tweet_media": {
            "items": {
              "$ref": "#/components/schemas/twitter_entity_media"
            },
            "type": "array"
          },
          "tweet_symbols": {
            "items": {
              "$ref": "#/components/schemas/twitter_entity_symbol"
            },
            "type": "array"
          },
          "tweet_urls": {
            "items": {
              "$ref": "#/components/schemas/twitter_entity_url"
            },
            "type": "array"
          },
          "tweet_user_mentions": {
            "items": {
              "$ref": "#/components/schemas/twitter_entity_mention"
            },
            "type": "array"
          }
        },
        "title": "nested_tweet",
        "type": "object"
      },
      "network_info": {
        "properties": {
          "ad_domain": {
            "$ref": "#/components/schemas/domain"
          },
          "blacklisted_by": {
            "items": {
              "$ref": "#/components/schemas/organization"
            },
            "type": "array"
          },
          "domain": {
            "$ref": "#/components/schemas/domain"
          },
          "download_bw": {
            "format": "float",
            "title": "download_bw",
            "type": "number"
          },
          "host_name": {
            "title": "host_name",
            "type": "string"
          },
          "ipv4": {
            "$ref": "#/components/schemas/ipv4_address"
          },
          "is_proxy": {
            "title": "is_proxy",
            "type": "boolean"
          },
          "isp": {
            "$ref": "#/components/schemas/organization"
          },
          "partial_ipv4": {
            "$ref": "#/components/schemas/ipv4_address"
          },
          "upload_bw": {
            "format": "float",
            "title": "upload_bw",
            "type": "number"
          }
        },
        "title": "network_info",
        "type": "object"
      },
      "network_protocol": {
        "title": "network_protocol",
        "type": "string"
      },
      "organization": {
        "title": "organization",
        "type": "string"
      },
      "password": {
        "properties": {
          "encrypted_text": {
            "title": "encrypted_text",
            "type": "string"
          },
          "encryption_algorithm": {
            "title": "encryption_algorithm",
            "type": "string"
          },
          "plain_text": {
            "$ref": "#/components/schemas/password_plaintext"
          }
        },
        "title": "password",
        "type": "object"
      },
      "password_plaintext": {
        "title": "password_plaintext",
        "type": "string"
      },
      "paste": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "author": {
            "$ref": "#/components/schemas/profile"
          },
          "body": {
            "title": "body",
            "type": "string"
          },
          "collection_ts": {
            "format": "date-time",
            "title": "collection_ts",
            "type": "string"
          },
          "ingested": {
            "format": "date-time",
            "title": "ingested",
            "type": "string"
          },
          "paste_id": {
            "title": "paste_id",
            "type": "string"
          },
          "service": {
            "$ref": "#/components/schemas/service"
          },
          "source": {
            "title": "source",
            "type": "string"
          },
          "source_location": {
            "$ref": "#/components/schemas/inet_location"
          },
          "timestamp": {
            "format": "date-time",
            "title": "timestamp",
            "type": "string"
          },
          "title": {
            "title": "title",
            "type": "string"
          }
        },
        "title": "paste",
        "type": "object"
      },
      "path": {
        "title": "path",
        "type": "string"
      },
      "payment_card": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "brand": {
            "$ref": "#/components/schemas/brand"
          },
          "expiry_date": {
            "format": "date-time",
            "title": "expiry_date",
            "type": "string"
          },
          "issuer": {
            "$ref": "#/components/schemas/organization"
          },
          "owner": {
            "$ref": "#/components/schemas/profile"
          },
          "partial_number_prefix": {
            "$ref": "#/components/schemas/bin"
          },
          "partial_number_suffix": {
            "title": "partial_number_suffix",
            "type": "string"
          },
          "product": {
            "$ref": "#/components/schemas/product"
          },
          "service_code": {
            "title": "service_code",
            "type": "string"
          },
          "type": {
            "title": "type",
            "type": "string"
          },
          "vbv": {
            "title": "vbv",
            "type": "string"
          }
        },
        "title": "payment_card",
        "type": "object"
      },
      "phone_number": {
        "title": "phone_number",
        "type": "string"
      },
      "postal_code": {
        "title": "postal_code",
        "type": "string"
      },
      "product": {
        "title": "product",
        "type": "string"
      },
      "product_batch": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "description": {
            "title": "description",
            "type": "string"
          },
          "name": {
            "$ref": "#/components/schemas/product_batch_name"
          },
          "release_date": {
            "format": "date-time",
            "title": "release_date",
            "type": "string"
          }
        },
        "title": "product_batch",
        "type": "object"
      },
      "product_batch_name": {
        "title": "product_batch_name",
        "type": "string"
      },
      "profile": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "contact": {
            "$ref": "#/components/schemas/contact"
          },
          "created": {
            "format": "date-time",
            "title": "created",
            "type": "string"
          },
          "identity": {
            "$ref": "#/components/schemas/identity"
          },
          "language": {
            "$ref": "#/components/schemas/language"
          },
          "telegram": {
            "$ref": "#/components/schemas/telegram_profile"
          },
          "twitter": {
            "$ref": "#/components/schemas/twitter_profile"
          }
        },
        "title": "profile",
        "type": "object"
      },
      "region": {
        "title": "region",
        "type": "string"
      },
      "security_question": {
        "properties": {
          "answer": {
            "title": "answer",
            "type": "string"
          },
          "question": {
            "title": "question",
            "type": "string"
          }
        },
        "title": "security_question",
        "type": "object"
      },
      "service": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "description": {
            "title": "description",
            "type": "string"
          },
          "geo_location": {
            "$ref": "#/components/schemas/geo_location"
          },
          "id": {
            "title": "id",
            "type": "string"
          },
          "inet_location": {
            "$ref": "#/components/schemas/inet_location"
          },
          "name": {
            "$ref": "#/components/schemas/service_name"
          },
          "software": {
            "$ref": "#/components/schemas/product"
          }
        },
        "title": "service",
        "type": "object"
      },
      "service_account": {
        "properties": {
          "created_at": {
            "format": "date-time",
            "title": "created_at",
            "type": "string"
          },
          "login": {
            "title": "login",
            "type": "string"
          },
          "original_id": {
            "title": "original_id",
            "type": "string"
          },
          "password": {
            "$ref": "#/components/schemas/password"
          },
          "profile": {
            "$ref": "#/components/schemas/profile"
          },
          "security_questions": {
            "items": {
              "$ref": "#/components/schemas/security_question"
            },
            "type": "array"
          },
          "service": {
            "$ref": "#/components/schemas/service"
          },
          "service_account_info": {
            "$ref": "#/components/schemas/service_account_info"
          }
        },
        "title": "service_account",
        "type": "object"
      },
      "service_account_info": {
        "properties": {
          "balance": {
            "format": "float",
            "title": "balance",
            "type": "number"
          },
          "currency": {
            "title": "currency",
            "type": "string"
          },
          "last_transaction_ts": {
            "format": "date-time",
            "title": "last_transaction_ts",
            "type": "string"
          },
          "linked_payment_method_description": {
            "title": "linked_payment_method_description",
            "type": "string"
          },
          "points": {
            "format": "int32",
            "title": "points",
            "type": "integer"
          }
        },
        "title": "service_account_info",
        "type": "object"
      },
      "service_name": {
        "title": "service_name",
        "type": "string"
      },
      "sha256_hash": {
        "title": "sha256_hash",
        "type": "string"
      },
      "shop_listing": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "batch": {
            "$ref": "#/components/schemas/product_batch"
          },
          "currency": {
            "title": "currency",
            "type": "string"
          },
          "data_availability": {
            "$ref": "#/components/schemas/data_availability"
          },
          "description": {
            "title": "description",
            "type": "string"
          },
          "host_access": {
            "$ref": "#/components/schemas/host_access"
          },
          "host_info": {
            "$ref": "#/components/schemas/host_info"
          },
          "ingested": {
            "format": "date-time",
            "title": "ingested",
            "type": "string"
          },
          "is_verified": {
            "title": "is_verified",
            "type": "boolean"
          },
          "item_qty": {
            "format": "int32",
            "title": "item_qty",
            "type": "integer"
          },
          "item_sold": {
            "format": "int32",
            "title": "item_sold",
            "type": "integer"
          },
          "item_type": {
            "title": "item_type",
            "type": "string"
          },
          "listing_id": {
            "title": "listing_id",
            "type": "string"
          },
          "listing_url": {
            "$ref": "#/components/schemas/inet_location"
          },
          "payment_card": {
            "$ref": "#/components/schemas/payment_card"
          },
          "price": {
            "format": "float",
            "title": "price",
            "type": "number"
          },
          "profile": {
            "$ref": "#/components/schemas/profile"
          },
          "publish_ts": {
            "format": "date-time",
            "title": "publish_ts",
            "type": "string"
          },
          "seller": {
            "$ref": "#/components/schemas/profile"
          },
          "service_account": {
            "$ref": "#/components/schemas/service_account"
          },
          "shop": {
            "$ref": "#/components/schemas/service"
          },
          "source": {
            "title": "source",
            "type": "string"
          },
          "timestamp": {
            "format": "date-time",
            "title": "timestamp",
            "type": "string"
          },
          "title": {
            "title": "title",
            "type": "string"
          },
          "verification_ts": {
            "format": "date-time",
            "title": "verification_ts",
            "type": "string"
          }
        },
        "title": "shop_listing",
        "type": "object"
      },
      "street": {
        "title": "street",
        "type": "string"
      },
      "street_address": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "number": {
            "format": "int32",
            "title": "number",
            "type": "integer"
          },
          "street": {
            "$ref": "#/components/schemas/street"
          }
        },
        "title": "street_address",
        "type": "object"
      },
      "tag": {
        "properties": {
          "location_point": {
            "$ref": "#/components/schemas/location_point"
          },
          "name": {
            "$ref": "#/components/schemas/name"
          },
          "value": {
            "title": "value",
            "type": "string"
          }
        },
        "title": "tag",
        "type": "object"
      },
      "telegram_profile": {
        "properties": {
          "name": {
            "$ref": "#/components/schemas/telegram_user_name"
          },
          "user_id": {
            "format": "int64",
            "title": "user_id",
            "type": "integer"
          }
        },
        "title": "telegram_profile",
        "type": "object"
      },
      "telegram_user_name": {
        "title": "telegram_user_name",
        "type": "string"
      },
      "tweet": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "author": {
            "$ref": "#/components/schemas/profile"
          },
          "body": {
            "title": "body",
            "type": "string"
          },
          "display_text_range": {
            "items": {
              "format": "int32",
              "type": "integer"
            },
            "type": "array"
          },
          "geo_location": {
            "$ref": "#/components/schemas/geo_location"
          },
          "id_str": {
            "$ref": "#/components/schemas/message_id"
          },
          "in_reply_to": {
            "$ref": "#/components/schemas/message_id"
          },
          "ingested": {
            "format": "date-time",
            "title": "ingested",
            "type": "string"
          },
          "is_quote": {
            "title": "is_quote",
            "type": "boolean"
          },
          "language": {
            "$ref": "#/components/schemas/language"
          },
          "place": {
            "$ref": "#/components/schemas/geo_location"
          },
          "possibly_sensitive": {
            "title": "possibly_sensitive",
            "type": "boolean"
          },
          "quote_count": {
            "format": "int32",
            "title": "quote_count",
            "type": "integer"
          },
          "quoted_status": {
            "$ref": "#/components/schemas/nested_tweet"
          },
          "quotes": {
            "$ref": "#/components/schemas/message_id"
          },
          "recipient": {
            "$ref": "#/components/schemas/profile"
          },
          "reply_count": {
            "format": "int32",
            "title": "reply_count",
            "type": "integer"
          },
          "retweet_count": {
            "format": "int32",
            "title": "retweet_count",
            "type": "integer"
          },
          "retweeted": {
            "$ref": "#/components/schemas/message_id"
          },
          "retweeted_status": {
            "$ref": "#/components/schemas/nested_tweet"
          },
          "source": {
            "title": "source",
            "type": "string"
          },
          "timestamp": {
            "format": "date-time",
            "title": "timestamp",
            "type": "string"
          },
          "tweet_hashtags": {
            "items": {
              "$ref": "#/components/schemas/twitter_entity_hashtag"
            },
            "type": "array"
          },
          "tweet_media": {
            "items": {
              "$ref": "#/components/schemas/twitter_entity_media"
            },
            "type": "array"
          },
          "tweet_symbols": {
            "items": {
              "$ref": "#/components/schemas/twitter_entity_symbol"
            },
            "type": "array"
          },
          "tweet_urls": {
            "items": {
              "$ref": "#/components/schemas/twitter_entity_url"
            },
            "type": "array"
          },
          "tweet_user_mentions": {
            "items": {
              "$ref": "#/components/schemas/twitter_entity_mention"
            },
            "type": "array"
          }
        },
        "title": "tweet",
        "type": "object"
      },
      "twitter_entity_hashtag": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "hashtag": {
            "$ref": "#/components/schemas/hashtag"
          },
          "indices": {
            "items": {
              "format": "int32",
              "type": "integer"
            },
            "type": "array"
          }
        },
        "title": "twitter_entity_hashtag",
        "type": "object"
      },
      "twitter_entity_media": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "display_location": {
            "$ref": "#/components/schemas/inet_location"
          },
          "expanded_location": {
            "$ref": "#/components/schemas/inet_location"
          },
          "indices": {
            "items": {
              "format": "int32",
              "type": "integer"
            },
            "type": "array"
          },
          "inet_location": {
            "$ref": "#/components/schemas/inet_location"
          },
          "media_id_str": {
            "title": "media_id_str",
            "type": "string"
          },
          "media_location": {
            "$ref": "#/components/schemas/inet_location"
          },
          "media_type": {
            "title": "media_type",
            "type": "string"
          },
          "source_status_id_str": {
            "$ref": "#/components/schemas/message_id"
          }
        },
        "title": "twitter_entity_media",
        "type": "object"
      },
      "twitter_entity_mention": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "indices": {
            "items": {
              "format": "int32",
              "type": "integer"
            },
            "type": "array"
          },
          "mentioned_user": {
            "$ref": "#/components/schemas/profile"
          }
        },
        "title": "twitter_entity_mention",
        "type": "object"
      },
      "twitter_entity_symbol": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "indices": {
            "items": {
              "format": "int32",
              "type": "integer"
            },
            "type": "array"
          },
          "text": {
            "title": "text",
            "type": "string"
          }
        },
        "title": "twitter_entity_symbol",
        "type": "object"
      },
      "twitter_entity_url": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "display_location": {
            "$ref": "#/components/schemas/inet_location"
          },
          "expanded_location": {
            "$ref": "#/components/schemas/inet_location"
          },
          "indices": {
            "items": {
              "format": "int32",
              "type": "integer"
            },
            "type": "array"
          },
          "inet_location": {
            "$ref": "#/components/schemas/inet_location"
          }
        },
        "title": "twitter_entity_url",
        "type": "object"
      },
      "twitter_handle": {
        "title": "twitter_handle",
        "type": "string"
      },
      "twitter_profile": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "description": {
            "title": "description",
            "type": "string"
          },
          "followers_count": {
            "format": "int32",
            "title": "followers_count",
            "type": "integer"
          },
          "id_str": {
            "title": "id_str",
            "type": "string"
          },
          "profile_background_location": {
            "$ref": "#/components/schemas/inet_location"
          },
          "profile_banner_location": {
            "$ref": "#/components/schemas/inet_location"
          },
          "profile_image_location": {
            "$ref": "#/components/schemas/inet_location"
          },
          "protected": {
            "title": "protected",
            "type": "boolean"
          },
          "statuses_count": {
            "format": "int32",
            "title": "statuses_count",
            "type": "integer"
          },
          "user_location": {
            "title": "user_location",
            "type": "string"
          },
          "verified": {
            "title": "verified",
            "type": "boolean"
          }
        },
        "title": "twitter_profile",
        "type": "object"
      },
      "url": {
        "title": "url",
        "type": "string"
      },
      "web_content_publish": {
        "properties": {
          "__id": {
            "title": "__id",
            "type": "string"
          },
          "__type": {
            "title": "__type",
            "type": "string"
          },
          "author": {
            "$ref": "#/components/schemas/profile"
          },
          "collection_ts": {
            "format": "date-time",
            "title": "collection_ts",
            "type": "string"
          },
          "inet_location": {
            "$ref": "#/components/schemas/inet_location"
          },
          "ingested": {
            "format": "date-time",
            "title": "ingested",
            "type": "string"
          },
          "language": {
            "$ref": "#/components/schemas/language"
          },
          "links": {
            "items": {
              "$ref": "#/components/schemas/inet_location"
            },
            "type": "array"
          },
          "raw_text": {
            "title": "raw_text",
            "type": "string"
          },
          "source": {
            "title": "source",
            "type": "string"
          },
          "text": {
            "title": "text",
            "type": "string"
          },
          "timestamp": {
            "format": "date-time",
            "title": "timestamp",
            "type": "string"
          },
          "title": {
            "title": "title",
            "type": "string"
          }
        },
        "title": "web_content_publish",
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
    "/docs/{type}/{id}": {
      "get": {
        "description": "",
        "operationId": "get-docs-type-id",
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
            "description": "The accept type for the response",
            "in": "header",
            "name": "Accept",
            "required": true,
            "schema": {
              "default": "application/json",
              "type": "string"
            }
          },
          {
            "description": "If false, then the document's topics and labels are not returned in the response body.",
            "in": "query",
            "name": "refs",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "description": "Truncates document fields to the given length using unicode ellipsis (\\x2026) to indicate truncation",
            "in": "query",
            "name": "truncate",
            "schema": {
              "type": "integer"
            }
          },
          {
            "description": "If true, any HTML content in the alert is sanitized to ensure it does not potentially contain malicious tags. If not used, be careful when rendering/using the alert/doc content. This param can also be specified as a json path in the alert document to sanitize and may be repeated in this case.",
            "in": "query",
            "name": "sanitize",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "The document type to fetch",
            "in": "path",
            "name": "type",
            "required": true,
            "schema": {
              "enum": [
                "document_analysis",
                "domain_discovery",
                "email_analysis",
                "forum_post",
                "paste",
                "shop_listing",
                "tweet",
                "web_content_publish"
              ],
              "type": "string"
            }
          },
          {
            "description": "The document ID to fetch",
            "in": "path",
            "name": "id",
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
                  "$ref": "#/components/schemas/Doc"
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
                      "message": "Internal Error"
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
        "summary": "Retrieve an indexed document by its type and ID",
        "tags": [
          "DTM Docs"
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
      "name": "DTM Docs"
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

← [DTM Docs](../dtm-docs.md) · [up](../README.md) · [Fetch the labels for an existing document](get-docs-type-id-labels.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-docs-type-id>.*
