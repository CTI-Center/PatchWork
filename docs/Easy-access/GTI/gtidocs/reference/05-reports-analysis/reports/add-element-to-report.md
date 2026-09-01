---
title: "Add new associations, IoCs or TTPs to a report"
source: https://gtidocs.virustotal.com/reference/add-element-to-report
slug: add-element-to-report
section: reference
group: "Reports & Analysis"
updatedAt: 2026-04-15T07:47:05.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Reports & Analysis](../README.md) › [Reports](../reports.md) › Add new associations, IoCs or TTPs to a report

---

# add-new-associations,-iocs-or-ttps-to-a-report

As the owner, you can use this endpoint to add elements such as **IoCs**, **Attack Techniques** and other **associations** to any of your [Reports](../../17-api-objects/report-object.md).

> ❗️
>
> This endpoint is currently in **Private Preview**.

Commonly used **relationships** are listed below. For the full specification, see the complete list [here](../../17-api-objects/report-object.md#relationships).

* `associations`: it allows you to associate the following object types: threat actor, malware family, software or toolkit, IoC collection, vulnerability.
* `reports`: it allows you to associate reports.
* `attack_techniques`: it allows you associate attack techniques.
* `files`,`domains`,`urls`,`ip_addresses`: they allow you to associate IoCs.

As showed in the object creation request body template [here](create-report.md), for the `urls` relationship you either use `{"type": "url", "url": <a URL string>}` or `{"type": "url", "id": <a sha256 URL identifier>}` as object descriptors. For domains and IP addresses you can use `{"type": "domain", "id": <a domain>}` or `{"type": "ip_address", "id": <an IP address>}`.

## examples

Add new elements, `google.com` and `virustotal.com` domains, to an owned report.

```python
import requests

object_id = "report--0efaa5e4a4b94c54aae31ec28922c37b"
relationship = "domains"
url = f"https://www.virustotal.com/api/v3/collections/{object_id}/relationships/{relationship}"

payload = { "data": 
    [
        {
            "type": "domain",
            "id": "google.com"
        },
        {
            "type": "domain",
            "id": "virustotal.com"
        }
    ]
}
headers = {
    "accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"
}
response = requests.post(url, json=payload, headers=headers)
```

Associate your report--0efaa5e4a4b94c54aae31ec28922c37b report with the malware--f872b3e0-c277-5716-baae-885a9c410398 Software or Toolkit, and the CVE-2026-39958 vulnerability.

```python
import requests

object_id = "report--0efaa5e4a4b94c54aae31ec28922c37b"
relationship = "associations"
url = f"https://www.virustotal.com/api/v3/collections/{object_id}/relationships/{relationship}"

payload = { "data": 
    [
        {
            "type": "collection",
            "id": "malware--f872b3e0-c277-5716-baae-885a9c410398"
        },
        {
            "type": "collection",
            "id": "vulnerability--cve-2026-39958"
        }
    ]
}
headers = {
    "accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"
}
response = requests.post(url, json=payload, headers=headers)
```

Associate your report--0efaa5e4a4b94c54aae31ec28922c37b report with the the report--26-10018712 report.

```python
import requests

object_id = "report--0efaa5e4a4b94c54aae31ec28922c37b"
relationship = "reports"
url = f"https://www.virustotal.com/api/v3/collections/{object_id}/relationships/{relationship}"

payload = { "data": 
    [
        {
            "type": "collection",
            "id": "report--26-10018712"
        }
    ]
}
headers = {
    "accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"
}
response = requests.post(url, json=payload, headers=headers)
```

Link the T1087 attack technique to your report.

```python
import requests

object_id = "report--0efaa5e4a4b94c54aae31ec28922c37b"
relationship = "attack_techniques"
url = f"https://www.virustotal.com/api/v3/collections/{object_id}/relationships/{relationship}"

payload = { "data": 
    [
        {
          "type": "attack_technique", 
          "id": "T1087"
        }
    ]
}
headers = {
    "accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"
}
response = requests.post(url, json=payload, headers=headers)
```

# openapi-definition

```json
{
  "info": {
    "title": "Reports & Analysis",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "paths": {
    "/collections/{id}/relationships/{relationship}": {
      "post": {
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
            "in": "path",
            "name": "id",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Report's id"
          },
          {
            "in": "path",
            "name": "relationship",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Relationship name (see [table](https://gtidocs.readme.io/reference/report-object#relationships))"
          },
          {
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            },
            "description": "Your API key"
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "data": {
                    "type": "string",
                    "format": "json",
                    "description": "Object descriptor"
                  }
                },
                "required": [
                  "data"
                ]
              }
            }
          }
        },
        "operationId": "post_collections-id-relationships-relationship"
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

← [Update a report](update-report.md) · [up](../README.md) · [Delete associations, IoCs and TTPs from a report](delete-element-from-report.md) →

*Archived from <https://gtidocs.virustotal.com/reference/add-element-to-report>.*
