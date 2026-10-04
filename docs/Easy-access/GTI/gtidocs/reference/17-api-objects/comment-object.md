---
title: "Comments"
source: https://gtidocs.virustotal.com/reference/comment-object
slug: comment-object
section: reference
group: "API OBJECTS"
updatedAt: 2025-09-25T00:40:20.000Z
retrieved: 2026-09-01
---

[gtidocs](../../README.md) › [API Reference](../README.md) › [API OBJECTS](README.md) › Comments

---

# comments

comment object

Comments

## object-attributes

* `attributes`: data about a specific comment.
  * `date`:  <*integer*> when the comment was done.
  * `text`:  <*string*> comment in text.
  * `html`:  <*string*> comment in html format.
  * `votes`: <*dictionary*> unweighted number of total votes from the community, divided in "harmless" and "malicious".
    * `positive`: <*integer*> number of positive votes.
    * `negative`: <*integer*> number of negative votes.
    * `abuse`: <*integer*> number of negative votes.
  * `tags`: <*list of strings*> identificative attributes.
* `id`:  <*string*> resource identifier of the comment.
* `links`: contains "self", with a link to the comment itself.
* `type`:  <*string*> value is "comment", that is the object type.

```json "vote" object
{
  "attributes": {"date": <int:timestamp>,
                 "text": <string>,
                 "html": "<string>",
                 "votes": {
                    "positive": <int>,
                    "negative": <int>,
                    "abuse": <int>
                 },
                 "tags": ["<string>"],
                 },
  "id": "<string>",
  "links": {"self": "<string>"},
  "type": "vote"
}
```

## relationships

In addition to the previously described attributes, Comment objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../01-api-introduction/api-responses/introduction-relationships.md) section. The available relationships are described in the following table:

| Relationship | Description            | Accessibility | Return object type               |
| :----------- | :--------------------- | :------------ | :------------------------------- |
| author       | Author of the comment. | Everyone.     | Details of the comment's author. |

---

← [Campaign](campaign-object.md) · [up](README.md) · [🔀 author](comment-object/comment-object-author.md) →

*Archived from <https://gtidocs.virustotal.com/reference/comment-object>.*
