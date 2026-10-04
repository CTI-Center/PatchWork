---
title: "Request a domain (re)scan"
source: https://gtidocs.virustotal.com/reference/domains-rescan
slug: domains-rescan
section: reference
group: "IoC Investigation"
updatedAt: 2026-02-05T12:43:34.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Domains & Resolutions](../domains-resolutions.md) › Request a domain (re)scan

---

# request-a-domain-(re)scan

This endpoint can be used to analyse domains or reanalyse them to refresh their verdicts, whois information, SSL certs, etc. This endpoint sends the domain to be (re)scanned and returns an analysis ID that can be used to retrieve the verdicts from the available vendors using the [Analyses](../analyses-submissions-operations/analysis.md) endpoint.

```json Example response
{
    "data": {
        "type": "analysis",
        "id": "d-f4e5279ebbcf9d485e33f3c67007b73e9f12d54bbca875545819a2307a194752-1715608490",
        "links": {
            "self": "https://www.virustotal.com/api/v3/analyses/d-f4e5279ebbcf9d485e33f3c67007b73e9f12d54bbca875545819a2307a194752-1715608490"
        }
    }
}
```

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
    "/domains/{domain}/analyse": {
      "post": {
        "tags": [
          "Domains & Resolutions"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "domains-rescan",
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
          }
        ],
        "responses": {
          "200": {
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
        "summary": "Request an domain rescan"
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

← [Get comments on a domain](domains-comments-get.md) · [up](../README.md) · [Add a comment to a domain](domains-comments-post.md) →

*Archived from <https://gtidocs.virustotal.com/reference/domains-rescan>.*
