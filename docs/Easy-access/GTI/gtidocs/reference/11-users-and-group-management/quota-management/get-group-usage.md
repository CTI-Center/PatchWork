---
title: "Get a group's usage per feature"
source: https://gtidocs.virustotal.com/reference/get-group-usage
slug: get-group-usage
section: reference
group: "Users and group management"
updatedAt: 2026-01-23T12:02:17.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Users and group management](../README.md) › [Quota Management](../quota-management.md) › Get a group's usage per feature

---

# get-a-group's-usage-per-feature

This endpoint retrieves a group's usage data for a **specified feature**, **broken down by user**.

```json Example response
{
    "data": /* <_list of dictionaries_> List of users */
    [
        {
            "id": "<_string_> User identifier",
            "type": "user",
            "links":
            {
                "self": "https://www.virustotal.com/api/v3/users/<user identifier>"
            },
            "attributes": "<_dictionary_> User object attributes. When the 'attributes' request parameter is used, only specified attributes are listed. ",
            "relationships": /* <_list of dictionaries_> (optional) List of objects descriptors related to the user. It is included only when the 'relationships' request parameter is used. */
            {
                "<_string_> Relationship name":
                {
                    "data": /* <_list of dictionaries_> List of objects descriptors. */
                    [
                        {
                            "type": "<_string_> Object type",
                            "id": "<_string_> Object identifier"
                        }
                    ],
                    "links":
                    {
                        "self": "https://www.virustotal.com/api/v3/users/<user identifier>/relationships/<relationship name>?limit=20",
                        "related": "https://www.virustotal.com/api/v3/users/<user identifier>/<object type>"
                    }
                }
            },
            "context_attributes":
            {
                "quota_consumed_from_group": "<_integer_> Consumed specified feature quota"
            }
        }
    ],
    "links":
    {
        "self": "https://www.virustotal.com/api/v3/groups/gti_testers/users_consuming_quota/..."
    }
}
```

By default, all user attributes are included. To retrieve a specific subset, provide a comma-separated list of desired [user attributes](../../17-api-objects/user-object.md#object-attributes) using the `attributes` request parameter.

Additionally, you can specify the desired types of user relationships (e.g., votes, graphs, comments, or mentions) by providing a comma-separated list of them using the `relationships` request parameter.

You can also sort users by their consumption of the chosen feature, in either ascending (`asc`) or descending (`desc`) order, using the `order` request parameter.

> 🚧 Time range restrictions
>
> This endpoint supports a maximum time range of the current and the 2 previous months. The `period` request parameter can be specified in two formats (YYYY-MM, YYYY-MM-DD), depending on the requested feature, to retrieve data for a particular month.

Available features and `period` formats are:

* `intelligence_hunting_rules` - count of active Livehunt jobs per user. They are not tied to a period of time so they don't support the `period` request parameter.
* `api_requests_daily` - daily count of API requests per user. `period` formats: YYYY-MM (complete month consumption), YYYY-MM-DD (specific day consumption).
* `api_requests_monthly` - monthly count of API requests per user. `period` formats: YYYY-MM (complete month consumption), YYYY-MM-DD (specific day consumption).
* `intelligence_downloads_monthly` - monthly count of files downloads per user. `period` format: YYYY-MM.
* `intelligence_retrohunt_jobs_monthly` - monthly count of Retrohunt jobs per user. `period` format: YYYY-MM.
* `intelligence_vtdiff_creation_monthly` - monthly count of VTDiff jobs per user. `period` format: YYYY-MM.
* `intelligence_searches_monthly` - monthly count of Intelligence Searches per user. `period` format: YYYY-MM.
* `private_scans_monthly` - monthly count of File Private Scans per user. `period` format: YYYY-MM.
* `private_urlscans_monthly` - monthly count of URL Private Scans per user. `period` format: YYYY-MM.

If the `period` parameter is not specified, you will get the current month consumption.

# examples

Get consumption of web interface intelligence searches from the past month (2025-04).

```python
import requests

id = "your group identifier"
quota_name = "intelligence_searches_monthly"

url = f"https://www.virustotal.com/api/v3/groups/{id}/users_consuming_quota/{quota_name}?period=2025-04"
headers = {"accept": "application/json","x-apikey": <api-key>}
response = requests.get(url, headers=headers)
```

Get API consumption from 2025-05-06 of all users and their votes and comments.

```python
import requests

id = "your group identifier"
quota_name = "api_requests_daily"

url = f"https://www.virustotal.com/api/v3/groups/{id}/users_consuming_quota/{quota_name}?period=2025-05-06&relationships=votes,comments"
headers = {"accept": "application/json","x-apikey": <api-key>}
response = requests.get(url, headers=headers)
```

List 10 users (email address and 2FA status) who have downloaded the most files in the last month, via web interface.

```python
import requests

id = "your group identifier"
quota_name = "intelligence_downloads_monthly"
attributes = "email,has_2fa"

url = f"https://www.virustotal.com/api/v3/groups/{id}/users_consuming_quota/{quota_name}?order=desc&limit=10&attributes={attributes}"
headers = {"accept": "application/json","x-apikey": <api-key>}
response = requests.get(url, headers=headers)
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
      "name": "Quota Management"
    }
  ],
  "paths": {
    "/groups/{id}/users_consuming_quota/{quota_name}": {
      "get": {
        "tags": [
          "Quota Management"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "get-group-usage",
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
            "description": "Quota name",
            "in": "path",
            "name": "quota_name",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
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
            "description": "A string in format YYYY-MM-DD (for daily quotas) or YYYY-MM (for monthly quotas)",
            "in": "query",
            "name": "period",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Maximum number of users quota to retrieve (Max 40)",
            "in": "query",
            "name": "limit",
            "schema": {
              "default": 10,
              "format": "int32",
              "type": "integer",
              "maximum": 40,
              "minimum": 0
            }
          },
          {
            "description": "Sort users based on their consumption ('desc' for descendant, 'asc' for ascendant)",
            "in": "query",
            "name": "order",
            "schema": {
              "default": "desc",
              "type": "string"
            }
          },
          {
            "description": "Comma-separated users' attributes to return (by default, all attributes are returned)",
            "in": "query",
            "name": "attributes",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Comma-separated users' [relationships](https://gtidocs.readme.io/reference/user-object#relationships) to return (by default, no relationships are returned)",
            "in": "query",
            "name": "relationships",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Continuation cursor",
            "in": "query",
            "name": "cursor",
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
                    "value": "{}"
                  }
                },
                "schema": {
                  "properties": {},
                  "type": "object"
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
        "summary": "Get a group's certain feature usage"
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

← [Get a group’s API usage](group-api-usage.md) · [up](../README.md) · [Service Account Management](../service-account-management.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get-group-usage>.*
