---
title: "Create"
source: https://gtidocs.virustotal.com/reference/post_notes-item-type-item-uid
slug: post_notes-item-type-item-uid
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:26.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Notes](../notes.md) › Create

---

# create

Creates a note on an entity or issue.

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
      "name": "Notes"
    }
  ],
  "paths": {
    "/notes/{item_type}/{item_uid}": {
      "post": {
        "tags": [
          "Notes"
        ],
        "summary": "Create",
        "description": "",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "example": {
                  "note_text": "- testing a note that supports markdown\n- and has some neat new features"
                }
              }
            }
          }
        },
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
            "name": "item_type",
            "in": "path",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "issue or entity",
            "example": "issue"
          },
          {
            "name": "item_uid",
            "in": "path",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "id from /api/v3/asm/search/issues/collection:CollectionName or /api/v3/asm/search/entities/collection:CollectionName"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "text/plain": {
                "schema": {
                  "type": "string"
                },
                "example": "{\n    \"success\": true,\n    \"message\": \"Note add queued for issue 6b884a854d4998f787e1dde6b937f0ca63c844dcfe9558e1c2758cef0ca6d459\",\n    \"result\": true\n}"
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

← [Index](get_notes-item-type-item-uid.md) · [up](../README.md) · [Delete](delete_notes-item-type-item-uid-note-uid.md) →

*Archived from <https://gtidocs.virustotal.com/reference/post_notes-item-type-item-uid>.*
