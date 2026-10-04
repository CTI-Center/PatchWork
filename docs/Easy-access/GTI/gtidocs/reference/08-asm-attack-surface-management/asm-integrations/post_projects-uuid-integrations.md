---
title: "Create"
source: https://gtidocs.virustotal.com/reference/post_projects-uuid-integrations
slug: post_projects-uuid-integrations
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:42.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [ASM Integrations](../asm-integrations.md) › Create

---

# create

Attack Surface Management currently supports the following integrations, Use the samples in the post body:

_**GCP**_:

``` json
{
  "name": "Test GCP Integration",
  "secrets": {
    "service_account_email": "Email.Address@Service-Account-here.com"
  },
  "type": "GcpCredential"
}

 ```

**Jira:**

``` json
{
    "name": "Test JIRA Integration",
    "secrets": {
        "jira_api_key": "APIKEYHERE",
        "host": "hostname.com",
        "username": "Email.Address@here.com"
    },
    "type": "jira"
}

 ```

**Azure:**

``` json
{
    "name": "Test Azure Integration",
    "secrets": {
        "tenant_id": "TenantIdhere"
    },
    "type": "azure"
}

 ```

**Github:**

``` json
{
    "name": "Test github Integration",
    "secrets": {
        "github_access_token": "TokenHere"
    },
    "type": "github"
}

 ```

**Akamai:**

``` json
  {
    "name": "Test akamai Integration",
    "secrets": {
        "client_secret": "SecretHere",
        "host": "hosthere.com",
        "access_token": "AccessTokenHere",
        "client_token": "ClientTokenHere"
    },
    "type": "akamai"
}

 ```

**Godaddy:**

``` json
{
    "name": "Test godaddy Integration",
    "secrets": {
        "api_key": "KeyHere",
        "api_secret": "SecretHere"
    },
    "type": "godaddy"
}

 ```

**Cloudflare:**

``` json
{
    "name": "Test cloudflare Integration",
    "secrets": {
        "cloudflare_api_key": "APIKeyHere"
    },
    "type": "cloudflare"
}

 ```

**AWS Roles:**

``` json
{
    "name": "Test AwsCredential Integration",
    "secrets": {
        "aws_role_arn": "RoleHere"
    },
    "type": "AwsCredential"
}

 ```

**AWS Keys:**

``` json
{
    "name": "Test AwsCredential Integration",
    "secrets": {
        "aws_access_key_id": "KeyHere",
        "aws_secret_access_key": "SecretHere",
    },
    "type": "AwsCredential"
}

 ```

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
      "name": "ASM Integrations",
      "description": "Add your integration(s) here. Once added you can associate them to a collection within the Integrations Collections section."
    }
  ],
  "paths": {
    "/projects/{uuid}/integrations": {
      "post": {
        "tags": [
          "ASM Integrations"
        ],
        "summary": "Create",
        "description": "",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "example": {
                  "name": "Test JIRA Integration",
                  "secrets": {
                    "jira_api_key": "APIKEYHERE",
                    "host": "hostname.com",
                    "username": "Email.Address@here.com"
                  },
                  "type": "jira"
                }
              }
            }
          }
        },
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
            "name": "uuid",
            "in": "path",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Required: uuid from /api/v3/asm/projects",
            "example": "{{project_uuid}}"
          }
        ],
        "responses": {
          "200": {
            "description": "Successful response",
            "content": {
              "application/json": {}
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

← [ASM Integrations](../asm-integrations.md) · [up](../README.md) · [Index](get_projects-uuid-integrations.md) →

*Archived from <https://gtidocs.virustotal.com/reference/post_projects-uuid-integrations>.*
