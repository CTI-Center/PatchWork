---
title: "Graphs"
source: https://gtidocs.virustotal.com/reference/graph-object
slug: graph-object
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:43:12.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Graphs

---

# graphs

Information about graphs.

A Graph object represents a graph in [Google Threat Intelligence Graph](https://www.virustotal.com/graph/).

## object-attributes

* `comments_count`: <*integer*> number of comments.
* `creation_date`: <*integer*> when the graph was created.
* `graph_data`: <*dictionary*> it contains the following subfields:
  * `description`: <*string*> contains the graph name.
  * `version`: <*string*> is the graph version.
* `last_modified_date`: <*integer*> last time the graph was modified.
* `links`: <*list of dictionaries*> list of different relations with the network location.
  * `connection_type`: <*string*> type of connection ("network\_location", "urls", "referrer\_files", "contacted\_urls", etc.)
  * `source`: <*string*> source object ID.
  * `target`: <*string*> target object ID.
* `nodes`: <*list of dictionaries*> list of different nodes of the graph.
  * `entity_attributes`: <*dictionary*> contains entity specific attributes. Fields on each element may vary depending on the nature of the node.
    * `has_detections`: <*boolean*> whether the entity is marked as malicious or not.
    * `type_tag`: <*string*> file type tag. Only returned in file nodes.
    * `country`: <*string*> IP country. Only returned in IP nodes.
    * `relationship_type`: <*string*> describes how the relationship was built. Can be either "intelligence", "hunting", "retrohunt" or "commonality". Only returned in relationship nodes.
    * `intelligence_query`: <*string*> in case the relationship type is "intelligence", contains the VT Intelligence query used to create the relationship. Only returned in relationship nodes.
    * `ruleset_id`: <*string*> in case the relationship type is "hunting", contains the ruleset ID where the relationship was extracted. Only returned in relationship nodes.
    * `retrohunt_job_id`: <*string*> in case the relationship type is "retrohunt", contains the Retrohunt job where the relationship was extrascted. Only returned in relationship nodes.
    * `commonalities`: <*list of dictionaries*> in case the relationship type is "commonality", it contains the commonalities used to extract the relationship. Only returned in relationship nodes. Every item on the list contains the following fields:
      * `commonality`: <*string*> commonality type.
      * `value`: <*string*> commonality value.
  * `entity_id`: <*string*> id of this specific element (i.e. a hash or '[www.whatever.com'](http://www.whatever.com')).
  * `fx`: <*float*> node's horizontal pinned position in the graph. The node's position doesn't change unless the user drags it.
  * `fy`: <*float*> node's vertical pinned position in the graph. The node's position doesn't change unless the user drags it.
  * `index`: <*integer*> node's id in the graph.
  * `type`: <*string*> node type (i.e. "url", "relationship", "file", "domain")
  * `x`: <*float*> relative horizontal location of the node.
  * `y`: <*float*> relative vertical location of the node.
* `private`: <*boolean*> whether the graph is private or not.
* `views_count`: <*integer*> number of times the graph has been viewed.

```json "graph" object
{
  "data": {
    "attributes": {
      "comments_count": <int>,
      "creation_date": <int:timestamp>,
      "graph_data": {
        "description": "<string>",
        "version": "<string>"
      },
      "last_modified_date": <int:timestamp>,
      "links": [
        {
          "connection_type": "<string>",
          "source": "<string>",
          "target": "<string>"
        }
      ],
      "nodes": [
        {
          "entity_attributes": {
            "commonalities": [
              {
                "commonality": "<string>",
                "value": "<string>"
              }
            ],
            "country": "<string>",
            "has_detections": <boolean>,
            "intelligence_query": "<string>",
            "relationship_type": "<string>",
            "retrohunt_job_id": "<string>",
            "ruleset_id": "<string>",
            "type_tag": "<string>"
          },
          "entity_id": "<string>",
          "fx": <float>,
          "fy": <float>
          "index": <int>,
          "text": "<string>",
          "type": "<string>",
          "x": <float>,
          "y": <float>
        }
      ],
      "private": <boolean>,
      "views_count": <int>
    },
    "id": "<string>",
    "links": {
      "self": "https://www.virustotal.com/api/v3/graphs/<id>"
    },
    "type": "graph"
  }
}
```
```json Example
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
      "private": true,
      "views_count": 2
    },
    "id": "g0538d03053194c338643183e315b134ec3463a392330430938033934f3be3f37",
    "links": {
      "self": "https://www.virustotal.com/api/v3/graphs/g0538d03053194c338643183e315b134ec3463a392330430938033934f3be3f37"
    },
    "type": "graph"
  }
}
```

## relationships

In addition to the previously described attributes, Graph objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../01-api-introduction/api-responses/introduction-relationships.md) section.

The following table shows a summary of available relationships for graph objects.

| Relationship | Description                                                                    | Accessibility | Return object type                                                                                                           |
| :----------- | :----------------------------------------------------------------------------- | :------------ | :--------------------------------------------------------------------------------------------------------------------------- |
| comments     | Comments for the graph.                                                        | Viewers.      | A list of [Comments](comment-object.md).                                                                                    |
| editors      | Graph's editors.                                                               | Viewers.      | A list of [Users](user-object.md) and [Groups](group-object.md).                                                           |
| group        | Group owning the graph.                                                        | Viewers.      | A single [Group](group-object.md) object.                                                                                   |
| items        | Items related to the graph. They can be: files, urls, domains or IP addresses. | Viewers.      | A list of [Files](file-object.md), [IP addresses](ip-object.md), [URLs](url-object.md) and [Domains](domains-object.md). |
| owner        | Graph's owner.                                                                 | Viewers.      | A single [User](user-object.md) object.                                                                                     |
| viewers      | Graph's viewers.                                                               | Viewers.      | A list of [Users](user-object.md) and [Groups](group-object.md).                                                           |

These relationships are detailed in the subsections below.

---

← [Flow Execution](flow-execution-object.md) · [up](README.md) · [🔀 comments](graph-object/graph-comments.md) →

*Archived from <https://gtidocs.virustotal.com/reference/graph-object>.*
