---
title: "List alerts"
source: https://gtidocs.virustotal.com/reference/get-alerts
slug: get-alerts
section: reference
group: "DTM (DIGITAL THREAT MONITORING)"
updatedAt: 2025-09-25T01:37:02.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [DTM (DIGITAL THREAT MONITORING)](../README.md) › [DTM Alerts](../dtm-alerts.md) › List alerts

---

# list-alerts

Get alerts for the current organization. This API uses the next link header to provide the URI of the next page of results. When fetching subsequent pages, only use the link header URI.

# openapi-definition

```json
{
  "components": {
    "schemas": {
      "AggregatedAlertRef": {
        "description": "Metadata about an aggregated alert that belongs to a parent alert bucket.",
        "properties": {
          "created_at": {
            "description": "The time the child alert was created.",
            "format": "date-time",
            "readOnly": true,
            "type": "string"
          },
          "doc_type": {
            "description": "The document type of the child alert.",
            "readOnly": true,
            "type": "string"
          },
          "has_analysis": {
            "description": "A boolean indicating if the child alert has analysis or file attachments.",
            "readOnly": true,
            "type": "boolean"
          },
          "id": {
            "description": "The ID of the aggregated chid alert.",
            "readOnly": true,
            "type": "string"
          },
          "monitor_id": {
            "description": "The ID of the monitor that generated the child alert.",
            "readOnly": true,
            "type": "string"
          },
          "status": {
            "description": "The status of the child alert.",
            "enum": [
              "new",
              "read",
              "escalated",
              "in_progress",
              "closed",
              "no_action_required",
              "duplicate",
              "not_relevant",
              "tracked_external"
            ],
            "readOnly": true,
            "type": "string"
          },
          "tags": {
            "description": "The tags of the child alert.",
            "items": {
              "type": "string"
            },
            "maxItems": 100,
            "type": "array"
          }
        },
        "title": "Aggregated Alert Reference",
        "type": "object"
      },
      "Alert": {
        "description": "An alert is created for each monitor that has at least one matching condition. The alert includes details and context regarding the (raw) document matched, the topics/labels matched from the monitor, as well as the labels and topics identified within the (raw) document.",
        "properties": {
          "aggregated_added_at": {
            "description": "Only applicable to alert buckets, this field is the timestamp at which the most recent child alert was aggregated into the bucket.",
            "format": "date-time",
            "readOnly": true,
            "type": "string"
          },
          "aggregated_alert_count": {
            "description": "Only applicable to alert buckets, and indicates the number of alerts aggregated into this bucket alert.",
            "readOnly": true,
            "type": "integer"
          },
          "aggregated_alert_count_new": {
            "description": "Only applicable to alert buckets, and indicates the number of alerts with new status in this bucket alert.",
            "readOnly": true,
            "type": "integer"
          },
          "aggregated_alerts": {
            "description": "Only applciable to alert buckets, this field contains metadata about each child alert aggregated into this bucket.",
            "items": {
              "$ref": "#/components/schemas/AggregatedAlertRef"
            },
            "readOnly": true,
            "type": "array"
          },
          "aggregated_under_id": {
            "description": "Only applicable to child alerts that are aggregated into a bucket, this field is the ID of the parent bucket alert.",
            "readOnly": true,
            "type": "string"
          },
          "ai_doc_summary": {
            "description": "If the group has the AI features enabled, this field will contain the AI analysis summary.",
            "readOnly": true,
            "type": "string"
          },
          "alert_summary": {
            "description": "The summary of the alert.",
            "readOnly": true,
            "type": "string"
          },
          "alert_type": {
            "description": "The type of this alert.",
            "enum": [
              "Compromised Credentials",
              "Domain Discovery",
              "Forum Post",
              "Message",
              "Paste",
              "Shop Listing",
              "Tweet",
              "Web Content"
            ],
            "readOnly": true,
            "type": "string"
          },
          "analysis": {
            "description": "If analysis has been added to the alert, then this property contains the analysis text.",
            "example": "Sample analysis text and can be markdown format.",
            "readOnly": false,
            "type": "string"
          },
          "attachments": {
            "description": "File attachments associated with the alert as part of the alert's analysis.",
            "items": {
              "$ref": "#/components/schemas/FileAttachment"
            },
            "readOnly": true,
            "type": "array"
          },
          "created_at": {
            "description": "The time this alert was created at.",
            "example": "2021-08-23T18:02:53Z",
            "readOnly": true,
            "type": "string"
          },
          "doc": {
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
            ],
            "readOnly": true
          },
          "doc_matches": {
            "description": "Any document matches generated for this alert.",
            "items": {
              "$ref": "#/components/schemas/Doc_match"
            },
            "readOnly": true,
            "type": "array"
          },
          "doc_url": {
            "description": "The URL to the document that triggered this alert.",
            "format": "uri",
            "readOnly": true,
            "type": "string"
          },
          "email_sent_at": {
            "description": "If email notifications are used for this alert, the timestamp the alert email was sent.",
            "readOnly": true,
            "type": "string"
          },
          "has_analysis": {
            "description": "True if the alert has analysis text or file attachments and false otherwise.",
            "readOnly": true,
            "type": "boolean"
          },
          "id": {
            "description": "The ID of the alert.",
            "example": "c4hu5j8mhcmiku5g7ieg",
            "readOnly": true,
            "type": "string"
          },
          "indicator_attributions": {
            "items": {
              "$ref": "#/components/schemas/IndicatorAttribution"
            },
            "readOnly": true,
            "type": "array"
          },
          "indicator_mscore": {
            "maximum": 100,
            "minimum": 0,
            "readOnly": true,
            "type": "integer"
          },
          "label_matches": {
            "description": "Any labels that matched for this alert.",
            "items": {
              "$ref": "#/components/schemas/Label_match"
            },
            "readOnly": true,
            "type": "array"
          },
          "labels": {
            "description": "The labels itentified in the document that triggered this alert.",
            "items": {
              "$ref": "#/components/schemas/Label"
            },
            "readOnly": true,
            "type": "array"
          },
          "labels_url": {
            "description": "The URL to the labels identified in the document that triggered this alert.",
            "format": "uri",
            "readOnly": true,
            "type": "string"
          },
          "meets_password_policy": {
            "description": "If the monitor that created the alert includes a password policy, this value indicates if the alert (when applicable) has a password that meets the policy.",
            "readOnly": true,
            "type": "boolean"
          },
          "monitor_id": {
            "description": "The ID of the monitor that generated this alert.",
            "example": "c4fbb52bqsiatib6i4gg",
            "readOnly": true,
            "type": "string"
          },
          "monitor_name": {
            "description": "The name of the monitor that generated this alert.",
            "readOnly": true,
            "type": "string"
          },
          "monitor_version": {
            "description": "The version of the monitor that generated this alert.",
            "readOnly": true,
            "type": "integer"
          },
          "relevance_class": {
            "description": "The relevance class suggested for this alert.",
            "enum": [
              "benign",
              "malicious"
            ],
            "type": "string"
          },
          "relevance_probability": {
            "description": "The relevance probability suggested for this alert.",
            "readOnly": true,
            "type": "number"
          },
          "status": {
            "description": "The status of this alert.",
            "enum": [
              "new",
              "closed",
              "read",
              "escalated",
              "in_progress",
              "no_action_required",
              "duplicate",
              "not_relevant",
              "tracked_external"
            ],
            "type": "string"
          },
          "tags": {
            "description": "The tags set for this alert.",
            "items": {
              "type": "string"
            },
            "readOnly": false,
            "type": "array"
          },
          "title": {
            "description": "The title of this alert.",
            "readOnly": true,
            "type": "string"
          },
          "topic_matches": {
            "description": "Any topic matches the monitor generated for this alert.",
            "items": {
              "$ref": "#/components/schemas/Topic_match"
            },
            "readOnly": true,
            "type": "array"
          },
          "topics": {
            "description": "The topics that were identified in the document that triggered this alert.",
            "items": {
              "$ref": "#/components/schemas/Topic"
            },
            "readOnly": true,
            "type": "array"
          },
          "topics_url": {
            "description": "The URL to the toics identified in the document that triggered this alert.",
            "format": "uri",
            "readOnly": true,
            "type": "string"
          },
          "updated_at": {
            "description": "The time this alert was last updated at.",
            "example": "2021-08-23T18:02:53Z",
            "readOnly": true,
            "type": "string"
          }
        },
        "required": [
          "id",
          "monitor_id",
          "created_at",
          "updated_at",
          "topic_matches",
          "doc_matches",
          "doc_url",
          "labels_url",
          "topics_url",
          "status",
          "alert_type",
          "alert_summary",
          "title",
          "label_matches",
          "indicator_attributions",
          "monitor_version"
        ],
        "title": "Alert",
        "type": "object"
      },
      "Alerts": {
        "description": "A list of alerts.",
        "properties": {
          "alerts": {
            "items": {
              "$ref": "#/components/schemas/Alert"
            },
            "readOnly": true,
            "type": "array"
          }
        },
        "required": [
          "alerts"
        ],
        "title": "Alerts",
        "type": "object"
      },
      "Doc_match": {
        "description": "A Doc Match represents the doc query that was matched for a monitor alert.",
        "properties": {
          "locations": {
            "description": "A list of locations for the match.",
            "items": {
              "$ref": "#/components/schemas/Location"
            },
            "minItems": 1,
            "readOnly": true,
            "type": "array"
          },
          "match_path": {
            "description": "The JSON field path of the match.",
            "example": "tweet.body",
            "readOnly": true,
            "type": "string"
          }
        },
        "required": [
          "match_path",
          "locations"
        ],
        "title": "Doc Match",
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
      "FileAttachment": {
        "description": "Metadata describing a file attachment.",
        "properties": {
          "content_type": {
            "description": "The content type of the file attachment.",
            "readOnly": true,
            "type": "string"
          },
          "created_at": {
            "description": "The time the file attachment was created.",
            "format": "date-time",
            "readOnly": true,
            "type": "string"
          },
          "created_by_user_id": {
            "description": "The user ID that created the attachment.",
            "readOnly": true,
            "type": "string"
          },
          "filesize_bytes": {
            "description": "The size of the attachment measured in bytes.",
            "readOnly": true,
            "type": "integer"
          },
          "id": {
            "description": "The ID of the file attachment.",
            "readOnly": true,
            "type": "string"
          },
          "name": {
            "description": "The file name of the attachment.",
            "readOnly": true,
            "type": "string"
          }
        },
        "title": "File Attachment",
        "type": "object"
      },
      "IndicatorAttribution": {
        "description": "Attributions assodicated with an indicator.",
        "properties": {
          "id": {
            "readOnly": true,
            "type": "string"
          },
          "name": {
            "readOnly": true,
            "type": "string"
          },
          "type": {
            "readOnly": true,
            "type": "string"
          }
        },
        "required": [
          "id",
          "name",
          "type"
        ],
        "title": "Indicator Attribution",
        "type": "object",
        "x-stoplight": {
          "id": "afpk4k0z11ag1"
        }
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
      "Label_match": {
        "description": "Indication of a label matching a monitor condition for label topics",
        "properties": {
          "label_id": {
            "description": "The ID of the identified label that was matched.",
            "type": "string"
          },
          "value": {
            "description": "The label value that was matched.",
            "type": "string"
          }
        },
        "required": [
          "label_id",
          "value"
        ],
        "title": "Label Match",
        "type": "object"
      },
      "Location": {
        "description": "Location represents a text location as specified by its start and end index and its matching value.",
        "properties": {
          "match_path": {
            "readOnly": true,
            "type": "string"
          },
          "offsets": {
            "description": "The offsets in the raw document where the value was identified.",
            "items": {
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "readOnly": true,
            "type": "array"
          },
          "value": {
            "description": "The value that was identified.",
            "maxLength": 1000,
            "readOnly": true,
            "type": "string"
          }
        },
        "required": [
          "offsets",
          "value"
        ],
        "title": "Location",
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
      "Topic_match": {
        "description": "A topic match indicates which search and topic was matched for a monitor alert.",
        "properties": {
          "topic_id": {
            "description": "The ID of the topic corresponding to this match.",
            "example": "1405131d-1d15-4d45-ae42-5535865b3d16",
            "readOnly": true,
            "type": "string"
          },
          "value": {
            "description": "The value of the topic that matched.",
            "example": "somevalue",
            "readOnly": true,
            "type": "string"
          }
        },
        "required": [
          "topic_id",
          "value"
        ],
        "title": "Topic Match",
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
    "/alerts": {
      "get": {
        "description": "",
        "operationId": "get-alerts",
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
            "description": "The alert field name to sort the response alerts by.",
            "in": "query",
            "name": "sort",
            "schema": {
              "default": "created_at",
              "enum": [
                "id",
                "created_at",
                "updated_at",
                "monitor_id"
              ],
              "example": "updated_at",
              "type": "string"
            }
          },
          {
            "description": "The order used to sort the response alerts field by.",
            "in": "query",
            "name": "order",
            "schema": {
              "default": "desc",
              "enum": [
                "asc",
                "desc"
              ],
              "example": "asc",
              "type": "string"
            }
          },
          {
            "description": "The number of alerts to return in each page. Max value of 25.",
            "in": "query",
            "name": "size",
            "schema": {
              "default": 10,
              "example": 20,
              "type": "integer",
              "maximum": 25,
              "minimum": 0
            }
          },
          {
            "description": "Only return alerts for the given monitor ID. This parameter can be specified multiple times to filter on more than one monitor ID.",
            "in": "query",
            "name": "monitor_id",
            "schema": {
              "example": "c4fcpm2bqsiatib6i4h0",
              "type": "string"
            }
          },
          {
            "description": "If false, doc, labels, and topics are not returned in the response body.",
            "in": "query",
            "name": "refs",
            "schema": {
              "default": true,
              "type": "boolean"
            }
          },
          {
            "description": "If true, then any links in the alert doc are sanitized and replaced.",
            "in": "query",
            "name": "replace_links",
            "schema": {
              "default": false,
              "type": "boolean"
            }
          },
          {
            "description": "If true, then the monitor's name that created the alert is returned in the alert response body.",
            "in": "query",
            "name": "monitor_name",
            "schema": {
              "default": false,
              "type": "boolean"
            }
          },
          {
            "description": "If true, then only alerts that have analysis are returned. An alert has anlysis if it has either analysis text or analysis file attachments.",
            "in": "query",
            "name": "has_analysis",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "description": "If true, then alert buckets are returned for aggregated alerts. If false, then bucket format is not returned, but instead all child aggregated alerts are.",
            "in": "query",
            "name": "buckets",
            "schema": {
              "default": false,
              "type": "boolean"
            }
          },
          {
            "description": "When listing alerts by date range, since defines the starting date in RFC3339 format",
            "in": "query",
            "name": "since",
            "schema": {
              "format": "date-time",
              "type": "string"
            }
          },
          {
            "description": "When listing alerts by date range, until defines the ending date in RFC3339 format",
            "in": "query",
            "name": "until",
            "schema": {
              "format": "date-time",
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
            "description": "Filter alerts by their status. This parameter can be specified multiple times.",
            "in": "query",
            "name": "status",
            "schema": {
              "enum": [
                "new",
                "read",
                "escalated",
                "in_progress",
                "closed",
                "no_action_required",
                "duplicate",
                "not_relevant",
                "tracked_external"
              ],
              "type": "string"
            }
          },
          {
            "description": "Filter alerts by alert type. This parameter can be specified multiple times.",
            "in": "query",
            "name": "alert_type",
            "schema": {
              "enum": [
                "Compromised Credentials",
                "Domain Discovery",
                "Forum Post",
                "Message",
                "Paste",
                "Shop Listing",
                "Tweet",
                "Web Content"
              ],
              "type": "string"
            }
          },
          {
            "description": "Search alert and triggering doc contents based on a simple Lucene query string including 1 or more text values separated by AND or OR.",
            "in": "query",
            "name": "search",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "If specified, then only alerts that have the given match value are returned. This parameter can be repeated multiple times.",
            "in": "query",
            "name": "match_value",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Filter alerts by tag(s). This parameter can be used more than once to filter on multiple tags.",
            "in": "query",
            "name": "tags",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "When using the search parameter, its value can be base64 encoded in which case search_encoding indicates the value encoding type.",
            "in": "query",
            "name": "search_encoding",
            "schema": {
              "enum": [
                "base64"
              ],
              "type": "string"
            }
          },
          {
            "description": "Return alerts that have the given severity. This parameter can be repeated multiple times.",
            "in": "query",
            "name": "severity",
            "schema": {
              "enum": [
                "high",
                "medium",
                "low"
              ],
              "type": "string"
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
            "description": "Filter alerts with mscores greater than or equal to the given value.",
            "in": "query",
            "name": "mscore_gte",
            "schema": {
              "maximum": 100,
              "minimum": 0,
              "type": "integer"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "examples": {
                  "list-alerts": {
                    "value": {
                      "alerts": [
                        {
                          "alert_summary": "See alert content for details",
                          "alert_type": "Domain Discovery",
                          "analysis": "Sample analysis text.",
                          "attachments": [
                            {
                              "content_type": "image/png",
                              "created_at": "2024-02-02T14:24:15.841001769Z",
                              "created_by_user_id": "b732d502-f8d3-103a-8371-ddaa058454c8",
                              "filesize_bytes": 4262,
                              "id": "cmufm3qec7l1h694o100",
                              "name": "Screenshot 2024-01-31 3.06.56 PM.png"
                            }
                          ],
                          "confidence": 0.5,
                          "created_at": "2024-01-16T20:11:42.468Z",
                          "doc": {
                            "__id": "d35713ca-707d-436d-84a5-220e3ae75b61",
                            "__type": "domain_discovery",
                            "domain": "mwise.mandiant.com",
                            "ingested": "2024-01-16T20:10:03Z",
                            "rr": [
                              {
                                "rdata_domain": "elb-2975-mwise-mandiant-com.swoogo.com",
                                "type": "CNAME"
                              }
                            ],
                            "source": "ctl-certstream",
                            "timestamp": "2024-01-16T20:02:00Z"
                          },
                          "doc_matches": [],
                          "doc_url": "https://api.intelligence.mandiant.com/v4/dtm/docs/domain_discovery/d35713ca-707d-436d-84a5-220e3ae75b61",
                          "email_sent_at": "",
                          "has_analysis": false,
                          "id": "cmje5vmbenj434u3nnvg",
                          "label_matches": [],
                          "labels_url": "https://api.intelligence.mandiant.com/v4/dtm/docs/domain_discovery/d35713ca-707d-436d-84a5-220e3ae75b61/labels",
                          "monitor_id": "clb20lirrtn3gnjncs40",
                          "monitor_version": 1,
                          "severity": "medium",
                          "status": "escalated",
                          "tags": [],
                          "title": "Suspicious domain \"mwise.mandiant.com\" similar to \"mandiant.com\"",
                          "topic_matches": [
                            {
                              "offsets": [
                                6,
                                18
                              ],
                              "term": "mandiant.com",
                              "topic_id": "95eed43c-8f51-49ce-a1d8-f88b5441cec3",
                              "value": "mwise.mandiant.com"
                            },
                            {
                              "topic_id": "doc_type:domain_discovery",
                              "value": "domain_discovery"
                            }
                          ],
                          "topics": [
                            {
                              "entity_locations": [
                                {
                                  "element_path": "domain",
                                  "offsets": [
                                    0,
                                    18
                                  ]
                                }
                              ],
                              "extractor": "dtm-ma",
                              "extractor_version": "0.1.302",
                              "id": "95eed43c-8f51-49ce-a1d8-f88b5441cec3",
                              "type": "domain",
                              "value": "mwise.mandiant.com"
                            },
                            {
                              "entity_locations": [
                                {
                                  "element_path": "rr[0].rdata_domain",
                                  "offsets": [
                                    0,
                                    38
                                  ]
                                }
                              ],
                              "extractor": "dtm-ma",
                              "extractor_version": "0.1.302",
                              "id": "6c2cbf1b-4116-4533-80d0-1bf6b0dcf7bb",
                              "type": "domain",
                              "value": "elb-2975-mwise-mandiant-com.swoogo.com"
                            }
                          ],
                          "topics_url": "https://api.intelligence.mandiant.com/v4/dtm/docs/domain_discovery/d35713ca-707d-436d-84a5-220e3ae75b61/topics",
                          "updated_at": "2024-01-20T11:17:36.261Z"
                        }
                      ]
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Alerts"
                }
              }
            },
            "description": "OK",
            "headers": {
              "Content-Type": {
                "description": "The content type of the response body.",
                "schema": {
                  "default": "application/json",
                  "example": "application/json",
                  "type": "string"
                }
              },
              "Link": {
                "description": "If another page of results is available for pagination, the Link header will contain the URI used to fetch the next page.",
                "schema": {
                  "example": "<https://api.intelligence.mandiant.com/v4/dtm/alerts?page=c52e5bc1hrv40t8d0gvg>; rel=\"next\"",
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
        "summary": "List alerts",
        "tags": [
          "DTM Alerts"
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
      "name": "DTM Alerts"
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

← [DTM Alerts](../dtm-alerts.md) · [up](../README.md) · [Get an existing alert by its ID](get-alerts-id.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-alerts>.*
