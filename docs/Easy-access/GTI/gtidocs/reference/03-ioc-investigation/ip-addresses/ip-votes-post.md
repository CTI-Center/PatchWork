---
title: "Add a vote to an IP address"
source: https://gtidocs.virustotal.com/reference/ip-votes-post
slug: ip-votes-post
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T02:03:37.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [IP addresses](../ip-addresses.md) › Add a vote to an IP address

---

# add-a-vote-to-an-ip-address

With this endpoint you can post a vote for a given file. The body for the POST request must be the JSON representation of a [vote object](../../17-api-objects/vote-object.md). Note however that you don't need to provide an ID for the object, as they are automatically generated for new votes.

The verdict attribute must have be either harmless or malicious.

```json Example request
{
  "data": {
    "type": "vote",
    "attributes": {
    	"verdict": "harmless"
    }
  }
}
```

Returns a [Vote](../../17-api-objects/vote-object.md) object.

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
      "post": {
        "tags": [
          "IP addresses"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "ip-votes-post",
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
            "in": "header",
            "name": "x-apikey",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "properties": {
                  "data": {
                    "default": "{\"type\": \"vote\", \"attributes\": {\"verdict\": \"malicious\"}}",
                    "description": "Vote object",
                    "format": "json",
                    "type": "string"
                  }
                },
                "required": [
                  "data"
                ],
                "type": "object"
              }
            }
          }
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"data\": {\n        \"attributes\": {\n            \"date\": 1574246672,\n            \"value\": 1,\n            \"verdict\": \"harmless\"\n        },\n        \"id\": \"i-IP-a68784ad\",\n        \"links\": {\n            \"self\": null\n        },\n        \"type\": \"vote\"\n    }\n}"
                  }
                },
                "schema": {
                  "properties": {
                    "data": {
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
                            "self": {}
                          },
                          "type": "object"
                        },
                        "type": {
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
          },
          "409": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"error\": {\n        \"code\": \"AlreadyExistsError\",\n        \"message\": \"User \\\"UserName\\\" already voted \\\"harmless\\\" for this ip_address\"\n    }\n}"
                  }
                },
                "schema": {
                  "properties": {
                    "error": {
                      "properties": {
                        "code": {
                          "type": "string"
                        },
                        "message": {
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
            "description": "409"
          }
        },
        "security": [],
        "summary": "Add a vote to an IP address"
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

← [Get votes on an IP address](ip-votes.md) · [up](../README.md) · [Get objects related to an IP address](ip-relationships.md) →

*Archived from <https://gtidocs.virustotal.com/reference/ip-votes-post>.*
