---
title: "Create a graph"
source: https://gtidocs.virustotal.com/reference/create-graphs
slug: create-graphs
section: reference
group: "Threat Graph"
updatedAt: 2025-09-25T00:38:35.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [Threat Graph](../README.md) › [Threat Graphs](../threat-graphs.md) › Create a graph

---

# create-a-graph

This endpoint can be used to create new graphs. Note that private graphs will increment the usage of the private graphs quota in your Google Threat Intelligence plan.

```json Request example
{
  "data": {
    "attributes": {
      "comments_count": 0,
      "creation_date": 1599060646,
      "graph_data": {
        "description": "test",
        "version": "5.0.0"
      },
      "last_modified_date": 1599117623,
      "links": [
        {
          "connection_type": "last_serving_ip_address",
          "source": "ecd87dff4decb36ebf35cf2d327cce62fe1e5666d694c4b0f11ff67d540ff4dc",
          "target": "relationships_last_serving_ip_address_ecd87dff4decb36ebf35cf2d327cce62fe1e5666d694c4b0f11ff67d540ff4dc"
        },
        {
          "connection_type": "last_serving_ip_address",
          "source": "relationships_last_serving_ip_address_e743cffce9efddfb4f1d7e7dc3c10c6d562e61b5f65e6dd3fd4f28b604fcc2f6",
          "target": "138.133.35.39"
        },
        {
          "connection_type": "contacted_ips",
          "source": "e743cffce9efddfb4f1d7e7dc3c10c6d562e61b5f65e6dd3fd4f28b604fcc2f6",
          "target": "relationships_contacted_ips_e743cffce9efddfb4f1d7e7dc3c10c6d562e61b5f65e6dd3fd4f28b604fcc2f6"
        },
        {
          "connection_type": "contacted_ips",
          "source": "relationships_contacted_ips_e743cffce9efddfb4f1d7e7dc3c10c6d562e61b5f65e6dd3fd4f28b604fcc2f6",
          "target": "138.133.35.39"
        },
        {
          "connection_type": "commonality",
          "source": "relationships_commonality_106438826",
          "target": "f053cb783411211b54e2837ec01e0998e3d9bc042f599d95f7f2cb4ba348305d"
        },
        {
          "connection_type": "hunting",
          "source": "relationships_hunting_6534979578789888",
          "target": "5a041d8d72fc12d21e09fd781831ff8279199025c3b3da4b13ec24d20200340f"
        }
      ],
      "nodes": [
        {
          "entity_attributes": {
            "has_detections": true
          },
          "entity_id": "e743cffce9efddfb4f1d7e7dc3c10c6d562e61b5f65e6dd3fd4f28b604fcc2f6",
          "index": 0,
          "text": "",
          "type": "url",
          "x": 0,
          "y": 0
        },
        {
          "entity_attributes": {},
          "entity_id": "relationships_last_serving_ip_address_e743cffce9efddfb4f1d7e7dc3c10c6d562e61b5f65e6dd3fd4f28b604fcc2f6",
          "index": 1,
          "text": "",
          "type": "relationship",
          "x": -27.425258029385414,
          "y": -19.198748008541706
        },
        {
          "entity_attributes": {
            "country": "OM",
            "has_detections": true
          },
          "entity_id": "138.133.35.39",
          "fx": -60.42155469411466,
          "fy": -1.7339803589372877,
          "index": 2,
          "text": "",
          "type": "ip_address",
          "x": -60.42155469411466,
          "y": -1.7339803589372877
        },
        {
          "entity_attributes": {
            "has_detections": false,
            "type_tag": "text"
          },
          "entity_id": "733314c4b079b42174c6b55fb89755faca798378ab999ea240b3f14b0d24a90f",
          "index": 6,
          "text": "",
          "type": "file",
          "x": 27.265746471390678,
          "y": -9.726931961146573
        },
        {
          "entity_attributes": {
            "has_detections": false
          },
          "entity_id": "www.blablabla.com",
          "index": 88,
          "text": "",
          "type": "domain",
          "x": -234.75082645175817,
          "y": 8.15972244734705
        },
        {
          "entity_attributes": {
            "intelligence_query": "entity: url path: blablabla",
            "relationship_type": "intelligence"
          },
          "entity_id": "intelligence_-1173580683",
          "index": 154,
          "text": "VTI: entity: url path: blablabla",
          "type": "relationship",
          "x": -27.95565446983731,
          "y": -64.23455937679253
        },,
        {
          "entity_attributes": {
            "commonalities": [
              {
                "commonality": "path",
                "value": "/"
              }
            ],
            "relationship_type": "commonality"
          },
          "entity_id": "relationships_commonality_106438826",
          "fx": -107.49097518267031,
          "fy": 198.2339878510857,
          "index": 160,
          "text": "path: /",
          "type": "relationship",
          "x": -107.49097518267031,
          "y": 198.2339878510857
        },
        {
          "entity_attributes": {
            "relationship_type": "hunting",
            "ruleset_id": "6533973538739388"
          },
          "entity_id": "relationships_hunting_6533973538739388",
          "index": 161,
          "text": "",
          "type": "relationship",
          "x": -130.72553403592232,
          "y": 346.7297024640031
        }
      ],
      "private": true
    },
    "type": "graph"
  }
}
```

```json Response example
{
    "data": {
        "id": "g0538d03053194c338643183e315b134ec3463a392330430938033934f3be3f37",
        "type": "graph"
    }
}
```

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
      "post": {
        "tags": [
          "Threat Graphs"
        ],
        "deprecated": false,
        "description": "",
        "operationId": "create-graphs",
        "parameters": [
          {
            "description": "Your API key",
            "in": "header",
            "name": "x-apikey",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "properties": {
                  "RAW_BODY": {
                    "format": "json",
                    "type": "string"
                  }
                },
                "type": "object"
              }
            }
          }
        },
        "security": [],
        "summary": "Create a graph"
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

← [Search graphs](graphs.md) · [up](../README.md) · [Delete a graph](graphs-delete.md) →

*Archived from <https://gtidocs.virustotal.com/reference/create-graphs>.*
