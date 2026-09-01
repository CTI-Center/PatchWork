---
title: "Export IoCs"
source: https://gtidocs.virustotal.com/reference/threat-profile-download
slug: threat-profile-download
section: reference
group: "Global Landscape"
updatedAt: 2026-05-25T08:19:58.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Global Landscape](../README.md) › [Threat Profiles](../threat-profiles.md) › Export IoCs

---

# export-iocs

Use this endpoint to export Indicators of Compromise (IoCs) associated with all Recommendations in a certain Threat Profile. Supported formats include JSON, CSV, and STIX.

> 📘
>
> Note that if the `/format` parameter is omitted, this endpoint defaults to JSON.

> 📘
>
> Please note that this endpoint only supports exports under 32 MB. For larger exports, use [this endpoint](red:threat_profile_download_url) instead.

# examples

Get 10 IoCs of each type that are associated with recommendations in my threat profile, in JSON format.

```python
import requests

id = "dc2f47a9baa2460089cdd78f7339b19c"
limit = 10 
url = f"https://www.virustotal.com/api/v3/threat_profiles/{id}/download?limit={limit}"

headers = {"x-apikey": <api-key>,"accept": "application/json"}

response = requests.get(url, headers=headers)
```

Get all IoCs that are associated with recommendations in my threat profile, in CSV format.

```python
import requests

id = "dc2f47a9baa2460089cdd78f7339b19c"
format = "csv" 

url = f"https://www.virustotal.com/api/v3/threat_profiles/{id}/download/{format}"

headers = {"x-apikey": <api-key>,"accept": "application/json"}

response = requests.get(url, headers=headers)
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
    "/threat_profiles/{profile_id}/download/{format}": {
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
                  "properties": {}
                }
              }
            }
          }
        },
        "parameters": [
          {
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            },
            "description": "Your API key",
            "required": true
          },
          {
            "in": "path",
            "name": "format",
            "schema": {
              "type": "string",
              "enum": [
                "json",
                "csv",
                "stix"
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
            "in": "query",
            "name": "limit",
            "schema": {
              "type": "string"
            },
            "description": "Maximum number of IoCs per type"
          }
        ],
        "operationId": "get_threat-profiles-profile-id-download-format",
        "summary": "Export IoCs"
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

← [Get a Threat Profile's timeline associations](get-threat-profile-timeline-associations.md) · [up](../README.md) · [Export URL for Large IoC Packages](threat-profile_download-url.md) →

*Archived from <https://gtidocs.virustotal.com/reference/threat-profile-download>.*
