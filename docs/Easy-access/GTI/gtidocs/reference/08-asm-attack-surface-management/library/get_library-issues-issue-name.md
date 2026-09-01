---
title: "Issues List - Specific Isssue"
source: https://gtidocs.virustotal.com/reference/get_library-issues-issue-name
slug: get_library-issues-issue-name
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:35.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Library](../library.md) › Issues List - Specific Isssue

---

# issues-list---specific-isssue

Send a specific entity type, and get the definition

# openapi-definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "ASM (ATTACK SURFACE MANAGEMENT)",
    "version": "1.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3/asm"
    }
  ],
  "tags": [
    {
      "name": "Library"
    }
  ],
  "paths": {
    "/library/issues/{issue_name}": {
      "get": {
        "tags": [
          "Library"
        ],
        "summary": "Issues List - Specific Isssue",
        "description": "",
        "parameters": [
          {
            "name": "issue_name",
            "in": "path",
            "schema": {
              "type": "string"
            },
            "required": true,
            "example": "missing_dmarc_policy"
          },
          {
            "description": "Your API key",
            "in": "header",
            "name": "x-apikey",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "headers": {
              "Date": {
                "schema": {
                  "type": "string",
                  "example": "Wed, 10 Mar 2021 16:37:45 GMT"
                }
              },
              "Content-Type": {
                "schema": {
                  "type": "string",
                  "example": "application/json"
                }
              },
              "Transfer-Encoding": {
                "schema": {
                  "type": "string",
                  "example": "chunked"
                }
              },
              "Connection": {
                "schema": {
                  "type": "string",
                  "example": "keep-alive"
                }
              },
              "Set-Cookie": {
                "schema": {
                  "type": "string",
                  "example": "rack.session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVG86HVJhY2s6OlNlc3Npb246OlNlc3Npb25JZAY6D0BwdWJsaWNfaWRJIkUxZDEwOWVjZjNhZjg2ZjQyZjVhMWU5NDIzNjQ2ODVhYjc5NWMwZTZlMTgyYjE0NzgyNjVmMTYzMDEyZGRkZTg2BjsARkkiFXBvc3Rfc2lnbmluX3BhdGgGOwBGIgwvc2lnbmlu--599b4fb47fdf41d17c27205eed3f5a751e993ea4; path=/; expires=Fri, 09 Apr 2021 16:37:45 GMT; HttpOnly"
                }
              },
              "X-Content-Type-Options": {
                "schema": {
                  "type": "string",
                  "example": "nosniff"
                }
              },
              "Vary": {
                "schema": {
                  "type": "string",
                  "example": "Origin"
                }
              },
              "Via": {
                "schema": {
                  "type": "string",
                  "example": "1.1 vegur"
                }
              },
              "CF-Cache-Status": {
                "schema": {
                  "type": "string",
                  "example": "DYNAMIC"
                }
              },
              "cf-request-id": {
                "schema": {
                  "type": "string",
                  "example": "08be99725300000f3e05850000000001"
                }
              },
              "Expect-CT": {
                "schema": {
                  "type": "string",
                  "example": "max-age=604800, report-uri=\"https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct\""
                }
              },
              "Report-To": {
                "schema": {
                  "type": "string",
                  "example": "{\"max_age\":604800,\"group\":\"cf-nel\",\"endpoints\":[{\"url\":\"https:\\/\\/a.nel.cloudflare.com\\/report?s=VakeRmXj8nJPabhkHVXvRNJO0Z7fVKooBSDnFkUxS1Y0BKovdBNZCtfx5IJD3LENGk2rkZwYAFYU5CDfE%2BcAvuTkLQd8dotV28ZCMWyXX1Y%3D\"}]}"
                }
              },
              "NEL": {
                "schema": {
                  "type": "string",
                  "example": "{\"max_age\":604800,\"report_to\":\"cf-nel\"}"
                }
              },
              "Server": {
                "schema": {
                  "type": "string",
                  "example": "cloudflare"
                }
              },
              "CF-RAY": {
                "schema": {
                  "type": "string",
                  "example": "62ddf8308b2b0f3e-DFW"
                }
              },
              "Content-Encoding": {
                "schema": {
                  "type": "string",
                  "example": "br"
                }
              }
            },
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                },
                "example": {
                  "success": true,
                  "message": "success",
                  "result": {
                    "added": "2020-01-01",
                    "name": "missing_dmarc_policy",
                    "pretty_name": "Missing DMARC Policy",
                    "category": "misconfiguration",
                    "source": "DNS",
                    "severity": 4,
                    "status": "confirmed",
                    "description": "DMARC is a policy (configured in a DNS record) that explains the email authentication practices for a given domain. When configured, it helps prevent spam and other abuses. In practice, it simply provides a receiving mail server (upon receipt of a new email) with enough information to  determine the validity of a sender. All domains configured to send email should implement DMARC, as it is one of the most important steps that can be taken to improve email deliverability.",
                    "references": [
                      {
                        "type": "description",
                        "uri": "https://www.sparkpost.com/resources/email-explained/dmarc-explained/"
                      },
                      {
                        "type": "description",
                        "uri": "https://www.sonicwall.com/support/knowledge-base/what-is-a-dmarc-record-and-how-do-i-create-it-on-dns-server/170504796167071/"
                      }
                    ]
                  }
                }
              }
            }
          }
        }
      }
    }
  },
  "x-readme": {
    "explorer-enabled": true,
    "proxy-enabled": false,
    "samples-enabled": true
  }
}
```

---

← [Issues List](get_library-issues.md) · [up](../README.md) · [Issues Stats](get_library-issues-stats.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_library-issues-issue-name>.*
