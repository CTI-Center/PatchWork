---
title: "Request an IP address (re)scan"
source: https://gtidocs.virustotal.com/reference/ip-analyse
slug: ip-analyse
section: reference
group: "IoC Investigation"
updatedAt: 2026-02-05T12:43:34.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [IP addresses](../ip-addresses.md) › Request an IP address (re)scan

---

# request-an-ip-address-(re)scan

Reanalyse an IP address already in Google Threat Intelligence

This endpoint can be used to analyse IPs or to reanalyse them to refresh their verdicts, whois information, SSL certs, etc. This endpoint sends the IP to be (re)scanned and returns an analysis ID that can be used to retrieve the verdicts from the available vendors using the [Analyses](../analyses-submissions-operations/analysis.md) endpoint.

```json Example response
{
    "data": {
        "type": "analysis",
        "id": "i-f41d931c01fcee6c19e73200aa87ea5d8a8de5316c5288a8df869d31efa1d0fc-1715609875",
        "links": {
            "self": "https://www.virustotal.com/api/v3/analyses/i-f41d931c01fcee6c19e73200aa87ea5d8a8de5316c5288a8df869d31efa1d0fc-1715609875"
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
      "name": "IP addresses"
    }
  ],
  "paths": {
    "/ip_addresses/{id}/analyse": {
      "post": {
        "tags": [
          "IP addresses"
        ],
        "summary": "Request an IP address rescan (re-analyse)",
        "description": "Reanalyse an IP address already in Google Threat Intelligence",
        "operationId": "ip-analyse",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "IP address",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "x-apikey",
            "in": "header",
            "description": "Your API key",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          }
        },
        "deprecated": false,
        "security": []
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

← [Get comments on an IP address](ip-comments-get.md) · [up](../README.md) · [Add a comment to an IP address](ip-comments-post.md) →

*Archived from <https://gtidocs.virustotal.com/reference/ip-analyse>.*
