---
title: "Objects"
source: https://gtidocs.virustotal.com/reference/introduction-objects
slug: introduction-objects
section: reference
group: "API Introduction"
updatedAt: 2025-09-25T00:33:27.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API Introduction](../README.md) › [API responses](../api-responses.md) › Objects

---

# objects

Objects are a key concept in the Google Theat Intelligence API. Each object has an identifier and a type. Identifiers are unique among objects of the same type, which means that a (type, identifier) pair uniquely identifies any object across the API. In this documentation, those (type, identifier) pairs are referred as **object descriptors**.

Each object has an associated URL with the following structure:

```
https://www.virustotal.com/api/v3/{collection name}/{object id}
```

Usually `{collection name}` is the plural form of the object type, for example, `files` is the collection containing all the objects of type `file`, and `analyses` is the collection containing all the `analysis` objects. The format for `{object id}` varies from one object type to another.

A `GET` request to the object's URL returns information about the object in the following format:

```json Example response
{
  "data": {
    "type": "{object type}",
    "id": "{object id}",
    "links": {
      "self": "https://www.virustotal.com/api/v3/{collection name}/{object id}"
    },
    "attributes" : {
      "integer_attribute": 1234,
      "string_attribute": "this is a string",
      "dictionary_attribute": { "one": 1, "two": 2 },
      "list_attribute": [ "foo", "bar", "baz" ]
    },
    "relationships" : {
       ..
    }
  } 
}
```

Besides an ID and a type, the object has a set of **attributes** and **relationships**. Attributes can be of any type supported by JSON, including lists and dictionaries. The `attributes` field is always present in all objects, but `relationships` is optional, depending on whether or not you asked for relationships to be included while making your request. This will discussed in depth in the [Relationships](introduction-relationships.md) section.

Each object type has its own pre-defined set of attributes, you won't be able to add nor remove attributes, you can only modify existing ones (as long as they are writable). To modify an object's attributes you must send a `PATCH` request to the object's URL. If you try to modify a read-only attribute you will get an error. The `PATCH` request's body must contain the attributes you want to modify in a structure like the one shown in the example below. Any attribute not included in the request will remain unchanged.

```json Example PATCH request
{
  "data": {
    "type": "{object type}",
    "id": "{object id}",
    "attributes" : {
      "integer_attribute": 1234,
      "string_attribute": "this is a new string",
    }
  } 
}
```

Notice that both the object's ID and type are included in the `PATCH` request's body, and they must match those specified in the URL.

Some object types can be also deleted by sending a `DELETE` request to the object's URL.

---

← [Key concepts](introduction-key-concepts.md) · [up](../README.md) · [Errors](introduction-errors.md) →

*Archived from <https://gtidocs.virustotal.com/reference/introduction-objects>.*
