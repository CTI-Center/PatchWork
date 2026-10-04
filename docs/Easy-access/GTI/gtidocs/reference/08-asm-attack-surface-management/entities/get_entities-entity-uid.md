---
title: "Get Detail"
source: https://gtidocs.virustotal.com/reference/get_entities-entity-uid
slug: get_entities-entity-uid
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:20.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Entities](../entities.md) › Get Detail

---

# get-detail

Obtains an individual entity's searchable details

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
    "/entities/{entity_uid}": {
      "get": {
        "tags": [
          "Entities"
        ],
        "summary": "Get Detail",
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
            "name": "entity_uid",
            "in": "path",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Required: id from /api/v3/asm/search/entities/",
            "example": "1f7b1b98a62ee28bf509871a1f573287fd51b70436b2fa6a9f9b0140e9eaddb6"
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
                  "example": "Fri, 17 Feb 2023 22:08:18 GMT"
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
                  "example": "6134"
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
                  "message": "successfully returned entity",
                  "result": {
                    "uuid": "89fcba93-ddc9-44a6-a78c-615db734aa23",
                    "dynamic_id": "Intrigue::Entity::IpAddress#192.168.1.109",
                    "collection_name": "collectionname_a6mz56o",
                    "alias_group": null,
                    "aliases": null,
                    "allow_list": true,
                    "ancestors": [
                      {
                        "name": "192.168.1.109",
                        "type": "Intrigue::Entity::IpAddress"
                      }
                    ],
                    "category": null,
                    "collection_naics": null,
                    "confidence": null,
                    "deleted": false,
                    "deny_list": false,
                    "details": {
                      "name": "192.168.1.109",
                      "ports": [
                        {
                          "number": 80,
                          "protocol": "tcp"
                        }
                      ],
                      "version": 4,
                      "net_name": "",
                      "whitelist": true,
                      "geolocation": {
                        "asn": {
                          "asn": 22612,
                          "isp": "Namecheap",
                          "name": "Namecheap, Inc.",
                          "organization": "Web-hosting.com",
                          "connection_type": "Corporate"
                        },
                        "city": "Macenta",
                        "postal": null,
                        "country": "Guinea",
                        "latitude": 8.53829,
                        "continent": "Africa",
                        "longitude": -9.47282,
                        "time_zone": "Africa/Conakry",
                        "country_code": "GN",
                        "continent_code": "AF"
                      },
                      "network.asn": "AS22612",
                      "network.rir": "ARIN",
                      "resolutions": [],
                      "cloud_hosted": false,
                      "network.name": "",
                      "network.block": "192.168.1.0/21",
                      "cloud_providers": [],
                      "whois_full_text": "\n#\n# ARIN WHOIS data and services are subject to the Terms of Use\n# available at: https://www.arin.net/resources/registry/whois/tou/\n#\n# If you see inaccuracies in the results, please report at\n# https://www.arin.net/resources/registry/whois/inaccuracy_reporting/\n#\n# Copyright 1997-2022, American Registry for Internet Numbers, Ltd.\n#\n\n\nNetRange:       192.168.1.0 - 192.168.1.255\nCIDR:           192.168.1.0/21\nNetName:        NCNET-3\nNetHandle:      NET-192-64-112-0-1\nParent:         NET192 (NET-192-0-0-0-0)\nNetType:        Direct Allocation\nOriginAS:       AS16626, AS174, AS3356, AS4323, AS22612, AS32421\nOrganization:   Namecheap, Inc. (NAMEC-4)\nRegDate:        2012-12-17\nUpdated:        2015-03-24\nComment:        http://namecheap.com\r\nComment:        for any abuse please use: abuse@namecheap.com\nRef:            https://rdap.arin.net/registry/ip/192.168.1.0\n\n\nOrgName:        Namecheap, Inc.\nOrgId:          NAMEC-4\nAddress:        11400 W. Olympic Blvd. Suite 200\nCity:           Los Angeles\nStateProv:      CA\nPostalCode:     90064\nCountry:        US\nRegDate:        2011-01-28\nUpdated:        2017-01-28\nRef:            https://rdap.arin.net/registry/entity/NAMEC-4\n\nReferralServer:  rwhois://whois.namecheaphosting.com:4321\n\nOrgTechHandle: TECHT4-ARIN\nOrgTechName:   Tech team\nOrgTechPhone:  +1-661-310-2107 \nOrgTechEmail:  tech@namecheaphosting.com\nOrgTechRef:    https://rdap.arin.net/registry/entity/TECHT4-ARIN\n\nOrgTechHandle: EFIME-ARIN\nOrgTechName:   Efimenko, Igor \nOrgTechPhone:  +1-323-375-2822 \nOrgTechEmail:  igor.e@namecheap.com\nOrgTechRef:    https://rdap.arin.net/registry/entity/EFIME-ARIN\n\nOrgAbuseHandle: ABUSE2885-ARIN\nOrgAbuseName:   Abuse team\nOrgAbusePhone:  +1-323-375-2822 \nOrgAbuseEmail:  abuse@namecheaphosting.com\nOrgAbuseRef:    https://rdap.arin.net/registry/entity/ABUSE2885-ARIN\n\n\n#\n# ARIN WHOIS data and services are subject to the Terms of Use\n# available at: https://www.arin.net/resources/registry/whois/tou/\n#\n# If you see inaccuracies in the results, please report at\n# https://www.arin.net/resources/registry/whois/inaccuracy_reporting/\n#\n# Copyright 1997-2022, American Registry for Internet Numbers, Ltd.\n#\n\n\n%rwhois V-1.0,V-1.5:00090h:00 billing.web-hosting.com (Ubersmith RWhois Server V-4.5.5)\nautharea=192.168.1.0/24\nxautharea=192.168.1.0/24\nnetwork:Class-Name:network\nnetwork:Auth-Area:192.168.1.0/24\nnetwork:ID:NET-79088.192.168.1.0/24\nnetwork:Network-Name:anycast-edge-fwd-range\nnetwork:IP-Network:192.168.1.0/24\nnetwork:IP-Network-Block:192.168.1.0 - 192.168.1255\nnetwork:Org-Name:Web-hosting.com\nnetwork:Street-Address:\nnetwork:City:Atlanta\nnetwork:State:GA\nnetwork:Postal-Code:30303/3030\nnetwork:Country-Code:US\nnetwork:Tech-Contact:MAINT-79088.192.168.1.0/24\nnetwork:Created:20190523134201000\nnetwork:Updated:20190523163005000\nnetwork:Updated-By:net-admin@namecheap.com\ncontact:POC-Name:Network team\ncontact:POC-Email:net-admin@namecheap.com\ncontact:POC-Phone:\ncontact:Tech-Name:Network team\ncontact:Tech-Email:net-admin@namecheap.com\ncontact:Tech-Phone:\ncontact:Abuse-Name:Abuse team\ncontact:Abuse-Email:abuse@namecheaphosting.com\n%ok\n",
                      "network.country_code": "US",
                      "exfil_lookup_identifier": "61539b426980b7959a65f017657025ab",
                      "network.allocation_date": "2012-12-17"
                    },
                    "details_file": "data/v4/collectionname_a6mz56o/2022_10_05/collectionname_a6mz56o/entities/1b3e614b751e35dfab02737d474e133e862ef80c.json",
                    "description": null,
                    "first_seen": "2022-10-05T19:27:33.000Z",
                    "hidden": false,
                    "last_seen": "2022-10-05T19:27:33.000Z",
                    "name": "192.168.14109",
                    "scoped": true,
                    "scoped_reason": "allow_list_override",
                    "seed": null,
                    "source": null,
                    "status": null,
                    "task_results": [
                      {
                        "name": "search_shodan_on_192.168.1.109",
                        "task": "search_shodan",
                        "depth": 4,
                        "entity_name": "192.168.1.109",
                        "entity_type": "Intrigue::Entity::IpAddress"
                      },
                      {
                        "name": "enrich/uri_on_http://192.168.1.109:80",
                        "task": "enrich/uri",
                        "depth": 4,
                        "entity_name": "http://192.168.1.109:80",
                        "entity_type": "Intrigue::Entity::Uri"
                      }
                    ],
                    "type": "Intrigue::Entity::IpAddress",
                    "uid": "1fb70436b2fa66a62ee1b1b989eaddb871a1f573287fd5128bf509a9f9b0140e",
                    "created_at": "2022-10-05T19:28:27.973Z",
                    "updated_at": "2022-10-05T19:28:27.978Z",
                    "collection_id": 134840,
                    "elasticsearch_mappings_hash": null,
                    "collection": "collectionname_a6mz56o",
                    "collection_uuid": "f12c71db-d34d-4733-a19e-b8742ed7eb70",
                    "organization_uuid": "075892c8-fe6f-454e-a071-34a7342c16a3",
                    "collection_type": "user_collection",
                    "fingerprint": [],
                    "summary": {
                      "scoped": true,
                      "issues": {
                        "current_with_cve": 0,
                        "current_by_severity": {},
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
                        "latitude": 8.53829,
                        "longitude": -9.47282,
                        "asn": null
                      },
                      "ports": {
                        "tcp": [
                          80
                        ],
                        "udp": [],
                        "count": 1
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
                    },
                    "tags": []
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

← [Search Entities](get_search-entities-search-string.md) · [up](../README.md) · [Get Full Detail](get_entities-entity-uid-raw.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_entities-entity-uid>.*
