---
title: "Get Issue point in time"
source: https://gtidocs.virustotal.com/reference/get_time-series-point-in-time-issues-uid
slug: get_time-series-point-in-time-issues-uid
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:24.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Time Series](../time-series.md) › Get Issue point in time

---

# get-issue-point-in-time

Returns issue details for issues associated with an entity at a specific point in time.

| key | Format | **Notes** |
| --- | --- | --- |
| property | status, last_seen | required |
| property_end_value_filter | string | optional  <br>If provided, the result set will be filtered to only return results where the property value at the end point in time is equal to the provided filter value. |
| transition | changed, unchanged, stagnated | required  <br>  <br>changed means the property had more than one value over the time period  <br>  <br>Example: 1, 2, 3, 4  <br>  <br>unchanged means the property had only one value over the time period  <br>  <br>Example: 1, 1, 1, 1  <br>  <br>stagnated means the property initially was changing but ended up unchanged (more than one consecutive trailing value are the same)  <br>  <br>Example: 1, 2, 3, 3 |
| start | ISO8601 timestamp string (UTC) | required  <br>  <br>Example: 2023-06-16T09:50:20Z |
| end | ISO8601 timestamp string (UTC) | required  <br>  <br>Example: 2023-06-26T09:50:20Z |

# openapi-definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "ASM (ATTACK SURFACE MANAGEMENT)",
    "version": "1.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3/asm"
    }
  ],
  "tags": [
    {
      "name": "Time Series"
    }
  ],
  "paths": {
    "/time_series/point_in_time/issues/{uid}": {
      "get": {
        "tags": [
          "Time Series"
        ],
        "summary": "Get Issue point in time",
        "description": "",
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
            "name": "PROJECT-ID",
            "in": "header",
            "schema": {
              "type": "string"
            },
            "description": "Required: id from /api/v3/asm/projects",
            "example": "{{project-id}}"
          },
          {
            "name": "point_in_time",
            "in": "query",
            "schema": {
              "type": "string"
            },
            "description": "required, YYYY-MM-DD or ISO8601 timestamp string (UTC), Example: 2023-06-16T09:50:20Z ",
            "example": "2023-08-02"
          },
          {
            "name": "uid",
            "in": "path",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "id or uuid from /api/v3/asm/search/issues/:search_string",
            "example": "9ae8bad035ed88b7f2cf7636fddd2b3edbee6ca4d308ac17ccbfa079ef600da0"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "headers": {
              "Server": {
                "schema": {
                  "type": "string",
                  "example": "Cowboy"
                }
              },
              "Date": {
                "schema": {
                  "type": "string",
                  "example": "Fri, 18 Aug 2023 21:14:57 GMT"
                }
              },
              "Connection": {
                "schema": {
                  "type": "string",
                  "example": "keep-alive"
                }
              },
              "Content-Type": {
                "schema": {
                  "type": "string",
                  "example": "application/json"
                }
              },
              "X-Content-Type-Options": {
                "schema": {
                  "type": "string",
                  "example": "nosniff"
                }
              },
              "Vary": {
                "schema": {
                  "type": "string",
                  "example": "Origin"
                }
              },
              "Content-Length": {
                "schema": {
                  "type": "integer",
                  "example": "2415"
                }
              },
              "Via": {
                "schema": {
                  "type": "string",
                  "example": "1.1 vegur"
                }
              }
            },
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                },
                "example": {
                  "success": true,
                  "message": "Success",
                  "result": {
                    "issue": {
                      "uid": "9ae8bad035ed88b7f2cf7636fddd2b3edbee6ca4d308ac17ccbfa079ef600da0",
                      "name": "deprecated_ssl_protocol_detected",
                      "tags": [],
                      "type": "standard",
                      "uuid": "7cbdbac4-0b62-430d-a0a0-0bb83185fb12",
                      "scoped": true,
                      "source": "intrigue",
                      "status": "open_new",
                      "details": {
                        "name": "deprecated_ssl_protocol_detected",
                        "added": "2020-01-01",
                        "proof": {
                          "description": "It has been identified that the target supports one or more deprecated protocols",
                          "deprecated_protocols": [
                            {
                              "type": "tls",
                              "enabled": "1",
                              "version": "1.0"
                            },
                            {
                              "type": "tls",
                              "enabled": "1",
                              "version": "1.1"
                            }
                          ]
                        },
                        "status": "confirmed",
                        "category": "misconfiguration",
                        "severity": 5,
                        "references": [
                          {
                            "uri": "https://www.ssl.com/article/deprecating-early-tls/",
                            "type": "description"
                          },
                          {
                            "uri": "https://support.globalsign.com/ssl/general-ssl/how-enable-or-disable-ssl-and-tls-versions",
                            "type": "remediation"
                          }
                        ],
                        "description": "This server is configured to allow a deprecated ssl / tls protocol.",
                        "pretty_name": "Deprecated SSL/TLS Protocol Detected",
                        "remediation": "Disable the weak protocol according the instructions for your web server."
                      },
                      "summary": {
                        "scoped": true,
                        "status": "open_new",
                        "category": "misconfiguration",
                        "severity": 5,
                        "confidence": "confirmed",
                        "status_new": "open",
                        "identifiers": null,
                        "pretty_name": "Deprecated SSL/TLS Protocol Detected",
                        "ticket_list": [],
                        "status_new_detailed": "new"
                      },
                      "category": "misconfiguration",
                      "severity": 5,
                      "upstream": "intrigue",
                      "entity_id": 398829558,
                      "last_seen": "2023-08-01T00:37:56.000Z",
                      "collection": "broadscopeenabled_g6zjj10",
                      "confidence": "confirmed",
                      "created_at": "2023-04-20T16:47:47.709Z",
                      "dynamic_id": 35906366,
                      "entity_uid": "28abaa9fea296764a8da0f76832056773852f5f82ae553769fd3b462a46bc205",
                      "first_seen": "2023-04-20T16:47:03.000Z",
                      "updated_at": "2023-08-01T02:14:33.057Z",
                      "alias_group": "38",
                      "description": "This server is configured to allow a deprecated ssl / tls protocol.",
                      "entity_name": "https://attacksurface.app:8443",
                      "entity_type": "Intrigue::Entity::Uri",
                      "identifiers": null,
                      "pretty_name": "Deprecated SSL/TLS Protocol Detected",
                      "ticket_list": [],
                      "collection_id": 142553,
                      "collection_type": "user_collection",
                      "collection_uuid": "2ffc71a9-8588-4612-9a1c-95784e7b9b8e",
                      "epss_v2_score_lte": null,
                      "organization_uuid": "075892c8-fe6f-454e-a071-34a7342c16a3",
                      "cisa_known_exploited": false,
                      "epss_v2_percentile_gte": null,
                      "elasticsearch_mappings_hash": "2e1457527740b3d5d83404bcae8f15bf"
                    },
                    "point_in_time": "2023-08-02T00:00:00.000Z"
                  }
                }
              }
            }
          }
        }
      }
    }
  },
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": false,
    "samples-enabled": true
  }
}
```

---

← [Get Issue points in time](get_time-series-points-in-time-issues-uid.md) · [up](../README.md) · [Technologies](../technologies.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_time-series-point-in-time-issues-uid>.*
