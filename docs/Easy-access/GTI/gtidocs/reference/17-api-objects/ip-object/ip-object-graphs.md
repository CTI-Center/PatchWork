---
title: "🔀 graphs"
source: https://gtidocs.virustotal.com/reference/ip-object-graphs
slug: ip-object-graphs
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:43:30.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [IP addresses](../ip-object.md) › 🔀 graphs

---

# 🔀-graphs

The *graphs* relationship returns a list of **graphs containing the given IP address**.

This relationship can be retrieved using the [relationships API endpoint](../../03-ioc-investigation/ip-addresses/ip-relationships.md). The response contains a list of [Graph](../graph-object.md)  objects.

```json /ip_addresses/{ip_address}/graphs
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
                        "source": "3c6fa0946d1b42654e794e8a44214ed94238542a41d94c974b38451bd5c463b8",
                        "target": "relationships_contacted_domains_3c6fa0946d1b42654e794e8a44214ed94238542a41d94c974b38451bd5c463b8"
                    },
                    {
                        "connection_type": "contacted_ips",
                        "source": "3c6fa0946d1b42654e794e8a44214ed94238542a41d94c974b38451bd5c463b8",
                        "target": "relationships_contacted_ips_3c6fa0946d1b42654e794e8a44214ed94238542a41d94c974b38451bd5c463b8"
                    },
                    {
                        "connection_type": "contacted_domains",
                        "source": "relationships_contacted_domains_3c6fa0946d1b42654e794e8a44214ed94238542a41d94c974b38451bd5c463b8",
                        "target": "blablabla.com"
                    },
                    {
                        "connection_type": "contacted_ips",
                        "source": "relationships_contacted_ips_3c6fa0946d1b42654e794e8a44214ed94238542a41d94c974b38451bd5c463b8",
                        "target": "65.131.145.248"
                    }
                ],
                "nodes": [
                    {
                        "entity_attributes": {
                            "has_detections": true,
                            "type_tag": "peexe"
                        },
                        "entity_id": "3c6fa0946d1b42654e794e8a44214ed94238542a41d94c974b38451bd5c463b8",
                        "fx": 196.85105675839864,
                        "fy": -187.1954091906271,
                        "index": 0,
                        "text": "3c6fa0946d1b42654e794e8a44214ed94238542a41d94c974b38451bd5c463b8",
                        "type": "file",
                        "x": 196.85105675839864,
                        "y": -187.1954091906271
                    },
                    {
                        "entity_attributes": {},
                        "entity_id": "relationships_contacted_domains_3c6fa0946d1b42654e794e8a44214ed94238542a41d94c974b38451bd5c463b8",
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
                    },
                    {
                        "entity_attributes": {},
                        "entity_id": "relationships_contacted_ips_3c6fa0946d1b42654e794e8a44214ed94238542a41d94c974b38451bd5c463b8",
                        "fx": 194.97214955287814,
                        "fy": -152.8770386477522,
                        "index": 4,
                        "text": "",
                        "type": "relationship",
                        "x": 194.97214955287814,
                        "y": -152.8770386477522
                    },
                    {
                        "entity_attributes": {
                            "country": "US"
                        },
                        "entity_id": "65.131.145.248",
                        "fx": 195.29917084952132,
                        "fy": -122.74807539531734,
                        "index": 5,
                        "text": "",
                        "type": "ip_address",
                        "x": 195.29917084952132,
                        "y": -122.74807539531734
                    }
                ],
                "views_count": 3
            },
            "id": "gf2d46f3b83a643ae8305233df3e7c3fbd35743fbc53f4831a3ff35d3329304cf",
            "links": {
                "self": "https://www.virustotal.com/api/v3/graphs/gf2d46f3b83a643ae8305233df3e7c3fbd35743fbc53f4831a3ff35d3329304cf"
            },
            "type": "graph"
        }
    ],
    "links": {
        "next": "https://www.virustotal.com/api/v3/ip_addresses/65.131.145.248/graphs?cursor=True%3ACr4HCvADCsID9yO2-Tz_____jIGJlo2KjIuQi56TnJOQipv_AAD_dG2goJmLjKCg_wAA_12ej4-akZiWkZr_AAD_c3R4lpGbmof_AAD_XZiNno-XjP8AAP9zdG2bkJyglpv_AAD_XZiZzZvLyZmbncfInsnLnZ6ax8fPys3MnpuZm5rInJuZnZueysjLz5mdnMrNmcvHnM6eyZm4zMqbnszNxp7Py5yZ_wAA_3N_mJnNm8vJmZudx8ieycudnprHx8_Kzcyem5mbmsicm5mdm57KyMvPmZ24ys2Zy8eczp7JmZnMypuezM3Gns_LnJn_AAD__wD-__6MgYmWjYqMi5CL4pOck5CKm_8AdG2goJmLjKCg_wBdno-PmpGYlpGa_wBzdG2WkZuah_8AXZiNno-XjP8Ac3Rtm5CcoJab_wBdmJnNm8vJmZudx8ieycudnprHx8_Kzcyem5mbmsicm5mdm57KyMvPmZ2cys2Zy8eczp7JmZnMypu4zM3Gns_LnJn_AHN_mJnNm8vJmZudx8ieycudnprHx8_Kzcyem5mbmsicm5mdm57KyMvPmZ2cys2Zy8e4zp7JmZnMypuezM3Gns_LnJn_AP_-EAEh214v0Zsk1Mk5AAAAAMMGSdxIAVAAWgsJN7QS-43PoHEQA2CYxbn0B4INRG9jdW1lbnRJbmRleBqUAyhBTkQgKElTICJjdXN0b21lcl9uYW1lIiAiYXBwZW5naW5lIikgKElTI4Jncm91cF9uYW1lIiAic352aXJ1c3RvdGFsY2xvdWQiKSAoSVMgIm5hbWVzcGFjZSIgIiIpIChJUyAiaW5kZXhfbmFtZSIgImdyYXBocyIpIChBTkQgKElTICJyYXRvbV9ub2RlX2lwX2FkZHJlc3MiICI2Ni4xN4EuMjQ4LjE3OCIpIChPUiAoSVMgInJhdG9tX293bmVyIiAibWdtYWNpYXMiKSAoSVMgInJhdG9tX2Vka4RvcnMiICJ1Om1nbWFjaWFzIikgKElTICJyYXRvbV9lZGl0b3JzIiAiZzp2aXJ1c3RvdGFsIikgKElTI4JyYXRvbV92aWV3ZXJzIiAiKiIpIChJUyAicmF0b21fdmlld2VycyIgInU6bWdtYWNpYXMiKSAoSVMgI4JhdG9tX3ZpZXdlcnMiICJnOnZpcnVzdG90YWwiKSkgKElTICJyYXRvbV9kZWxldGVkIiAiZmFsc2UiK4kpOhkKDChOIG9yZGVyX2lkKRABGQAAAAAAAPD_SgUIAEDoBw&limit=1",
        "self": "https://www.virustotal.com/api/v3/ip_addresses/65.131.145.248/graphs?limit=1"
    },
    "meta": {
        "count": 87,
        "cursor": "True:Cr4HCvADCsID9yO2-Tz_____jIGJlo2KjIuQi56TnJOQipv_AAD_dG2goJmLjKCg_wAA_12ej4-akZiWkZr_AAD_c3R4lpGbmof_AAD_XZiNno-XjP8AAP9zdG2bkJyglpv_AAD_XZiZzZvLyZmbncfInsnLnZ6ax8fPys3MnpuZm5rInJuZnZueysjLz5mdnMrNmcvHnM6eyZm4zMqbnszNxp7Py5yZ_wAA_3N_mJnNm8vJmZudx8ieycudnprHx8_Kzcyem5mbmsicm5mdm57KyMvPmZ24ys2Zy8eczp7JmZnMypuezM3Gns_LnJn_AAD__wD-__6MgYmWjYqMi5CL4pOck5CKm_8AdG2goJmLjKCg_wBdno-PmpGYlpGa_wBzdG2WkZuah_8AXZiNno-XjP8Ac3Rtm5CcoJab_wBdmJnNm8vJmZudx8ieycudnprHx8_Kzcyem5mbmsicm5mdm57KyMvPmZ2cys2Zy8eczp7JmZnMypu4zM3Gns_LnJn_AHN_mJnNm8vJmZudx8ieycudnprHx8_Kzcyem5mbmsicm5mdm57KyMvPmZ2cys2Zy8e4zp7JmZnMypuezM3Gns_LnJn_AP_-EAEh214v0Zsk1Mk5AAAAAMMGSdxIAVAAWgsJN7QS-43PoHEQA2CYxbn0B4INRG9jdW1lbnRJbmRleBqUAyhBTkQgKElTICJjdXN0b21lcl9uYW1lIiAiYXBwZW5naW5lIikgKElTI4Jncm91cF9uYW1lIiAic352aXJ1c3RvdGFsY2xvdWQiKSAoSVMgIm5hbWVzcGFjZSIgIiIpIChJUyAiaW5kZXhfbmFtZSIgImdyYXBocyIpIChBTkQgKElTICJyYXRvbV9ub2RlX2lwX2FkZHJlc3MiICI2Ni4xN4EuMjQ4LjE3OCIpIChPUiAoSVMgInJhdG9tX293bmVyIiAibWdtYWNpYXMiKSAoSVMgInJhdG9tX2Vka4RvcnMiICJ1Om1nbWFjaWFzIikgKElTICJyYXRvbV9lZGl0b3JzIiAiZzp2aXJ1c3RvdGFsIikgKElTI4JyYXRvbV92aWV3ZXJzIiAiKiIpIChJUyAicmF0b21fdmlld2VycyIgInU6bWdtYWNpYXMiKSAoSVMgI4JhdG9tX3ZpZXdlcnMiICJnOnZpcnVzdG90YWwiKSkgKElTICJyYXRvbV9kZWxldGVkIiAiZmFsc2UiK4kpOhkKDChOIG9yZGVyX2lkKRABGQAAAAAAAPD_SgUIAEDoBw"
    }
}
```

---

← [🔀 comments](ip-object-comments.md) · [up](../README.md) · [🔀 historical_ssl_certificates](ip-object-historical-ssl-certificates.md) →

*Archived from <https://gtidocs.virustotal.com/reference/ip-object-graphs>.*
