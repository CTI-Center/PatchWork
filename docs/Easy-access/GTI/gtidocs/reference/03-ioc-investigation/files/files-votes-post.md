---
title: "Add a vote on a file"
source: https://gtidocs.virustotal.com/reference/files-votes-post
slug: files-votes-post
section: reference
group: "IoC Investigation"
updatedAt: 2025-09-25T02:03:56.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Files](../files.md) › Add a vote on a file

---

# add-a-vote-on-a-file

With this endpoint you can post a vote for a given file. The body for the `POST` request must be the JSON representation of a vote object. Notice however that you don't need to provide an ID for the object, as they are automatically generated for new votes.

The verdict attribute must have be either `harmless` or `malicious`.

Returns a [Vote](../../17-api-objects/vote-object.md) object.

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
      "name": "Files"
    }
  ],
  "paths": {
    "/files/{id}/votes": {
      "post": {
        "tags": [
          "Files"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "files-votes-post",
        "parameters": [
          {
            "description": "SHA-256, SHA-1 or MD5 identifying the file",
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
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "properties": {
                  "data": {
                    "default": "{\"type\": \"vote\", \"attributes\": {\"verdict\": \"malicious\"}}",
                    "description": "A vote object",
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
                    "value": "{\n  \"error\": {\n    \"code\": \"AlreadyExistsError\",\n    \"message\": \"User \\\"username\\\" already voted \\\"malicious\\\" for this file\"\n  }\n}"
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
        "summary": "Add a vote on a file"
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

← [Get votes on a file](files-votes-get.md) · [up](../README.md) · [Get objects related to a file](files-relationships.md) →

*Archived from <https://gtidocs.virustotal.com/reference/files-votes-post>.*
