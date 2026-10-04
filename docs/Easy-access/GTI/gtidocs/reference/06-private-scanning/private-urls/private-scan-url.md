---
title: "Private Scan URL"
source: https://gtidocs.virustotal.com/reference/private-scan-url
slug: private-scan-url
section: reference
group: "Private Scanning"
updatedAt: 2025-09-25T00:37:17.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Private Scanning](../README.md) › [Private URLs](../private-urls.md) › Private Scan URL

---

# private-scan-url

This returns an [Analysis](../../17-api-objects/analyses-object.md) ID. The analysis can be retrieved by using the [Analysis](get-a-private-url-analysis-report.md) endpoint.

### analysis-observations:

To get a more comprehensive analysis and gather different kinds of information beyond what a typical sandbox provides, you should use `chrome_headless_linux` as an additional or specific type of sandbox environment.

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
      "name": "Private URLs"
    }
  ],
  "paths": {
    "/urls": {
      "post": {
        "tags": [
          "Private URLs"
        ],
        "summary": "Private Scan URL",
        "description": "",
        "operationId": "private-scan-url",
        "parameters": [
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
        "requestBody": {
          "content": {
            "application/x-www-form-urlencoded": {
              "schema": {
                "type": "object",
                "required": [
                  "url"
                ],
                "properties": {
                  "url": {
                    "type": "string",
                    "description": "URL to scan."
                  },
                  "user_agent": {
                    "type": "string",
                    "description": "User agent string."
                  },
                  "sandboxes": {
                    "type": "string",
                    "description": "Comma separated eg: `chrome_headless_linux,cape_win,zenbox_windows` possible values `chrome_headless_linux`, `cape_win` and `zenbox_windows`."
                  },
                  "retention_period_days": {
                    "description": "Optional, number of days the report and URL are kept in VT (between 1 and 28). If not set it defaults to the group's retention policy preference (1 day by default).",
                    "type": "integer",
                    "default": 1,
                    "format": "int32",
                    "maximum": 28,
                    "minimum": 1
                  },
                  "storage_region": {
                    "description": "Optional, storage region where the URL will be stored. By default uses the group's private_scanning.storage_region preference. Allowed values are US, CA, EU, GB",
                    "type": "string",
                    "enum": [
                      "US",
                      "CA",
                      "EU",
                      "GB"
                    ]
                  },
                  "interaction_sandbox": {
                    "default": "cape_win",
                    "description": "Select the sandbox desired for interactive use, possible values `cape_win`.",
                    "type": "string"
                  },
                  "interaction_timeout": {
                    "description": "Interaction timeout in seconds, minimum value: 60. (1 minute.) Max value: 1800: (30 minutes)",
                    "type": "integer",
                    "default": 60,
                    "format": "int32",
                    "maximum": 1800,
                    "minimum": 60
                  }
                }
              }
            }
          }
        },
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
        "deprecated": false
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

← [Private URLs](../private-urls.md) · [up](../README.md) · [Get a URL analysis report](get-a-private-url-analysis-report.md) →

*Archived from <https://gtidocs.virustotal.com/reference/private-scan-url>.*
