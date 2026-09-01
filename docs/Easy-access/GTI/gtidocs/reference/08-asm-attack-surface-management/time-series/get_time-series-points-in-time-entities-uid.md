---
title: "Get Entity points in time"
source: https://gtidocs.virustotal.com/reference/get_time-series-points-in-time-entities-uid
slug: get_time-series-points-in-time-entities-uid
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:23.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Time Series](../time-series.md) › Get Entity points in time

---

# get-entity-points-in-time

Returns the dates of when an entity was seen.

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
    "/time_series/points_in_time/entities/{uid}": {
      "get": {
        "tags": [
          "Time Series"
        ],
        "summary": "Get Entity points in time",
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
            "name": "start",
            "in": "query",
            "schema": {
              "type": "string"
            },
            "description": "required, YYYY-MM-DD or ISO8601 timestamp string (UTC), Example: 2023-06-16T09:50:20Z",
            "example": "2023-07-16T08:36:54Z"
          },
          {
            "name": "end",
            "in": "query",
            "schema": {
              "type": "string"
            },
            "description": "required, YYYY-MM-DD or ISO8601 timestamp string (UTC), Example: 2023-06-16T09:50:20Z",
            "example": "2023-08-02T09:50:20Z"
          },
          {
            "name": "uid",
            "in": "path",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "id or uuid from /api/v3/asm/search/entities/:search_string",
            "example": "28abaa9fea296764a8da0f76832056773852f5f82ae553769fd3b462a46bc205"
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
                  "example": "Fri, 18 Aug 2023 20:03:46 GMT"
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
                  "example": "739"
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
                    "entity": {
                      "uid": "28abaa9fea296764a8da0f76832056773852f5f82ae553769fd3b462a46bc205",
                      "points_in_time": [
                        "2023-07-22T06:19:37Z",
                        "2023-07-23T09:54:03Z",
                        "2023-07-24T11:18:18Z",
                        "2023-07-25T10:18:06Z",
                        "2023-07-26T08:37:46Z",
                        "2023-07-27T12:15:42Z",
                        "2023-07-28T16:47:30Z",
                        "2023-07-29T06:31:11Z",
                        "2023-07-30T08:06:11Z",
                        "2023-08-01T00:37:56Z",
                        "2023-08-02T22:40:57Z",
                        "2023-08-03T11:55:00Z",
                        "2023-08-04T11:27:48Z",
                        "2023-08-05T05:33:34Z",
                        "2023-08-06T04:49:42Z",
                        "2023-08-08T01:20:45Z",
                        "2023-08-09T08:10:57Z",
                        "2023-08-10T02:11:53Z",
                        "2023-08-12T22:27:46Z",
                        "2023-08-14T02:34:19Z",
                        "2023-08-16T00:30:05Z",
                        "2023-08-17T05:59:09Z",
                        "2023-08-18T01:21:47Z"
                      ]
                    },
                    "start": "2023-07-16T08:36:54Z",
                    "end": "2023-08-18T09:50:20Z"
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

← [Get Entity point in time](get_time-series-point-in-time-entities-uid.md) · [up](../README.md) · [Get Issue points in time](get_time-series-points-in-time-issues-uid.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_time-series-points-in-time-entities-uid>.*
