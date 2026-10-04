---
title: "Get a domain report"
source: https://gtidocs.virustotal.com/reference/domain-info
slug: domain-info
section: reference
group: "IoC Investigation"
updatedAt: 2026-02-05T12:43:34.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Domains & Resolutions](../domains-resolutions.md) › Get a domain report

---

# get-a-domain-report

> 🚧 gti\_assessment attribute
>
> To get the **gti\_assessment** attribute in the JSON response, ensure that the **x-tool** header is added to the request headers. This header should be used to identify your tool or service with a custom name.

Returns a [Domain](../../17-api-objects/domains-object.md) object.

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
      "name": "Domains & Resolutions"
    }
  ],
  "paths": {
    "/domains/{domain}": {
      "get": {
        "tags": [
          "Domains & Resolutions"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "domain-info",
        "parameters": [
          {
            "description": "Domain name",
            "in": "path",
            "name": "domain",
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
          },
          {
            "description": "The name of your tool or service. This is required to obtain the gti_assesment data",
            "in": "header",
            "name": "x-tool",
            "required": false,
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
                  "Result": {
                    "value": ""
                  }
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
          }
        },
        "security": [],
        "summary": "Get a domain report"
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

← [Domains & Resolutions](../domains-resolutions.md) · [up](../README.md) · [Get comments on a domain](domains-comments-get.md) →

*Archived from <https://gtidocs.virustotal.com/reference/domain-info>.*
