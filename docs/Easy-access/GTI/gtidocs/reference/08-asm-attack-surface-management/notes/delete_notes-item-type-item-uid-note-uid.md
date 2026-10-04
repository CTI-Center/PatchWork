---
title: "Delete"
source: https://gtidocs.virustotal.com/reference/delete_notes-item-type-item-uid-note-uid
slug: delete_notes-item-type-item-uid-note-uid
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:27.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Notes](../notes.md) › Delete

---

# delete

Deletes all notes on an entity or issue.

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
    "/notes/{item_type}/{item_uid}/{note_uid}": {
      "delete": {
        "tags": [
          "Notes"
        ],
        "summary": "Delete",
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
            "description": "id from /api/v3/asm/search/issues/collection:CollectionName or /api/v3/asm/search/entities/collection:CollectionName",
            "example": "6b884a854d4998f787e1dde6b937f0ca63c844dcfe9558e1c2758cef0ca6d459"
          },
          {
            "name": "note_uid",
            "in": "path",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "uid of note from /api/v3/asm/search/issues/collection:CollectionName or /api/v3/asm/search/entities/collection:CollectionName",
            "example": "ee74ee7d3c06791bf984480810169ab123d97541b39afd623bd08b3981450d93"
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
                "example": "{\n    \"success\": true,\n    \"message\": \"Note remove queued for ee74ee7d3c06791bf984480810169ab123d97541b39afd623bd08b3981450d93 on issue 6b884a854d4998f787e1dde6b937f0ca63c844dcfe9558e1c2758cef0ca6d459\",\n    \"result\": true\n}"
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

← [Create](post_notes-item-type-item-uid.md) · [up](../README.md) · [Tags](../tags.md) →

*Archived from <https://gtidocs.virustotal.com/reference/delete_notes-item-type-item-uid-note-uid>.*
