---
title: "Search graphs"
source: https://gtidocs.virustotal.com/reference/graphs
slug: graphs
section: reference
group: "Threat Graph"
updatedAt: 2025-09-25T00:38:34.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Threat Graph](../README.md) › [Threat Graphs](../threat-graphs.md) › Search graphs

---

# search-graphs

Endpoint used to search graphs.

There are a set of multiple modifiers that you can use to refine your search results. You can combine all of them together and use them in conjunction with AND, OR and NOT operators.

Date and numeric fields support the suffix plus or minus to match values greater or less than the passed value. If not sign has been added to the modifier, you will get exact matches. You can use more than once the same modifier in the same query to define ranges: `creation_date:2018-11-1+` `creation_date:2018-11-12-` will match graphs created between 2018-11-1 and 2018-11-22.

**Graph-related modifiers**

| Modifier              | Description                                        | Example                                                              |
| :-------------------- | :------------------------------------------------- | :------------------------------------------------------------------- |
| id:                   | Filters by graph identifier.                       | id:g675a2fd4c8834e288afd71bbbe88f78884e7d21a8c9348b5ab45cc9281cffc3c |
| name:                 | Filters by graph name.                             | name:Wannacry                                                        |
| owner:                | Filters by graphs owned by user.                   | owner:richard\_hendricks                                             |
| group:                | Filters by graphs owned by group.                  | group:piedpiper                                                      |
| visible\_to\_user:    | Filters by graphs visible to user.                 | visible\_to\_user:richard\_hendricks                                 |
| visible\_to\_group:   | Filters by graphs visible to group.                | visible\_to\_group:piedpiper                                         |
| private:              | Filters by private graphs.                         | private:true, private:false                                          |
| creation\_date:       | Filters by the graph creation date.                | creation\_date:2018-11-1                                             |
| last\_modified\_date: | Filters by the last date the graph was modified.   | last\_modified\_date:2018-11-12                                      |
| total\_nodes:         | Filters by graphs containing some amount of nodes. | total\_nodes:100                                                     |
| comments\_count:      | Filter by the number of comments of the graph.     | comments\_count:10+                                                  |
| views\_count:         | Filter by the number of graph views.               | views\_count:1000+                                                   |

**Node-related modifiers**

| Modifier     | Description                                              | Example                                                               |
| :----------- | :------------------------------------------------------- | :-------------------------------------------------------------------- |
| label:       | Filters by graphs containing nodes with a specific label | label:Kill switch                                                     |
| file:        | Filters by graphs containing the file.                   | file:131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267 |
| domain:      | Filters by graphs containing the domain.                 | domain:piedpiper.com                                                  |
| ip\_address: | Filters by graphs containing the ip address.             | ip\_address:1.1.1.1                                                   |
| url:         | Filters by graphs containing the url.                    | url:<https://piedpiper.com/the-box/>                                  |
| actor:       | Filters by graphs containing the actor.                  | actor:funny bear                                                      |
| victim:      | Filters by graphs containing the victim.                 | victim:richard\_hendricks                                             |
| email:       | Filters by graphs containing the email.                  | email:<richard@piedpiper.com>                                         |
| department:  | Filters by graphs containing the department.             | department:engineers                                                  |

In addition to these modifiers, you can do a free search query. The search engine will return graphs that match the query with the content of any field in the graph.

```curl All graphs
curl --request POST \
  --url https://www.virustotal.com/api/v3/graphs \
  --header 'x-apikey: <your API key>'
```
```curl FIlter by user
curl --request POST \
  --url https://www.virustotal.com/api/v3/graphs?filter=owner:bbunny \
  --header 'x-apikey: <your API key>'
```
```curl Attributes selection
curl --request POST \
  --url https://www.virustotal.com/api/v3/graphs?filter=owner:bbunny&attributes=private,graph_data \
  --header 'x-apikey: <your API key>'
```
```curl Filter by domain
curl --request POST \
  --url https://www.virustotal.com/api/v3/graphs?filter=domain:hooli.com \
  --header 'x-apikey: <your API key>'
```

Supported `order` fields are: `name`, `owner`, `creation_date`, `last_modified_date`, `views_count` and `comments_count`.

# openapi-definition

```json
{
  "components": {
    "securitySchemes": {
      "sec0": {
        "in": "header",
        "name": "x-apikey",
        "type": "apiKey"
      }
    }
  },
  "info": {
    "title": "Threat Graph",
    "version": "3.0"
  },
  "openapi": "3.1.0",
  "tags": [
    {
      "name": "Threat Graphs"
    }
  ],
  "paths": {
    "/graphs": {
      "get": {
        "tags": [
          "Threat Graphs"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "graphs",
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
            "description": "Return the graphs matching the given criteria only",
            "in": "query",
            "name": "filter",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Maximum number graphs to retrieve",
            "in": "query",
            "name": "limit",
            "schema": {
              "format": "int32",
              "type": "integer",
              "maximum": 40,
              "minimum": 0
            }
          },
          {
            "description": "Continuation cursor",
            "in": "query",
            "name": "cursor",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Sort order",
            "in": "query",
            "name": "order",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Specific fields to retrieve",
            "in": "query",
            "name": "attributes",
            "schema": {
              "type": "string"
            }
          }
        ],
        "security": [],
        "summary": "Search graphs"
      }
    }
  },
  "security": [
    {
      "sec0": []
    }
  ],
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

← [Threat Graphs](../threat-graphs.md) · [up](../README.md) · [Create a graph](create-graphs.md) →

*Archived from <https://gtidocs.virustotal.com/reference/graphs>.*
