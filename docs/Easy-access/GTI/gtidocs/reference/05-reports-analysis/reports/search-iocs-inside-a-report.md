---
title: "Search IoCs inside a report"
source: https://gtidocs.virustotal.com/reference/search-iocs-inside-a-report
slug: search-iocs-inside-a-report
section: reference
group: "Reports & Analysis"
updatedAt: 2025-09-25T00:36:44.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Reports & Analysis](../README.md) › [Reports](../reports.md) › Search IoCs inside a report

---

# search-iocs-inside-a-report

> 🚧 Special privileges required
>
> Reports & Analysis are only available to users with the Google Threat Intelligence (Google TI) Enterprise or Enterprise Plus licenses.

Allows to search IoCs inside a report using advanced intelligence queries.

The expected input is the same as [/intelligence/search](../../03-ioc-investigation/search-metadata/intelligence-search.md). By default it searches files, in order to search other entities use `entity:domain/ip/url`.

## examples

Search for IoCs related to a report that meet certain conditions.

```python
import requests
import urllib

object_id = "report--24-10074013"
query = "p:4+"
attributes = "name"
limit = "2"
url = f"https://www.virustotal.com/api/v3/collections/{object_id}/search?query={query}&limit={limit}&attributes={attributes}"
headers = {"accept": "application/json","x-apikey": <api-key>}
response = requests.get(url, headers=headers)
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
    "/collections/{id}/search": {
      "get": {
        "tags": [
          "Reports"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "search-iocs-inside-a-report",
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
          },
          {
            "description": "Intelligence query",
            "in": "query",
            "name": "query",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Maximum number of IoCs to retrieve (max 40)",
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
            "description": "Continuation cursor",
            "in": "query",
            "name": "cursor",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Sorting order",
            "in": "query",
            "name": "order",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Comma-separated attributes to return from the resulting IoCs",
            "in": "query",
            "name": "attributes",
            "schema": {
              "type": "string"
            }
          },
          {
            "description": "Comma-separated name of relationships descriptors to return from the IoCs",
            "in": "query",
            "name": "relationships",
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
                    "value": "{\n\"meta\": {\n  \"cursor\": <string>,\n  \"total_hits\": <int>,\n  \"allowed_orders\": [<string>, ...]\n},\n\"data\": [\n  <IOC>,\n  <IOC>,\n  ...\n],\n\"links\": {\n  \"self\": <string>,\n  \"next\": <string>\n}"
                  }
                }
              },
              "text/plain": {
                "examples": {
                  "Example": {
                    "value": "{\n\t\"data\":\n\t[\n\t\t{\n\t\t\t\"id\": \"280fbf353fdffefc5a0af40c706377142fff718c7b87bc8b0daab10849f388d0\",\n\t\t\t\"type\": \"file\",\n\t\t\t\"links\":\n\t\t\t{\n\t\t\t\t\"self\": \"https://www.virustotal.com/api/v3/files/280fbf353fdffefc5a0af40c706377142fff718c7b87bc8b0daab10849f388d0\"\n\t\t\t},\n\t\t\t\"attributes\":\n\t\t\t{\n\t\t\t\t\"names\":\n\t\t\t\t[\n\t\t\t\t\t\"AWS IAM Configuration.rdp\",\n\t\t\t\t\t\"280fbf353fdffefc5a0af40c706377142fff718c7b87bc8b0daab10849f388d0.rdp\"\n\t\t\t\t]\n\t\t\t}\n\t\t},\n\t\t{\n\t\t\t\"id\": \"280fbf353fdffefc5a0af40c706377142fff718c7b87bc8b0daab10849f388d0\",\n\t\t\t\"type\": \"file\",\n\t\t\t\"links\":\n\t\t\t{\n\t\t\t\t\"self\": \"https://www.virustotal.com/api/v3/files/280fbf353fdffefc5a0af40c706377142fff718c7b87bc8b0daab10849f388d0\"\n\t\t\t},\n\t\t\t\"attributes\":\n\t\t\t{\n\t\t\t\t\"names\":\n\t\t\t\t[\n\t\t\t\t\t\"AWS IAM Configuration.rdp\",\n\t\t\t\t\t\"280fbf353fdffefc5a0af40c706377142fff718c7b87bc8b0daab10849f388d0.rdp\"\n\t\t\t\t]\n\t\t\t}\n\t\t}\n\t],\n\t\"meta\":\n\t{\n\t\t\"cursor\": \"eJwVy9FOgzAUgOFXamEYvZxh4GZOsazlQO86mCJtyUExMOLDOy__5P9-Te1fO08zjmQxy0hF9Nwy_yNH_wmcFnQdXrWfLpE_l-6kz-hji3Arau8kc1EVUwaMP8iaChuAq0DV3U9nVYqSE2EgAZrdMMz2UtE3Bi6g8lqG3lqfxVjT0LFkUkoUV6cXhfz_m5q4fysZ2xBpBO5npUpj3ekLqy63mmupyqLM11nVNIqMDhJ9g-n-6f1ljSBeH0G1GwztCupjFf89mN7gkYltvwjVD0W6Txplgkglb7bjrhlgZ9I2aoJezOA4KL0UaX83MjF4WERehSJ1DAZY7oZB3iSN_ANc-20d\",\n\t\t\"total_hits\": 7,\n\t\t\"allowed_orders\":\n\t\t[\n\t\t\t\"first_submission_date\",\n\t\t\t\"last_submission_date\",\n\t\t\t\"positives\",\n\t\t\t\"times_submitted\",\n\t\t\t\"size\",\n\t\t\t\"unique_sources\",\n\t\t\t\"gti_score\"\n\t\t]\n\t},\n\t\"links\":\n\t{\n\t\t\"self\": \"https://www.virustotal.com/api/v3/collections/report--24-10067783/search?query=name:IAM&attributes=names&limit=2\",\n\t\t\"next\": \"https://www.virustotal.com/api/v3/collections/report--24-10067783/search?query=name%3AIAM&attributes=names&limit=2&cursor=eJwVy9FOgzAUgOFXamEYvZxh4GZOsazlQO86mCJtyUExMOLDOy__5P9-Te1fO08zjmQxy0hF9Nwy_yNH_wmcFnQdXrWfLpE_l-6kz-hji3Arau8kc1EVUwaMP8iaChuAq0DV3U9nVYqSE2EgAZrdMMz2UtE3Bi6g8lqG3lqfxVjT0LFkUkoUV6cXhfz_m5q4fysZ2xBpBO5npUpj3ekLqy63mmupyqLM11nVNIqMDhJ9g-n-6f1ljSBeH0G1GwztCupjFf89mN7gkYltvwjVD0W6Txplgkglb7bjrhlgZ9I2aoJezOA4KL0UaX83MjF4WERehSJ1DAZY7oZB3iSN_ANc-20d\"\n\t}\n}"
                  }
                },
                "schema": {
                  "properties": {
                    "data": {
                      "items": {
                        "properties": {
                          "attributes": {
                            "properties": {
                              "names": {
                                "items": {
                                  "type": "string"
                                },
                                "type": "array"
                              }
                            },
                            "type": "object"
                          },
                          "id": {
                            "type": "string"
                          },
                          "links": {
                            "properties": {
                              "self": {
                                "type": "string"
                              }
                            },
                            "type": "object"
                          },
                          "type": {
                            "type": "string"
                          }
                        },
                        "type": "object"
                      },
                      "type": "array"
                    },
                    "links": {
                      "properties": {
                        "next": {
                          "type": "string"
                        },
                        "self": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    },
                    "meta": {
                      "properties": {
                        "allowed_orders": {
                          "items": {
                            "type": "string"
                          },
                          "type": "array"
                        },
                        "cursor": {
                          "type": "string"
                        },
                        "total_hits": {
                          "default": 0,
                          "type": "integer"
                        }
                      },
                      "type": "object"
                    }
                  },
                  "type": "object"
                }
              }
            },
            "description": "200"
          }
        },
        "summary": "Search IoCs inside a report"
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

← [Get MITRE tactics and techniques associated with a report](get-report-mitre-tree.md) · [up](../README.md) · [Export IOCs from a report](export-report-iocs.md) →

*Archived from <https://gtidocs.virustotal.com/reference/search-iocs-inside-a-report>.*
