---
title: "Index"
source: https://gtidocs.virustotal.com/reference/get_projects-uuid-integrations
slug: get_projects-uuid-integrations
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:42.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [ASM Integrations](../asm-integrations.md) › Index

---

# index

List all integrations configured for the project.

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
    "/projects/{uuid}/integrations": {
      "get": {
        "tags": [
          "ASM Integrations"
        ],
        "summary": "Index",
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
            "description": "OK",
            "headers": {
              "Date": {
                "schema": {
                  "type": "string",
                  "example": "Fri, 09 Sep 2022 16:55:58 GMT"
                }
              },
              "Content-Type": {
                "schema": {
                  "type": "string",
                  "example": "application/json"
                }
              },
              "Transfer-Encoding": {
                "schema": {
                  "type": "string",
                  "example": "chunked"
                }
              },
              "Connection": {
                "schema": {
                  "type": "string",
                  "example": "keep-alive"
                }
              },
              "X-Content-Type-Options": {
                "schema": {
                  "type": "string",
                  "example": "nosniff"
                }
              },
              "Vary": {
                "schema": {
                  "type": "string",
                  "example": "Origin"
                }
              },
              "Via": {
                "schema": {
                  "type": "string",
                  "example": "1.1 vegur"
                }
              },
              "CF-Cache-Status": {
                "schema": {
                  "type": "string",
                  "example": "DYNAMIC"
                }
              },
              "Report-To": {
                "schema": {
                  "type": "string",
                  "example": "{\"endpoints\":[{\"url\":\"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=6RFtbjtxrFDWfaT6eJav0ILuL1NSITgAsTBtkDvHH%2F9PsY976wx0Gbbidu0oeyxV0z%2F97%2Bb2QYTHl2pcgs2Co4UXRWgqxrUHcK%2B0UIzIlGzhp8ArDF%2FCHqplLVoxbP3gLg%3D%3D\"}],\"group\":\"cf-nel\",\"max_age\":604800}"
                }
              },
              "NEL": {
                "schema": {
                  "type": "string",
                  "example": "{\"success_fraction\":0,\"report_to\":\"cf-nel\",\"max_age\":604800}"
                }
              },
              "Server": {
                "schema": {
                  "type": "string",
                  "example": "cloudflare"
                }
              },
              "CF-RAY": {
                "schema": {
                  "type": "string",
                  "example": "7481745a1af286fc-ORD"
                }
              },
              "Content-Encoding": {
                "schema": {
                  "type": "string",
                  "example": "br"
                }
              }
            },
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                },
                "example": {
                  "success": true,
                  "message": "Success",
                  "result": [
                    {
                      "id": 180,
                      "uuid": "8bc49144-7704-4381-994c-2e7ada9fee98",
                      "name": "Github Integration 1",
                      "description": "",
                      "type": "github",
                      "created_at": "2022-09-06T23:38:10.751Z",
                      "updated_at": "2022-09-06T00:00:00.000Z",
                      "user_email": "Email not found or token is missing email access permissions."
                    },
                    {
                      "id": 183,
                      "uuid": "f38fc0fa-a7e2-4501-89de-9e590659a68a",
                      "name": "Test github Integration",
                      "description": "",
                      "type": "github",
                      "created_at": "2022-09-07T16:11:06.609Z",
                      "updated_at": "2022-09-07T00:00:00.000Z",
                      "user_email": "Email not found or token is missing email access permissions."
                    },
                    {
                      "id": 184,
                      "uuid": "3fab6628-9f98-45b4-9285-9efea0b55d3e",
                      "name": "Test Azure Integration",
                      "description": "",
                      "type": "azure",
                      "created_at": "2022-09-07T16:15:37.703Z",
                      "updated_at": "2022-09-07T00:00:00.000Z"
                    }
                  ]
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

← [Create](post_projects-uuid-integrations.md) · [up](../README.md) · [Jira projects](get_projects-uuid-integrations-jira-projects.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_projects-uuid-integrations>.*
