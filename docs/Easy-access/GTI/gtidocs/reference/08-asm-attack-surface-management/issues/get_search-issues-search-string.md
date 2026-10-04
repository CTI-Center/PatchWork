---
title: "Search Issues"
source: https://gtidocs.virustotal.com/reference/get_search-issues-search-string
slug: get_search-issues-search-string
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:21.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Issues](../issues.md) › Search Issues

---

# search-issues

Search Endpoint for all issue data. If no operator is used, "name" field is searched

Valid Search Keywords ('**search_string' parameter)**:

- collection:name_123k221
    
- name:string
    
- uid:12345
    
- tag:tag_name
    
- last_seen_after:string
    
    - last_scan_count_1 (1-10)
        
    - last_refresh
        
    - YYYY-MM-DD
        
    - configured_scan_count
        
- last_seen_before:string
    
    - last_scan_count_1 (1-10)
        
    - last_refresh
        
    - YYYY-MM-DD
        
    - configured_scan_count
        
- first_seen_after:string
    
    - last_scan_count_1 (1-10)
        
    - last_refresh
        
    - YYYY-MM-DD
        
    - configured_scan_count
        
- entity_uid:12345
    
- entity_type:string
    
    - ApiEndpoint, AppEndpoint, AutonomousSystem, AwsEC2Instance, AwsRdsDbInstance, AwsS3Bucket, AzureStorageAccount, AzureVirtualMachine, DnsRecord, Domain, EmailAddress, GcpApiGateway, GcpAppEngineApplication, GcpCloudFunction, GcpCloudSQLInstance, GcpComputeEngineInstance, GcpStorageBucket, GithubAccount, GithubRepository, IpAddress, Nameserver, NetBlock, NetworkService, SslCertificate, UniqueKeyword, UniqueToken, Uri
        
- entity_name:string
    
- scoped:true | false
    
- severity:integer 1-5
    
- severity_lte:integer 1-5
    
- severity_gte:integer 1-5
    
- status_new:open or closed
    
- status_detailed:string
    
    - open_triaged, open_in_progress, closed_mitigated, closed_resolved, closed_duplicate, closed_out_of_scope, closed_benign, closed_risk_accepted, closed_false_positive, closed_no_reproduce, closed_tracked_externally

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
      "name": "Issues"
    }
  ],
  "paths": {
    "/search/issues/{search_string}": {
      "get": {
        "tags": [
          "Issues"
        ],
        "summary": "Search Issues",
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
            "description": "ID from /api/v3/asm/projects",
            "example": "{{project-id}}",
            "required": true
          },
          {
            "name": "page_size",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 50,
              "maximum": 100,
              "minimum": 0
            },
            "description": "Optional: Used to control how many results returned per page <default 50, max 1000> ",
            "example": "1"
          },
          {
            "name": "page_token",
            "in": "query",
            "schema": {
              "type": "string"
            },
            "description": "Optional: Used to get the next page of results. Use the value from next_page_token in results. The next_page_token will change with each new page. When using page_token do not use the \"page\" key. ",
            "example": "eyJhbGciOiJBMjU2R0NNS1ciLCJlbmMiOiJBMjU2R0NNIiwiaXYiOiJaaXRVdGVIOV9ORUNlY2RnIiwidGFnIjoiN0JWUnk0QjRXalNTN1dCWmMwY2FWdyJ9.dpg0fRevYn8P6TocpJ9DUSxVFurrYXqaXuqGI8CaK2o.NoNoFUbHyAEh6ckk.3hOnO4BKO57sBoTvCCxrK_QJLxFZKRID98b9MklxR1FpZW2dZpNEQHSilyXaWAwC6-qXX5hL6Xr0SNQGyWFNHQp2GFmAzAaBalRpohwB1ADZ6ALj93juPChmaQLjsfTQOEFOnVdFhxx_wo_cfXWqGUn_SIxcm309dHT9-SvbNF7XtDaZ6U4sg3F7NORR8lKTyrCQvf2l4itOw0HAKxePav1ys_tIiTJx4ct-utmIYg6eB8vjVpDflhblQe7_JqlDTbI8JWX4GqL2tqmDvCHcpxOiSPPENzYV2D-C1xoTRCctfaZRh9BERs_cFA.OmkBu4OHPgXcnATiO5FcCw\n"
          },
          {
            "name": "search_string",
            "in": "path",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Example with multiple keywords.",
            "example": "collection:collectionname_a6mz56o first_seen_after:2022-01-01 last_seen_before:last_refresh"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "headers": {
              "Server": {
                "schema": {
                  "type": "string",
                  "example": "Cowboy"
                }
              },
              "Date": {
                "schema": {
                  "type": "string",
                  "example": "Fri, 17 Feb 2023 22:17:48 GMT"
                }
              },
              "Connection": {
                "schema": {
                  "type": "string",
                  "example": "keep-alive"
                }
              },
              "Content-Type": {
                "schema": {
                  "type": "string",
                  "example": "application/json"
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
              "Content-Length": {
                "schema": {
                  "type": "integer",
                  "example": "3908"
                }
              },
              "Via": {
                "schema": {
                  "type": "string",
                  "example": "1.1 vegur"
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
                            "must": {
                              "range": {
                                "first_seen": {
                                  "gte": "2022-01-01T00:00:00Z"
                                }
                              }
                            },
                            "filter": {
                              "bool": {
                                "should": [
                                  {
                                    "bool": {
                                      "must": [
                                        {
                                          "match": {
                                            "collection": "collectionname_a6mz56o"
                                          }
                                        },
                                        {
                                          "range": {
                                            "last_seen": {
                                              "lte": "2023-01-31T18:59:39Z"
                                            }
                                          }
                                        }
                                      ]
                                    }
                                  }
                                ]
                              }
                            }
                          }
                        },
                        "aggs": {
                          "collection_bucket": {
                            "terms": {
                              "field": "collection",
                              "size": 10
                            }
                          },
                          "confidence": {
                            "terms": {
                              "field": "summary.confidence",
                              "size": 3
                            }
                          },
                          "issue_name_bucket": {
                            "terms": {
                              "field": "name.raw",
                              "size": 10
                            }
                          },
                          "severity_bucket": {
                            "terms": {
                              "field": "summary.severity",
                              "size": 5
                            }
                          },
                          "status_bucket": {
                            "terms": {
                              "field": "summary.status",
                              "size": 10
                            }
                          },
                          "status_new_bucket": {
                            "terms": {
                              "field": "summary.status_new.raw",
                              "size": 10
                            }
                          },
                          "status_detailed_bucket": {
                            "terms": {
                              "field": "summary.status_detailed.raw",
                              "size": 10
                            }
                          },
                          "ticket_list_bucket": {
                            "terms": {
                              "field": "summary.ticket_list.raw",
                              "size": 50
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
                      "search_string": "collection:collectionname_a6mz56o first_seen_after:2022-01-01 last_seen_before:last_refresh",
                      "search_type": "issues",
                      "sort_direction": "asc",
                      "sort_field": "last_seen",
                      "group_by_field": null
                    },
                    "total_hits": 3945,
                    "timed_out": false,
                    "more": true,
                    "page": 0,
                    "page_size": 1,
                    "total_pages": 3945,
                    "hits": [
                      {
                        "id": "2e0134b5b346a5d0a9d5ee0efe7dfb69dfcc5c1cf65a6df63568f85dc587a120",
                        "alias_group": "86373",
                        "dynamic_id": 21852016,
                        "name": "inferred_cve_2019_10081",
                        "first_seen": "2022-10-07T17:36:37.000Z",
                        "last_seen": "2022-10-07T17:36:37.000Z",
                        "collection": "collectionname_a6mz56o",
                        "collection_type": "user_collection",
                        "collection_uuid": "f12c71db-d34d-4733-a19e-b8742ed7eb70",
                        "organization_uuid": "075892c8-fe6f-454e-a071-34a7342c16a3",
                        "entity_type": "Intrigue::Entity::Uri",
                        "entity_name": "https://www.gridability.eu:443",
                        "entity_uid": "2a7cdfb23b2253a9ea4cc88962e0b7cd9b1622f7d44e56f675a8700b934d1f51",
                        "upstream": "intrigue",
                        "summary": {
                          "pretty_name": "Apache HTTPD 2.4.39 mod_http2 Resource Exhaustion Vulnerability (Inferred CVE-2019-10081)",
                          "severity": 2,
                          "scoped": true,
                          "confidence": "potential",
                          "status": "open_new",
                          "category": "unknown",
                          "identifiers": [
                            {
                              "name": "CVE-2019-10081",
                              "type": "CVE"
                            }
                          ],
                          "status_new": "open",
                          "status_new_detailed": "new",
                          "ticket_list": []
                        },
                        "tags": []
                      }
                    ],
                    "aggregations": {
                      "severity_bucket": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                          {
                            "key": "1",
                            "doc_count": 1697
                          },
                          {
                            "key": "3",
                            "doc_count": 798
                          },
                          {
                            "key": "2",
                            "doc_count": 726
                          },
                          {
                            "key": "5",
                            "doc_count": 569
                          },
                          {
                            "key": "4",
                            "doc_count": 155
                          }
                        ]
                      },
                      "ticket_list_bucket": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": []
                      },
                      "issue_name_bucket": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 2220,
                        "buckets": [
                          {
                            "key": "inferred_cve_2021_40438",
                            "doc_count": 265
                          },
                          {
                            "key": "inferred_cve_2020_11022",
                            "doc_count": 248
                          },
                          {
                            "key": "inferred_cve_2020_11023",
                            "doc_count": 248
                          },
                          {
                            "key": "inferred_cve_2019_11358",
                            "doc_count": 237
                          },
                          {
                            "key": "inferred_cve_2015_9251",
                            "doc_count": 206
                          },
                          {
                            "key": "deprecated_ssl_protocol_detected",
                            "doc_count": 178
                          },
                          {
                            "key": "weak_ssl_ciphers_enabled",
                            "doc_count": 99
                          },
                          {
                            "key": "wordpress_api_exposed",
                            "doc_count": 88
                          },
                          {
                            "key": "wordpress_admin_login_exposed",
                            "doc_count": 81
                          },
                          {
                            "key": "wordpress_user_info_leak",
                            "doc_count": 75
                          }
                        ]
                      },
                      "status_bucket": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                          {
                            "key": "open_new",
                            "doc_count": 3940
                          },
                          {
                            "key": "open_triaged",
                            "doc_count": 3
                          },
                          {
                            "key": "closed_benign",
                            "doc_count": 1
                          },
                          {
                            "key": "closed_tracked_externally",
                            "doc_count": 1
                          }
                        ]
                      },
                      "collection_bucket": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                          {
                            "key": "collectionname_a6mz56o",
                            "doc_count": 3945
                          }
                        ]
                      },
                      "confidence": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                          {
                            "key": "potential",
                            "doc_count": 2834
                          },
                          {
                            "key": "confirmed",
                            "doc_count": 1111
                          }
                        ]
                      },
                      "status_new_bucket": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                          {
                            "key": "open",
                            "doc_count": 3943
                          },
                          {
                            "key": "closed",
                            "doc_count": 2
                          }
                        ]
                      },
                      "status_detailed_bucket": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": []
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

← [Issues](../issues.md) · [up](../README.md) · [Get Detail](get_issues-id.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_search-issues-search-string>.*
