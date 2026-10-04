---
title: "Create"
source: https://gtidocs.virustotal.com/reference/post_collections-collection-uuid-collection-runs
slug: post_collections-collection-uuid-collection-runs
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:18.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Collection Runs](../collection-runs.md) › Create

---

# create

This will schedule a scan for the collection entered

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
      "name": "Collection Runs"
    }
  ],
  "paths": {
    "/collections/{collection_uuid}/collection_runs": {
      "post": {
        "tags": [
          "Collection Runs"
        ],
        "summary": "Create",
        "description": "",
        "requestBody": {
          "content": {}
        },
        "security": [],
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
            "name": "collection_uuid",
            "in": "path",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Required: uuid of collection from /api/v3/asm/user_collections",
            "example": "f33be380-13b7-46b0-a20d-cb2e1f0c3dcb"
          }
        ],
        "responses": {
          "200": {
            "description": "Scan scheduled",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                },
                "example": {
                  "success": true,
                  "message": "Collection scan",
                  "result": true
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

← [Index](get_collections-collection-uuid-collection-runs.md) · [up](../README.md) · [Entities](../entities.md) →

*Archived from <https://gtidocs.virustotal.com/reference/post_collections-collection-uuid-collection-runs>.*
