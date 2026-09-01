---
title: "Get votes on an IP address"
source: https://gtidocs.virustotal.com/reference/ip-votes
slug: ip-votes
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T02:03:36.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [IP addresses](../ip-addresses.md) › Get votes on an IP address

---

# get-votes-on-an-ip-address

Returns a list of [Vote](../../17-api-objects/vote-object.md) objects.

# openapi-definition

```json
{
  "info": {
    "title": "IoC Investigation",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "IP addresses"
    }
  ],
  "paths": {
    "/ip_addresses/{ip}/votes": {
      "get": {
        "tags": [
          "IP addresses"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "ip-votes",
        "parameters": [
          {
            "description": "IP Address",
            "in": "path",
            "name": "ip",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Your API key",
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"data\": [\n        {\n            \"attributes\": {\n                \"date\": 1574246328,\n                \"value\": 47,\n                \"verdict\": \"harmless\"\n            },\n            \"id\": \"i-1.1.1.1-a68784ad\",\n            \"links\": {\n                \"self\": \"https://www.virustotal.com/api/v3/votes/i-1.1.1.1-a68784ad\"\n            },\n            \"type\": \"vote\"\n        },\n        {\n            \"attributes\": {\n                \"date\": 1569486791,\n                \"value\": -1,\n                \"verdict\": \"malicious\"\n            },\n            \"id\": \"i-1.1.1.1-e15e57e9\",\n            \"links\": {\n                \"self\": \"https://www.virustotal.com/api/v3/votes/i-1.1.1.1-e15e57e9\"\n            },\n            \"type\": \"vote\"\n        }\n    ],\n    \"links\": {\n        \"self\": \"https://www.virustotal.com/api/v3/ip_addresses/1.1.1.1/votes?limit=10\"\n    }\n}"
                  }
                },
                "schema": {
                  "properties": {
                    "data": {
                      "items": {
                        "properties": {
                          "attributes": {
                            "properties": {
                              "date": {
                                "default": 0,
                                "type": "integer"
                              },
                              "value": {
                                "default": 0,
                                "type": "integer"
                              },
                              "verdict": {
                                "type": "string"
                              }
                            },
                            "type": "object"
                          },
                          "id": {
                            "type": "string"
                          },
                          "links": {
                            "properties": {
                              "self": {
                                "type": "string"
                              }
                            },
                            "type": "object"
                          },
                          "type": {
                            "type": "string"
                          }
                        },
                        "type": "object"
                      },
                      "type": "array"
                    },
                    "links": {
                      "properties": {
                        "self": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    }
                  },
                  "type": "object"
                }
              }
            },
            "description": "200"
          },
          "400": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "properties": {},
                  "type": "object"
                }
              }
            },
            "description": "400"
          }
        },
        "security": [],
        "summary": "Get votes on an IP address"
      }
    }
  },
  "security": [],
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3"
    }
  ],
  "x-readme": {
    "explorer-enabled": true,
    "headers": [],
    "proxy-enabled": false,
    "samples-enabled": true
  }
}
```

---

← [Get object descriptors related to an IP address](ip-relationships-ids.md) · [up](../README.md) · [Add a vote to an IP address](ip-votes-post.md) →

*Archived from <https://gtidocs.virustotal.com/reference/ip-votes>.*
