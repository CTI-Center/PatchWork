---
title: "Export URL for Large IoC Packages"
source: https://gtidocs.virustotal.com/reference/threat-profile_download-url
slug: threat-profile_download-url
section: reference
group: "Global Landscape"
updatedAt: 2026-05-25T08:19:39.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Global Landscape](../README.md) › [Threat Profiles](../threat-profiles.md) › Export URL for Large IoC Packages

---

# export-url-for-large-ioc-packages

Use this endpoint to export Indicators of Compromise (IoCs) associated with all Recommendations in a certain Threat Profile when the export exceeds 32MB. Supported formats include JSON, CSV, and STIX.

The endpoint returns a JSON object containing a temporary download URL:

```json

{
    "data":"https://storage.googleapis.com/vtcollectiondumps/exporter/4c584...d825d4.json?..."
}
```

To retrieve the export, make a subsequent `GET` request to the URL provided in the `data` field of the response.

> 📘
>
> Note that if the `/format` parameter is omitted, this endpoint defaults to JSON.

# examples

Get all IoCs that are associated with recommendations in my threat profile, in STIX format.

```python
import requests

id = "dc2f47a9baa2460089cdd78f7339b19c"
format = "stix" 

url = f"https://www.virustotal.com/api/v3/threat_profiles/{id}/download_url/{format}"

headers = {"x-apikey": <api-key>,"accept": "application/json"}

response = requests.get(url, headers=headers)
response = requests.get(response.json()["data"], headers=headers)
```

# openapi-definition

```json
{
  "info": {
    "title": "Threat Landscape",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "paths": {
    "/threat_profiles/{profile_id}/download_url/{format}": {
      "get": {
        "description": "",
        "responses": {
          "200": {
            "description": "200",
            "content": {}
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "name"
                  ]
                }
              }
            }
          }
        },
        "parameters": [
          {
            "in": "path",
            "name": "format",
            "schema": {
              "type": "string",
              "enum": [
                "csv",
                "stix",
                "json"
              ],
              "default": "json"
            },
            "required": true,
            "description": "Export format"
          },
          {
            "in": "path",
            "name": "profile_id",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Threat Profile's ID"
          },
          {
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Your API key"
          }
        ],
        "operationId": "get_threat-profiles-profile-id-download-url-format",
        "summary": "Export URL for Large IoC Packages"
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

← [Export IoCs](threat-profile-download.md) · [up](../README.md) · [Dark Web](../dark-web.md) →

*Archived from <https://gtidocs.virustotal.com/reference/threat-profile_download-url>.*
