---
title: "Set Status"
source: https://gtidocs.virustotal.com/reference/post_issues-id-status
slug: post_issues-id-status
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:22.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Issues](../issues.md) › Set Status

---

# set-status

Set status on an individual entity. The body takes a json input with a single 'status' field.

Values for Payload status:

- open_new
- open_triaged
- open_in_progress
- closed_resolved
- closed_duplicate
- closed_out_of_scope
- closed_benign
- closed_risk_accepted
- closed_false_positive
- closed_no_repro
- closed_tracked_externally
- closed

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
      "name": "Issues"
    }
  ],
  "paths": {
    "/issues/{id}/status": {
      "post": {
        "tags": [
          "Issues"
        ],
        "summary": "Set Status",
        "description": "",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "example": {
                  "status": "open_triaged"
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
            "name": "id",
            "in": "path",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Required: id from /api/v3/asm/search/issues/"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                },
                "example": {
                  "success": true,
                  "message": "Successfully reported status as open_triaged",
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

← [Get Detail](get_issues-id.md) · [up](../README.md) · [Time Series](../time-series.md) →

*Archived from <https://gtidocs.virustotal.com/reference/post_issues-id-status>.*
