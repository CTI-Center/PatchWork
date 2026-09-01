---
title: "Add a vote to a domain"
source: https://gtidocs.virustotal.com/reference/domain-votes-post
slug: domain-votes-post
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T02:03:44.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Domains & Resolutions](../domains-resolutions.md) › Add a vote to a domain

---

# add-a-vote-to-a-domain

With this endpoint you can post a vote for a given domain. The body for the POST request must be the JSON representation of a [vote object](../../17-api-objects/vote-object.md). Note however that you don't need to provide an ID for the object, as they are automatically generated for new votes.

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

Returns a [votes](../../17-api-objects/vote-object.md) object.

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
      "name": "Domains & Resolutions"
    }
  ],
  "paths": {
    "/domains/{domain}/votes": {
      "post": {
        "tags": [
          "Domains & Resolutions"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "domain-votes-post",
        "parameters": [
          {
            "description": "hostname or domain name",
            "in": "path",
            "name": "domain",
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
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "properties": {
                  "data": {
                    "default": "{\"type\": \"vote\", \"attributes\": {\"verdict\": \"harmless\"}}",
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
                    "value": "{}"
                  }
                },
                "schema": {
                  "properties": {},
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
                    "value": "{\n  \"error\": {\n    \"code\": \"AlreadyExistsError\",\n    \"message\": \"User \\\"username\\\" already voted \\\"harmless\\\" for this domain\"\n  }\n}"
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
        "summary": "Add a vote to a domain"
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

← [Get votes on a domain](domains-votes-get.md) · [up](../README.md) · [Get objects related to a domain](domains-relationships.md) →

*Archived from <https://gtidocs.virustotal.com/reference/domain-votes-post>.*
