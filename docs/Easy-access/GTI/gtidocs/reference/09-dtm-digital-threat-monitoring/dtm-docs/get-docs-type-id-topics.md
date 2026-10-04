---
title: "Fetch the topics for an existing document"
source: https://gtidocs.virustotal.com/reference/get-docs-type-id-topics
slug: get-docs-type-id-topics
section: reference
group: "DTM (DIGITAL THREAT MONITORING)"
updatedAt: 2025-09-25T02:07:03.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [DTM (DIGITAL THREAT MONITORING)](../README.md) › [DTM Docs](../dtm-docs.md) › Fetch the topics for an existing document

---

# fetch-the-topics-for-an-existing-document

A read-only endpoint to fetch the topics for an existing document saved in the system.

# openapi-definition

```json
{
  "components": {
    "schemas": {
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
      "Topics": {
        "description": "A list of topics extracted from a document by our analytics processing.",
        "properties": {
          "topics": {
            "description": "The list of topics.",
            "items": {
              "$ref": "#/components/schemas/Topic"
            },
            "type": "array"
          }
        },
        "required": [
          "topics"
        ],
        "title": "Topics",
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
    "/docs/{type}/{id}/topics": {
      "get": {
        "description": "",
        "operationId": "get-docs-type-id-topics",
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
            "description": "The type of document for which the topics will be searched.",
            "in": "path",
            "name": "type",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "The ID of the document to fetch the topics for.",
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
                "examples": {
                  "get-topics": {
                    "value": {
                      "topics": [
                        {
                          "confidence": 100,
                          "entity_locations": [
                            {
                              "element_path": "body",
                              "offsets": [
                                55,
                                59
                              ]
                            }
                          ],
                          "extractor": "analysis-pipeline.preprocessor",
                          "extractor_version": "1.0.0",
                          "id": "7c4b1126-40e5-4c18-bec2-6568c8a3a85a",
                          "type": "domain",
                          "value": "t.co"
                        }
                      ]
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Topics"
                }
              }
            },
            "description": "OK"
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
        "summary": "Fetch the topics for an existing document",
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

← [Fetch the labels for an existing document](get-docs-type-id-labels.md) · [up](../README.md) · [Search for documents](post-docs-search.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-docs-type-id-topics>.*
