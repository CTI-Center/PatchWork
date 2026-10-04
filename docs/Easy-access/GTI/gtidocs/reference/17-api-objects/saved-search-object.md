---
title: "Saved Searches"
source: https://gtidocs.virustotal.com/reference/saved-search-object
slug: saved-search-object
section: reference
group: "API OBJECTS"
updatedAt: 2025-12-03T07:24:38.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Saved Searches

---

# saved-searches

Saved Searches are designed to store complex or frequently executed threat intelligence searches for reuse against our database of Indicators of Compromise (IoCs).

## object-attributes

A saved search object contains the following attributes:

* `creation_date`: <*int:timestamp*> saved search object creation date (UTC timestamp).
* `last_modification_date`: <*int:timestamp*> last time when the saved search's information was updated (UTC timestamp).
* `last_execution_date`: <*int:timestamp*> last time the saved search was run (UTC timestamp or 0).
* `name`: <*string*> saved search's name.
* `description`: <*string*> saved search's description.
* `search_query`: <*string*> saved search's query/logic.
* `private`: <*boolean*> whether the saved search is private or not.
* `origin`: <*string*> saved search's origin. Available options are: Crowdsourced, Google Threat Intelligence, Partner.
* `tags`: <*list of strings*> saved search's associated tags.

The `context_attributes` define the specific relationship between the user who requested the object and the object itself.

```json Saved Search object
{
    "attributes": {
        "creation_date": <_int:timestamp_>,
        "description": "<_string_>",
        "last_execution_date": \<_int:timestamp_>,
        "last_modification_date": \<_int:timestamp_>,
        "name": "<_string_>",
        "origin": "<_string_>",
        "private": <_boolean_>,
        "search_query": "<_string_>",
        "tags": <_list of strings_>
    },
    "context_attributes": {
        "role": "<_string_>",
        "shared_with_me": <_boolean_>
    },
    "id": "<_string_>",
    "links": {
        "self": "https://www.virustotal.com/api/v3/saved_searches/<_string_>"
    },
    "type": "saved_search"
}
```

# relationships

In addition to the previously described attributes, Saved Searches objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../01-api-introduction/api-responses/introduction-relationships.md) section.

The following table shows a summary of available relationships.

| Relationship | Return object type                                                                                               | Allowed Methods |
| ------------ | ---------------------------------------------------------------------------------------------------------------- | --------------- |
| owner        | [User](user-object.md) who created the object.                                                                  | GET             |
| editors      | List of [users](user-object.md) that can edit the object (only available to the owner or editor of the object). | GET, POST       |
| viewers      | List of [users](user-object.md) that can view the object (only available to the owner or editor of the object). | GET, POST       |

---

← [Resolutions](resolution-object.md) · [up](README.md) · [Screenshots](screenshots-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/saved-search-object>.*
