---
title: "Index"
source: https://gtidocs.virustotal.com/reference/get_collections-collection-uuid-collection-runs
slug: get_collections-collection-uuid-collection-runs
section: reference
group: "ASM (ATTACK SURFACE MANAGEMENT)"
updatedAt: 2025-09-25T02:06:18.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [ASM (ATTACK SURFACE MANAGEMENT)](../README.md) › [Collection Runs](../collection-runs.md) › Index

---

# index

Returns up to last 10 collection scans

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
      "name": "Collection Runs"
    }
  ],
  "paths": {
    "/collections/{collection_uuid}/collection_runs": {
      "get": {
        "tags": [
          "Collection Runs"
        ],
        "summary": "Index",
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
            "name": "collection_uuid",
            "in": "path",
            "schema": {
              "type": "string"
            },
            "required": true,
            "description": "Required: uuid from /api/v3/asm/user_collections"
          }
        ],
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object"
                },
                "example": {
                  "success": true,
                  "message": "Collection runs retrieved!",
                  "result": [
                    {
                      "id": 660929,
                      "uuid": "578b4a28-bd7e-4436-a661-91b52e757ce3",
                      "status": "finished",
                      "priority": 400,
                      "duration": 2126,
                      "entity_count": 18,
                      "created_at": "2022-09-09T00:02:30.357Z",
                      "started_at": "2022-09-09T05:20:55.000Z",
                      "finished_at": "2022-09-09T05:56:21.000Z",
                      "collection_name": "Attacksurface_APP_QA",
                      "collection_type": "user_collection",
                      "collection_uuid": "c1b502fe-1020-4a85-a620-e02614526ee9",
                      "created_by_uuid": "8c92ef9b-c4c5-4ea2-8340-93e5ed53b9ea",
                      "created_by_email": "jcran@intrigue.io",
                      "project_name": "ASMQA_AttackSurfaceAPP",
                      "project_uuid": "be884e25-a0bb-4836-a836-df5eab176186",
                      "engine": "engine-group-57-control-0"
                    },
                    {
                      "id": 660517,
                      "uuid": "ac553570-58d9-420d-9ded-abc6944d7446",
                      "status": "finished",
                      "priority": 510,
                      "duration": 639,
                      "entity_count": 14,
                      "created_at": "2022-09-08T20:42:03.179Z",
                      "started_at": "2022-09-08T20:42:22.000Z",
                      "finished_at": "2022-09-08T20:53:01.000Z",
                      "collection_name": "Attacksurface_APP_QA",
                      "collection_type": "user_collection",
                      "collection_uuid": "c1b502fe-1020-4a85-a620-e02614526ee9",
                      "created_by_uuid": "c1ac6a07-fda8-4568-90c3-ea2ba6ec2535",
                      "created_by_email": "dallas@attacksurface.app",
                      "project_name": "ASMQA_AttackSurfaceAPP",
                      "project_uuid": "be884e25-a0bb-4836-a836-df5eab176186",
                      "engine": "engine-group-7-control-0"
                    },
                    {
                      "id": 660427,
                      "uuid": "db989601-bc40-46f9-99f2-aef3eda4204f",
                      "status": "finished",
                      "priority": 400,
                      "duration": 2036,
                      "entity_count": 20,
                      "created_at": "2022-09-08T00:02:38.112Z",
                      "started_at": "2022-09-08T12:20:42.000Z",
                      "finished_at": "2022-09-08T12:54:38.000Z",
                      "collection_name": "Attacksurface_APP_QA",
                      "collection_type": "user_collection",
                      "collection_uuid": "c1b502fe-1020-4a85-a620-e02614526ee9",
                      "created_by_uuid": "8c92ef9b-c4c5-4ea2-8340-93e5ed53b9ea",
                      "created_by_email": "jcran@intrigue.io",
                      "project_name": "ASMQA_AttackSurfaceAPP",
                      "project_uuid": "be884e25-a0bb-4836-a836-df5eab176186",
                      "engine": "engine-group-77-control-0"
                    },
                    {
                      "id": 659932,
                      "uuid": "b0ea8329-59c4-4209-8363-8fcd92bfb4cf",
                      "status": "finished",
                      "priority": 400,
                      "duration": 2265,
                      "entity_count": 20,
                      "created_at": "2022-09-07T00:02:31.016Z",
                      "started_at": "2022-09-07T07:13:48.000Z",
                      "finished_at": "2022-09-07T07:51:33.000Z",
                      "collection_name": "Attacksurface_APP_QA",
                      "collection_type": "user_collection",
                      "collection_uuid": "c1b502fe-1020-4a85-a620-e02614526ee9",
                      "created_by_uuid": "8c92ef9b-c4c5-4ea2-8340-93e5ed53b9ea",
                      "created_by_email": "jcran@intrigue.io",
                      "project_name": "ASMQA_AttackSurfaceAPP",
                      "project_uuid": "be884e25-a0bb-4836-a836-df5eab176186",
                      "engine": "engine-group-58-control-0"
                    },
                    {
                      "id": 659418,
                      "uuid": "07b23ebf-406d-43ef-adfc-a1c2242089ec",
                      "status": "finished",
                      "priority": 400,
                      "duration": 2490,
                      "entity_count": 23,
                      "created_at": "2022-09-06T00:02:29.329Z",
                      "started_at": "2022-09-06T05:46:09.000Z",
                      "finished_at": "2022-09-06T06:27:39.000Z",
                      "collection_name": "Attacksurface_APP_QA",
                      "collection_type": "user_collection",
                      "collection_uuid": "c1b502fe-1020-4a85-a620-e02614526ee9",
                      "created_by_uuid": "8c92ef9b-c4c5-4ea2-8340-93e5ed53b9ea",
                      "created_by_email": "jcran@intrigue.io",
                      "project_name": "ASMQA_AttackSurfaceAPP",
                      "project_uuid": "be884e25-a0bb-4836-a836-df5eab176186",
                      "engine": "engine-group-9-control-0"
                    },
                    {
                      "id": 658941,
                      "uuid": "5fef2ec6-cd2a-41eb-9fbb-f7513a1da95a",
                      "status": "finished",
                      "priority": 400,
                      "duration": 2730,
                      "entity_count": 23,
                      "created_at": "2022-09-05T00:02:07.105Z",
                      "started_at": "2022-09-05T07:57:22.000Z",
                      "finished_at": "2022-09-05T08:42:52.000Z",
                      "collection_name": "Attacksurface_APP_QA",
                      "collection_type": "user_collection",
                      "collection_uuid": "c1b502fe-1020-4a85-a620-e02614526ee9",
                      "created_by_uuid": "8c92ef9b-c4c5-4ea2-8340-93e5ed53b9ea",
                      "created_by_email": "jcran@intrigue.io",
                      "project_name": "ASMQA_AttackSurfaceAPP",
                      "project_uuid": "be884e25-a0bb-4836-a836-df5eab176186",
                      "engine": "engine-group-92-control-0"
                    },
                    {
                      "id": 658518,
                      "uuid": "a0d99fd6-ddcf-4814-8db0-6cb2fa24e4a0",
                      "status": "finished",
                      "priority": 400,
                      "duration": 268,
                      "entity_count": 23,
                      "created_at": "2022-09-04T00:02:42.206Z",
                      "started_at": "2022-09-04T09:40:39.000Z",
                      "finished_at": "2022-09-04T09:45:07.000Z",
                      "collection_name": "Attacksurface_APP_QA",
                      "collection_type": "user_collection",
                      "collection_uuid": "c1b502fe-1020-4a85-a620-e02614526ee9",
                      "created_by_uuid": "8c92ef9b-c4c5-4ea2-8340-93e5ed53b9ea",
                      "created_by_email": "jcran@intrigue.io",
                      "project_name": "ASMQA_AttackSurfaceAPP",
                      "project_uuid": "be884e25-a0bb-4836-a836-df5eab176186",
                      "engine": "engine-group-41-control-0"
                    },
                    {
                      "id": 658094,
                      "uuid": "75a96480-d61a-467f-8d61-db0c1e9ca633",
                      "status": "finished",
                      "priority": 400,
                      "duration": 2356,
                      "entity_count": 23,
                      "created_at": "2022-09-03T00:02:18.279Z",
                      "started_at": "2022-09-03T14:11:25.000Z",
                      "finished_at": "2022-09-03T14:50:41.000Z",
                      "collection_name": "Attacksurface_APP_QA",
                      "collection_type": "user_collection",
                      "collection_uuid": "c1b502fe-1020-4a85-a620-e02614526ee9",
                      "created_by_uuid": "8c92ef9b-c4c5-4ea2-8340-93e5ed53b9ea",
                      "created_by_email": "jcran@intrigue.io",
                      "project_name": "ASMQA_AttackSurfaceAPP",
                      "project_uuid": "be884e25-a0bb-4836-a836-df5eab176186",
                      "engine": "engine-group-86-control-0"
                    },
                    {
                      "id": 657633,
                      "uuid": "83f9a245-683c-4508-b0bd-7d8aa10fa3e9",
                      "status": "finished",
                      "priority": 400,
                      "duration": 1325,
                      "entity_count": 22,
                      "created_at": "2022-09-02T00:02:23.698Z",
                      "started_at": "2022-09-02T09:18:08.000Z",
                      "finished_at": "2022-09-02T09:40:13.000Z",
                      "collection_name": "Attacksurface_APP_QA",
                      "collection_type": "user_collection",
                      "collection_uuid": "c1b502fe-1020-4a85-a620-e02614526ee9",
                      "created_by_uuid": "8c92ef9b-c4c5-4ea2-8340-93e5ed53b9ea",
                      "created_by_email": "jcran@intrigue.io",
                      "project_name": "ASMQA_AttackSurfaceAPP",
                      "project_uuid": "be884e25-a0bb-4836-a836-df5eab176186",
                      "engine": "engine-group-3-control-0"
                    },
                    {
                      "id": 657174,
                      "uuid": "78d9926f-dfaa-4698-8f67-3affea5acfde",
                      "status": "finished",
                      "priority": 400,
                      "duration": 1996,
                      "entity_count": 27,
                      "created_at": "2022-09-01T00:02:35.438Z",
                      "started_at": "2022-09-01T12:56:31.000Z",
                      "finished_at": "2022-09-01T13:29:47.000Z",
                      "collection_name": "Attacksurface_APP_QA",
                      "collection_type": "user_collection",
                      "collection_uuid": "c1b502fe-1020-4a85-a620-e02614526ee9",
                      "created_by_uuid": "8c92ef9b-c4c5-4ea2-8340-93e5ed53b9ea",
                      "created_by_email": "jcran@intrigue.io",
                      "project_name": "ASMQA_AttackSurfaceAPP",
                      "project_uuid": "be884e25-a0bb-4836-a836-df5eab176186",
                      "engine": "engine-group-88-control-0"
                    }
                  ]
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

← [Collection Runs](../collection-runs.md) · [up](../README.md) · [Create](post_collections-collection-uuid-collection-runs.md) →

*Archived from <https://gtidocs.virustotal.com/reference/get_collections-collection-uuid-collection-runs>.*
