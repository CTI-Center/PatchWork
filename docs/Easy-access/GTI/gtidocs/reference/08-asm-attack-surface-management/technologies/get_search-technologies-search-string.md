---
title: "Search Technologies"
source: https://gtidocs.virustotal.com/reference/get_search-technologies-search-string
slug: get_search-technologies-search-string
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T01:36:42.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Technologies](../technologies.md) › Search Technologies

---

# search-technologies

Search Endpoint for all technology data. If no operator is used, "name" field is searched

Valid Search Keywords ('**search_string' parameter)**:

- collection:intrigue_123k221
    
- name:google_analytics
    
- label:wordpress_plugin
    
- last_seen_after:string
    
    - last_scan_count_1 (1-10)
        
    - last_refresh
        
    - configured_scan_count
        
    - YYYY-MM-DD
        
- last_seen_before:string
    
    - last_scan_count_1 (1-10)
        
    - last_refresh
        
    - configured_scan_count
        
    - YYYY-MM-DD
        
- first_seen_after:string
    
    - last_scan_count_1 (1-10)
        
    - last_refresh
        
    - configured_scan_count
        
    - YYYY-MM-DD
        
- cpe_type:application or service, hardware, os
    
- product:text
    
- vendor:google

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
      "name": "Technologies"
    }
  ],
  "paths": {
    "/search/technologies/{search_string}": {
      "get": {
        "tags": [
          "Technologies"
        ],
        "summary": "Search Technologies",
        "description": "",
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
            "name": "PROJECT-ID",
            "in": "header",
            "schema": {
              "type": "string"
            },
            "description": "Required: id from /api/v3/asm/projects",
            "example": "{{project-id}}"
          },
          {
            "name": "search_string",
            "in": "path",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "sample with multiple filters",
            "example": "cpe:\"cpe:2.3:s:cloudflare:cloudflare::\""
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "headers": {
              "Content-Type": {
                "schema": {
                  "type": "string",
                  "example": "application/json"
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
                  "message": "Search completed!",
                  "result": {
                    "search": {
                      "search_body": {
                        "query": {
                          "bool": {
                            "filter": [
                              {
                                "bool": {
                                  "should": [
                                    {
                                      "match": {
                                        "collection": "collectinname_mw3tdwq"
                                      }
                                    }
                                  ]
                                }
                              }
                            ]
                          }
                        },
                        "aggs": {
                          "collection_bucket": {
                            "terms": {
                              "field": "collection",
                              "size": 10
                            }
                          },
                          "vendor_bucket": {
                            "terms": {
                              "field": "vendor",
                              "size": 10
                            }
                          },
                          "product_bucket": {
                            "terms": {
                              "field": "product",
                              "size": 20
                            }
                          },
                          "label_bucket": {
                            "terms": {
                              "field": "labels",
                              "size": 20
                            }
                          }
                        },
                        "sort": [
                          {
                            "last_seen": "asc"
                          },
                          "_doc"
                        ]
                      },
                      "search_string": "",
                      "search_type": "technologies",
                      "sort_direction": "asc",
                      "sort_field": "last_seen",
                      "group_by_field": null
                    },
                    "total_hits": 2,
                    "timed_out": false,
                    "more": false,
                    "page": 0,
                    "page_size": 50,
                    "total_pages": 0,
                    "hits": [
                      {
                        "id": "1e3f72d7464444970f241dd3ee056456818d2ed51da1a2041c20da4a840c6314",
                        "name": "Cloudflare",
                        "dynamic_id": "cpe:2.3:s:cloudflare:cloudflare::",
                        "collection": "collectionname_mw3tdwq",
                        "collection_type": "UserCollection",
                        "collection_naics": [],
                        "collection_uuid": null,
                        "organization_uuid": null,
                        "cpe": "cpe:2.3:s:cloudflare:cloudflare::",
                        "cpe_type": "service",
                        "first_seen": "2022-08-18T21:07:16Z",
                        "last_seen": "2022-09-09T06:02:08Z",
                        "labels": [
                          "cdn",
                          "paas",
                          "waf"
                        ],
                        "vendor": "Cloudflare",
                        "product": "Cloudflare",
                        "version": "",
                        "update": "",
                        "unique_instance_count": 8,
                        "instances": [
                          "36ef1c6be38e83da694a16aae40cf8bb9b437feef16062cd198ffd1fd8016757",
                          "2efe370ffbfdbd1a6a8b2f829261cb915f3de9cc58e0e62bf30f91163afe4aa6",
                          "e0adf7542a95bac4e27c3f262b8fa65c690ef21ec8fd29319aabf64cbd6635eb",
                          "88dc130e69d5ed2d220117f00bd19114266b518cf2a4c0a9a8abb774df724897",
                          "178391e700e4d16549b6976f239ba077b72662db5e9d34259f8cc637539fd394",
                          "c13b89223e6f034fa0fe9d56ed5badc0527c9c74a6df10c0ff4611a964a2127a",
                          "a4cfa1fddf10ea18959c863c7864d343f8b9568248ad75504005980ca6253a01",
                          "27876b9959a1feef847cd3b05f8fd08086f60898179aa7b8b55b9fbf849a831f"
                        ],
                        "updated_at": "2022-09-09T06:02:16Z",
                        "collection_tags": []
                      },
                      {
                        "id": "0453aee6881543d07c1bb2ec0f4de1a0ff0fc23ef089c5bd425e9c29db2dbfbf",
                        "name": "Attacksurface",
                        "dynamic_id": "cpe:2.3:s:attacksurface:attacksurface::",
                        "collection": "collectionnname_mw3tdwq",
                        "collection_type": "UserCollection",
                        "collection_naics": [],
                        "collection_uuid": null,
                        "organization_uuid": null,
                        "cpe": "cpe:2.3:s:attacksurface:attacksurface::",
                        "cpe_type": "service",
                        "first_seen": "2022-08-19T22:57:21Z",
                        "last_seen": "2022-09-09T06:02:09Z",
                        "labels": [],
                        "vendor": "Attacksurface",
                        "product": "Attacksurface",
                        "version": "",
                        "update": "",
                        "unique_instance_count": 2,
                        "instances": [
                          "88dc130e69d5ed2d220117f00bd19114266b518cf2a4c0a9a8abb774df724897",
                          "a4cfa1fddf10ea18959c863c7864d343f8b9568248ad75504005980ca6253a01"
                        ],
                        "updated_at": "2022-09-09T06:02:16Z",
                        "collection_tags": []
                      }
                    ],
                    "aggregations": {
                      "collection_bucket": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                          {
                            "key": "attacksurface_mw3tdwq",
                            "doc_count": 2
                          }
                        ]
                      },
                      "label_bucket": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                          {
                            "key": "cdn",
                            "doc_count": 1
                          },
                          {
                            "key": "paas",
                            "doc_count": 1
                          },
                          {
                            "key": "waf",
                            "doc_count": 1
                          }
                        ]
                      },
                      "product_bucket": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                          {
                            "key": "Attacksurface",
                            "doc_count": 1
                          },
                          {
                            "key": "Cloudflare",
                            "doc_count": 1
                          }
                        ]
                      },
                      "vendor_bucket": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                          {
                            "key": "Attacksurface",
                            "doc_count": 1
                          },
                          {
                            "key": "Cloudflare",
                            "doc_count": 1
                          }
                        ]
                      }
                    },
                    "next_page_token": "eyJhbGciOiJBMjU2R0NNS1ciLCJlbmMiOiJBMjU2R0NNIiwiaXYiOiJDMmhPQlRweE5jT2psUTNlIiwidGFnIjoiTGpqaFhvQ1F0RWZjXzdJTkt4ZG5XZyJ9.MmWAi13CT942tNOv07i7l40wt9wm4XKt9PZ10x34cu0.0GDiGDyp6Snff9mk.MVB3X0pjYjkN8-9-glzlVQl5VjsAMkxtkFN_A8ZELCUGnpSg-pUEfMntNZ4iglMLk7amm4Bh7saZ2QGzNRLCmGcwIxlmSqTWqB1UrSRRkdMpHec5O1EdAyh41SK4B2Vh8DnTnBwLQFYdExi82oNobIX5tWdJmVKdsAFFm7F_0gW1J2TR49HreXyXxv5UtCRvFf3FlqvbPzWEO6cyQ8eMUuNEGvLi_F5YncAfxwsjuNY-FHk-TUl0aUOEj3mD4ZnaokFI4HK6SB95SqJ7WCFSf3iSulVSMihnuJ7e0V_YCS9Lrk8n6DSOHdPelQ.-Z1v3MQn335tNg7FcflqPA"
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

← [Technologies](../technologies.md) · [up](../README.md) · [Notes](../notes.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_search-technologies-search-string>.*
