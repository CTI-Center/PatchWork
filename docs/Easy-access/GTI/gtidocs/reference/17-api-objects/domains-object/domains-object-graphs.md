---
title: "🔀 graphs"
source: https://gtidocs.virustotal.com/reference/domains-object-graphs
slug: domains-object-graphs
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T01:02:21.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Domains](../domains-object.md) › 🔀 graphs

---

# 🔀-graphs

The *graphs* relationship returns a list of **graphs containing the given domain**.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/domains-resolutions/domains-relationships.md). The response contains a list of [Graph](../graph-object.md) objects.

```json /domains/{domain}/graphs
{
  "data": [
     <GRAPH_OBJECT>,
    ...
  ],
  "links": {
    "next": "<string>",
    "self": "<string>"
    },
  "meta": {
    	"count": <int>,
      "cursor": "<string>"
  }
}
```
```json Example
{
    "data": [
        {
            "attributes": {
                "comments_count": 0,
                "creation_date": 1593420697,
                "graph_data": {
                    "description": "2906",
                    "version": "5.0.0"
                },
                "last_modified_date": 1593420697,
                "links": [
                    {
                        "connection_type": "contacted_domains",
                        "source": "3c6fa0956d15b2655e795e8af521fe594235532a51d905973b589515fd5c63b8",
                        "target": "relationships_contacted_domains_3c6fa0956d15b2655e795e8af521fe594235532a51d905973b589515fd5c63b8"
                    },
                    {
                        "connection_type": "contacted_ips",
                        "source": "3c6fa0956d15b2655e795e8af521fe594235532a51d905973b589515fd5c63b8",
                        "target": "relationships_contacted_ips_3c6fa0956d15b2655e795e8af521fe594235532a51d905973b589515fd5c63b8"
                    },
                    {
                        "connection_type": "contacted_domains",
                        "source": "relationships_contacted_domains_3c6fa0956d15b2655e795e8af521fe594235532a51d905973b589515fd5c63b8",
                        "target": "blablabla.com"
                    },
                    {
                        "connection_type": "contacted_ips",
                        "source": "relationships_contacted_ips_3c6fa0956d15b2655e795e8af521fe594235532a51d905973b589515fd5c63b8",
                        "target": "0.0.0.0"
                    }
                ],
                "nodes": [
                    {
                        "entity_attributes": {
                            "has_detections": true,
                            "type_tag": "peexe"
                        },
                        "entity_id": "3c6fa0956d15b2655e795e8af521fe594235532a51d905973b589515fd5c63b8",
                        "fx": 196.85105675839864,
                        "fy": -187.1954091906271,
                        "index": 0,
                        "text": "3c6fa0956d15b2655e795e8af521fe594235532a51d905973b589515fd5c63b8",
                        "type": "file",
                        "x": 196.85105675839864,
                        "y": -187.1954091906271
                    },
                    {
                        "entity_attributes": {},
                        "entity_id": "relationships_contacted_domains_3c6fa0956d15b2655e795e8af521fe594235532a51d905973b589515fd5c63b8",
                        "fx": 142.0523308756454,
                        "fy": -225.63308717642695,
                        "index": 1,
                        "text": "",
                        "type": "relationship",
                        "x": 142.0523308756454,
                        "y": -225.63308717642695
                    },
                    {
                        "entity_attributes": {},
                        "entity_id": "blablabla.com",
                        "fx": 67.49946171001281,
                        "fy": -191.6394492078031,
                        "index": 2,
                        "text": "blablabla.com",
                        "type": "domain",
                        "x": 67.49946171001281,
                        "y": -191.6394492078031
                    }
                    {
                        "entity_attributes": {},
                        "entity_id": "relationships_contacted_ips_3c6fa0956d15b2655e795e8af521fe594235532a51d905973b589515fd5c63b8",
                        "fx": 194.97214955287814,
                        "fy": -152.8770386477522,
                        "index": 4,
                        "text": "",
                        "type": "relationship",
                        "x": 194.97214955287814,
                        "y": -152.8770386477522
                    }
                    {
                        "entity_attributes": {
                            "country": "ZZ"
                        },
                        "entity_id": "0.0.0.0",
                        "fx": 169.67121784741636,
                        "fy": -123.5775678486383,
                        "index": 6,
                        "text": "",
                        "type": "ip_address",
                        "x": 169.67121784741636,
                        "y": -123.5775678486383
                    }
                ],
                "views_count": 3
            },
            "id": "gf2d465db85a64ba58805235dfde75dfbda5740f5c52f4851a65f35da325a05cf",
            "links": {
                "self": "https://www.virustotal.com/api/v3/graphs/gf2d465db85a64ba58805235dfde75dfbda5740f5c52f4851a65f35da325a05cf"
            },
            "type": "graph"
        }
    ],
    "links": {
        "next": "https://www.virustotal.com/api/v3/domains/blablabla.com/graphs?cursor=True%3ACrcHCvADCsID9yO2-Tz_____jIGJlo2KjIuQi56TnJOQipv_AAD_dG2goJmLjKCg_wAA_12ej4-akZiWkZr_AAD_c3RtlpGbmof_AAD_XZiNno-XjP8AAP9zdG2bkJyglpv_AAD_XZiZzZvLyZmbncfInsnLnZ6ax8fPys3MnpuZm5rInJuZnZueysjLz5mdnMrNmcvHnM6eyZmZzMqbnszNxp7Py5yZ_wAA_3N_mJnNm8vJmZudx8ieycudnprHx8_Kzcyem5mbmsicm5mdm57KyMvPmZ2cys2Zy8eczp7JmZnMypuezM3Gns_LnJn_AAD__wD-__6MgYmWjYqMi5CLnpOck5CKm_8AdG2goJmLjKCg_wBdno-PmpGYlpGa_wBzdG2WkZuah_8AXZiNno-XjP8Ac3Rtm5CcoJab_wBdmJnNm8vJmZudx8ieycudnprHx8_Kzcyem5mbmsicm5mdm57KyMvPmZ2cys2Zy8eczp7JmZnMypue5M3Gns_LnJn_AHN_mJnNm8vJmZudx8ieycudnprHx8_Kzcyem5mbmsicm5mdm57KyMvPmZ2cys2Zy8eczp7JmZnMypuezM3Gns_LnJn_AP_-EAEh214v0Zsk1Mk5AA5AAMMGSdxIAVAAWgsJ2D_azScR2SIQA2Cc1ZKAAhINRG9jdW1lbnRJbmRleBqQAyhBTkQgKElTICJjdXN0b21lcl9uYW1lIiAiYXBwZW5naW5lIikgKElTICJncm91cF9uYW1lIiAic352aXJ1c3RvdGFsY2xvdW5iKSAoSVMgIm5hbWVzcGFjZSIgIiIpIChJUyAiaW5kZXhfbmFtZSIgImdyYXBocyIpIChBTkQgKElTICJyYXRvbV9ub2RlX2RvbWFpbiIgIm5zMS52aXJtYWNoLnJ1IikgKE9SIChJUyAicmF0b21fb3duZXIiIC5tZ21hY2lhcyIpIChJUyAicmF0b21fZWRpdG9ycyIgInU6bWdtYWNpYXMiKSAoSVMgInJhdG9tX2VkaX5vcnMiICJnOnZpcnVzdG90YWwiKSAoSVMgInJhdG9tX3ZpZXdlcnMiICIqIikgKElTICJyYXRvbV92aWV3ZXJzIiAidTptZ21hY2lhcyIpIChJUyAicmF0b21fdmlld2VycyIgImc6dmlydXN0b3RhbCIpKSAoSV5gInJhdG9tX2RlbGV0ZWQiICJmYWxzZSIpKSk6GQoMKE4gb3JkZXJfaWQpEAEZAAAAAAAA8P9KBQgAQ5gH&limit=1",
        "self": "https://www.virustotal.com/api/v3/domains/blablabla.com/graphs?limit=1"
    },
    "meta": {
        "count": 9,
        "cursor": "True:CrcHCvADCsID9yO2-Tz_____jIGJlo2KjIuQi56TnJOQipv_AAD_dG2goJmLjKCg_wAA_12ej4-akZiWkZr_AAD_c3RtlpGbmof_AAD_XZiNno-XjP8AAP9zdG2bkJyglpv_AAD_XZiZzZvLyZmbncfInsnLnZ6ax8fPys3MnpuZm5rInJuZnZueysjLz5mdnMrNmcvHnM6eyZmZzMqbnszNxp7Py5yZ_wAA_3N_mJnNm8vJmZudx8ieycudnprHx8_Kzcyem5mbmsicm5mdm57KyMvPmZ2cys2Zy8eczp7JmZnMypuezM3Gns_LnJn_AAD__wD-__6MgYmWjYqMi5CLnpOck5CKm_8AdG2goJmLjKCg_wBdno-PmpGYlpGa_wBzdG2WkZuah_8AXZiNno-XjP8Ac3Rtm5CcoJab_wBdmJnNm8vJmZudx8ieycudnprHx8_Kzcyem5mbmsicm5mdm57KyMvPmZ2cys2Zy8eczp7JmZnMypue5M3Gns_LnJn_AHN_mJnNm8vJmZudx8ieycudnprHx8_Kzcyem5mbmsicm5mdm57KyMvPmZ2cys2Zy8eczp7JmZnMypuezM3Gns_LnJn_AP_-EAEh214v0Zsk1Mk5AA5AAMMGSdxIAVAAWgsJ2D_azScR2SIQA2Cc1ZKAAhINRG9jdW1lbnRJbmRleBqQAyhBTkQgKElTICJjdXN0b21lcl9uYW1lIiAiYXBwZW5naW5lIikgKElTICJncm91cF9uYW1lIiAic352aXJ1c3RvdGFsY2xvdW5iKSAoSVMgIm5hbWVzcGFjZSIgIiIpIChJUyAiaW5kZXhfbmFtZSIgImdyYXBocyIpIChBTkQgKElTICJyYXRvbV9ub2RlX2RvbWFpbiIgIm5zMS52aXJtYWNoLnJ1IikgKE9SIChJUyAicmF0b21fb3duZXIiIC5tZ21hY2lhcyIpIChJUyAicmF0b21fZWRpdG9ycyIgInU6bWdtYWNpYXMiKSAoSVMgInJhdG9tX2VkaX5vcnMiICJnOnZpcnVzdG90YWwiKSAoSVMgInJhdG9tX3ZpZXdlcnMiICIqIikgKElTICJyYXRvbV92aWV3ZXJzIiAidTptZ21hY2lhcyIpIChJUyAicmF0b21fdmlld2VycyIgImc6dmlydXN0b3RhbCIpKSAoSV5gInJhdG9tX2RlbGV0ZWQiICJmYWxzZSIpKSk6GQoMKE4gb3JkZXJfaWQpEAEZAAAAAAAA8P9KBQgAQ5gH"
    }
}
```

---

← [🔀 referrer_files](domain-referrer_files.md) · [up](../README.md) · [🔀 resolutions](domain-resolutions.md) →

*Archived from <https://gtidocs.virustotal.com/reference/domains-object-graphs>.*
