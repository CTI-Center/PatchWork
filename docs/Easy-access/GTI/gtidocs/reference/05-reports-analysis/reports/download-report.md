---
title: "Download a Report"
source: https://gtidocs.virustotal.com/reference/download-report
slug: download-report
section: reference
group: "Reports & Analysis"
updatedAt: 2025-09-25T00:36:48.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Reports & Analysis](../README.md) › [Reports](../reports.md) › Download a Report

---

# download-a-report

> 🚧 Special privileges required
>
> Reports & Analysis are only available to users with the Google Threat Intelligence (Google TI) Enterprise or Enterprise Plus licenses.

This endpoint allows you to download a generated report in PDF format.

`curl --request GET 'https://www.virustotal.com/api/v3/collections/report--25-10000400/download_report' --header 'x-apikey: <your API key>'`

```json
{
    "data": "https://vtcollectionreports.commondatastorage.googleapis.com/collection-pdf-report/xxxxxx"
}
```

# openapi-definition

```json
{
  "info": {
    "title": "Reports & Analysis",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Reports",
      "description": "Reports & Analysis endpoints"
    }
  ],
  "paths": {
    "/collections/{id}/download_report": {
      "get": {
        "tags": [
          "Reports"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "download-report",
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
            "description": "Report's ID",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/pdf": {}
            },
            "description": "200"
          }
        },
        "security": [],
        "summary": "Download a Report"
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

← [Export IOCs from a given report's relationship](export-iocs-report-relationship.md) · [up](../README.md) · [Subscribe to a report](create-report-subscription-preferences.md) →

*Archived from <https://gtidocs.virustotal.com/reference/download-report>.*
