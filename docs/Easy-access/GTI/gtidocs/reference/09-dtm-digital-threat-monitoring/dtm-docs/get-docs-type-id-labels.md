---
title: "Fetch the labels for an existing document"
source: https://gtidocs.virustotal.com/reference/get-docs-type-id-labels
slug: get-docs-type-id-labels
section: reference
group: "DTM (DIGITAL THREAT MONITORING)"
updatedAt: 2025-09-25T02:07:03.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [DTM (DIGITAL THREAT MONITORING)](../README.md) › [DTM Docs](../dtm-docs.md) › Fetch the labels for an existing document

---

# fetch-the-labels-for-an-existing-document

A read-only endpoint to fetch the labels for an existing document indexed in our system.

# openapi-definition

```json
{
  "components": {
    "schemas": {
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
      "Labels": {
        "description": "A list of labels that have been extracted from a document by our analytics processing.",
        "properties": {
          "labels": {
            "description": "The list of labels.",
            "items": {
              "$ref": "#/components/schemas/Label"
            },
            "type": "array"
          }
        },
        "required": [
          "labels"
        ],
        "title": "Labels",
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
    "/docs/{type}/{id}/labels": {
      "get": {
        "description": "",
        "operationId": "get-docs-type-id-labels",
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
            "description": "The document type.",
            "in": "path",
            "name": "type",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "The document's ID.",
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
                  "get-labels": {
                    "value": {
                      "labels": [
                        {
                          "classifier": "classifier-language",
                          "confidence": 53,
                          "element_path": "body",
                          "id": "747f72e9-1a93-477e-a204-ac17ae78479e",
                          "label": "en",
                          "version": "1-0-0"
                        },
                        {
                          "classifier": "classifier-threat",
                          "confidence": 100,
                          "element_path": "",
                          "id": "c155dcad-9e90-480e-889b-985e507df477",
                          "label": "information-security/malware/ransomware",
                          "version": "2-0-0"
                        }
                      ]
                    }
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Labels"
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
        "summary": "Fetch the labels for an existing document",
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

← [Retrieve an indexed document by its type and ID](get-docs-type-id.md) · [up](../README.md) · [Fetch the topics for an existing document](get-docs-type-id-topics.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-docs-type-id-labels>.*
