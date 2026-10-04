---
title: "Destroy"
source: https://gtidocs.virustotal.com/reference/delete_integrations-uuid
slug: delete_integrations-uuid
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:43.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [ASM Integrations](../asm-integrations.md) › Destroy

---

# destroy

Delete an existing integration. This cannot be undone!

To obtain a UUID for your integration, please see the GET Index query first:

![](https://content.pstmn.io/f577cdca-1f0b-49b5-9515-14872c74b4ca/SW50ZWdyYXRpb24gRGVzdHJveS5wbmc=)

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
    "/integrations/{uuid}": {
      "delete": {
        "tags": [
          "ASM Integrations"
        ],
        "summary": "Destroy",
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
            "description": "uuid from /api/v3/asm/projects/:uuid/integrations"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "headers": {
              "Date": {
                "schema": {
                  "type": "string",
                  "example": "Fri, 09 Sep 2022 16:56:48 GMT"
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
                  "example": "{\"endpoints\":[{\"url\":\"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=69B12vtYo6ovZcSmiGiV3P%2Fx9C3%2FZcFcSVtg6AzzSY7Pi96biQ20gax5GpOqlvySvDj%2FIYMEz1p7QXsgOM7lkFej%2FnVhHGRg%2BcC5j3Np6K4Jdf5j51%2F7bEVrsVs02elQBw%3D%3D\"}],\"group\":\"cf-nel\",\"max_age\":604800}"
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
                  "example": "748175933d7886fc-ORD"
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
                  "success": false,
                  "message": "Success",
                  "result": null
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

← [Jira projects](get_projects-uuid-integrations-jira-projects.md) · [up](../README.md) · [Integration Collections](../integration-collections.md) →

*Archived from <https://gtidocs.virustotal.com/reference/delete_integrations-uuid>.*
