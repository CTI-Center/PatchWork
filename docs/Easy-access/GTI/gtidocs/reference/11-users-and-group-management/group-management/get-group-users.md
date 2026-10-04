---
title: "Get group users"
source: https://gtidocs.virustotal.com/reference/get-group-users
slug: get-group-users
section: reference
group: "Users and group management"
updatedAt: 2026-02-09T10:10:51.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Users and group management](../README.md) › [Group Management](../group-management.md) › Get group users

---

# get-group-users

Returns a list of group [members descriptors](../../17-api-objects/user-object.md), including their assigned group roles, feature-specific privileges, and any individual quota overrides that are lower than the group defaults as follows:

```json
{
    "data": [
        {
            "type": "user",
            "id": "\<_string_> user ID.",
            "context_attributes": {
                "role": "\<_string_> user group role as \"admin\" or \"user\".",
                "quota_limits": "\<_dictionary_> a dictionary of quota overrides. These entries appear only when a user's individual allowance is configured to be lower than the group’s default.",
                "roles": "\<_list of strings_> a list of privileges assigned to the user within the group, such as USER_ROLE_GROUP_ADMIN, USER_ROLE_PRIVATE_SCANNING, USER_ROLE_FILE_DOWNLOADS, USER_ROLE_DTM_ADMIN, USER_ROLE_ASM_USER, etc."
            }
        }
    ]
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
    "/groups/{id}/relationships/users": {
      "get": {
        "tags": [
          "Group Management"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-group-users",
        "parameters": [
          {
            "description": "Group ID",
            "in": "path",
            "name": "id",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Your API key.",
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
        "summary": "Get group users"
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

← [Check if a user is a group admin](check-user-group-administrator.md) · [up](../README.md) · [Add users to a group](update-group-users.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-group-users>.*
