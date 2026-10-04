---
title: "Jira projects"
source: https://gtidocs.virustotal.com/reference/get_projects-uuid-integrations-jira-projects
slug: get_projects-uuid-integrations-jira-projects
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:42.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [ASM Integrations](../asm-integrations.md) › Jira projects

---

# jira-projects

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
      "name": "ASM Integrations",
      "description": "Add your integration(s) here. Once added you can associate them to a collection within the Integrations Collections section."
    }
  ],
  "paths": {
    "/projects/{uuid}/integrations/jira/projects": {
      "get": {
        "tags": [
          "ASM Integrations"
        ],
        "summary": "Jira projects",
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
            "name": "uuid",
            "in": "path",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Required: uuid from /api/v3/asm/projects",
            "example": "{{project_uuid}}"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful response",
            "content": {
              "application/json": {}
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

← [Index](get_projects-uuid-integrations.md) · [up](../README.md) · [Destroy](delete_integrations-uuid.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_projects-uuid-integrations-jira-projects>.*
