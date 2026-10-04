---
title: "Collections"
source: https://gtidocs.virustotal.com/reference/introduction-collections
slug: introduction-collections
section: reference
group: "API Introduction"
updatedAt: 2025-09-25T00:33:30.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API Introduction](../README.md) › [API responses](../api-responses.md) › Collections

---

# collections

Collections are sets of objects. For most object types there is a top-level collection representing all objects of that type. Those collections can be accessed by using a URL like:

```
https://www.virustotal.com/api/v3/{collection_name}
```

Many operations in the Google Threat Intelligence API are performed by sending requests to a collection. For example, you can analyse a file by sending a `POST` request to `/api/v3/files`, which effectively adds a new item to the `files` collection. You can create a new Hunting ruleset by sending a `POST` request to `/api/v3/intelligence/hunting_rulesets`. Sending a `POST` request to a collection is usually the way in which new objects are created.

Similarly, a `DELETE` request sent to a collection has the effect of deleting all objects in that collection. As you may imagine, there's no `DELETE` method for certain collections like `files`, `urls` or `analyses`, but you can use `DELETE` on other collection types such as `hunting_notifications` to remove all your Hunting notifications.

Many collections are also iterable, you can retrieve all objects in the collection by sending successive `GET` requests to the collection. On each request you get a number of objects and a cursor that is used to continue the iteration. The snippet below exemplifies the response from a `GET` request to `/api/v3/{collection name}`.

```json Example collection response
{
    "data": [
      { .. object 1 .. },
      { .. object 2 .. },
      { .. object 3 .. }
    ],
    "meta": {
      "cursor": "CuABChEKBGRhdGUSCQjA1.."
    },
    "links": {
        "next": "https://www.virustotal.com/api/v3/{collection name}?cursor=CuABChEKBGRhdGUSCQjA1..",
        "self": "https://www.virustotal.com/api/v3/{collection name}"
    }
}
```

As the `next` field in the `links` section suggest, you can use the `cursor` in the response's metadata as a parameter in a subsequent call for retrieving the next set of objects. You can also use the `limit` parameter for controlling how many objects are returned on each call.

---

← [Relationships](introduction-relationships.md) · [up](../README.md) · [OpenAPI Specifications](../openapi-specs.md) →

*Archived from <https://gtidocs.virustotal.com/reference/introduction-collections>.*
