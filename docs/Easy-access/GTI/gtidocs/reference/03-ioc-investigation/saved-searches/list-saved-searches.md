---
title: "List Saved Searches"
source: https://gtidocs.virustotal.com/reference/list-saved-searches
slug: list-saved-searches
section: reference
group: "IoC Investigation"
updatedAt: 2025-12-05T14:27:20.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [IoC Investigation](../README.md) › [Saved Searches](../saved-searches.md) › List Saved Searches

---

# list-saved-searches

<br />

Use this endpoint to list [Saved Searches](../../17-api-objects/saved-search-object.md) you have access to as owner, editor or viewer.

# filters

Available filters for saved searches:

* `creation_date`: filters saved searches by their last modification date, accepting either the `YYYY-MM-DDTHH:MM:SS` format or an Epoch UTC timestamp format. E.g.:`creation_date:2025-10-27+`, `creation_date:2025-11-27T01:15:09`, `creation_date:2025-09-15-`, `creation_date:1764326675-`.
* `last_modification_date`: filters saved searches by their last modification date, accepting either the `YYYY-MM-DDTHH:MM:SS` format or an Epoch UTC timestamp format. E.g.:`last_modification_date:2025-10-28+`, `last_modification_date:2025-10-27T09:31:25`, `last_modification_date:2025-10-26-`, `last_modification_date:1763721875+`.
* `shared_with_me:true`: filters saved searches that were created by other users but shared with the current one. Note that this filter only supports the `true` value.
* `origin`: filters saved searches by their origin. Available options: **Crowdsourced** for those created by the community, **Google Threat Intelligence** for those created GTIG team and **Partner** for those created by trusted partners. E.g.: `origin:Crowdsourced`, `origin:"Google Threat Intelligence"`.
* `owner`: filters saved searches based on their creator/owner user identifier. It is particularly useful for listing saved searches created by users whose content you trust or want to follow. E.g.:`owner:<user_id>`.
* `editor`: filters saved searches editable by a specified user. E.g.:`editor:<user_id>`.
* `viewer`: Filters saved searches viewable by a specified user. E.g.:`viewer:<user_id>`.

# orders

Available sorting options for saved searches:

* `creation_date`: sorts saved searches by their last modification date ascending (`+`) or descending (`-`). E.g.:`creation_date+`, `creation_date-`.
* `last_modification_date`: sorts saved searches by their last modification date ascending (`+`) or descending (`-`). E.g.:`last_modification_date+`, `last_modification_date-` (default order).
* `name`: sorts saved searches by their name ascending (`+`) or descending (`-`). E.g.:`name+`, `name-`.

# examples

List all of my saved searches, including their editors, and display only the name and description.

```python
import requests
import urllib
 
filters = "shared_with_me:true"
relationships = "editors"
attributes = "name,description"
 
url = f"https://www.virustotal.com/api/v3/saved_searches?filter={urllib.parse.quote(filters)}&relationships={relationships}&attributes={attributes}"
 
headers = {"accept": "application/json","x-apikey": <api-key>}
 
response = requests.get(url, headers=headers)
```

Retrieve saved searches created by Ana during August and September 2025.

```python
import requests
import urllib
 
filters = "owner:ana creation_date:2025-08-01+ creation_date:2025-10-01+"
 
url = f"https://www.virustotal.com/api/v3/saved_searches?filter={urllib.parse.quote(filters)}"
 
headers = {"accept": "application/json","x-apikey": <api-key>}
 
response = requests.get(url, headers=headers)
```

List all saved searches created by the Google Threat Intelligence team.

```python
import requests
import urllib
 
filters = "origin:'Google Threat Intelligence'"
 
url = f"https://www.virustotal.com/api/v3/saved_searches?filter={urllib.parse.quote(filters)}"
 
headers = {"accept": "application/json","x-apikey": <api-key>}
 
response = requests.get(url, headers=headers)
```

# openapi-definition

```json
{
  "info": {
    "title": "IoC Investigation",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "paths": {
    "/saved_searches": {
      "get": {
        "description": "",
        "operationId": "get_saved_searches",
        "responses": {
          "200": {
            "description": "200"
          },
          "400": {
            "description": "400",
            "content": {}
          }
        },
        "parameters": [
          {
            "in": "query",
            "name": "filter",
            "schema": {
              "type": "string"
            },
            "description": "Filter saved searches by different properties."
          },
          {
            "in": "header",
            "name": "x-apikey",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Your API Key."
          },
          {
            "in": "query",
            "name": "cursor",
            "schema": {
              "type": "string"
            },
            "description": "Continuation cursor."
          },
          {
            "in": "query",
            "name": "limit",
            "schema": {
              "type": "integer",
              "default": "10"
            },
            "description": "Maximum number of saved searches to retrieve. The maximum value is 40."
          },
          {
            "in": "query",
            "name": "order",
            "schema": {
              "type": "string",
              "default": "last_modification_date-"
            },
            "description": "Sorting order."
          },
          {
            "in": "query",
            "name": "relationships",
            "schema": {
              "type": "string",
              "enum": [
                "owner",
                "editors",
                "viewers"
              ]
            }
          },
          {
            "in": "query",
            "name": "attributes",
            "schema": {
              "type": "string"
            },
            "description": "A comma-separated list of the [_saved search attributes_](https://gtidocs.readme.io/reference/saved-search-object#object-attributes) to be returned. (All attributes are returned by default.)"
          }
        ]
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

← [Saved Searches](../saved-searches.md) · [up](../README.md) · [Get a Saved Search](get-saved-searches.md) →

*Archived from <https://gtidocs.virustotal.com/reference/list-saved-searches>.*
