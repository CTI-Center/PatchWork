---
title: "Relationships"
source: https://gtidocs.virustotal.com/reference/introduction-relationships
slug: introduction-relationships
section: reference
group: "API Introduction"
updatedAt: 2025-09-25T00:33:29.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API Introduction](../README.md) › [API responses](../api-responses.md) › Relationships

---

# relationships

Relationships are the way in which the Google Threat Intelligence API expresses links or dependencies between objects. An object can be related to objects of the same or a different type. For example, a file object can be related to some other file object that contains the first one, or a file object can be related to URL objects representing the URLs embedded in the file.

Relationships can be one-to-one or one-to-many, depending of whether the object is related a single object or to multiple objects.

When retrieving a particular object with a `GET` request you may want to retrieve its relationships with other objects too. This can be done by specifying the relationship you want to retrieve in the `relationships` parameter.

```
https://www.virustotal.com/api/v3/{collection name}/{object id}?relationships={relationship}
```

More than one relationship can be included in the response by specifying a comma-separated list of relationship names.

```
https://www.virustotal.com/api/v3/{collection name}/{object id}?relationships={relationship 1},{relationship 2}
```

The objects returned by such requests include the `relationships` dictionary, where keys are the names of the requested relationships, and values are either an object descriptor (if the relationship is one-to-one) or a collection as described in the [Collections](../../17-api-objects/ioc-collection-object.md) section (if the relationship is one-to-many). Notice however that these collections don't contain the whole related objects but only their descriptors (i.e: their type and ID).

```json Relationships in an object
{
  "type": "{object type}",
  "id": "{object id}",
  "links": {
    "self": "https://www.virustotal.com/api/v3/{collection name}/{object id}"
  },
  "attributes" : {
     ..
  },
  "relationships" : {
     "{one-to-one relationship}": {
       "data": {
         "id": "www.google.com",
         "type": "domain"
       },
       "links": {
         "related": "https://www.virustotal.com/api/v3/{collection name}/{object id}/{one-to-one relationship}",
         "self": "https://www.virustotal.com/api/v3/{collection name}/{object id}/relationships/{one-to-one relationship}"
       }
     },
     "{one-to-many relationship}": {
       "data": [
         { .. object descriptor 1 .. },
         { .. object descriptor 2 .. },
         { .. object descriptor 3 .. }
       ],
       "meta": {
         "cursor": "CuABChEKBGRhdGUSCQjA1LC...",
       },
       "links": {
         "next": "https://www.virustotal.com/api/v3/{collection name}/{object id}/relationships/{one-to-many relationship}?cursor=CuABChEKBGRhdGUSCQjA1LC...",
         "self": "https://www.virustotal.com/api/v3/{collection name}/{object id}/relationships/{one-to-many relationship}"
       },
     },
    "{relationship 2}": { ... },
    "{relationship 3}": { ... }
  }
}
```

If you take a closer look to the `links` field for the relationship in the example above, you'll see that the `self` URL looks like:

```
https://www.virustotal.com/api/v3/{collection name}/{object id}/relationships/{relationship}
```

One-to-many relationships are simply collections that contains objects that are somehow related to a primary object, so they usually have their own URL that you can use to iterate over the related objects by sending `GET` requests to the URL as described in the [Collections](introduction-collections.md) section. Actually, there are two types of URLs:

```
https://www.virustotal.com/api/v3/{collection name}/{object id}/relationships/{relationship}
https://www.virustotal.com/api/v3/{collection name}/{object id}/{relationship}
```

The first one is a collection that contains only the descriptors (type and ID) for the related objects, the second one contains the complete objects, with all their attributes. If you are interested only in the type and ID of the related objects you should use the first one, as it's more efficient to retrieve only the descriptors than the complete objects.

Another important difference between both endpoints is that `{object id}/relationships/{relationship}` represents the relationship, as an independent entity, and can support operations that change the relationship without altering the objects. On the other hand, `{object id}/{relationship}` is representing the related objects, not the relationship. For example, if you want to grant a user viewing permissions to a Graph, you use:

```
POST https://www.virustotal.com/api/v3/graphs/{id}/relationships/viewers
```

This endpoint receives a user descriptor, it doesn't modify the user nor the graph, it simply creates a relationship between them. On the other hand, when you create a new comment for a file you use:

```
POST https://www.virustotal.com/api/v3/files/{id}/comments
```

Because in this case you are not only modifying the relationship between a file and a comment, you are also creating a new comment object.

## relationships-with-objects-not-present-in-google-threat-intelligence's-database

For a variety of reasons, an object might be related to another object not present in our database. In those cases, the returned relationship will just contain the element ID and a "NotFoundError" error code.

```json NotFoundError in relationships
{
  "data": [
    {
      "error": {
        "code": "NotFoundError",
        "message": "{item type} with id \"{item id}\" not found"
      },
      "id": "{item id}",
      "type": "{item type}"
    },
    { .. object 2 .. },
    ...
  ],
  "links": {
    "self": "https://www.virustotal.com/api/v3/{collection name}/{object id}/{one-to-many relationship}"
  }
}
```

When only object descriptors are requested (that is, requesting `/api/v3/{collection name}/{object id}/**relationships**/{relationship name}` instead of \`/api/v3/\{collection name}/\{object id}/\{relationship name}) this error is not returned.

---

← [Errors](introduction-errors.md) · [up](../README.md) · [Collections](introduction-collections.md) →

*Archived from <https://gtidocs.virustotal.com/reference/introduction-relationships>.*
