---
title: "Get Entity point in time"
source: https://gtidocs.virustotal.com/reference/get_time-series-point-in-time-entities-uid
slug: get_time-series-point-in-time-entities-uid
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:23.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Time Series](../time-series.md) › Get Entity point in time

---

# get-entity-point-in-time

Returns entity details of an entity for a specific point in time.

| **Key** | Format | **Notes** |
| --- | --- | --- |
| uid | string | required  <br>  <br>id or uuid from [https://asm-api.advantage.mandiant.com/search/entities/:search_string](https://asm-api.advantage.mandiant.com/search/entities/:search_string) |
| point_in_time | YYYY-MM-DD or ISO8601 timestamp string (UTC) | required  <br>  <br>Results from from [https://asm-api.advantage.mandiant.com/time_series/points_in_time/entities/:uid?start=](https://asm-api.advantage.mandiant.com/time_series/points_in_time/entities/:uid?start=)  <br>  <br>  <br>Example: 2023-06-26T09:50:20Z, or YYYY-MM-DD |

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
      "name": "Time Series"
    }
  ],
  "paths": {
    "/time_series/point_in_time/entities/{uid}": {
      "get": {
        "tags": [
          "Time Series"
        ],
        "summary": "Get Entity point in time",
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
            "name": "point_in_time",
            "in": "query",
            "schema": {
              "type": "string"
            },
            "description": "required, YYYY-MM-DD or ISO8601 timestamp string (UTC), Example: 2023-06-16T09:50:20Z \nFrom /api/v3/asm/time_series/points_in_time/entities/:uid?start=",
            "example": "2023-07-23"
          },
          {
            "name": "uid",
            "in": "path",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "id or uuid from /api/v3/asm/search/entities/:search_string",
            "example": "28abaa9fea296764a8da0f76832056773852f5f82ae553769fd3b462a46bc205"
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
                  "example": "Fri, 18 Aug 2023 20:12:29 GMT"
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
                  "example": "7167"
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
                  "message": "Success",
                  "result": {
                    "entity": {
                      "uid": "28abaa9fea296764a8da0f76832056773852f5f82ae553769fd3b462a46bc205",
                      "name": "https://attacksurface.app:8443",
                      "seed": false,
                      "tags": [],
                      "type": "Intrigue::Entity::Uri",
                      "uuid": "52a1e3fb-0f83-4186-bbb7-15218cc8cdaa",
                      "hidden": false,
                      "scoped": true,
                      "source": null,
                      "status": null,
                      "aliases": null,
                      "deleted": false,
                      "details": {
                        "asn": null,
                        "ssl": 1,
                        "uri": "https://attacksurface.app:8443",
                        "code": "403",
                        "port": 8443,
                        "forms": false,
                        "title": "CNAME Cross-User Banned | Cloudflare",
                        "verbs": null,
                        "cookies": null,
                        "headers": [
                          "date: Sat, 22 Jul 2023 04:35:01 GMT",
                          "content-type: text/html; charset=UTF-8",
                          "content-length: 6282",
                          "report-to: {\"endpoints\":[{\"url\":\"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=S73LNOORxYqJ7nlhuLVyKFRWA1NDKf7l45RmVQgHiaRAUf3pyrEVvjAwmkWTpkv0BqG4AjwQkd%2FDADXSOPIEwOuKWVPMHQ4ZkTbZRr1pPmMwbT0JfAlXcR%2BoFiWJn8zJPkmtfQm794Kh\"}],\"group\":\"cf-nel\",\"max_age\":604800}",
                          "nel: {\"success_fraction\":0,\"report_to\":\"cf-nel\",\"max_age\":604800}",
                          "x-frame-options: SAMEORIGIN",
                          "referrer-policy: same-origin",
                          "cache-control: private, max-age=0, no-store, no-cache, must-revalidate, post-check=0, pre-check=0",
                          "expires: Thu, 01 Jan 1970 00:00:01 GMT",
                          "server: cloudflare",
                          "cf-ray: 7ea8f97ff9d7081e-IAD",
                          "alt-svc: h3=\":8443\"; ma=86400"
                        ],
                        "host_id": 9416579,
                        "net_geo": "US",
                        "scripts": [
                          "https://performance.radar.cloudflare.com/beacon.js"
                        ],
                        "service": "https",
                        "auth.2fa": true,
                        "auth.any": false,
                        "dom_sha1": "4272956ee10a520790a681365631f1617b5c122c",
                        "net_name": "",
                        "protocol": "tcp",
                        "alt_names": [
                          "attacksurface.app",
                          "attacksurface.app"
                        ],
                        "auth.ntlm": false,
                        "generator": null,
                        "auth.basic": false,
                        "auth.forms": false,
                        "ip_address": "2606:4700:3035::6815:807",
                        "favicon_md5": null,
                        "fingerprint": [
                          {
                            "cpe": "cpe:2.3:s:cloudflare:cloudflare::",
                            "hide": false,
                            "tags": [
                              "CDN",
                              "WAF",
                              "PaaS"
                            ],
                            "type": "fingerprint",
                            "tasks": null,
                            "issues": null,
                            "method": "ident",
                            "update": null,
                            "vendor": "Cloudflare",
                            "product": "Cloudflare",
                            "version": null,
                            "inference": false,
                            "description": "Cloudflare - Headers Match",
                            "match_logic": "any",
                            "positive_matches": [
                              {
                                "match_type": "content_headers",
                                "match_content": "(?i-mx:^cf(-)?ray:)"
                              },
                              {
                                "match_type": "content_headers",
                                "match_content": "(?i-mx:^cf-ray:)"
                              },
                              {
                                "match_type": "content_headers",
                                "match_content": "(?i-mx:^server: cloudflare$)"
                              }
                            ]
                          }
                        ],
                        "geolocation": {
                          "city": "Toronto",
                          "postal": "M5A",
                          "country": "Canada",
                          "latitude": 43.6532,
                          "continent": "North America",
                          "longitude": -79.3832,
                          "time_zone": "America/Toronto",
                          "country_code": "CA",
                          "continent_code": "NA"
                        },
                        "api_endpoint": false,
                        "cloud_hosted": true,
                        "favicon_sha1": null,
                        "domain_cookies": null,
                        "redirect_chain": [],
                        "redirect_count": 0,
                        "cloud_providers": [
                          "Cloudflare"
                        ],
                        "net_country_code": null,
                        "certificate_chain": [
                          {
                            "expiration": "2023-09-30 10:16:38 +0000 UTC",
                            "issuerCommonName": "GTS CA 1P5",
                            "subjectCommonName": "attacksurface.app",
                            "signatureAlgorithm": "SHA256-RSA",
                            "certificateAuthority": false
                          },
                          {
                            "expiration": "2027-09-30 00:00:42 +0000 UTC",
                            "issuerCommonName": "GTS Root R1",
                            "subjectCommonName": "GTS CA 1P5",
                            "signatureAlgorithm": "SHA256-RSA",
                            "certificateAuthority": true
                          },
                          {
                            "expiration": "2028-01-28 00:00:42 +0000 UTC",
                            "issuerCommonName": "GlobalSign Root CA",
                            "subjectCommonName": "GTS Root R1",
                            "signatureAlgorithm": "SHA256-RSA",
                            "certificateAuthority": true
                          }
                        ],
                        "screenshot_exists": true,
                        "cloud_fingerprints": [
                          "cloudflare"
                        ],
                        "response_data_hash": "l2uJoJvtMPtz47QOjh3Fyx2A5dMp2Y6YLIr8C0AWZeU=",
                        "exfil_lookup_identifier": "1f1ff837b6c05d37ad393e3d2daf6821"
                      },
                      "summary": {
                        "http": {
                          "auth": {
                            "2fa": true,
                            "any": false,
                            "ntlm": false,
                            "basic": false,
                            "forms": false
                          },
                          "code": 403,
                          "title": "CNAME Cross-User Banned | Cloudflare",
                          "content": {
                            "hash": null,
                            "forms": false,
                            "favicon_hash": null
                          }
                        },
                        "ports": {
                          "tcp": [
                            8443
                          ],
                          "udp": [],
                          "count": 1
                        },
                        "vulns": {
                          "vulns": [],
                          "current_count": 0
                        },
                        "issues": {
                          "current_count": 2,
                          "all_time_count": 2,
                          "critical_or_high": false,
                          "current_with_cve": 0,
                          "current_by_severity": {
                            "5": 2
                          },
                          "all_time_by_severity": {
                            "5": 2
                          }
                        },
                        "scoped": true,
                        "network": {
                          "asn": null,
                          "name": "",
                          "type": null,
                          "route": null
                        },
                        "technology": {
                          "cpes": [
                            {
                              "cpe": "cpe:2.3:s:cloudflare:cloudflare::",
                              "detection_method": "Cloudflare - Headers Match"
                            },
                            {
                              "cpe": "cpe:2.3:s:attacksurface:attacksurface::",
                              "detection_method": "Host DNS Resolution: subfinder"
                            }
                          ],
                          "cloud": true,
                          "technologies": [
                            "Cloudflare",
                            "Attacksurface"
                          ],
                          "cloud_providers": [
                            "Cloudflare"
                          ],
                          "technology_labels": [
                            "CDN",
                            "PaaS",
                            "WAF",
                            "enterprise software",
                            "hosting",
                            "security",
                            "technology"
                          ]
                        },
                        "geolocation": {
                          "asn": null,
                          "city": "Toronto",
                          "latitude": 43.6532,
                          "longitude": -79.3832,
                          "country_code": "CA",
                          "country_name": null
                        },
                        "task_results": [
                          "port_scan",
                          "port_scan_lambda",
                          "search_shodan_ranger",
                          "port_scan",
                          "port_scan_lambda",
                          "search_shodan_ranger"
                        ],
                        "screenshot_exists": true
                      },
                      "category": null,
                      "ancestors": [
                        {
                          "name": "attacksurface.app",
                          "type": "Intrigue::Entity::Domain"
                        }
                      ],
                      "deny_list": false,
                      "last_seen": "2023-07-22T06:19:37.000Z",
                      "allow_list": false,
                      "collection": "broadscopeenabled_g6zjj10",
                      "confidence": null,
                      "created_at": "2023-04-20T16:47:46.856Z",
                      "dynamic_id": "Intrigue::Entity::Uri#https://attacksurface.app:8443",
                      "first_seen": "2023-04-20T16:47:03.000Z",
                      "updated_at": "2023-07-22T06:21:11.497Z",
                      "alias_group": "088de90f6772b88c94554175dea71bdbe542db40",
                      "description": null,
                      "fingerprint": [
                        {
                          "cpe": "cpe:2.3:s:cloudflare:cloudflare::",
                          "hide": false,
                          "tags": [
                            "CDN",
                            "WAF",
                            "PaaS"
                          ],
                          "type": "fingerprint",
                          "tasks": null,
                          "issues": null,
                          "method": "ident",
                          "update": null,
                          "vendor": "Cloudflare",
                          "product": "Cloudflare",
                          "version": null,
                          "inference": false,
                          "description": "Cloudflare - Headers Match",
                          "match_logic": "any",
                          "local_icon_path": "/assets/fingerprints/cloudflare.png",
                          "positive_matches": [
                            {
                              "match_type": "content_headers",
                              "match_content": "(?i-mx:^cf(-)?ray:)"
                            },
                            {
                              "match_type": "content_headers",
                              "match_content": "(?i-mx:^cf-ray:)"
                            },
                            {
                              "match_type": "content_headers",
                              "match_content": "(?i-mx:^server: cloudflare$)"
                            }
                          ]
                        }
                      ],
                      "details_file": "data/v5/broadscopeenabled_g6zjj10/2023_07_22_06_19_37/entities/dd31a13bb1d554c1e522fa7703ce8650d263b15d.json",
                      "task_results": [
                        {
                          "name": "port_scan_on_172.67.156.152",
                          "task": "port_scan",
                          "depth": 4,
                          "entity_name": "172.67.156.152",
                          "entity_type": "Intrigue::Entity::IpAddress"
                        },
                        {
                          "name": "port_scan_lambda_on_172.67.156.152",
                          "task": "port_scan_lambda",
                          "depth": 4,
                          "entity_name": "172.67.156.152",
                          "entity_type": "Intrigue::Entity::IpAddress"
                        },
                        {
                          "name": "search_shodan_ranger_on_172.67.156.152",
                          "task": "search_shodan_ranger",
                          "depth": 4,
                          "entity_name": "172.67.156.152",
                          "entity_type": "Intrigue::Entity::IpAddress"
                        },
                        {
                          "name": "port_scan_on_104.21.8.7",
                          "task": "port_scan",
                          "depth": 4,
                          "entity_name": "104.21.8.7",
                          "entity_type": "Intrigue::Entity::IpAddress"
                        },
                        {
                          "name": "port_scan_lambda_on_104.21.8.7",
                          "task": "port_scan_lambda",
                          "depth": 4,
                          "entity_name": "104.21.8.7",
                          "entity_type": "Intrigue::Entity::IpAddress"
                        },
                        {
                          "name": "search_shodan_ranger_on_104.21.8.7",
                          "task": "search_shodan_ranger",
                          "depth": 4,
                          "entity_name": "104.21.8.7",
                          "entity_type": "Intrigue::Entity::IpAddress"
                        }
                      ],
                      "collection_id": 142553,
                      "scoped_reason": "allow_list_override",
                      "collection_name": "broadscopeenabled_g6zjj10",
                      "collection_type": "user_collection",
                      "collection_uuid": "2ffc71a9-8588-4612-9a1c-95784e7b9b8e",
                      "collection_naics": null,
                      "organization_uuid": "075892c8-fe6f-454e-a071-34a7342c16a3",
                      "elasticsearch_mappings_hash": "8ed8ab645a58aab29a6a36b4ab0512fa"
                    },
                    "point_in_time": "2023-07-23T00:00:00.000Z"
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

← [Time Series](../time-series.md) · [up](../README.md) · [Get Entity points in time](get_time-series-points-in-time-entities-uid.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_time-series-point-in-time-entities-uid>.*
