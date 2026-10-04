---
title: "Delete associations, IoCs and TTPs from a report"
source: https://gtidocs.virustotal.com/reference/delete-element-from-report
slug: delete-element-from-report
section: reference
group: "Reports & Analysis"
updatedAt: 2026-04-15T07:47:57.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Reports & Analysis](../README.md) › [Reports](../reports.md) › Delete associations, IoCs and TTPs from a report

---

# delete-associations,-iocs-and-ttps-from-a-report

As the owner, you can use this endpoint to remove elements such as **IoCs**, **Attack Techniques** and other **associations** from any of your [Reports](../../17-api-objects/report-object.md).

> ❗️
>
> This endpoint is currently in **Private Preview**.

Commonly used **relationships** are listed below. For the full specification, see the complete list [here](../../17-api-objects/report-object.md#relationships).

* `associations`: it allows you to disassociate the following object types: threat actor, malware family, software or toolkit, IoC collection, vulnerability.
* `reports`: it allows you to disassociate reports.
* `attack_techniques`: it allows you disassociate attack techniques.
* `files`,`domains`,`urls`,`ip_addresses`: they allow you to disassociate IoCs.

As showed in the object creation request body template [here](create-report.md), for the `urls` relationship you either use `{"type": "url", "url": <a URL string>}` or `{"type": "url", "id": <a sha256 URL identifier>}` as object descriptors. For domains and IP addresses you can use `{"type": "domain", "id": <a domain>}` or `{"type": "ip_address", "id": <an IP address>}`.

## examples

Delete an element, `google.com` domain, from your report--0efaa5e4a4b94c54aae31ec28922c37b report.

```python
import requests

object_id = "report--0efaa5e4a4b94c54aae31ec28922c37b"
relationship = "domains"
url = f"https://www.virustotal.com/api/v3/collections/{object_id}/{relationship}"
payload = { "data": 
    [
        {
            "type": "domain",
            "id": "google.com"
        }
    ]
}
headers = {
    "accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"
}
response = requests.delete(url, json=payload, headers=headers)
```

Disassociate the CVE-2026-39958 vulnerability from your report--0efaa5e4a4b94c54aae31ec28922c37b report.

```python
import requests

object_id = "report--0efaa5e4a4b94c54aae31ec28922c37b"
relationship = "associations"
url = f"https://www.virustotal.com/api/v3/collections/{object_id}/relationships/{relationship}"

payload = { "data": 
    [
        {
            "type": "collection",
            "id": "vulnerability--cve-2026-39958"
        }
    ]
}
headers = {
    "accept": "application/json","x-apikey": <api-key>,"content-type": "application/json"
}
response = requests.delete(url, json=payload, headers=headers)
```

Disassociate the report--26-10018712 report from your report.

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
response = requests.delete(url, json=payload, headers=headers)
```

Unlink the T1087 attack technique from your report.

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
response = requests.delete(url, json=payload, headers=headers)
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
      "delete": {
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
                    "description": "Objects descriptors",
                    "format": "json"
                  }
                },
                "required": [
                  "data"
                ]
              }
            }
          }
        },
        "operationId": "delete_collections-id-relationships-relationship"
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

← [Add new associations, IoCs or TTPs to a report](add-element-to-report.md) · [up](../README.md) · [Get object descriptors related to a report](get-report-related-descriptors.md) →

*Archived from <https://gtidocs.virustotal.com/reference/delete-element-from-report>.*
