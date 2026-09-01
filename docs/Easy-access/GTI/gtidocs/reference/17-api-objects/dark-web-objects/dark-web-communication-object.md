---
title: "Dark Web Communication"
source: https://gtidocs.virustotal.com/reference/dark-web-communication-object
slug: dark-web-communication-object
section: reference
group: "API OBJECTS"
updatedAt: 2026-02-27T12:41:07.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [API Reference](../../README.md) › [API OBJECTS](../README.md) › [Dark Web](../dark-web-objects.md) › Dark Web Communication

---

# dark-web-communication

A Dark Web Communication object is the smallest communication unit ingested in our dark web dataset, whose `type` is set to `ddw_communication`.

# object-attributes

Dark Web Communication objects contains the following attributes:

* `subject`: <*string*> the primary title of the Dark Web communication object. This may include the title of a forum or blog post, the name of a repository or paste, or the display name of a Telegram channel.
* `origin_url`: \<string> the URL pointing to the specific communication entity from which the content was retrieved.
* `communication_type`:  <*string*> the type of the communication object. Available values are: `forum_post`, `web_content`, `paste` and `messenger_message` for messages on Telegram channels.
* `timestamp`: \<integer> the time of communication publication when possible, otherwise time of collection. (UTC timestamp).
* `update_timestamp`: \<integer> timestamp of the latest update, as indicated by the source content.(UTC timestamp).
* `original_id`: <*string*> the unique identifier of the communication entity on its original platform.
* `content`: <*string*> the original content of the communication entity from its source.
* `content_translated`: <*string*> the English translation of the communication content.

# relationships

In addition to the previously described attributes, communication objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](../../01-api-introduction/api-responses/introduction-relationships.md) section.

The following table shows a summary of available relationships.

| Relationship           | Return object type                                                                             |
| :--------------------- | :--------------------------------------------------------------------------------------------- |
| author                 | The [Dark Web User Profile](dark-web-user-profile-object.md) of the communication's author.   |
| communication\_channel | The [Dark Web Communication Channel](dark-web-communication-channel-object.md) it belongs to. |
| conversation\_thread   | The [Dark Web Conversation Thread](dark-web-conversation-thread-object.md) it belongs to.     |
| service                | The [Dark Web Service](dark-web-service-object.md) it belongs to.                             |

<br />

---

← [Dark Web](../dark-web-objects.md) · [up](../README.md) · [Dark Web Communication Channel](dark-web-communication-channel-object.md) →

*Archived from <https://gtidocs.virustotal.com/reference/dark-web-communication-object>.*
