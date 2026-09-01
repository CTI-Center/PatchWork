---
title: "Search Entities"
source: https://gtidocs.virustotal.com/reference/get_search-entities-search-string
slug: get_search-entities-search-string
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:19.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Entities](../entities.md) › Search Entities

---

# search-entities

Search Endpoint for all entity data. If no operator is used, "name" field is searched

Valid Search Keywords ('**search_string' parameter)**:

- collection:intrigue_123k221
    
- type:string
    
    - ApiEndpoint, AppEndpoint, AutonomousSystem, AwsEC2Instance, AwsRdsDbInstance, AwsS3Bucket, AzureStorageAccount, AzureVirtualMachine, DnsRecord, Domain, EmailAddress, GcpApiGateway, GcpAppEngineApplication, GcpCloudFunction, GcpCloudSQLInstance, GcpComputeEngineInstance, GcpStorageBucket, GithubAccount, GithubRepository, IpAddress, Nameserver, NetBlock, NetworkService, SslCertificate, UniqueKeyword, UniqueToken, Uri
        
- name:string
    
- hidden:false | true
    
- tag:tagname
    
- country:us (alpha-2 country coded)
    
- uid:12345
    
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
        
- scoped:true | false
    
- http_code:404
    
- http_auth:true | false
    
- http_auth_basic:true | false
    
- http_auth_ntlm:true | false
    
- http_title:string
    
- http_forms:true | false
    
- http_cookie
    
- technology:jquery
    
- cloud:true | false
    
- cloud_provider
    
- network
    
- port_tcp
    
- port_udp
    
- port_count_lte:1
    
- port_count_gte:1
    
- issue_count_lte:1
    
- issue_count_gte:1
    
- vuln:cve
    
- vuln_count_gte:1
    
- vuln_count_lte:1
    
- critical_or_high:true | false
    
- resolves_to:string

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
      "name": "Entities"
    }
  ],
  "paths": {
    "/search/entities/{search_string}": {
      "get": {
        "tags": [
          "Entities"
        ],
        "summary": "Search Entities",
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
            "example": "100"
          },
          {
            "name": "page_token",
            "in": "query",
            "schema": {
              "type": "string"
            },
            "description": "Optional: Used to get the next page of results. Use the value from next_page_token in results. The next_page_token will change with each new page. When using page_token do not use the \"page\" key. ",
            "example": "eyJhbGciOiJBMjU2R0NNS1ciLCJlbmMiOiJBMjU2R0NNIiwiaXYiOiJaaXRVdGVIOV9ORUNlY2RnIiwidGFnIjoiN0JWUnk0QjRXalNTN1dCWmMwY2FWdyJ9.dpg0fRevYn8P6TocpJ9DUSxVFurrYXqaXuqGI8CaK2o.NoNoFUbHyAEh6ckk.3hOnO4BKO57sBoTvCCxrK_QJLxFZKRID98b9MklxR1FpZW2dZpNEQHSilyXaWAwC6-qXX5hL6Xr0SNQGyWFNHQp2GFmAzAaBalRpohwB1ADZ6ALj93juPChmaQLjsfTQOEFOnVdFhxx_wo_cfXWqGUn_SIxcm309dHT9-SvbNF7XtDaZ6U4sg3F7NORR8lKTyrCQvf2l4itOw0HAKxePav1ys_tIiTJx4ct-utmIYg6eB8vjVpDflhblQe7_JqlDTbI8JWX4GqL2tqmDvCHcpxOiSPPENzYV2D-C1xoTRCctfaZRh9BERs_cFA.OmkBu4OHPgXcnATiO5FcCw"
          },
          {
            "name": "search_string",
            "in": "path",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Example with multiple keywords. If no string is entered all entities for the project will be returned",
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
                  "example": "Fri, 17 Feb 2023 22:00:24 GMT"
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
                  "example": "4760"
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
                            "must": [
                              {
                                "bool": {
                                  "should": [
                                    {
                                      "match": {
                                        "summary.scoped": {
                                          "query": "true",
                                          "operator": "AND"
                                        }
                                      }
                                    }
                                  ],
                                  "minimum_should_match": 1
                                }
                              },
                              {
                                "range": {
                                  "first_seen": {
                                    "gte": "2022-01-01T00:00:00Z"
                                  }
                                }
                              }
                            ],
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
                          "entity_type_bucket": {
                            "terms": {
                              "field": "type.raw",
                              "size": 25
                            }
                          },
                          "scoped_bucket": {
                            "terms": {
                              "field": "scoped",
                              "size": 3
                            }
                          },
                          "issues_severity_1_bucket": {
                            "sum": {
                              "field": "summary.issues.current_by_severity.1"
                            }
                          },
                          "issues_severity_2_bucket": {
                            "sum": {
                              "field": "summary.issues.current_by_severity.2"
                            }
                          },
                          "issues_severity_3_bucket": {
                            "sum": {
                              "field": "summary.issues.current_by_severity.3"
                            }
                          },
                          "issues_severity_4_bucket": {
                            "sum": {
                              "field": "summary.issues.current_by_severity.4"
                            }
                          },
                          "issues_severity_5_bucket": {
                            "sum": {
                              "field": "summary.issues.current_by_severity.5"
                            }
                          },
                          "country_code_bucket": {
                            "terms": {
                              "field": "summary.geolocation.country_code.raw",
                              "size": 10
                            }
                          },
                          "technolgy_bucket": {
                            "terms": {
                              "field": "summary.technology.cpes.cpe.raw",
                              "size": 10
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
                      "search_type": "entities",
                      "sort_direction": "asc",
                      "sort_field": "last_seen",
                      "group_by_field": null
                    },
                    "total_hits": 4323,
                    "timed_out": false,
                    "more": true,
                    "page": 0,
                    "page_size": 1,
                    "total_pages": 4323,
                    "hits": [
                      {
                        "id": "1f7b1b98a62ee28bf509871a1f573287fd51b70436b2fa6a9f9b0140e9eaddb6",
                        "dynamic_id": "Intrigue::Entity::IpAddress#192.168.1.109",
                        "alias_group": null,
                        "aliases": null,
                        "hidden": false,
                        "name": "192.168.1.109",
                        "type": "Intrigue::Entity::IpAddress",
                        "seed": null,
                        "first_seen": "2022-10-05T19:27:33Z",
                        "last_seen": "2022-10-05T19:27:33Z",
                        "collection": "collectionname_a6mz56o",
                        "collection_type": "user_collection",
                        "collection_naics": null,
                        "collection_uuid": "f11e71db-d12d-4733-a19e-b8742ed7eb70",
                        "organization_uuid": "075811c8-fe6f-412f-a071-34a7342c16a3",
                        "tags": [],
                        "issues": [],
                        "exfil_lookup_identifier": "61539b426980b7959a65f017657025ab",
                        "summary": {
                          "scoped": true,
                          "issues": {
                            "current_by_severity": {},
                            "current_with_cve": 0,
                            "all_time_by_severity": {},
                            "current_count": 0,
                            "all_time_count": 0,
                            "critical_or_high": false
                          },
                          "task_results": [
                            "search_shodan",
                            "enrich/uri"
                          ],
                          "geolocation": {
                            "city": "Macenta",
                            "country_code": "GN",
                            "country_name": null,
                            "latitude": 8.54829,
                            "longitude": -9.48282,
                            "asn": null
                          },
                          "ports": {
                            "count": 1,
                            "tcp": [
                              80
                            ],
                            "udp": []
                          },
                          "resolutions": [],
                          "network": {
                            "name": "Namecheap, Inc.",
                            "asn": 22612,
                            "route": null,
                            "type": null
                          },
                          "technology": {
                            "cloud": false,
                            "cloud_providers": [],
                            "cpes": [],
                            "technologies": [],
                            "technology_labels": []
                          }
                        }
                      }
                    ],
                    "aggregations": {
                      "scoped_bucket": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": []
                      },
                      "issues_severity_1_bucket": {
                        "value": 1114
                      },
                      "collection_bucket": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                          {
                            "key": "collectionname_a6mz56o",
                            "doc_count": 4323
                          }
                        ]
                      },
                      "technolgy_bucket": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 2971,
                        "buckets": [
                          {
                            "key": "cpe:2.3:s:cloudflare:cloudflare::",
                            "doc_count": 615
                          },
                          {
                            "key": "cpe:2.3:a:php:php::",
                            "doc_count": 185
                          },
                          {
                            "key": "cpe:2.3:a:jquery:jquery:1.10.2:",
                            "doc_count": 145
                          },
                          {
                            "key": "cpe:2.3:a:apache:http_server::",
                            "doc_count": 140
                          },
                          {
                            "key": "cpe:2.3:a:php:php:7.1.33:",
                            "doc_count": 136
                          },
                          {
                            "key": "cpe:2.3:a:apache:http_server:2.4.38:",
                            "doc_count": 129
                          },
                          {
                            "key": "cpe:2.3:s:the_open_graph_protocol:the_open_graph_protocol::",
                            "doc_count": 121
                          },
                          {
                            "key": "cpe:2.3:a:openbsd:openssh::",
                            "doc_count": 108
                          },
                          {
                            "key": "cpe:2.3:a:ssh:ssh:2.0:",
                            "doc_count": 108
                          },
                          {
                            "key": "cpe:2.3:a:google:tag_manager::",
                            "doc_count": 106
                          }
                        ]
                      },
                      "entity_type_bucket": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                          {
                            "key": "Intrigue::Entity::NetworkService",
                            "doc_count": 2275
                          },
                          {
                            "key": "Intrigue::Entity::Uri",
                            "doc_count": 743
                          },
                          {
                            "key": "Intrigue::Entity::SslCertificate",
                            "doc_count": 582
                          },
                          {
                            "key": "Intrigue::Entity::IpAddress",
                            "doc_count": 531
                          },
                          {
                            "key": "Intrigue::Entity::DnsRecord",
                            "doc_count": 118
                          },
                          {
                            "key": "Intrigue::Entity::UniqueToken",
                            "doc_count": 41
                          },
                          {
                            "key": "Intrigue::Entity::ApiEndpoint",
                            "doc_count": 22
                          },
                          {
                            "key": "Intrigue::Entity::AwsS3Bucket",
                            "doc_count": 7
                          },
                          {
                            "key": "Intrigue::Entity::PreCertificate",
                            "doc_count": 4
                          }
                        ]
                      },
                      "country_code_bucket": {
                        "doc_count_error_upper_bound": 0,
                        "sum_other_doc_count": 0,
                        "buckets": [
                          {
                            "key": "US",
                            "doc_count": 3141
                          },
                          {
                            "key": "CA",
                            "doc_count": 329
                          },
                          {
                            "key": "BR",
                            "doc_count": 9
                          },
                          {
                            "key": "DE",
                            "doc_count": 8
                          },
                          {
                            "key": "HK",
                            "doc_count": 8
                          },
                          {
                            "key": "GN",
                            "doc_count": 2
                          },
                          {
                            "key": "VG",
                            "doc_count": 2
                          }
                        ]
                      },
                      "issues_severity_5_bucket": {
                        "value": 371
                      },
                      "issues_severity_4_bucket": {
                        "value": 70
                      },
                      "issues_severity_3_bucket": {
                        "value": 239
                      },
                      "issues_severity_2_bucket": {
                        "value": 59
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

← [Entities](../entities.md) · [up](../README.md) · [Get Detail](get_entities-entity-uid.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_search-entities-search-string>.*
