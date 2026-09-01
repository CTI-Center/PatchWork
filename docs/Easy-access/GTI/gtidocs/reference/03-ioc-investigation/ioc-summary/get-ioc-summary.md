---
title: "Retrieve summary for a list of IoCs"
source: https://gtidocs.virustotal.com/reference/get-ioc-summary
slug: get-ioc-summary
section: reference
group: "IoC Investigation"
updatedAt: 2026-03-25T09:11:02.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [IOC Summary](../ioc-summary.md) › Retrieve summary for a list of IoCs

---

# retrieve-summary-for-a-list-of-iocs

Retrieve summary for a list of IoCs.The request body should contain a list of IoC descriptors.

Retrieve summary for a list of IoCs.The request body should contain a list of IoC descriptors.

### input

Accepts a list of up to 1,000 IoC descriptors in a single POST request.

### supported-ioc-types

File hashes (MD5, SHA1, SHA256), domains, URLs, and IP addresses.

### output

Returns a concise summary object for each requested IoC, intended to improve efficiency and performance for large-scale enrichments.

### large-payloads

If the response exceeds the 30MB size limit, the API provides a GCS fallback mechanism, returning an HTTP 302 Found redirect to a short-lived (15 minutes TTL) signed URL for downloading the full JSON result.

### error-handling

Batch requests follow an "all-or-nothing" approach; if any single IoC cannot be processed, the entire request will be rejected with a 400 Bad Request.

### example

```json
POST /api/v3/iocs/summary
    Content-Type: application/json
    x-apikey: <YOUR_API_KEY>
   
    {
      "iocs": [
        {
          "type": "file",
          "id": "44d88612fea8a8f36de82e1278abb02f"
        },
        {
          "type": "domain",
          "id": "example.com"
        },
        {
          "type": "ip_address",
          "id": "8.8.8.8"
        }
      ]
    }
```

<br />

# openapi-definition

```json
{
  "info": {
    "title": "IoC Investigation",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "paths": {
    "/iocs/summary": {
      "post": {
        "summary": "Retrieve summary for a list of IoCs.",
        "description": "Retrieve summary for a list of IoCs.\n\nThe request body should contain a list of IoC descriptors.",
        "operationId": "IocsSummaryHandler_post",
        "parameters": [
          {
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Google TI API key"
          }
        ],
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
                  "iocs": {
                    "type": "array",
                    "items": {
                      "properties": {
                        "type": {
                          "type": "string",
                          "description": "Type of IOC"
                        },
                        "id": {
                          "type": "string",
                          "description": "IOC's Hash or id"
                        }
                      },
                      "type": "object",
                      "required": [
                        "type",
                        "id"
                      ]
                    },
                    "description": "Array of IOCs"
                  }
                },
                "required": [
                  "iocs"
                ]
              }
            }
          }
        }
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

← [IOC Summary](../ioc-summary.md) · [up](../README.md) · [YARA Rules](../../04-yara-hunting/yara-rules.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-ioc-summary>.*
