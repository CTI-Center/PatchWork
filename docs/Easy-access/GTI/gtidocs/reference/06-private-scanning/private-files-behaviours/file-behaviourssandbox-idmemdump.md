---
title: "Get the PCAP file generated during a private file’s behavior analysis"
source: https://gtidocs.virustotal.com/reference/file-behaviourssandbox-idmemdump
slug: file-behaviourssandbox-idmemdump
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:37:06.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private Files Behaviours](../private-files-behaviours.md) › Get the PCAP file generated during a private file’s behavior analysis

---

# get-the-pcap-file-generated-during-a-private-file’s-behavior-analysis

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

Fetch the memdump file associated with the sandbox execution.

# openapi-definition

```json
{
  "info": {
    "title": "Private Scanning",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Private Files Behaviours"
    }
  ],
  "paths": {
    "/file_behaviours/{sandbox_id}/pcap": {
      "get": {
        "tags": [
          "Private Files Behaviours"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "file-behaviourssandbox-idmemdump",
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
            "description": "Sandbox report ID",
            "in": "path",
            "name": "sandbox_id",
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
        "summary": "Get the PCAP file generated during a private file’s behavior analysis"
      }
    }
  },
  "security": [],
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3/private"
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

← [Get the memdump file generated during a private file’s behavior analysis](privatefile-behaviourssandbox-idpcap.md) · [up](../README.md) · [Get object descriptors related to a private file's behaviour report](privatefile-behaviourssandbox-idrelationshipsrelationship.md) →

*Archived from <https://gtidocs.virustotal.com/reference/file-behaviourssandbox-idmemdump>.*
