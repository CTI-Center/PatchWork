---
title: "Authentication"
source: https://gtidocs.virustotal.com/reference/ti-authentication
slug: ti-authentication
section: reference
group: "GTI Alerts"
updatedAt: 2026-03-06T12:09:47.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [GTI Alerts](../README.md) › [Get Started](../ti-get-started.md) › Authentication

---

# authentication

This is your first endpoint! Edit this page to start documenting your API.

Use this endpoint to get the bearer token required on OAuth 2.0 auhtentication.

This endpoint returns a JSON containing the `acess_token` and the `expires_in` data.

```json Example response
{
  "access_token": "ya29.d.s0Ad...",
  "issued_token_type": "urn:ietf:params:oauth:token-type:access_token",
  "token_type": "Bearer",
  "expires_in": 14398
}
```

# openapi-definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "version": "1.0.0",
    "title": "ATD Authentication"
  },
  "servers": [
    {
      "url": "https://idp.prod.identity.proactive.virustotal.com"
    }
  ],
  "paths": {
    "/realms/master/exchange/api-key": {
      "post": {
        "summary": "New Endpoint",
        "description": "This is your first endpoint! Edit this page to start documenting your API.",
        "responses": {
          "200": {
            "description": "Successful response"
          }
        },
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "api_key": {
                    "type": "string"
                  }
                },
                "required": [
                  "api_key"
                ]
              }
            }
          }
        },
        "operationId": "post_realms-master-exchange-api-key"
      }
    }
  },
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": false
  }
}
```

---

← [Get Started](../ti-get-started.md) · [up](../README.md) · [Alerts](../alerts.md) →

*Archived from <https://gtidocs.virustotal.com/reference/ti-authentication>.*
