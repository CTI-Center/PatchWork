---
title: "Update SAML configuration of a group."
source: https://gtidocs.virustotal.com/reference/groups-patch-samlconfig
slug: groups-patch-samlconfig
section: reference
group: "Users and group management"
updatedAt: 2025-09-25T00:39:03.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Users and group management](../README.md) › [Group Management](../group-management.md) › Update SAML configuration of a group.

---

# update-saml-configuration-of-a-group.

This request accepts a JSON body containing the group saml configuration attributes to update. Attributes not present in the request body remain the same. It returns the updated configuration.

```json Example response
{
  "data": {
    "idp_entity_id": "https://sts.example.com/12345678-1234-1234-1234-1234567890ab/",
    "sso_url": "https://sso.example.com/12345678-1234-1234-1234-1234567890ab/saml2",
    "x509_certificates": [
      "-----BEGIN CERTIFICATE-----\n[... CERTIFICATE CONTENT ...]\n-----END CERTIFICATE-----\n"
    ],
    "rp_entity_id": "ExampleVirusTotalSSO",
    "force_users_saml_login": false,
    "login_url": "https://www.virustotal.com/gui/sso/[...encoded_string...]"
  }
}
```

# openapi-definition

```json
{
  "info": {
    "title": "Users and group management",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Group Management"
    }
  ],
  "paths": {
    "/groups/{id}/saml_config": {
      "patch": {
        "tags": [
          "Group Management"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "groups-patch-samlconfig",
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
            "description": "Group ID",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "properties": {
                  "data": {
                    "description": "A SAML configuration object",
                    "format": "json",
                    "type": "string"
                  }
                },
                "required": [
                  "data"
                ],
                "type": "object"
              }
            }
          }
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": ""
                  }
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
        "security": [],
        "summary": "Update SAML configuration of a group."
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

← [Get SAML configuration details of a group.](groups-get-samlconfig.md) · [up](../README.md) · [Delete SAML configuration of a group.](groups-del-samlconfig.md) →

*Archived from <https://gtidocs.virustotal.com/reference/groups-patch-samlconfig>.*
